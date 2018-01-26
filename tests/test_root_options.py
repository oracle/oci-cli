# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import oci_cli
import oci
import os
from mock import patch


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
    result = invoke_example_operation(runner, ['--cli-rc-file', 'tests/resources/default_files/settings_with_invalid_default_profile'], config_file)
    assert "ERROR: Profile 'INAVLID_PROFILE' not found in config file" in result.output
    assert 1 == result.exit_code


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


def invoke_example_operation(runner, root_args, config_file):
    args = root_args + (['--config-file', config_file] if config_file else []) + ['os', 'ns', 'get']
    return runner.invoke(oci_cli.cli, args)
