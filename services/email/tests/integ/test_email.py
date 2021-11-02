# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import oci_cli
import pytest
from tests import util
from tests import test_config_container

CASSETTE_LIBRARY_DIR = 'services/email/tests/cassettes'

util.set_admin_pass_phrase()


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('email_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.mark.skip("Failing due to matcher update")
def test_sender_crud(runner, config_file, config_profile):
    sender_id = None
    try:
        params = [
            'email', 'sender', 'create',
            '--email-address', util.random_name('clisender', insert_underscore=False) + '@oracle.com',
            '--compartment-id', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        sender_id = json.loads(result.output)['data']['id']

        util.wait_until(['email', 'sender', 'get', '--sender-id', sender_id], 'ACTIVE', max_wait_seconds=600)

        params = [
            'email', 'sender', 'list',
            '-c', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0
    finally:
        if sender_id:
            params = [
                'email', 'sender', 'delete',
                '--sender-id', sender_id,
                '--force'
            ]

            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)


@pytest.mark.skip("Failing due to matcher update")
def test_suppression_crud(runner, config_file):
    config_profile = 'ADMIN'
    suppression_id = None
    try:
        params = [
            'email', 'suppression', 'create',
            '--email-address', util.random_name('cli_suppression_email', insert_underscore=False) + '@oracle.com',
            '--compartment-id', util.TENANT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        suppression_id = json.loads(result.output)['data']['id']

        params = [
            'email', 'suppression', 'get',
            '--suppression-id', suppression_id
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        params = [
            'email', 'suppression', 'list',
            '-c', util.TENANT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0
    finally:
        if suppression_id:
            params = [
                'email', 'suppression', 'delete',
                '--suppression-id', suppression_id,
                '--force'
            ]

            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)


def test_smtp_credential(runner, config_file, config_profile):
    smtp_credential_id = None
    try:
        params = [
            'iam', 'smtp-credential', 'create',
            '--user-id', util.ADMIN_USER_ID,
            '--description', 'Test SMTP credentials for CLI user',
            '--profile', 'ADMIN'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        smtp_credential_id = json.loads(result.output)['data']['id']

        params = [
            'iam', 'smtp-credential', 'update',
            '--smtp-credential-id', smtp_credential_id,
            '--user-id', util.ADMIN_USER_ID,
            '--description', 'Updated Test SMTP credentials for CLI user',
            '--profile', 'ADMIN'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert 'Updated' in json.loads(result.output)['data']['description']

        params = [
            'iam', 'smtp-credential', 'list',
            '--user-id', util.ADMIN_USER_ID,
            '--profile', 'ADMIN'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0
    finally:
        if smtp_credential_id:
            params = [
                'iam', 'smtp-credential', 'delete',
                '--smtp-credential-id', smtp_credential_id,
                '--user-id', util.ADMIN_USER_ID,
                '--force',
                '--profile', 'ADMIN'
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
