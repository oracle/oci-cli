# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import logging
import arrow
import click
import filecmp
import json
import math
import os
import os.path
import pytest
import re
import oci_cli
from tests import util
from tests import test_config_container
from mimetypes import guess_type
import random

CASSETTE_LIBRARY_DIR = 'services/object_storage/tests/cassettes'
CONTENT_INPUT_FILE = 'tests/resources/content_input.txt'
GENERATED_CONTENT_INPUT_FILE = 'tests/temp/generated_content_input.txt'
CONTENT_OUTPUT_FILE = 'tests/resources/content_output.txt'
LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES = 5
DEFAULT_TEST_PART_SIZE = 2
MOVE_BUCKET_TO_COMPARTMENT_ID = os.environ.get('OCI_CLI_MOVE_BUCKET_TO_COMPARTMENT_ID')

created_buckets = 'created_buckets'


@pytest.fixture
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('object_storage_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.fixture
def content_input_file():
    if not os.path.exists(GENERATED_CONTENT_INPUT_FILE):
        util.create_large_file(GENERATED_CONTENT_INPUT_FILE, LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)
    return GENERATED_CONTENT_INPUT_FILE


@pytest.fixture(params=[True, False])
def multipart(request):
    return request.param


@pytest.fixture(params=[True, False])
def debug(request):
    return request.param


@pytest.fixture(scope='module', autouse=True)
def test_data(object_storage_client, test_id):
    # Setup the test data
    util.ensure_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, util.bucket_regional_prefix() + 'Cli' + test_id)
    yield
    try:
        util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, util.bucket_regional_prefix() + 'Cli' + test_id)
    except Exception as ex:
        pass
    bucket_name = util.bucket_regional_prefix() + 'Cli' + test_id + '_test_metadata'
    invoke_new(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--empty', '--force'])


@pytest.fixture(scope='function')
def delete_pending_buckets():
    data = {created_buckets: []}
    yield data
    logging.debug("--------Deleting Created Buckets-----------")
    for bucket_name in data[created_buckets]:
        delete_bucket(bucket_name)


def delete_bucket(bucket_name):
    invoke_new(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--empty', '--force'])


def is_none(value):
    # If the fix for CASPER-10721 is not deployed, then the value for archival-state is returned as UNKNOWN_ENUM_VALUE
    return value is None or (value == 'UNKNOWN_ENUM_VALUE')


def setup_function():
    if os.path.exists(CONTENT_OUTPUT_FILE):
        os.remove(CONTENT_OUTPUT_FILE)


def setup_module():
    if os.getenv('RECORD_ONLY', '') == '1':
        return
    # generate large file for multipart testing
    util.create_large_file(GENERATED_CONTENT_INPUT_FILE, LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)


def teardown_module():
    if os.path.exists(CONTENT_OUTPUT_FILE):
        os.remove(CONTENT_OUTPUT_FILE)

    if os.path.exists(GENERATED_CONTENT_INPUT_FILE):
        os.remove(GENERATED_CONTENT_INPUT_FILE)


@util.skip_while_rerecording
def test_run_all_operations(runner, config_file, config_profile, debug, delete_pending_buckets):
    """Successfully calls every operation with required arguments only."""
    bucket_name = 'cli_temp_bucket_' + str(random.randint(0, 1000000)) + ('_debug' if debug else '_no_debug')
    object_name = 'a'

    # ns get
    result = invoke(runner, config_file, config_profile, ['ns', 'get'], debug=debug)
    validate_response(result, includes_debug_data=debug)
    assert util.NAMESPACE in result.output

    # bucket create
    result = invoke(runner, config_file, config_profile, ['bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name', bucket_name], debug=debug)
    delete_pending_buckets[created_buckets].append(bucket_name)
    validate_response(result, includes_debug_data=debug)

    # bucket get with namespace
    result = invoke(runner, config_file, config_profile, ['bucket', 'get', '-ns', util.NAMESPACE, '--name', bucket_name], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # bucket get without namespace
    result = invoke(runner, config_file, config_profile, ['bucket', 'get', '--name', bucket_name], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # bucket update
    result = invoke(runner, config_file, config_profile, ['bucket', 'update', '-ns', util.NAMESPACE, '--name', bucket_name, '--metadata', '{"foo1":"bar1","key_with_underscore":"value_with_underscore"}'], debug=debug)
    validate_response(result, includes_debug_data=debug)

    assert 'foo1' in result.output
    assert 'key_with_underscore' in result.output
    assert 'value_with_underscore' in result.output

    # remove foo1, keep key_with_underscore
    result = invoke(runner, config_file, config_profile, ['bucket', 'update', '-ns', util.NAMESPACE, '--name', bucket_name, '--metadata', '{"foo1":null}'], debug=debug)
    validate_response(result, includes_debug_data=debug)
    assert 'bar1' not in result.output
    assert 'key_with_underscore' in result.output
    if not debug:
        assert 'foo1' not in result.output

    # bucket list (with both short and long version of compartment-id)
    result = invoke(runner, config_file, config_profile, ['bucket', 'list', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--limit', '10'], debug=debug)
    validate_response(result, includes_debug_data=debug)
    result = invoke(runner, config_file, config_profile, ['bucket', 'list', '-ns', util.NAMESPACE, '-c', util.COMPARTMENT_ID, '--limit', '10'], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # object put
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file', CONTENT_INPUT_FILE], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # object get
    result = invoke(runner, config_file, config_profile, ['object', 'get', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file', CONTENT_OUTPUT_FILE], debug=debug)
    validate_response(result, json_response_expected=False, includes_debug_data=debug)
    assertEqual(get_file_content(CONTENT_INPUT_FILE), get_file_content(CONTENT_OUTPUT_FILE))

    # object head
    result = invoke(runner, config_file, config_profile, ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # object restore status - Available
    result = invoke(runner, config_file, config_profile, ['object', 'restore-status', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name])
    assert 'Available' in result.output

    # object list
    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # object delete
    result = invoke(runner, config_file, config_profile, ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name], input='n', debug=debug)
    assert result.exit_code != 0
    result = invoke(runner, config_file, config_profile, ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name], input='y', debug=debug)
    validate_response(result, json_response_expected=False, includes_debug_data=debug)

    # object put with verify-checksum
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file', CONTENT_INPUT_FILE, '--verify-checksum'], debug=debug)
    validate_response(result, includes_debug_data=debug, json_response_expected=False)
    assert "md5 checksum matches" in result.output

    # object delete
    result = invoke(runner, config_file, config_profile, ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name], input='y', debug=debug)
    validate_response(result, json_response_expected=False, includes_debug_data=debug)

    # object put with default file
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name + '_from_defaults_file', '--defaults-file', 'tests/resources/default_files/specific_command_default'], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # object get with default file
    os.remove(CONTENT_OUTPUT_FILE)
    result = invoke(runner, config_file, config_profile, ['object', 'get', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name + '_from_defaults_file', '--defaults-file', 'tests/resources/default_files/specific_command_default'], debug=debug)
    validate_response(result, json_response_expected=False, includes_debug_data=debug)
    assertEqual(get_file_content(CONTENT_INPUT_FILE), get_file_content(CONTENT_OUTPUT_FILE))

    invoke(runner, config_file, config_profile, ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name + '_from_defaults_file'], input='y', debug=debug)

    # bucket delete
    result = invoke(runner, config_file, config_profile, ['bucket', 'delete', '-ns', util.NAMESPACE, '--name', bucket_name, '--force'], debug=debug)
    validate_response(result, includes_debug_data=debug)
    delete_pending_buckets[created_buckets].remove(bucket_name)


@util.skip_while_rerecording
def test_run_all_ia_operations(runner, config_file, config_profile, debug, delete_pending_buckets):
    """Successfully calls every operation with required arguments only."""
    bucket_name = 'cli_temp_bucket_ia_' + str(random.randint(0, 1000000)) + ('_debug' if debug else '_no_debug')
    object_name = 'a'
    object_name_std = 'a-std'
    object_name_ia = 'a-ia'

    # bucket create
    result = invoke(runner, config_file, config_profile, ['bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name', bucket_name], debug=debug)
    delete_pending_buckets[created_buckets].append(bucket_name)
    validate_response(result, includes_debug_data=debug)

    # object put
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file', CONTENT_INPUT_FILE], debug=debug)
    validate_response(result, includes_debug_data=debug)
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name_std, '--file', CONTENT_INPUT_FILE], debug=debug)
    validate_response(result, includes_debug_data=debug)
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name_ia, '--file', CONTENT_INPUT_FILE, '--storage-tier', 'InfrequentAccess'], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # object head
    result = invoke(runner, config_file, config_profile, ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name])
    validate_response(result)
    head_output = json.loads(result.output)
    assert 'storage-tier' in head_output
    assertEquals('Standard', head_output['storage-tier'])

    result = invoke(runner, config_file, config_profile, ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name_std])
    validate_response(result)
    head_output = json.loads(result.output)
    assert 'storage-tier' in head_output
    assertEquals('Standard', head_output['storage-tier'])

    result = invoke(runner, config_file, config_profile, ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name_ia])
    validate_response(result)
    head_output = json.loads(result.output)
    assert 'storage-tier' in head_output
    assertEquals('InfrequentAccess', head_output['storage-tier'])

    # object update-storage-tier
    result = invoke(runner, config_file, config_profile, ['object', 'update-storage-tier', '-ns', util.NAMESPACE, '-bn', bucket_name, '--object-name', object_name_std, '--storage-tier', 'InfrequentAccess'])
    validate_response(result)
    result = invoke(runner, config_file, config_profile, ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name_std])
    validate_response(result)
    head_output = json.loads(result.output)
    assert 'storage-tier' in head_output
    assertEquals('InfrequentAccess', head_output['storage-tier'])

    # object list
    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name])
    validate_response(result)
    list_json = json.loads(result.output)
    for object_item in list_json['data']:
        if object_item['name'] == object_name:
            assertEquals('Standard', object_item['storage-tier'])
            assert is_none(object_item['archival-state'])
        elif object_item['name'] == object_name_ia:
            assertEquals('InfrequentAccess', object_item['storage-tier'])
            assert is_none(object_item['archival-state'])

    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--fields', 'name,size'])
    validate_response(result)
    json_head = json.loads(result.output)
    for object_item in json_head['data']:
        assert object_item['storage-tier'] is None

    copy_bucket_name = None
    copy_object_name = None
    if not test_config_container.using_vcr_with_mock_responses():
        # Copy object
        # -- create destination bucket
        copy_bucket_name = 'cli_temp_bucket_ia_copy_' + str(random.randint(0, 1000000)) + (
            '_debug' if debug else '_no_debug')
        result = invoke(runner, config_file, config_profile,
                        ['bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name',
                         copy_bucket_name], debug=debug)
        delete_pending_buckets[created_buckets].append(copy_bucket_name)
        validate_response(result, includes_debug_data=debug)
        # -- copy object to the destination bucket
        copy_object_name = 'a-object-copy'
        result = invoke(runner, config_file, config_profile,
                        ['object', 'copy', '-ns', util.NAMESPACE, '-bn', bucket_name, '--source-object-name', object_name,
                         '--destination-bucket', copy_bucket_name, '--destination-object-name', copy_object_name,
                         '--destination-object-storage-tier', 'InfrequentAccess',
                         '--wait-for-state', 'COMPLETED', '--wait-for-state', 'FAILED'], debug=debug)
        # text+JSON is present, removing text to parse JSON
        # TODO: find a better solution
        filtered_output = result.output("Action completed. Waiting until the work request has entered state: ('COMPLETED', 'FAILED')", "")
        validate_response(filtered_output, includes_debug_data=debug)
        # -- verify storage tier of the copied object
        result = invoke(runner, config_file, config_profile, ['object', 'head', '-ns', util.NAMESPACE, '-bn', copy_bucket_name, '--name', copy_object_name])
        validate_response(result)
        head_output = json.loads(result.output)
        assert 'storage-tier' in head_output
        assertEquals('InfrequentAccess', head_output['storage-tier'])

    # object delete
    result = invoke(runner, config_file, config_profile,
                    ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name], input='y',
                    debug=debug)
    validate_response(result, json_response_expected=False, includes_debug_data=debug)
    result = invoke(runner, config_file, config_profile,
                    ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name_std],
                    input='y', debug=debug)
    validate_response(result, json_response_expected=False, includes_debug_data=debug)
    result = invoke(runner, config_file, config_profile,
                    ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name_ia],
                    input='y', debug=debug)
    validate_response(result, json_response_expected=False, includes_debug_data=debug)
    if copy_object_name is not None:
        result = invoke(runner, config_file, config_profile,
                        ['object', 'delete', '-ns', util.NAMESPACE, '-bn', copy_bucket_name, '--name',
                         copy_object_name], input='y', debug=debug)
        validate_response(result, json_response_expected=False, includes_debug_data=debug)

    # bucket delete
    result = invoke(runner, config_file, config_profile,
                    ['bucket', 'delete', '-ns', util.NAMESPACE, '--name', bucket_name, '--force'], debug=debug)
    validate_response(result, includes_debug_data=debug)
    delete_pending_buckets[created_buckets].remove(bucket_name)
    if copy_bucket_name is not None:
        result = invoke(runner, config_file, config_profile,
                        ['bucket', 'delete', '-ns', util.NAMESPACE, '--name', copy_bucket_name, '--force'], debug=debug)
        validate_response(result, includes_debug_data=debug)
        delete_pending_buckets[created_buckets].remove(copy_bucket_name)


@util.skip_while_rerecording
def test_archive_bucket(runner, config_file, config_profile, delete_pending_buckets):
    bucket_name = 'cli_temp_archive_bucket_' + str(random.randint(0, 1000000)) + '_no_debug'
    object_name = 'a'

    # bucket create archive
    result = invoke(runner, config_file, config_profile, ['bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name', bucket_name, '--storage-tier', 'Archive'])
    delete_pending_buckets[created_buckets].append(bucket_name)
    validate_response(result)

    # object put
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file', CONTENT_INPUT_FILE])
    validate_response(result)

    # object get not available
    result = invoke(runner, config_file, config_profile, ['object', 'get', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file', CONTENT_OUTPUT_FILE])
    assert result.exit_code != 0

    # object head and validate archival state
    result = invoke(runner, config_file, config_profile, ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name])
    validate_response(result)
    json_head = json.loads(result.output)
    assertEquals('Archived', json_head['archival-state'])

    # object list and validate archival state
    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name])
    validate_response(result)
    list_json = json.loads(result.output)
    for object_item in list_json['data']:
        assertEquals('Archive', object_item['storage-tier'])
        assertEquals('Archived', object_item['archival-state'])

    # object restore status - Archived
    result = invoke(runner, config_file, config_profile, ['object', 'restore-status', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name])
    assert 'Archived' in result.output

    # object restore
    result = invoke(runner, config_file, config_profile, ['object', 'restore', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name])
    validate_response(result, json_response_expected=False)

    # object head and validate archival state
    result = invoke(runner, config_file, config_profile, ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name])
    validate_response(result)
    json_head = json.loads(result.output)
    assertEquals('Restoring', json_head['archival-state'])

    # object list and validate archival state
    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name])
    validate_response(result)
    list_json = json.loads(result.output)
    for object_item in list_json['data']:
        if object_item['name'] == object_name:
            assertEquals('Restoring', object_item['archival-state'])

    # object restore status - Restoring
    result = invoke(runner, config_file, config_profile, ['object', 'restore-status', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name])
    assert 'Restoring' in result.output

    # object delete
    result = invoke(runner, config_file, config_profile, ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name], input='y')
    validate_response(result, json_response_expected=False)

    result = invoke(runner, config_file, config_profile, ['bucket', 'delete', '-ns', util.NAMESPACE, '--name', bucket_name, '--force'])
    validate_response(result)
    delete_pending_buckets[created_buckets].remove(bucket_name)


def test_move_bucket_to_another_compartment(vcr_fixture, object_storage_client, runner, config_file, config_profile, test_id_recorded, delete_pending_buckets):
    if not MOVE_BUCKET_TO_COMPARTMENT_ID:
        pytest.skip('Skipping as no value was provided for the environment variable OCI_CLI_MOVE_BUCKET_TO_COMPARTMENT_ID')

    bucket_name = 'cli_move_bucket_compartment_{}'.format(test_id_recorded)

    # Create a bucket in the first compartment (given by util.COMPARTMENT_ID)
    result = invoke(runner, config_file, config_profile, ['bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name', bucket_name])
    delete_pending_buckets[created_buckets].append(bucket_name)
    validate_response(result)

    # Make sure that the bucket appears in the first compartment
    all_buckets_response = oci_cli.cli_util.list_call_get_all_results(
        object_storage_client.list_buckets,
        namespace_name=util.NAMESPACE,
        compartment_id=util.COMPARTMENT_ID
    )
    assert_bucket_in_list(bucket_name, all_buckets_response.data)

    # Move the bucket to the other compartment
    result = invoke(runner, config_file, config_profile, ['bucket', 'update', '-ns', util.NAMESPACE, '--name', bucket_name, '--compartment-id', MOVE_BUCKET_TO_COMPARTMENT_ID])
    validate_response(result)

    # The bucket should report itself as being moved to another compartment
    result = invoke(runner, config_file, config_profile, ['bucket', 'get', '-ns', util.NAMESPACE, '--name', bucket_name])
    parsed_result = json.loads(result.output)
    assert MOVE_BUCKET_TO_COMPARTMENT_ID == parsed_result['data']['compartment-id']

    # Listing the bucket in the old compartment does not show our moved bucket
    all_buckets_response = oci_cli.cli_util.list_call_get_all_results(
        object_storage_client.list_buckets,
        namespace_name=util.NAMESPACE,
        compartment_id=util.COMPARTMENT_ID
    )
    assert_bucket_in_list(bucket_name, all_buckets_response.data, invert=True)

    # The moved bucket appears in the target compartment
    all_buckets_response = oci_cli.cli_util.list_call_get_all_results(
        object_storage_client.list_buckets,
        namespace_name=util.NAMESPACE,
        compartment_id=MOVE_BUCKET_TO_COMPARTMENT_ID
    )
    assert_bucket_in_list(bucket_name, all_buckets_response.data)

    # bucket delete
    result = invoke(runner, config_file, config_profile, ['bucket', 'delete', '-ns', util.NAMESPACE, '--name', bucket_name, '--force'])
    validate_response(result)
    delete_pending_buckets[created_buckets].remove(bucket_name)


def test_namespace_metadata(vcr_fixture, runner, config_file, config_profile):
    util.set_admin_pass_phrase()
    result = util.invoke_command_as_admin(['os', 'ns', 'get-metadata', '-ns', util.NAMESPACE])
    util.unset_admin_pass_phrase()
    validate_response(result)
    response = json.loads(result.output)
    assert response["data"]["default-s3-compartment-id"] is not None
    assert response["data"]["default-swift-compartment-id"] is not None


@util.skip_while_rerecording
def test_set_client_request_id(runner, config_file, config_profile):
    input_id = 'examplerequestid'
    result = invoke(runner, config_file, config_profile, ['ns', 'get'], root_params=['--request-id', input_id], debug=True)
    validate_response(result, includes_debug_data=True)
    assert input_id in result.output


def test_bucket_options(vcr_fixture, runner, config_file, config_profile, test_id_recorded, delete_pending_buckets):
    bucket = 'cli_test_bucket_options_' + test_id_recorded

    # bucket create
    result = invoke(runner, config_file, config_profile, ['bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name', bucket])
    delete_pending_buckets[created_buckets].append(bucket)
    validate_response(result)

    # bucket get
    result = invoke(runner, config_file, config_profile, ['bucket', 'get', '-ns', util.NAMESPACE, '--name', bucket])
    response = json.loads(result.output)
    etag = response['etag']

    result = invoke(runner, config_file, config_profile, ['bucket', 'get', '-ns', util.NAMESPACE, '--name', bucket, '--if-match', etag])
    validate_response(result)
    result = invoke(runner, config_file, config_profile, ['bucket', 'get', '-ns', util.NAMESPACE, '--name', bucket, '--if-match', 'blah'])
    util.validate_service_error(result, 'The If-Match header')

    result = invoke(runner, config_file, config_profile, ['bucket', 'get', '-ns', util.NAMESPACE, '--name', bucket, '--if-none-match', 'blah'])
    validate_response(result)
    result = invoke(runner, config_file, config_profile, ['bucket', 'get', '-ns', util.NAMESPACE, '--name', bucket, '--if-none-match', etag])
    util.validate_service_error(result)

    # bucket delete
    result = invoke(runner, config_file, config_profile, ['bucket', 'delete', '-ns', util.NAMESPACE, '--name', bucket, '--if-match', 'blah', '--force'])
    util.validate_service_error(result)
    result = invoke(runner, config_file, config_profile, ['bucket', 'delete', '-ns', util.NAMESPACE, '--name', bucket, '--if-match', etag, '--force'])
    validate_response(result)
    delete_pending_buckets[created_buckets].remove(bucket)


# removing cassette as duplicate call being made, changes replication id
@util.skip_while_rerecording
def test_create_replication_policy(runner, config_file, config_profile, test_id, delete_pending_buckets):
    source_bucket = 'cli_test_create_replication_policy_source_' + test_id
    dest_bucket = 'cli_test_create_replication_policy_dest_' + test_id

    # bucket create
    result = invoke(runner, config_file, config_profile, ['bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name', source_bucket])
    delete_pending_buckets[created_buckets].append(source_bucket)
    validate_response(result)

    # bucket create for replication
    result = invoke(runner, config_file, config_profile, ['bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name', dest_bucket])
    delete_pending_buckets[created_buckets].append(dest_bucket)
    validate_response(result)

    # create policy
    result = invoke(runner, config_file, config_profile, ['replication', 'create-replication-policy', '-ns', util.NAMESPACE, '--name', 'replication-test-policy', '-bn', source_bucket, '--destination-bucket', dest_bucket, '--destination-region', util.OS_REPLICATION_DESTINATION_REGION])
    validate_response(result)
    response = json.loads(result.output)
    replication_id = response['data']['id']
    # delete policy
    result = invoke(runner, config_file, config_profile, ['replication', 'delete-replication-policy', '-ns', util.NAMESPACE, '--replication-id', replication_id, '--bucket-name', source_bucket, '--force'])
    validate_response(result)

    # bucket delete
    result = invoke(runner, config_file, config_profile, ['bucket', 'delete', '-ns', util.NAMESPACE, '--name', source_bucket, '--force'])
    validate_response(result)
    delete_pending_buckets[created_buckets].remove(source_bucket)
    result = invoke(runner, config_file, config_profile, ['bucket', 'delete', '-ns', util.NAMESPACE, '--name', dest_bucket, '--force'])
    validate_response(result)
    delete_pending_buckets[created_buckets].remove(dest_bucket)


@util.skip_while_rerecording
def test_object_put_confirmation_prompt(runner, config_file, config_profile, content_input_file, test_id, multipart):
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket7'
    object_name = 'cli_test_object_put_confirmation_prompt_' + test_id
    put_required_args = ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file', content_input_file]

    if multipart:
        put_required_args = put_required_args + ['--part-size', str(DEFAULT_TEST_PART_SIZE)]

    head_required_args = ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name]
    content_input_file_size = os.path.getsize(content_input_file)

    # Putting the object for the first time should not require a prompt.
    result = invoke(runner, config_file, config_profile, put_required_args)
    validate_response(result)
    json_head = json.loads(invoke(runner, config_file, config_profile, head_required_args).output)
    assertEquals(content_input_file_size, int(json_head['content-length']))
    etag = json_head['etag']

    # Test confirmation prompt accept.
    result = invoke(runner, config_file, config_profile, put_required_args, input='y')
    validate_response(result, json_response_expected=False)
    json_head = json.loads(invoke(runner, config_file, config_profile, head_required_args).output)
    assertEquals(content_input_file_size, int(json_head['content-length']))
    new_etag = json_head['etag']
    assertNotEquals(etag, new_etag)
    etag = new_etag

    # Test confirmation prompt reject.
    result = invoke(runner, config_file, config_profile, put_required_args, input='n')
    assert result.exit_code != 0
    json_head = json.loads(invoke(runner, config_file, config_profile, head_required_args).output)
    # Make sure that etag and content length haven't changed.
    assertEquals(content_input_file_size, int(json_head['content-length']))
    assertEquals(etag, json_head['etag'])

    # Test no-overwrite
    result = invoke(runner, config_file, config_profile, put_required_args + ['--no-overwrite'])
    assert result.exit_code == 0
    json_head = json.loads(invoke(runner, config_file, config_profile, head_required_args).output)
    # Make sure that etag and content length haven't changed.
    assertEquals(content_input_file_size, int(json_head['content-length']))
    assertEquals(etag, json_head['etag'])

    # Test force
    result = invoke(runner, config_file, config_profile, put_required_args + ['--force'])
    validate_response(result)
    new_etag = json.loads(result.output)['etag']
    assertNotEquals(etag, new_etag)
    etag = new_etag
    json_head = json.loads(invoke(runner, config_file, config_profile, head_required_args).output)
    assertEquals(content_input_file_size, int(json_head['content-length']))

    # Test if-match with force
    result = invoke(runner, config_file, config_profile, put_required_args + ['--if-match', etag, '--force'])
    validate_response(result)
    new_etag = json.loads(result.output)['etag']
    assertNotEquals(etag, new_etag)
    etag = new_etag
    json_head = json.loads(invoke(runner, config_file, config_profile, head_required_args).output)
    assertEquals(content_input_file_size, int(json_head['content-length']))

    # Test if-match with force incorrect etag
    result = invoke(runner, config_file, config_profile, put_required_args + ['--if-match', 'incorrect_etag', '--force'])
    assert result.exit_code != 0
    json_head = json.loads(invoke(runner, config_file, config_profile, head_required_args).output)
    # Make sure that etag and content length haven't changed.
    assertEquals(content_input_file_size, int(json_head['content-length']))
    assertEquals(etag, json_head['etag'])

    # Test if-match with incorrect etag
    result = invoke(runner, config_file, config_profile, put_required_args + ['--if-match', 'incorrect_etag'])
    assert result.exit_code != 0
    json_head = json.loads(invoke(runner, config_file, config_profile, head_required_args).output)
    # Make sure that etag and content length haven't changed.
    assertEquals(content_input_file_size, int(json_head['content-length']))
    assertEquals(etag, json_head['etag'])

    # Test if-match with confirmation prompt reject.
    result = invoke(runner, config_file, config_profile, put_required_args + ['--if-match', etag], input='n')
    assert result.exit_code != 0
    json_head = json.loads(invoke(runner, config_file, config_profile, head_required_args).output)
    # Make sure that etag and content length haven't changed.
    assertEquals(content_input_file_size, int(json_head['content-length']))
    assertEquals(etag, json_head['etag'])

    # Test if-match with prompt accept.
    result = invoke(runner, config_file, config_profile, put_required_args + ['--if-match', etag], input='y')
    validate_response(result, json_response_expected=False)
    json_head = json.loads(invoke(runner, config_file, config_profile, head_required_args).output)
    new_etag = json_head['etag']
    assert etag != new_etag
    assert content_input_file_size == int(json_head['content-length'])
    etag = new_etag

    # Test force with verify-checksum
    result = invoke(runner, config_file, config_profile, put_required_args + ['--force', '--verify-checksum'], strip_multipart_stderr_output=False)
    validate_response(result, json_response_expected=False)
    assert "md5 checksum matches" in result.output
    json_head = json.loads(invoke(runner, config_file, config_profile, head_required_args).output)
    new_etag = json_head['etag']
    assert etag != new_etag
    assert content_input_file_size == int(json_head['content-length'])
    etag = new_etag

    # Clean up
    result = invoke(runner, config_file, config_profile, ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--force', '--if-match', etag])
    validate_response(result)


@util.skip_while_rerecording
def test_object_options(runner, config_file, config_profile, test_id, content_input_file, multipart):
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket7'
    object_name = 'cli_test_object_put_options_' + test_id
    required_args = ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file', content_input_file, '--force']

    if multipart:
        required_args = required_args + ['--part-size', str(DEFAULT_TEST_PART_SIZE)]

    head_required_args = ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name]

    # Test object put ifm and md5
    result = invoke(runner, config_file, config_profile, required_args + ['--if-match', 'foo'])
    try:
        util.validate_service_error(result, 'IfMatchFailed')
    except AssertionError as e:
        # known issue with requests: https://github.com/requests/requests/issues/4062
        # ConnectionError is now wrapped as oci.exceptions.RequestException
        util.validate_service_error(result, 'RequestException')
        util.validate_service_error(result, 'EPIPE')

    result = invoke(runner, config_file, config_profile, required_args)
    if result.exit_code is None:
        result.exit_code = 0
    assertEqual(0, result.exit_code)
    json_output = json.loads(result.output)
    etag = json_output['etag']

    result = invoke(runner, config_file, config_profile, required_args + ['--if-match', etag])
    validate_response(result)

    if multipart:
        assert json_output['opc-multipart-md5']
    else:
        md5 = json_output['opc-content-md5']

        # multi part uploads do not take into account --content-md5 param
        result = invoke(runner, config_file, config_profile, required_args + ['--content-md5', 'foo'])
        try:
            util.validate_service_error(result, error_message='The value of the Content-MD5 header')
        except AssertionError as e:
            # known issue with requests: https://github.com/requests/requests/issues/4062
            # ConnectionError is now wrapped as oci.exceptions.RequestException
            util.validate_service_error(result, 'RequestException')
            util.validate_service_error(result, 'EPIPE')

        result = invoke(runner, config_file, config_profile, required_args + ['--content-md5', md5])
        validate_response(result)

    # Test object metadata
    result = invoke(runner, config_file, config_profile, required_args + ['--metadata', '{"foo1":"bar1","foo2":"bar2"}'])
    validate_response(result)
    result = invoke(runner, config_file, config_profile, head_required_args)
    validate_response(result)
    assert 'foo1' in result.output
    assert 'bar2' in result.output

    # Test object auto content-type for file input
    result = invoke(runner, config_file, config_profile, required_args + ['--content-type', 'auto'])
    validate_response(result)
    result = invoke(runner, config_file, config_profile, head_required_args)
    validate_response(result)
    expected_content_type, _ = guess_type(content_input_file)
    assert expected_content_type in result.output

    result = invoke(runner, config_file, config_profile, required_args + ['--metadata', '{"foo2":"bar2"}'])
    validate_response(result)
    result = invoke(runner, config_file, config_profile, head_required_args)
    validate_response(result)
    assert 'foo1' not in result.output
    assert 'foo2' in result.output

    # Test object head ifm and ifnm
    required_args = head_required_args
    etag = json.loads(invoke(runner, config_file, config_profile, required_args).output)['etag']

    result = invoke(runner, config_file, config_profile, required_args + ['--if-match', etag])
    validate_response(result)
    result = invoke(runner, config_file, config_profile, required_args + ['--if-match', 'foo'])
    util.validate_service_error(result)

    # Test object get
    required_args = ['object', 'get', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file', '-']
    result = invoke(runner, config_file, config_profile, required_args)
    validate_response(result, json_response_expected=False)
    # Check that "-f -" writes file content to SDTOUT.
    assert (get_file_content(content_input_file) in result.output)

    result = invoke(runner, config_file, config_profile, required_args + ['--if-match', etag])
    validate_response(result, json_response_expected=False)
    result = invoke(runner, config_file, config_profile, required_args + ['--if-match', 'foo'])
    util.validate_service_error(result)

    result = invoke(runner, config_file, config_profile, required_args + ['--if-none-match', etag])
    util.validate_service_error(result)
    result = invoke(runner, config_file, config_profile, required_args + ['--if-none-match', 'foo'])
    validate_response(result, json_response_expected=False)

    required_args = ['object', 'get', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file', '-']
    result = invoke(runner, config_file, config_profile, required_args + ['--range', 'bytes=2-4'])

    # the two different content input files have different data
    expected_response_data = 'amp' if content_input_file == CONTENT_INPUT_FILE else 'aaa'
    assertEqual(expected_response_data, result.output)

    # Test object delete
    required_args = ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--force']
    result = invoke(runner, config_file, config_profile, required_args + ['--if-match', 'foo'])
    util.validate_service_error(result)
    result = invoke(runner, config_file, config_profile, required_args + ['--if-match', etag])
    validate_response(result)


def subtest_object_list_preserves_prefixes_order(runner, config_file, config_profile, test_id):
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket8'

    # object list
    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--delimiter', '/', '--limit', '3'])
    validate_response(result)

    prefixes = json.loads(result.output)['prefixes']

    # check that they are ordered
    assertListEqual(prefixes, ["a/", "b/", "f/", "s/"])


def subtest_object_list_versions_preserves_prefixes_order(runner, config_file, config_profile, test_id):
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket8'

    # object list
    result = invoke(runner, config_file, config_profile, ['object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name, '--delimiter', '/', '--limit', '3'])
    validate_response(result)

    prefixes = json.loads(result.output)['prefixes']

    # check that they are ordered
    assertListEqual(prefixes, ["a/", "b/", "f/", "s/"])


@util.skip_while_rerecording
def test_object_put_default_name(runner, config_file, config_profile, test_id):
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket7'
    object_name = "TestObject_" + test_id
    filename = os.path.join("tests/temp", object_name)

    with open(filename, 'w') as f:
        f.write("Test object content")

    put_required_args = ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--file',
                         filename, '--force']
    put_result = invoke(runner, config_file, config_profile, put_required_args)
    validate_response(put_result)

    # get object to confirm it exists with expected name
    get_result = invoke(runner, config_file, config_profile, ['object', 'get', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file', '-'])
    validate_response(get_result, json_response_expected=False)

    # delete object to clean up
    delete_required_args = ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name,
                            '--force']
    invoke(runner, config_file, config_profile, delete_required_args)

    # remove file to cleanup
    os.remove(filename)


@util.skip_while_rerecording
def test_object_put_from_stdin(runner, config_file, config_profile, test_id):
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket7'
    object_name = "TestObject_" + test_id
    filename = os.path.join("tests/temp", object_name)

    with open(filename, 'w') as f:
        f.write("Test object content")

    with open(filename, 'r') as f:
        put_required_args = ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--force', '--file',
                             '-', '--name', object_name]

        # supply object content file through stdin
        put_result = invoke(runner, config_file, config_profile, put_required_args, input=f)
        print(put_result.output)

    validate_response(put_result)

    assert json.loads(put_result.output)['opc-content-md5'] == 'H8BEg3FCR+1WmoYYrQbc2Q=='

    # delete object to clean up
    delete_required_args = ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name,
                            '--force']
    invoke(runner, config_file, config_profile, delete_required_args)

    # remove file to cleanup
    os.remove(filename)


@util.skip_while_rerecording
def test_object_put_empty_file(runner, config_file, config_profile, test_id):
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket7'
    object_name = "TestEmptyObject_" + test_id
    filename = os.path.join("tests/temp", object_name)

    with open(filename, 'w') as f:
        pass

    with open(filename, 'r') as f:
        put_required_args = ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--force', '--file',
                             '-', '--name', object_name]

        # supply object content file through stdin
        put_result = invoke(runner, config_file, config_profile, put_required_args, input=f)
        print(put_result.output)

    validate_response(put_result)

    assert json.loads(put_result.output)['opc-content-md5'] == '1B2M2Y8AsgTpgAmY7PhCfg=='

    put_required_args = ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--force', '--file',
                         filename, '--name', object_name]

    # supply file through filename
    put_result = invoke(runner, config_file, config_profile, put_required_args)
    print(put_result.output)
    validate_response(put_result)
    assert json.loads(put_result.output)['opc-content-md5'] == '1B2M2Y8AsgTpgAmY7PhCfg=='

    # delete object to clean up
    delete_required_args = ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name,
                            '--force']
    invoke(runner, config_file, config_profile, delete_required_args)

    # remove file to cleanup
    os.remove(filename)


@util.skip_while_rerecording
def test_object_put_from_stdin_with_auto_content_type(runner, config_file, config_profile, test_id):
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket7'
    object_name = "TestObject_" + test_id + ".txt"
    filename = os.path.join("tests/temp", object_name)

    with open(filename, 'w') as f:
        f.write("Test object content")

    with open(filename, 'r') as f:
        put_required_args = ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--force', '--file',
                             '-', '--name', object_name, '--content-type', 'auto']

        # supply object content file through stdin
        put_result = invoke(runner, config_file, config_profile, put_required_args, input=f)

    validate_response(put_result)

    head_required_args = ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name]
    result = invoke(runner, config_file, config_profile, head_required_args)
    expected_content_type, _ = guess_type(object_name)
    assert expected_content_type in result.output

    # delete object to clean up
    delete_required_args = ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name,
                            '--force']
    invoke(runner, config_file, config_profile, delete_required_args)

    # remove file to cleanup
    os.remove(filename)


# Tests for guess_type returns None for object_name.
@util.skip_while_rerecording
def test_object_put_from_stdin_with_invalid_object_name_extension_one(runner, config_file, config_profile, test_id):
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket7'
    object_name = "TestObject_" + test_id + ".zzzzz"
    filename = os.path.join("tests/temp", object_name)

    with open(filename, 'w') as f:
        f.write("Test object content")

    with open(filename, 'r') as f:
        put_required_args = ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--force', '--file',
                             '-', '--name', object_name, '--content-type', 'auto']

        # supply object content file through stdin
        put_result = invoke(runner, config_file, config_profile, put_required_args, input=f)

    validate_response(put_result)

    head_required_args = ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name]
    result = invoke(runner, config_file, config_profile, head_required_args)

    assert "application/octet-stream" in result.output

    # delete object to clean up
    delete_required_args = ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name,
                            '--force']
    invoke(runner, config_file, config_profile, delete_required_args)

    # remove file to cleanup
    os.remove(filename)


# Object Name extension mismatches with the input contents.
@util.skip_while_rerecording
def test_object_put_from_stdin_with_invalid_object_name_extension_two(runner, config_file, config_profile, test_id):
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket7'
    object_name = "TestObject_" + test_id + ".txt"
    filename = os.path.join("tests/temp", object_name)

    with open(filename, 'wb') as f:
        f.write("Test object content".encode('utf-8'))

    with open(filename, 'r') as f:
        put_required_args = ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--force', '--file',
                             '-', '--name', object_name, '--content-type', 'auto']

        # supply object content file through stdin
        put_result = invoke(runner, config_file, config_profile, put_required_args, input=f)

    validate_response(put_result)

    head_required_args = ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name]
    result = invoke(runner, config_file, config_profile, head_required_args)
    expected_content_type, _ = guess_type(object_name)
    assert expected_content_type in result.output

    # delete object to clean up
    delete_required_args = ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name,
                            '--force']
    invoke(runner, config_file, config_profile, delete_required_args)

    # remove file to cleanup
    os.remove(filename)


@util.skip_while_rerecording
def test_object_put_from_stdin_requires_object_name(runner, config_file, config_profile, test_id):
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket7'
    put_required_args = ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--file', '-', '--force']
    put_result = invoke(runner, config_file, config_profile, put_required_args)

    assert 'UsageError' in put_result.output


@pytest.mark.parametrize('content_type,content_language,content_encoding', [{'image/gif', 'en', 'gzip'}, {'notarealtype', 'notareallanguage', 'notarealencoding'}, {'text/html; charset=ISO-8859-4', 'mi, en', 'compress'}])
@util.skip_while_rerecording
def test_object_content_headers(runner, config_file, config_profile, content_type, content_language, content_encoding, content_input_file, test_id, multipart):
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket7'
    object_name = 'cli_test_object_put_options_' + test_id
    put_required_args = ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file',
                         content_input_file, '--force']

    if multipart:
        put_required_args = put_required_args + ['--part-size', str(DEFAULT_TEST_PART_SIZE)]

    # Put an object with content headers set.
    result = invoke(runner, config_file, config_profile, put_required_args + ['--content-type', content_type, '--content-language', content_language, '--content-encoding', content_encoding])
    validate_response(result)

    # Head - ensure we get the same headers back.
    result = invoke(runner, config_file, config_profile, ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name])
    json_response = json.loads(result.output)
    assertEqual(content_type, json_response['content-type'])
    assertEqual(content_language, json_response['content-language'])
    assertEqual(content_encoding, json_response['content-encoding'])

    # Get - ensure that there is no attempt to decode based on the encoding header. (The file is not actually a gzip,
    # so this would fail if it attempts to decode.)
    result = invoke(runner, config_file, config_profile, ['object', 'get', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file', '-'])
    validate_response(result, json_response_expected=False)
    # Check that "-f -" writes file content to SDTOUT.
    assert (get_file_content(content_input_file) in result.output)

    # cleanup
    required_args = ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--force']
    result = invoke(runner, config_file, config_profile, required_args)
    validate_response(result)


def test_list_options(vcr_fixture, runner, config_file, config_profile, object_storage_client, test_id_recorded):
    subtest_bucket_list(runner, config_file, config_profile)
    subtest_object_list(runner, config_file, config_profile, test_id_recorded)
    subtest_object_list_preserves_prefixes_order(runner, config_file, config_profile, test_id_recorded)
    subtest_object_list_paging(runner, config_file, config_profile, test_id_recorded)
    subtest_object_list_versions(runner, config_file, config_profile, test_id_recorded)
    subtest_object_list_versions_preserves_prefixes_order(runner, config_file, config_profile, test_id_recorded)
    subtest_object_list_versions_paging(runner, config_file, config_profile, test_id_recorded)


def test_bucket_list_with_tags(vcr_fixture, runner, config_file, config_profile):
    result_tags_not_requested = invoke(runner, config_file, config_profile, ['bucket', 'list', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID])
    parsed_data = json.loads(result_tags_not_requested.output)

    for bucket_summary in parsed_data['data']:
        assert bucket_summary['defined-tags'] is None
        assert bucket_summary['freeform-tags'] is None

    result_tags_requested = invoke(runner, config_file, config_profile, ['bucket', 'list', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--fields', 'tags'])
    parsed_data = json.loads(result_tags_requested.output)

    for bucket_summary in parsed_data['data']:
        assert bucket_summary['defined-tags'] is not None
        assert bucket_summary['freeform-tags'] is not None


@util.skip_while_rerecording
def test_copy_object(runner, config_file, config_profile, test_id):
    result = invoke(runner, config_file, config_profile, ['object', 'copy'])
    assert "Error: Missing option" in result.output
    assert "bucket-name" in result.output
    assert "source-object-name" in result.output
    assert "destination-bucket" in result.output
    assert "destination-object-name" not in result.output
    assert "destination-namespace" not in result.output
    assert "destination-region" not in result.output


def subtest_bucket_list(runner, config_file, config_profile):
    """Tests all optional parameters for oci bucket list."""
    result = invoke(runner, config_file, config_profile, ['bucket', 'list', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--limit', '1'])
    validate_response(result)
    assertEqual(1, result.output.count('"namespace"'))

    result = invoke(runner, config_file, config_profile, ['bucket', 'list', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--limit', '1000'])
    validate_response(result)
    assert result.output.count('"namespace"') > 5
    assert result.output.count('"namespace"') <= 1000

    result = invoke(runner, config_file, config_profile, ['bucket', 'list', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--limit', '20'])
    validate_response(result)
    assertEqual(20, result.output.count('"namespace"'))
    assert 'opc-next-page' in result.output

    # Test that --page option works
    result = invoke(runner, config_file, config_profile, ['bucket', 'list', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--limit', '3'])
    validate_response(result)
    output = json.loads(result.output)
    # Verify we got 3 buckets back, don't preform the test if there isn't enough buckets.
    if len(output["data"]) == 3:
        bucketName = output["data"][2]["name"]
        result = invoke(runner, config_file, config_profile, ['bucket', 'list', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--limit', '2'])
        validate_response(result)
        output = json.loads(result.output)
        assert "opc-next-page" in output
        page = output["opc-next-page"]
        result = invoke(runner, config_file, config_profile,
                        ['bucket', 'list', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--limit', '2', '--page', page])
        validate_response(result)
        output = json.loads(result.output)
        assert output["data"][0]["name"] == bucketName


def subtest_object_list(runner, config_file, config_profile, test_id):
    """Tests all optional parameters for oci object list."""
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket6'
    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '1'])
    validate_response(result)
    assertEqual(1, result.output.count('"name"'))

    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '10000'])
    validate_response(result)
    assert result.output.count('"name"') > 100
    assert result.output.count('"name"') < 10000
    assert 'next-start-with' not in result.output

    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '105'])
    validate_response(result)
    assertEqual(105, result.output.count('"name"'))
    # Ensure next_start is shown when limit is less than total number of objects, but greater than
    # the page sized used internally by object list.
    assert 'next-start-with' in result.output

    # Should get 100..109, 10.
    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--prefix', 'ob10'])
    validate_response(result)
    assertEqual(11, result.output.count('"name"'))

    # Should get 102, 103
    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--start', 'ob102', '--end', 'ob104'])
    validate_response(result)
    assertEqual(2, result.output.count('"name"'))
    assert 'next-start-with' not in result.output

    # Same as previous, but with a limit of 1. We should now get a next_start_with token.
    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--start', 'ob102', '--end', 'ob104', '--limit', '1'])
    validate_response(result)
    assertEqual(1, result.output.count('"name"'))
    assert 'next-start-with' in result.output

    # Should get 102, 103
    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '1'])
    validate_response(result)
    assertEqual(1, result.output.count('"name"'))
    assert 'next-start-with' in result.output

    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '2'])
    validate_response(result)
    assertEqual(2, result.output.count('"name"'))
    assert 'next-start-with' in result.output

    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--start', 'ob2', '--limit', '1'])
    validate_response(result)
    assertEqual(1, result.output.count('"name"'))
    assert 'next-start-with' in result.output

    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket2'
    # Should return objects "a/b/object4", "a/b/object5", and prefixe "a/b/c/".
    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--delimiter', '/', '--prefix', 'a/b/'])
    validate_response(result)
    assert "a/b/object4" in result.output
    assert "a/b/object5" in result.output
    assert "a/b/c/" in result.output

    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '1', '--fields', ''])
    validate_response(result)
    assert '"md5": null' in result.output
    assert '"size": null' in result.output
    assert '"time-created": null' in result.output

    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '1', '--fields', 'md5,size,timeCreated'])
    validate_response(result)
    assert '"md5": null' not in result.output
    assert '"size": null' not in result.output
    assert '"time-created": null' not in result.output


def subtest_object_list_versions(runner, config_file, config_profile, test_id):
    """Tests all optional parameters for oci object list-object-versions."""
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket6'
    result = invoke(runner, config_file, config_profile, ['object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name, '--fields', 'name,size,md5,storageTier', '--limit', '1'])
    validate_response(result)
    assertEqual(1, result.output.count('"name"'))
    list_objects = json.loads(result.output)
    assertEquals('Standard', list_objects['data'][0]['storage-tier'])

    result = invoke(runner, config_file, config_profile, ['object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '10000'])
    validate_response(result)
    assert result.output.count('"name"') > 100
    assert result.output.count('"name"') < 10000
    assert 'opc-next-page' not in result.output

    result = invoke(runner, config_file, config_profile, ['object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '105'])
    validate_response(result)
    assertEqual(105, result.output.count('"name"'))
    # Ensure next_start is shown when limit is less than total number of objects, but greater than
    # the page sized used internally by object list.
    assert 'opc-next-page' in result.output

    # Should get 100..109, 10.
    result = invoke(runner, config_file, config_profile, ['object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name, '--prefix', 'ob10'])
    validate_response(result)
    assertEqual(11, result.output.count('"name"'))

    # Should get 102, 103
    result = invoke(runner, config_file, config_profile, ['object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name, '--start', 'ob102', '--end', 'ob104'])
    validate_response(result)
    assertEqual(2, result.output.count('"name"'))
    assert 'opc-next-page' not in result.output

    # Same as previous, but with a limit of 1. We should now get a opc-next-page token.
    result = invoke(runner, config_file, config_profile, ['object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name, '--start', 'ob102', '--end', 'ob104', '--limit', '1'])
    validate_response(result)
    assertEqual(1, result.output.count('"name"'))
    assert 'opc-next-page' in result.output

    # Should get 102, 103
    result = invoke(runner, config_file, config_profile, ['object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '1'])
    validate_response(result)
    assertEqual(1, result.output.count('"name"'))
    assert 'opc-next-page' in result.output

    result = invoke(runner, config_file, config_profile, ['object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '2'])
    validate_response(result)
    assertEqual(2, result.output.count('"name"'))
    assert 'opc-next-page' in result.output

    result = invoke(runner, config_file, config_profile, ['object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name, '--start', 'ob2', '--limit', '1'])
    validate_response(result)
    assertEqual(1, result.output.count('"name"'))
    assert 'opc-next-page' in result.output

    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket2'
    # Should return objects "a/b/object4", "a/b/object5", and prefixe "a/b/c/".
    result = invoke(runner, config_file, config_profile, ['object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name, '--delimiter', '/', '--prefix', 'a/b/'])
    validate_response(result)
    assert "a/b/object4" in result.output
    assert "a/b/object5" in result.output
    assert "a/b/c/" in result.output

    result = invoke(runner, config_file, config_profile, ['object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '1', '--fields', ''])
    validate_response(result)
    assert '"md5": null' in result.output
    assert '"size": null' in result.output
    assert '"time-created": null' in result.output

    result = invoke(runner, config_file, config_profile, ['object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '1', '--fields', 'md5,size,timeCreated'])
    validate_response(result)
    assert '"md5": null' not in result.output
    assert '"size": null' not in result.output
    assert '"time-created": null' not in result.output


def subtest_object_list_paging(runner, config_file, config_profile, test_id):
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket6'

    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '10000'])
    validate_response(result)
    list_size = result.output.count('"name"')

    page_size = 15
    pages = 0
    count = 0
    next_start = None
    while True:
        args = ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', str(page_size)]
        if next_start:
            args.extend(['--start', next_start])
        result = invoke(runner, config_file, config_profile, args)

        validate_response(result)
        count = count + result.output.count('"name"')
        pages = pages + 1

        # Safety check to make sure we don't end up in an infinite loop.
        assert (pages < 30)

        next_start = json.loads(result.output).get('next-start-with', None)
        if not next_start:
            break

    assertEqual(list_size, count)
    assert (pages == math.ceil(float(list_size) / page_size))


def subtest_object_list_versions_paging(runner, config_file, config_profile, test_id):
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id}ReadOnlyTestBucket6'

    result = invoke(runner, config_file, config_profile, ['object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '10000'])
    validate_response(result)
    list_size = result.output.count('"name"')

    page_size = 15
    pages = 0
    count = 0
    next_start = None
    while True:
        args = ['object', 'list-object-versions', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', str(page_size)]
        if next_start:
            args.extend(['--page', next_start])
        result = invoke(runner, config_file, config_profile, args)

        validate_response(result)
        count = count + result.output.count('"name"')
        pages = pages + 1

        # Safety check to make sure we don't end up in an infinite loop.
        assert (pages < 30)

        next_start = json.loads(result.output).get('opc-next-page', None)
        if not next_start:
            break

    assertEqual(list_size, count)
    assert (pages == math.ceil(float(list_size) / page_size))


def test_preauthenticated_requests(vcr_fixture, runner, config_file, config_profile, test_id_recorded):
    preauthenticated_request_name_1 = util.random_name('cli_preauth_request_1')
    preauthenticated_request_name_2 = util.random_name('cli_preauth_request_2')
    bucket_name = util.bucket_regional_prefix() + f'Cli{test_id_recorded}ReadOnlyTestBucket6'

    target_year = 2100
    target_date_for_epoch_timestamp = arrow.now().replace(year=target_year)

    expiry_time_input_and_expected = [
        # TODO: Enable this case
        # {'input': target_date_for_epoch_timestamp.format('X'), 'expected': target_date_for_epoch_timestamp.replace(microsecond=0)},
        {'input': '{}-10-10'.format(target_year), 'expected': arrow.Arrow(target_year, 10, 10, 0, 0, 0, 0, tzinfo='utc')},
        {'input': '{}-05-31T17:15:15.123+08:00'.format(target_year), 'expected': arrow.Arrow(target_year, 5, 31, 17, 15, 15, 123000, tzinfo='+08:00')},
        {'input': '{}-06-01T06:15:15-07:00'.format(target_year), 'expected': arrow.Arrow(target_year, 6, 1, 6, 15, 15, 0, tzinfo='-07:00')},
        {'input': '{}-12-31T00:15:15.444Z'.format(target_year), 'expected': arrow.Arrow(target_year, 12, 31, 0, 15, 15, 444000, tzinfo='utc')},
        {'input': '{}-11-30T06:15:15Z'.format(target_year), 'expected': arrow.Arrow(target_year, 11, 30, 6, 15, 15, 0, tzinfo='utc')},
    ]

    for item in expiry_time_input_and_expected:
        # create PAR
        par_id_1 = create_and_validate_bucket_level_par(runner, config_file, config_profile, preauthenticated_request_name_1, bucket_name, item['input'], item['expected'])
        par_id_2 = create_and_validate_bucket_level_par(runner, config_file, config_profile, preauthenticated_request_name_2, bucket_name, item['input'], item['expected'])

        # get PAR
        result = invoke(runner, config_file, config_profile, ['preauth-request', 'get', '-ns', util.NAMESPACE, '-bn', bucket_name, '--par-id', par_id_1])
        validate_response(result)

        # list PAR
        result = invoke(runner, config_file, config_profile, ['preauth-request', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name])
        validate_response(result)

        # list PAR variant with --all
        result = invoke(runner, config_file, config_profile, ['preauth-request', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--all'])
        validate_response(result)
        assert 'opc-next-page' not in result.output

        # list PAR variant with --limit
        result = invoke(runner, config_file, config_profile, ['preauth-request', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name, '--limit', '1'])
        validate_response(result)
        assert 'opc-next-page' in result.output

        # delete PARs
        result = invoke(runner, config_file, config_profile, ['preauth-request', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--par-id', par_id_1, '--force'])
        validate_response(result)

        result = invoke(runner, config_file, config_profile, ['preauth-request', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--par-id', par_id_2, '--force'])
        validate_response(result)


# Function to invoke commands in a newer manner
def invoke_new(commands, debug=False, ** args):
    if debug is True:
        commands = ['--debug'] + commands
    return util.invoke_command(commands, ** args)


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile, 'os'] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile, 'os'] + params, ** args)

    # many object storage operations output a progress bar in stderr but click doesnt differentiate between
    # stdout and stderr in result.output so we have to strip it out in order to validate the json response
    if strip_progress_bar and ('Uploading object' in result.output or 'Downloading object' in result.output):
        cleaned_output = result.output.replace('Uploading object', '').replace('Downloading object', '')
        try:
            new_output_bytes = bytes(cleaned_output, result.runner.charset)
        except TypeError:
            new_output_bytes = cleaned_output
        finally:
            result = click.testing.Result(result.runner, new_output_bytes, result.exit_code, result.exception, result.exc_info)

    # multipart uploads print out an upload ID and information when each part is uploaded successfully
    # for doing validation we need to strip this out
    if strip_multipart_stderr_output and result.output.startswith('Upload ID: '):
        cleaned_output = re.search('{(.*)}', result.output.replace('\n', '')).group(0)
        try:
            new_output_bytes = bytes(cleaned_output, result.runner.charset)
        except TypeError:
            new_output_bytes = cleaned_output
        finally:
            result = click.testing.Result(result.runner, new_output_bytes, result.exit_code, result.exception, result.exc_info)

    return result


@util.skip_while_rerecording
def test_get_object_multipart_download(runner, config_file, config_profile, test_id, object_storage_client, delete_pending_buckets):
    test_file_path = os.path.join('tests', 'temp', 'for_multipart_download_{}.bin'.format(test_id))
    util.create_large_file(test_file_path, 400)

    bucket_name = 'cli_temp_bucket_' + test_id
    object_name = 'for_multipart_download_{}'.format(test_id)
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, bucket_name)

    # bucket create
    result = invoke(runner, config_file, config_profile, ['bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name', bucket_name])
    delete_pending_buckets[created_buckets].append(bucket_name)
    validate_response(result)
    # put the test object in the bucket
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file', test_file_path])
    validate_response(result)

    # download the object with multipart options
    download_file_path = os.path.join('tests', 'temp', 'result_for_multipart_download_{}.bin'.format(test_id))
    result = invoke(
        runner,
        config_file,
        config_profile,
        ['object', 'get', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file', download_file_path, '--multipart-download-threshold', '200', '--debug']
    )
    validate_response(result, json_response_expected=False)
    if not filecmp.cmp(test_file_path, download_file_path):
        print('Result: {}'.format(result.output))
        print('{} size: {}'.format(test_file_path, os.path.getsize(test_file_path)))
        print('{} size: {}'.format(download_file_path, os.path.getsize(test_file_path)))

        pytest.fail('Files {} and {} are not equal'.format(test_file_path, download_file_path))

    os.remove(test_file_path)
    os.remove(download_file_path)

    result = invoke(runner, config_file, config_profile, ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--force'])
    validate_response(result, json_response_expected=False)

    result = invoke(runner, config_file, config_profile, ['bucket', 'delete', '-ns', util.NAMESPACE, '--name', bucket_name, '--force'])
    validate_response(result, json_response_expected=False)
    delete_pending_buckets[created_buckets].remove(bucket_name)


def get_file_content(filename):
    with open(filename, 'r') as file:
        return file.read()


def extra_response_validation(result):
    assert 'opc-client-request-id' in result.output


def validate_response(result, includes_debug_data=False, json_response_expected=True):
    extra_validation = None
    if includes_debug_data:
        extra_validation = extra_response_validation
    util.validate_response(result, extra_validation=extra_validation, includes_debug_data=includes_debug_data, json_response_expected=json_response_expected)


def create_and_validate_bucket_level_par(runner, config_file, config_profile, preauthenticated_request_name, bucket_name, specified_date, expected_arrow_date):
    result = invoke(runner, config_file, config_profile, ['preauth-request', 'create', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', preauthenticated_request_name, '--access-type', 'AnyObjectWrite', '--time-expires', specified_date])
    validate_response(result)

    response = json.loads(result.output)
    assert response['data']['id'] is not None
    assert response['data']['access-uri'] is not None
    assert response['data']['time-created'] is not None
    assert response['data']['object-name'] is None  # Bucket PARs don't have a referenced object
    assert response['data']['access-type'] == 'AnyObjectWrite'
    assert response['data']['name'] == preauthenticated_request_name

    # RFC3339 date. Currently we always emit the date in UTC so we coerce the expected data passed to this method
    if expected_arrow_date.microsecond == 0:
        assert response['data']['time-expires'] == expected_arrow_date.to('utc').format('YYYY-MM-DDTHH:mm:ssZZ')
    else:
        assert response['data']['time-expires'] == expected_arrow_date.to('utc').format('YYYY-MM-DDTHH:mm:ss.SSSSSSZZ')

    par_id = response['data']['id']

    return par_id


def assert_bucket_in_list(bucket_name, bucket_list, invert=False):
    found_bucket = False
    for bucket in bucket_list:
        if bucket.name == bucket_name:
            found_bucket = True
            break

    # We can invert the logic by passing the invert parameter as True to this method. The default behaviour is to
    # check that the bucket is in the list, so the inverse is to make sure that it isn't in the list
    if not invert:
        assert found_bucket
    else:
        assert not found_bucket


# TODO: clean up and remove all of these which are drop in replacements for unittest validations
def assertEqual(a, b):
    assert a == b


def assertEquals(a, b):
    assertEqual(a, b)


def assertListEqual(a, b):
    if len(a) != len(b):
        return False

    equal = True
    for i in range(0, len(a)):
        equal = equal and a[i] == b[i]

    return equal


def assertNotEquals(a, b):
    assert not a == b
