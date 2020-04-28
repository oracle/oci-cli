# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from . import util
import oci_cli
from conftest import runner


class TestHelp(unittest.TestCase):

    def setUp(self):
        self.runner = runner()

    def test_help_on_all_commands(self):
        # Get a list of commands, where each command is a list of strings corresponding to the
        # command structure. Example: ['bucket', 'list']
        commands = sorted(util.collect_commands(oci_cli.cli))
        for command in commands:
            if len(command) < 1:
                continue

            # Test the command with -?, -h, and --help.
            help_command = command + ['-?']
            result = self.invoke_example_operation(help_command + ['--cli-rc-file', 'tests/resources/default_files/use_click_help'])
            if result.exit_code != 0:
                print(command)
                print(result.output)
            self.validate_response(result)

            help_command = command + ['-h']
            result = self.invoke_example_operation(help_command + ['--cli-rc-file', 'tests/resources/default_files/use_click_help'])
            self.validate_response(result)

            help_command = command + ['--help']
            result = self.invoke_example_operation(help_command + ['--cli-rc-file', 'tests/resources/default_files/use_click_help'])
            self.validate_response(result)

    def invoke_example_operation(self, command_list):
        return self.runner.invoke(oci_cli.cli, command_list)

    def validate_response(self, result):
        self.assertEqual(0, result.exit_code)

        # Ensure that compartment-id shortcut is set.
        if "--compartment-id TEXT" in result.output:
            assert ("-c, --compartment-id" in result.output)


if __name__ == '__main__':
    unittest.main()
