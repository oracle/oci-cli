# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import oci_cli
import pytest
from tests import util
from tests import test_config_container

CASSETTE_LIBRARY_DIR = 'services/resource_search/tests/cassettes'


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('resourcesearch_{name}.yml'.format(name=request.function.__name__)):
        yield


def test_list_resource_type(runner, config_file, config_profile):
    params = [
        'search', 'resource-type', 'list'
    ]

    result = invoke(runner, config_file, config_profile, params)

    assert len(json.loads(result.output)['data']) > 1


def test_get_resource_type(runner, config_file, config_profile):
    params = [
        'search', 'resource-type', 'get',
        '--name', 'Group'
    ]

    result = invoke(runner, config_file, config_profile, params)

    assert len(json.loads(result.output)['data']) > 1
    assert json.loads(result.output)["data"]["name"] == "Group"


def test_freetext_search(runner, config_file, config_profile, identity_client):
    user_name = identity_client.get_user(util.USER_ID).data.name
    params = [
        'search', 'resource', 'free-text-search',
        '--text', user_name
    ]

    result = invoke(runner, config_file, config_profile, params)

    assert len(json.loads(result.output)['data']) >= 0


def test_structured_query_search(runner, config_file, config_profile):
    params = [
        'search', 'resource', 'structured-search',
        '--query-text', 'query all resources'
    ]

    result = invoke(runner, config_file, config_profile, params)
    assert len(json.loads(result.output)['data']) >= 0


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile] + params, ** args)

    return result
