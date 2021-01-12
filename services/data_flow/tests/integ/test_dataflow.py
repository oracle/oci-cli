# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util
configErrorMessage = "Incorrect 'configuration' value, cannot proceed. Configuration should be either in a plain text format of 'param_name_1=value_1 param_name_2=value_2 ...' or a json format of '{ \"param_name_1\": \"value_1\", \"param_name_2\": \"value_2\", }, ...'"
paramsErrorMessage = "Incorrect 'parameters' value, cannot proceed. Parameters should be either in a plain text format of 'param_name_1=value_1 param_name_2=value_2 ...' or a json format of '[ { \"name\": \"param_name_1\", \"value\": \"value_1\"}, { \"name\": \"param_name_2\", \"value\": \"value_2\"}, ...]'"


class TestDataFlow(unittest.TestCase):

    @util.log_test
    def test_application_create_validations(self):
        """
        # check call with plain text arguments, parameters, configuration
        result = self.invoke(['application', 'create', '--compartment-id', util.COMPARTMENT_ID, '--display-name', 'unit-test',
                              '--driver-shape', 'unit-test', '--executor-shape', 'unit-test', '--file-uri', 'unit-test',
                              '--language', 'JAVA', '--num-executors', '1', '--spark-version', 'unit-test',
                              '--arguments', '--input ${input} --output ${output} 10',
                              '--parameters', 'input="~/myInput.txt" output="~/myOutput.txt",
                              '--configuration', 'spark.app.name="My App Name" spark.shuffle.io.maxRetries=4'
                              ])
        util.validate_response(result)

        # check call with json arguments, parameters, configuration
        result = self.invoke(['application', 'create', '--compartment-id', util.COMPARTMENT_ID, '--display-name', 'unit-test',
                              '--driver-shape', 'unit-test', '--executor-shape', 'unit-test', '--file-uri', 'unit-test',
                              '--language', 'JAVA', '--num-executors', '1', '--spark-version', 'unit-test',
                              '--arguments', '["--input", "${input}", "--output", "${output}", "10"]',
                              '--parameters', '[ {"name": "input", "value": "~/myInput.txt" }, { "name": "output", "value": "~/myOutput.txt" } ]',
                              '--configuration', '{ "spark.app.name": "My App Name", "spark.shuffle.io.maxRetries": "4" }'
                              ])
        util.validate_response(result)
        """
        # check parameters errors 1
        result = self.invoke(['application', 'create', '--compartment-id', util.COMPARTMENT_ID, '--display-name', 'unit-test',
                              '--driver-shape', 'unit-test', '--executor-shape', 'unit-test', '--file-uri', 'unit-test',
                              '--language', 'JAVA', '--num-executors', '1', '--spark-version', 'unit-test',
                              '--parameters', 'input="~/myInput.txt" output "~/myOutput.txt"'])
        assert paramsErrorMessage in result.output

        # check parameters errors 2: Missing = sign after word '...'
        result = self.invoke(['application', 'create', '--compartment-id', util.COMPARTMENT_ID, '--display-name', 'unit-test',
                              '--driver-shape', 'unit-test', '--executor-shape', 'unit-test', '--file-uri', 'unit-test',
                              '--language', 'JAVA', '--num-executors', '1', '--spark-version', 'unit-test',
                              '--parameters', 'input "~/myInput.txt" output'])
        assert paramsErrorMessage in result.output

        # check configuration errors 1: Incorrect 'configuration' value...
        result = self.invoke(['application', 'create', '--compartment-id', util.COMPARTMENT_ID, '--display-name', 'unit-test',
                              '--driver-shape', 'unit-test', '--executor-shape', 'unit-test', '--file-uri', 'unit-test',
                              '--language', 'JAVA', '--num-executors', '1', '--spark-version', 'unit-test',
                              '--configuration', 'spark.app.name="My App Name" spark.shuffle.io.maxRetries 4'])
        assert configErrorMessage in result.output

        # check configuration errors 2: Missing = sign after word '...'
        result = self.invoke(['application', 'create', '--compartment-id', util.COMPARTMENT_ID, '--display-name', 'unit-test',
                              '--driver-shape', 'unit-test', '--executor-shape', 'unit-test', '--file-uri', 'unit-test',
                              '--language', 'JAVA', '--num-executors', '1', '--spark-version', 'unit-test',
                              '--configuration', 'spark.app.name "My App Name" spark.shuffle.io.maxRetries'])
        assert configErrorMessage in result.output

    @util.log_test
    def test_application_update_validations(self):
        # check parameters errors 1
        result = self.invoke(['application', 'update', '--application-id', 'unit-test',
                              '--parameters', 'input="~/myInput.txt" output "~/myOutput.txt"'])
        assert paramsErrorMessage in result.output

        # check parameters errors 2: Missing = sign after word '...'
        result = self.invoke(['application', 'update', '--application-id', 'unit-test',
                              '--parameters', 'input "~/myInput.txt" output'])
        assert paramsErrorMessage in result.output

        # check configuration errors 1: Incorrect 'configuration' value...
        result = self.invoke(['application', 'update', '--application-id', 'unit-test',
                              '--configuration', 'spark.app.name="My App Name" spark.shuffle.io.maxRetries 4'])
        assert configErrorMessage in result.output

        # check configuration errors 2: Missing = sign after word '...'
        result = self.invoke(['application', 'update', '--application-id', 'unit-test',
                              '--configuration', 'spark.app.name "My App Name" spark.shuffle.io.maxRetries'])
        assert configErrorMessage in result.output

    def invoke(self, params, debug=False, **args):
        commands = ['data-flow'] + params

        if debug is True:
            commands = ['--debug'] + commands

        return util.invoke_command(commands, **args)
