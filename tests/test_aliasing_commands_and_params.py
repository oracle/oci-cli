# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from . import util
from . import test_config_container
import json
import os
import os.path


def test_command_global_alias_collision():
    with test_config_container.create_vcr().use_cassette('aliasing_commands_and_params_test_command_global_alias_collision.yml'):
        result = invoke(['os', 'bucket', 'create', '--cli-rc-file', os.path.join('tests', 'resources', 'aliasing', 'global_command_alias_with_collision'), '-?'])
        assert "Could not use 'create' as an alias for 'list' as it belongs to an existing command under 'os bucket'" in result.output

        # This command causes no collision and so should give no error but instead just emit the help
        result = invoke(['os', 'bucket', 'ls', '--cli-rc-file', os.path.join('tests', 'resources', 'aliasing', 'global_command_alias_with_collision'), '-?'])
        assert 'oci os bucket ls' in result.output
        assert '--compartment-id' in result.output
        assert '--namespace' in result.output


def test_command_sequence_alias_collision():
    with test_config_container.create_vcr().use_cassette('aliasing_commands_and_params_test_command_sequence_alias_collision.yml'):
        result = invoke(['os', 'bucket', 'create', '--cli-rc-file', os.path.join('tests', 'resources', 'aliasing', 'command_sequence_alias_with_collision'), '-?'])
        assert "Could not use 'create' as an alias for 'list' as it belongs to an existing command under 'os bucket'" in result.output

        # This command causes no collision and so should give no error but instead just emit the help
        result = invoke(['os', 'object', 'meta', '--cli-rc-file', os.path.join('tests', 'resources', 'aliasing', 'command_sequence_alias_with_collision'), '-?'])
        assert 'oci os object meta' in result.output
        assert '--namespace' in result.output
        assert '--bucket-name' in result.output


def test_invoke_using_global_command_alias():
    with test_config_container.create_vcr().use_cassette('aliasing_commands_and_params_test_invoke_using_global_command_alias.yml'):

        # Grab the Object Storage namespace
        result = invoke(['os', 'ns', 'get'])
        util.validate_response(result)
        namespace = json.loads(result.output)['data']

        result = invoke(['os', 'bucket', 'ls', '-ns', namespace, '-c', util.COMPARTMENT_ID, '--cli-rc-file', os.path.join('tests', 'resources', 'aliasing', 'global_command_alias_with_collision')])
        util.validate_response(result)

        parsed_result = json.loads(result.output)
        for d in parsed_result['data']:
            assert d['namespace'] == namespace
            assert d['name']

        result = invoke(['net', 'vcn', 'list', '-c', util.COMPARTMENT_ID, '--cli-rc-file', os.path.join('tests', 'resources', 'aliasing', 'global_command_alias_with_collision')])
        util.validate_response(result)

        if result.output != '':
            parsed_result = json.loads(result.output)
            for d in parsed_result['data']:
                assert d['id']


def test_invoke_using_command_sequence_alias():
    with test_config_container.create_vcr().use_cassette('aliasing_commands_and_params_test_invoke_using_command_sequence_alias.yml'):
        # Grab the Object Storage namespace
        result = invoke(['os', 'ns', 'get'])
        util.validate_response(result)
        namespace = json.loads(result.output)['data']

        result = invoke(['os', 'bucket', 'ls', '-ns', namespace, '-c', util.COMPARTMENT_ID, '--cli-rc-file', os.path.join('tests', 'resources', 'aliasing', 'command_sequence_alias_with_collision')])
        util.validate_response(result)

        parsed_result = json.loads(result.output)
        for d in parsed_result['data']:
            assert d['namespace'] == namespace
            assert d['name']


def test_param_alias_with_collision():
    with test_config_container.create_vcr().use_cassette('aliasing_commands_and_params_test_param_alias_with_collision.yml'):
        result = invoke(['compute', 'instance', 'list', '-?', '--cli-rc-file', os.path.join('tests', 'resources', 'aliasing', 'param_alias_with_collision')])
        assert 'Could not add alias --compartment-id to param --display-name as it conflicts with existing options for parameter --compartment-id' in result.output


def test_param_alias_no_collision():
    with test_config_container.create_vcr().use_cassette('aliasing_commands_and_params_test_param_alias_no_collision.yml'):
        result = invoke(['network', 'security-list', 'create', '-?', '--cli-rc-file', os.path.join('tests', 'resources', 'aliasing', 'param_alias_with_no_collision')])
        assert 'Could not alias' not in result.output

        # Check our aliases are displayed in the help
        assert '--compy' in result.output
        assert '-vid' in result.output
        assert '-dn' in result.output
        assert '--egress' in result.output
        assert '--ingress' in result.output


def test_param_alias_with_bad_name():
    with test_config_container.create_vcr().use_cassette('aliasing_commands_and_params_test_param_alias_with_bad_name.yml'):
        result = invoke(['network', 'security-list', 'create', '-?', '--cli-rc-file', os.path.join('tests', 'resources', 'aliasing', 'param_alias_with_bad_name')])
        assert "Could not create an alias for -foo as aliases need to be prefixed with '--' or be a single dash followed by a single letter. For example: --alias, -a" in result.output


def test_invoke_using_param_aliases():
    with test_config_container.create_vcr().use_cassette('aliasing_commands_and_params_test_invoke_using_param_aliases.yml'):
        result = invoke(['compute', 'instance', 'list', '--compy', util.COMPARTMENT_ID, '--ad', util.availability_domain(), '--cli-rc-file', os.path.join('tests', 'resources', 'aliasing', 'param_alias_with_no_collision')])
        util.validate_response(result)

        if result.output != '':
            parsed_result = json.loads(result.output)
            for d in parsed_result['data']:
                assert d['id']
                assert d['image-id']
                assert util.availability_domain() == d['availability-domain']

        result = invoke(['compute', 'instance', 'list', '--compy', util.COMPARTMENT_ID, '-a', util.availability_domain(), '--cli-rc-file', os.path.join('tests', 'resources', 'aliasing', 'param_alias_with_no_collision')])
        util.validate_response(result)

        if result.output != '':
            parsed_result = json.loads(result.output)
            for d in parsed_result['data']:
                assert d['id']
                assert d['image-id']
                assert util.availability_domain() == d['availability-domain']


def test_using_defaults_and_aliases():
    with test_config_container.create_vcr().use_cassette('aliasing_commands_and_params_test_using_defaults_and_aliases.yml'):
        file_with_aliases_and_defaults = """
[DEFAULT]
compute.machine.ls.compartment-id={}
compute.machine.ls.ad={}

[OCI_CLI_COMMAND_ALIASES]
machine=instance
ls=list

[OCI_CLI_PARAM_ALIASES]
--ad = --availability-domain
""".format(util.COMPARTMENT_ID, util.availability_domain())

        if not os.path.exists(os.path.join('tests', 'temp')):
            os.makedirs(os.path.join('tests', 'temp'))

        test_default_file_path = os.path.join('tests', 'temp', 'test_default_file')
        with open(test_default_file_path, 'w') as f:
            f.write(file_with_aliases_and_defaults)

        result = invoke(['compute', 'machine', 'ls', '--cli-rc-file', test_default_file_path])
        util.validate_response(result)

        if result.output != '':
            parsed_result = json.loads(result.output)
            for d in parsed_result['data']:
                assert d['availability-domain'] == util.availability_domain()

        os.remove(test_default_file_path)


def invoke(commands, debug=False, ** args):
    if debug is True:
        commands = ['--debug'] + commands

    return util.invoke_command(commands, ** args)
