# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import filecmp
import json
import pytest
import oci
import oci_cli
import os
import random
import shutil
import string
import time
from . import util


OBJECTS_TO_CREATE_IN_BUCKET_FOR_BULK_GET = 100
OBJECTS_TO_CREATE_IN_FOLDER_FOR_BULK_PUT = 20
CONTENT_STRING_LENGTH = 5000
MID_SIZED_FILE_IN_MEBIBTYES = 20
LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES = 150  # Default multipart is 128MiB


# Holds the objects we create and their content so that we can verify results
bulk_get_object_to_content = {}
bulk_get_prefix_to_object = {
    'a/b/c/d': [],
    'a/b/c': [],
    'a/b': [],
    '/a': [],
    '': []
}
bulk_get_bucket_name = None

bulk_put_large_files = set()
bulk_put_mid_sized_files = set()
root_bulk_put_folder = None
bulk_put_bucket_name = None


# Generate test data for different operations:
#
#    Bulk Get: create a new bucket and populate it with some objects, then tear it all down afterwards
#    Bulk Put: create a folder structure containing small and large files, then tear it all down afterwards
#    Bulk Delete: uses the folders and files generated for bulk put
@pytest.fixture(scope='module', autouse=True)
def generate_test_data(object_storage_client):
    global bulk_get_object_to_content, bulk_get_bucket_name, root_bulk_put_folder, bulk_put_large_files, bulk_put_mid_sized_files, bulk_put_bucket_name

    # Create a test bucket
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkGetTest_{}'.format(int(time.time()))
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    object_storage_client.create_bucket(util.NAMESPACE, create_bucket_request)

    bulk_get_bucket_name = create_bucket_request.name

    # Create items at various heirarchy levels (to be surfaced as different directories on disk)
    for i in range(OBJECTS_TO_CREATE_IN_BUCKET_FOR_BULK_GET):
        if i % 5 == 4:
            object_name = 'a/b/c/d/Object_{}'.format(i)
            bulk_get_prefix_to_object['a/b/c/d'].append(object_name)
        elif i % 5 == 3:
            object_name = 'a/b/c/Object_{}'.format(i)
            bulk_get_prefix_to_object['a/b/c'].append(object_name)
        elif i % 5 == 2:
            object_name = 'a/b/Object_{}'.format(i)
            bulk_get_prefix_to_object['a/b'].append(object_name)
        elif i % 5 == 1:
            # This is equivalent to a/ on the file system because we drop the leading slash (we drop path separators from the front to avoid unexpected results)
            object_name = '/a/Object_{}'.format(i)
            bulk_get_prefix_to_object['/a'].append(object_name)
        else:
            # At the root of the bucket
            object_name = 'Object_{}'.format(i)
            bulk_get_prefix_to_object[''].append(object_name)

        object_content = generate_random_string(CONTENT_STRING_LENGTH)
        object_storage_client.put_object(util.NAMESPACE, create_bucket_request.name, object_name, object_content)
        bulk_get_object_to_content[object_name] = object_content

    # makedirs creates all subfolders recursively
    root_bulk_put_folder = 'tests/temp/bulk_put_{}'.format(int(time.time()))
    bulk_put_folder_leaf = '{}/subfolder1/subfolder2/subfolder3'.format(root_bulk_put_folder)
    os.makedirs(bulk_put_folder_leaf)

    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkPutTest_{}'.format(int(time.time()))
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    object_storage_client.create_bucket(util.NAMESPACE, create_bucket_request)

    bulk_put_bucket_name = create_bucket_request.name

    subfolders = ['', 'subfolder1', 'subfolder1/subfolder2', 'subfolder1/subfolder2/subfolder3']
    for subfolder in subfolders:
        if subfolder == '':
            full_folder = root_bulk_put_folder
        else:
            full_folder = os.path.join(root_bulk_put_folder, subfolder)

        for i in range(OBJECTS_TO_CREATE_IN_FOLDER_FOR_BULK_PUT + 1):
            file_path = '{}/object_{}'.format(full_folder, i)
            if i != 0 and i % OBJECTS_TO_CREATE_IN_FOLDER_FOR_BULK_PUT == 0:
                # Put in one big file per subfolder
                util.create_large_file(file_path, LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)
                bulk_put_large_files.add(file_path)
            elif i != 0 and i % 10 == 0:
                # Put in the occasional file with a reasonable size so that we can force multipart
                util.create_large_file(file_path, MID_SIZED_FILE_IN_MEBIBTYES)
                bulk_put_mid_sized_files.add(file_path)
            else:
                with open(file_path, 'w') as f:
                    f.write(generate_random_string(CONTENT_STRING_LENGTH))

    yield

    # Tear down stuff by deleting all the things and then deleting the buckets
    delete_bucket_and_all_items(object_storage_client, bulk_get_bucket_name)
    delete_bucket_and_all_items(object_storage_client, bulk_put_bucket_name)

    # Remove all directories recursively
    shutil.rmtree(root_bulk_put_folder)


def test_normalize_object_name_path():
    assert '/this/is/a/path' == oci_cli.object_storage_cli.normalize_object_name_path_for_object_storage('/this/is/a/path')
    assert '/this/is/a/path' == oci_cli.object_storage_cli.normalize_object_name_path_for_object_storage('/this/is/a/path', '/')
    assert '/this/is/a/path' == oci_cli.object_storage_cli.normalize_object_name_path_for_object_storage('\\this\\is\\a\\path', '\\')
    assert '/this/is/a/path' == oci_cli.object_storage_cli.normalize_object_name_path_for_object_storage('\\this/is/a\\path', '\\')

    assert 'thisisapath' == oci_cli.object_storage_cli.normalize_object_name_path_for_object_storage('thisisapath')
    assert 'thisisapath' == oci_cli.object_storage_cli.normalize_object_name_path_for_object_storage('thisisapath', '/')
    assert 'thisisapath' == oci_cli.object_storage_cli.normalize_object_name_path_for_object_storage('thisisapath', '\\')


def test_get_all_objects_in_bucket():
    download_folder = 'tests/temp/get_all_{}'.format(bulk_get_bucket_name)
    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--download-dir', download_folder])

    # Ensure that content matches
    for object_name in bulk_get_object_to_content:
        if object_name[0] == '/' or object_name[0] == '\\':
            file_path = os.path.join(download_folder, object_name[1:])
        else:
            file_path = os.path.join(download_folder, object_name)

        with open(file_path, 'r') as content_file:
            content = content_file.read()
            assert content == bulk_get_object_to_content[object_name]

    assert len(bulk_get_object_to_content) == get_count_of_files_in_folder_and_subfolders(download_folder)

    shutil.rmtree(download_folder)


def test_get_directory_and_subdirectories():
    download_folder = 'tests/temp/get_directory_and_subdirectories_{}'.format(bulk_get_bucket_name)

    # This should get us a/b/<object>, a/b/c/<object> and a/b/c/d/<object>
    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--download-dir', download_folder, '--prefix', 'a/b'])

    for object_name in bulk_get_prefix_to_object['a/b']:
        file_path = os.path.join(download_folder, object_name)
        with open(file_path, 'r') as content_file:
            content = content_file.read()
            assert content == bulk_get_object_to_content[object_name]

    for object_name in bulk_get_prefix_to_object['a/b/c']:
        file_path = os.path.join(download_folder, object_name)
        with open(file_path, 'r') as content_file:
            content = content_file.read()
            assert content == bulk_get_object_to_content[object_name]

    for object_name in bulk_get_prefix_to_object['a/b/c/d']:
        file_path = os.path.join(download_folder, object_name)
        with open(file_path, 'r') as content_file:
            content = content_file.read()
            assert content == bulk_get_object_to_content[object_name]

    assert len(bulk_get_prefix_to_object['a/b']) + len(bulk_get_prefix_to_object['a/b/c']) + len(bulk_get_prefix_to_object['a/b/c/d']) == get_count_of_files_in_folder_and_subfolders(download_folder)

    shutil.rmtree(download_folder)


def test_get_directory_no_subdirectory():
    download_folder = 'tests/temp/get_directory_only_{}'.format(bulk_get_bucket_name)
    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--download-dir', download_folder, '--prefix', 'a/b/c/', '--delimiter', '/'])

    for object_name in bulk_get_prefix_to_object['a/b/c']:
        file_path = os.path.join(download_folder, object_name)
        with open(file_path, 'r') as content_file:
            content = content_file.read()
            assert content == bulk_get_object_to_content[object_name]

    assert len(bulk_get_prefix_to_object['a/b/c']) == get_count_of_files_in_folder_and_subfolders(download_folder)

    shutil.rmtree(download_folder)


def test_get_files_skipped():
    download_folder = 'tests/temp/skip_and_replace_{}'.format(bulk_get_bucket_name)
    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--download-dir', download_folder])

    # Sanity check
    assert len(bulk_get_object_to_content) == get_count_of_files_in_folder_and_subfolders(download_folder)

    # We should skip over all objects since there is no --overwrite. There should be prompts
    result = invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--download-dir', download_folder])
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert 'Are you sure you want to overwrite it?' in result.output
    assert len(parsed_result['skipped-objects']) == len(bulk_get_object_to_content)

    # We should skip over all objects since we say --no-overwrite. Additionally there should be no prompts
    result = invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--download-dir', download_folder, '--no-overwrite'])
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert 'Are you sure you want to overwrite it?' not in result.output
    assert len(parsed_result['skipped-objects']) == len(bulk_get_object_to_content)

    # We should skip over no objects since we --overwrite
    result = invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--download-dir', download_folder, '--overwrite'])
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert len(parsed_result['skipped-objects']) == 0

    shutil.rmtree(download_folder)


def test_get_no_objects():
    download_folder = 'tests/temp/no_objects_{}'.format(bulk_get_bucket_name)
    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--download-dir', download_folder, '--prefix', 'batman'])

    assert 0 == get_count_of_files_in_folder_and_subfolders(download_folder)

    shutil.rmtree(download_folder)


# Bulk puts objects, uses multipart where appropriate (when we breach the default of 128MiB)
def test_bulk_put_default_options():
    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name, '--src-dir', root_bulk_put_folder])

    # No failures or skips and we uploaded everything
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert parsed_result['skipped-objects'] == []
    assert parsed_result['upload-failures'] == {}
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)

    # Check that we multipart uploaded the big files
    for file in bulk_put_large_files:
        assert 'Split file {} into'.format(get_object_name_from_path(root_bulk_put_folder, file)) in result.output

    # Sanity check that we didn't multipart upload the smaller files
    for file in bulk_put_mid_sized_files:
        assert 'Split file {} into'.format(get_object_name_from_path(root_bulk_put_folder, file)) not in result.output

    # Pull everything down and verify that the files match (everything in source appears in destination and they are equal)
    download_folder = 'tests/temp/verify_files_{}'.format(bulk_put_bucket_name)
    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name, '--download-dir', download_folder])
    object_name_set = set()
    for dir_name, subdir_list, file_list in os.walk(root_bulk_put_folder):
        for file in file_list:
            source_file_path = os.path.join(dir_name, file)
            downloaded_file_path = source_file_path.replace(root_bulk_put_folder, download_folder)

            assert os.path.exists(downloaded_file_path)
            assert filecmp.cmp(source_file_path, downloaded_file_path, shallow=False)

            # Sanity check that we're reporting back that we uploaded the right files
            assert get_object_name_from_path(root_bulk_put_folder, source_file_path) in parsed_result['uploaded-objects']
            object_name_set.add(get_object_name_from_path(root_bulk_put_folder, source_file_path))

    # If we try and put it in the same bucket without --overwrite then everything should be skipped. There should be prompts
    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name, '--src-dir', root_bulk_put_folder])
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert 'Are you sure you want to overwrite it?' in result.output
    assert set(parsed_result['skipped-objects']) == object_name_set
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['uploaded-objects'] == {}

    # If we say to --no-overwrite then everything should be skipped. There should be no prompts
    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name, '--src-dir', root_bulk_put_folder, '--no-overwrite'])
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert 'Are you sure you want to overwrite it?' not in result.output
    assert set(parsed_result['skipped-objects']) == object_name_set
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['uploaded-objects'] == {}

    # Now we force it
    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name, '--src-dir', root_bulk_put_folder, '--overwrite'])
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert parsed_result['skipped-objects'] == []
    assert parsed_result['upload-failures'] == {}
    assert len(parsed_result['uploaded-objects']) == len(object_name_set)
    for object_name in object_name_set:
        assert object_name in parsed_result['uploaded-objects']

    shutil.rmtree(download_folder)


# Tests that multipart params are applied:
#
#   - Try to upload with a part size of 10MiB (this will force the large and mid-sized files to be multipart uploaded)
#   - Try to upload with multipart disabled
def test_bulk_put_with_multipart_params(object_storage_client):
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkPutMultipartsTest_{}'.format(int(time.time()))
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    object_storage_client.create_bucket(util.NAMESPACE, create_bucket_request)

    result = invoke([
        'os', 'object', 'bulk-upload',
        '--namespace', util.NAMESPACE,
        '--bucket-name', create_bucket_request.name,
        '--src-dir', root_bulk_put_folder,
        '--part-size', '10',
        '--parallel-upload-count', '5'
    ])
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert parsed_result['skipped-objects'] == []
    assert parsed_result['upload-failures'] == {}
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)

    # Check that we multipart uploaded the big and small files
    for file in bulk_put_large_files:
        assert 'Split file {} into'.format(get_object_name_from_path(root_bulk_put_folder, file)) in result.output
    for file in bulk_put_mid_sized_files:
        assert 'Split file {} into'.format(get_object_name_from_path(root_bulk_put_folder, file)) in result.output

    result = invoke([
        'os', 'object', 'bulk-upload',
        '--namespace', util.NAMESPACE,
        '--bucket-name', create_bucket_request.name,
        '--src-dir', root_bulk_put_folder,
        '--no-multipart',
        '--overwrite'
    ])
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert parsed_result['skipped-objects'] == []
    assert parsed_result['upload-failures'] == {}
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)

    # Check that we didn't multipart uploaded either the big or small files
    for file in bulk_put_large_files:
        assert 'Split file {} into'.format(get_object_name_from_path(root_bulk_put_folder, file)) not in result.output
    for file in bulk_put_mid_sized_files:
        assert 'Split file {} into'.format(get_object_name_from_path(root_bulk_put_folder, file)) not in result.output

    delete_bucket_and_all_items(object_storage_client, create_bucket_request.name)


def test_bulk_put_with_non_existent_folder():
    fake_directory = 'tests/folder/not/exist'
    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name, '--src-dir', fake_directory])

    assert 'UsageError' in result.output
    assert 'The specified --src-dir {} (expanded to: {}) does not exist'.format(fake_directory, fake_directory) in result.output


def test_delete_when_no_objects_in_bucket(object_storage_client):
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkDelete_{}'.format(int(time.time()))
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    object_storage_client.create_bucket(util.NAMESPACE, create_bucket_request)

    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', create_bucket_request.name])
    assert 'There are no objects to delete in {}'.format(create_bucket_request.name) in result.output

    delete_bucket_and_all_items(object_storage_client, create_bucket_request.name)


def test_delete_dry_run():
    # Dry-run against entire bucket
    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--dry-run'])
    parsed_result = json.loads(result.output)
    assert set(parsed_result['deleted-objects']) == set(bulk_get_object_to_content.keys())

    # Dry-run against a folder and all subfolders
    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--prefix', 'a/b/', '--dry-run'])
    parsed_result = json.loads(result.output)
    expected_objects = set().union(bulk_get_prefix_to_object['a/b'], bulk_get_prefix_to_object['a/b/c'], bulk_get_prefix_to_object['a/b/c/d'])
    assert set(parsed_result['deleted-objects']) == expected_objects

    # Dry-run against a folder and no subfolders
    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--prefix', 'a/b/', '--delimiter', '/', '--dry-run'])
    parsed_result = json.loads(result.output)
    assert set(parsed_result['deleted-objects']) == set(bulk_get_prefix_to_object['a/b'])


def test_delete(object_storage_client):
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkDelete_{}'.format(int(time.time()))
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    object_storage_client.create_bucket(util.NAMESPACE, create_bucket_request)

    invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', create_bucket_request.name, '--src-dir', root_bulk_put_folder])
    num_objects_to_delete = get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)

    # Sanity check that the bucket has things in it
    assert get_number_of_objects_in_bucket(object_storage_client, create_bucket_request.name) > 0

    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', create_bucket_request.name])
    if num_objects_to_delete >= 1000:
        confirm_prompt = 'WARNING: This command will delete at least {} objects. Are you sure you wish to continue?'.format(num_objects_to_delete)
    else:
        confirm_prompt = 'WARNING: This command will delete {} objects. Are you sure you wish to continue?'.format(num_objects_to_delete)
    assert confirm_prompt in result.output

    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', create_bucket_request.name, '--force'])
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert parsed_result['delete-failures'] == {}
    assert len(parsed_result['deleted-objects']) == num_objects_to_delete

    # Check that the bucket is now empty
    assert get_number_of_objects_in_bucket(object_storage_client, create_bucket_request.name) == 0

    delete_bucket_and_all_items(object_storage_client, create_bucket_request.name)


def invoke(commands, debug=False, ** args):
        if debug is True:
            commands = ['--debug'] + commands

        return util.invoke_command(commands, ** args)


def get_count_of_files_in_folder_and_subfolders(directory):
    file_count = 0
    for dir_name, subdir_list, file_list in os.walk(directory):
        file_count = file_count + len(file_list)

    return file_count


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


# Pull JSON data out of output which may have stuff other than JSON in it. Assumes that nothing
# comes after the JSON data
def parse_json_response_from_mixed_output(output):
    lines = output.split('\n')
    json_str = ''
    object_begun = False
    for line in lines:
        if object_begun or line.startswith('{'):
            object_begun = True
            json_str += line

    return json.loads(json_str)


# For the bulk operations, object names are taken from the file path of the thing we uploaded.
def get_object_name_from_path(path_root, full_path):
    return full_path.replace(path_root + '/', '')


def delete_bucket_and_all_items(object_storage_client, bucket_name):
    list_object_responses = oci_cli.object_storage_cli.retrying_list_objects(
        client=object_storage_client,
        request_id=None,
        namespace=util.NAMESPACE,
        bucket_name=bucket_name,
        prefix=None,
        start=None,
        end=None,
        limit=1000,
        delimiter=None,
        fields='name',
        retrieve_all=True
    )
    for response in list_object_responses:
        for obj in response.data.objects:
            object_storage_client.delete_object(util.NAMESPACE, bucket_name, obj.name)
    object_storage_client.delete_bucket(util.NAMESPACE, bucket_name)


def get_number_of_objects_in_bucket(object_storage_client, bucket_name):
    list_object_responses = oci_cli.object_storage_cli.retrying_list_objects(
        client=object_storage_client,
        request_id=None,
        namespace=util.NAMESPACE,
        bucket_name=bucket_name,
        prefix=None,
        start=None,
        end=None,
        limit=1000,
        delimiter=None,
        fields='name',
        retrieve_all=True
    )
    num_objects_in_bucket = 0
    for response in list_object_responses:
        num_objects_in_bucket = num_objects_in_bucket + len(response.data.objects)

    return num_objects_in_bucket
