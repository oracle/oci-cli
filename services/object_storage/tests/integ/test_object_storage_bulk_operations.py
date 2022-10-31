# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import base64
import datetime
import filecmp
import json
import logging
import os
import random
import shutil
import string
from mimetypes import guess_type
import sys

import oci
import pytest
import six
from oci.object_storage.models import CreatePreauthenticatedRequestDetails, CreateReplicationPolicyDetails, \
    CreateMultipartUploadDetails

import services.object_storage.src.oci_cli_object_storage as oci_cli_object_storage
from tests import test_config_container
from tests import util

OBJECTS_TO_CREATE_IN_BUCKET_FOR_BULK_GET = 100
OBJECTS_TO_CREATE_IN_FOLDER_FOR_BULK_PUT = 20
CONTENT_STRING_LENGTH = 5000
CONTENT_STRING_LENGTH_SHORT = 50
MID_SIZED_FILE_IN_MEBIBTYES = 20
LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES = 150  # Default multipart is 128MiB
GENERATED_ENC_KEY_FILE = 'tests/temp/generated_enc_key_bulk.txt'


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
bulk_get_bucket_name_recorded = None

bulk_put_large_files = set()
bulk_put_mid_sized_files = set()
root_bulk_put_folder = None
bulk_put_bucket_name = None

created_buckets = 'created_buckets'
test_success = 'test_success'


def is_python2():
    return sys.version_info[0] < 3


@pytest.fixture
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir='services/object_storage/tests/cassettes').use_cassette('object_storage_bulk_operations_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.fixture(params=[False])
def debug(request):
    return request.param


@pytest.fixture(scope='function')
def on_error_fixture():
    data = {created_buckets: [], test_success: False}
    yield data
    if not data[test_success]:
        for bucket_name in data[created_buckets]:
            delete_test_bucket_on_failure(bucket_name)


@pytest.fixture(scope='function')
def delete_pending_buckets():
    data = {created_buckets: []}
    yield data
    logging.debug("--------Deleting Created Buckets-----------")
    for bucket_name in data[created_buckets]:
        delete_bucket(bucket_name)


def delete_bucket(bucket_name):
    invoke(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--empty', '--force'])


def create_empty_dir_at_path(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)


# Generate test data for different operations:
#
#    Bulk Get: create a new bucket and populate it with some objects, then tear it all down afterwards
#    Bulk Put: create a folder structure containing small and large files, then tear it all down afterwards
#    Bulk Delete: uses the folders and files generated for bulk put


@pytest.fixture(scope='module', autouse=True)
def generate_test_data(object_storage_client, test_id):
    global bulk_get_object_to_content, bulk_get_bucket_name, root_bulk_put_folder, bulk_put_large_files, bulk_put_mid_sized_files, bulk_put_bucket_name

    # Create a test bucket
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkGetTest_{}'.format(test_id)
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
    root_bulk_put_folder = 'tests/temp/bulk_put_{}'.format(test_id)
    bulk_put_folder_leaf = '{}/subfolder1/subfolder2/subfolder3'.format(root_bulk_put_folder)
    if not os.path.exists(bulk_put_folder_leaf):
        os.makedirs(bulk_put_folder_leaf)

    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkPutTest_{}'.format(test_id)
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

    # create the SSE-C encryption key
    enc_key_str = generate_aes256_key_str()
    with open(GENERATED_ENC_KEY_FILE, 'w') as f:
        f.write(enc_key_str)

    yield
    # deleting buckets directly here only to prevent changes in util.py file
    invoke(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--empty', '--force'])
    invoke(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name, '--empty', '--force'])
    # Tear down stuff by deleting all the things and then deleting the buckets
    # util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bulk_get_bucket_name)
    # util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bulk_put_bucket_name)

    # remove the SSE-C key file
    if os.path.exists(GENERATED_ENC_KEY_FILE):
        os.remove(GENERATED_ENC_KEY_FILE)

    # Remove all directories recursively
    shutil.rmtree(root_bulk_put_folder)


@pytest.fixture(params=[False, True])
def customer_key(request):
    return request.param


@util.skip_while_rerecording
def test_normalize_object_name_path():
    assert '/this/is/a/path' == oci_cli_object_storage.objectstorage_cli_extended.normalize_file_path_for_object_storage('/this/is/a/path')
    assert '/this/is/a/path' == oci_cli_object_storage.objectstorage_cli_extended.normalize_file_path_for_object_storage('/this/is/a/path', '/')
    assert '/this/is/a/path' == oci_cli_object_storage.objectstorage_cli_extended.normalize_file_path_for_object_storage('\\this\\is\\a\\path', '\\')
    assert '/this/is/a/path' == oci_cli_object_storage.objectstorage_cli_extended.normalize_file_path_for_object_storage('\\this/is/a\\path', '\\')

    assert 'thisisapath' == oci_cli_object_storage.objectstorage_cli_extended.normalize_file_path_for_object_storage('thisisapath')
    assert 'thisisapath' == oci_cli_object_storage.objectstorage_cli_extended.normalize_file_path_for_object_storage('thisisapath', '/')
    assert 'thisisapath' == oci_cli_object_storage.objectstorage_cli_extended.normalize_file_path_for_object_storage('thisisapath', '\\')


@pytest.fixture(scope='module', autouse=True)
def set_recorded_variable(test_id_recorded):
    global bulk_get_bucket_name_recorded
    bulk_get_bucket_name_recorded = f'ObjectStorageBulkGetTest_{test_id_recorded}'


def test_get_all_objects_in_bucket(vcr_fixture):
    download_folder = 'tests/temp/get_all_{}'.format(bulk_get_bucket_name_recorded)

    result = invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name_recorded, '--download-dir', download_folder, '--dry-run'])
    assert len(os.listdir(download_folder)) == 0
    result = invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name_recorded, '--download-dir', download_folder])

    # Ensure that content matches
    for object_name in bulk_get_object_to_content:
        if object_name[0] == '/':
            file_path = os.path.join(download_folder, object_name[1:])
        elif object_name[0:2] == '\\':
            file_path = os.path.join(download_folder, object_name[2:])
        else:
            file_path = os.path.join(download_folder, object_name)

        with open(file_path, 'r') as content_file:
            content = content_file.read()
            assert content == bulk_get_object_to_content[object_name]

    assert len(bulk_get_object_to_content) == get_count_of_files_in_folder_and_subfolders(download_folder)

    shutil.rmtree(download_folder)


def test_get_directory_and_subdirectories(vcr_fixture):
    download_folder = 'tests/temp/get_directory_and_subdirectories_{}'.format(bulk_get_bucket_name_recorded)

    # This should get us a/b/<object>, a/b/c/<object> and a/b/c/d/<object>
    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name_recorded, '--download-dir', download_folder, '--prefix', 'a/b'])

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


def test_get_directory_no_subdirectory(vcr_fixture):
    download_folder = 'tests/temp/get_directory_only_{}'.format(bulk_get_bucket_name_recorded)
    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name_recorded, '--download-dir', download_folder, '--prefix', 'a/b/c/', '--delimiter', '/'])

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
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert 'Are you sure you want to overwrite it?' in result.output
    assert len(parsed_result['skipped-objects']) == len(bulk_get_object_to_content)

    # We should skip over all objects since we say --no-overwrite. Additionally there should be no prompts
    result = invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--download-dir', download_folder, '--no-overwrite'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert 'Are you sure you want to overwrite it?' not in result.output
    assert len(parsed_result['skipped-objects']) == len(bulk_get_object_to_content)

    # We should skip over no objects since we --overwrite
    result = invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--download-dir', download_folder, '--overwrite'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert len(parsed_result['skipped-objects']) == 0

    shutil.rmtree(download_folder)


def test_get_no_objects(vcr_fixture):
    download_folder = 'tests/temp/no_objects_{}'.format(bulk_get_bucket_name)
    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--download-dir', download_folder, '--prefix', 'batman'])

    assert 0 == get_count_of_files_in_folder_and_subfolders(download_folder)

    shutil.rmtree(download_folder)


@util.skip_while_rerecording
def test_get_multipart(object_storage_client, test_id, delete_pending_buckets):
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkGetMultipartsTest_{}'.format(test_id)
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, create_bucket_request.name)
    object_storage_client.create_bucket(util.NAMESPACE, create_bucket_request)
    delete_pending_buckets[created_buckets].append(create_bucket_request.name)

    large_file_root_dir = os.path.join('tests', 'temp', 'multipart_get_large_files')
    create_empty_dir_at_path(large_file_root_dir)

    util.create_large_file(os.path.join(large_file_root_dir, '1.bin'), LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)
    util.create_large_file(os.path.join(large_file_root_dir, '2.bin'), LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)
    util.create_large_file(os.path.join(large_file_root_dir, '3.bin'), LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)
    util.create_large_file(os.path.join(large_file_root_dir, '4.bin'), LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)
    util.create_large_file(os.path.join(large_file_root_dir, '5.bin'), LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)
    util.create_large_file(os.path.join(large_file_root_dir, '6.bin'), 1)  # Creates a 1 MiB file for variety
    # check --dry-run with bulk-upload
    invoke([
        'os', 'object', 'bulk-upload',
        '--namespace', util.NAMESPACE,
        '--bucket-name', create_bucket_request.name,
        '--src-dir', large_file_root_dir,
        '--exclude', '6.bin',
        '--dry-run'
    ])
    large_file_verify_dir = os.path.join('tests', 'temp', 'multipart_get_large_files_verify')
    create_empty_dir_at_path(large_file_verify_dir)
    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', create_bucket_request.name,
            '--download-dir', large_file_verify_dir])
    assert get_count_of_files_in_folder_and_subfolders(large_file_verify_dir) == 0
    shutil.rmtree(large_file_verify_dir)
    # --dry-run bulk-upload check ends
    large_file_verify_dir = os.path.join('tests', 'temp', 'multipart_get_large_files_verify')
    invoke([
        'os', 'object', 'bulk-upload',
        '--namespace', util.NAMESPACE,
        '--bucket-name', create_bucket_request.name,
        '--src-dir', large_file_root_dir
    ])
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
    delete_pending_buckets[created_buckets].remove(create_bucket_request.name)


# Since we've created a reasonable number of objects in this test suite, it's a good opportunity to test using the --all and --limit parameters
def test_list_all_objects_operations(vcr_fixture):
    result = invoke(['os', 'object', 'list', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name_recorded, '--all'])
    parsed_result = json.loads(result.output)
    assert len(parsed_result['data']) == OBJECTS_TO_CREATE_IN_BUCKET_FOR_BULK_GET
    assert 'next-start-with' not in result.output

    result = invoke(['os', 'object', 'list', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name_recorded, '--all', '--page-size', '20'])
    parsed_result = json.loads(result.output)
    assert len(parsed_result['data']) == OBJECTS_TO_CREATE_IN_BUCKET_FOR_BULK_GET
    assert 'next-start-with' not in result.output

    result = invoke(['os', 'object', 'list', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name_recorded, '--limit', '47'])
    parsed_result = json.loads(result.output)
    assert len(parsed_result['data']) == 47
    assert 'next-start-with' in result.output

    result = invoke(['os', 'object', 'list', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name_recorded, '--limit', '33', '--page-size', '3'])
    parsed_result = json.loads(result.output)
    assert len(parsed_result['data']) == 33
    assert 'next-start-with' in result.output


# Bulk puts objects, uses multipart where appropriate (when we breach the default of 128MiB)
@util.skip_while_rerecording
def test_bulk_put_default_options(customer_key):
    pytest.skip('To fix Team City Object storage failure')
    ssec_params = []
    if customer_key:
        ssec_params = ['--encryption-key-file', GENERATED_ENC_KEY_FILE]

    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name,
                     '--src-dir', root_bulk_put_folder] + ssec_params)

    # No failures or skips and we uploaded everything
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['skipped-objects'] == []
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)

    # Pull everything down and verify that the files match (everything in source appears in destination and they are equal)
    download_folder = 'tests/temp/verify_files_{}'.format(bulk_put_bucket_name)
    invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name,
            '--download-dir', download_folder] + ssec_params)
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
    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name,
                     '--src-dir', root_bulk_put_folder] + ssec_params)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert 'Are you sure you want to overwrite it?' in result.output
    assert set(parsed_result['skipped-objects']) == object_name_set
    assert parsed_result['uploaded-objects'] == {}

    # If we say to --no-overwrite then everything should be skipped. There should be no prompts
    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name,
                     '--src-dir', root_bulk_put_folder, '--no-overwrite'] + ssec_params)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert 'Are you sure you want to overwrite it?' not in result.output
    assert set(parsed_result['skipped-objects']) == object_name_set
    assert parsed_result['uploaded-objects'] == {}

    # Now we force it
    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name,
                     '--src-dir', root_bulk_put_folder, '--overwrite'] + ssec_params)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['skipped-objects'] == []
    assert len(parsed_result['uploaded-objects']) == len(object_name_set)
    for object_name in object_name_set:
        assert object_name in parsed_result['uploaded-objects']

    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name,
                     '--src-dir', root_bulk_put_folder, '--overwrite', '--verify-checksum'] + ssec_params)

    # No failures or skips and we uploaded everything
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['skipped-objects'] == []
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)
    for uploaded_object_name in parsed_result['uploaded-objects']:
        assert "md5 checksum matches" in parsed_result['uploaded-objects'][uploaded_object_name]['verify-md5-checksum']

    shutil.rmtree(download_folder)


# Bulk puts objects with --content-type as auto
@util.skip_while_rerecording
def test_bulk_put_auto_content_type():
    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name, '--src-dir', root_bulk_put_folder, '--content-type', 'auto', '--overwrite'])

    # No failures or skips and we uploaded everything
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['skipped-objects'] == []
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)

    result = invoke([
        'os', 'object', 'bulk-upload',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bulk_put_bucket_name,
        '--src-dir', root_bulk_put_folder,
        '--content-type', 'auto', '--overwrite', '--verify-checksum'
    ])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['skipped-objects'] == []
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)
    for uploaded_object_name in parsed_result['uploaded-objects']:
        assert "md5 checksum matches" in parsed_result['uploaded-objects'][uploaded_object_name]['verify-md5-checksum']

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
def test_bulk_put_with_multipart_params(object_storage_client, test_id, delete_pending_buckets):
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkPutMultipartsTest_{}'.format(test_id)
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, create_bucket_request.name)
    object_storage_client.create_bucket(util.NAMESPACE, create_bucket_request)
    delete_pending_buckets[created_buckets].append(create_bucket_request.name)

    # storage-tier check
    result = invoke([
        'os', 'object', 'bulk-upload',
        '--namespace', util.NAMESPACE,
        '--bucket-name', create_bucket_request.name,
        '--src-dir', root_bulk_put_folder,
        '--part-size', '10',
        '--storage-tier', 'InfrequentAccess'
    ])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['skipped-objects'] == []
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)

    result = invoke(['os', 'object', 'list', '--namespace', util.NAMESPACE, '--bucket-name', create_bucket_request.name, '--fields=name,size,storageTier', '--all', '--page-size', '1000'])
    parsed_result = json.loads(result.output)
    if 'data' in parsed_result:
        objects = parsed_result['data']
        for obj in objects:
            assert 'InfrequentAccess' == obj['storage-tier']

    # no-multipart check
    result = invoke([
        'os', 'object', 'bulk-upload',
        '--namespace', util.NAMESPACE,
        '--bucket-name', create_bucket_request.name,
        '--src-dir', root_bulk_put_folder,
        '--no-multipart',
        '--overwrite',
        '--storage-tier', 'InfrequentAccess'
    ])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['skipped-objects'] == []
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)

    result = invoke(['os', 'object', 'list', '--namespace', util.NAMESPACE, '--bucket-name', create_bucket_request.name, '--fields=name,size,storageTier', '--all', '--page-size', '1000'])
    parsed_result = json.loads(result.output)
    if 'data' in parsed_result:
        objects = parsed_result['data']
        for obj in objects:
            assert 'InfrequentAccess' == obj['storage-tier']

    # verify checksum check
    result = invoke([
        'os', 'object', 'bulk-upload',
        '--namespace', util.NAMESPACE,
        '--bucket-name', create_bucket_request.name,
        '--src-dir', root_bulk_put_folder,
        '--no-multipart', '--overwrite', '--verify-checksum'
    ])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['skipped-objects'] == []
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)
    for uploaded_object_name in parsed_result['uploaded-objects']:
        assert "md5 checksum matches" in parsed_result['uploaded-objects'][uploaded_object_name]['verify-md5-checksum']

    delete_bucket_and_all_items(object_storage_client, create_bucket_request.name)
    delete_pending_buckets[created_buckets].remove(create_bucket_request.name)


@util.skip_while_rerecording
def test_content_type_with_no_multipart(object_storage_client, test_id, delete_pending_buckets):
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkPutMultipartsTest_{}'.format(test_id)
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, create_bucket_request.name)
    object_storage_client.create_bucket(util.NAMESPACE, create_bucket_request)
    delete_pending_buckets[created_buckets].append(create_bucket_request.name)
    content_type = "plaint/text"

    result = invoke([
        'os', 'object', 'bulk-upload',
        '--namespace', util.NAMESPACE,
        '--bucket-name', create_bucket_request.name,
        '--src-dir', root_bulk_put_folder,
        '--no-multipart',
        '--overwrite',
        '--content-type', content_type
    ])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['skipped-objects'] == []
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)

    get_object_result = object_storage_client.get_object(namespace_name=util.NAMESPACE, bucket_name=create_bucket_request.name, object_name="object_1")
    assert get_object_result.headers["content-type"] == content_type

    delete_bucket_and_all_items(object_storage_client, create_bucket_request.name)
    delete_pending_buckets[created_buckets].remove(create_bucket_request.name)


@util.skip_while_rerecording
def test_bulk_put_with_prefix():
    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', bulk_put_bucket_name, '--src-dir', root_bulk_put_folder, '--object-prefix', 'bulk_put_prefix_test/'])

    # No failures or skips and we uploaded everything
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['skipped-objects'] == []
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)

    result = invoke([
        'os', 'object', 'bulk-upload',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bulk_put_bucket_name,
        '--src-dir', root_bulk_put_folder,
        '--object-prefix', 'bulk_put_prefix_test/', '--overwrite', '--verify-checksum'
    ])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['skipped-objects'] == []
    assert len(parsed_result['uploaded-objects']) == get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)
    for uploaded_object_name in parsed_result['uploaded-objects']:
        assert "md5 checksum matches" in parsed_result['uploaded-objects'][uploaded_object_name]['verify-md5-checksum']

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
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['skipped-objects'] == []

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
    parsed_dry_run_result = util.parse_json_response_from_mixed_output(result.output)
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
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
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
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['skipped-objects'] == []

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
    parsed_dry_run_result = util.parse_json_response_from_mixed_output(result.output)
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
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
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


def test_bulk_get_when_bucket_name_is_invalid(vcr_fixture, debug):
    """
    Run the bulk-download command using an invalid bucket name and validate that it throws a ServiceError
    """

    invalid_bucket_name = 'invalid_bucket'
    result = invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name',
                     invalid_bucket_name, '--download-dir', bulk_get_bucket_name_recorded, '--dry-run'], debug=debug)
    assert 'ServiceError:' in result.output
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['status'] == 404
    assert parsed_result['code'] == 'BucketNotFound'

    result = invoke(['os', 'object', 'bulk-download', '--namespace', util.NAMESPACE, '--bucket-name',
                     invalid_bucket_name, '--download-dir', bulk_get_bucket_name_recorded], debug=debug)
    assert 'ServiceError:' in result.output
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['status'] == 404
    assert parsed_result['code'] == 'BucketNotFound'


@util.skip_while_rerecording
def test_bulk_put_when_bucket_name_is_invalid(debug):
    """
    Run the bulk-upload command using an invalid bucket name and validate that it throws a ServiceError
    """

    invalid_bucket_name = 'invalid_bucket'
    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name',
                     invalid_bucket_name, '--src-dir', root_bulk_put_folder, '--dry-run'], debug=debug)
    assert 'ServiceError:' in result.output
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['status'] == 404
    assert parsed_result['code'] == 'BucketNotFound'

    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name',
                     invalid_bucket_name, '--src-dir', root_bulk_put_folder], debug=debug)
    assert 'ServiceError:' in result.output
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['status'] == 404
    assert parsed_result['code'] == 'BucketNotFound'


def test_delete_when_no_objects_in_bucket(vcr_fixture, object_storage_client, test_id_recorded, delete_pending_buckets):
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkDelete_{}'.format(test_id_recorded)
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    object_storage_client.create_bucket(util.NAMESPACE, create_bucket_request)
    delete_pending_buckets[created_buckets].append(create_bucket_request.name)

    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', create_bucket_request.name])
    assert 'There are no objects to delete in {}'.format(create_bucket_request.name) in result.output
    delete_bucket_and_all_items(object_storage_client, create_bucket_request.name)
    delete_pending_buckets[created_buckets].remove(create_bucket_request.name)


def test_delete_dry_run(vcr_fixture):
    # Dry-run against entire bucket
    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name_recorded, '--dry-run'])
    parsed_result = json.loads(result.output)
    assert set(parsed_result['deleted-objects']) == set(bulk_get_object_to_content.keys())

    # Dry-run against a folder and all subfolders
    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name_recorded, '--prefix', 'a/b/', '--dry-run'])
    parsed_result = json.loads(result.output)
    expected_objects = set().union(bulk_get_prefix_to_object['a/b'], bulk_get_prefix_to_object['a/b/c'], bulk_get_prefix_to_object['a/b/c/d'])
    assert set(parsed_result['deleted-objects']) == expected_objects

    # Dry-run against a folder and no subfolders
    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name_recorded, '--prefix', 'a/b/', '--delimiter', '/', '--dry-run'])
    parsed_result = json.loads(result.output)
    assert set(parsed_result['deleted-objects']) == set(bulk_get_prefix_to_object['a/b'])


@util.skip_while_rerecording
def test_delete(object_storage_client, test_id, delete_pending_buckets):
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageBulkDelete_{}'.format(test_id)
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, create_bucket_request.name)
    object_storage_client.create_bucket(util.NAMESPACE, create_bucket_request)
    delete_pending_buckets[created_buckets].append(create_bucket_request.name)

    invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', create_bucket_request.name, '--src-dir', root_bulk_put_folder])
    num_objects_to_delete = get_count_of_files_in_folder_and_subfolders(root_bulk_put_folder)

    # Sanity check that the bucket has things in it
    assert get_number_of_objects_in_bucket(object_storage_client, create_bucket_request.name) > 0

    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', create_bucket_request.name])

    assert "at least" in result.output
    assert str(min(1000, num_objects_to_delete)) in result.output
    assert "objects" in result.output

    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', create_bucket_request.name, '--force'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['delete-failures'] == {}
    assert len(parsed_result['deleted-objects']) == num_objects_to_delete

    # Check that the bucket is now empty
    assert get_number_of_objects_in_bucket(object_storage_client, create_bucket_request.name) == 0

    delete_bucket_and_all_items(object_storage_client, create_bucket_request.name)
    delete_pending_buckets[created_buckets].remove(create_bucket_request.name)


@util.skip_while_rerecording
def test_bulk_operation_table_output_query(object_storage_client, test_id, delete_pending_buckets):
    create_bucket_request = oci.object_storage.models.CreateBucketDetails()
    create_bucket_request.name = 'ObjectStorageTableOutput_{}'.format(test_id)
    create_bucket_request.compartment_id = util.COMPARTMENT_ID
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, create_bucket_request.name)
    object_storage_client.create_bucket(util.NAMESPACE, create_bucket_request)
    delete_pending_buckets[created_buckets].append(create_bucket_request.name)

    result = invoke(['os', 'object', 'bulk-upload', '--namespace', util.NAMESPACE, '--bucket-name', create_bucket_request.name, '--src-dir', root_bulk_put_folder, '--output', 'table', '--query', "[?action=='Uploaded'].{file: name, \"opc-content-md5\": \"opc-content-md5\"}"])
    assert 'file' in result.output
    assert 'opc-content-md5' in result.output
    assert 'etag' not in result.output

    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--dry-run', '--output', 'table'])
    assert 'action' in result.output
    assert 'name' in result.output
    assert 'type' in result.output
    assert '/a/Object_1' in result.output

    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name, '--dry-run', '--output', 'table', '--query', "[?name=='Object_0'][name]"])
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
    delete_pending_buckets[created_buckets].remove(create_bucket_request.name)
    shutil.rmtree(target_download_folder)


def generate_data_bulk_delete_object(object_storage_client, bucket_name,
                                     count=OBJECTS_TO_CREATE_IN_BUCKET_FOR_BULK_GET):
    # Create items at various heirarchy levels (to be surfaced as different directories on disk)
    for i in range(count):
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
        object_storage_client.put_object(util.NAMESPACE, bucket_name, object_name, object_content)


def test_bulk_delete_versions_when_no_objects_in_bucket(vcr_fixture, object_storage_client, debug, test_id_recorded):
    bucket_name = 'ObjectStorageBulkDeleteVersions_{}'.format(test_id_recorded)
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bucket_name)

    # bucket create with versioning enabled
    result = invoke(['os', 'bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name',
                     bucket_name, '--versioning', 'Enabled'], debug=debug)
    validate_response(result, includes_debug_data=debug)

    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name])
    assert 'There are no objects to delete in {}'.format(bucket_name) in result.output

    object_storage_client.delete_bucket(util.NAMESPACE, bucket_name)


def test_bulk_delete_versions_dry_run(vcr_fixture, object_storage_client, debug, test_id_recorded):
    bucket_name = 'ObjectStorageBulkDeleteVersions_{}'.format(test_id_recorded)
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bucket_name)

    # bucket create with versioning enabled
    result = invoke(['os', 'bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name',
                     bucket_name, '--versioning', 'Enabled'], debug=debug)
    validate_response(result, includes_debug_data=debug)

    generate_data_bulk_delete_object(object_storage_client, bucket_name)

    num_versions_to_delete = get_number_of_versions_in_bucket(object_storage_client, bucket_name, None)

    # Dry-run with both --object-name and --prefix; bulk-delete-versions doesn't support this operation
    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bulk_get_bucket_name,
                     '--object-name', 'Object_1', '--prefix', 'O', '--dry-run'])
    assert 'UsageError' in result.output
    assert 'The --object-name parameter cannot be combined with either --prefix or --include or --exclude' in result.output

    # Dry-run against entire bucket
    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--dry-run'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['delete-failures'] == {}
    assert len(parsed_result['deleted-objects']) == num_versions_to_delete

    # Dry-run against a folder and all subfolders
    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--prefix', 'a/b/', '--dry-run'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    expected_objects = set().union(bulk_get_prefix_to_object['a/b'], bulk_get_prefix_to_object['a/b/c'], bulk_get_prefix_to_object['a/b/c/d'])
    assert len(parsed_result['deleted-objects']) == len(expected_objects)

    # Dry-run against a folder and no subfolders
    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--prefix', 'a/b/', '--delimiter', '/', '--dry-run'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['delete-failures'] == {}

    # Dry-run with a single object-name
    num_object_name_versions = get_number_of_versions_in_bucket(object_storage_client, bucket_name, 'Object_5')
    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--object-name', 'Object_5', '--dry-run'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert len(parsed_result['deleted-objects']) == num_object_name_versions

    # delete-versions after --dry-run test
    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--force'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['delete-failures'] == {}
    assert len(parsed_result['deleted-objects']) == num_versions_to_delete

    object_storage_client.delete_bucket(util.NAMESPACE, bucket_name)


# Test bulk-delete-versions full functionality
def test_bulk_delete_versions(vcr_fixture, object_storage_client, debug, test_id_recorded):
    bucket_name = 'ObjectStorageBulkDeleteVersions_{}'.format(test_id_recorded)
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bucket_name)

    # bucket create with versioning enabled
    result = invoke(['os', 'bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name',
                     bucket_name, '--versioning', 'Enabled'], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # generate object-names
    generate_data_bulk_delete_object(object_storage_client, bucket_name)
    # generate versions
    generate_data_bulk_delete_object(object_storage_client, bucket_name)
    num_versions_to_delete = get_number_of_versions_in_bucket(object_storage_client, bucket_name, None)

    # Sanity check that the bucket has things in it
    assert num_versions_to_delete > 0

    # --- Delete rest of the versions
    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name])

    assert "at least" in result.output
    assert str(min(1000, num_versions_to_delete)) in result.output
    assert "object versions" in result.output

    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--force'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['delete-failures'] == {}
    assert len(parsed_result['deleted-objects']) == num_versions_to_delete

    # Check that the bucket is now empty
    assert get_number_of_versions_in_bucket(object_storage_client, bucket_name, None) == 0

    object_storage_client.delete_bucket(util.NAMESPACE, bucket_name)


def test_basic_bulk_delete_versions_object_name(vcr_fixture, object_storage_client, debug, test_id_recorded):
    bucket_name = 'ObjectStorageBulkDeleteVersions_{}'.format(test_id_recorded)
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bucket_name)

    result = invoke(['os', 'bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name',
                     bucket_name, '--versioning', 'Enabled'], debug=debug)
    validate_response(result, includes_debug_data=debug)

    object_content = generate_random_string(CONTENT_STRING_LENGTH_SHORT)
    object_storage_client.put_object(util.NAMESPACE, bucket_name, 'Object_1', object_content)
    object_storage_client.put_object(util.NAMESPACE, bucket_name, 'Object_2', object_content)
    object_storage_client.put_object(util.NAMESPACE, bucket_name, 'Object_3', object_content)

    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--object-name', 'Object_1', '--force'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['delete-failures'] == {}
    assert len(parsed_result['deleted-objects']) == 1

    # test if only first object has been deleted
    result = invoke(['os', 'object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name])
    assert "Object_2" in result.output
    assert "Object_3" in result.output

    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--force'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['delete-failures'] == {}
    assert len(parsed_result['deleted-objects']) == 2

    # Check that the bucket is now empty
    assert get_number_of_versions_in_bucket(object_storage_client, bucket_name, None) == 0

    object_storage_client.delete_bucket(util.NAMESPACE, bucket_name)


# [CASPER-13879] Test bulk-delete-versions (test for pagination)
# Try to delete with random object-name not present in bucket such that it hits pagination and loop terminates successfully
# Delete objects placed in different pages, object versions ranging over multiple pages
@util.skip_while_rerecording
def test_bulk_delete_versions_pagination_him(object_storage_client, debug, test_id):
    bucket_name = 'ObjectStorageBulkDeleteVersionsPagination_{}'.format(test_id)
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bucket_name)

    # bucket create with versioning enabled
    result = invoke(['os', 'bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name',
                     bucket_name, '--versioning', 'Enabled'], debug=debug)
    validate_response(result, includes_debug_data=debug)
    num_versions = 1501    # Atleast 3 pages should be created
    object_name_present_1 = 'Object.txt'
    object_name_present_2 = 'TestObject.pdf'

    for i in range(num_versions):
        object_content = generate_random_string(CONTENT_STRING_LENGTH_SHORT)
        object_storage_client.put_object(util.NAMESPACE, bucket_name, object_name_present_1, object_content)
        object_storage_client.put_object(util.NAMESPACE, bucket_name, object_name_present_2, object_content)

    # Adding 3 random objects(one each of txt/pdf extension) at 3 different places in the list
    object_content = generate_random_string(CONTENT_STRING_LENGTH_SHORT)
    object_storage_client.put_object(util.NAMESPACE, bucket_name, "arandom.txt", object_content)
    object_storage_client.put_object(util.NAMESPACE, bucket_name, "arandom.pdf", object_content)

    object_content = generate_random_string(CONTENT_STRING_LENGTH_SHORT)
    object_storage_client.put_object(util.NAMESPACE, bucket_name, "random.txt", object_content)
    object_storage_client.put_object(util.NAMESPACE, bucket_name, "random.pdf", object_content)

    object_content = generate_random_string(CONTENT_STRING_LENGTH_SHORT)
    object_storage_client.put_object(util.NAMESPACE, bucket_name, "zrandom.txt", object_content)
    object_storage_client.put_object(util.NAMESPACE, bucket_name, "zrandom.pdf", object_content)

    # Deleting an object not present in bucket
    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--object-name', "absentobject.pdf"])
    confirm_prompt = 'There are no objects to delete in {}'.format(bucket_name)
    assert confirm_prompt in result.output

    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--object-name', "absentobject.txt", '--force'])
    assert '' in result.output

    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--prefix', 'absent'])
    confirm_prompt = 'There are no objects to delete in {}'.format(bucket_name)
    assert confirm_prompt in result.output

    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--prefix', 'absent', '--force'])
    assert '' in result.output

    # Deleting the single object versions present in different pages using object names and prefixes
    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--object-name', "arandom.txt"])

    assert "delete at least" in result.output
    assert "1" in result.output
    assert "object versions" in result.output

    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--object-name', "arandom.txt", '--force'])

    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert len(parsed_result['deleted-objects']) == 1

    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--object-name', "random.txt"])

    assert "delete at least" in result.output
    assert "1" in result.output
    assert "object versions" in result.output

    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--object-name', "random.txt", '--force'])

    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert len(parsed_result['deleted-objects']) == 1

    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--object-name', "zrandom.txt"])

    assert "delete at least" in result.output
    assert "1" in result.output
    assert "object versions" in result.output

    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--object-name', "zrandom.txt", '--force'])

    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert len(parsed_result['deleted-objects']) == 1

    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--prefix', "arandom"])

    assert "delete at least" in result.output
    assert "1" in result.output
    assert "object versions" in result.output

    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--prefix', "arandom", '--force'])

    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert len(parsed_result['deleted-objects']) == 1

    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--prefix', "random"])

    assert "delete at least" in result.output
    assert "1" in result.output
    assert "object versions" in result.output

    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--prefix', "random", '--force'])

    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert len(parsed_result['deleted-objects']) == 1

    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--prefix', "zrandom"])

    assert "delete at least" in result.output
    assert "1" in result.output
    assert "object versions" in result.output

    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--prefix', "zrandom", '--force'])

    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert len(parsed_result['deleted-objects']) == 1

    # Deleting objects such that versions exist in more than one page using object name
    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--object-name', object_name_present_1])

    assert "delete at least" in result.output
    assert "1000" in result.output
    assert "object versions" in result.output

    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--object-name', object_name_present_1, '--force'])

    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert len(parsed_result['deleted-objects']) == num_versions

    # Deleting objects such that versions exist in more than one page using prefix
    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--prefix', 'Test'])

    assert "delete at least" in result.output
    assert "1000" in result.output
    assert "object versions" in result.output

    result = invoke(['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--prefix', 'Test', '--force'])

    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert len(parsed_result['deleted-objects']) == num_versions

    assert get_number_of_versions_in_bucket(object_storage_client, bucket_name, None) == 0

    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bucket_name)


# [CASPER-13879] Test bulk-delete-versions (test for pagination)
# Delete objects placed in different pages with include/exclude options, Also object versions ranging over multiple pages
@util.skip_while_rerecording
def test_bulk_delete_versions_pagination_include_exclude(object_storage_client, debug, test_id):
    bucket_name = 'ObjectStorageBulkDeleteVersionsPaginationIncludeExclude{}'.format(test_id)
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bucket_name)

    # bucket create with versioning enabled
    result = invoke(['os', 'bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name',
                     bucket_name, '--versioning', 'Enabled'], debug=debug)
    validate_response(result, includes_debug_data=debug)
    num_versions = 100
    extensions = ['pdf', 'txt', 'html', 'csv']
    pdf_array = []
    for i in range(26):
        object_content = generate_random_string(CONTENT_STRING_LENGTH_SHORT)
        ext = random.choice(extensions)
        obj_name = chr(ord('a') + i) + '_object.' + ext
        if ext == 'pdf':
            pdf_array.append(obj_name)
        for j in range(num_versions):
            object_storage_client.put_object(util.NAMESPACE, bucket_name, obj_name, object_content)

    # Delete objects with inclusions - dry-run
    result = invoke([
        'os', 'object', 'bulk-delete-versions',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bucket_name,
        '--include', '*.pdf',
        '--dry-run'
    ])
    parsed_dry_run_result = util.parse_json_response_from_mixed_output(result.output)
    assert len(parsed_dry_run_result['deleted-objects']) == len(pdf_array) * num_versions
    parsed_result_with_object_names = [i.split(',')[0] for i in parsed_dry_run_result['deleted-objects']]
    assert set(parsed_result_with_object_names) == set(pdf_array)

    # Delete objects with exclusions - dry-run
    result = invoke([
        'os', 'object', 'bulk-delete-versions',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bucket_name,
        '--exclude', '*.txt',
        '--exclude', '*.html',
        '--exclude', '*.csv',
        '--dry-run'
    ])
    parsed_dry_run_result = util.parse_json_response_from_mixed_output(result.output)
    assert len(parsed_dry_run_result['deleted-objects']) == len(pdf_array) * num_versions
    parsed_result_with_object_names = [i.split(',')[0] for i in parsed_dry_run_result['deleted-objects']]
    assert set(parsed_result_with_object_names) == set(pdf_array)

    result = invoke([
        'os', 'object', 'bulk-delete-versions',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bucket_name,
        '--include', '*.pdf',
        '--force'
    ])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['delete-failures'] == {}
    parsed_result_with_object_names = [i.split(',')[0] for i in parsed_result['deleted-objects']]
    assert set(parsed_result_with_object_names) == set(pdf_array)

    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bucket_name)


# [CASPER-13879] Test bulk-delete with prefi/include/exclude option ~ multiple object names(test for pagination)
# Creating multiple objects with different extensions and names such that objects to be deleted exist in multiple pages
@util.skip_while_rerecording
def test_bulk_delete_pagination(object_storage_client, debug, test_id):
    bucket_name = 'ObjectStorageBulkDeletePagination_{}'.format(test_id)
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bucket_name)

    result = invoke(['os', 'bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name',
                     bucket_name], debug=debug)
    validate_response(result, includes_debug_data=debug)

    object_content = generate_random_string(CONTENT_STRING_LENGTH_SHORT)
    object_storage_client.put_object(util.NAMESPACE, bucket_name, "random.txt", object_content)     # For checking delete with prefix

    num_obj_with_alpha = 100
    extensions = ['pdf', 'txt', 'html', 'csv']
    pdf_array = []
    for i in range(26):
        for j in range(num_obj_with_alpha):
            object_content = generate_random_string(CONTENT_STRING_LENGTH_SHORT)
            ext = random.choice(extensions)
            obj_name = chr(ord('a') + i) + '_object' + str(j) + '.' + ext
            if ext == 'pdf':
                pdf_array.append(obj_name)
            object_storage_client.put_object(util.NAMESPACE, bucket_name, obj_name, object_content)

    # Delete object which does not exist in bucket using prefix
    result = invoke(
        ['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--prefix', "zyxwvu"])
    confirm_prompt = 'There are no objects to delete in {}'.format(bucket_name)
    assert confirm_prompt in result.output

    result = invoke(
        ['os', 'object', 'bulk-delete-versions', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--prefix', "uvxyz", '--force'])
    assert '' in result.output

    # Delete object such that it heats pagination
    result = invoke(
        ['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
         '--prefix', "random"])

    assert "delete at least" in result.output
    assert "1" in result.output
    assert "objects" in result.output

    # Delete objects on multiple pages with inclusions
    result = invoke([
        'os', 'object', 'bulk-delete',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bucket_name,
        '--include', '*.pdf',
        '--dry-run'
    ])
    parsed_dry_run_result = util.parse_json_response_from_mixed_output(result.output)
    assert len(parsed_dry_run_result['deleted-objects']) == len(pdf_array)
    assert set(parsed_dry_run_result['deleted-objects']) == set(pdf_array)

    # Delete objects with exclusions - dry-run
    result = invoke([
        'os', 'object', 'bulk-delete',
        '--namespace', util.NAMESPACE,
        '--bucket-name', bucket_name,
        '--exclude', '*.txt',
        '--exclude', '*.html',
        '--exclude', '*.csv',
        '--dry-run'
    ])
    parsed_dry_run_result = util.parse_json_response_from_mixed_output(result.output)
    assert len(parsed_dry_run_result['deleted-objects']) == len(pdf_array)
    assert set(parsed_dry_run_result['deleted-objects']) == set(pdf_array)

    result = invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--include', '*.pdf', '--force'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['delete-failures'] == {}
    parsed_result_with_object_names = [i.split(',')[0] for i in parsed_result['deleted-objects']]
    assert set(parsed_result_with_object_names) == set(pdf_array)

    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bucket_name)


def test_delete_bucket_empty_dry_run(object_storage_client, debug, test_id_recorded, on_error_fixture):
    bucket_name = 'ObjectStorageBucketDelete_{}'.format(test_id_recorded)
    bucket_delete_test_helper(object_storage_client, bucket_name, debug, test_id_recorded, on_error_fixture)


@util.skip_while_rerecording
def test_delete_bucket_empty_dry_run_versioned(object_storage_client, debug, test_id, on_error_fixture):
    bucket_name = 'ObjectStorageBucketDelete_Versioned_{}'.format(test_id)
    bucket_delete_test_helper(object_storage_client, bucket_name, debug, test_id, on_error_fixture, is_versioned=True)


def bucket_delete_test_helper(object_storage_client, source_bucket_name, debug, test_id, on_error_fixture, is_versioned=False):
    # this is a test helper for bucket delete command. It tests and validates the output from --dry-run as well
    # as --empty along with the prompts
    clear_and_create_new_bucket(object_storage_client, source_bucket_name, debug, is_versioned)
    on_error_fixture[created_buckets].append(source_bucket_name)
    # create a bucket in a different region
    dest_bucket_name = 'ObjectStorageBucketDelete_Rep_{}'.format(test_id)
    if is_versioned:
        dest_bucket_name = 'ObjectStorageBucketDelete_Versioned_Rep_{}'.format(test_id)
    n_pars, n_uploads = 10, 10

    # create replication bucket
    create_replication_bucket(dest_bucket_name, debug)
    on_error_fixture[created_buckets].append(dest_bucket_name)
    generate_all_data_in_bucket(object_storage_client, source_bucket_name, debug, dest_bucket_name, n_pars, n_uploads,
                                True, is_versioned)
    if is_versioned:
        n_objects = get_number_of_versions_in_bucket(object_storage_client, source_bucket_name, None)
    else:
        n_objects = get_number_of_objects_in_bucket(object_storage_client, source_bucket_name)
    # Sanity check that the bucket has things in it
    assert n_objects > 0

    # Dry-run without specifying empty first should result in an error
    result = invoke(
        ['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', source_bucket_name, '--dry-run'])
    assert 'UsageError' in result.output
    assert '--empty' in result.output

    # Dry-run for the whole bucket
    result = invoke(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', source_bucket_name,
                     '--empty', '--dry-run'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    verify_bucket_delete_output(parsed_result, n_objects, n_pars, n_uploads)

    # delete bucket after --dry-run test, use --empty with force for actual deletion without prompt
    result = invoke(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', source_bucket_name,
                     '--empty', '--force'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    verify_bucket_delete_output(parsed_result, n_objects, n_pars, n_uploads)
    assert_that_bucket_is_deleted(source_bucket_name, debug)
    on_error_fixture[created_buckets].remove(source_bucket_name)

    clean_up_replication_bucket(dest_bucket_name, debug)
    on_error_fixture[test_success] = True


@util.skip_while_rerecording
def test_delete_bucket_without_objects(object_storage_client, debug, test_id):
    bucket_name = 'ObjectStorageBucketDelete_WithoutObjects_{}'.format(test_id)
    clear_and_create_new_bucket(object_storage_client, bucket_name, debug)

    result = invoke(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name])
    assert 'Are you sure you want to delete this bucket?' in result.output

    result = invoke(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--force'])
    assert result.output == ''

    assert_that_bucket_is_deleted(bucket_name, debug)


@util.skip_while_rerecording
def test_delete_bucket_with_par_rep_policy_uploads_but_no_objects(object_storage_client, debug, test_id, on_error_fixture):
    bucket_name = 'ObjectStorageBucketDelete_WithoutObject_WithParUploadRepPolicy_{}'.format(test_id)

    clear_and_create_new_bucket(object_storage_client, bucket_name, debug)
    on_error_fixture[created_buckets].append(bucket_name)

    rep_policy_dest_bucket = 'ObjectStorageBucketDelete_WithoutObjects_WithParUploadRepPolicy_Rep_{}'.format(test_id)
    create_replication_bucket(rep_policy_dest_bucket, debug)
    on_error_fixture[created_buckets].append(rep_policy_dest_bucket)
    generate_all_data_in_bucket(object_storage_client, bucket_name, debug, rep_policy_dest_bucket, 10, 10, False, False)

    # delete bucket after --dry-run test, use --empty with force for actual deletion without prompt
    result = invoke(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--empty', '--force'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    verify_bucket_delete_output(parsed_result, 0, 10, 10)
    assert_that_bucket_is_deleted(bucket_name, debug)
    on_error_fixture[created_buckets].remove(bucket_name)

    # clean up the replication bucket
    clean_up_replication_bucket(rep_policy_dest_bucket, debug)
    on_error_fixture[test_success] = True


@util.skip_while_rerecording
def test_delete_bucket_with_objects_paging(object_storage_client, debug, test_id):
    bucket_name = 'ObjectStorageBucketDelete_Paging_{}'.format(test_id)
    clear_and_create_new_bucket(object_storage_client, bucket_name, debug)

    objects_to_create = 1100
    for i in range(objects_to_create):
        object_name = 'Object_{}'.format(i)
        object_content = generate_random_string(CONTENT_STRING_LENGTH_SHORT)
        object_storage_client.put_object(util.NAMESPACE, bucket_name, object_name, object_content)

    no_of_objects_from_list = get_number_of_objects_in_bucket(object_storage_client, bucket_name)
    assert no_of_objects_from_list == objects_to_create

    # delete bucket after --dry-run test, use --empty with force for actual deletion without prompt
    result = invoke(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--empty'])
    assert 'pre-authenticated requests' in result.output

    result = invoke(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--empty',
                    '--force'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    verify_bucket_delete_output(parsed_result, no_of_objects_from_list, 0, 0, 0)
    assert_that_bucket_is_deleted(bucket_name, debug)


@util.skip_while_rerecording
def test_delete_bucket_with_object_versions_paging(object_storage_client, debug, test_id):
    bucket_name = 'ObjectStorageBucketDelete_Versioned_Paging_{}'.format(test_id)
    clear_and_create_new_bucket(object_storage_client, bucket_name, debug, is_versioned=True)

    num_versions = 1100
    object_name = 'Object_103'
    object_content = generate_random_string(CONTENT_STRING_LENGTH_SHORT)
    for i in range(num_versions):
        object_storage_client.put_object(util.NAMESPACE, bucket_name, object_name, object_content)

    no_of_object_versions = get_number_of_versions_in_bucket(object_storage_client, bucket_name, object_name)
    assert no_of_object_versions == num_versions

    # delete bucket after --dry-run test, use --empty with force for actual deletion without prompt
    result = invoke(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--empty'])
    assert 'pre-authenticated requests' in result.output

    result = invoke(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--empty',
                     '--force'])
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    verify_bucket_delete_output(parsed_result, no_of_object_versions, 0, 0, 0)
    assert_that_bucket_is_deleted(bucket_name, debug)


@util.skip_while_rerecording
def test_clear_test_data_util_with_same_prefix(object_storage_client, debug, test_id):
    bucket_prefix = f'ObjectStorageClearTest{test_id}'
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bucket_prefix)

    # create a non versioned bucket
    bucket_1 = "{}Bucket_{}".format(bucket_prefix, test_id)
    result = invoke(['os', 'bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID,
                     '--name', bucket_1], debug=debug)
    validate_response(result, includes_debug_data=debug)
    generate_data_bulk_delete_object(object_storage_client, bucket_1, 10)

    # create a versioned bucket
    bucket_2 = "{}VersionedBucket_{}".format(bucket_prefix, test_id)
    result = invoke(['os', 'bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID,
                     '--name', bucket_2, '--versioning', 'Enabled'], debug=debug)
    validate_response(result, includes_debug_data=debug)
    generate_data_bulk_delete_object(object_storage_client, bucket_2, 10)
    generate_data_bulk_delete_object(object_storage_client, bucket_2, 10)

    # clear both the buckets
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bucket_prefix)

    # verify that no bucket exists
    assert_that_bucket_is_deleted(bucket_1, debug)
    assert_that_bucket_is_deleted(bucket_2, debug)


@util.skip_while_rerecording
def test_clear_test_data_util_with_different_prefix(object_storage_client, debug, test_id):
    common_prefix = f'ObjectStorageClearTest{test_id}'
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, common_prefix)

    # try to create a random bucket with prefix and versioning
    idx_with_diff_prefix = random.randint(0, 2)
    idx_with_versioning = random.randint(0, 2)
    bucket_names = []
    for idx in range(3):
        bucket_prefix = common_prefix + 'FirstPrefix'
        if idx == idx_with_diff_prefix:
            bucket_prefix = common_prefix + 'SecondPrefix'
        # create a non versioned bucket
        bucket_name = "{}Bucket_{}_{}".format(bucket_prefix, idx, test_id)
        bucket_names.append(bucket_name)
        command = ['os', 'bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID,
                   '--name', bucket_name]
        if idx == idx_with_versioning:
            command.extend(['--versioning', 'Enabled'])
        result = invoke(command, debug=debug)
        validate_response(result, includes_debug_data=debug)
        generate_data_bulk_delete_object(object_storage_client, bucket_name, 10)
        if idx == idx_with_versioning:
            generate_data_bulk_delete_object(object_storage_client, bucket_name, 10)

    # clear the buckets with first prefix
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, common_prefix + 'FirstPrefix')

    # verify that no bucket with the prefix exist
    for idx, bucket_name in enumerate(bucket_names):
        # validate and clear the bucket with second prefix
        if 'SecondPrefix' in bucket_name:
            assert_that_bucket_exists(bucket_name, debug)
            util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, common_prefix + 'SecondPrefix')
            assert_that_bucket_is_deleted(bucket_name, debug)
        else:
            assert_that_bucket_is_deleted(bucket_name, debug)


def assert_that_bucket_is_deleted(bucket_name, debug, region=None):
    parsed_result = get_bucket_with_region(bucket_name, debug, region)

    assert parsed_result.get('status') is not None
    assert parsed_result['status'] == 404
    assert parsed_result['code'] == 'BucketNotFound'


def assert_that_bucket_exists(bucket_name, debug, region=None):
    parsed_result = get_bucket_with_region(bucket_name, debug, region)

    assert parsed_result.get('data') is not None
    assert parsed_result['data'].get('name') is not None
    assert parsed_result['data']['name'] == bucket_name


def get_bucket_with_region(bucket_name, debug, region):
    command = ['os', 'bucket', 'get', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name]
    if region:
        command.extend(['--region', region])
    result = invoke(command, debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    return parsed_result


def clear_and_create_new_bucket(object_storage_client, bucket_name, debug, is_versioned=False):
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bucket_name)
    command = ['os', 'bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID,
               '--name', bucket_name]
    if is_versioned:
        command.extend(['--versioning', 'Enabled'])
    result = invoke(command, debug=debug)
    validate_response(result, includes_debug_data=debug)


def delete_test_bucket_on_failure(bucket_name):
    invoke(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--empty', '--force'])


def clean_up_replication_bucket(rep_bucket_name, debug):
    parsed_result = get_bucket_with_region(rep_bucket_name, debug, util.OS_REPLICATION_DESTINATION_REGION)
    if parsed_result.get('data'):
        print('Cleaning up replication bucket: {}'.format(rep_bucket_name))
        invoke(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name',
                rep_bucket_name, '--empty', '--force', '--region', util.OS_REPLICATION_DESTINATION_REGION])
        assert_that_bucket_is_deleted(rep_bucket_name, debug, region=util.OS_REPLICATION_DESTINATION_REGION)


def generate_all_data_in_bucket(object_storage_client, bucket_name, debug, rep_bucket_name, n_pars, n_upload,
                                generate_objects, is_versioned):
    if generate_objects:
        # generate object names
        generate_data_bulk_delete_object(object_storage_client, bucket_name, 10)
        if is_versioned:
            # generate object versions by overwriting the same data
            generate_data_bulk_delete_object(object_storage_client, bucket_name, 10)
    generate_data_preauth_request(object_storage_client, bucket_name, n_pars)
    generate_data_replication_policy(object_storage_client, bucket_name, rep_bucket_name)
    generate_data_multipart_upload(object_storage_client, bucket_name, n_upload)


def create_replication_bucket(rep_bucket_name, debug):
    clean_up_replication_bucket(rep_bucket_name, debug)
    result = invoke(['os', 'bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name',
                     rep_bucket_name, '--region', util.OS_REPLICATION_DESTINATION_REGION], debug=debug)
    validate_response(result, includes_debug_data=debug)


def verify_bucket_delete_output(parsed_result, num_objects_to_delete, no_of_pars_to_create, no_of_multipart_uploads,
                                no_of_rep_policy=1):
    for key in parsed_result.keys():
        assert parsed_result[key]['delete-failures'] == {}
        objects_ = parsed_result[key]['deleted-objects']
        if key == 'object':
            assert len(objects_) == num_objects_to_delete
        elif key == 'preauth-request':
            assert len(objects_) == no_of_pars_to_create
        elif key == 'multipart-upload':
            assert len(objects_) == no_of_multipart_uploads
        else:
            assert len(objects_) == no_of_rep_policy


def generate_data_preauth_request(object_storage_client, bucket_name, no_of_objects):
    for i in range(no_of_objects):
        create_par_request = CreatePreauthenticatedRequestDetails()
        create_par_request.name = "test_par_" + str(i)
        if i % 5 == 4:
            create_par_request.access_type = CreatePreauthenticatedRequestDetails.ACCESS_TYPE_ANY_OBJECT_WRITE
            create_par_request.bucket_listing_action = "Deny"
        elif i % 5 == 3:
            create_par_request.access_type = CreatePreauthenticatedRequestDetails.ACCESS_TYPE_ANY_OBJECT_READ
            create_par_request.bucket_listing_action = "ListObjects"
        elif i % 5 == 2:
            create_par_request.access_type = CreatePreauthenticatedRequestDetails.ACCESS_TYPE_ANY_OBJECT_READ_WRITE
            create_par_request.bucket_listing_action = "ListObjects"
        elif i % 5 == 1:
            create_par_request.access_type = CreatePreauthenticatedRequestDetails.ACCESS_TYPE_ANY_OBJECT_READ_WRITE
            create_par_request.bucket_listing_action = "ListObjects"
            create_par_request.object_name = "prefix/"
        else:
            create_par_request.access_type = CreatePreauthenticatedRequestDetails.ACCESS_TYPE_OBJECT_READ_WRITE
            create_par_request.object_name = "Object_{}".format(i)

        create_par_request.time_expires = datetime.datetime.now() + datetime.timedelta(days=1)
        object_storage_client.create_preauthenticated_request(util.NAMESPACE, bucket_name, create_par_request)


def generate_data_replication_policy(object_storage_client, source_bucket, destination_bucket):
    # create one replication policy per bucket
    create_rep_policy_request = CreateReplicationPolicyDetails()
    create_rep_policy_request.name = "test_rep_policy"
    create_rep_policy_request.destination_region_name = util.OS_REPLICATION_DESTINATION_REGION
    create_rep_policy_request.destination_bucket_name = destination_bucket
    object_storage_client.create_replication_policy(util.NAMESPACE, source_bucket, create_rep_policy_request)


def generate_data_multipart_upload(object_storage_client, bucket_name, no_of_objects):
    for i in range(no_of_objects):
        create_multipart_upload_request = CreateMultipartUploadDetails()
        create_multipart_upload_request.object = "Object_{}".format(i)
        object_storage_client.create_multipart_upload(util.NAMESPACE, bucket_name, create_multipart_upload_request)


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


# For the bulk operations, object names are taken from the file path of the thing we uploaded. Normalize to
# / in the paths (Windows can go both ways) then chop the front bit off
def get_object_name_from_path(path_root, full_path):
    return full_path.replace(os.sep, '/').replace(path_root + '/', '')


def delete_bucket_and_all_items(object_storage_client, bucket_name):
    util.invoke_command(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--empty', '--force'])


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


def get_number_of_versions_in_bucket(object_storage_client, bucket_name, object_name):
    list_object_versions_responses = oci_cli_object_storage.objectstorage_cli_extended.retrying_list_object_versions(
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
        page=None,
        retrieve_all=True
    )
    num_versions_in_bucket = 0
    for response in list_object_versions_responses:
        # To avoid slowness if object_name is not provided
        if object_name:
            for obj in response.data.items:
                if object_name != obj.name:
                    continue
                num_versions_in_bucket = num_versions_in_bucket + 1
        else:
            num_versions_in_bucket = num_versions_in_bucket + len(response.data.items)

    return num_versions_in_bucket


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


def generate_aes256_key_str():
    key = os.urandom(32)
    return base64.b64encode(key).decode('utf-8')


def extra_response_validation(result):
    assert 'opc-client-request-id' in result.output


def validate_response(result, includes_debug_data=False, json_response_expected=True):
    extra_validation = None
    if includes_debug_data:
        extra_validation = extra_response_validation
    util.validate_response(result, extra_validation=extra_validation, includes_debug_data=includes_debug_data,
                           json_response_expected=json_response_expected)
