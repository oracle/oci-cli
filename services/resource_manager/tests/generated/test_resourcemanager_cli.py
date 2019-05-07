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
    custom_vcr = test_config_container.create_vcr(cassette_library_dir="services/resource_manager/tests/cassettes/for_generated")

    cassette_location = 'resource_manager_{name}.yml'.format(name=request.function.__name__)
    with custom_vcr.use_cassette(cassette_location):
        yield


@pytest.mark.generated
def test_cancel_job(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('resource_manager', 'CancelJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('resource_manager', 'ResourceManager', 'CancelJob')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_cancel_job.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_cancel_job', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_cancel_job.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_cancel_job'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_cancel_job.pem'])
            config_file = 'tests/resources/config_for_test_cancel_job'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('resource_manager_root_group.command_name', 'resource-manager')
    resource_group_command_name = oci_cli.cli_util.override('job_group.command_name', 'job')
    request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='CancelJob')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('resource_manager', 'CancelJob', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('cancel_job.command_name', 'cancel')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: resource_manager, CancelJob. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('cancel_job.command_name', 'cancel'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('cancel_job.command_name', 'cancel')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'resource_manager',
                    'CancelJob',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'cancelJob',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_cancel_job.pem'):
                    os.remove('tests/resources/keyfile_for_test_cancel_job.pem')
                if os.path.exists('tests/resources/config_for_test_cancel_job'):
                    os.remove('tests/resources/config_for_test_cancel_job')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='CancelJob')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_job(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('resource_manager', 'CreateJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('resource_manager', 'ResourceManager', 'CreateJob')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_job.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_job', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_job.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_job'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_job.pem'])
            config_file = 'tests/resources/config_for_test_create_job'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('resource_manager_root_group.command_name', 'resource-manager')
    resource_group_command_name = oci_cli.cli_util.override('job_group.command_name', 'job')
    request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='CreateJob')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateJobDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('resource_manager', 'CreateJob', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_job.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: resource_manager, CreateJob. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_job.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_job.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'resource_manager',
                    'CreateJob',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'job',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_job.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_job.pem')
                if os.path.exists('tests/resources/config_for_test_create_job'):
                    os.remove('tests/resources/config_for_test_create_job')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='CreateJob')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_stack(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('resource_manager', 'CreateStack'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('resource_manager', 'ResourceManager', 'CreateStack')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_stack.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_stack', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_stack.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_stack'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_stack.pem'])
            config_file = 'tests/resources/config_for_test_create_stack'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('resource_manager_root_group.command_name', 'resource-manager')
    resource_group_command_name = oci_cli.cli_util.override('stack_group.command_name', 'stack')
    request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='CreateStack')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateStackDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('resource_manager', 'CreateStack', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_stack.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: resource_manager, CreateStack. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_stack.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_stack.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'resource_manager',
                    'CreateStack',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'stack',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_stack.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_stack.pem')
                if os.path.exists('tests/resources/config_for_test_create_stack'):
                    os.remove('tests/resources/config_for_test_create_stack')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='CreateStack')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_stack(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('resource_manager', 'DeleteStack'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('resource_manager', 'ResourceManager', 'DeleteStack')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_stack.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_stack', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_stack.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_stack'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_stack.pem'])
            config_file = 'tests/resources/config_for_test_delete_stack'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('resource_manager_root_group.command_name', 'resource-manager')
    resource_group_command_name = oci_cli.cli_util.override('stack_group.command_name', 'stack')
    request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='DeleteStack')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('resource_manager', 'DeleteStack', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_stack.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: resource_manager, DeleteStack. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_stack.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_stack.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'resource_manager',
                    'DeleteStack',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteStack',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_stack.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_stack.pem')
                if os.path.exists('tests/resources/config_for_test_delete_stack'):
                    os.remove('tests/resources/config_for_test_delete_stack')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='DeleteStack')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_job(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('resource_manager', 'GetJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('resource_manager', 'ResourceManager', 'GetJob')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_job.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_job', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_job.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_job'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_job.pem'])
            config_file = 'tests/resources/config_for_test_get_job'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('resource_manager_root_group.command_name', 'resource-manager')
    resource_group_command_name = oci_cli.cli_util.override('job_group.command_name', 'job')
    request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='GetJob')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('resource_manager', 'GetJob', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_job.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: resource_manager, GetJob. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_job.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_job.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'resource_manager',
                    'GetJob',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'job',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_job.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_job.pem')
                if os.path.exists('tests/resources/config_for_test_get_job'):
                    os.remove('tests/resources/config_for_test_get_job')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='GetJob')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_job_logs(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('resource_manager', 'GetJobLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('resource_manager', 'ResourceManager', 'GetJobLogs')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_job_logs.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_job_logs', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_job_logs.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_job_logs'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_job_logs.pem'])
            config_file = 'tests/resources/config_for_test_get_job_logs'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('resource_manager_root_group.command_name', 'resource-manager')
    resource_group_command_name = oci_cli.cli_util.override('job_group.command_name', 'job')
    request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='GetJobLogs')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('resource_manager', 'GetJobLogs', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_job_logs.command_name', 'get-job-logs')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: resource_manager, GetJobLogs. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_job_logs.command_name', 'get-job-logs'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_job_logs.command_name', 'get-job-logs')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'resource_manager',
                    'GetJobLogs',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_job_logs.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_job_logs.pem')
                if os.path.exists('tests/resources/config_for_test_get_job_logs'):
                    os.remove('tests/resources/config_for_test_get_job_logs')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='GetJobLogs')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_job_logs_content(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('resource_manager', 'GetJobLogsContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('resource_manager', 'ResourceManager', 'GetJobLogsContent')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_job_logs_content.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_job_logs_content', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_job_logs_content.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_job_logs_content'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_job_logs_content.pem'])
            config_file = 'tests/resources/config_for_test_get_job_logs_content'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('resource_manager_root_group.command_name', 'resource-manager')
    resource_group_command_name = oci_cli.cli_util.override('job_group.command_name', 'job')
    request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='GetJobLogsContent')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('resource_manager', 'GetJobLogsContent', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_job_logs_content.command_name', 'get-job-logs-content')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: resource_manager, GetJobLogsContent. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_job_logs_content.command_name', 'get-job-logs-content'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_job_logs_content.command_name', 'get-job-logs-content')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'resource_manager',
                    'GetJobLogsContent',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'string',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_job_logs_content.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_job_logs_content.pem')
                if os.path.exists('tests/resources/config_for_test_get_job_logs_content'):
                    os.remove('tests/resources/config_for_test_get_job_logs_content')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='GetJobLogsContent')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_job_tf_config(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('resource_manager', 'GetJobTfConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('resource_manager', 'ResourceManager', 'GetJobTfConfig')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_job_tf_config.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_job_tf_config', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_job_tf_config.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_job_tf_config'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_job_tf_config.pem'])
            config_file = 'tests/resources/config_for_test_get_job_tf_config'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('resource_manager_root_group.command_name', 'resource-manager')
    resource_group_command_name = oci_cli.cli_util.override('job_group.command_name', 'job')
    request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='GetJobTfConfig')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('resource_manager', 'GetJobTfConfig', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_job_tf_config.command_name', 'get-job-tf-config')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: resource_manager, GetJobTfConfig. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_job_tf_config.command_name', 'get-job-tf-config'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_job_tf_config.command_name', 'get-job-tf-config')))

            params.extend(['--from-json', input_content])
            import tempfile
            tmp = tempfile.NamedTemporaryFile(delete=False)
            tmp_file_name = tmp.name
            tmp.close()
            try:
                params.extend(['--file', tmp_file_name])
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'resource_manager',
                    'GetJobTfConfig',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'binary',
                    False,
                    True,
                    tmp_file_name
                )
            finally:
                if os.path.isfile(tmp_file_name):
                    os.unlink(tmp_file_name)  # deletes the file
                if os.path.exists('tests/resources/keyfile_for_test_get_job_tf_config.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_job_tf_config.pem')
                if os.path.exists('tests/resources/config_for_test_get_job_tf_config'):
                    os.remove('tests/resources/config_for_test_get_job_tf_config')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='GetJobTfConfig')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_job_tf_state(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('resource_manager', 'GetJobTfState'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('resource_manager', 'ResourceManager', 'GetJobTfState')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_job_tf_state.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_job_tf_state', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_job_tf_state.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_job_tf_state'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_job_tf_state.pem'])
            config_file = 'tests/resources/config_for_test_get_job_tf_state'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('resource_manager_root_group.command_name', 'resource-manager')
    resource_group_command_name = oci_cli.cli_util.override('job_group.command_name', 'job')
    request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='GetJobTfState')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('resource_manager', 'GetJobTfState', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_job_tf_state.command_name', 'get-job-tf-state')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: resource_manager, GetJobTfState. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_job_tf_state.command_name', 'get-job-tf-state'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_job_tf_state.command_name', 'get-job-tf-state')))

            params.extend(['--from-json', input_content])
            import tempfile
            tmp = tempfile.NamedTemporaryFile(delete=False)
            tmp_file_name = tmp.name
            tmp.close()
            try:
                params.extend(['--file', tmp_file_name])
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'resource_manager',
                    'GetJobTfState',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'binary',
                    False,
                    True,
                    tmp_file_name
                )
            finally:
                if os.path.isfile(tmp_file_name):
                    os.unlink(tmp_file_name)  # deletes the file
                if os.path.exists('tests/resources/keyfile_for_test_get_job_tf_state.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_job_tf_state.pem')
                if os.path.exists('tests/resources/config_for_test_get_job_tf_state'):
                    os.remove('tests/resources/config_for_test_get_job_tf_state')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='GetJobTfState')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_stack(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('resource_manager', 'GetStack'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('resource_manager', 'ResourceManager', 'GetStack')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_stack.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_stack', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_stack.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_stack'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_stack.pem'])
            config_file = 'tests/resources/config_for_test_get_stack'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('resource_manager_root_group.command_name', 'resource-manager')
    resource_group_command_name = oci_cli.cli_util.override('stack_group.command_name', 'stack')
    request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='GetStack')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('resource_manager', 'GetStack', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_stack.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: resource_manager, GetStack. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_stack.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_stack.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'resource_manager',
                    'GetStack',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'stack',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_stack.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_stack.pem')
                if os.path.exists('tests/resources/config_for_test_get_stack'):
                    os.remove('tests/resources/config_for_test_get_stack')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='GetStack')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_stack_tf_config(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('resource_manager', 'GetStackTfConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('resource_manager', 'ResourceManager', 'GetStackTfConfig')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_stack_tf_config.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_stack_tf_config', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_stack_tf_config.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_stack_tf_config'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_stack_tf_config.pem'])
            config_file = 'tests/resources/config_for_test_get_stack_tf_config'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('resource_manager_root_group.command_name', 'resource-manager')
    resource_group_command_name = oci_cli.cli_util.override('stack_group.command_name', 'stack')
    request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='GetStackTfConfig')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('resource_manager', 'GetStackTfConfig', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_stack_tf_config.command_name', 'get-stack-tf-config')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: resource_manager, GetStackTfConfig. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_stack_tf_config.command_name', 'get-stack-tf-config'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_stack_tf_config.command_name', 'get-stack-tf-config')))

            params.extend(['--from-json', input_content])
            import tempfile
            tmp = tempfile.NamedTemporaryFile(delete=False)
            tmp_file_name = tmp.name
            tmp.close()
            try:
                params.extend(['--file', tmp_file_name])
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'resource_manager',
                    'GetStackTfConfig',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'binary',
                    False,
                    True,
                    tmp_file_name
                )
            finally:
                if os.path.isfile(tmp_file_name):
                    os.unlink(tmp_file_name)  # deletes the file
                if os.path.exists('tests/resources/keyfile_for_test_get_stack_tf_config.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_stack_tf_config.pem')
                if os.path.exists('tests/resources/config_for_test_get_stack_tf_config'):
                    os.remove('tests/resources/config_for_test_get_stack_tf_config')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='GetStackTfConfig')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_jobs(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('resource_manager', 'ListJobs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('resource_manager', 'ResourceManager', 'ListJobs')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_jobs.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_jobs', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_jobs.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_jobs'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_jobs.pem'])
            config_file = 'tests/resources/config_for_test_list_jobs'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('resource_manager_root_group.command_name', 'resource-manager')
    resource_group_command_name = oci_cli.cli_util.override('job_group.command_name', 'job')
    request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='ListJobs')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('resource_manager', 'ListJobs', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_jobs.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: resource_manager, ListJobs. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_jobs.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_jobs.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'resource_manager',
                    'ListJobs',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_jobs.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_jobs.pem')
                if os.path.exists('tests/resources/config_for_test_list_jobs'):
                    os.remove('tests/resources/config_for_test_list_jobs')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='ListJobs')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_stacks(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('resource_manager', 'ListStacks'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('resource_manager', 'ResourceManager', 'ListStacks')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_stacks.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_stacks', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_stacks.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_stacks'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_stacks.pem'])
            config_file = 'tests/resources/config_for_test_list_stacks'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('resource_manager_root_group.command_name', 'resource-manager')
    resource_group_command_name = oci_cli.cli_util.override('stack_group.command_name', 'stack')
    request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='ListStacks')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('resource_manager', 'ListStacks', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_stacks.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: resource_manager, ListStacks. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_stacks.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_stacks.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'resource_manager',
                    'ListStacks',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_stacks.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_stacks.pem')
                if os.path.exists('tests/resources/config_for_test_list_stacks'):
                    os.remove('tests/resources/config_for_test_list_stacks')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='ListStacks')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_job(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('resource_manager', 'UpdateJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('resource_manager', 'ResourceManager', 'UpdateJob')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_job.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_job', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_job.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_job'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_job.pem'])
            config_file = 'tests/resources/config_for_test_update_job'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('resource_manager_root_group.command_name', 'resource-manager')
    resource_group_command_name = oci_cli.cli_util.override('job_group.command_name', 'job')
    request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='UpdateJob')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateJobDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('resource_manager', 'UpdateJob', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_job.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: resource_manager, UpdateJob. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_job.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_job.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'resource_manager',
                    'UpdateJob',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'job',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_job.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_job.pem')
                if os.path.exists('tests/resources/config_for_test_update_job'):
                    os.remove('tests/resources/config_for_test_update_job')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='UpdateJob')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_stack(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('resource_manager', 'UpdateStack'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('resource_manager', 'ResourceManager', 'UpdateStack')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_stack.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_stack', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_stack.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_stack'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_stack.pem'])
            config_file = 'tests/resources/config_for_test_update_stack'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('resource_manager_root_group.command_name', 'resource-manager')
    resource_group_command_name = oci_cli.cli_util.override('stack_group.command_name', 'stack')
    request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='UpdateStack')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateStackDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('resource_manager', 'UpdateStack', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_stack.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: resource_manager, UpdateStack. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_stack.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_stack.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'resource_manager',
                    'UpdateStack',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'stack',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_stack.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_stack.pem')
                if os.path.exists('tests/resources/config_for_test_update_stack'):
                    os.remove('tests/resources/config_for_test_update_stack')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='resource_manager', api_name='UpdateStack')
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
