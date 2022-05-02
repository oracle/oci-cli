# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from . import util
import click
import json
import oci_cli
import six
import random
import vcr
import os
import pytest
from common_util import ignored_commands

# Commands which we skip evaluation of because they don't have the JSON input


IGNORE_COMMANDS_LOCATION = 'tests/resources/json_ignore_command_list.txt'

ALLOW_JSON_TEST_FAILURES_ENV_VAR = 'ALLOW_JSON_TEST_FAILURES'


@pytest.fixture(autouse=True, scope='function')
def ignored_extended_commands():
    ignored_commands = []
    with open(IGNORE_COMMANDS_LOCATION, 'r') as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            if len(line) != 0:
                ignored_commands.append(line.split(', '))

    return ignored_commands


# Commands which have no parameters and so produce empty dictionaries
# Current output:
# ['iam', 'region', 'list'],
# ['network', 'peer-region-for-remote-peering', 'list-allowed-peer-regions-for-remote-peering'],
# ['os', 'ns', 'get']
# From returned list of (command, number of params, number of required params),
# filter command names with number of params <= 2 (--help and --from-json) into a sorted list.
COMMANDS_WITH_NO_PARAMS = sorted(command for command, _, _ in
                                 filter(lambda x: x[1] <= 2 and x[0] not in ignored_commands.IGNORED_COMMANDS,
                                        util.collect_leaf_commands_with_counts(oci_cli.cli)))


@pytest.fixture(autouse=True, scope='function')
def commands_list(service):
    commands_list = util.filter_commands_list(service)
    return commands_list


def test_all_commands_generate_skeleton(commands_list):
    failed_to_parse_commands = []
    commands_with_bad_json = []  # We don't expect any commands that emit an empty dict
    for cmd in commands_list:

        full_command = list(cmd)
        full_command.append('--generate-full-command-json-input')
        result = util.invoke_command(full_command)
        assert result.exit_code == 0
        try:
            parsed_output = json.loads(result.output)
            if parsed_output == {} and cmd not in COMMANDS_WITH_NO_PARAMS:
                commands_with_bad_json.append(cmd)
        except Exception:
            failed_to_parse_commands.append(cmd)

    assert len(failed_to_parse_commands) == 0, 'The following commands failed to parse: {}'.format(failed_to_parse_commands)
    assert len(commands_with_bad_json) == 0, 'The following commands had invalid JSON skeletons: {}'.format(commands_with_bad_json)


none_mode_vcr = vcr.VCR(record_mode='none')


# Test which invokes all the command using the request formed by invoking --generate-full-command-json-input option.
# The main aim of this test is to verify if all the generated CLI code is function and CLI <-> PythonSDK interaction.
# In this test, we use VCR with record mode none as to stop any out-going http request.
@none_mode_vcr.use_cassette('invalid-file-path')
def test_run_all_commands(runner, config_file, config_profile, tmpdir, ignored_extended_commands, commands_list):
    failed_commands = []
    for cmd in commands_list:
        if cmd not in ignored_extended_commands:
            full_command = list(cmd)
            try:
                result = util.invoke_command(full_command + ['--generate-full-command-json-input'])
                try:
                    assert result.exit_code == 0
                except AssertionError as ae:
                    print("--generate-full-command-json-input failure for: {}".format(full_command))
                    print(ae)
                    print(result.output)
                    failed_commands.append(cmd)
                    continue
                json_input = process_json_input(result.output, tmpdir)
                json_input = json.dumps(json_input)
                full_command.extend(['--from-json', json_input])

                result = invoke(runner, config_file, 'ADMIN', full_command)

                if 'Error: Missing option --endpoint.' in result.output:
                    # some services require --endpoint to be passed.
                    full_command.extend(['--endpoint', 'https://region.domain.com'])
                    result = invoke(runner, config_file, 'ADMIN', full_command)

                if result.exit_code != 0 and 'CannotOverwriteExistingCassetteException' not in result.output:
                    failed_commands.append(cmd)
                    print(cmd)
                    print(result.output)

            except Exception:
                failed_commands.append(cmd)
                print(cmd)

    handle_failed_commands(failed_commands)


def handle_failed_commands(failed_commands):
    try:
        assert len(failed_commands) == 0, 'The following commands failed to run: {}'.format(failed_commands)
    except AssertionError as ae:
        if ALLOW_JSON_TEST_FAILURES_ENV_VAR in os.environ:
            print("Writing failed commands to json_ignore_commands_list.txt file")
            append_failed_commands_to_file(failed_commands)
        else:
            raise ae


def append_failed_commands_to_file(failed_commands):
    with open(IGNORE_COMMANDS_LOCATION, 'a') as f:
        for cmd in failed_commands:
            f.write(', '.join(cmd))
            f.write('\n')


def process_json_input(input, tmpdir):
    modified_input = json.loads(input)
    # if the command accepts list of objects, we will process the first element in the list and pass it to the test.
    if type(input) == list:
        modified_input = modified_input[0]
    # Remove waiter and listing options
    modified_input.pop('waitForState', None)
    modified_input.pop('limit', None)
    modified_input.pop('all', None)
    for key in modified_input:
        # if input is a Multiple choice option, this will extract a single choice from the choice list.
        if isinstance(modified_input[key], list) and len(modified_input[key]) == 1 and isinstance(modified_input[key][0], six.string_types):
            first_val = str(modified_input[key][0])
            if "|" in first_val:
                modified_input[key][0] = get_choice_from_choices(first_val)
        # input is a choice option, get the first choice.
        if "|" in str(modified_input[key]):
            modified_input[key] = get_choice_from_choices(str(modified_input[key]))

        if modified_input[key] == '/path/to/file':
            # create a temp file.
            fh = tmpdir.join("input.txt")
            fh.write("sample text")
            filepath = os.path.join(fh.dirname, fh.basename)
            modified_input[key] = filepath

    if type(json.loads(input)) is list:
        return [modified_input]

    return modified_input


def get_choice_from_choices(choices):
    choice = random.choice(choices.split('|'))
    return choice


def _traverse_oci_cli(command, path, failed_commands, ignored_extended_commands):
    if hasattr(command, "commands"):
        for name, command in six.iteritems(command.commands):
            _traverse_oci_cli(command, path + [name], failed_commands, ignored_extended_commands)
    else:
        if path not in ignored_commands.IGNORED_COMMANDS and path not in ignored_extended_commands:
            complex_options = [option for option in command.params if str(option.type) == 'COMPLEX_TYPE']
            if complex_options:
                for option in complex_options:
                    full_command = path + ['--generate-param-json-input', option.name.replace('_', '-')]
                    result = util.invoke_command(full_command)
                    if result.exit_code != 0 or 'is not a recognized complex type, so no example JSON can be produced. Invoke help for this command' in result.output:
                        print(full_command, result.exit_code)
                        failed_commands.append(path)


def test_generate_param_json_input_for_all_complex_types(ignored_extended_commands):
    failed_commands = []
    _traverse_oci_cli(oci_cli.cli, [], failed_commands, ignored_extended_commands)

    handle_failed_commands(failed_commands)


def teardown_module(module):
    # This teardown is required when running multiple tests together because oci_cli.cli is only loaded once and some option definitions will get
    # modified when doing the --generate-full-command-json-input thing. This is OK when a customer invokes the CLI because it's new commands each
    # time, but in tests things are shared.
    #
    # The reset method here should put things back as they are so that other tests that come after this one aren't interfered with
    reset_prompt_in_group(oci_cli.cli.commands)


def reset_prompt_in_group(click_group):
    for cmd_name, cmd in six.iteritems(click_group):
        if isinstance(cmd, click.Group):
            reset_prompt_in_group(cmd.commands)
        else:
            for p in cmd.params:
                if p.expose_value is False and '--force' in p.opts:
                    p.prompt = "Are you sure you want to delete this resource?"
                    p.callback = oci_cli.cli_util.confirmation_callback


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = ['--config-file', config_file]

    if config_profile:
        root_params.extend(['--profile', config_profile])

    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug'] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + params, ** args)

    return result
