# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from . import util
import oci_cli
from conftest import runner
import pytest


@pytest.fixture(scope='function')
def commands_list(service):
    commands_list = util.filter_commands_list(service)
    return commands_list


runner = runner()


def invoke_example_operation(command_list):
    return runner.invoke(oci_cli.cli, command_list)


def validate_response(result):
    assert result.exit_code == 0

    # Ensure that compartment-id shortcut is set.
    if "--compartment-id TEXT" in result.output:
        assert ("-c, --compartment-id" in result.output)


def test_help_on_all_commands(commands_list):
    # Get a list of commands, where each command is a list of strings corresponding to the
    # command structure. Example: ['bucket', 'list']
    commands = commands_list
    for command in commands:
        if len(command) < 1:
            continue

        # Test the command with -?, -h, and --help.
        help_command = command + ['-?']
        result = invoke_example_operation(help_command + ['--cli-rc-file', 'tests/resources/default_files/use_click_help'])
        if result.exit_code != 0:
            print(command)
            print(result.output)
        validate_response(result)

        help_command = command + ['-h']
        result = invoke_example_operation(help_command + ['--cli-rc-file', 'tests/resources/default_files/use_click_help'])
        validate_response(result)

        help_command = command + ['--help']
        result = invoke_example_operation(help_command + ['--cli-rc-file', 'tests/resources/default_files/use_click_help'])
        validate_response(result)
