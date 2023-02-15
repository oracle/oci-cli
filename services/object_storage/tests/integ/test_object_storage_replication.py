# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import time
import pytest

from tests import util, test_config_container
from services.object_storage.tests.common.constants import CASSETTE_LIBRARY_DIR, DEST_REGION

BUCKET_NAME = 'ObjectStorageReplicationTest'
DEST_BUCKET_NAME = 'ObjectStorageReplicationDest'
POLICY_NAME = 'replication-policy-cli'

object_content_map = {}

created_buckets = 'created_buckets'


@pytest.fixture
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('object_storage_replication_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.fixture(scope='function')
def delete_created_buckets():
    data = {created_buckets: []}
    yield data
    for bucket_name in data[created_buckets]:
        delete_bucket(bucket_name)


def create_test_data(object_storage_client, suffix, delete_created_buckets):
    # Setup test data

    # Create Original Bucket
    source_bucket_name = get_source_bucket_name(suffix)

    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, source_bucket_name)
    util.create_bucket(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, source_bucket_name)
    delete_created_buckets[created_buckets].append(source_bucket_name)

    # Create Destination Bucket
    destination_bucket_name = get_destination_bucket_name(suffix)
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, destination_bucket_name)
    util.create_bucket(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, destination_bucket_name)
    delete_created_buckets[created_buckets].append(destination_bucket_name)

    create_replication_policy(source_bucket_name, destination_bucket_name, POLICY_NAME)

    object_content = 'Sample Content'
    for i in range(3):
        object_name = f'object_{i}'
        object_content_map[object_name] = object_content
        object_storage_client.put_object(util.NAMESPACE, source_bucket_name, object_name, object_content)


def invoke_new(commands, debug=False, ** args):
    if debug is True:
        commands = ['--debug'] + commands
    return util.invoke_command(commands, ** args)


def delete_bucket(bucket_name):
    try:
        invoke_new(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--empty', '--force'])
    except Exception as e:
        pass


def create_replication_policy(bucket_name, dest_bucket, name=POLICY_NAME):
    return invoke_new(['os', 'replication', 'create-replication-policy', '--bucket-name', bucket_name, '--destination-bucket', dest_bucket, '--destination-region', DEST_REGION,
                       '--name', name])


def list_replication_policy(bucket_name):
    return invoke_new(['os', 'replication', 'list-replication-policies', '--bucket-name', bucket_name])


def get_source_bucket_name(suffix):
    return f'{BUCKET_NAME}_{suffix}'


def get_destination_bucket_name(suffix):
    return f'{DEST_BUCKET_NAME}_{suffix}'


def test_basic_replication_command(vcr_fixture, object_storage_client, test_id_recorded, delete_created_buckets):
    suffix = f'basic_{test_id_recorded}'
    source_bucket_name = get_source_bucket_name(suffix)
    create_test_data(object_storage_client, suffix, delete_created_buckets)
    result = list_replication_policy(source_bucket_name)
    response = util.parse_json_response_from_mixed_output(result.output)
    assert response['data'][0]['name'] == POLICY_NAME


def test_delete_main_bucket_and_check_count_in_destination(vcr_fixture, object_storage_client, test_id_recorded, delete_created_buckets):
    suffix = f'count_{test_id_recorded}'
    source_bucket_name = get_source_bucket_name(suffix)
    destination_bucket_name = get_destination_bucket_name(suffix)
    create_test_data(object_storage_client, suffix, delete_created_buckets)
    # object replication is async, increase sleep to 300s if rerecording
    time.sleep(10)
    delete_bucket(source_bucket_name)
    time.sleep(10)
    response = object_storage_client.list_objects(util.NAMESPACE, destination_bucket_name)
    assert len(response.data.objects) == len(object_content_map)


def test_no_delete_bucket_with_replication(vcr_fixture, object_storage_client, test_id_recorded, delete_created_buckets):
    suffix = f'no_delete_{test_id_recorded}'
    source_bucket_name = get_source_bucket_name(suffix)
    create_test_data(object_storage_client, suffix, delete_created_buckets)
    result = invoke_new(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', source_bucket_name, '--force'])
    assert 'ServiceError' in result.output
    assert 'BucketReplicationEnabled' in result.output
