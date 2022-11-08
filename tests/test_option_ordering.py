# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import os.path
import unittest
from . import util


class TestOptionOrdering(unittest.TestCase):

    def setUp(self):
        util.set_admin_pass_phrase()

    def test_no_options(self):
        result = self.invoke_operation(['os', 'ns', 'get'])
        self.assertEqual(0, result.exit_code)
        assert not self.has_debug_data(result)

    def test_fail_unknown_options(self):
        result = self.invoke_operation(['iam', 'user', 'list', '--compartment-id', util.TENANT_ID, '--limit', '1', '--not-an-option'])
        self.assertNotEqual(0, result.exit_code)

        result = self.invoke_operation(['--not-an-option'])
        self.assertNotEqual(0, result.exit_code)

        result = self.invoke_operation(['iam', 'user', '-q'])
        self.assertNotEqual(0, result.exit_code)

    def test_debug_at_root(self):
        result = self.invoke_operation(['-d', 'os', 'ns', 'get'])
        self.assertEqual(0, result.exit_code)
        assert self.has_debug_data(result)

    def test_debug_at_service(self):
        result = self.invoke_operation(['os', '-d', 'ns', 'get'])
        self.assertEqual(0, result.exit_code)
        assert self.has_debug_data(result)

    def test_debug_at_noun(self):
        result = self.invoke_operation(['os', 'ns', '-d', 'get'])
        self.assertEqual(0, result.exit_code)
        assert self.has_debug_data(result)

    def test_debug_at_verb(self):
        result = self.invoke_operation(['os', 'ns', 'get', '-d'])
        self.assertEqual(0, result.exit_code)
        assert self.has_debug_data(result)

    def test_debug_with_command_option(self):
        result = self.invoke_operation(['iam', 'user', 'list', '--compartment-id', util.TENANT_ID, '--limit', '1', '-d'])
        self.assertEqual(None, result.exit_code)
        assert self.has_debug_data(result)

    def test_help_at_root(self):
        self.verify_help([], [None, '-?', '--help'], 'Usage: oci [OPTIONS]')

    def test_help_at_service(self):
        self.verify_help(['os'], [None, '-?', '--help'], 'Usage: oci os [OPTIONS]')

    def test_help_at_noun(self):
        self.verify_help(['os', 'ns'], [None, '-?', '--help'], 'Usage: oci os ns [OPTIONS]')

    def test_help_at_verb(self):
        self.verify_help(['os', 'ns', 'get'], ['-?', '--help'], 'Usage: oci os ns get [OPTIONS]')

    def test_empty_path_option_returns_error(self):
        result = self.invoke_operation(['iam', 'user', 'get', '--user-id', ''])
        self.assertNotEqual(0, result.exit_code)
        assert "UsageError: Parameter --user-id cannot be whitespace or empty string" in result.output

    def test_delete_confirmation_missing_required_params_does_not_prompt(self):
        # missing required parameter --instance-id
        result = self.invoke_operation(['compute', 'instance', 'terminate'])
        assert result.exit_code != 0
        assert 'Error: Missing option(s) --instance-id' in result.output

    def invoke_operation(self, command):
        return util.invoke_command_as_admin(command)

    def has_debug_data(self, result):
        return 'send:' in result.output and 'Oracle-PythonSDK' in result.output

    def verify_help(self, command, help_commands, expected_output):
        """Runs the command with each of the possible help commands given, and verifies that in each case the output
        contains the expected string."""
        for help_command in help_commands:
            full_command = command
            if help_command:
                full_command = command + [help_command] + ['--cli-rc-file', os.path.join('tests', 'resources', 'default_files', 'use_click_help')]

            result = self.invoke_operation(full_command)
            self.assertEqual(0, result.exit_code)
            assert expected_output in result.output


if __name__ == '__main__':
    unittest.main()
