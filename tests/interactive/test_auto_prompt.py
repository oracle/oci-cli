# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from click.testing import CliRunner
from interactive.oci_shell_completer import OciShellCompleter
from oci_cli.cli_root import cli
from . import utils
from prompt_toolkit.document import Document
from prompt_toolkit.completion import CompleteEvent
from oci_cli.service_mapping import service_mapping
from oci_cli import dynamic_loader


class TestAutoPrompt(unittest.TestCase):

    def test_cli_interactive_import(self):
        # This funciton tests importing interactive mode
        from interactive.cli_interactive import start_interactive_shell
        _ = start_interactive_shell

    def test_cli_interactive_call(self):
        # This funciton tests calling interactive mode
        try:
            runner = CliRunner()
            result = runner.invoke(cli, ['-i'])
        except Exception:
            self.fail('Failed to run cli with interactive parameters')

    def test_root_command_suggestion(self):
        # This function is to test the commands suggestions on the root level
        ctx = utils.set_up_context(cli)
        completer = OciShellCompleter(ctx, service_mapping, dynamic_loader)
        document = Document('', 0)
        completions = completer.get_completions(document, CompleteEvent())
        expected_list = utils.get_expected_commands_list(cli, cli)
        actual_list = [completion.text for completion in completions]

        # unittest.TestCase.assertCountEqual tests if the two lists have the same elements regarding of their order
        self.assertCountEqual(expected_list, actual_list)

    def test_sub_commands_and_parameters_suggestion(self):
        # This is to test all the subcommands and parameters
        ctx = utils.set_up_context(cli)
        self._recursively_test_subcommands_and_parameters(ctx, cli, cli)

    def _recursively_test_subcommands_and_parameters(self, ctx, root_command, current_command,
                                                     previous_document_text="", previous_curser_position=0):

        subcommands = getattr(current_command, "commands", {})
        for subcommand_name, subcommand_obj in subcommands.items():
            completer = OciShellCompleter(ctx, service_mapping, dynamic_loader)
            document = Document(previous_document_text + subcommand_name + ' ',
                                previous_curser_position + len(subcommand_name) + 1)
            completions = completer.get_completions(document, CompleteEvent())
            expected_list = utils.get_expected_commands_list(root_command, subcommand_obj)
            actual_list = [completion.text for completion in completions]
            self.assertCountEqual(expected_list, actual_list)
            self._recursively_test_subcommands_and_parameters(ctx, root_command, subcommand_obj, document.text,
                                                              document.cursor_position)

    def test_parameters_exclusion_suggestion(self):
        # For example if the user provides "oci compute instance list -c x "
        # the completion should return all the other parameters excluding the --compartment-id
        ctx = utils.set_up_context(cli)
        self._recursively_test_parameters_exclusion_suggestion(cli, ctx, cli)

    def _recursively_test_parameters_exclusion_suggestion(self, root_command, ctx, command, previous_document_text="",
                                                          previous_curser_position=0):

        subcommands = getattr(command, "commands", {})
        if not subcommands:  # The base case is here, no subcommands means we are at the parameters level
            expected_parameters_list = utils.get_expected_commands_list(root_command, command)
            expected_parameters_list = list(set(expected_parameters_list))
            # Now the expected_parameters_list has the parameters list for the command
            # let's test if taking out one parameter from this list and adding it to the document along with a fake
            # value, it should return the same parameters list excluding the parameter which was provided

            completer = OciShellCompleter(ctx, service_mapping, dynamic_loader)
            if expected_parameters_list:
                first_parameter = expected_parameters_list[0]
                multiple_dict = {x.name: x.multiple for x in command.params}
                first_parameter_snake = first_parameter.strip('-').replace('-', '_')
                if not multiple_dict.get(first_parameter_snake):
                    expected_parameters_list.remove(first_parameter)
                document = Document(previous_document_text + first_parameter + " x ",
                                    previous_curser_position + len(first_parameter) + 3)
                completions = completer.get_completions(document, CompleteEvent())
                actual_parameters_list = [completion.text for completion in completions]
                actual_parameters_list = list(set(actual_parameters_list))
                self.assertCountEqual(actual_parameters_list, expected_parameters_list)

        for subcommand_name, subcommand_obj in subcommands.items():
            document = Document(previous_document_text + subcommand_name + ' ',
                                previous_curser_position + len(subcommand_name) + 1)
            self._recursively_test_parameters_exclusion_suggestion(root_command, ctx, subcommand_obj, document.text,
                                                                   document.cursor_position)

    options = {
        '--config-file': '~/.oci/config',
        '--auth': 'api_key',
        '--region': 'us-phoenix-1',
        '--auth-purpose': 'dummy-text',
        '--cert-bundle': 'dummy-text',
        '--profile': 'DEFAULT'
    }

    def test_cli_authentication_in_interactive_mode(self):
        # Test if --config-file option works in interactive-cli-mode
        for option, value in self.options.items():
            with self.subTest(option=option, value=value):
                try:
                    runner1 = CliRunner()
                    runner2 = CliRunner()
                    # run the command in non-interactive mode
                    result_non_interactive = runner1.invoke(cli, [option, value])
                    # run the same cli command in interactive mode
                    runner2.invoke(cli, ['-i'])
                    result_interactive = runner2.invoke(cli, [option, value])
                    # assertions to compare the results of interactive mode and non-interactive mode
                    self.assertEqual(result_interactive.exit_code, result_non_interactive.exit_code)
                    # Exit code is non zero because of promt for creating config
                    # self.assertEqual(result_interactive.exit_code, 0)
                    # The output of the cmds is large so just comparing the first line here
                    self.assertEqual(result_interactive.output.splitlines()[0], result_non_interactive.output.splitlines()[0])
                except Exception:
                    self.fail(f'Failed to run interactive CLI with {option} option')
