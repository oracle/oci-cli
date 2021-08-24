# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util
from services.data_flow.src.oci_cli_data_flow.dataflow_cli_extended import convertArgumentStringToJson, convertParameterStringToJson, convertConfigurationStringToJson


class TestRunLogChanges(unittest.TestCase):
    def setUp(self):
        pass

    # Test 1 :
    # Rename "oci data-flow run get-run-log --file, --name, --run-id"
    # to     "oci data-flow run get-log     --file, --name, --run-id"

    # Test 1.1: get-run-log is removed
    def test_get_run_log_removed(self):
        result = util.invoke_command(['data-flow', 'run', 'get-run-log'])
        assert "Error: No such command 'get-run-log'." in result.output

    # Test 1.2: get-log is added
    def test_get_log_added(self):
        result = util.invoke_command(['data-flow', 'run', 'get-log', '--file', 'my_filename.gz', '--name', 'log-filename-on-server.gz'])
        assert 'Error: Missing option(s) --run-id.' in result.output

    # Test 2:
    # Rename "oci data-flow run-log-summary list-run-logs --run-id, --all-pages"
    # to     "oci data-flow run             list-logs     --run-id"

    # Test 2.1: run-log-summary is removed
    def test_run_log_summary_removed(self):
        result = util.invoke_command(['data-flow', 'run-log-summary'])
        assert "Error: No such command 'run-log-summary'." in result.output

    # Test 2.1: list-logs is added
    def test_list_logs_added(self):
        result = util.invoke_command(['data-flow', 'run', 'list-logs'])
        assert 'Error: Missing option(s) --run-id.' in result.output

    # Test 3: Check the conversion of 'arguments', 'parameters' and 'configuration' strings to json
    # Test 3.1: Test if argument string is correctly converted into a json array
    def test_convertArgumentsToJson(self):
        json = convertArgumentStringToJson("--input ${input} --output ${output} 10 'This is one arg'")
        assert json == '["--input", "${input}", "--output", "${output}", "10", "This is one arg"]'

    # Test 3.1: Test if parameters string is correctly converted into a json array
    def test_convertParametersToJson(self):
        json = convertParameterStringToJson("input='~/myInput.txt' output='~/myOutput.txt'")
        assert json == '[{"name": "input", "value": "~/myInput.txt"}, {"name": "output", "value": "~/myOutput.txt"}]'

    # Test 3.1: Test if parameters string is correctly converted into a json array
    def test_convertConfigurationStringToJson(self):
        json = convertConfigurationStringToJson("spark.app.name=\"My App Name\" spark.shuffle.io.maxRetries=4")
        assert json == '{"spark.app.name": "My App Name", "spark.shuffle.io.maxRetries": "4"}'
