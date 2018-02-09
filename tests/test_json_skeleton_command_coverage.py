# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from . import util

import click
import json
import oci_cli
import six


# Commands which we skip evaluation of because they don't have the JSON input
IGNORED_COMMANDS = [
    ['setup', 'autocomplete'],
    ['setup', 'config'],
    ['setup', 'keys'],
    ['setup', 'repair-file-permissions'],
    ['setup', 'oci-cli-rc']
]


# Commands which have no parameters and so produce empty dictionaries
COMMANDS_WITH_NO_PARAMS = [
    ['os', 'ns', 'get'],
    ['iam', 'region', 'list']
]


# Commands whose parameters are all marked as optional (though some combination of them may be needed for calls to succeed)
COMMANDS_WITH_ALL_OPTIONAL_PARAMS = [
    ['db', 'backup', 'list'],
    ['network', 'private-ip', 'list'],
    ['bv', 'volume', 'create'],
    ['bv', 'volume-backup-policy', 'list']
]


def test_all_commands_generate_skeleton():
    commands = sorted(util.collect_commands(oci_cli.cli, leaf_commands_only=True))

    failed_to_parse_commands = []
    commands_with_bad_json = []  # We don't expect any commands that emit an empty dict
    for cmd in commands:
        if cmd in IGNORED_COMMANDS:
            continue

        full_command = list(cmd)
        full_command.append('--generate-full-command-json-input')
        result = util.invoke_command(full_command)
        assert result.exit_code == 0
        try:
            # Sanity check that there are no errors
            assert 'error' not in result.output.lower()

            parsed_output = json.loads(result.output)
            if parsed_output == {} and cmd not in COMMANDS_WITH_NO_PARAMS:
                commands_with_bad_json.append(cmd)
        except Exception:
            failed_to_parse_commands.append(cmd)

    assert len(failed_to_parse_commands) == 0, 'The following commands failed to parse: {}'.format(failed_to_parse_commands)
    assert len(commands_with_bad_json) == 0, 'The following commands had invalid JSON skeletons: {}'.format(commands_with_bad_json)


def test_all_commands_can_accept_from_json_input():
    commands = sorted(util.collect_commands(oci_cli.cli, leaf_commands_only=True))

    for cmd in commands:
        if cmd in IGNORED_COMMANDS:
            continue

        full_command = list(cmd)
        full_command.extend(['--from-json', 'file://tests/resources/json_input/dummy.json'])
        result = util.invoke_command(full_command)

        # If the command takes no params, then invoking it should actually work (and so we should get nothing back or valid JSON back).
        #
        # If the command has only optional parameters, then invoking it should actually work (but we may get an error back from the service
        # as the operation may rely on some combination of parameters being provided).
        #
        # Otherwise make the assumption that at least one of them is required so we should get "Missing option" in
        # there somewhere, but nothing mentioning that our from-json option is not needed.  If the operation requires confirmation
        # then the output may contain 'Are you sure' but this means we have already gotten past the point where the '--from-json' is not
        # needed error would have been thrown.
        if cmd in COMMANDS_WITH_NO_PARAMS:
            if result.output:
                # Sanity check that there are no errors
                assert 'error' not in result.output.lower()

                json.loads(result.output)
        elif cmd in COMMANDS_WITH_ALL_OPTIONAL_PARAMS:
            if result.output:
                assert 'from-json' not in result.output
                assert 'Missing' in result.output or 'UsageError' in result.output or 'ServiceError' in result.output
        else:
            assert 'from-json' not in result.output
            if cmd == ['network', 'public-ip', 'get']:
                # This command displays a different message
                assert 'At least one of the options' in str(result.output)
            else:
                assert 'Missing option' in result.output or 'Are you sure' in str(result.output)


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
