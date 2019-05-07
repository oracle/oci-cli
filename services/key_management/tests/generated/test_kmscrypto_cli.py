# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import json
import pytest
from tests import generated_test_request_transformers
from tests import test_config_container  # noqa: F401
from tests import util
import vcr
import oci_cli
import os


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
    # instead of 'query' matcher (which ignores sessionId in the url)
    # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
    custom_vcr = test_config_container.create_vcr(cassette_library_dir="services/key_management/tests/cassettes/for_generated")

    cassette_location = 'key_management_{name}.yml'.format(name=request.function.__name__)
    with custom_vcr.use_cassette(cassette_location):
        yield


@pytest.mark.generated
def test_decrypt(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('key_management', 'Decrypt'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('key_management', 'KmsCrypto', 'Decrypt')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_decrypt.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_decrypt', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_decrypt.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_decrypt'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_decrypt.pem'])
            config_file = 'tests/resources/config_for_test_decrypt'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('kms_crypto_root_group.command_name', 'kms-crypto')
    resource_group_command_name = oci_cli.cli_util.override('decrypted_data_group.command_name', 'decrypted_data')
    request_containers = cli_testing_service_client.get_requests(service_name='key_management', api_name='Decrypt')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'DecryptDataDetails'
            details = request.pop(param_name[0].lower() + param_name[1:])
            for key in details:
                request[key] = details[key]
                override = util.variable_name_override(key)
                if override:
                    request[override] = request.pop(key)

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('key_management', 'Decrypt', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('decrypt.command_name', 'decrypt'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: key_management, Decrypt. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('decrypt.command_name', 'decrypt'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('decrypt.command_name', 'decrypt')))

            params.append('--endpoint')
            params.append(cli_testing_service_client.get_endpoint("key_management", "KmsCryptoClient", "Decrypt"))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'key_management',
                    'Decrypt',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'decryptedData',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_decrypt.pem'):
                    os.remove('tests/resources/keyfile_for_test_decrypt.pem')
                if os.path.exists('tests/resources/config_for_test_decrypt'):
                    os.remove('tests/resources/config_for_test_decrypt')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='key_management', api_name='Decrypt')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_encrypt(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('key_management', 'Encrypt'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('key_management', 'KmsCrypto', 'Encrypt')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_encrypt.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_encrypt', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_encrypt.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_encrypt'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_encrypt.pem'])
            config_file = 'tests/resources/config_for_test_encrypt'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('kms_crypto_root_group.command_name', 'kms-crypto')
    resource_group_command_name = oci_cli.cli_util.override('encrypted_data_group.command_name', 'encrypted_data')
    request_containers = cli_testing_service_client.get_requests(service_name='key_management', api_name='Encrypt')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'EncryptDataDetails'
            details = request.pop(param_name[0].lower() + param_name[1:])
            for key in details:
                request[key] = details[key]
                override = util.variable_name_override(key)
                if override:
                    request[override] = request.pop(key)

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('key_management', 'Encrypt', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('encrypt.command_name', 'encrypt'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: key_management, Encrypt. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('encrypt.command_name', 'encrypt'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('encrypt.command_name', 'encrypt')))

            params.append('--endpoint')
            params.append(cli_testing_service_client.get_endpoint("key_management", "KmsCryptoClient", "Encrypt"))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'key_management',
                    'Encrypt',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'encryptedData',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_encrypt.pem'):
                    os.remove('tests/resources/keyfile_for_test_encrypt.pem')
                if os.path.exists('tests/resources/config_for_test_encrypt'):
                    os.remove('tests/resources/config_for_test_encrypt')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='key_management', api_name='Encrypt')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_generate_data_encryption_key(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('key_management', 'GenerateDataEncryptionKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('key_management', 'KmsCrypto', 'GenerateDataEncryptionKey')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_generate_data_encryption_key.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_generate_data_encryption_key', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_generate_data_encryption_key.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_generate_data_encryption_key'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_generate_data_encryption_key.pem'])
            config_file = 'tests/resources/config_for_test_generate_data_encryption_key'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('kms_crypto_root_group.command_name', 'kms-crypto')
    resource_group_command_name = oci_cli.cli_util.override('generated_key_group.command_name', 'generated_key')
    request_containers = cli_testing_service_client.get_requests(service_name='key_management', api_name='GenerateDataEncryptionKey')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'GenerateKeyDetails'
            details = request.pop(param_name[0].lower() + param_name[1:])
            for key in details:
                request[key] = details[key]
                override = util.variable_name_override(key)
                if override:
                    request[override] = request.pop(key)

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('key_management', 'GenerateDataEncryptionKey', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('generate_data_encryption_key.command_name', 'generate-data-encryption-key'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: key_management, GenerateDataEncryptionKey. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('generate_data_encryption_key.command_name', 'generate-data-encryption-key'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('generate_data_encryption_key.command_name', 'generate-data-encryption-key')))

            params.append('--endpoint')
            params.append(cli_testing_service_client.get_endpoint("key_management", "KmsCryptoClient", "GenerateDataEncryptionKey"))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'key_management',
                    'GenerateDataEncryptionKey',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'generatedKey',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_generate_data_encryption_key.pem'):
                    os.remove('tests/resources/keyfile_for_test_generate_data_encryption_key.pem')
                if os.path.exists('tests/resources/config_for_test_generate_data_encryption_key'):
                    os.remove('tests/resources/config_for_test_generate_data_encryption_key')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='key_management', api_name='GenerateDataEncryptionKey')
                request = request_containers[i]['request'].copy()


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = ['--config-file', config_file]

    if config_profile:
        root_params.extend(['--profile', config_profile])

    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug'] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + params, ** args)

    return result
