# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import oci_cli
import os
import pytest

from tests import util
from tests import test_config_container

CASSETTE_LIBRARY_DIR = 'services/ons/tests/cassettes'
COMPARTMENT_ID_CHANGE_TO = os.getenv('OCI_CLI_CHANGE_TO_COMPARTMENT_ID')
util.set_admin_pass_phrase()


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('notification_{name}.yml'.format(name=request.function.__name__)):
        yield


def test_topic_crud(runner, config_file, config_profile):
    topic_id = None
    try:
        # Create Topic
        params = [
            'ons', 'topic', 'create',
            '--name', util.random_name('topic_name'),
            '-c', util.COMPARTMENT_ID,
            '--description', 'A description of the topic'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        topic_id = json.loads(result.output)['data']['topic-id']
        util.wait_until(['ons', 'topic', 'get', '--topic-id', topic_id], 'ACTIVE', max_wait_seconds=600)

        # Update topic
        params = [
            'ons', 'topic', 'update',
            '--topic-id', topic_id,
            '--description', 'new description'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert json.loads(result.output)['data']['description'] == 'new description'

        # List all topics
        params = [
            'ons', 'topic', 'list',
            '--compartment-id', util.COMPARTMENT_ID
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0

        # Change compartment
        if COMPARTMENT_ID_CHANGE_TO:
            params = [
                'ons', 'topic', 'change-compartment',
                '--topic-id', topic_id,
                '--compartment-id', COMPARTMENT_ID_CHANGE_TO
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)
            assert result.output != ''
    finally:
        if topic_id:
            params = [
                'ons', 'topic', 'delete',
                '--topic-id', topic_id,
                '--force'
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)


# TODO: Test is failing in py2.7:
#    Comment to record new tests.
#    Later on fix running in 2.7
@pytest.mark.skip('Test failing only in non-Python3 environment')
def test_subscription_crud(runner, config_file, config_profile):
    topic_id = None
    try:
        # Create Topic
        params = [
            'ons', 'topic', 'create',
            '--name', util.random_name('topic_name'),
            '-c', util.COMPARTMENT_ID,
            '--description', 'A description of the topic'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        topic_id = json.loads(result.output)['data']['topic-id']
        util.wait_until(['ons', 'topic', 'get', '--topic-id', topic_id], 'ACTIVE', max_wait_seconds=600)

        # Create HTTPS subscription
        params = [
            'ons', 'subscription', 'create',
            '--topic-id', topic_id,
            '-c', util.COMPARTMENT_ID,
            '--protocol', 'HTTPS',
            '--subscription-endpoint', 'https://example.com'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        subscription_id = json.loads(result.output)['data']['id']

        # Re-send subscription confirmation
        params = [
            'ons', 'subscription', 'resend-confirmation',
            '--id', subscription_id
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # Get the subscription
        params = [
            'ons', 'subscription', 'get',
            '--subscription-id', subscription_id,
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # List all subscriptions
        params = [
            'ons', 'subscription', 'list',
            '--compartment-id', util.COMPARTMENT_ID
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # Change compartment
        # Need to find a way to confirm the subscription before we can change the compartment.
        TEST_SUBSCRIPTION_CHANGE_COMPARTMENT = False
        if COMPARTMENT_ID_CHANGE_TO and TEST_SUBSCRIPTION_CHANGE_COMPARTMENT:
            params = [
                'ons', 'subscription', 'change-compartment',
                '--subscription-id', subscription_id,
                '--compartment-id', COMPARTMENT_ID_CHANGE_TO
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)
            assert result.output != ''
    finally:

        if topic_id:
            params = [
                'ons', 'topic', 'delete',
                '--topic-id', topic_id,
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
