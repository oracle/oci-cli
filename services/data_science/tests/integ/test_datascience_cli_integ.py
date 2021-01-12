# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci_cli
import pytest
from tests import util
from tests import test_config_container

CASSETTE_LIBRARY_DIR = 'services/data_science/tests/cassettes'


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('data_science_{name}.yml'.format(name=request.function.__name__)):
        yield


def test_head_model_artifact(runner, config_file, config_profile):
    model_id = "ocid1.datasciencemodel.oc1.iad.amaaaaaav66vvniayzhtlhlj4pws4hqogmbphhag5mp2umdguzucfoc5ouhq"
    params = [
        'data-science', 'model', 'head-model-artifact',
        '--model-id', model_id
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert 'content-disposition' in result.output
    assert 'content-length' in result.output
    assert 'content-md5' in result.output
    assert 'content-type' in result.output
    assert 'date' in result.output
    assert 'etag' in result.output
    assert 'last-modified' in result.output
    assert 'x-content-type-options' in result.output
    assert 'opc-request-id' in result.output


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None,
           strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile] + params, ** args)

    return result
