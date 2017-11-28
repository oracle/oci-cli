# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import oci_cli
import os.path


def test_missing_user(runner, malformed_config_file):
    result = invoke_example_operation(runner, malformed_config_file, 'MISSING_USER')
    validate_missing_param_error(result, 'user', 'log into the console')


def test_missing_fingerprint(runner, malformed_config_file):
    result = invoke_example_operation(runner, malformed_config_file, 'MISSING_FINGERPRINT')
    validate_missing_param_error(result, 'fingerprint', 'openssl rsa')


def test_missing_key(runner, malformed_config_file):
    result = invoke_example_operation(runner, malformed_config_file, 'MISSING_KEY')
    validate_missing_param_error(result, 'key', 'PEM key file')


def test_missing_tenancy(runner, malformed_config_file):
    result = invoke_example_operation(runner, malformed_config_file, 'MISSING_TENANCY')
    validate_missing_param_error(result, 'tenancy', 'OCID')


def test_missing_region(runner, malformed_config_file):
    result = invoke_example_operation(runner, malformed_config_file, 'MISSING_REGION')
    validate_missing_param_error(result, 'region', 'us-phoenix-1')


def test_region_parameter(runner, malformed_config_file):
    result = invoke_example_operation(runner, malformed_config_file, 'MISSING_REGION', ['--region', 'us-phoenix-1'])
    assert 0 == result.exit_code


def test_no_validation_when_using_help(runner, malformed_config_file):
    # Do not validate the config when asking for help.
    result = invoke_example_operation(runner, malformed_config_file, 'MISSING_KEY', command_args=['--cli-rc-file', os.path.join('tests', 'resources', 'default_files', 'use_click_help'), '-?'])
    assert 0 == result.exit_code


def validate_missing_param_error(result, key, message):
    assert 1 == result.exit_code
    assert message in result.output
    assert key in result.output


def invoke_example_operation(runner, config_file, profile, root_args=[], command_args=[]):
    return runner.invoke(oci_cli.cli, root_args + ['--config-file', config_file, '--profile', profile, 'os', 'ns', 'get'] + command_args)
