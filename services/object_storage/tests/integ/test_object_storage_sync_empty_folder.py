# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates. All rights reserved.


import os
import shutil
from pathlib import Path

import pytest

import test_object_storage_bulk_operations as bulk_operation
from test_object_storage_sync_download import parse_dry_run_result
from tests import util
import services.object_storage.tests.common.util as object_storage_util

OBJECTS_TO_CREATE_IN_REMOTE_FOR_SYNC = 20

sync_local_object_content = {}
sync_upload_bucket_name = str()
sync_upload_test_dir = str()
sync_download_test_dir = str()


@pytest.fixture(params=[False])
def debug(request):
    return request.param


@pytest.fixture(scope='module', autouse=True)
def generate_files_in_local(object_storage_client, test_id):
    global sync_upload_bucket_name, sync_upload_test_dir, sync_download_test_dir

    print('Setting up the test bucket for sync upload..')
    sync_upload_bucket_name = 'ObjectStorageEmptySyncUploadTest_{}'.format(test_id)
    sync_upload_test_dir = 'tests/temp/sync_empty_upload_{}'.format(test_id)
    sync_download_test_dir = 'tests/temp/sync_empty_download_{}'.format(test_id)
    if os.path.exists(sync_upload_test_dir):
        shutil.rmtree(sync_upload_test_dir)

    Path(sync_upload_test_dir).mkdir(parents=True, exist_ok=False)
    bulk_operation.clear_and_create_new_bucket(object_storage_client, sync_upload_bucket_name, False)

    object_storage_util.create_mixed_dir_at_path(sync_upload_test_dir)

    yield

    print("Tearing down..")
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, sync_upload_bucket_name)

    object_storage_util.remove_dir_at_path(sync_upload_test_dir)
    object_storage_util.remove_dir_at_path(sync_download_test_dir)


sync_remote_prefixes = ['a/b/c/', 'a/b/', 'a/', '']


@pytest.fixture(scope='function')
def generate_content_in_remote(object_storage_client):
    global sync_upload_bucket_name, sync_download_test_dir, sync_upload_bucket_name, sync_upload_test_dir

    print('Setting up the content in remote')
    bulk_operation.clear_and_create_new_bucket(object_storage_client, sync_upload_bucket_name, False)

    for i in range(OBJECTS_TO_CREATE_IN_REMOTE_FOR_SYNC):
        object_name = f'{sync_remote_prefixes[i%4]}Object{i}'
        object_content = bulk_operation.generate_random_string(bulk_operation.CONTENT_STRING_LENGTH)
        object_storage_client.put_object(util.NAMESPACE, sync_upload_bucket_name, object_name, object_content)

        empty_dir = f'{sync_remote_prefixes[i%4]}Empty{i}/'
        object_storage_client.put_object(util.NAMESPACE, sync_upload_bucket_name, empty_dir, None)
    yield
    print("Tearing down remote content..")


def teardown_function():
    bulk_operation.invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name',
                           sync_upload_bucket_name, '--force'], debug=debug)


def check_all_src_files_are_synced(parsed_result, local_path, parent_path=None, files_to_skip={}):
    uploaded_set = parsed_result['uploaded-objects'].keys()
    skipped = parsed_result['skipped-objects']
    upload_failures = parsed_result['upload-failures'].keys()
    all_upload_set = set(uploaded_set)
    if len(files_to_skip):
        assert set(skipped) == set(files_to_skip)
    assert upload_failures == dict.keys({})
    local_files_set = object_storage_util.get_file_set_at_path(local_path, parent_path)
    assert all_upload_set == local_files_set - set(files_to_skip)


@util.skip_while_rerecording
def test_sync_empty_folder_syncs_all_files(test_id):
    bucket_name = sync_upload_bucket_name
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    bucket_name, '--src-dir', sync_upload_test_dir], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    check_all_src_files_are_synced(parsed_result, sync_upload_test_dir)


def test_sync_empty_folder_sync_skip_already_present_file(test_id):
    bucket_name = sync_upload_bucket_name
    # uploading some file
    upload_abs_path = os.path.join(sync_upload_test_dir, 'content_folder', 'content_folder')
    upload_path = os.path.relpath(upload_abs_path, sync_upload_test_dir)
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    bucket_name, '--src-dir', sync_upload_test_dir, '--include', f'{upload_path}*'], debug=debug)

    parsed_result = util.parse_json_response_from_mixed_output(result.output)

    check_all_src_files_are_synced(parsed_result, upload_abs_path, sync_upload_test_dir)

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    bucket_name, '--src-dir', sync_upload_test_dir], debug=debug)

    parsed_result = util.parse_json_response_from_mixed_output(result.output)

    skipped = parsed_result['skipped-objects']
    already_uploaded_local_files = object_storage_util.get_file_set_at_path(upload_abs_path, sync_upload_test_dir, )

    assert already_uploaded_local_files == set(skipped)

    skipped_files_set = object_storage_util.get_file_set_at_path(upload_abs_path, sync_upload_test_dir)

    check_all_src_files_are_synced(parsed_result, sync_upload_test_dir, parent_path=None, files_to_skip=skipped_files_set)


def test_sync_empty_folder_which_has_content_later(test_id):
    bucket_name = sync_upload_bucket_name

    # uploading some file
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    bucket_name, '--src-dir', sync_upload_test_dir], debug=debug)

    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    check_all_src_files_are_synced(parsed_result, sync_upload_test_dir)

    empty_folder_path = os.path.join(sync_upload_test_dir, 'empty_folder')
    object_storage_util.create_mixed_dir_at_path(empty_folder_path)

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    bucket_name, '--src-dir', sync_upload_test_dir], debug=debug)

    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    uploaded_set = parsed_result['uploaded-objects'].keys()
    filled_empty_folder_files_set = object_storage_util.get_file_set_at_path(empty_folder_path, sync_upload_test_dir)
    assert filled_empty_folder_files_set == uploaded_set


@util.skip_while_rerecording
def test_sync_empty_folder_sync_dry_run_all_files(test_id):
    bucket_name = sync_upload_bucket_name
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    bucket_name, '--src-dir', sync_upload_test_dir, '--dry-run'], debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    all_upload_set = set({}).union(uploaded_set, deleted_set, skipped_set)
    local_files_set = object_storage_util.get_file_set_at_path(sync_upload_test_dir, '')
    assert local_files_set == all_upload_set


@util.skip_while_rerecording
def test_sync_empty_folder_uploaded_should_be_in_downloaded(test_id):
    bucket_name = sync_upload_bucket_name
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    bucket_name, '--src-dir', sync_upload_test_dir], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    check_all_src_files_are_synced(parsed_result, sync_upload_test_dir)
    local_files_set = object_storage_util.get_file_set_at_path(sync_upload_test_dir)

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    bucket_name, '--dest-dir', sync_download_test_dir], debug=debug)

    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    downloaded_files, skipped_files = object_storage_util.unpack_bulk_download_result(parsed_result)
    all_downloaded_files_set = set(downloaded_files)

    assert all_downloaded_files_set == local_files_set


@util.skip_while_rerecording
def test_sync_empty_folder_inside_empty_folder(test_id):
    bucket_name = sync_upload_bucket_name
    empty_folder_path = os.path.join(sync_upload_test_dir, 'empty_folder')
    object_storage_util.create_empty_dir_at_path(empty_folder_path)
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    bucket_name, '--src-dir', empty_folder_path], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    check_all_src_files_are_synced(parsed_result, empty_folder_path)
