# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import filecmp
import json
import pytest
import oci
import oci_cli_object_storage
import os
import random
import shutil
import six
import string
from tests import util
from tests import test_config_container
from mimetypes import guess_type


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


@pytest.fixture
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir='services/object_storage/tests/cassettes').use_cassette('object_storage_bulk_operations_{name}.yml'.format(name=request.function.__name__)):
        yield


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
    create_bucket_request.name = 'ObjectStorageBulkGetTest_{}'.format(util.random_number_string())
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, create_bucket_request.name)
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
    root_bulk_put_folder = 'tests/temp/bulk_put_{}'.format(util.random_number_string())
    bulk_put_folder_leaf = '{}/subfolder1/subfolder2/subfolder3'.format(root_bulk_put_folder)
    if not os.path.exists(bulk_put_folder_leaf):
        os.makedirs(bulk_put_folder_leaf)

    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkPutTest_{}'.format(util.random_number_string())
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, create_bucket_request.name)
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


@util.skip_while_rerecording
def test_normalize_object_name_path():
    assert '/this/is/a/path' == oci_cli_object_storage.objectstorage_cli_extended.normalize_object_name_path_for_object_storage('/this/is/a/path')
    assert '/this/is/a/path' == oci_cli_object_storage.objectstorage_cli_extended.normalize_object_name_path_for_object_storage('/this/is/a/path', '/')
    assert '/this/is/a/path' == oci_cli_object_storage.objectstorage_cli_extended.normalize_object_name_path_for_object_storage('\\this\\is\\a\\path', '\\')
    assert '/this/is/a/path' == oci_cli_object_storage.objectstorage_cli_extended.normalize_object_name_path_for_object_storage('\\this/is/a\\path', '\\')

    assert 'thisisapath' == oci_cli_object_storage.objectstorage_cli_extended.normalize_object_name_path_for_object_storage('thisisapath')
    assert 'thisisapath' == oci_cli_object_storage.objectstorage_cli_extended.normalize_object_name_path_for_object_storage('thisisapath', '/')
    assert 'thisisapath' == oci_cli_object_storage.objectstorage_cli_extended.normalize_object_name_path_for_object_storage('thisisapath', '\\')


@util.skip_while_rerecording
def test_get_all_objects_in_bucket(vcr_fixture):
    download_folder = 'tests/temp/get_all_{}'.format(bulk_get_bucket_name)
    result = invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--download-dir', download_folder])
    print(result.output)

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


@util.skip_while_rerecording
def test_get_directory_and_subdirectories(vcr_fixture):
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


@util.skip_while_rerecording
def test_get_directory_no_subdirectory(vcr_fixture):
    download_folder = 'tests/temp/get_directory_only_{}'.format(bulk_get_bucket_name)
    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--download-dir', download_folder, '--prefix', 'a/b/c/', '--delimiter', '/'])

    for object_name in bulk_get_prefix_to_object['a/b/c']:
        file_path = os.path.join(download_folder, object_name)
        with open(file_path, 'r') as content_file:
            content = content_file.read()
            assert content == bulk_get_object_to_content[object_name]

    assert len(bulk_get_prefix_to_object['a/b/c']) == get_count_of_files_in_folder_and_subfolders(download_folder)

    shutil.rmtree(download_folder)


@util.skip_while_rerecording
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


@util.skip_while_rerecording
def test_get_no_objects(vcr_fixture):
    download_folder = 'tests/temp/no_objects_{}'.format(bulk_get_bucket_name)
    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--download-dir', download_folder, '--prefix', 'batman'])

    assert 0 == get_count_of_files_in_folder_and_subfolders(download_folder)

    shutil.rmtree(download_folder)


@util.skip_while_rerecording
def test_get_multipart(object_storage_client):
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkGetMultipartsTest_{}'.format(util.random_number_string())
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, create_bucket_request.name)
    object_storage_client.create_bucket(util.NAMESPACE, create_bucket_request)

    large_file_root_dir = os.path.join('tests', 'temp', 'multipart_get_large_files')
    if not os.path.exists(large_file_root_dir):
        os.makedirs(large_file_root_dir)
    util.create_large_file(os.path.join(large_file_root_dir, '1.bin'), LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)
    util.create_large_file(os.path.join(large_file_root_dir, '2.bin'), LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)
    util.create_large_file(os.path.join(large_file_root_dir, '3.bin'), LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)
    util.create_large_file(os.path.join(large_file_root_dir, '4.bin'), LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)
    util.create_large_file(os.path.join(large_file_root_dir, '5.bin'), LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)
    util.create_large_file(os.path.join(large_file_root_dir, '6.bin'), 1)  # Creates a 1 MiB file for variety

    invoke([
        'os', 'object', 'bulk-upload',
        '--namespace', util.NAMESPACE,
        '--bucket-name', create_bucket_request.name,
        '--src-dir', large_file_root_dir
    ])

    large_file_verify_dir = os.path.join('tests', 'temp', 'multipart_get_large_files_verify')

    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', create_bucket_request.name, '--download-dir', large_file_verify_dir, '--multipart-download-threshold', '128'])

    assert get_count_of_files_in_folder_and_subfolders(large_file_verify_dir) == 6
    assert filecmp.cmp(os.path.join(large_file_root_dir, '1.bin'), os.path.join(large_file_verify_dir, '1.bin'))
    assert filecmp.cmp(os.path.join(large_file_root_dir, '2.bin'), os.path.join(large_file_verify_dir, '2.bin'))
    assert filecmp.cmp(os.path.join(large_file_root_dir, '3.bin'), os.path.join(large_file_verify_dir, '3.bin'))
    assert filecmp.cmp(os.path.join(large_file_root_dir, '4.bin'), os.path.join(large_file_verify_dir, '4.bin'))
    assert filecmp.cmp(os.path.join(large_file_root_dir, '5.bin'), os.path.join(large_file_verify_dir, '5.bin'))
    assert filecmp.cmp(os.path.join(large_file_root_dir, '6.bin'), os.path.join(large_file_verify_dir, '6.bin'))

    shutil.rmtree(large_file_root_dir)
    shutil.rmtree(large_file_verify_dir)

    delete_bucket_and_all_items(object_storage_client, create_bucket_request.name)


# Since we've created a reasonable number of objects in this test suite, it's a good opportunity to test using the --all and --limit parameters
@util.skip_while_rerecording
def test_list_all_objects_operations(vcr_fixture):
    result = invoke(['os', 'object', 'list', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--all'])
    parsed_result = json.loads(result.output)
    assert len(parsed_result['data']) == OBJECTS_TO_CREATE_IN_BUCKET_FOR_BULK_GET
    assert 'next-start-with' not in result.output

    result = invoke(['os', 'object', 'list', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--all', '--page-size', '20'])
    parsed_result = json.loads(result.output)
    assert len(parsed_result['data']) == OBJECTS_TO_CREATE_IN_BUCKET_FOR_BULK_GET
    assert 'next-start-with' not in result.output

    result = invoke(['os', 'object', 'list', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--limit', '47'])
    parsed_result = json.loads(result.output)
    assert len(parsed_result['data']) == 47
    assert 'next-start-with' in result.output

    result = invoke(['os', 'object', 'list', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--limit', '33', '--page-size', '3'])
    parsed_result = json.loads(result.output)
    assert len(parsed_result['data']) == 33
    assert 'next-start-with' in result.output


# Bulk puts objects, uses multipart where appropriate (when we breach the default of 128MiB)
@util.skip_while_rerecording
def test_bulk_put_default_options():
    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name, '--src-dir', root_bulk_put_folder])

    # No failures or skips and we uploaded everything
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert parsed_result['skipped-objects'] == []
    assert parsed_result['upload-failures'] == {}
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)

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


# Bulk puts objects with --content-type as auto
@util.skip_while_rerecording
def test_bulk_put_auto_content_type():
    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name, '--src-dir', root_bulk_put_folder, '--content-type', 'auto', '--overwrite'])

    # No failures or skips and we uploaded everything
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert parsed_result['skipped-objects'] == []
    assert parsed_result['upload-failures'] == {}
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)

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
            assert guess_type(source_file_path) == guess_type(downloaded_file_path)

            # Sanity check that we're reporting back that we uploaded the right files
            assert get_object_name_from_path(root_bulk_put_folder, source_file_path) in parsed_result['uploaded-objects']
            object_name_set.add(get_object_name_from_path(root_bulk_put_folder, source_file_path))

    shutil.rmtree(download_folder)


# Tests that multipart params are applied:
#
#   - Try to upload with a part size of 10MiB (this will force the large and mid-sized files to be multipart uploaded)
#   - Try to upload with multipart disabled
@util.skip_while_rerecording
def test_bulk_put_with_multipart_params(object_storage_client):
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkPutMultipartsTest_{}'.format(util.random_number_string())
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, create_bucket_request.name)
    object_storage_client.create_bucket(util.NAMESPACE, create_bucket_request)

    result = invoke([
        'os', 'object', 'bulk-upload',
        '--namespace', util.NAMESPACE,
        '--bucket-name', create_bucket_request.name,
        '--src-dir', root_bulk_put_folder,
        '--part-size', '10'
    ])
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert parsed_result['skipped-objects'] == []
    assert parsed_result['upload-failures'] == {}
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)

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

    delete_bucket_and_all_items(object_storage_client, create_bucket_request.name)


@util.skip_while_rerecording
def test_bulk_put_with_prefix():
    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name, '--src-dir', root_bulk_put_folder, '--object-prefix', 'bulk_put_prefix_test/'])

    # No failures or skips and we uploaded everything
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert parsed_result['skipped-objects'] == []
    assert parsed_result['upload-failures'] == {}
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)

    download_folder = 'tests/temp/verify_files_bulk_put_prefix_{}'.format(bulk_put_bucket_name)
    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name, '--download-dir', download_folder, '--prefix', 'bulk_put_prefix_test/'])

    actual_download_folder = os.path.join(download_folder, 'bulk_put_prefix_test')
    for dir_name, subdir_list, file_list in os.walk(root_bulk_put_folder):
        for file in file_list:
            source_file_path = os.path.join(dir_name, file)
            downloaded_file_path = source_file_path.replace(root_bulk_put_folder, actual_download_folder)

            assert os.path.exists(downloaded_file_path)
            assert filecmp.cmp(source_file_path, downloaded_file_path, shallow=False)

            # Sanity check that we're reporting back that we uploaded the right files
            assert 'bulk_put_prefix_test/{}'.format(get_object_name_from_path(root_bulk_put_folder, source_file_path)) in parsed_result['uploaded-objects']

    shutil.rmtree(download_folder)


@util.skip_while_rerecording
def test_bulk_put_with_non_existent_folder():
    fake_directory = 'tests/folder/not/exist'
    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name, '--src-dir', fake_directory])

    assert 'UsageError' in result.output
    assert 'The specified --src-dir {} (expanded to: {}) does not exist'.format(fake_directory, fake_directory) in result.output


@util.skip_while_rerecording
def test_bulk_put_get_delete_with_inclusions(object_storage_client):
    inclusion_test_folder = os.path.join('tests', 'temp', 'os_bulk_upload_inclusion_test')
    if not os.path.exists(inclusion_test_folder):
        os.makedirs(inclusion_test_folder)

    # Make some files for include/exclude
    folders_to_files = {
        '': ['test_file1.txt', 'test_file2.png'],
        'subfolder': ['blah.pdf', 'hello.txt', 'testfile3.png'],
        'subfolder/subfolder2': ['xyz.jpg', 'blag.txt', 'byz.jpg', 'testfile4.png']
    }
    for folder, files in six.iteritems(folders_to_files):
        folder_path = os.path.join(inclusion_test_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'w') as f:
                # For non-text extension types this won't create a valid file, but for testing is probably OK
                f.write(generate_random_string(CONTENT_STRING_LENGTH))

    result = invoke([
        'os',
        'object',
        'bulk-upload',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bulk_put_bucket_name,
        '--src-dir', inclusion_test_folder,
        '--object-prefix', 'inclusion_test/',
        '--include', '*.txt',  # Matches test_file1.txt, subfolder/hello.txt, subfolder/subfolder2/blag.txt
        '--include', 'subfolder/*.png',  # Matches subfolder/testfile3.png, subfolder/subfolder2/testfile4.png
        '--include', 'subfolder/[b]lah.pdf',  # Matches subfolder/blah.pdf
        '--include', '*/[ax]yz.jpg'  # Matches subfolder/subfolder2/xyz.jpg
    ])
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert parsed_result['skipped-objects'] == []
    assert parsed_result['upload-failures'] == {}

    expected_uploaded_files = [
        '{}{}'.format('inclusion_test/', 'test_file1.txt'),
        '{}{}'.format('inclusion_test/', 'subfolder/hello.txt'),
        '{}{}'.format('inclusion_test/', 'subfolder/subfolder2/blag.txt'),
        '{}{}'.format('inclusion_test/', 'subfolder/testfile3.png'),
        '{}{}'.format('inclusion_test/', 'subfolder/subfolder2/testfile4.png'),
        '{}{}'.format('inclusion_test/', 'subfolder/blah.pdf'),
        '{}{}'.format('inclusion_test/', 'subfolder/subfolder2/xyz.jpg')
    ]

    # Check that we uploaded what we said we did
    assert len(parsed_result['uploaded-objects']) == len(expected_uploaded_files)
    for f in expected_uploaded_files:
        assert f in parsed_result['uploaded-objects']

    download_folder_base = os.path.join('tests', 'temp', 'verify_os_bulk_upload_inclusion_test')
    verify_downloaded_folders_for_inclusion_exclusion_tests(
        expected_uploaded_files=expected_uploaded_files,
        source_folder=inclusion_test_folder,
        download_folder=download_folder_base,
        download_prefix_no_slash='inclusion_test'
    )

    # Download objects with inclusions to make sure that works
    target_download_folder = os.path.join(download_folder_base, 'get_with_include')
    invoke([
        'os', 'object', 'bulk-download',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bulk_put_bucket_name,
        '--download-dir', target_download_folder,
        '--prefix', 'inclusion_test/',
        '--include', '*.txt',
        '--include', 'subfolder/*.png',
        '--include', 'subfolder/blah.pdf',
    ])
    expected_uploaded_files.remove('{}{}'.format('inclusion_test/', 'subfolder/subfolder2/xyz.jpg'))  # This is not in our --include switches
    assert not os.path.exists(os.path.join(target_download_folder, 'inclusion_test', 'subfolder', 'subfolder2', 'xyz.jpg'))
    for expected_file in expected_uploaded_files:
        target_file = os.path.join(target_download_folder, expected_file)
        original_file = target_file.replace(os.path.join(target_download_folder, 'inclusion_test'), inclusion_test_folder)

        assert os.path.exists(target_file)
        assert filecmp.cmp(original_file, target_file, shallow=False)

    # Download a specific object with inclusions
    invoke([
        'os', 'object', 'bulk-download',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bulk_put_bucket_name,
        '--download-dir', target_download_folder,
        '--prefix', 'inclusion_test/',
        '--include', 'subfolder/subfolder2/xyz.jpg'
    ])
    assert os.path.exists(os.path.join(target_download_folder, 'inclusion_test', 'subfolder', 'subfolder2', 'xyz.jpg'))

    # Delete objects with inclusions
    result = invoke([
        'os', 'object', 'bulk-delete',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bulk_put_bucket_name,
        '--prefix', 'inclusion_test/',
        '--include', '*.txt',
        '--include', 'subfolder/blah.pdf',
        '--dry-run'
    ])
    parsed_dry_run_result = parse_json_response_from_mixed_output(result.output)
    assert len(parsed_dry_run_result['deleted-objects']) == 4

    result = invoke([
        'os', 'object', 'bulk-delete',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bulk_put_bucket_name,
        '--prefix', 'inclusion_test/',
        '--include', '*.txt',
        '--include', 'subfolder/blah.pdf',
        '--force'
    ])
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert parsed_result['delete-failures'] == {}
    assert set(parsed_result['deleted-objects']) == set(parsed_dry_run_result['deleted-objects'])

    list_objects_responses = oci_cli_object_storage.objectstorage_cli_extended.retrying_list_objects(
        client=object_storage_client,
        request_id=None,
        namespace=util.NAMESPACE,
        bucket_name=bulk_put_bucket_name,
        prefix='inclusion_test/',
        start=None,
        end=None,
        limit=1000,
        delimiter=None,
        fields='name',
        retrieve_all=True
    )
    remaining_objects = []
    for response in list_objects_responses:
        remaining_objects.extend(map(lambda obj: obj.name, response.data.objects))
    assert len(remaining_objects) == 3
    assert '{}{}'.format('inclusion_test/', 'subfolder/testfile3.png') in remaining_objects
    assert '{}{}'.format('inclusion_test/', 'subfolder/subfolder2/testfile4.png') in remaining_objects
    assert '{}{}'.format('inclusion_test/', 'subfolder/subfolder2/xyz.jpg') in remaining_objects

    shutil.rmtree(target_download_folder)
    shutil.rmtree(inclusion_test_folder)


@util.skip_while_rerecording
def test_bulk_put_get_delete_with_exclusions(object_storage_client):
    exclusion_test_folder = os.path.join('tests', 'temp', 'os_bulk_upload_exclusion_test')
    if not os.path.exists(exclusion_test_folder):
        os.makedirs(exclusion_test_folder)

    # Make some files for include/exclude
    folders_to_files = {
        '': ['test_file1.txt', 'test_file2.png'],
        'subfolder': ['blah.pdf', 'hello.txt', 'testfile3.png'],
        'subfolder/subfolder2': ['xyz.jpg', 'blag.txt', 'byz.jpg', 'testfile4.png']
    }
    for folder, files in six.iteritems(folders_to_files):
        folder_path = os.path.join(exclusion_test_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'w') as f:
                # For non-text extension types this won't create a valid file, but for testing is probably OK
                f.write(generate_random_string(CONTENT_STRING_LENGTH))

    result = invoke([
        'os',
        'object',
        'bulk-upload',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bulk_put_bucket_name,
        '--src-dir', exclusion_test_folder,
        '--object-prefix', 'exclusion_test/',
        '--exclude', '*.txt',
        '--exclude', '*.ps1',  # Shouldn't match anything
        '--exclude', 'subfolder/subfolder2/xyz.jpg',
        '--exclude', 'subfolder/[spqr]lah.pdf'  # blah.pdf should still be included because it's not slah.pdf, plah.pdf, qlah.pdf or rlah.pdf
    ])
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert parsed_result['skipped-objects'] == []
    assert parsed_result['upload-failures'] == {}

    expected_uploaded_files = [
        '{}{}'.format('exclusion_test/', 'test_file2.png'),
        '{}{}'.format('exclusion_test/', 'subfolder/blah.pdf'),
        '{}{}'.format('exclusion_test/', 'subfolder/testfile3.png'),
        '{}{}'.format('exclusion_test/', 'subfolder/subfolder2/byz.jpg'),
        '{}{}'.format('exclusion_test/', 'subfolder/subfolder2/testfile4.png')
    ]

    # Check that we uploaded what we said we did
    assert len(parsed_result['uploaded-objects']) == len(expected_uploaded_files)
    for f in expected_uploaded_files:
        assert f in parsed_result['uploaded-objects']

    download_folder_base = os.path.join('tests', 'temp', 'verify_os_bulk_upload_exclusion_test')
    verify_downloaded_folders_for_inclusion_exclusion_tests(
        expected_uploaded_files=expected_uploaded_files,
        source_folder=exclusion_test_folder,
        download_folder=download_folder_base,
        download_prefix_no_slash='exclusion_test'
    )

    # Download objects with exclusions to make sure that works
    target_download_folder = os.path.join(download_folder_base, 'get_with_exclude')
    invoke([
        'os', 'object', 'bulk-download',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bulk_put_bucket_name,
        '--download-dir', target_download_folder,
        '--prefix', 'exclusion_test/',
        '--exclude', '*.jpg',
        '--exclude', 'subfolder/subfolder2/*.png',
        '--exclude', 'subfolder/blah.pdf',
    ])

    assert not os.path.exists(os.path.join(target_download_folder, 'exclusion_test', 'subfolder', 'blah.pdf'))
    assert not os.path.exists(os.path.join(target_download_folder, 'exclusion_test', 'subfolder', 'subfolder2', 'byz.jpg'))
    assert not os.path.exists(os.path.join(target_download_folder, 'exclusion_test', 'subfolder', 'subfolder2', 'testfile4.png'))

    assert get_count_of_files_in_folder_and_subfolders(target_download_folder) == 2
    assert os.path.exists(os.path.join(target_download_folder, 'exclusion_test', 'test_file2.png'))
    assert os.path.exists(os.path.join(target_download_folder, 'exclusion_test', 'subfolder', 'testfile3.png'))

    assert filecmp.cmp(
        os.path.join(exclusion_test_folder, 'test_file2.png'),
        os.path.join(target_download_folder, 'exclusion_test', 'test_file2.png')
    )
    assert filecmp.cmp(
        os.path.join(exclusion_test_folder, 'subfolder', 'testfile3.png'),
        os.path.join(target_download_folder, 'exclusion_test', 'subfolder', 'testfile3.png')
    )

    # Delete objects with exclusions
    result = invoke([
        'os', 'object', 'bulk-delete',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bulk_put_bucket_name,
        '--prefix', 'exclusion_test/',
        '--exclude', '*.jpg',
        '--exclude', 'subfolder/blah.pdf',
        '--dry-run'
    ])
    parsed_dry_run_result = parse_json_response_from_mixed_output(result.output)
    assert len(parsed_dry_run_result['deleted-objects']) == 3

    result = invoke([
        'os', 'object', 'bulk-delete',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bulk_put_bucket_name,
        '--prefix', 'exclusion_test/',
        '--exclude', '*.jpg',
        '--exclude', 'subfolder/blah.pdf',
        '--force'
    ])
    parsed_result = parse_json_response_from_mixed_output(result.output)
    assert parsed_result['delete-failures'] == {}
    assert set(parsed_result['deleted-objects']) == set(parsed_dry_run_result['deleted-objects'])

    list_objects_responses = oci_cli_object_storage.objectstorage_cli_extended.retrying_list_objects(
        client=object_storage_client,
        request_id=None,
        namespace=util.NAMESPACE,
        bucket_name=bulk_put_bucket_name,
        prefix='exclusion_test/',
        start=None,
        end=None,
        limit=1000,
        delimiter=None,
        fields='name',
        retrieve_all=True
    )
    remaining_objects = []
    for response in list_objects_responses:
        remaining_objects.extend(map(lambda obj: obj.name, response.data.objects))
    assert len(remaining_objects) == 2
    assert '{}{}'.format('exclusion_test/', 'subfolder/blah.pdf') in remaining_objects
    assert '{}{}'.format('exclusion_test/', 'subfolder/subfolder2/byz.jpg') in remaining_objects

    shutil.rmtree(target_download_folder)
    shutil.rmtree(exclusion_test_folder)


@util.skip_while_rerecording
def test_delete_when_no_objects_in_bucket(vcr_fixture, object_storage_client):
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkDelete_{}'.format(util.random_number_string())
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    object_storage_client.create_bucket(util.NAMESPACE, create_bucket_request)

    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', create_bucket_request.name])
    assert 'There are no objects to delete in {}'.format(create_bucket_request.name) in result.output

    delete_bucket_and_all_items(object_storage_client, create_bucket_request.name)


@util.skip_while_rerecording
def test_delete_dry_run(vcr_fixture):
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


@util.skip_while_rerecording
def test_delete(object_storage_client):
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkDelete_{}'.format(random.randint(0, 1000000))
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, create_bucket_request.name)
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


@util.skip_while_rerecording
def test_bulk_operation_table_output_query(object_storage_client):
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageTableOutput_{}'.format(util.random_number_string())
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, create_bucket_request.name)
    object_storage_client.create_bucket(util.NAMESPACE, create_bucket_request)

    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', create_bucket_request.name, '--src-dir', root_bulk_put_folder, '--output', 'table', '--query', "[?action=='Uploaded'].{file: file, \"opc-content-md5\": \"opc-content-md5\"}"])
    assert 'file' in result.output
    assert 'opc-content-md5' in result.output
    assert 'etag' not in result.output

    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--dry-run', '--output', 'table'])
    assert 'action' in result.output
    assert 'object' in result.output
    assert '/a/Object_1' in result.output

    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--dry-run', '--output', 'table', '--query', "[?object=='Object_0'][object]"])
    assert 'action' not in result.output
    assert '/a/Object_1' not in result.output
    assert 'Object_0' in result.output

    target_download_folder = os.path.join('tests', 'temp', create_bucket_request.name)
    result = invoke([
        'os', 'object', 'bulk-download',
        '--namespace', util.NAMESPACE,
        '--bucket-name', create_bucket_request.name,
        '--download-dir', target_download_folder,
        '--output', 'table',
    ])

    delete_bucket_and_all_items(object_storage_client, create_bucket_request.name)

    shutil.rmtree(target_download_folder)


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
    if test_config_container.using_vcr_with_mock_responses():
        return 'a' * length
    else:
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


# For the bulk operations, object names are taken from the file path of the thing we uploaded. Normalize to
# / in the paths (Windows can go both ways) then chop the front bit off
def get_object_name_from_path(path_root, full_path):
    return full_path.replace(os.sep, '/').replace(path_root + '/', '')


def delete_bucket_and_all_items(object_storage_client, bucket_name):
    list_object_responses = oci_cli_object_storage.objectstorage_cli_extended.retrying_list_objects(
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
    list_object_responses = oci_cli_object_storage.objectstorage_cli_extended.retrying_list_objects(
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


def verify_downloaded_folders_for_inclusion_exclusion_tests(expected_uploaded_files, source_folder, download_folder, download_prefix_no_slash):
    # Download uploaded files and check they are the same
    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name, '--download-dir', download_folder, '--prefix', download_prefix_no_slash + '/'])

    # The strings in the expected_uploaded_files array have a "/" in them, but this doesn't match with paths on Windows. Using normpath converts these of
    # "\" on Windows and so our matching/comparison works. For Linux/Unix/macOS this doesn't appear to have an impact
    normalized_expected_uploaded_files = []
    for euf in expected_uploaded_files:
        normalized_expected_uploaded_files.append(os.path.normpath(euf))

    actual_download_folder = os.path.join(download_folder, download_prefix_no_slash)
    files_compared = 0
    for dir_name, subdir_list, file_list in os.walk(source_folder):
        for file in file_list:
            source_file_path = os.path.join(dir_name, file)
            downloaded_file_path = source_file_path.replace(source_folder, actual_download_folder)

            if downloaded_file_path.replace(actual_download_folder, download_prefix_no_slash) in normalized_expected_uploaded_files:
                files_compared += 1
                assert os.path.exists(downloaded_file_path)
                assert filecmp.cmp(source_file_path, downloaded_file_path, shallow=False)
    assert files_compared == len(expected_uploaded_files)

    shutil.rmtree(actual_download_folder)
