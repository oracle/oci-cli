# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from . import util
from . import test_config_container
import click
import json
import oci_cli
import six
import random
import vcr
import os


# Commands which we skip evaluation of because they don't have the JSON input
IGNORED_COMMANDS = [
    ['setup', 'autocomplete'],
    ['setup', 'bootstrap'],
    ['setup', 'config'],
    ['setup', 'keys'],
    ['setup', 'repair-file-permissions'],
    ['setup', 'oci-cli-rc'],
    ['session', 'authenticate'],
    ['session', 'export'],
    ['session', 'import'],
    ['session', 'refresh'],
    ['session', 'terminate'],
    ['session', 'validate'],
    # Note this is being added b/c python sdk doesn't generate models
    # for top level enums.
    # This means that the --generate-full-command-json-input will not work
    # for these commands.
    ['cims', 'incident', 'create'],
    ['cims', 'incident', 'update'],
    ['dts', 'nfs-dataset', 'activate'],
    ['dts', 'nfs-dataset', 'create'],
    ['dts', 'nfs-dataset', 'deactivate'],
    ['dts', 'nfs-dataset', 'delete'],
    ['dts', 'nfs-dataset', 'get-seal-manifest'],
    ['dts', 'nfs-dataset', 'list'],
    ['dts', 'nfs-dataset', 'reopen'],
    ['dts', 'nfs-dataset', 'seal'],
    ['dts', 'nfs-dataset', 'seal-status'],
    ['dts', 'nfs-dataset', 'set-export'],
    ['dts', 'nfs-dataset', 'show'],
    ['dts', 'physical-appliance', 'list'],
    ['dts', 'physical-appliance', 'show'],
    ['dts', 'physical-appliance', 'unregister'],
    ['dts', 'physical-appliance', 'configure-encryption'],
    ['dts', 'physical-appliance', 'finalize'],
    ['dts', 'physical-appliance', 'initialize-authentication'],
    ['dts', 'physical-appliance', 'unlock'],
    ['dts', 'job', 'verify-upload-user-credentials']
]

# List of extended commands for which test_run_all_commands will fail. These tests fail because of the extended code, where we
# check for a combination of input params. Please add a new command to this list, if the test is failing because of extended code.
IGNORE_EXTENDED_TESTS_COMMANDS = [
    ['bv', 'boot-volume', 'create'],
    ['bv', 'volume', 'create'],
    ['compute', 'instance', 'launch'],
    ['iam', 'api-key', 'upload'],
    ['iam', 'user', 'api-key', 'upload'],
    ['network', 'public-ip', 'get'],
    ['os', 'object', 'bulk-download'],
    ['os', 'object', 'bulk-upload'],
    ['os', 'object', 'put'],
    ['os', 'object', 'resume-put'],
    ['os', 'object', 'bulk-delete'],
    ['batch', 'job-log', 'get'],
    ['waas', 'protection-settings', 'update'],
    ['resource-manager', 'stack', 'update'],
    ['resource-manager', 'stack', 'create'],
    ['waas', 'protection-settings', 'update'],
    ['waas', 'policy-config', 'update'],
    ['dts', 'nfs-dataset', 'activate'],
    ['dts', 'nfs-dataset', 'create'],
    ['dts', 'nfs-dataset', 'deactivate'],
    ['dts', 'nfs-dataset', 'delete'],
    ['dts', 'nfs-dataset', 'get-seal-manifest'],
    ['dts', 'nfs-dataset', 'list'],
    ['dts', 'nfs-dataset', 'reopen'],
    ['dts', 'nfs-dataset', 'seal'],
    ['dts', 'nfs-dataset', 'seal-status'],
    ['dts', 'nfs-dataset', 'set-export'],
    ['dts', 'nfs-dataset', 'show'],
    ['dts', 'physical-appliance', 'list'],
    ['dts', 'physical-appliance', 'show'],
    ['dts', 'physical-appliance', 'unregister'],
    ['dts', 'physical-appliance', 'configure-encryption'],
    ['dts', 'physical-appliance', 'finalize'],
    ['dts', 'physical-appliance', 'initialize-authentication'],
    ['dts', 'physical-appliance', 'unlock'],
    ['dts', 'job', 'verify-upload-user-credentials'],
    ['resource-manager', 'job', 'create-import-tf-state-job'],
    ['waas', 'waas-policy', 'list'],
    ['waas', 'certificate', 'list']
]


# Commands which have no parameters and so produce empty dictionaries
# Current output:
# ['iam', 'region', 'list'],
# ['network', 'peer-region-for-remote-peering', 'list-allowed-peer-regions-for-remote-peering'],
# ['os', 'ns', 'get']
# From returned list of (command, number of params, number of required params),
# filter command names with number of params <= 2 (--help and --from-json) into a sorted list.
COMMANDS_WITH_NO_PARAMS = sorted(command for command, _, _ in
                                 filter(lambda x: x[1] <= 2 and x[0] not in IGNORED_COMMANDS,
                                        util.collect_leaf_commands_with_counts(oci_cli.cli)))


# Commands whose parameters are all marked as optional
# though some combination of them may be needed for calls to succeed
# Current output:
# [['bv', 'volume', 'create'],
# ['bv', 'volume-backup-policy', 'list'],
# ['db', 'backup', 'list'],
# ['fs', 'export', 'list'],
# ['iam', 'compartment', 'list'],
# ['iam', 'region', 'list'],
# ['network', 'peer-region-for-remote-peering', 'list-allowed-peer-regions-for-remote-peering'],
# ['network', 'private-ip', 'list'],
# ['network', 'public-ip', 'get'],
# ['network', 'service', 'list'],
# ['os', 'ns', 'get'],
# ['os', 'ns', 'get-metadata'],
# ['os', 'ns', 'update-metadata'],
# ['rqs', 'resource-type', 'list']]
# From returned list of (command, number of params, number of required params),
# filter command names with number of required params == 0 and command not in IGNORED_COMMANDS list into a sorted list.
COMMANDS_WITH_ALL_OPTIONAL_PARAMS = sorted(command for command, _, _ in
                                           filter(lambda x: x[2] == 0 and x[0] not in IGNORED_COMMANDS,
                                                  util.collect_leaf_commands_with_counts(oci_cli.cli)))

commands_list = [cmd for cmd in sorted(util.collect_commands(oci_cli.cli, leaf_commands_only=True))
                 if cmd not in IGNORED_COMMANDS]


def test_all_commands_generate_skeleton():

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
def test_run_all_commands(runner, config_file, config_profile, tmpdir):
    failed_commands = []
    for cmd in commands_list:
        if cmd not in IGNORE_EXTENDED_TESTS_COMMANDS:
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

    assert len(failed_commands) == 0, 'The following commands failed to run: {}'.format(failed_commands)


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


def _traverse_oci_cli(command, path, failed_commands):
    if hasattr(command, "commands"):
        for name, command in six.iteritems(command.commands):
            _traverse_oci_cli(command, path + [name], failed_commands)
    else:
        if path not in IGNORED_COMMANDS:
            complex_options = [option for option in command.params if str(option.type) == 'COMPLEX_TYPE']
            if complex_options:
                for option in complex_options:
                    full_command = path + ['--generate-param-json-input', option.name.replace('_', '-')]
                    result = util.invoke_command(full_command)
                    if result.exit_code != 0 or 'is not a recognized complex type, so no example JSON can be produced. Invoke help for this command' in result.output:
                        print(full_command, result.exit_code)
                        failed_commands.append(full_command)


def test_generate_param_json_input_for_all_complex_types():
    failed_commands = []
    _traverse_oci_cli(oci_cli.cli, [], failed_commands)
    assert len(failed_commands) == 0, 'The following commands failed to run: {}'.format(failed_commands)


def test_all_commands_can_accept_from_json_input():
    with test_config_container.create_vcr().use_cassette('json_skeleton_command_coverage_test_all_commands_can_accept_from_json_input.yml'):
        for cmd in commands_list:
            full_command = list(cmd)
            full_command.extend(['--from-json', 'file://tests/resources/json_input/dummy.json'])
            result = util.invoke_command(full_command)
            if result.output:
                if 'CannotOverwriteExistingCassetteException' in result.output:
                    continue
                assert 'from-json' not in result.output
                if cmd in [['iam', 'compartment', 'list'],
                           ['iam', 'availability-domain', 'list']]:
                    # This command works with only optional parameters, so check that there are no errors and that\
                    # a response was received
                    assert 'error' not in result.output.lower() and 'missing' not in result.output.lower()
                    assert 'compartment-id' in result.output
                elif cmd in [['iam', 'region-subscription', 'list']]:
                    # This command works with only optional parameters, so check that there are no errors and that\
                    # a response was received
                    assert 'error' not in result.output.lower() and 'missing' not in result.output.lower()
                    assert 'region-name' in result.output
                elif cmd in [['network', 'service', 'list']]:
                    assert 'error' not in result.output.lower() and 'missing' not in result.output.lower()
                else:
                    assert 'from-json' not in result.output
                    if cmd == ['network', 'public-ip', 'get']:
                        # This command displays a different message
                        assert 'At least one of the options' in str(result.output)
        return


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
