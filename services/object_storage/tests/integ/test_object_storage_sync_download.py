# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates. All rights reserved.

import os
import shutil
import string
from pathlib import Path
import random

import pytest

import test_object_storage_bulk_operations as bulk_operation
from tests import util, test_config_container

CASSETTE_LIBRARY_DIR = 'services/object_storage/tests/cassettes'
OBJECTS_TO_CREATE_IN_REMOTE_FOR_SYNC = 20

sync_remote_object_content = {}
sync_download_bucket_name = str()
sync_download_test_dir = str()
sync_upload_bucket_name = str()
sync_upload_test_dir = str()

sync_download_bucket_name_recorded = str()
sync_download_test_dir_recorded = str()
sync_upload_test_dir_recorded = str()

sync_remote_prefixes = {
    'a/b/c': [],
    'a/b': [],
    'a': [],
    '': []
}


@pytest.fixture
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('object_storage_sync_download_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.fixture(params=[False])
def debug(request):
    return request.param


@pytest.fixture(scope='module', autouse=True)
def set_recorded_variable(test_id_recorded):
    global sync_download_bucket_name_recorded, sync_download_test_dir_recorded, sync_upload_test_dir_recorded
    sync_download_bucket_name_recorded = 'ObjectStorageSyncDownloadTest_{}'.format(test_id_recorded)
    sync_download_test_dir_recorded = 'tests/temp/sync_download_{}'.format(test_id_recorded)
    sync_upload_test_dir_recorded = 'tests/temp/sync_upload_{}'.format(test_id_recorded)


@pytest.fixture(scope='module', autouse=True)
def generate_files_in_remote(object_storage_client, test_id):
    global sync_download_bucket_name, sync_download_test_dir, sync_upload_bucket_name, sync_upload_test_dir

    print('Setting up the test bucket for sync download..')
    sync_download_bucket_name = 'ObjectStorageSyncDownloadTest_{}'.format(test_id)
    sync_download_test_dir = 'tests/temp/sync_download_{}'.format(test_id)
    if os.path.exists(sync_download_test_dir):
        shutil.rmtree(sync_download_test_dir)

    bulk_operation.clear_and_create_new_bucket(object_storage_client, sync_download_bucket_name, False)

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
        object_storage_client.put_object(util.NAMESPACE, sync_download_bucket_name, object_name, object_content)
        sync_remote_object_content[object_name] = object_content

    sync_upload_test_dir = 'tests/temp/sync_upload_{}'.format(test_id)

    yield

    print("Tearing down..")
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, sync_download_bucket_name)
    if os.path.exists(sync_download_test_dir):
        shutil.rmtree(sync_download_test_dir)


@pytest.fixture(autouse=True)
def teardown(debug):
    yield
    if os.path.exists(sync_download_test_dir):
        shutil.rmtree(sync_download_test_dir)


def test_sync_dest_dry_run(vcr_fixture, debug):
    """
    1. Check for UsageError for incorrect params
    2. Download the files to local and validate the output. Should get the list of all the objects to be downloaded.
    3. Validate the list
    """

    # test output when neither --src-dir nor --dest-dir is provided
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dry-run'], debug=debug)
    assert 'UsageError' in result.output
    assert 'Either' in result.output
    assert '--src-dir' in result.output
    assert '--dest-dir' in result.output

    # test output when both --src-dir and --dest-dir are provided
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dry-run', '--src-dir', sync_upload_test_dir_recorded,
                                    '--dest-dir', sync_download_test_dir_recorded], debug=debug)
    assert 'UsageError' in result.output
    assert 'Only' in result.output
    assert '--src-dir' in result.output
    assert '--dest-dir' in result.output

    # test --dry-run output with --dest-dir and validate
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dry-run', '--dest-dir', sync_download_test_dir_recorded],
                                   debug=debug)
    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(os.listdir(sync_download_test_dir_recorded)) == 0
    assert len(downloaded_set) == len(sync_remote_object_content.keys())
    assert deleted_set == set()
    assert skipped_set == set()


@util.skip_while_rerecording
def test_sync_dest():
    """
    1. Download the files to local and validate the output and file contents
    """

    download_and_validate_all_objects()

    assert len(sync_remote_object_content) == bulk_operation.get_count_of_files_in_folder_and_subfolders(
        sync_download_test_dir)


@util.skip_while_rerecording
def test_sync_dest_updated_objects(object_storage_client):
    """
    1. Download all the objects to destination directory
    2. Randomly modify one object with different content (This action would change the size and last modification time)
    3. Randomly another object with same content (This action would just modify the last modified time)
    4. As we sync only based on the above two criteria, the next time we download from the source directory we expect
        the modified files to get transferred to local
    5. Rest of the objects in the remote should get skipped
    """

    download_and_validate_all_objects()

    # re-upload one object with different content
    f_diff_content = random.choice(list(sync_remote_object_content))
    f_same_content = random.choice([o for o in sync_remote_object_content if o != f_diff_content])
    new_content = bulk_operation.generate_random_string(bulk_operation.CONTENT_STRING_LENGTH)
    sync_remote_object_content[f_diff_content] = new_content
    object_storage_client.put_object(util.NAMESPACE, sync_download_bucket_name, f_diff_content, new_content)
    # re-upload another object with same content
    object_storage_client.put_object(util.NAMESPACE, sync_download_bucket_name, f_same_content,
                                     sync_remote_object_content[f_same_content])

    # invoke sync
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['download-failures'] == {}
    assert set(parsed_result['downloaded-objects']) == {f_diff_content, f_same_content}
    assert len(parsed_result['skipped-objects']) == len(sync_remote_object_content.keys()) - 2

    compare_file_content_to_local(sync_remote_object_content, sync_download_test_dir,
                                  files_in_scope=[f_diff_content, f_same_content])


@util.skip_while_rerecording
def test_sync_dest_new_objects(object_storage_client):
    """
    1. Download the files to local and validate the output and file contents
    2. Create a new file in remote
    3. When we try to sync against local again only the new object should get downloaded and
        rest of the objects should get skipped as they are already present in local.
    """

    download_and_validate_all_objects()

    new_object_name = 'a/new_object'
    new_file_contents = {new_object_name: bulk_operation.generate_random_string(bulk_operation.CONTENT_STRING_LENGTH)}
    object_storage_client.put_object(util.NAMESPACE, sync_download_bucket_name, new_object_name,
                                     new_file_contents[new_object_name])

    try:
        result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                        sync_download_bucket_name, '--dest-dir', sync_download_test_dir], debug=debug)
        parsed_result = util.parse_json_response_from_mixed_output(result.output)
        assert parsed_result['download-failures'] == {}
        assert set(parsed_result['downloaded-objects']) == {new_object_name}
        assert len(parsed_result['skipped-objects']) == len(sync_remote_object_content.keys())
        compare_file_content_to_local(new_file_contents, sync_download_test_dir)
    finally:
        object_storage_client.delete_object(util.NAMESPACE, sync_download_bucket_name, new_object_name)


def test_sync_dest_include_dry_run(vcr_fixture, debug):
    """
    1. Select one object from remote and perform a --dry-run by specifying the same file name in --include.
    2. We expect that only this object gets transferred. No other objects gets transferred/skipped.
    """

    # invoke sync with include
    file_name_to_sync = 'Object_0'
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', sync_download_test_dir_recorded, '--include',
                                    file_name_to_sync, '--dry-run'], debug=debug)
    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert downloaded_set == {file_name_to_sync}


def test_sync_dest_include(vcr_fixture, debug):
    """
    1. Select one object from remote and download that by passing that parameter to --include
    2. Validate that only that object got transferred to local. Also, validate the contents of the object
        just to assert that they are the same.
    3. Sync again with --include option and validate that the same object gets skipped now.
    """

    file_name_to_include = 'Object_0'
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', sync_download_test_dir_recorded, '--include',
                                    file_name_to_include], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['download-failures'] == {}
    assert set(parsed_result['downloaded-objects']) == {file_name_to_include}
    assert parsed_result['skipped-objects'] == []
    assert bulk_operation.get_count_of_files_in_folder_and_subfolders(sync_download_test_dir_recorded) == 1
    compare_file_content_to_local(slice_dict_by_key(sync_remote_object_content, {file_name_to_include}, True),
                                  sync_download_test_dir_recorded)

    # try downloading the files again and verify that it's skipped
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', sync_download_test_dir_recorded, '--include',
                                    file_name_to_include], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['download-failures'] == {}
    assert parsed_result['downloaded-objects'] == []
    assert file_name_to_include in parsed_result['skipped-objects']


def test_sync_dest_exclude_dry_run(vcr_fixture, debug):
    """
    1. Select one object from local and perform a --dry-run by specifying it in --exclude
    2. Validate that every other object is in the transfer list except the one in exclude list
    """

    file_name_to_exclude = 'Object_0'
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', sync_download_test_dir_recorded, '--exclude',
                                    file_name_to_exclude, '--dry-run'], debug=debug)
    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(downloaded_set) == len(sync_remote_object_content.keys()) - 1
    assert file_name_to_exclude not in downloaded_set


@util.skip_while_rerecording
def test_sync_dest_exclude(debug):
    """
    1. Select one object from remote and sync against local by specifying it in --exclude
    2. Validate that all other objects except the excluded file gets transferred
    """

    file_name_to_exclude = 'Object_0'
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--exclude',
                                    file_name_to_exclude], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['download-failures'] == {}
    assert file_name_to_exclude not in set(parsed_result['downloaded-objects'])
    assert len(parsed_result['downloaded-objects']) == len(sync_remote_object_content.keys()) - 1
    assert parsed_result['skipped-objects'] == []
    assert bulk_operation.get_count_of_files_in_folder_and_subfolders(sync_download_test_dir) == len(sync_remote_object_content.keys()) - 1
    compare_file_content_to_local(slice_dict_by_key(sync_remote_object_content, {file_name_to_exclude}, False),
                                  sync_download_test_dir)


def test_sync_dest_dir_prefix(vcr_fixture, debug):
    """
    1. Set a prefix to apply to all the transactions during sync
    2. Perform a --dry-run with the prefix applied and verify that all the files in the remote get transferred.
    3. Sync against local with the same prefix and verify that all objects from remote is available in local
        under the specified prefix
    4. Validate the contents of the remote objects against their counter part in local.
    """

    prefix_test_dir = 'prefix'
    prefix_test_path = os.path.join(sync_download_test_dir_recorded, prefix_test_dir)

    prefix_to_sync = 'a/b'
    # perform a dry run the get the objects to be transferred
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', prefix_test_path, '--prefix',
                                    prefix_to_sync, '--dry-run'], debug=debug)

    _, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    count_of_prefixed_files = len(list(filter(lambda f: f.startswith(prefix_to_sync), sync_remote_object_content)))
    assert len(downloaded_set) == count_of_prefixed_files
    assert len(skipped_set) == 0

    # sync with the same prefix and verify that the object doesn't contain the prefix supplied. Also, verify the content
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', prefix_test_path, '--prefix',
                                    prefix_to_sync], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['download-failures'] == {}
    assert set(parsed_result['downloaded-objects']) == set(downloaded_set)
    assert parsed_result['skipped-objects'] == []

    # map and verify the contents from dry-run values
    assert bulk_operation.get_count_of_files_in_folder_and_subfolders(prefix_test_path) == len(downloaded_set)

    new_object_content_map = {}
    for o_name in sync_remote_object_content:
        if o_name in downloaded_set:
            # get the new download destination after removing the prefix
            n_o_name = prefix_test_dir + o_name[len(prefix_to_sync):]
            new_object_content_map[n_o_name] = sync_remote_object_content[o_name]

    compare_file_content_to_local(new_object_content_map, sync_download_test_dir_recorded)


@util.skip_while_rerecording
def test_sync_dest_with_delete(debug):
    """
    1. Perform a --dry-run against a blank local by specifying --delete option.
    2. Verify that all objects gets transferred and nothing gets deleted because there are no extra objects in local.
    3. Download all the objects from remote to local
    4. Create new files in local which are not present in remote
    5. Perform a --dry-run against the updated local with the same parameter as before.
    6. This time all the remote objects should be present in local as we downloaded them earlier so we expect them
        to get skipped
    7. Validate that all the new files created in local from previous step would be in deleted list as they are
        not present in the remote
    8. Perform an actual sync now and validate the above 2 points
    """

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--delete',
                                    '--dry-run'], debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))

    assert len(deleted_set) == 0
    assert len(downloaded_set) == len(sync_remote_object_content.keys())
    assert len(skipped_set) == 0

    download_and_validate_all_objects()
    new_local_file_set = create_new_files_local(sync_download_test_dir, 10)

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--delete',
                                    '--dry-run'], debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))

    assert len(downloaded_set) == 0
    assert len(skipped_set) == len(sync_remote_object_content.keys())
    assert deleted_set == new_local_file_set

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--delete'],
                                   debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['download-failures'] == {}
    assert parsed_result['downloaded-objects'] == []
    assert len(parsed_result['skipped-objects']) == len(sync_remote_object_content.keys())
    assert set(parsed_result['deleted-files']) == new_local_file_set


@util.skip_while_rerecording
def test_sync_dest_with_delete_empty_folders(debug):
    """
    1. Perform a --dry-run against a blank local by specifying --delete option.
    2. Verify that all objects gets transferred and nothing gets deleted because there are no extra objects in local.
    3. Download all the objects from remote to local and note the count of folders in local
    4. Create new empty folders in local
    5. Perform a --dry-run against the updated local with the same parameter as before.
    6. This time all the remote objects should be present in local as we downloaded them earlier so we expect them
        to get skipped
    7. Validate that none of the folders from local are deleted in the dry-run and no. of folders in our local is equal
        to what we created + what we downloaded from remote
    8. Now perform an actual sync with --dest-dir and --delete option
    7. Validate that all the empty folders created locally get deleted and folders downloaded from remote remains
    """

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--delete',
                                    '--dry-run'], debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))

    assert len(deleted_set) == 0
    assert len(downloaded_set) == len(sync_remote_object_content.keys())
    assert len(skipped_set) == 0

    download_and_validate_all_objects()

    local_folders_from_remote = next(os.walk(sync_download_test_dir))[1]  # local folders created due to sync from remote

    new_local_empty_folder_set = create_empty_folders_local(sync_download_test_dir, 10)

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--delete',
                                    '--dry-run'], debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))

    assert len(downloaded_set) == 0
    assert len(skipped_set) == len(sync_remote_object_content.keys())
    assert len(deleted_set) == 0  # As no files are present in dest-dir, only empty folders

    # Validate that no. of folders in dest-dir is equal to the no. of folders created from remote sync + empty folders created locally
    assert len(new_local_empty_folder_set) + len(local_folders_from_remote) == len(
        next(os.walk(sync_download_test_dir))[1])

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--delete'],
                                   debug=debug)

    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['download-failures'] == {}
    assert parsed_result['downloaded-objects'] == []
    assert len(parsed_result['skipped-objects']) == len(sync_remote_object_content.keys())
    assert len(parsed_result['deleted-files']) == 0  # As no files are present in dest-dir, only empty folders

    # Validate that no. of folders in dest-dir are only in remote bucket as there cannot
    # be any empty folder in remote source bucket and
    # sync command was executed with --delete option so all the empty folders in dest-dir should be deleted
    assert len(next(os.walk(sync_download_test_dir))[1]) == len(local_folders_from_remote)


def test_sync_dest_with_delete_and_include(vcr_fixture, object_storage_client):
    """
    1. Create new set of objects in remote with .pdf and .doc extensions.
    2. Perform a dry run with --delete to include only *.pdf and validate that only .pdf files are transferred.
    3. Create new set of files in local with .pdf and .txt extensions.
    4. Perform step:2 again and validate that all .pdf files are transferred but only the .pdf files from local
        gets deleted. Nothing happens to .txt files.
    5. Perform step:2 again including *.pdf and *.doc both and validate that only files matching the pattern gets
        transferred/deleted
    6. Perform actual sync and validate the final output with the ones from the dry-run
    """

    r_obj_set_1 = create_new_objects_remote(object_storage_client, sync_download_bucket_name_recorded, 6, extension='pdf')
    r_obj_set_2 = create_new_objects_remote(object_storage_client, sync_download_bucket_name_recorded, 4, extension='doc')

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', sync_download_test_dir_recorded, '--delete',
                                    '--include', '*.pdf', '--dry-run'], debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert deleted_set == set()
    assert skipped_set == set()
    assert len(downloaded_set) == len(r_obj_set_1)

    l_file_set_1 = create_new_files_local(sync_download_test_dir_recorded, 3, extension='pdf')
    l_file_set_2 = create_new_files_local(sync_download_test_dir_recorded, 5, extension='txt')

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', sync_download_test_dir_recorded, '--delete',
                                    '--include', '*.pdf', '--dry-run'], debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(deleted_set) == len(l_file_set_1)
    assert skipped_set == set()
    assert len(downloaded_set) == len(r_obj_set_1)

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', sync_download_test_dir_recorded, '--delete',
                                    '--include', '*.pdf', '--include', '*.doc', '--dry-run'], debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(deleted_set) == len(l_file_set_1)
    assert skipped_set == set()
    assert len(downloaded_set) == len(r_obj_set_1.union(r_obj_set_2))

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', sync_download_test_dir_recorded, '--delete',
                                    '--include', '*.pdf', '--include', '*.doc'], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['download-failures'] == {}
    assert set(parsed_result['downloaded-objects']) == r_obj_set_1.union(r_obj_set_2)
    assert parsed_result['skipped-objects'] == []
    assert set(parsed_result['deleted-files']) == l_file_set_1

    cleanup_objects_from_remote(object_storage_client, r_obj_set_1.union(r_obj_set_2), sync_download_bucket_name_recorded)


@util.skip_while_rerecording
def test_sync_dest_with_delete_and_exclude(object_storage_client):
    """
    1. Create new set of objects in remote with .pdf and .doc extensions.
    2. Perform a dry run with --delete to exclude only *.pdf and validate that all other files are transferred.
    3. Create new set of files in local with .doc and .txt extensions.
    4. Perform step:2 again excluding *.doc and validate that all files except .doc files gets transferred but
        only .txt files are deleted from local. Nothing happens to .doc file in local
    5. Perform step:2 again including *.pdf and *.doc both and validate that originally created files in the bucket gets
        transferred but only .txt files are deleted from local.
    6. Perform actual sync and validate the final output with the ones from the dry-run
    """

    r_obj_set_1 = create_new_objects_remote(object_storage_client, sync_download_bucket_name, 6, extension='pdf')
    r_obj_set_2 = create_new_objects_remote(object_storage_client, sync_download_bucket_name, 4, extension='doc')

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--delete',
                                    '--exclude', '*.pdf', '--dry-run'], debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert deleted_set == set()
    assert skipped_set == set()
    assert len(downloaded_set) == len(r_obj_set_2) + len(sync_remote_object_content.keys())

    l_file_set_1 = create_new_files_local(sync_download_test_dir, 3, extension='doc')
    l_file_set_2 = create_new_files_local(sync_download_test_dir, 5, extension='txt')

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--delete',
                                    '--exclude', '*.doc', '--dry-run'], debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(deleted_set) == len(l_file_set_2)
    assert skipped_set == set()
    assert len(downloaded_set) == len(r_obj_set_1) + len(sync_remote_object_content.keys())

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--delete',
                                    '--exclude', '*.pdf', '--exclude', '*.doc', '--dry-run'], debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(deleted_set) == len(l_file_set_2)
    assert skipped_set == set()
    assert len(downloaded_set) == len(sync_remote_object_content.keys())

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--delete',
                                    '--exclude', '*.pdf', '--exclude', '*.doc'], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['download-failures'] == {}
    assert set(parsed_result['downloaded-objects']) == set(sync_remote_object_content.keys())
    assert parsed_result['skipped-objects'] == []
    assert set(parsed_result['deleted-files']) == l_file_set_2

    cleanup_objects_from_remote(object_storage_client, r_obj_set_1.union(r_obj_set_2), sync_download_bucket_name)


def test_sync_dest_with_delete_and_prefix(vcr_fixture, debug):
    """
    1. Create an empty directory for prefix test.
    2. Create new files in the prefix directory root which are not present in remote. Make sure the new files created
        also maintains a hierarchical structure.
    3. Perform a --dry-run by assigning a prefix to the sync command.
    4. Validate that only the objects with the prefix are in the downloaded set while new objects not present
        are in deleted list
    5. Perform the actual sync with local
    6. Validate that the objects in the downloaded set actually get downloaded.
    7. Verify that the prefix gets removed while downloading
    8. Verify that the new objects in the deleted list actually gets deleted
    9. Finally, verify the contents of the downloaded object against remote
    """

    prefix_test_dir = 'prefix_delete'
    prefix_test_path = os.path.join(sync_download_test_dir_recorded, prefix_test_dir)

    # create new files which are not present in remote
    new_local_file_set = create_new_files_local(prefix_test_path, 10)

    prefix_to_sync = 'a/b'
    # perform a dry run the get the objects to be transferred
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', prefix_test_path, '--prefix',
                                    prefix_to_sync, '--delete', '--dry-run'], debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    count_of_prefixed_files = len(list(filter(lambda f: f.startswith(prefix_to_sync), sync_remote_object_content)))
    assert len(downloaded_set) == count_of_prefixed_files
    assert len(skipped_set) == 0
    assert deleted_set == new_local_file_set

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', prefix_test_path, '--prefix',
                                    prefix_to_sync, '--delete'], debug=debug)

    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['download-failures'] == {}
    assert len(parsed_result['downloaded-objects']) == count_of_prefixed_files
    assert len(parsed_result['skipped-objects']) == 0
    assert set(parsed_result['deleted-files']) == new_local_file_set
    # verify that prefixes are removed while downloading and validate the file contents
    compare_file_content_to_local({k[len(prefix_to_sync):]: v for k, v in sync_remote_object_content.items()
                                   if k.startswith(prefix_to_sync)}, prefix_test_path)


def test_sync_dest_with_delete_include_and_prefix(vcr_fixture, object_storage_client, debug):
    """
    Assert that scope of file transfer and delete is only limited to --include pattern

    1. Decide on a prefix to sync with.
    2. Create new files in object-storage with the specified prefix and with extensions .pdf and .doc
    3. Perform a --dry-run with --prefix and --include only *.pdf files
    4. Validate that only .pdf objects from the remote with the specified prefix gets downloaded.
    5. Create new files in local with .pdf and .txt extensions
    6. Perform step:3 again and validate same files are transferred but only new .pdf files in local are deleted.
    7. Perform step:3 again including .pdf and .doc files and validate all .pdf and .doc files are transferred
        but only .pdf files are deleted from local.
    """

    _prefix = 'prefix_delete_include'

    r_obj_set_1 = create_new_objects_remote(object_storage_client, sync_download_bucket_name_recorded, 6, extension='pdf',
                                            prefix=_prefix)
    r_obj_set_2 = create_new_objects_remote(object_storage_client, sync_download_bucket_name_recorded, 4, extension='doc',
                                            prefix=_prefix)

    # create other .pdf files in the bucket root just to assert that these are not fetched during download
    r_obj_set_3 = create_new_objects_remote(object_storage_client, sync_download_bucket_name_recorded, 11, extension='pdf',
                                            prefix=None)

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', sync_download_test_dir_recorded, '--delete',
                                    '--include', '*.pdf', '--prefix', _prefix, '--dry-run'], debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert deleted_set == set()
    assert skipped_set == set()
    assert len(downloaded_set) == len(r_obj_set_1)

    # create new files which are not present in remote
    l_file_set_1 = create_new_files_local(sync_download_test_dir_recorded, 3, extension='pdf')
    l_file_set_2 = create_new_files_local(sync_download_test_dir_recorded, 7, extension='txt')

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', sync_download_test_dir_recorded, '--delete',
                                    '--include', '*.pdf', '--prefix', _prefix, '--dry-run'], debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(deleted_set) == len(l_file_set_1)
    assert skipped_set == set()
    assert len(downloaded_set) == len(r_obj_set_1)

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', sync_download_test_dir_recorded, '--delete',
                                    '--include', '*.pdf', '--include', '*.doc', '--dry-run', '--prefix', _prefix],
                                   debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(deleted_set) == len(l_file_set_1)
    assert skipped_set == set()
    assert len(downloaded_set) == len(r_obj_set_1.union(r_obj_set_2))

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name_recorded, '--dest-dir', sync_download_test_dir_recorded, '--delete',
                                    '--include', '*.pdf', '--include', '*.doc', '--prefix', _prefix], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['download-failures'] == {}
    assert set(parsed_result['downloaded-objects']) == r_obj_set_1.union(r_obj_set_2)
    assert parsed_result['skipped-objects'] == []
    assert set(parsed_result['deleted-files']) == l_file_set_1

    cleanup_objects_from_remote(object_storage_client, r_obj_set_1.union(r_obj_set_2).union(r_obj_set_3), sync_download_bucket_name_recorded)


@util.skip_while_rerecording
def test_sync_dest_with_delete_exclude_and_prefix(object_storage_client, debug):
    """
    Assert that scope of file transfer and delete is only limited to --exclude pattern

    1. Decide on a prefix to sync
    2. Create new objects with extension .pdf and .doc and the prefix
    3. Perform a dry run with --delete excluding *.pdf specifying the prefix.
    4. Validate that only .doc files are transferred. Nothing gets deleted at this point.
    5. Create new files in local with .doc and .txt extensions.
    6. Perform step:3 excluding *.doc along with the prefix. Validate that all .pdf files are downloaded but
        only .txt files are deleted. We expect *.doc being excluded from delete as well.
    7. Perform step:3 again excluding *.pdf and *.doc. Validate this time only .txt files get deleted. Nothing is transferred.
    8. Perform actual sync and validate the final output with the previous step.
    """

    _prefix = 'prefix_delete_exclude'

    r_obj_set_1 = create_new_objects_remote(object_storage_client, sync_download_bucket_name, 6, extension='pdf',
                                            prefix=_prefix)
    r_obj_set_2 = create_new_objects_remote(object_storage_client, sync_download_bucket_name, 4, extension='doc',
                                            prefix=_prefix)

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--delete',
                                    '--exclude', '*.pdf', '--prefix', _prefix, '--dry-run'], debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert deleted_set == set()
    assert skipped_set == set()
    assert len(downloaded_set) == len(r_obj_set_2)

    l_file_set_1 = create_new_files_local(sync_download_test_dir, 3, extension='doc')
    l_file_set_2 = create_new_files_local(sync_download_test_dir, 5, extension='txt')

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--delete',
                                    '--exclude', '*.doc', '--prefix', _prefix, '--dry-run'], debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(deleted_set) == len(l_file_set_2)
    assert skipped_set == set()
    assert len(downloaded_set) == len(r_obj_set_1)

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--delete',
                                    '--exclude', '*.pdf', '--exclude', '*.doc', '--prefix', _prefix, '--dry-run'],
                                   debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert len(deleted_set) == len(l_file_set_2)
    assert skipped_set == set()
    assert len(downloaded_set) == 0

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--delete',
                                    '--exclude', '*.pdf', '--exclude', '*.doc', '--prefix', _prefix], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['download-failures'] == {}
    assert set(parsed_result['downloaded-objects']) == set()
    assert parsed_result['skipped-objects'] == []
    assert set(parsed_result['deleted-files']) == l_file_set_2

    cleanup_objects_from_remote(object_storage_client, r_obj_set_1.union(r_obj_set_2), sync_download_bucket_name)


@util.skip_while_rerecording
def test_sync_between_src_and_dest(debug):
    """
    1. Download and validate all objects from the remote
    2. While downloading we set the last modified time of the local file same as remote.
    3. Perform a --dry-run by specifying the --src-dir flag and setting the download directory as source directory.
    4. Validate that all the files in the local are in the skipped list because either the size or
        last m_time of the files wouldn't have changed.
    5. Perform another --dry-run with --src-dir keeping the other param same but adding --delete option and
        validate that all the files are in the skipped list and nothing gets deleted
    6. Finally, perform the actual sync and validate the actually transferred/skipped/deleted objects against
        the ones in dry_run.
    """

    download_and_validate_all_objects()

    # try to sync this directory as source directory with --dry-run and validate that no object is synced
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--src-dir', sync_download_test_dir, '--dry-run'],
                                   debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert deleted_set == set()
    assert uploaded_set == set()
    assert len(skipped_set) == len(sync_remote_object_content.keys())

    # try to sync this directory as source directory with --dry-run and --delete and validate that no object is synced
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--src-dir', sync_download_test_dir, '--dry-run',
                                    '--delete'], debug=debug)
    deleted_set, uploaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert deleted_set == set()
    assert uploaded_set == set()
    assert len(skipped_set) == len(sync_remote_object_content.keys())

    # try to sync this directory as source directory and validate that no object is synced
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--src-dir', sync_download_test_dir], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['uploaded-objects'] == {}
    assert len(parsed_result['skipped-objects']) == len(sync_remote_object_content.keys())

    # try to sync this directory as source directory with --delete and validate that no object is synced
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--src-dir', sync_download_test_dir, '--delete'],
                                   debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['upload-failures'] == {}
    assert parsed_result['uploaded-objects'] == {}
    assert len(parsed_result['skipped-objects']) == len(sync_remote_object_content.keys())


def test_sync_dest_validate_unsupported_params(vcr_fixture, debug):
    """
    Validate that the following parameters can not be specified with --dest-dir:

    ['--cache-control', '--content-disposition', '--content-encoding', '--content-language', '--content-type',
    '--metadata', '--storage-tier']

    """

    unsupported_params = ('--cache-control',
                          '--content-disposition',
                          '--content-encoding',
                          '--content-language',
                          '--content-type',
                          '--metadata',
                          '--storage-tier')

    for unsupported_param in unsupported_params:
        if unsupported_param == '--storage-tier':
            result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                            sync_download_bucket_name_recorded, '--dest-dir', sync_download_test_dir_recorded,
                                            unsupported_param, random.choice(['Standard', 'InfrequentAccess', 'Archive'])],
                                           debug=debug)
        else:
            result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                            sync_download_bucket_name_recorded, '--dest-dir', sync_download_test_dir_recorded,
                                            unsupported_param, generate_random_string(10)], debug=debug)

        assert 'UsageError' in result.output
        assert unsupported_param in result.output
        assert '--dest-dir' in result.output


@util.skip_while_rerecording
def test_sync_dest_skip_archived_objects(object_storage_client, debug):
    """
    1. Upload an archived tier object to the remote using the os client.
    2. Perform a --dry-run against local and validate that the file is present in skipped list.
    3. Next, perform the actual sync and verify that the file is present in the skip list of the output.
    """

    archived_object = 'archived_object'
    object_storage_client.put_object(util.NAMESPACE, sync_download_bucket_name, archived_object,
                                     generate_random_string(10), storage_tier='Archive')

    # Perform a dry-run and validate that the archived object is skipped
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir, '--dry-run'],
                                   debug=debug)

    deleted_set, downloaded_set, skipped_set = parse_dry_run_result(result.output.strip().split('\n'))
    assert any(filter(lambda f_n: archived_object in f_n, skipped_set))

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert any(filter(lambda f_n: archived_object in f_n, parsed_result['skipped-objects']))
    object_storage_client.delete_object(util.NAMESPACE, sync_download_bucket_name, archived_object)


def test_sync_dest_when_bucket_name_is_invalid(vcr_fixture, debug):
    """
    Run the sync command specifying --dest-dir using an invalid bucket name and validate that it throws a ServiceError
    """

    invalid_bucket_name = 'invalid_bucket'
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    invalid_bucket_name, '--dest-dir', sync_download_test_dir_recorded, '--dry-run'], debug=debug)
    assert 'ServiceError:' in result.output
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['status'] == 404
    assert parsed_result['code'] == 'BucketNotFound'

    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    invalid_bucket_name, '--dest-dir', sync_download_test_dir_recorded], debug=debug)
    assert 'ServiceError:' in result.output
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['status'] == 404
    assert parsed_result['code'] == 'BucketNotFound'


def download_and_validate_all_objects():
    result = bulk_operation.invoke(['os', 'object', 'sync', '--namespace', util.NAMESPACE, '--bucket-name',
                                    sync_download_bucket_name, '--dest-dir', sync_download_test_dir], debug=debug)
    parsed_result = util.parse_json_response_from_mixed_output(result.output)
    assert parsed_result['download-failures'] == {}
    assert set(parsed_result['downloaded-objects']) == set(sync_remote_object_content.keys())
    assert parsed_result['skipped-objects'] == []
    compare_file_content_to_local(sync_remote_object_content, sync_download_test_dir)


def compare_file_content_to_local(file_content_map, path_to_test, files_in_scope=None):
    # Ensure that content matches
    for object_name in file_content_map:
        if files_in_scope and object_name not in files_in_scope:
            continue

        if object_name[0] == '/':
            file_path = os.path.join(path_to_test, object_name[1:])
        elif object_name[0:2] == "\\":
            file_path = os.path.join(path_to_test, object_name[2:])
        else:
            file_path = os.path.join(path_to_test, object_name)

        with open(file_path, 'r') as content_file:
            content = content_file.read()
            assert content == file_content_map[object_name]


def create_new_files_local(path, no_of_files_to_create, with_content=False, extension='txt'):
    # write new files in local
    new_local_file_set = set()
    for i in range(no_of_files_to_create):
        if i % 2 == 1:
            new_file_path = os.path.join(path, 'dir', 'new_file_{}.{}'.format(i, extension))
        else:
            new_file_path = os.path.join(path, 'new_file_{}.{}'.format(i, extension))
        Path(os.path.dirname(new_file_path)).mkdir(parents=True, exist_ok=True)
        with open(new_file_path, 'w') as fh:
            if with_content:
                fh.write(bulk_operation.generate_random_string(bulk_operation.CONTENT_STRING_LENGTH))
        new_local_file_set.add(new_file_path.replace(os.sep, '/'))
    return new_local_file_set


def create_empty_folders_local(path, no_of_folders_to_create):
    # create new folders in local
    new_local_folder_set = set()
    for i in range(no_of_folders_to_create):
        new_folder_path = os.path.join(path, 'new_folder_{}/'.format(i))
        Path(os.path.dirname(new_folder_path)).mkdir(parents=True, exist_ok=True)
        new_local_folder_set.add(new_folder_path)
    return new_local_folder_set


def cleanup_files_from_local(file_set):
    for file in file_set:
        if os.path.exists(file):
            os.remove(file)


def create_new_objects_remote(client, bucket_name, no_of_files_to_create, with_content=False, extension='txt',
                              prefix=None):
    new_remote_obj_set = set()
    for i in range(no_of_files_to_create):
        if i % 2 == 1:
            object_name = os.path.join('dir', 'new_obj_{}.{}'.format(i, extension))
        else:
            object_name = 'new_obj_{}.{}'.format(i, extension)
        if prefix:
            object_name = os.path.join(prefix, object_name)
        object_name = object_name.replace(os.sep, '/')
        content = bulk_operation.generate_random_string(bulk_operation.CONTENT_STRING_LENGTH)
        client.put_object(util.NAMESPACE, bucket_name, object_name, content if with_content else '')
        new_remote_obj_set.add(object_name)
    return new_remote_obj_set


def cleanup_objects_from_remote(client, obj_set, bucket_name):
    for obj in obj_set:
        client.delete_object(util.NAMESPACE, bucket_name, obj)


def parse_dry_run_result(parsed_result):
    transferred_set, skipped_set, deleted_set = set(), set(), set()
    for result in parsed_result:
        if result.startswith('Downloading object') or result.startswith('Uploading file'):
            transferred_set.add(result.split(':')[1].strip())
        elif result.startswith('Skipping object') or result.startswith('Skipping file'):
            skipped_set.add(result.split(':')[1].strip())
        elif result.startswith('Deleting file') or result.startswith('Deleting object'):
            deleted_set.add(result.split(':')[1].strip())

    return deleted_set, transferred_set, skipped_set


def slice_dict_by_key(d, key_set, include):
    if include:
        return {k: d[k] for k in d if k in key_set}
    else:
        return {k: d[k] for k in d if k not in key_set}


def generate_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
