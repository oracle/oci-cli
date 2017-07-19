# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import oraclebmc_cli


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
    assert 0 != result.exit_code


def invoke_example_operation(runner, root_args, config_file):
    return runner.invoke(oraclebmc_cli.cli, root_args + ['--config-file', config_file, 'os', 'ns', 'get'])
