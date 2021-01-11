# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import oci_cli
import pytest
from tests import util
from tests import test_config_container

CASSETTE_LIBRARY_DIR = 'services/waas/tests/cassettes'
util.set_admin_pass_phrase()


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('waas_{name}.yml'.format(name=request.function.__name__)):
        yield


def test_policy_crud(runner, config_file, config_profile):
    domain = util.random_name('cli-domain', insert_underscore=False) + '.oci.example.com'
    origin = util.random_name('cli-domain', insert_underscore=False) + '.origin.oci.example.com'

    policy_id = None

    try:
        result = invoke(runner, config_file, config_profile, [
            'waas', 'waas-policy', 'create',
            '--domain', domain,
            '--origins', '{"primary":{"uri":"%s","httpPort":80}}' % origin,
            '--compartment-id', util.COMPARTMENT_ID
        ])
        util.validate_response(result)

        work_request_id = json.loads(result.output)['opc-work-request-id']
        result = invoke(runner, config_file, config_profile, [
            'waas', 'work-request', 'get',
            '--work-request-id', work_request_id
        ])
        util.validate_response(result)

        policy_id = json.loads(result.output)['data']['resources'][0]['identifier']

        util.wait_until(['waas', 'waas-policy', 'get', '--waas-policy-id', policy_id], 'ACTIVE', max_wait_seconds=600)

        params = [
            'waas', 'waas-policy', 'list',
            '-c', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0
    finally:
        if policy_id:
            params = [
                'waas', 'waas-policy', 'delete',
                '--waas-policy-id', policy_id,
                '--force'
            ]

            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile] + params, ** args)

    return result
