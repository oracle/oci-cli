# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import oci_cli
import pytest
from tests import util
from tests import test_config_container

CASSETTE_LIBRARY_DIR = 'services/announcements_service/tests/cassettes'
TENANCY_ID = "ocid1.tenancy.oc1..aaaaaaaa3vi3ft3yi3sq4nhiql4nvbzjz6gipbn72h7werl6njs6xsq4wgdq"


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('{name}.yml'.format(name=request.function.__name__)):
        yield


def test_announcements_announce_list(runner, config_file, config_profile):
    params = [
        'announce', 'announcements', 'list',
        '-c', TENANCY_ID
    ]
    result = invoke(runner, config_file, config_profile, params + ['--limit', '20'])
    parsed_result = json.loads(result.output)
    util.validate_response(result)

    assert len(json.loads(result.output)['data']['items']) == 20
    assert "opc-next-page" in parsed_result

    result = invoke(runner, config_file, config_profile, params + ['--limit', '80'])
    parsed_result = json.loads(result.output)
    util.validate_response(result)

    assert (len(parsed_result['data']['items']) + len(parsed_result['data']['user-statuses'])) == 80

    result = invoke(runner, config_file, config_profile, params + ['--all'])
    parsed_result_all = json.loads(result.output)
    util.validate_response(result)

    result = invoke(runner, config_file, config_profile, params)
    parsed_result = json.loads(result.output)
    util.validate_response(result)

    assert parsed_result['data'] == parsed_result_all['data']


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None,
           strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile] + params, ** args)

    return result
