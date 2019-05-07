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
    custom_vcr = test_config_container.create_vcr(cassette_library_dir="services/load_balancer/tests/cassettes/for_generated")

    cassette_location = 'load_balancer_{name}.yml'.format(name=request.function.__name__)
    with custom_vcr.use_cassette(cassette_location):
        yield


@pytest.mark.generated
def test_create_backend(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'CreateBackend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'CreateBackend')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_backend.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_backend', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_backend.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_backend'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_backend.pem'])
            config_file = 'tests/resources/config_for_test_create_backend'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('backend_group.command_name', 'backend')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreateBackend')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateBackendDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'CreateBackend', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_backend.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, CreateBackend. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_backend.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_backend.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'CreateBackend',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'createBackend',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_backend.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_backend.pem')
                if os.path.exists('tests/resources/config_for_test_create_backend'):
                    os.remove('tests/resources/config_for_test_create_backend')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreateBackend')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_backend_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'CreateBackendSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'CreateBackendSet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_backend_set.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_backend_set', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_backend_set.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_backend_set'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_backend_set.pem'])
            config_file = 'tests/resources/config_for_test_create_backend_set'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('backend_set_group.command_name', 'backend_set')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreateBackendSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateBackendSetDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'CreateBackendSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_backend_set.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, CreateBackendSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_backend_set.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_backend_set.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'CreateBackendSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'createBackendSet',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_backend_set.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_backend_set.pem')
                if os.path.exists('tests/resources/config_for_test_create_backend_set'):
                    os.remove('tests/resources/config_for_test_create_backend_set')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreateBackendSet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_certificate(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'CreateCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'CreateCertificate')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_certificate.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_certificate', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_certificate.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_certificate'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_certificate.pem'])
            config_file = 'tests/resources/config_for_test_create_certificate'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('certificate_group.command_name', 'certificate')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreateCertificate')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateCertificateDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'CreateCertificate', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_certificate.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, CreateCertificate. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_certificate.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_certificate.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'CreateCertificate',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'createCertificate',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_certificate.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_certificate.pem')
                if os.path.exists('tests/resources/config_for_test_create_certificate'):
                    os.remove('tests/resources/config_for_test_create_certificate')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreateCertificate')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_hostname(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'CreateHostname'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'CreateHostname')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_hostname.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_hostname', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_hostname.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_hostname'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_hostname.pem'])
            config_file = 'tests/resources/config_for_test_create_hostname'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('hostname_group.command_name', 'hostname')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreateHostname')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateHostnameDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'CreateHostname', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_hostname.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, CreateHostname. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_hostname.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_hostname.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'CreateHostname',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'createHostname',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_hostname.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_hostname.pem')
                if os.path.exists('tests/resources/config_for_test_create_hostname'):
                    os.remove('tests/resources/config_for_test_create_hostname')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreateHostname')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_listener(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'CreateListener'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'CreateListener')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_listener.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_listener', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_listener.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_listener'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_listener.pem'])
            config_file = 'tests/resources/config_for_test_create_listener'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('listener_group.command_name', 'listener')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreateListener')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateListenerDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'CreateListener', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_listener.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, CreateListener. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_listener.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_listener.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'CreateListener',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'createListener',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_listener.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_listener.pem')
                if os.path.exists('tests/resources/config_for_test_create_listener'):
                    os.remove('tests/resources/config_for_test_create_listener')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreateListener')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_load_balancer(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'CreateLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'CreateLoadBalancer')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_load_balancer.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_load_balancer', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_load_balancer.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_load_balancer'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_load_balancer.pem'])
            config_file = 'tests/resources/config_for_test_create_load_balancer'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('load_balancer_group.command_name', 'load_balancer')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreateLoadBalancer')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateLoadBalancerDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'CreateLoadBalancer', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_load_balancer.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, CreateLoadBalancer. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_load_balancer.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_load_balancer.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'CreateLoadBalancer',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'createLoadBalancer',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_load_balancer.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_load_balancer.pem')
                if os.path.exists('tests/resources/config_for_test_create_load_balancer'):
                    os.remove('tests/resources/config_for_test_create_load_balancer')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreateLoadBalancer')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_path_route_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'CreatePathRouteSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'CreatePathRouteSet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_path_route_set.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_path_route_set', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_path_route_set.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_path_route_set'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_path_route_set.pem'])
            config_file = 'tests/resources/config_for_test_create_path_route_set'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('path_route_set_group.command_name', 'path_route_set')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreatePathRouteSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreatePathRouteSetDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'CreatePathRouteSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_path_route_set.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, CreatePathRouteSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_path_route_set.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_path_route_set.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'CreatePathRouteSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'createPathRouteSet',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_path_route_set.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_path_route_set.pem')
                if os.path.exists('tests/resources/config_for_test_create_path_route_set'):
                    os.remove('tests/resources/config_for_test_create_path_route_set')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreatePathRouteSet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_rule_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'CreateRuleSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'CreateRuleSet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_rule_set.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_rule_set', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_rule_set.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_rule_set'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_rule_set.pem'])
            config_file = 'tests/resources/config_for_test_create_rule_set'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('rule_set_group.command_name', 'rule_set')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreateRuleSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateRuleSetDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'CreateRuleSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_rule_set.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, CreateRuleSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_rule_set.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_rule_set.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'CreateRuleSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'createRuleSet',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_rule_set.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_rule_set.pem')
                if os.path.exists('tests/resources/config_for_test_create_rule_set'):
                    os.remove('tests/resources/config_for_test_create_rule_set')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='CreateRuleSet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_backend(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'DeleteBackend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'DeleteBackend')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_backend.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_backend', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_backend.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_backend'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_backend.pem'])
            config_file = 'tests/resources/config_for_test_delete_backend'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('backend_group.command_name', 'backend')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteBackend')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'DeleteBackend', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_backend.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, DeleteBackend. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_backend.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_backend.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'DeleteBackend',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteBackend',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_backend.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_backend.pem')
                if os.path.exists('tests/resources/config_for_test_delete_backend'):
                    os.remove('tests/resources/config_for_test_delete_backend')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteBackend')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_backend_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'DeleteBackendSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'DeleteBackendSet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_backend_set.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_backend_set', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_backend_set.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_backend_set'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_backend_set.pem'])
            config_file = 'tests/resources/config_for_test_delete_backend_set'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('backend_set_group.command_name', 'backend_set')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteBackendSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'DeleteBackendSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_backend_set.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, DeleteBackendSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_backend_set.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_backend_set.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'DeleteBackendSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteBackendSet',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_backend_set.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_backend_set.pem')
                if os.path.exists('tests/resources/config_for_test_delete_backend_set'):
                    os.remove('tests/resources/config_for_test_delete_backend_set')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteBackendSet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_certificate(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'DeleteCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'DeleteCertificate')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_certificate.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_certificate', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_certificate.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_certificate'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_certificate.pem'])
            config_file = 'tests/resources/config_for_test_delete_certificate'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('certificate_group.command_name', 'certificate')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteCertificate')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'DeleteCertificate', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_certificate.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, DeleteCertificate. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_certificate.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_certificate.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'DeleteCertificate',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteCertificate',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_certificate.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_certificate.pem')
                if os.path.exists('tests/resources/config_for_test_delete_certificate'):
                    os.remove('tests/resources/config_for_test_delete_certificate')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteCertificate')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_hostname(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'DeleteHostname'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'DeleteHostname')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_hostname.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_hostname', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_hostname.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_hostname'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_hostname.pem'])
            config_file = 'tests/resources/config_for_test_delete_hostname'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('hostname_group.command_name', 'hostname')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteHostname')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'DeleteHostname', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_hostname.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, DeleteHostname. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_hostname.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_hostname.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'DeleteHostname',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteHostname',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_hostname.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_hostname.pem')
                if os.path.exists('tests/resources/config_for_test_delete_hostname'):
                    os.remove('tests/resources/config_for_test_delete_hostname')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteHostname')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_listener(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'DeleteListener'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'DeleteListener')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_listener.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_listener', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_listener.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_listener'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_listener.pem'])
            config_file = 'tests/resources/config_for_test_delete_listener'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('listener_group.command_name', 'listener')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteListener')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'DeleteListener', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_listener.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, DeleteListener. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_listener.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_listener.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'DeleteListener',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteListener',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_listener.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_listener.pem')
                if os.path.exists('tests/resources/config_for_test_delete_listener'):
                    os.remove('tests/resources/config_for_test_delete_listener')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteListener')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_load_balancer(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'DeleteLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'DeleteLoadBalancer')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_load_balancer.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_load_balancer', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_load_balancer.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_load_balancer'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_load_balancer.pem'])
            config_file = 'tests/resources/config_for_test_delete_load_balancer'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('load_balancer_group.command_name', 'load_balancer')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteLoadBalancer')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'DeleteLoadBalancer', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_load_balancer.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, DeleteLoadBalancer. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_load_balancer.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_load_balancer.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'DeleteLoadBalancer',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteLoadBalancer',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_load_balancer.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_load_balancer.pem')
                if os.path.exists('tests/resources/config_for_test_delete_load_balancer'):
                    os.remove('tests/resources/config_for_test_delete_load_balancer')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteLoadBalancer')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_path_route_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'DeletePathRouteSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'DeletePathRouteSet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_path_route_set.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_path_route_set', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_path_route_set.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_path_route_set'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_path_route_set.pem'])
            config_file = 'tests/resources/config_for_test_delete_path_route_set'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('path_route_set_group.command_name', 'path_route_set')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeletePathRouteSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'DeletePathRouteSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_path_route_set.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, DeletePathRouteSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_path_route_set.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_path_route_set.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'DeletePathRouteSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deletePathRouteSet',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_path_route_set.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_path_route_set.pem')
                if os.path.exists('tests/resources/config_for_test_delete_path_route_set'):
                    os.remove('tests/resources/config_for_test_delete_path_route_set')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeletePathRouteSet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_rule_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'DeleteRuleSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'DeleteRuleSet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_rule_set.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_rule_set', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_rule_set.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_rule_set'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_rule_set.pem'])
            config_file = 'tests/resources/config_for_test_delete_rule_set'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('rule_set_group.command_name', 'rule_set')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteRuleSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'DeleteRuleSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_rule_set.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, DeleteRuleSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_rule_set.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_rule_set.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'DeleteRuleSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteRuleSet',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_rule_set.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_rule_set.pem')
                if os.path.exists('tests/resources/config_for_test_delete_rule_set'):
                    os.remove('tests/resources/config_for_test_delete_rule_set')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='DeleteRuleSet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_backend(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'GetBackend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'GetBackend')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_backend.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_backend', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_backend.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_backend'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_backend.pem'])
            config_file = 'tests/resources/config_for_test_get_backend'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('backend_group.command_name', 'backend')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetBackend')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'GetBackend', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_backend.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, GetBackend. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_backend.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_backend.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'GetBackend',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'backend',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_backend.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_backend.pem')
                if os.path.exists('tests/resources/config_for_test_get_backend'):
                    os.remove('tests/resources/config_for_test_get_backend')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetBackend')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_backend_health(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'GetBackendHealth'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'GetBackendHealth')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_backend_health.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_backend_health', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_backend_health.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_backend_health'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_backend_health.pem'])
            config_file = 'tests/resources/config_for_test_get_backend_health'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('backend_health_group.command_name', 'backend_health')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetBackendHealth')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'GetBackendHealth', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_backend_health.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, GetBackendHealth. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_backend_health.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_backend_health.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'GetBackendHealth',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'backendHealth',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_backend_health.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_backend_health.pem')
                if os.path.exists('tests/resources/config_for_test_get_backend_health'):
                    os.remove('tests/resources/config_for_test_get_backend_health')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetBackendHealth')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_backend_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'GetBackendSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'GetBackendSet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_backend_set.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_backend_set', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_backend_set.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_backend_set'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_backend_set.pem'])
            config_file = 'tests/resources/config_for_test_get_backend_set'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('backend_set_group.command_name', 'backend_set')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetBackendSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'GetBackendSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_backend_set.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, GetBackendSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_backend_set.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_backend_set.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'GetBackendSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'backendSet',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_backend_set.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_backend_set.pem')
                if os.path.exists('tests/resources/config_for_test_get_backend_set'):
                    os.remove('tests/resources/config_for_test_get_backend_set')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetBackendSet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_backend_set_health(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'GetBackendSetHealth'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'GetBackendSetHealth')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_backend_set_health.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_backend_set_health', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_backend_set_health.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_backend_set_health'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_backend_set_health.pem'])
            config_file = 'tests/resources/config_for_test_get_backend_set_health'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('backend_set_health_group.command_name', 'backend_set_health')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetBackendSetHealth')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'GetBackendSetHealth', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_backend_set_health.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, GetBackendSetHealth. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_backend_set_health.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_backend_set_health.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'GetBackendSetHealth',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'backendSetHealth',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_backend_set_health.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_backend_set_health.pem')
                if os.path.exists('tests/resources/config_for_test_get_backend_set_health'):
                    os.remove('tests/resources/config_for_test_get_backend_set_health')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetBackendSetHealth')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_health_checker(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'GetHealthChecker'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'GetHealthChecker')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_health_checker.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_health_checker', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_health_checker.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_health_checker'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_health_checker.pem'])
            config_file = 'tests/resources/config_for_test_get_health_checker'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('health_checker_group.command_name', 'health_checker')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetHealthChecker')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'GetHealthChecker', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_health_checker.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, GetHealthChecker. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_health_checker.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_health_checker.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'GetHealthChecker',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'healthChecker',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_health_checker.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_health_checker.pem')
                if os.path.exists('tests/resources/config_for_test_get_health_checker'):
                    os.remove('tests/resources/config_for_test_get_health_checker')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetHealthChecker')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_hostname(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'GetHostname'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'GetHostname')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_hostname.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_hostname', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_hostname.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_hostname'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_hostname.pem'])
            config_file = 'tests/resources/config_for_test_get_hostname'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('hostname_group.command_name', 'hostname')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetHostname')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'GetHostname', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_hostname.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, GetHostname. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_hostname.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_hostname.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'GetHostname',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'hostname',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_hostname.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_hostname.pem')
                if os.path.exists('tests/resources/config_for_test_get_hostname'):
                    os.remove('tests/resources/config_for_test_get_hostname')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetHostname')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_load_balancer(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'GetLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'GetLoadBalancer')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_load_balancer.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_load_balancer', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_load_balancer.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_load_balancer'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_load_balancer.pem'])
            config_file = 'tests/resources/config_for_test_get_load_balancer'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('load_balancer_group.command_name', 'load_balancer')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetLoadBalancer')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'GetLoadBalancer', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_load_balancer.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, GetLoadBalancer. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_load_balancer.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_load_balancer.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'GetLoadBalancer',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'loadBalancer',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_load_balancer.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_load_balancer.pem')
                if os.path.exists('tests/resources/config_for_test_get_load_balancer'):
                    os.remove('tests/resources/config_for_test_get_load_balancer')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetLoadBalancer')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_load_balancer_health(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'GetLoadBalancerHealth'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'GetLoadBalancerHealth')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_load_balancer_health.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_load_balancer_health', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_load_balancer_health.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_load_balancer_health'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_load_balancer_health.pem'])
            config_file = 'tests/resources/config_for_test_get_load_balancer_health'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('load_balancer_health_group.command_name', 'load_balancer_health')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetLoadBalancerHealth')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'GetLoadBalancerHealth', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_load_balancer_health.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, GetLoadBalancerHealth. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_load_balancer_health.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_load_balancer_health.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'GetLoadBalancerHealth',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'loadBalancerHealth',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_load_balancer_health.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_load_balancer_health.pem')
                if os.path.exists('tests/resources/config_for_test_get_load_balancer_health'):
                    os.remove('tests/resources/config_for_test_get_load_balancer_health')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetLoadBalancerHealth')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_path_route_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'GetPathRouteSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'GetPathRouteSet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_path_route_set.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_path_route_set', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_path_route_set.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_path_route_set'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_path_route_set.pem'])
            config_file = 'tests/resources/config_for_test_get_path_route_set'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('path_route_set_group.command_name', 'path_route_set')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetPathRouteSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'GetPathRouteSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_path_route_set.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, GetPathRouteSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_path_route_set.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_path_route_set.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'GetPathRouteSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'pathRouteSet',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_path_route_set.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_path_route_set.pem')
                if os.path.exists('tests/resources/config_for_test_get_path_route_set'):
                    os.remove('tests/resources/config_for_test_get_path_route_set')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetPathRouteSet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_rule_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'GetRuleSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'GetRuleSet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_rule_set.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_rule_set', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_rule_set.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_rule_set'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_rule_set.pem'])
            config_file = 'tests/resources/config_for_test_get_rule_set'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('rule_set_group.command_name', 'rule_set')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetRuleSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'GetRuleSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_rule_set.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, GetRuleSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_rule_set.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_rule_set.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'GetRuleSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'ruleSet',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_rule_set.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_rule_set.pem')
                if os.path.exists('tests/resources/config_for_test_get_rule_set'):
                    os.remove('tests/resources/config_for_test_get_rule_set')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetRuleSet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_work_request(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'GetWorkRequest')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_work_request.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_work_request', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_work_request.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_work_request'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_work_request.pem'])
            config_file = 'tests/resources/config_for_test_get_work_request'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('work_request_group.command_name', 'work_request')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetWorkRequest')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'GetWorkRequest', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_work_request.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, GetWorkRequest. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_work_request.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_work_request.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'GetWorkRequest',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'workRequest',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_work_request.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_work_request.pem')
                if os.path.exists('tests/resources/config_for_test_get_work_request'):
                    os.remove('tests/resources/config_for_test_get_work_request')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='GetWorkRequest')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_backend_sets(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'ListBackendSets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'ListBackendSets')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_backend_sets.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_backend_sets', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_backend_sets.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_backend_sets'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_backend_sets.pem'])
            config_file = 'tests/resources/config_for_test_list_backend_sets'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('backend_set_group.command_name', 'backend_set')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListBackendSets')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'ListBackendSets', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_backend_sets.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, ListBackendSets. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_backend_sets.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_backend_sets.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'ListBackendSets',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_backend_sets.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_backend_sets.pem')
                if os.path.exists('tests/resources/config_for_test_list_backend_sets'):
                    os.remove('tests/resources/config_for_test_list_backend_sets')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListBackendSets')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_backends(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'ListBackends'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'ListBackends')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_backends.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_backends', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_backends.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_backends'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_backends.pem'])
            config_file = 'tests/resources/config_for_test_list_backends'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('backend_group.command_name', 'backend')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListBackends')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'ListBackends', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_backends.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, ListBackends. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_backends.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_backends.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'ListBackends',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_backends.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_backends.pem')
                if os.path.exists('tests/resources/config_for_test_list_backends'):
                    os.remove('tests/resources/config_for_test_list_backends')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListBackends')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_certificates(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'ListCertificates'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'ListCertificates')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_certificates.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_certificates', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_certificates.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_certificates'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_certificates.pem'])
            config_file = 'tests/resources/config_for_test_list_certificates'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('certificate_group.command_name', 'certificate')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListCertificates')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'ListCertificates', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_certificates.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, ListCertificates. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_certificates.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_certificates.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'ListCertificates',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_certificates.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_certificates.pem')
                if os.path.exists('tests/resources/config_for_test_list_certificates'):
                    os.remove('tests/resources/config_for_test_list_certificates')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListCertificates')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_hostnames(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'ListHostnames'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'ListHostnames')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_hostnames.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_hostnames', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_hostnames.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_hostnames'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_hostnames.pem'])
            config_file = 'tests/resources/config_for_test_list_hostnames'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('hostname_group.command_name', 'hostname')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListHostnames')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'ListHostnames', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_hostnames.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, ListHostnames. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_hostnames.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_hostnames.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'ListHostnames',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_hostnames.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_hostnames.pem')
                if os.path.exists('tests/resources/config_for_test_list_hostnames'):
                    os.remove('tests/resources/config_for_test_list_hostnames')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListHostnames')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_load_balancer_healths(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'ListLoadBalancerHealths'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'ListLoadBalancerHealths')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_load_balancer_healths.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_load_balancer_healths', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_load_balancer_healths.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_load_balancer_healths'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_load_balancer_healths.pem'])
            config_file = 'tests/resources/config_for_test_list_load_balancer_healths'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('load_balancer_health_group.command_name', 'load_balancer_health')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListLoadBalancerHealths')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'ListLoadBalancerHealths', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_load_balancer_healths.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, ListLoadBalancerHealths. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_load_balancer_healths.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_load_balancer_healths.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'ListLoadBalancerHealths',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_load_balancer_healths.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_load_balancer_healths.pem')
                if os.path.exists('tests/resources/config_for_test_list_load_balancer_healths'):
                    os.remove('tests/resources/config_for_test_list_load_balancer_healths')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListLoadBalancerHealths')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_load_balancers(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'ListLoadBalancers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'ListLoadBalancers')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_load_balancers.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_load_balancers', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_load_balancers.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_load_balancers'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_load_balancers.pem'])
            config_file = 'tests/resources/config_for_test_list_load_balancers'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('load_balancer_group.command_name', 'load_balancer')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListLoadBalancers')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'ListLoadBalancers', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_load_balancers.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, ListLoadBalancers. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_load_balancers.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_load_balancers.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'ListLoadBalancers',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_load_balancers.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_load_balancers.pem')
                if os.path.exists('tests/resources/config_for_test_list_load_balancers'):
                    os.remove('tests/resources/config_for_test_list_load_balancers')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListLoadBalancers')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_path_route_sets(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'ListPathRouteSets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'ListPathRouteSets')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_path_route_sets.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_path_route_sets', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_path_route_sets.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_path_route_sets'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_path_route_sets.pem'])
            config_file = 'tests/resources/config_for_test_list_path_route_sets'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('path_route_set_group.command_name', 'path_route_set')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListPathRouteSets')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'ListPathRouteSets', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_path_route_sets.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, ListPathRouteSets. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_path_route_sets.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_path_route_sets.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'ListPathRouteSets',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_path_route_sets.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_path_route_sets.pem')
                if os.path.exists('tests/resources/config_for_test_list_path_route_sets'):
                    os.remove('tests/resources/config_for_test_list_path_route_sets')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListPathRouteSets')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_policies(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'ListPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'ListPolicies')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_policies.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_policies', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_policies.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_policies'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_policies.pem'])
            config_file = 'tests/resources/config_for_test_list_policies'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('load_balancer_policy_group.command_name', 'load_balancer_policy')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListPolicies')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'ListPolicies', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_policies.command_name', 'list-policies')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, ListPolicies. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_policies.command_name', 'list-policies'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_policies.command_name', 'list-policies')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'ListPolicies',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_policies.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_policies.pem')
                if os.path.exists('tests/resources/config_for_test_list_policies'):
                    os.remove('tests/resources/config_for_test_list_policies')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListPolicies')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_protocols(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'ListProtocols'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'ListProtocols')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_protocols.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_protocols', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_protocols.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_protocols'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_protocols.pem'])
            config_file = 'tests/resources/config_for_test_list_protocols'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('load_balancer_protocol_group.command_name', 'load_balancer_protocol')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListProtocols')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'ListProtocols', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_protocols.command_name', 'list-protocols')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, ListProtocols. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_protocols.command_name', 'list-protocols'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_protocols.command_name', 'list-protocols')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'ListProtocols',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_protocols.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_protocols.pem')
                if os.path.exists('tests/resources/config_for_test_list_protocols'):
                    os.remove('tests/resources/config_for_test_list_protocols')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListProtocols')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_rule_sets(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'ListRuleSets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'ListRuleSets')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_rule_sets.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_rule_sets', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_rule_sets.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_rule_sets'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_rule_sets.pem'])
            config_file = 'tests/resources/config_for_test_list_rule_sets'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('rule_set_group.command_name', 'rule_set')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListRuleSets')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'ListRuleSets', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_rule_sets.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, ListRuleSets. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_rule_sets.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_rule_sets.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'ListRuleSets',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_rule_sets.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_rule_sets.pem')
                if os.path.exists('tests/resources/config_for_test_list_rule_sets'):
                    os.remove('tests/resources/config_for_test_list_rule_sets')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListRuleSets')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_shapes(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'ListShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'ListShapes')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_shapes.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_shapes', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_shapes.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_shapes'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_shapes.pem'])
            config_file = 'tests/resources/config_for_test_list_shapes'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('load_balancer_shape_group.command_name', 'load_balancer_shape')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListShapes')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'ListShapes', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_shapes.command_name', 'list-shapes')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, ListShapes. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_shapes.command_name', 'list-shapes'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_shapes.command_name', 'list-shapes')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'ListShapes',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_shapes.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_shapes.pem')
                if os.path.exists('tests/resources/config_for_test_list_shapes'):
                    os.remove('tests/resources/config_for_test_list_shapes')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListShapes')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_work_requests(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'ListWorkRequests')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_work_requests.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_work_requests', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_work_requests.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_work_requests'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_work_requests.pem'])
            config_file = 'tests/resources/config_for_test_list_work_requests'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('work_request_group.command_name', 'work_request')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListWorkRequests')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'ListWorkRequests', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_work_requests.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, ListWorkRequests. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_work_requests.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_work_requests.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'ListWorkRequests',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_work_requests.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_work_requests.pem')
                if os.path.exists('tests/resources/config_for_test_list_work_requests'):
                    os.remove('tests/resources/config_for_test_list_work_requests')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='ListWorkRequests')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_backend(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'UpdateBackend'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'UpdateBackend')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_backend.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_backend', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_backend.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_backend'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_backend.pem'])
            config_file = 'tests/resources/config_for_test_update_backend'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('backend_group.command_name', 'backend')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateBackend')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateBackendDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'UpdateBackend', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_backend.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, UpdateBackend. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_backend.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_backend.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'UpdateBackend',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateBackend',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_backend.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_backend.pem')
                if os.path.exists('tests/resources/config_for_test_update_backend'):
                    os.remove('tests/resources/config_for_test_update_backend')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateBackend')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_backend_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'UpdateBackendSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'UpdateBackendSet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_backend_set.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_backend_set', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_backend_set.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_backend_set'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_backend_set.pem'])
            config_file = 'tests/resources/config_for_test_update_backend_set'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('backend_set_group.command_name', 'backend_set')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateBackendSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateBackendSetDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'UpdateBackendSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_backend_set.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, UpdateBackendSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_backend_set.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_backend_set.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'UpdateBackendSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateBackendSet',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_backend_set.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_backend_set.pem')
                if os.path.exists('tests/resources/config_for_test_update_backend_set'):
                    os.remove('tests/resources/config_for_test_update_backend_set')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateBackendSet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_health_checker(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'UpdateHealthChecker'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'UpdateHealthChecker')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_health_checker.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_health_checker', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_health_checker.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_health_checker'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_health_checker.pem'])
            config_file = 'tests/resources/config_for_test_update_health_checker'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('health_checker_group.command_name', 'health_checker')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateHealthChecker')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'HealthChecker'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'UpdateHealthChecker', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_health_checker.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, UpdateHealthChecker. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_health_checker.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_health_checker.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'UpdateHealthChecker',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateHealthChecker',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_health_checker.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_health_checker.pem')
                if os.path.exists('tests/resources/config_for_test_update_health_checker'):
                    os.remove('tests/resources/config_for_test_update_health_checker')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateHealthChecker')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_hostname(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'UpdateHostname'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'UpdateHostname')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_hostname.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_hostname', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_hostname.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_hostname'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_hostname.pem'])
            config_file = 'tests/resources/config_for_test_update_hostname'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('hostname_group.command_name', 'hostname')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateHostname')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateHostnameDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'UpdateHostname', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_hostname.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, UpdateHostname. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_hostname.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_hostname.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'UpdateHostname',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateHostname',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_hostname.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_hostname.pem')
                if os.path.exists('tests/resources/config_for_test_update_hostname'):
                    os.remove('tests/resources/config_for_test_update_hostname')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateHostname')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_listener(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'UpdateListener'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'UpdateListener')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_listener.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_listener', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_listener.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_listener'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_listener.pem'])
            config_file = 'tests/resources/config_for_test_update_listener'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('listener_group.command_name', 'listener')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateListener')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateListenerDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'UpdateListener', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_listener.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, UpdateListener. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_listener.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_listener.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'UpdateListener',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateListener',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_listener.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_listener.pem')
                if os.path.exists('tests/resources/config_for_test_update_listener'):
                    os.remove('tests/resources/config_for_test_update_listener')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateListener')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_load_balancer(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'UpdateLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'UpdateLoadBalancer')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_load_balancer.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_load_balancer', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_load_balancer.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_load_balancer'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_load_balancer.pem'])
            config_file = 'tests/resources/config_for_test_update_load_balancer'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('load_balancer_group.command_name', 'load_balancer')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateLoadBalancer')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateLoadBalancerDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'UpdateLoadBalancer', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_load_balancer.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, UpdateLoadBalancer. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_load_balancer.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_load_balancer.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'UpdateLoadBalancer',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateLoadBalancer',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_load_balancer.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_load_balancer.pem')
                if os.path.exists('tests/resources/config_for_test_update_load_balancer'):
                    os.remove('tests/resources/config_for_test_update_load_balancer')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateLoadBalancer')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_path_route_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'UpdatePathRouteSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'UpdatePathRouteSet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_path_route_set.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_path_route_set', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_path_route_set.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_path_route_set'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_path_route_set.pem'])
            config_file = 'tests/resources/config_for_test_update_path_route_set'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('path_route_set_group.command_name', 'path_route_set')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdatePathRouteSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdatePathRouteSetDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'UpdatePathRouteSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_path_route_set.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, UpdatePathRouteSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_path_route_set.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_path_route_set.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'UpdatePathRouteSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updatePathRouteSet',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_path_route_set.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_path_route_set.pem')
                if os.path.exists('tests/resources/config_for_test_update_path_route_set'):
                    os.remove('tests/resources/config_for_test_update_path_route_set')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdatePathRouteSet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_rule_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('load_balancer', 'UpdateRuleSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('load_balancer', 'LoadBalancer', 'UpdateRuleSet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_rule_set.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_rule_set', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_rule_set.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_rule_set'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_rule_set.pem'])
            config_file = 'tests/resources/config_for_test_update_rule_set'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('lb_root_group.command_name', 'lb')
    resource_group_command_name = oci_cli.cli_util.override('rule_set_group.command_name', 'rule_set')
    request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateRuleSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateRuleSetDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('load_balancer', 'UpdateRuleSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_rule_set.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: load_balancer, UpdateRuleSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_rule_set.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_rule_set.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'load_balancer',
                    'UpdateRuleSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateRuleSet',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_rule_set.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_rule_set.pem')
                if os.path.exists('tests/resources/config_for_test_update_rule_set'):
                    os.remove('tests/resources/config_for_test_update_rule_set')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='load_balancer', api_name='UpdateRuleSet')
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
