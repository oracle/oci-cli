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
    custom_vcr = test_config_container.create_vcr(cassette_library_dir="services/email/tests/cassettes/for_generated")

    cassette_location = 'email_{name}.yml'.format(name=request.function.__name__)
    with custom_vcr.use_cassette(cassette_location):
        yield


@pytest.mark.generated
def test_create_sender(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('email', 'CreateSender'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('email', 'Email', 'CreateSender')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_sender.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_sender', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_sender.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_sender'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_sender.pem'])
            config_file = 'tests/resources/config_for_test_create_sender'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('email_root_group.command_name', 'email')
    resource_group_command_name = oci_cli.cli_util.override('sender_group.command_name', 'sender')
    request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='CreateSender')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateSenderDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('email', 'CreateSender', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_sender.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: email, CreateSender. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_sender.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_sender.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'email',
                    'CreateSender',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'sender',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_sender.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_sender.pem')
                if os.path.exists('tests/resources/config_for_test_create_sender'):
                    os.remove('tests/resources/config_for_test_create_sender')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='CreateSender')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_suppression(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('email', 'CreateSuppression'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('email', 'Email', 'CreateSuppression')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_suppression.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_suppression', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_suppression.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_suppression'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_suppression.pem'])
            config_file = 'tests/resources/config_for_test_create_suppression'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('email_root_group.command_name', 'email')
    resource_group_command_name = oci_cli.cli_util.override('suppression_group.command_name', 'suppression')
    request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='CreateSuppression')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateSuppressionDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('email', 'CreateSuppression', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_suppression.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: email, CreateSuppression. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_suppression.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_suppression.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'email',
                    'CreateSuppression',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'suppression',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_suppression.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_suppression.pem')
                if os.path.exists('tests/resources/config_for_test_create_suppression'):
                    os.remove('tests/resources/config_for_test_create_suppression')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='CreateSuppression')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_sender(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('email', 'DeleteSender'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('email', 'Email', 'DeleteSender')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_sender.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_sender', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_sender.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_sender'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_sender.pem'])
            config_file = 'tests/resources/config_for_test_delete_sender'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('email_root_group.command_name', 'email')
    resource_group_command_name = oci_cli.cli_util.override('sender_group.command_name', 'sender')
    request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='DeleteSender')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('email', 'DeleteSender', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_sender.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: email, DeleteSender. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_sender.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_sender.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'email',
                    'DeleteSender',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteSender',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_sender.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_sender.pem')
                if os.path.exists('tests/resources/config_for_test_delete_sender'):
                    os.remove('tests/resources/config_for_test_delete_sender')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='DeleteSender')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_suppression(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('email', 'DeleteSuppression'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('email', 'Email', 'DeleteSuppression')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_suppression.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_suppression', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_suppression.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_suppression'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_suppression.pem'])
            config_file = 'tests/resources/config_for_test_delete_suppression'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('email_root_group.command_name', 'email')
    resource_group_command_name = oci_cli.cli_util.override('suppression_group.command_name', 'suppression')
    request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='DeleteSuppression')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('email', 'DeleteSuppression', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_suppression.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: email, DeleteSuppression. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_suppression.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_suppression.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'email',
                    'DeleteSuppression',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteSuppression',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_suppression.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_suppression.pem')
                if os.path.exists('tests/resources/config_for_test_delete_suppression'):
                    os.remove('tests/resources/config_for_test_delete_suppression')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='DeleteSuppression')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_sender(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('email', 'GetSender'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('email', 'Email', 'GetSender')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_sender.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_sender', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_sender.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_sender'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_sender.pem'])
            config_file = 'tests/resources/config_for_test_get_sender'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('email_root_group.command_name', 'email')
    resource_group_command_name = oci_cli.cli_util.override('sender_group.command_name', 'sender')
    request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='GetSender')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('email', 'GetSender', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_sender.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: email, GetSender. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_sender.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_sender.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'email',
                    'GetSender',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'sender',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_sender.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_sender.pem')
                if os.path.exists('tests/resources/config_for_test_get_sender'):
                    os.remove('tests/resources/config_for_test_get_sender')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='GetSender')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_suppression(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('email', 'GetSuppression'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('email', 'Email', 'GetSuppression')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_suppression.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_suppression', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_suppression.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_suppression'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_suppression.pem'])
            config_file = 'tests/resources/config_for_test_get_suppression'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('email_root_group.command_name', 'email')
    resource_group_command_name = oci_cli.cli_util.override('suppression_group.command_name', 'suppression')
    request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='GetSuppression')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('email', 'GetSuppression', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_suppression.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: email, GetSuppression. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_suppression.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_suppression.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'email',
                    'GetSuppression',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'suppression',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_suppression.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_suppression.pem')
                if os.path.exists('tests/resources/config_for_test_get_suppression'):
                    os.remove('tests/resources/config_for_test_get_suppression')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='GetSuppression')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_senders(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('email', 'ListSenders'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('email', 'Email', 'ListSenders')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_senders.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_senders', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_senders.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_senders'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_senders.pem'])
            config_file = 'tests/resources/config_for_test_list_senders'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('email_root_group.command_name', 'email')
    resource_group_command_name = oci_cli.cli_util.override('sender_group.command_name', 'sender')
    request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='ListSenders')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('email', 'ListSenders', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_senders.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: email, ListSenders. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_senders.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_senders.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'email',
                    'ListSenders',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_senders.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_senders.pem')
                if os.path.exists('tests/resources/config_for_test_list_senders'):
                    os.remove('tests/resources/config_for_test_list_senders')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='ListSenders')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_suppressions(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('email', 'ListSuppressions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('email', 'Email', 'ListSuppressions')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_suppressions.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_suppressions', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_suppressions.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_suppressions'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_suppressions.pem'])
            config_file = 'tests/resources/config_for_test_list_suppressions'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('email_root_group.command_name', 'email')
    resource_group_command_name = oci_cli.cli_util.override('suppression_group.command_name', 'suppression')
    request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='ListSuppressions')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('email', 'ListSuppressions', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_suppressions.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: email, ListSuppressions. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_suppressions.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_suppressions.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'email',
                    'ListSuppressions',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_suppressions.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_suppressions.pem')
                if os.path.exists('tests/resources/config_for_test_list_suppressions'):
                    os.remove('tests/resources/config_for_test_list_suppressions')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='ListSuppressions')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_sender(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('email', 'UpdateSender'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('email', 'Email', 'UpdateSender')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_sender.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_sender', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_sender.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_sender'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_sender.pem'])
            config_file = 'tests/resources/config_for_test_update_sender'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('email_root_group.command_name', 'email')
    resource_group_command_name = oci_cli.cli_util.override('sender_group.command_name', 'sender')
    request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='UpdateSender')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateSenderDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('email', 'UpdateSender', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_sender.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: email, UpdateSender. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_sender.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_sender.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'email',
                    'UpdateSender',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'sender',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_sender.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_sender.pem')
                if os.path.exists('tests/resources/config_for_test_update_sender'):
                    os.remove('tests/resources/config_for_test_update_sender')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='email', api_name='UpdateSender')
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
