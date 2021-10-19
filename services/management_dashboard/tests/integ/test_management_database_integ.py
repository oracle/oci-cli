# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci_cli
import pytest
from tests import test_config_container
import json
import os
# Steps to recreate test case
# Replace Compartment-id (use quotes) in file://services/management_dashboard/tests/integ/import.json and  run "oci management-dashboard dashboard import --from-json
# file://services/management_dashboard/tests/integ/import.json"
# After import, use command "oci management-dashboard dashboard list -c <CompartmentID>" to make sure the dashboard is created and get the "dashboard-id".
# Now you can run: oci management-dashboard dashboard export  --export-dashboard-id "{\"dashboardIds\":[\"<Dashboard Id\"]}"


CASSETTE_LIBRARY_DIR = 'services/management_dashboard/tests/cassettes/for_generated'


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    custom_vcr = test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR)

    cassette_location = 'management_dashboard_{name}.yml'.format(name=request.function.__name__)
    with custom_vcr.use_cassette(cassette_location):
        yield


@pytest.mark.skip()
def test_export_import_management_dashboard(runner, config_file, config_profile):
    params = [
        'management-dashboard', 'dashboard', 'export',
        '--export-dashboard-id', os.environ['OCI_CLI_MANAGEMENT_DASHBOARD_ID'],
    ]
    result = invoke(runner, config_file, config_profile, params)
    assert result.exit_code == 0
    import_json = json.loads(result.output)['data']
    params = [
        'management-dashboard', 'dashboard', 'import',
        '--from-json', json.dumps(import_json),
    ]
    result = invoke(runner, config_file, config_profile, params)
    assert result.exit_code == 0


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None,
           strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile] + params, ** args)

    return result
