# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import oci_cli

from tests import util


CASSETTE_LIBRARY_DIR = 'services/data_safe/tests/cassettes'
WORKFLOW_REQUEST_EXPECTED_DATA = {"opc-work-request-id": ""}


def run_test(runner, config_file, config_profile, params, expected_data=None, check_values=True, check_length=False, debug=False, root_params=None, decode_response=True, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug:
        response = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile] + params, ** args)
    else:
        response = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile] + params, ** args)

    if hasattr(response, "output"):
        print("******** BEGIN RESPONSE **********")
        print(response.output)
        print("******** END RESPONSE ************")

    if decode_response:
        _validate_result(response, expected_data, check_values, check_length)

        return json.loads(response.output)
    else:
        return response.output


def _validate_result(result, expected_data, check_values, check_length):
    assert result is not None

    util.validate_response(result)

    output = json.loads(result.output)
    if "data" in output:
        response_data = output["data"]
    else:
        response_data = output

    if check_length:
        assert len(response_data) > 0

    if expected_data:
        assert isinstance(expected_data, dict) is True

        for k, v in expected_data.items():
            if check_values:
                assert response_data[k] == expected_data[k]
            else:
                _assert_key_value_exists(response_data, k)


def _assert_key_value_exists(data, k):
    assert k in data
    assert data[k] is not None
