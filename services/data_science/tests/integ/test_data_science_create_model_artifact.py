# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci_cli
import pytest
from tests import test_config_container
import json

CASSETTE_LIBRARY_DIR = 'services/data_science/tests/cassettes'
COMPARTMENT_ID = "ocid1.compartment.oc1..aaaaaaaabf7prp3qxkumkkv265phy56oi4d6q4fblrxhswygvuz3t5qs5uca"
large_file_path = "services/data_science/tests/integ/data_science_large_file.txt"


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('data_science_{name}.yml'.format(name=request.function.__name__)):
        yield


def test_data_science_model_create_model_artifact(runner, config_file, config_profile):
    params = [
        'data-science',
        'project',
        'create',
        '--compartment-id', COMPARTMENT_ID,
    ]
    result = invoke(runner, config_file, config_profile, params)
    assert result.exit_code == 0
    PROJECT_ID = json.loads(result.output)['data']['id']
    print(PROJECT_ID)
    params = [
        'data-science',
        'model',
        'create',
        '--compartment-id', COMPARTMENT_ID,
        '--project-id', PROJECT_ID,
    ]
    result = invoke(runner, config_file, config_profile, params)
    MODEL_ID = json.loads(result.output)['data']['id']
    print(MODEL_ID)
    assert result.exit_code == 0
    model_artifact_path = large_file_path
    params = [
        'data-science',
        'model',
        'create-model-artifact',
        '--model-artifact-file', model_artifact_path,
        '--model-id', MODEL_ID,
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
