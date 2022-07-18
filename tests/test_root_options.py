# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci_cli
import oci
import os
import six.moves
import traceback
from mock import patch
from oci_cli.cli_constants import OCI_CONFIG_REQUIRED_VARS as config_required_vars


def test_control_case(runner, config_file):
    # Use the correct R2 endpoint, should succeed.
    result = invoke_example_operation(runner, [], config_file)
    assert 0 == result.exit_code


def test_endpoint_option_sucess(runner, config_file):
    # Use the correct R2 endpoint, should succeed.
    result = invoke_example_operation(runner, ['--endpoint', "https://objectstorage.us-phoenix-1.oraclecloud.com"], config_file)
    assert 0 == result.exit_code


def test_endpoint_option_bad_endpoint(runner, config_file):
    result = invoke_example_operation(runner, ['--endpoint', 'https://notaservice.us-phoenix-1.oraclecloud.com'], config_file)
    assert 0 != result.exit_code


def test_endpoint_and_region_option(runner, config_file):
    # Should use the endpoint, not the region.
    result = invoke_example_operation(runner, ['--endpoint', "https://objectstorage.us-phoenix-1.oraclecloud.com", '--region', 'badregion'], config_file)
    assert 0 == result.exit_code


def test_endpoint_option_without_region_in_config(runner, malformed_config_file):
    # Config file does not have region, but endpoint option is given.
    result = invoke_example_operation(runner, ['--endpoint', "https://objectstorage.us-phoenix-1.oraclecloud.com", '--profile', 'MISSING_REGION'], config_file=malformed_config_file)
    assert 0 == result.exit_code


def test_endpoint_in_config_not_used(runner):
    # Config file specifies an invalid endpoint and a valid region. Endpoint is not a valid
    # key in the config, so verify that it is not used.
    result = invoke_example_operation(runner, ['--profile', 'SPECIFY_BAD_ENDPOINT'], config_file='tests/resources/malformed_config')
    assert 0 == result.exit_code


def test_region_option_without_region_in_config(runner):
    # Config file does not have region, but region option is given.
    result = invoke_example_operation(runner, ['--region', "us-phoenix-1", '--profile', 'MISSING_REGION'], config_file='tests/resources/malformed_config')
    assert 0 == result.exit_code


def test_cert_bundle_option(runner, config_file):
    result = invoke_example_operation(runner, ['--cert-bundle', 'tests/resources/doesnotexist'], config_file)
    assert 'BadParameter: Cannot find cert_bundle file' in result.output
    assert 0 != result.exit_code


def test_connection_timeout_read_timeout_option_success(runner, config_file):
    # Should take the given timeout
    result = invoke_example_operation(runner, ['--connection-timeout', "20", "--read-timeout", "20"], config_file)
    assert 0 == result.exit_code


def test_connection_timeout_option_success(runner, config_file):
    # Should take the given timeout
    result = invoke_example_operation(runner, ['--connection-timeout', "30"], config_file)
    assert 0 == result.exit_code


def test_profile_option_overrides_default_setting(runner, config_file):
    result = invoke_example_operation(runner, ['--profile', 'DEFAULT', '--cli-rc-file', 'tests/resources/default_files/settings_with_invalid_default_profile'], config_file)
    assert 0 == result.exit_code


def test_profile_option_overrides_environment_variable(runner, config_file):
    os.environ[oci_cli.cli_constants.OCI_CLI_PROFILE_ENV_VAR] = 'INVALID_PROFILE'
    result = invoke_example_operation(runner, ['--profile', 'DEFAULT'], config_file)
    del os.environ[oci_cli.cli_constants.OCI_CLI_PROFILE_ENV_VAR]
    assert 0 == result.exit_code


def test_profile_env_var_overrides_default_setting(runner, config_file):
    os.environ[oci_cli.cli_constants.OCI_CLI_PROFILE_ENV_VAR] = 'DEFAULT'
    result = invoke_example_operation(runner, ['--cli-rc-file', 'tests/resources/default_files/settings_with_invalid_default_profile'], config_file)
    del os.environ[oci_cli.cli_constants.OCI_CLI_PROFILE_ENV_VAR]
    assert 0 == result.exit_code


def test_default_profile_setting_from_cli_rc_file(runner, config_file):
    env_vars = copy_config_required_vars()
    result = invoke_example_operation(runner, ['--cli-rc-file', 'tests/resources/default_files/settings_with_invalid_default_profile'], config_file)
    assert "ERROR: Profile 'INAVLID_PROFILE' not found in config file" in result.output
    assert 1 == result.exit_code
    os.environ.update(env_vars)


def test_rc_file_location_environment_variable(runner, config_file):
    env_vars = copy_config_required_vars()
    os.environ[oci_cli.cli_constants.OCI_CLI_RC_FILE_ENV_VAR] = 'tests/resources/default_files/settings_with_invalid_default_profile'
    result = invoke_example_operation(runner, [], config_file)
    del os.environ[oci_cli.cli_constants.OCI_CLI_RC_FILE_ENV_VAR]
    assert "ERROR: Profile 'INAVLID_PROFILE' not found in config file" in result.output
    assert 1 == result.exit_code
    os.environ.update(env_vars)


def test_config_file_location_environment_variable(runner, config_file):
    original_value = os.environ[oci_cli.cli_constants.OCI_CLI_CONFIG_FILE_ENV_VAR]
    os.environ[oci_cli.cli_constants.OCI_CLI_CONFIG_FILE_ENV_VAR] = 'tests/invalid_config'
    result = invoke_example_operation(runner, [], None, command_input='n')
    del os.environ[oci_cli.cli_constants.OCI_CLI_CONFIG_FILE_ENV_VAR]
    assert 1 == result.exit_code
    assert 'tests/invalid_config' in result.output

    # restore OCI_CLI_CONFIG_FILE env variable env variable as it used in other tests.
    os.environ[oci_cli.cli_constants.OCI_CLI_CONFIG_FILE_ENV_VAR] = original_value


def test_config_values_from_environment_variable_mock_config(runner, config_file):
    result = invoke_example_operation(runner, [], None)
    assert 0 == result.exit_code

    if oci_cli.cli_constants.OCI_CLI_USER_ENV_VAR in os.environ:
        del os.environ[oci_cli.cli_constants.OCI_CLI_USER_ENV_VAR]

    original_value = os.environ[oci_cli.cli_constants.OCI_CLI_CONFIG_FILE_ENV_VAR]
    os.environ[oci_cli.cli_constants.OCI_CLI_CONFIG_FILE_ENV_VAR] = 'tests/invalid_config'

    result = invoke_example_operation(runner, [], None, command_input='n')
    assert 1 == result.exit_code

    # restore OCI_CLI_CONFIG_FILE env variable env variable as it used in other tests.
    os.environ[oci_cli.cli_constants.OCI_CLI_CONFIG_FILE_ENV_VAR] = original_value


def test_config_values_from_environment_variable_overrides_default_settings(runner, config_file):
    values_to_test = list(oci_cli.cli_constants.OCI_CONFIG_ENV_VARS)
    values_to_test.extend([
        oci_cli.cli_constants.OCI_CLI_CERT_BUNDLE_ENV_VAR,
        oci_cli.cli_constants.OCI_CLI_ENDPOINT_ENV_VAR,
        oci_cli.cli_constants.OCI_CLI_REGION_ENV_VAR
    ])

    for key in values_to_test:
        print("Testing entry: " + key)
        os.environ[key] = 'invalid_value'
        result = invoke_example_operation(runner, [], config_file)
        del os.environ[key]
        if key not in [oci_cli.cli_constants.OCI_CLI_DELEGATION_TOKEN_FILE_ENV_VAR, oci_cli.cli_constants.OCI_CLI_SECURITY_TOKEN_FILE_ENV_VAR, oci_cli.cli_constants.OCI_CLI_PASSPHRASE_ENV_VAR]:
            assert 0 != result.exit_code


def test_root_level_options_overrides_environment_variable(runner, config_file):
    original_value = os.environ[oci_cli.cli_constants.OCI_CLI_CONFIG_FILE_ENV_VAR]
    values_to_test = [
        oci_cli.cli_constants.OCI_CLI_ENDPOINT_ENV_VAR,
        oci_cli.cli_constants.OCI_CLI_REGION_ENV_VAR,
        oci_cli.cli_constants.OCI_CLI_CONFIG_FILE_ENV_VAR,
        oci_cli.cli_constants.OCI_CLI_RC_FILE_ENV_VAR
    ]

    for key in values_to_test:
        print("Testing entry: " + key)
        os.environ[key] = 'invalid_value'

        result = invoke_example_operation(runner,
                                          ['--endpoint', 'https://objectstorage.us-phoenix-1.oraclecloud.com',
                                           '--region', "us-phoenix-1",
                                           '--cli-rc-file', 'tests/resources/default_files/settings_with_invalid_default_profile',
                                           '--profile', 'DEFAULT'],
                                          'internal_resources/config')

        del os.environ[key]
        assert 0 == result.exit_code

    # restore OCI_CLI_CONFIG_FILE env variable env variable as it used in other tests.
    os.environ[oci_cli.cli_constants.OCI_CLI_CONFIG_FILE_ENV_VAR] = original_value


def test_auth_instance_principal_param(runner, config_file):
    with patch.object(oci.auth.signers.InstancePrincipalsSecurityTokenSigner, '__init__', return_value=None) as mock_init:
        result = invoke_example_operation(runner, ['--auth', 'instance_principal'], 'non-existent-config')
    assert mock_init.called


def test_auth_instance_principal_env_var(runner, config_file):
    os.environ[oci_cli.cli_constants.OCI_CLI_AUTH_ENV_VAR] = 'instance_principal'
    with patch.object(oci.auth.signers.InstancePrincipalsSecurityTokenSigner, '__init__', return_value=None) as mock_init:
        result = invoke_example_operation(runner, [], 'non-existent-config')
    del os.environ[oci_cli.cli_constants.OCI_CLI_AUTH_ENV_VAR]
    assert mock_init.called


def test_auth_instance_principal_env_var_invalid(runner, config_file):
    os.environ[oci_cli.cli_constants.OCI_CLI_AUTH_ENV_VAR] = 'instance_pri'
    with patch.object(oci.auth.signers.InstancePrincipalsSecurityTokenSigner, '__init__', return_value=None) as mock_init:
        result = invoke_example_operation(runner, [], 'non-existent-config')
    del os.environ[oci_cli.cli_constants.OCI_CLI_AUTH_ENV_VAR]

    assert result.exit_code != 1
    assert 'Invalid value for OCI_CLI_AUTH' in result.output


def test_operation_retries_if_no_retry_not_supplied(runner, config_file):
    fake_endpoint = 'https://fakenamenotexist.netcom'
    result = invoke_example_operation(runner, ['--debug', '--endpoint', fake_endpoint], config_file)
    stack_trace = traceback.format_tb(result.exc_info[2])
    found_make_retrying_call = False
    for trace in stack_trace:
        if 'make_retrying_call' in trace:
            found_make_retrying_call = True

    assert found_make_retrying_call


# This test module interferes when run other modules and we're not mocking. What appears to be happening is that
# when a test module that contains a @pytest.mark.usefixtures class (this is needed for unittest-based tests as
# they don't otherwise support py.test fixture injection) is run BEFORE this module and another is run
# AFTER this module the debug level on HTTP clients is not appropriately reset.
#
# This teardown explicitly does this so that we don't get debug output in other tests (which can cause failures)
def teardown_module(module):
    six.moves.http_client.HTTPConnection.debuglevel = 0


def invoke_example_operation(runner, root_args, config_file, command_input=None):
    args = root_args + (['--config-file', config_file] if config_file else []) + ['os', 'ns', 'get']
    return runner.invoke(oci_cli.cli, args, input=command_input)


# Copies the env vars which are required to mock a config and removes them
# Needed for some tests if we've set env vars to mock a config but want to use an invalid config instead
def copy_config_required_vars():
    config_env_vars = {}
    for key in config_required_vars:
        if config_required_vars[key] in os.environ:
            config_env_vars.update({config_required_vars[key]: os.environ[config_required_vars[key]]})
            os.environ.pop(config_required_vars[key])
    return config_env_vars
