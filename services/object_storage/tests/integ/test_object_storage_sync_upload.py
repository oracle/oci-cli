# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates. All rights reserved.

import os
import random
import shutil
import time
from io import StringIO
from pathlib import Path

import pytest

import services.object_storage.src.oci_cli_object_storage.objectstorage_cli_extended as os_cli
from oci_cli import cli_util
import test_object_storage_bulk_operations as bulk_operation
from test_object_storage_sync_download import parse_dry_run_result, \
    generate_random_string, create_new_objects_remote, create_new_files_local, cleanup_files_from_local
from tests import util
import services.object_storage.tests.common.util as object_storage_util

OBJECTS_TO_CREATE_IN_REMOTE_FOR_SYNC = 20

sync_local_object_content = {}
sync_upload_bucket_name = str()
sync_upload_test_dir = str()

sync_remote_prefixes = {
    'a/b/c': [],
    'a/b': [],
    'a': [],
    '': []
}

new_path = 'new_path'
new_files_set = 'new_files_set'
new_dir = 'new_dir'


@pytest.fixture(params=[False])
def debug(request):
    return request.param


@pytest.fixture(scope='module', autouse=True)
def generate_files_in_remote(object_storage_client, test_id):
    global sync_upload_bucket_name, sync_upload_test_dir

    print('Setting up the test bucket for sync upload..')
    sync_upload_bucket_name = 'ObjectStorageSyncUploadTest_{}'.format(test_id)
    sync_upload_test_dir = 'tests/temp/sync_upload_{}'.format(test_id)
    if os.path.exists(sync_upload_test_dir):
        shutil.rmtree(sync_upload_test_dir)

    Path(sync_upload_test_dir).mkdir(parents=True, exist_ok=False)
    bulk_operation.clear_and_create_new_bucket(object_storage_client, sync_upload_bucket_name, False)

    for i in range(OBJECTS_TO_CREATE_IN_REMOTE_FOR_SYNC):
        if i % 4 == 3:
            object_name = 'a/b/c/Object_{}'.format(i)
            sync_remote_prefixes['a/b/c'].append(object_name)
        elif i % 4 == 2:
            object_name = 'a/b/Object_{}'.format(i)
            sync_remote_prefixes['a/b'].append(object_name)
        elif i % 4 == 1:
            object_name = 'a/Object_{}'.format(i)
            sync_remote_prefixes['a'].append(object_name)
        else:
            # At the root of the bucket
            object_name = 'Object_{}'.format(i)
            sync_remote_prefixes[''].append(object_name)

        object_content = bulk_operation.generate_random_string(bulk_operation.CONTENT_STRING_LENGTH)
        local_file_path = os.path.join(sync_upload_test_dir, object_name)
        Path(local_file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(local_file_path, 'w') as fh:
            fh.write(object_content)
        sync_local_object_content[object_name] = object_content

    yield

    print("Tearing down..")
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, sync_upload_bucket_name)
    if os.path.exists(sync_upload_test_dir):
        shutil.rmtree(sync_upload_test_dir)


@pytest.fixture(autouse=True)
def teardown(debug):
    yield
    bulk_operation.invoke(['os', 'object', 'bulk-delete', '--namespace', util.NAMESPACE, '--bucket-name',
                           sync_upload_bucket_name, '--force'], debug=debug)


@pytest.fixture()
def cleanup_new_content_set():
    data = {new_files_set: {}, new_dir: ''}
    yield data
    cleanup_files_from_local(data[new_files_set])
    object_storage_util.remove_dir_at_path(data[new_dir])


@util.skip_while_rerecording
def test_sync_src_dry_run(object_storage_client, debug):
    """
    1. Check for UsageError for incorrect params
    2. Upload the files in remote and validate the output. Should get the list of all the objects to be uploaded.
    3. Validate the list
    """

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--dry-run', '--src-dir', sync_upload_test_dir],
                                   debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(get_list_of_objects(object_storage_client, util.NAMESPACE, sync_upload_bucket_name)) == 0
    assert len(uploaded_set) == len(sync_local_object_content.keys())
    assert deleted_set == set()
    assert skipped_set == set()


@util.skip_while_rerecording
def test_sync_src(object_storage_client):
    """
    1. Upload the files to remote.
    2. validate the output and file contents
    """

    upload_and_validate_all_objects(object_storage_client, debug)
    assert len(sync_local_object_content) == len(get_list_of_objects(object_storage_client, util.NAMESPACE,
                                                                     sync_upload_bucket_name))


@util.skip_while_rerecording
def test_sync_src_updated_objects(object_storage_client):
    """
    1. Upload all the objects from src directory
    2. Randomly modify one file with different content (This action would change the size and last modification time)
    3. Randomly modify another file with same content (This action would just modify the last modified time)
    4. As we sync only based on the above two criteria, the next time we upload from the source directory
        we expect the modified files to get transferred to remote
    5. Rest of the objects in the local should get skipped
    """

    upload_and_validate_all_objects(object_storage_client, debug)

    # write one local object with different content
    f_diff_content = random.choice(list(sync_local_object_content))
    new_content = bulk_operation.generate_random_string(bulk_operation.CONTENT_STRING_LENGTH_SHORT)
    sync_local_object_content[f_diff_content] = new_content
    with open(os.path.join(sync_upload_test_dir, f_diff_content), 'w') as fh:
        fh.write(new_content)

    f_same_content = random.choice([o for o in sync_local_object_content if o != f_diff_content])
    fp_f_same_content = os.path.join(sync_upload_test_dir, f_same_content)
    original_mtime = os.stat(fp_f_same_content).st_mtime
    # Update the last modification time of one file while keeping the content same.
    # setting local file modification time to a future date (+5 sec)  so that sync properly works
    # otherwise the m_time of the new object might be too close to it's counterpart in remote
    # and we might end up skipping it as local writes are very fast
    updated_mtime = time.time() + 5
    os.utime(fp_f_same_content, (updated_mtime, updated_mtime))

    try:
        result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                        sync_upload_bucket_name, '--src-dir', sync_upload_test_dir], debug=debug)
        parsed_result = util.parse_json_response_from_mixed_output(result.output)
        assert parsed_result['upload-failures'] == {}
        assert set(parsed_result['uploaded-objects']) == {f_diff_content, f_same_content}
        assert len(parsed_result['skipped-objects']) == len(sync_local_object_content.keys()) - 2

        compare_file_content_to_remote(object_storage_client, sync_local_object_content,
                                       objects_in_scope=[f_diff_content, f_same_content])
    finally:
        # set the original time back to the f_same_content file so that it doesn't get picked up by subsequent tests
        os.utime(fp_f_same_content, (original_mtime, original_mtime))


@util.skip_while_rerecording
def test_sync_src_new_objects(object_storage_client, cleanup_new_content_set):
    """
    1. Upload the files to remote and validate the output and file contents
    2. Create a new file in local
    3. When we try to sync against remote again only the new object should get uploaded and
        rest of the files should get skipped as they are already present.
    4. Remove the newly created file after test
    """

    upload_and_validate_all_objects(object_storage_client, debug)
    # add a new object to the remote
    new_object_name = 'a/new_object'
    new_file_contents = {new_object_name: bulk_operation.generate_random_string(bulk_operation.CONTENT_STRING_LENGTH)}
    new_file_path = os.path.join(sync_upload_test_dir, new_object_name)
    cleanup_new_content_set[new_files_set] = {new_file_path}
    with open(new_file_path, 'w') as fh:
        fh.write(new_file_contents[new_object_name])

    try:
        result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                        sync_upload_bucket_name, '--src-dir', sync_upload_test_dir], debug=debug)
        parsed_result = util.parse_json_response_from_mixed_output(result.output)
        assert parsed_result['upload-failures'] == {}
        assert set(parsed_result['uploaded-objects'].keys()) == {new_object_name}
        assert len(parsed_result['skipped-objects']) == len(sync_local_object_content.keys())

        compare_file_content_to_remote(object_storage_client, new_file_contents, objects_in_scope=[new_object_name])
    finally:
        os.remove(new_file_path)


@util.skip_while_rerecording
def test_sync_src_include_dry_run(debug):
    """
    1. Randomly select one file from local and perform a --dry-run on the remote
        specifying the same file name in --include.
    2. We expect that only this file gets transferred. No other files gets transferred/skipped.
    """

    file_name_to_sync = random.choice(list(sync_local_object_content))
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--include',
                                    file_name_to_sync, '--dry-run'], debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert uploaded_set == {(os.path.join(sync_upload_test_dir, file_name_to_sync)).replace(os.sep, '/')}
    assert deleted_set == set()
    assert skipped_set == set()


@util.skip_while_rerecording
def test_sync_src_include(object_storage_client, debug):
    """
    1. Randomly select one file from local and upload that by passing that parameter to --include
    2. Validate that only that file got transferred to remote.
        Also, validate the contents of the file just to assert that they are the same.
    3. Sync again with --include option and validate that the same file gets skipped now.
    """

    file_name_to_include = random.choice(list(sync_local_object_content))
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--include',
                                    file_name_to_include], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert file_name_to_include in parsed_result['uploaded-objects']
    assert parsed_result['skipped-objects'] == []
    assert len(get_list_of_objects(object_storage_client, util.NAMESPACE, sync_upload_bucket_name)) == 1
    compare_file_content_to_remote(object_storage_client, sync_local_object_content,
                                   objects_in_scope=file_name_to_include)

    # try downloading the files again and verify that it's skipped
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--include',
                                    file_name_to_include], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['uploaded-objects'] == {}
    assert len(parsed_result['skipped-objects']) == 1
    assert file_name_to_include in parsed_result['skipped-objects']


@util.skip_while_rerecording
def test_sync_src_exclude_dry_run(debug):
    """
    1. Randomly select one file from local and perform a --dry-run on the remote specifying it in --exclude
    2. Validate that every other file is in the transfer list except the one in exclude list
    """

    file_name_to_exclude = random.choice(list(sync_local_object_content))
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--exclude',
                                    file_name_to_exclude, '--dry-run'], debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(uploaded_set) == len(sync_local_object_content.keys()) - 1
    assert file_name_to_exclude not in uploaded_set
    assert deleted_set == set()
    assert skipped_set == set()


@util.skip_while_rerecording
def test_sync_src_exclude(object_storage_client, debug):
    """
    1. Randomly select one file from local and sync against remote by specifying it in --exclude
    2. Validate that all other files except the excluded file gets transferred
    """

    file_name_to_exclude = random.choice(list(sync_local_object_content))
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--exclude',
                                    file_name_to_exclude], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    objects_transferred = set(sync_local_object_content.keys())
    objects_transferred.remove(file_name_to_exclude)
    assert len(parsed_result['uploaded-objects']) == len(objects_transferred)
    assert file_name_to_exclude not in parsed_result['uploaded-objects']
    assert parsed_result['skipped-objects'] == []
    assert len(get_list_of_objects(object_storage_client, util.NAMESPACE, sync_upload_bucket_name)) == len(
        objects_transferred)
    compare_file_content_to_remote(object_storage_client, sync_local_object_content,
                                   objects_in_scope=objects_transferred)


@util.skip_while_rerecording
def test_sync_dest_dir_prefix(object_storage_client, debug):
    """
    1. Set a prefix to apply to all the transactions during sync
    2. Perform a --dry-run with the prefix applied and verify that all the files in the source directory get transferred.
    3. Sync against remote with the same prefix and verify that all objects from source directory is available
        in remote under the specified prefix
    4. Validate the contents of the local files against their counter part in remote.
    """

    prefix_to_sync = 'upload_prefix/'
    # perform a dry run the get the objects to be transferred
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--prefix',
                                    prefix_to_sync, '--dry-run'], debug=debug)

    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    # verify that all objects gets uploaded
    assert set([o[len(sync_upload_test_dir):].strip('/') for o in uploaded_set]) == set(
        sync_local_object_content.keys())
    assert len(skipped_set) == 0
    assert len(deleted_set) == 0

    # sync with the same prefix and validate that all object are available in remote under the specified prefix
    # Validate the contents of the files in local against the one from the prefix in remote
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--prefix',
                                    prefix_to_sync], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    actually_uploaded_objects = get_list_of_objects(object_storage_client, util.NAMESPACE, sync_upload_bucket_name,
                                                    prefix=prefix_to_sync)
    assert parsed_result['upload-failures'] == {}
    assert set(parsed_result['uploaded-objects']) == set([o.name for o in actually_uploaded_objects])
    assert parsed_result['skipped-objects'] == []

    # validate that prefix gets added to every file that gets uploaded
    new_object_content_map = {os.path.join(prefix_to_sync, k): v for k, v in sync_local_object_content.items()}
    compare_file_content_to_remote(object_storage_client, new_object_content_map, prefix_to_test=prefix_to_sync)


@util.skip_while_rerecording
def test_sync_src_with_delete(object_storage_client, debug):
    """
    1. Perform a --dry-run against a blank remote by specifying --delete option.
    2. Verify that all objects gets transferred and nothing gets deleted because
        there are no extra objects in remote.
    3. Upload all the objects from local to remote
    4. Create new files in remote which are not present in source
    5. Perform a --dry-run against the updated remote with the same parameter as before.
    6. This time all the source objects should be present in remote as we uploaded them earlier so
        we expect them to get skipped
    7. Validate that all the new objects created in remote from previous step would be in deleted list
        as they are not present in the source
    8. Perform an actual sync now and validate the above 2 points
    """

    # run the sync command with --delete option
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--delete',
                                    '--dry-run'], debug=debug)

    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(deleted_set) == 0
    assert len(uploaded_set) == len(sync_local_object_content.keys())
    assert len(skipped_set) == 0

    upload_and_validate_all_objects(object_storage_client, debug)
    new_local_file_set = create_new_objects_remote(object_storage_client, sync_upload_bucket_name, 11)

    # run the sync command with --delete option
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--delete',
                                    '--dry-run'], debug=debug)

    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(uploaded_set) == 0
    assert len(skipped_set) == len(sync_local_object_content.keys())
    assert deleted_set == new_local_file_set

    # run the sync command with --delete option
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--delete'],
                                   debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['uploaded-objects'] == {}
    assert len(parsed_result['skipped-objects']) == len(sync_local_object_content.keys())
    assert set(parsed_result['deleted-objects']) == new_local_file_set


@util.skip_while_rerecording
def test_sync_src_with_delete_paging(object_storage_client, debug):
    """
    1. Perform a --dry-run against a blank remote by specifying --delete option.
    2. Verify that all objects gets transferred and nothing gets deleted because
        there are no extra objects in remote.
    3. Upload all the objects from local to remote
    4. Create new files in remote which are not present in source
    5. Perform a --dry-run against the updated remote with the same parameter as before.
    6. This time all the source objects should be present in remote as we uploaded them earlier so
        we expect them to get skipped
    7. Validate that all the new objects created in remote from previous step would be in deleted list
        as they are not present in the source
    8. Perform an actual sync now and validate the above 2 points
    """

    # run the sync command with --delete option
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--delete',
                                    '--dry-run'], debug=debug)

    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(deleted_set) == 0
    assert len(uploaded_set) == len(sync_local_object_content.keys())
    assert len(skipped_set) == 0

    upload_and_validate_all_objects(object_storage_client, debug)
    new_local_file_set = create_new_objects_remote(object_storage_client, sync_upload_bucket_name, 1100)

    # run the sync command with --delete option
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--delete',
                                    '--dry-run'], debug=debug)

    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(uploaded_set) == 0
    assert len(skipped_set) == len(sync_local_object_content.keys())
    assert deleted_set == new_local_file_set

    # run the sync command with --delete option
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--delete'],
                                   debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['uploaded-objects'] == {}
    assert len(parsed_result['skipped-objects']) == len(sync_local_object_content.keys())
    assert set(parsed_result['deleted-objects']) == new_local_file_set


@util.skip_while_rerecording
def test_sync_src_with_delete_and_include(object_storage_client, cleanup_new_content_set):
    """
    1. Create new set of objects in local with .pdf and .doc extensions.
    2. Perform a dry run with --delete to include only *.pdf and validate that only .pdf files are transferred.
    3. Create new set of files in remote with .pdf and .txt extensions.
    4. Perform step:2 again and validate that all .pdf files are transferred but only the .pdf files from remote
        gets deleted. Nothing happens to .txt files.
    5. Perform step:2 again including *.pdf and *.doc both and validate that only files matching the pattern gets
        transferred/deleted
    6. Perform actual sync and validate the final output with the ones from the dry-run
    """

    l_file_set_1 = create_new_files_local(sync_upload_test_dir, 3, extension='pdf')
    l_file_set_2 = create_new_files_local(sync_upload_test_dir, 5, extension='doc')
    cleanup_new_content_set[new_files_set] = l_file_set_1.union(l_file_set_2)
    cleanup_new_content_set[new_dir] = os.path.join(sync_upload_test_dir, 'dir')

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--delete',
                                    '--include', '*.pdf', '--dry-run'], debug=debug)

    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert deleted_set == set()
    assert skipped_set == set()
    assert len(uploaded_set) == len(l_file_set_1)

    r_obj_set_1 = create_new_objects_remote(object_storage_client, sync_upload_bucket_name, 6, extension='pdf')
    r_obj_set_2 = create_new_objects_remote(object_storage_client, sync_upload_bucket_name, 4, extension='txt')

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--delete',
                                    '--include', '*.pdf', '--dry-run'], debug=debug)

    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(deleted_set) == len(r_obj_set_1)
    assert skipped_set == set()
    assert len(uploaded_set) == len(l_file_set_1)

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--delete',
                                    '--include', '*.pdf', '--include', '*.doc', '--dry-run'], debug=debug)

    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(deleted_set) == len(r_obj_set_1)
    assert skipped_set == set()
    assert len(uploaded_set) == len(l_file_set_1.union(l_file_set_2))

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--delete',
                                    '--include', '*.pdf', '--include', '*.doc'], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert set(parsed_result['uploaded-objects']) == set([(f[len(sync_upload_test_dir):].replace(os.sep, '/')).strip('/') for f in l_file_set_1.union(l_file_set_2)])
    assert parsed_result['skipped-objects'] == []
    assert set(parsed_result['deleted-objects']) == r_obj_set_1


@util.skip_while_rerecording
def test_sync_src_with_delete_and_exclude(object_storage_client, debug, cleanup_new_content_set):
    """
    1. Create new set of objects in local with .pdf and .doc extensions.
    2. Perform a dry run with --delete to exclude only *.pdf and validate that all other files are transferred.
    3. Create new set of files in remote with .doc and .txt extensions.
    4. Perform step:2 again excluding *.doc and validate that all files except .doc files gets transferred but
        only .txt files are deleted from remote. Nothing happens to .doc file in remote.
    5. Perform step:2 again including *.pdf and *.doc both and validate that originally created files in local would get
        transferred but only .txt files are deleted from remote.
    6. Perform actual sync and validate the final output with the ones from the dry-run
    """

    l_file_set_1 = create_new_files_local(sync_upload_test_dir, 3, extension='pdf')
    l_file_set_2 = create_new_files_local(sync_upload_test_dir, 5, extension='doc')
    cleanup_new_content_set[new_files_set] = l_file_set_1.union(l_file_set_2)
    cleanup_new_content_set[new_dir] = os.path.join(sync_upload_test_dir, 'dir')

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--delete',
                                    '--exclude', '*.pdf', '--dry-run'], debug=debug)

    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert deleted_set == set()
    assert skipped_set == set()
    assert len(uploaded_set) == len(l_file_set_2) + len(sync_local_object_content.keys())

    r_obj_set_1 = create_new_objects_remote(object_storage_client, sync_upload_bucket_name, 6, extension='doc')
    r_obj_set_2 = create_new_objects_remote(object_storage_client, sync_upload_bucket_name, 4, extension='txt')

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--delete',
                                    '--exclude', '*.doc', '--dry-run'], debug=debug)

    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(deleted_set) == len(r_obj_set_2)
    assert skipped_set == set()
    assert len(uploaded_set) == len(l_file_set_1) + len(sync_local_object_content.keys())

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--delete',
                                    '--exclude', '*.pdf', '--exclude', '*.doc', '--dry-run'], debug=debug)

    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(deleted_set) == len(r_obj_set_2)
    assert skipped_set == set()
    assert len(uploaded_set) == len(sync_local_object_content.keys())

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--delete',
                                    '--exclude', '*.pdf', '--exclude', '*.doc'], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert set(parsed_result['uploaded-objects']) == set(sync_local_object_content.keys())
    assert parsed_result['skipped-objects'] == []
    assert set(parsed_result['deleted-objects']) == r_obj_set_2


@util.skip_while_rerecording
def test_sync_src_with_delete_and_prefix(object_storage_client, debug):
    """
    1. Start with a fresh bucket
    2. Create new files at the bucket root which are not present in source
    3. Assign a prefix to sync and upload all the local files to that prefix in remote
    4. Validate that all the files are in the to-be-uploaded list
    5. Create new files at the prefix level which are not present in source
    6. Sync against remote again by specifying --delete
    7. Validate that all objects gets uploaded
    8. Validate that all new objects in the prefix level gets deleted
    9. Validate that no new objects from root gets deleted.
    """

    # create new files at bucket root which are not present in local
    new_remote_files_at_base = create_new_objects_remote(object_storage_client, sync_upload_bucket_name, 10,
                                                         prefix=None)

    prefix_to_sync = 'upload_prefix_include/'
    # perform a dry run the get the objects to be transferred
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--prefix',
                                    prefix_to_sync, '--delete', '--dry-run'], debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    # validate that all files from local gets transferred
    assert len(uploaded_set) == len(sync_local_object_content.keys())
    assert len(skipped_set) == 0
    # validate that no file gets deleted as these new files does not share the same prefix
    assert len(deleted_set) == 0

    # generate new files at the prefix level and perform the dry run again
    new_remote_files_at_prefix = create_new_objects_remote(object_storage_client, sync_upload_bucket_name, 10,
                                                           prefix=prefix_to_sync)
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--prefix',
                                    prefix_to_sync, '--delete', '--dry-run'], debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    # validate that all files from local gets transferred
    assert len(uploaded_set) == len(sync_local_object_content.keys())
    assert len(skipped_set) == 0
    # validate that files at the prefix level gets deleted where as the base files are not touched
    assert not any(filter(lambda f: f in new_remote_files_at_base, deleted_set))
    assert deleted_set == new_remote_files_at_prefix

    # perform the actual delete and validate
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--prefix',
                                    prefix_to_sync, '--delete'], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    # verify that prefixes are added while uploading and verify the files uploaded
    assert set(parsed_result['uploaded-objects']) == set(
        [os.path.join(prefix_to_sync, o) for o in sync_local_object_content])
    assert len(parsed_result['skipped-objects']) == 0
    assert set(parsed_result['deleted-objects']) == new_remote_files_at_prefix
    # verify that prefixes are added while uploading and validate the file contents
    new_content_map = {os.path.join(prefix_to_sync, k): v for k, v in sync_local_object_content.items()}
    compare_file_content_to_remote(object_storage_client, new_content_map, prefix_to_test=prefix_to_sync)


@util.skip_while_rerecording
def test_sync_src_with_delete_include_and_prefix(object_storage_client, debug, cleanup_new_content_set):
    """
    Assert that scope of file transfer and delete is only limited to --include pattern within the bucket prefix

    1. Create files in local with .pdf and .doc extensions.
    2. Perform a --dry-run --delete with the specified prefix and include *.pdf files.
    3. Validate that only .pdf files get transferred from local and nothing gets deleted.
    4. Create new files with .pdf and .txt extensions in the bucket with the specified prefix. Also create some extra
        pdf files which are not part of the prefix.
    5. Perform step:2 again. Validate that this time all .pdf files get transferred but only the new .pdf files in
        remote gets deleted. This operation has no effect on .txt files.
    6. Perform step:2 again including *pdf and *.doc. Verify that all .pdf and .doc files get transferred but only .pdf
        files get deleted from remote. Other files are not affected.
    7. Perform actual sync and verify the final output with the step above.
    """

    _prefix = 'upload_prefix_include_delete/'

    l_file_set_1 = create_new_files_local(sync_upload_test_dir, 6, extension='pdf')
    l_file_set_2 = create_new_files_local(sync_upload_test_dir, 4, extension='doc')
    cleanup_new_content_set[new_files_set] = l_file_set_1.union(l_file_set_2)
    cleanup_new_content_set[new_dir] = os.path.join(sync_upload_test_dir, 'dir')

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--prefix',
                                    _prefix, '--delete', '--dry-run', '--include', '*.pdf'], debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(uploaded_set) == len(l_file_set_1)
    assert len(skipped_set) == 0
    assert deleted_set == set()

    r_obj_set_1 = create_new_objects_remote(object_storage_client, sync_upload_bucket_name, 5, prefix=_prefix,
                                            extension='pdf')
    r_obj_set_2 = create_new_objects_remote(object_storage_client, sync_upload_bucket_name, 3, prefix=_prefix,
                                            extension='txt')
    # create other .pdf files outside the prefix level to verify that these won't fall in the scope of the command
    r_obj_set_3 = create_new_objects_remote(object_storage_client, sync_upload_bucket_name, 11, extension='pdf')

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--prefix',
                                    _prefix, '--delete', '--dry-run', '--include', '*.pdf'], debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(uploaded_set) == len(l_file_set_1)
    assert len(skipped_set) == 0
    assert len(deleted_set) == len(r_obj_set_1)

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--prefix',
                                    _prefix, '--delete', '--dry-run', '--include', '*.pdf', '--include', '*.doc'],
                                   debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(uploaded_set) == len(l_file_set_1.union(l_file_set_2))
    assert len(skipped_set) == 0
    assert len(deleted_set) == len(r_obj_set_1)

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--prefix',
                                    _prefix, '--delete', '--include', '*.pdf', '--include', '*.doc'],
                                   debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert set(parsed_result['uploaded-objects']) == set([(os.path.join(_prefix, f[len(sync_upload_test_dir):].replace(os.sep, '/').strip('/'))) for f in l_file_set_1.union(l_file_set_2)])
    assert parsed_result['skipped-objects'] == []
    assert set(parsed_result['deleted-objects']) == r_obj_set_1


@util.skip_while_rerecording
def test_sync_src_with_delete_exclude_and_prefix(object_storage_client, debug, cleanup_new_content_set):
    """
    Assert that scope of file transfer and delete is only limited to --exclude pattern within the bucket prefix

    1. Create files in local with .pdf and .doc extensions.
    2. Perform a --dry-run --delete with the specified prefix and exclude *.pdf files.
    3. Validate that only .doc + original files get transferred from local and nothing gets deleted.
    4. Create new files with .pdf and .txt extensions in the bucket with the specified prefix. Also create some extra
        pdf files which are not part of the prefix.
    5. Perform step:2 again. Validate that this time all .doc + original files get transferred but only the
        new .txt files in remote gets deleted. This operation has no effect on .doc files.
    6. Perform step:2 again excluding *pdf and *.doc. Verify that only the original files get transferred but only .txt
        files get deleted from remote.
    7. Perform actual sync and verify the final output with the step above.
    """

    _prefix = 'upload_prefix_exclude_delete/'
    l_file_set_1 = create_new_files_local(sync_upload_test_dir, 6, extension='pdf')
    l_file_set_2 = create_new_files_local(sync_upload_test_dir, 4, extension='doc')
    cleanup_new_content_set[new_files_set] = l_file_set_1.union(l_file_set_2)
    cleanup_new_content_set[new_dir] = os.path.join(sync_upload_test_dir, 'dir')

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--prefix',
                                    _prefix, '--delete', '--dry-run', '--exclude', '*.pdf'], debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(uploaded_set) == len(l_file_set_2) + len(sync_local_object_content.keys())
    assert len(skipped_set) == 0
    assert deleted_set == set()

    r_obj_set_1 = create_new_objects_remote(object_storage_client, sync_upload_bucket_name, 5, prefix=_prefix,
                                            extension='pdf')
    r_obj_set_2 = create_new_objects_remote(object_storage_client, sync_upload_bucket_name, 3, prefix=_prefix,
                                            extension='txt')
    # create other .pdf files outside the prefix level to verify that these won't fall in the scope of the command
    r_obj_set_3 = create_new_objects_remote(object_storage_client, sync_upload_bucket_name, 11, extension='pdf')

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--prefix',
                                    _prefix, '--delete', '--dry-run', '--exclude', '*.pdf'], debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(uploaded_set) == len(l_file_set_2) + len(sync_local_object_content.keys())
    assert len(skipped_set) == 0
    assert len(deleted_set) == len(r_obj_set_2)

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--prefix',
                                    _prefix, '--delete', '--dry-run', '--exclude', '*.pdf', '--exclude', '*.doc'],
                                   debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(uploaded_set) == len(sync_local_object_content.keys())
    assert len(skipped_set) == 0
    assert len(deleted_set) == len(r_obj_set_2)

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir, '--prefix',
                                    _prefix, '--delete', '--exclude', '*.pdf', '--exclude', '*.doc'],
                                   debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert set(parsed_result['uploaded-objects']) == set([(os.path.join(_prefix, o).replace(os.sep, '/')) for o in sync_local_object_content.keys()])
    assert parsed_result['skipped-objects'] == []
    assert set(parsed_result['deleted-objects']) == r_obj_set_2


@util.skip_while_rerecording
def test_sync_src_with_content_headers(object_storage_client, debug):
    """
    1. Perform a sync with all the content headers, metadata
    2. Validate that all the objects synced would have these headers.
    """

    cache_control_header = random.choice(['no-cache', 'no-store', 'no-transform', 'only-if-cached', 'max-age=60'])
    content_disposition_header = random.choice(['inline', 'attachment', 'attachment; filename="filename.jpg"'])
    content_encoding_header = random.choice(['gzip', 'compress', 'deflate', 'br'])
    content_language_header = random.choice(['de-DE', 'en-US', 'en-CA'])
    content_type_header = random.choice(['text/plain', 'text/html', 'application/json', 'application/xml'])
    metadata_headers = {generate_random_string(5): generate_random_string(10) for _ in range(5)}

    # upload all the objects with content headers specified and validate that they are present for all the objects
    bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                           sync_upload_bucket_name, '--src-dir', sync_upload_test_dir,
                           '--cache-control', cache_control_header,
                           '--content-disposition', content_disposition_header,
                           '--content-encoding', content_encoding_header,
                           '--content-language', content_language_header,
                           '--content-type', content_type_header,
                           '--metadata', metadata_headers
                           ], debug=debug)

    for o in get_list_of_objects(object_storage_client, util.NAMESPACE, sync_upload_bucket_name):
        head_resp = object_storage_client.head_object(util.NAMESPACE, sync_upload_bucket_name, o.name)
        assert head_resp.headers['cache-control'] == cache_control_header
        assert head_resp.headers['content-disposition'] == content_disposition_header
        assert head_resp.headers['content-encoding'] == content_encoding_header
        assert head_resp.headers['content-language'] == content_language_header
        assert head_resp.headers['Content-Type'] == content_language_header
        for k in metadata_headers:
            assert head_resp.headers['opc-meta-' + k] == metadata_headers[k]


@util.skip_while_rerecording
def test_sync_src_with_no_follow_symlinks_file(debug):
    """
    1. Create a symlink to randomly point to a file within the tree
    2. Validate that the file gets skipped when sync is being used with --no-follow-symlink
    """

    file_to_create_a_symlink_of = os.path.join(sync_upload_test_dir, random.choice(list(sync_local_object_content)))

    # randomly generate a location for symlink file withing the test tree
    symlink_pref = os.path.join(random.choice(list(sync_remote_prefixes)), 'symlink_file')
    symlink_fp = os.path.join(sync_upload_test_dir, symlink_pref)

    # create the symlink
    create_symlink(file_to_create_a_symlink_of, symlink_fp)
    symlink_fp = symlink_fp.replace(os.sep, '/')
    symlink_pref = symlink_pref.replace(os.sep, '/')

    # validate the output from dry-run first
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir,
                                    '--dry-run', '--no-follow-symlinks'], debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert symlink_fp not in uploaded_set
    assert skipped_set == set()
    assert deleted_set == set()

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir,
                                    '--no-follow-symlinks'], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert symlink_pref not in parsed_result['uploaded-objects']
    assert parsed_result['skipped-objects'] == []
    os.unlink(symlink_fp)


@util.skip_while_rerecording
def test_sync_src_with_no_follow_symlinks_dir(debug):
    """
    1. Create a symlink to randomly point to a dir
    2. Validate that the directory get skipped while sync is being used with  --no-follow-symlink
    """

    # randomly generate a dir to create a symlink of
    dir_to_create_a_symlink_of = os.path.join(sync_upload_test_dir, random.choice(list(sync_remote_prefixes)))

    # randomly generate a location for symlink dir withing the test tree
    symlink_pref = os.path.join(random.choice(list(sync_remote_prefixes)), 'symlink_dir')
    symlink_fp = os.path.join(sync_upload_test_dir, symlink_pref)

    # create the symlink
    create_symlink(dir_to_create_a_symlink_of, symlink_fp, is_directory=True)
    symlink_fp = symlink_fp.replace(os.sep, '/')
    symlink_pref = symlink_pref.replace(os.sep, '/')

    # validate the output from dry-run first
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir,
                                    '--dry-run', '--no-follow-symlinks'], debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert not any(filter(lambda f: f.startswith(symlink_fp), uploaded_set))
    assert skipped_set == set()
    assert deleted_set == set()

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir,
                                    '--no-follow-symlinks'], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert not any(filter(lambda f: f.startswith(symlink_pref), parsed_result['uploaded-objects']))
    assert parsed_result['skipped-objects'] == []
    os.unlink(symlink_fp)


@util.skip_while_rerecording
def test_sync_src_with_follow_symlinks_file(object_storage_client, debug):
    """
    1. Create a symlink to randomly point to a file within the tree
    2. Validate that this symlink gets written to object storage by default. Also, validate the file content
    """

    random_file = random.choice(list(sync_local_object_content))
    file_to_create_a_symlink_of = os.path.join(sync_upload_test_dir, random_file)

    # randomly generate a location for symlink file withing the test tree
    symlink_pref = os.path.join(random.choice(list(sync_remote_prefixes)), 'symlink_file')
    symlink_fp = os.path.join(sync_upload_test_dir, symlink_pref)

    create_symlink(file_to_create_a_symlink_of, symlink_fp)
    symlink_fp = symlink_fp.replace(os.sep, '/')
    symlink_pref = symlink_pref.replace(os.sep, '/')
    # validate the output from dry-run first
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir,
                                    '--dry-run'], debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert symlink_fp in uploaded_set
    assert skipped_set == set()
    assert deleted_set == set()

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert symlink_pref in parsed_result['uploaded-objects']
    assert parsed_result['skipped-objects'] == []
    compare_file_content_to_remote(object_storage_client, {symlink_pref: sync_local_object_content[random_file]},
                                   objects_in_scope=symlink_pref)
    os.unlink(symlink_fp)


@util.skip_while_rerecording
def test_sync_src_with_follow_symlinks_dir(object_storage_client, debug):
    """
    1. Create a symlink to randomly point to a dir within the tree
    2. Take precaution to avoid circular symlink conditions
    3. Validate that all the file within the directory get transferred to object storage.
        Also, validate the contents of the transferred file with the original ones.
    """

    # We will not consider root as prefix because of circular imports
    random_dir = random.choice([p for p in sync_remote_prefixes if p != ''])
    dir_to_create_a_symlink_of = os.path.join(sync_upload_test_dir, random_dir)

    # WARNING: Can not create a random directory placeholder in the tree as it might turn into a circular link.
    # Hence choosing to create the symlink in the root
    symlink_pref = 'symlink_dir'
    symlink_fp = os.path.join(sync_upload_test_dir, symlink_pref)

    # create the symlink
    create_symlink(dir_to_create_a_symlink_of, symlink_fp, is_directory=True)
    symlink_fp = symlink_fp.replace(os.sep, '/')
    symlink_pref = symlink_pref.replace(os.sep, '/')
    dir_to_create_a_symlink_of = dir_to_create_a_symlink_of.replace(os.sep, '/')

    # validate the output from dry-run first
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir,
                                    '--dry-run'], debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    # validate that the symlink directory would upload all the objects of the original directory
    dir_content_with_symlink = {k[len(random_dir):].strip('/'): v for k, v in sync_local_object_content.items()
                                if k.startswith(random_dir)}
    for f in uploaded_set:
        if symlink_pref in f:
            assert f[len(symlink_fp):].strip('/') in dir_content_with_symlink
    assert skipped_set == set()
    assert deleted_set == set()

    # validate the same list against actual upload
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    for o in parsed_result['uploaded-objects']:
        if symlink_pref in o:
            # objects uploaded would only contain the symlink_prefix
            assert o[len(symlink_pref):].strip('/') in dir_content_with_symlink
    assert parsed_result['skipped-objects'] == []
    compare_file_content_to_remote(object_storage_client,
                                   {(os.path.join(symlink_pref, k)).replace(os.sep, '/'): v for k, v in dir_content_with_symlink.items()},
                                   prefix_to_test=symlink_pref)
    os.unlink(symlink_fp)


@util.skip_while_rerecording
def test_sync_src_when_bucket_name_is_invalid(debug):
    """
    Run the sync command specifying --src-dir using an invalid bucket name and validate that it throws a ServiceError
    """

    invalid_bucket_name = 'invalid_bucket'
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    invalid_bucket_name, '--src-dir', sync_upload_test_dir, '--dry-run'], debug=debug)
    assert 'ServiceError:' in result.output
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['status'] == 404
    assert parsed_result['code'] == 'BucketNotFound'

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    invalid_bucket_name, '--src-dir', sync_upload_test_dir], debug=debug)
    assert 'ServiceError:' in result.output
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['status'] == 404
    assert parsed_result['code'] == 'BucketNotFound'


def create_symlink(src_path_abs, symlink_fp, is_directory=False):
    # while creating the symlink first calculate the relative path of the object from the link destination.
    # If the path doesn't match the link would be broken
    os.symlink(
        os.path.relpath(
            src_path_abs.replace('/', os.sep),
            os.path.dirname(symlink_fp)
        ).replace('/', os.sep),
        symlink_fp.replace('/', os.sep),
        target_is_directory=is_directory)


def upload_and_validate_all_objects(object_storage_client, debug):
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_upload_bucket_name, '--src-dir', sync_upload_test_dir], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['skipped-objects'] == []
    assert set(parsed_result['uploaded-objects']) == set(sync_local_object_content.keys())
    compare_file_content_to_remote(object_storage_client, sync_local_object_content)


def get_list_of_objects(client, namespace, bucket_name, request_id=None, prefix=None, start=None, end=None,
                        limit=os_cli.OBJECT_LIST_PAGE_SIZE_BULK_OPERATIONS, delimiter=None, fields='name',
                        retrieve_all=True):
    list_object_response = \
        os_cli.retrying_list_objects(
            client=client,
            request_id=cli_util.use_or_generate_request_id(request_id),
            namespace=namespace,
            bucket_name=bucket_name,
            prefix=prefix,
            start=start,
            end=end,
            limit=limit,
            delimiter=delimiter,
            fields=fields,
            retrieve_all=retrieve_all
        )

    object_list = list()
    for response in list_object_response:
        for obj in response.data.objects:
            object_list.append(obj)
    return object_list


def compare_file_content_to_remote(client, object_content_map, prefix_to_test=None, objects_in_scope=None):
    namespace = util.NAMESPACE
    bucket_name = sync_upload_bucket_name
    for obj in get_list_of_objects(client, namespace, bucket_name, prefix=prefix_to_test):
        if objects_in_scope and obj.name not in objects_in_scope:
            continue

        obj_response = client.get_object(namespace, bucket_name, obj.name)

        sb = StringBuilder()
        for chunk in obj_response.data.raw.stream(os_cli.OBJECT_GET_CHUNK_SIZE, decode_content=False):
            sb.append(chunk.decode('utf-8'))

        assert object_content_map[obj.name] == str(sb)


# inner class to simulate an immutable string builder
class StringBuilder:
    _raw_str = None

    def __init__(self):
        self._raw_str = StringIO()

    def append(self, str):
        self._raw_str.write(str)

    def __str__(self):
        return self._raw_str.getvalue()
