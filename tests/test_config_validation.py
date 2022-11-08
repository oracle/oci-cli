# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci import identity, Response
import oci_cli
import os
import tempfile
import shutil
import unittest.mock as mock
import click

REGION = 'us-phoenix-1'
TEST_JWT_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPQ0kgVGVzdCBKV1QgVG9rZW4iLCJpYXQiOjE1MzkxMTAzOTAsImV4cCI6MTc2MDAzNTE5MCwiYXVkIjoid3d3Lm9yYWNsZWNsb3VkLmNvbSIsInN1YiI6Im9jaWQxLnVzZXIub2MxLi5hYWFhYWFhYTR2eGZvdnd5Z3R5amxxY3ptbjZqdTNrb3JrdGlkemxrNmF1dzZjNHRnc3h4eHh4eHh4eHgiLCJ0ZW5hbnQiOiJ0ZXN0X3RlbmFuY3kifQ.i9PP_5up4UAgFx7usppp_okaFDRpmzF0YECDsfN-gjU'
LIST_REGION_SUBSCRIPTIONS_RESPONSE = Response(status=None, headers=None, data=[
    identity.models.RegionSubscription(region_name="non-home-region", is_home_region=False),
    identity.models.RegionSubscription(region_name=REGION, is_home_region=True)
], request=None)


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


def test_auth_security_token_with_no_config(runner):
    try:
        # create a temporary config file path that will be treated as the default config that does not exist
        temp_dir = tempfile.mkdtemp()
        oci_cli.cli_setup.DEFAULT_DIRECTORY = temp_dir
        config_file = os.path.join(temp_dir, 'config')
        oci_cli.cli_setup.DEFAULT_CONFIG_LOCATION = config_file
        os.environ['OCI_CLI_CONFIG_FILE'] = config_file

        with mock.patch('oci_cli.cli_setup_bootstrap.webbrowser') as mock_webbrowser:
            with mock.patch('oci.identity.IdentityClient') as mock_identity_client_class:
                with mock.patch('oci_cli.cli_setup_bootstrap.StoppableHttpServer') as mock_stoppable_http_server:
                    mock_stoppable_http_server.return_value.serve_forever.return_value = TEST_JWT_TOKEN
                    mock_identity_client_class.return_value.list_region_subscriptions.return_value = LIST_REGION_SUBSCRIPTIONS_RESPONSE

                    # do not launch the web browser when running test
                    mock_webbrowser.open_new = mock.Mock(return_value=True)

                    # make sure config file does not exist yet
                    assert not os.path.exists(config_file)

                    stdin = [
                        'n',  # choose not to create new config file
                    ]

                    # test CLI command with security_token auth and no config file, and choose not to create new config file
                    result = invoke_example_operation(runner, config_file, 'DEFAULT', ['--auth', 'security_token'], command_input='\n'.join(stdin))
                    assert 'Could not find config file' in result.output
                    assert result.exit_code == 1

                    stdin = [
                        'Y',  # choose to create new config file
                        REGION
                    ]

                    # test CLI command with security_token auth and no config file, and choose to create new config file
                    result = invoke_example_operation(runner, config_file, 'DEFAULT', ['--auth', 'security_token'], command_input='\n'.join(stdin))
                    assert 'Could not find config file' in result.output
                    assert 'Do you want to create a new config file' in result.output
                    assert 'Try out your newly created session credentials' in result.output
                    assert result.exit_code == 0

                    # make sure config file now exists
                    assert os.path.exists(config_file)

                    # test CLI command with security_token auth and existing config file, and make sure new config file prompt does not appear
                    result = invoke_example_operation(runner, config_file, 'DEFAULT', ['--auth', 'security_token'], command_input='\n'.join(stdin))
                    assert 'Could not find config file' not in result.output
    finally:
        shutil.rmtree(temp_dir)
        os.environ['OCI_CLI_CONFIG_FILE'] = 'internal_resources/config'


def test_auth_security_token_with_expired_session(runner):
    try:
        # create a temporary config file path that will be treated as the default config containing an expired session profile
        temp_dir = tempfile.mkdtemp()
        oci_cli.cli_setup.DEFAULT_DIRECTORY = temp_dir
        config_file = os.path.join(temp_dir, 'config')
        oci_cli.cli_setup.DEFAULT_CONFIG_LOCATION = config_file
        os.environ['OCI_CLI_CONFIG_FILE'] = config_file

        profile_name = 'TESTSESSION'
        expired_test_jwt_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPQ0kgVGVzdCBKV1QgVG9rZW4iLCJpYXQiOjE1MzkxMTAzOTAsImV4cCI6MTYwMzAzNTE5MCwiYXVkIjoid3d3Lm9yYWNsZWNsb3VkLmNvbSIsInN1YiI6Im9jaWQxLnVzZXIub2MxLi5hYWFhYWFhYTR2eGZvdnd5Z3R5amxxY3ptbjZqdTNrb3JrdGlkemxrNmF1dzZjNHRnc3h4eHh4eHh4eHgiLCJ0ZW5hbnQiOiJ0ZXN0X3RlbmFuY3kifQ.D6siip7uDVm7-aNFbwYyVx4U-eGPGWAtXX0Hl_Q0BC8'
        valid_test_jwt_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPQ0kgVGVzdCBKV1QgVG9rZW4iLCJpYXQiOjE1MzkxMTAzOTAsImV4cCI6MTc2MDAzNTE5MCwiYXVkIjoid3d3Lm9yYWNsZWNsb3VkLmNvbSIsInN1YiI6Im9jaWQxLnVzZXIub2MxLi5hYWFhYWFhYTR2eGZvdnd5Z3R5amxxY3ptbjZqdTNrb3JrdGlkemxrNmF1dzZjNHRnc3h4eHh4eHh4eHgiLCJ0ZW5hbnQiOiJ0ZXN0X3RlbmFuY3kifQ.i9PP_5up4UAgFx7usppp_okaFDRpmzF0YECDsfN-gjU'
        test_private_key = [
            '-----BEGIN RSA PRIVATE KEY-----\n',
            'MIIEogIBAAKCAQBhXBjW6xVhhnPI8vlcJ/P/yhy4NWzRWcyw0mnB986dEit2n9O8\n',
            '5IrHEgqf1yuDZ26remS9hW+InL0uTafLNQ+njW4U7k7SerAmi1J5Lst3n0W67qHf\n',
            'onAUcEKuXB0TZs4TuUFZ9iwO7x8qREawClUYma2k0k9/PJrOqDk9b/YNwGjNHXdg\n',
            'IGG25fDEdWhEpmBRSFyQCxl/S7I8GPzJhwSzkD0xeVuTPyoc5kQ82VUKByw8Kmup\n',
            'cueKXfYmzFMrLY1FPOvq33HpPMQBfVlqlhMszTX6LesdqXKXeOcsDh1k1B8QGo7P\n',
            'N9fW7Pe+XBeKcqJZAEEKUlvLC1jFBcz6GbVpAgMBAAECggEAAIGvK2cbvF8ruQ7y\n',
            'lzUqAtm1XowAnfI+q2jc3gKBE7Ylfb+FJYV252RDo+NFubBPFhtT7NyF4QsXvObw\n',
            'iZEkHLYSrY8z38p9oiW1byX8LwooHbniI7y/oouW/TtDd3dgeR/MpEAwqH88BUdH\n',
            'quDS4obiLWpeuYXCNHMRoS009YtaGVldlxPp5gWD+5yvLXAa9+VE+IwCka+ap0mh\n',
            'ys4NYl7VruPFk2lEwlSLF7p1Y81wQMfy3FfwTqvZ0eEkLlH9UnLMDBwAc85IslxX\n',
            'jcGJMeq4zl1Ir+a6AlnsLo5azo1hZavJLwfkCRMa12WBcQh/0ZErplSK6UDaLjRa\n',
            'rpfpZQKBgQCvUYKdYV3LQMw47WzjbFnNGQkV7zSJJQN6Gr3dxII3mwUs3MU01dxS\n',
            'KgzfAZGX7XRyVxhqZ7bqfjH2y5ok3+f7aflnav2nFtrlXBas0fJOkSoacl0eG/Rc\n',
            '1HVY4I4cZWo/tEEQjETuvXh3OmeTNb2g7JkXVjbKHqYIJE0/XllfHwKBgQCOKi1K\n',
            'RbOXQr1f6IzOUzT/UxhWiBQJcu0gMCgC6hvuj77S+kYx3Qigsg8hdiyfoxVP4Goc\n',
            'EFYmoXLyy9XLmfiDQ4a2Hj/2gkB1z2m9yh7szr/X5lcktBI+Pi9y6MBLY98GW7ZR\n',
            'WuqaTGZNFtab8yf6nfWjsnY5/acNxRr8AWfCdwKBgHRgt0OhjpGNwgNIGDAfjL0J\n',
            'EW7uCwG/AD/d4IuGFqqyzQyqwH4COO6R21ltwSgJCHOePSblEhc3DhO1s+0mdOf/\n',
            'wP9VlmuEUGpQZvzxoNdmpXxIzmdeRygYII2PAsb2y0DedxJ1Co0wWPdMXdTqp6Zb\n',
            'aISFRnmFPtHIxz55cvohAoGAFYF33HZy1nz4HNwXANdBeyZc1io7rbo++NGQG/DC\n',
            'TPJd0ZieqchgF78X3t37niKThMPUCW7HOYzO0L/ZFbWzDFhYtpAY6PeHPMslmdpL\n',
            'l1MnXkewAxNidxv9HYrsG/t9r36MM/5m4vSPvTWpPWopMBZZJGxIyjj+3mxkyp6D\n',
            'zb0CgYEArqTyIwI9ocNQPzsLz77xASqp6A9wsx/K/UyKd/pvlb4likQpP6RIKasK\n',
            '0xbsmgjtLmiWxCywOpaN/Z4rsd5lPJNH65CcZJxkEvmzYH7x7OX+ymu7DpOHx35x\n',
            'x8liaJMyPiPM42GhJZDYvpqLdmubD/9dG6Fyz4E3W4z4Ms8AQOY=\n',
            '-----END RSA PRIVATE KEY-----'
        ]

        sessions_dir = os.path.join(temp_dir, 'sessions')
        os.mkdir(sessions_dir)
        session_dir = os.path.join(sessions_dir, profile_name)
        os.mkdir(session_dir)
        key_file = os.path.join(session_dir, oci_cli.cli_setup.DEFAULT_KEY_NAME + oci_cli.cli_setup.PRIVATE_KEY_FILENAME_SUFFIX)
        token_file = os.path.join(session_dir, 'token')

        profile = [
            '[{}]\n'.format(profile_name),
            'fingerprint = test_fingerprint\n',
            'key_file = {}\n'.format(key_file),
            'tenancy = test_tenancy\n',
            'region = {}\n'.format(REGION),
            'security_token_file = {}'.format(token_file)
        ]

        with open(config_file, 'w') as conf:
            conf.writelines(profile)

        with open(key_file, 'w') as keyf:
            keyf.writelines(test_private_key)

        with open(token_file, 'w') as tokenf:
            tokenf.write(expired_test_jwt_token)

        with mock.patch('oci_cli.cli_setup_bootstrap.webbrowser') as mock_webbrowser:
            with mock.patch('oci.identity.IdentityClient') as mock_identity_client_class:
                with mock.patch('oci_cli.cli_setup_bootstrap.StoppableHttpServer') as mock_stoppable_http_server:
                    # return "valid" token to simulate re-authenticated token
                    mock_stoppable_http_server.return_value.serve_forever.return_value = valid_test_jwt_token
                    mock_identity_client_class.return_value.list_region_subscriptions.return_value = LIST_REGION_SUBSCRIPTIONS_RESPONSE

                    # do not launch the web browser when running test
                    mock_webbrowser.open_new = mock.Mock(return_value=True)

                    stdin = [
                        'n',  # choose not to re-authenticate the session
                    ]

                    # test CLI command with security_token auth and expired session profile, and choose not to re-authenticate the session
                    result = invoke_example_operation(runner, config_file, profile_name, ['--auth', 'security_token'], command_input='\n'.join(stdin))
                    assert 'This CLI session has expired' in result.output
                    assert result.exit_code == 1

                    stdin = [
                        'Y',  # choose to re-authenticate session
                        REGION
                    ]

                    # test CLI command with security_token auth and expired session profile, and choose to re-authenticate the session
                    result = invoke_example_operation(runner, config_file, profile_name, ['--auth', 'security_token'], command_input='\n'.join(stdin))
                    assert 'This CLI session has expired' in result.output
                    assert 'Do you want to re-authenticate' in result.output
                    assert 'Try out your newly created session credentials' in result.output
                    assert result.exit_code == 0

                    # test CLI command with security_token auth and existing config file, and make sure expired session prompt does not appear
                    result = invoke_example_operation(runner, config_file, profile_name, ['--auth', 'security_token'], command_input='\n'.join(stdin))
                    assert 'This CLI session has expired' not in result.output
    finally:
        shutil.rmtree(temp_dir)
        os.environ['OCI_CLI_CONFIG_FILE'] = 'internal_resources/config'


def test_command_with_no_config(runner):
    try:
        # create a temporary config file path that will be treated as the default config that does not exist
        temp_dir = tempfile.mkdtemp()
        oci_cli.cli_setup.DEFAULT_DIRECTORY = temp_dir
        config_file = os.path.join(temp_dir, 'config')
        oci_cli.cli_setup.DEFAULT_CONFIG_LOCATION = config_file
        os.environ['OCI_CLI_CONFIG_FILE'] = config_file

        test_ocid = 'ocid1.user.oc1..aaaaaaaa4vxfovwygtyjlqczmn6ju3korktidzlk6auw6c4tgsug5brc2ekq'
        test_tenancy = 'ocid1.tenancy.oc1..aaaaaaaa3vi3ft3yi3sq4nhiql4nvbzjz6gipbn72h7werl6njs6xsq4wgdq'

        # make sure config file does not exist yet
        assert not os.path.exists(config_file)

        stdin = [
            'n',  # choose not to create new config file
        ]

        # test CLI command with no config file, and choose not to create new config file
        result = invoke_example_operation(runner, config_file, 'DEFAULT', command_input='\n'.join(stdin))
        assert 'Could not find config file' in result.output
        assert result.exit_code == 1

        stdin = [
            'Y',  # choose to create new config file
            'n',  # choose not to use browser login (no setup bootstrap)
            config_file,  # location for the new config file
            test_ocid,
            test_tenancy,
            REGION,
            'Y',  # generate new key pair
            temp_dir,  # directory for the keys
            oci_cli.cli_setup.DEFAULT_KEY_NAME,
            '',  # no private key passphrase
        ]

        # test CLI command with no config file, and choose to create new config file with browserless setup
        result = invoke_example_operation(runner, config_file, 'DEFAULT', command_input='\n'.join(stdin))
        assert 'Could not find config file' in result.output
        assert 'Do you want to create a new config file' in result.output
        assert 'Config written to' in result.output
        assert result.exit_code == 0

        # make sure config file now exists
        assert os.path.exists(config_file)

        # test CLI command with existing config file, and make sure new config file prompt does not appear
        result = invoke_example_operation(runner, config_file, 'DEFAULT', command_input='\n'.join(stdin))
        assert 'Could not find config file' not in result.output

        # remove the config file and api keys
        os.remove(config_file)
        os.remove(os.path.join(temp_dir, oci_cli.cli_setup.DEFAULT_KEY_NAME + oci_cli.cli_setup.PRIVATE_KEY_FILENAME_SUFFIX))
        os.remove(os.path.join(temp_dir, oci_cli.cli_setup.DEFAULT_KEY_NAME + oci_cli.cli_setup.PUBLIC_KEY_FILENAME_SUFFIX))

        with mock.patch('oci_cli.cli_setup_bootstrap.webbrowser') as mock_webbrowser:
            with mock.patch('oci.identity.IdentityClient') as mock_identity_client_class:
                with mock.patch('oci_cli.cli_setup_bootstrap.StoppableHttpServer') as mock_stoppable_http_server:
                    mock_stoppable_http_server.return_value.serve_forever.return_value = TEST_JWT_TOKEN
                    mock_identity_client_class.return_value.list_region_subscriptions.return_value = LIST_REGION_SUBSCRIPTIONS_RESPONSE

                    # do not launch the web browser when running unit test
                    mock_webbrowser.open_new = mock.Mock(return_value=True)

                    # make sure config file does not exist yet
                    assert not os.path.exists(config_file)

                    # when this test is being run, there might not be a runnable browser, in which case the oci setup config function would be used
                    # so, this forces oci setup bootstrap to be used for the purposes of this test
                    def config_setup_function():
                        if click.confirm('Do you want to create your config file by logging in through a browser?', default=True):
                            return oci_cli.cli_setup_bootstrap.bootstrap_oci_cli
                        # this won't be used during this test since the input given to the prompt above will be 'Y'
                        return oci_cli.cli_setup.generate_oci_config
                    oci_cli.cli_util.get_config_setup_function = config_setup_function

                    stdin = [
                        'Y',  # choose to create new config file
                        'Y',  # choose to use browser login (setup bootstrap)
                        REGION,
                        '',  # no private key passphrase
                    ]

                    # test CLI command with no config file, and choose to create new config file with browser-based setup
                    result = invoke_example_operation(runner, config_file, 'DEFAULT', command_input='\n'.join(stdin))
                    assert 'Could not find config file' in result.output
                    assert 'Do you want to create a new config file' in result.output
                    assert 'Config written to' in result.output
                    assert result.exit_code == 0

                    # make sure config file now exists
                    assert os.path.exists(config_file)

                    # test CLI command with existing config file, and make sure new config file prompt does not appear
                    result = invoke_example_operation(runner, config_file, 'DEFAULT', command_input='\n'.join(stdin))
                    assert 'Could not find config file' not in result.output
    finally:
        shutil.rmtree(temp_dir)
        os.environ['OCI_CLI_CONFIG_FILE'] = 'internal_resources/config'


def validate_missing_param_error(result, key, message):
    assert 1 == result.exit_code
    assert message in result.output
    assert key in result.output


def invoke_example_operation(runner, config_file, profile, root_args=[], command_args=[], command_input=None):
    return runner.invoke(oci_cli.cli, root_args + ['--config-file', config_file, '--profile', profile, 'os', 'ns', 'get'] + command_args, input=command_input)
