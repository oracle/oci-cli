# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import oci_cli
import pytest
from tests import util, test_config_container

CASSETTE_LIBRARY_DIR = 'services/object_storage/tests/cassettes'
BUCKET_NAME = None


@pytest.fixture
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('object_list_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.fixture(scope='module', autouse=True)
def test_data(object_storage_client, test_id_recorded):
    # Setup test data
    global BUCKET_NAME
    BUCKET_NAME = f'ObjectListBucket{test_id_recorded}'
    # Create the bucket with 2 objects
    util.clear_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID, BUCKET_NAME)
    util.create_bucket(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID,
                       BUCKET_NAME, objects=['object1', 'object2'])
    yield
    delete_bucket(BUCKET_NAME)


def delete_bucket(bucket_name):
    invoke_new(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--empty', '--force'])


def invoke_new(commands, debug=False, ** args):
    if debug is True:
        commands = ['--debug'] + commands
    return util.invoke_command(commands, ** args)


def test_os_object_list(vcr_fixture, runner, config_file, config_profile):
    params = [
        'os', 'object', 'list',
        '-bn', BUCKET_NAME,
        '--all'
    ]
    result = invoke(runner, config_file, config_profile, params + ['--stream-output'])
    assert result.exit_code == 0
    result_streamed = json.loads(result.output)
    util.validate_response(result)

    result = invoke(runner, config_file, config_profile, params)
    assert result.exit_code == 0
    result_all = json.loads(result.output)
    util.validate_response(result)

    assert len(result_streamed['data'][0]) == len(result_all['data'][0])
    assert len(result_streamed['data'][1]) == len(result_all['data'][1])

    assert len(result_streamed['data']) == len(result_all['data'])


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None,
           strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile',
                                                           config_profile] + params, **args)
    else:
        result = runner.invoke(oci_cli.cli,
                               root_params + ['--config-file', config_file, '--profile', config_profile] + params,
                               **args)

    return result
