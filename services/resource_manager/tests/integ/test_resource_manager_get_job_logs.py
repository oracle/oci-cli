# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import oci_cli
import pytest
from tests import util
from tests import test_config_container

CASSETTE_LIBRARY_DIR = 'services/resource_manager/tests/cassettes'
RESOURCE_JOB_ID = 'ocid1.ormjob.oc1.phx.aaaaaaaapgn6mmbr2u2ecppspei5go4m6zacv7vbilfpim7qxegr2w3mgyaa'


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('resource_manager_get_job_logs.yml'):
        yield


def test_get_job_logs(runner, config_file, config_profile):
    result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'job', 'get-job-logs',
        '--job-id', RESOURCE_JOB_ID,
        '--all'
    ])
    util.validate_response(result)
    parsed_output = json.loads(result.output)
    assert len(parsed_output['data']) == 34
    assert parsed_output['data'][0]['level'] == 'INFO'
    assert parsed_output['data'][0]['type'] == 'TERRAFORM_CONSOLE'

    result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'job', 'get-job-logs',
        '--job-id', RESOURCE_JOB_ID,
        '--limit', '5'
    ])
    util.validate_response(result)
    assert len(json.loads(result.output)['data']) == 5
    assert 'opc-next-page' in result.output


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, **args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile',
                                                           config_profile] + params, **args)
    else:
        result = runner.invoke(oci_cli.cli,
                               root_params + ['--config-file', config_file, '--profile', config_profile] + params,
                               **args)

    return result
