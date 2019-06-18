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
    custom_vcr = test_config_container.create_vcr(cassette_library_dir="services/core/tests/cassettes/for_generated")

    cassette_location = 'core_{name}.yml'.format(name=request.function.__name__)
    with custom_vcr.use_cassette(cassette_location):
        yield


@pytest.mark.generated
def test_change_boot_volume_backup_compartment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ChangeBootVolumeBackupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'ChangeBootVolumeBackupCompartment')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_change_boot_volume_backup_compartment.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_change_boot_volume_backup_compartment', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_change_boot_volume_backup_compartment.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_change_boot_volume_backup_compartment'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_change_boot_volume_backup_compartment.pem'])
            config_file = 'tests/resources/config_for_test_change_boot_volume_backup_compartment'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('boot_volume_backup_group.command_name', 'boot_volume_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ChangeBootVolumeBackupCompartment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'ChangeBootVolumeBackupCompartmentDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ChangeBootVolumeBackupCompartment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('change_boot_volume_backup_compartment.command_name', 'change-compartment'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ChangeBootVolumeBackupCompartment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('change_boot_volume_backup_compartment.command_name', 'change-compartment'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('change_boot_volume_backup_compartment.command_name', 'change-compartment')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ChangeBootVolumeBackupCompartment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'changeBootVolumeBackupCompartment',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_change_boot_volume_backup_compartment.pem'):
                    os.remove('tests/resources/keyfile_for_test_change_boot_volume_backup_compartment.pem')
                if os.path.exists('tests/resources/config_for_test_change_boot_volume_backup_compartment'):
                    os.remove('tests/resources/config_for_test_change_boot_volume_backup_compartment')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ChangeBootVolumeBackupCompartment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_change_boot_volume_compartment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ChangeBootVolumeCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'ChangeBootVolumeCompartment')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_change_boot_volume_compartment.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_change_boot_volume_compartment', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_change_boot_volume_compartment.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_change_boot_volume_compartment'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_change_boot_volume_compartment.pem'])
            config_file = 'tests/resources/config_for_test_change_boot_volume_compartment'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('boot_volume_group.command_name', 'boot_volume')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ChangeBootVolumeCompartment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'ChangeBootVolumeCompartmentDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ChangeBootVolumeCompartment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('change_boot_volume_compartment.command_name', 'change-compartment'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ChangeBootVolumeCompartment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('change_boot_volume_compartment.command_name', 'change-compartment'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('change_boot_volume_compartment.command_name', 'change-compartment')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ChangeBootVolumeCompartment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'changeBootVolumeCompartment',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_change_boot_volume_compartment.pem'):
                    os.remove('tests/resources/keyfile_for_test_change_boot_volume_compartment.pem')
                if os.path.exists('tests/resources/config_for_test_change_boot_volume_compartment'):
                    os.remove('tests/resources/config_for_test_change_boot_volume_compartment')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ChangeBootVolumeCompartment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_change_volume_backup_compartment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ChangeVolumeBackupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'ChangeVolumeBackupCompartment')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_change_volume_backup_compartment.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_change_volume_backup_compartment', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_change_volume_backup_compartment.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_change_volume_backup_compartment'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_change_volume_backup_compartment.pem'])
            config_file = 'tests/resources/config_for_test_change_volume_backup_compartment'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_backup_group.command_name', 'volume_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ChangeVolumeBackupCompartment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'ChangeVolumeBackupCompartmentDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ChangeVolumeBackupCompartment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('change_volume_backup_compartment.command_name', 'change-compartment'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ChangeVolumeBackupCompartment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('change_volume_backup_compartment.command_name', 'change-compartment'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('change_volume_backup_compartment.command_name', 'change-compartment')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ChangeVolumeBackupCompartment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'changeVolumeBackupCompartment',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_change_volume_backup_compartment.pem'):
                    os.remove('tests/resources/keyfile_for_test_change_volume_backup_compartment.pem')
                if os.path.exists('tests/resources/config_for_test_change_volume_backup_compartment'):
                    os.remove('tests/resources/config_for_test_change_volume_backup_compartment')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ChangeVolumeBackupCompartment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_change_volume_compartment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ChangeVolumeCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'ChangeVolumeCompartment')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_change_volume_compartment.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_change_volume_compartment', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_change_volume_compartment.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_change_volume_compartment'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_change_volume_compartment.pem'])
            config_file = 'tests/resources/config_for_test_change_volume_compartment'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group.command_name', 'volume')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ChangeVolumeCompartment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'ChangeVolumeCompartmentDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ChangeVolumeCompartment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('change_volume_compartment.command_name', 'change-compartment'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ChangeVolumeCompartment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('change_volume_compartment.command_name', 'change-compartment'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('change_volume_compartment.command_name', 'change-compartment')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ChangeVolumeCompartment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'changeVolumeCompartment',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_change_volume_compartment.pem'):
                    os.remove('tests/resources/keyfile_for_test_change_volume_compartment.pem')
                if os.path.exists('tests/resources/config_for_test_change_volume_compartment'):
                    os.remove('tests/resources/config_for_test_change_volume_compartment')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ChangeVolumeCompartment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_change_volume_group_backup_compartment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ChangeVolumeGroupBackupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'ChangeVolumeGroupBackupCompartment')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_change_volume_group_backup_compartment.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_change_volume_group_backup_compartment', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_change_volume_group_backup_compartment.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_change_volume_group_backup_compartment'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_change_volume_group_backup_compartment.pem'])
            config_file = 'tests/resources/config_for_test_change_volume_group_backup_compartment'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group_backup_group.command_name', 'volume_group_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ChangeVolumeGroupBackupCompartment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'ChangeVolumeGroupBackupCompartmentDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ChangeVolumeGroupBackupCompartment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('change_volume_group_backup_compartment.command_name', 'change-compartment'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ChangeVolumeGroupBackupCompartment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('change_volume_group_backup_compartment.command_name', 'change-compartment'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('change_volume_group_backup_compartment.command_name', 'change-compartment')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ChangeVolumeGroupBackupCompartment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'changeVolumeGroupBackupCompartment',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_change_volume_group_backup_compartment.pem'):
                    os.remove('tests/resources/keyfile_for_test_change_volume_group_backup_compartment.pem')
                if os.path.exists('tests/resources/config_for_test_change_volume_group_backup_compartment'):
                    os.remove('tests/resources/config_for_test_change_volume_group_backup_compartment')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ChangeVolumeGroupBackupCompartment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_change_volume_group_compartment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ChangeVolumeGroupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'ChangeVolumeGroupCompartment')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_change_volume_group_compartment.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_change_volume_group_compartment', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_change_volume_group_compartment.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_change_volume_group_compartment'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_change_volume_group_compartment.pem'])
            config_file = 'tests/resources/config_for_test_change_volume_group_compartment'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group_group.command_name', 'volume_group')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ChangeVolumeGroupCompartment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'ChangeVolumeGroupCompartmentDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ChangeVolumeGroupCompartment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('change_volume_group_compartment.command_name', 'change-compartment'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ChangeVolumeGroupCompartment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('change_volume_group_compartment.command_name', 'change-compartment'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('change_volume_group_compartment.command_name', 'change-compartment')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ChangeVolumeGroupCompartment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'changeVolumeGroupCompartment',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_change_volume_group_compartment.pem'):
                    os.remove('tests/resources/keyfile_for_test_change_volume_group_compartment.pem')
                if os.path.exists('tests/resources/config_for_test_change_volume_group_compartment'):
                    os.remove('tests/resources/config_for_test_change_volume_group_compartment')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ChangeVolumeGroupCompartment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_copy_volume_backup(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CopyVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'CopyVolumeBackup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_copy_volume_backup.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_copy_volume_backup', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_copy_volume_backup.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_copy_volume_backup'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_copy_volume_backup.pem'])
            config_file = 'tests/resources/config_for_test_copy_volume_backup'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_backup_group.command_name', 'volume_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CopyVolumeBackup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CopyVolumeBackupDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CopyVolumeBackup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('copy_volume_backup.command_name', 'copy'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CopyVolumeBackup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('copy_volume_backup.command_name', 'copy'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('copy_volume_backup.command_name', 'copy')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CopyVolumeBackup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volumeBackup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_copy_volume_backup.pem'):
                    os.remove('tests/resources/keyfile_for_test_copy_volume_backup.pem')
                if os.path.exists('tests/resources/config_for_test_copy_volume_backup'):
                    os.remove('tests/resources/config_for_test_copy_volume_backup')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CopyVolumeBackup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_boot_volume(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateBootVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'CreateBootVolume')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_boot_volume.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_boot_volume', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_boot_volume.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_boot_volume'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_boot_volume.pem'])
            config_file = 'tests/resources/config_for_test_create_boot_volume'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('boot_volume_group.command_name', 'boot_volume')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateBootVolume')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateBootVolumeDetails'
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

            if request.get('type') == 'bootVolumeBackup':
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_boot_volume_boot_volume_source_from_boot_volume_backup_details.command_name', 'create-boot-volume-boot-volume-source-from-boot-volume-backup-details')
                )

                if params:
                    del request['type']

            if request.get('type') == 'bootVolume':
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_boot_volume_boot_volume_source_from_boot_volume_details.command_name', 'create-boot-volume-boot-volume-source-from-boot-volume-details')
                )

                if params:
                    del request['type']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateBootVolume', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_boot_volume.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateBootVolume. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_boot_volume.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_boot_volume.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateBootVolume',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'bootVolume',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_boot_volume.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_boot_volume.pem')
                if os.path.exists('tests/resources/config_for_test_create_boot_volume'):
                    os.remove('tests/resources/config_for_test_create_boot_volume')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateBootVolume')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_boot_volume_backup(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateBootVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'CreateBootVolumeBackup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_boot_volume_backup.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_boot_volume_backup', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_boot_volume_backup.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_boot_volume_backup'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_boot_volume_backup.pem'])
            config_file = 'tests/resources/config_for_test_create_boot_volume_backup'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('boot_volume_backup_group.command_name', 'boot_volume_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateBootVolumeBackup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateBootVolumeBackupDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateBootVolumeBackup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_boot_volume_backup.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateBootVolumeBackup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_boot_volume_backup.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_boot_volume_backup.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateBootVolumeBackup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'bootVolumeBackup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_boot_volume_backup.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_boot_volume_backup.pem')
                if os.path.exists('tests/resources/config_for_test_create_boot_volume_backup'):
                    os.remove('tests/resources/config_for_test_create_boot_volume_backup')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateBootVolumeBackup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_volume(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'CreateVolume')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_volume.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_volume', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_volume.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_volume'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_volume.pem'])
            config_file = 'tests/resources/config_for_test_create_volume'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group.command_name', 'volume')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateVolume')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateVolumeDetails'
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

            if request.get('type') == 'volume':
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_volume_volume_source_from_volume_details.command_name', 'create-volume-volume-source-from-volume-details')
                )

                if params:
                    del request['type']

            if request.get('type') == 'volumeBackup':
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_volume_volume_source_from_volume_backup_details.command_name', 'create-volume-volume-source-from-volume-backup-details')
                )

                if params:
                    del request['type']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateVolume', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_volume.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateVolume. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_volume.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_volume.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateVolume',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volume',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_volume.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_volume.pem')
                if os.path.exists('tests/resources/config_for_test_create_volume'):
                    os.remove('tests/resources/config_for_test_create_volume')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateVolume')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_volume_backup(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'CreateVolumeBackup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_volume_backup.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_volume_backup', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_volume_backup.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_volume_backup'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_volume_backup.pem'])
            config_file = 'tests/resources/config_for_test_create_volume_backup'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_backup_group.command_name', 'volume_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateVolumeBackup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateVolumeBackupDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateVolumeBackup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_volume_backup.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateVolumeBackup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_volume_backup.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_volume_backup.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateVolumeBackup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volumeBackup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_volume_backup.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_volume_backup.pem')
                if os.path.exists('tests/resources/config_for_test_create_volume_backup'):
                    os.remove('tests/resources/config_for_test_create_volume_backup')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateVolumeBackup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_volume_backup_policy_assignment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateVolumeBackupPolicyAssignment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'CreateVolumeBackupPolicyAssignment')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_volume_backup_policy_assignment.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_volume_backup_policy_assignment', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_volume_backup_policy_assignment.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_volume_backup_policy_assignment'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_volume_backup_policy_assignment.pem'])
            config_file = 'tests/resources/config_for_test_create_volume_backup_policy_assignment'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_backup_policy_assignment_group.command_name', 'volume_backup_policy_assignment')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateVolumeBackupPolicyAssignment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateVolumeBackupPolicyAssignmentDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateVolumeBackupPolicyAssignment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_volume_backup_policy_assignment.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateVolumeBackupPolicyAssignment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_volume_backup_policy_assignment.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_volume_backup_policy_assignment.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateVolumeBackupPolicyAssignment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volumeBackupPolicyAssignment',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_volume_backup_policy_assignment.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_volume_backup_policy_assignment.pem')
                if os.path.exists('tests/resources/config_for_test_create_volume_backup_policy_assignment'):
                    os.remove('tests/resources/config_for_test_create_volume_backup_policy_assignment')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateVolumeBackupPolicyAssignment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_volume_group(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateVolumeGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'CreateVolumeGroup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_volume_group.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_volume_group', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_volume_group.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_volume_group'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_volume_group.pem'])
            config_file = 'tests/resources/config_for_test_create_volume_group'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group_group.command_name', 'volume_group')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateVolumeGroup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateVolumeGroupDetails'
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

            if request.get('type') == 'volumeGroupId':
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_volume_group_volume_group_source_from_volume_group_details.command_name', 'create-volume-group-volume-group-source-from-volume-group-details')
                )

                if params:
                    del request['type']

            if request.get('type') == 'volumeIds':
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_volume_group_volume_group_source_from_volumes_details.command_name', 'create-volume-group-volume-group-source-from-volumes-details')
                )

                if params:
                    del request['type']

            if request.get('type') == 'volumeGroupBackupId':
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_volume_group_volume_group_source_from_volume_group_backup_details.command_name', 'create-volume-group-volume-group-source-from-volume-group-backup-details')
                )

                if params:
                    del request['type']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateVolumeGroup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_volume_group.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateVolumeGroup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_volume_group.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_volume_group.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateVolumeGroup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volumeGroup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_volume_group.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_volume_group.pem')
                if os.path.exists('tests/resources/config_for_test_create_volume_group'):
                    os.remove('tests/resources/config_for_test_create_volume_group')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateVolumeGroup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_volume_group_backup(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateVolumeGroupBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'CreateVolumeGroupBackup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_volume_group_backup.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_volume_group_backup', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_volume_group_backup.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_volume_group_backup'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_volume_group_backup.pem'])
            config_file = 'tests/resources/config_for_test_create_volume_group_backup'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group_backup_group.command_name', 'volume_group_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateVolumeGroupBackup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateVolumeGroupBackupDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateVolumeGroupBackup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_volume_group_backup.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateVolumeGroupBackup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_volume_group_backup.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_volume_group_backup.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateVolumeGroupBackup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volumeGroupBackup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_volume_group_backup.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_volume_group_backup.pem')
                if os.path.exists('tests/resources/config_for_test_create_volume_group_backup'):
                    os.remove('tests/resources/config_for_test_create_volume_group_backup')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateVolumeGroupBackup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_boot_volume(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteBootVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'DeleteBootVolume')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_boot_volume.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_boot_volume', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_boot_volume.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_boot_volume'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_boot_volume.pem'])
            config_file = 'tests/resources/config_for_test_delete_boot_volume'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('boot_volume_group.command_name', 'boot_volume')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteBootVolume')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteBootVolume', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_boot_volume.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteBootVolume. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_boot_volume.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_boot_volume.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteBootVolume',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteBootVolume',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_boot_volume.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_boot_volume.pem')
                if os.path.exists('tests/resources/config_for_test_delete_boot_volume'):
                    os.remove('tests/resources/config_for_test_delete_boot_volume')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteBootVolume')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_boot_volume_backup(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteBootVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'DeleteBootVolumeBackup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_boot_volume_backup.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_boot_volume_backup', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_boot_volume_backup.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_boot_volume_backup'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_boot_volume_backup.pem'])
            config_file = 'tests/resources/config_for_test_delete_boot_volume_backup'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('boot_volume_backup_group.command_name', 'boot_volume_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteBootVolumeBackup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteBootVolumeBackup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_boot_volume_backup.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteBootVolumeBackup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_boot_volume_backup.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_boot_volume_backup.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteBootVolumeBackup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteBootVolumeBackup',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_boot_volume_backup.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_boot_volume_backup.pem')
                if os.path.exists('tests/resources/config_for_test_delete_boot_volume_backup'):
                    os.remove('tests/resources/config_for_test_delete_boot_volume_backup')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteBootVolumeBackup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_boot_volume_kms_key(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteBootVolumeKmsKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'DeleteBootVolumeKmsKey')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_boot_volume_kms_key.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_boot_volume_kms_key', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_boot_volume_kms_key.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_boot_volume_kms_key'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_boot_volume_kms_key.pem'])
            config_file = 'tests/resources/config_for_test_delete_boot_volume_kms_key'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('boot_volume_kms_key_group.command_name', 'boot_volume_kms_key')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteBootVolumeKmsKey')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteBootVolumeKmsKey', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_boot_volume_kms_key.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteBootVolumeKmsKey. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_boot_volume_kms_key.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_boot_volume_kms_key.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteBootVolumeKmsKey',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteBootVolumeKmsKey',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_boot_volume_kms_key.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_boot_volume_kms_key.pem')
                if os.path.exists('tests/resources/config_for_test_delete_boot_volume_kms_key'):
                    os.remove('tests/resources/config_for_test_delete_boot_volume_kms_key')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteBootVolumeKmsKey')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_volume(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'DeleteVolume')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_volume.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_volume', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_volume.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_volume'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_volume.pem'])
            config_file = 'tests/resources/config_for_test_delete_volume'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group.command_name', 'volume')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVolume')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteVolume', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_volume.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteVolume. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_volume.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_volume.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteVolume',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteVolume',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_volume.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_volume.pem')
                if os.path.exists('tests/resources/config_for_test_delete_volume'):
                    os.remove('tests/resources/config_for_test_delete_volume')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVolume')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_volume_backup(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'DeleteVolumeBackup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_volume_backup.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_volume_backup', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_volume_backup.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_volume_backup'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_volume_backup.pem'])
            config_file = 'tests/resources/config_for_test_delete_volume_backup'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_backup_group.command_name', 'volume_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeBackup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteVolumeBackup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_volume_backup.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteVolumeBackup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_volume_backup.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_volume_backup.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteVolumeBackup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteVolumeBackup',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_volume_backup.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_volume_backup.pem')
                if os.path.exists('tests/resources/config_for_test_delete_volume_backup'):
                    os.remove('tests/resources/config_for_test_delete_volume_backup')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeBackup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_volume_backup_policy_assignment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteVolumeBackupPolicyAssignment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'DeleteVolumeBackupPolicyAssignment')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_volume_backup_policy_assignment.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_volume_backup_policy_assignment', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_volume_backup_policy_assignment.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_volume_backup_policy_assignment'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_volume_backup_policy_assignment.pem'])
            config_file = 'tests/resources/config_for_test_delete_volume_backup_policy_assignment'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_backup_policy_assignment_group.command_name', 'volume_backup_policy_assignment')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeBackupPolicyAssignment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteVolumeBackupPolicyAssignment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_volume_backup_policy_assignment.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteVolumeBackupPolicyAssignment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_volume_backup_policy_assignment.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_volume_backup_policy_assignment.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteVolumeBackupPolicyAssignment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteVolumeBackupPolicyAssignment',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_volume_backup_policy_assignment.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_volume_backup_policy_assignment.pem')
                if os.path.exists('tests/resources/config_for_test_delete_volume_backup_policy_assignment'):
                    os.remove('tests/resources/config_for_test_delete_volume_backup_policy_assignment')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeBackupPolicyAssignment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_volume_group(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteVolumeGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'DeleteVolumeGroup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_volume_group.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_volume_group', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_volume_group.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_volume_group'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_volume_group.pem'])
            config_file = 'tests/resources/config_for_test_delete_volume_group'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group_group.command_name', 'volume_group')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeGroup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteVolumeGroup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_volume_group.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteVolumeGroup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_volume_group.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_volume_group.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteVolumeGroup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteVolumeGroup',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_volume_group.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_volume_group.pem')
                if os.path.exists('tests/resources/config_for_test_delete_volume_group'):
                    os.remove('tests/resources/config_for_test_delete_volume_group')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeGroup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_volume_group_backup(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteVolumeGroupBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'DeleteVolumeGroupBackup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_volume_group_backup.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_volume_group_backup', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_volume_group_backup.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_volume_group_backup'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_volume_group_backup.pem'])
            config_file = 'tests/resources/config_for_test_delete_volume_group_backup'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group_backup_group.command_name', 'volume_group_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeGroupBackup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteVolumeGroupBackup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_volume_group_backup.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteVolumeGroupBackup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_volume_group_backup.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_volume_group_backup.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteVolumeGroupBackup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteVolumeGroupBackup',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_volume_group_backup.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_volume_group_backup.pem')
                if os.path.exists('tests/resources/config_for_test_delete_volume_group_backup'):
                    os.remove('tests/resources/config_for_test_delete_volume_group_backup')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeGroupBackup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_volume_kms_key(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteVolumeKmsKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'DeleteVolumeKmsKey')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_volume_kms_key.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_volume_kms_key', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_volume_kms_key.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_volume_kms_key'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_volume_kms_key.pem'])
            config_file = 'tests/resources/config_for_test_delete_volume_kms_key'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_kms_key_group.command_name', 'volume_kms_key')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeKmsKey')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteVolumeKmsKey', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_volume_kms_key.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteVolumeKmsKey. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_volume_kms_key.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_volume_kms_key.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteVolumeKmsKey',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteVolumeKmsKey',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_volume_kms_key.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_volume_kms_key.pem')
                if os.path.exists('tests/resources/config_for_test_delete_volume_kms_key'):
                    os.remove('tests/resources/config_for_test_delete_volume_kms_key')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeKmsKey')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_boot_volume(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetBootVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'GetBootVolume')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_boot_volume.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_boot_volume', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_boot_volume.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_boot_volume'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_boot_volume.pem'])
            config_file = 'tests/resources/config_for_test_get_boot_volume'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('boot_volume_group.command_name', 'boot_volume')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetBootVolume')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetBootVolume', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_boot_volume.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetBootVolume. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_boot_volume.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_boot_volume.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetBootVolume',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'bootVolume',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_boot_volume.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_boot_volume.pem')
                if os.path.exists('tests/resources/config_for_test_get_boot_volume'):
                    os.remove('tests/resources/config_for_test_get_boot_volume')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetBootVolume')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_boot_volume_backup(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetBootVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'GetBootVolumeBackup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_boot_volume_backup.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_boot_volume_backup', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_boot_volume_backup.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_boot_volume_backup'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_boot_volume_backup.pem'])
            config_file = 'tests/resources/config_for_test_get_boot_volume_backup'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('boot_volume_backup_group.command_name', 'boot_volume_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetBootVolumeBackup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetBootVolumeBackup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_boot_volume_backup.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetBootVolumeBackup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_boot_volume_backup.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_boot_volume_backup.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetBootVolumeBackup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'bootVolumeBackup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_boot_volume_backup.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_boot_volume_backup.pem')
                if os.path.exists('tests/resources/config_for_test_get_boot_volume_backup'):
                    os.remove('tests/resources/config_for_test_get_boot_volume_backup')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetBootVolumeBackup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_boot_volume_kms_key(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetBootVolumeKmsKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'GetBootVolumeKmsKey')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_boot_volume_kms_key.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_boot_volume_kms_key', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_boot_volume_kms_key.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_boot_volume_kms_key'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_boot_volume_kms_key.pem'])
            config_file = 'tests/resources/config_for_test_get_boot_volume_kms_key'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('boot_volume_kms_key_group.command_name', 'boot_volume_kms_key')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetBootVolumeKmsKey')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetBootVolumeKmsKey', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_boot_volume_kms_key.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetBootVolumeKmsKey. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_boot_volume_kms_key.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_boot_volume_kms_key.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetBootVolumeKmsKey',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'bootVolumeKmsKey',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_boot_volume_kms_key.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_boot_volume_kms_key.pem')
                if os.path.exists('tests/resources/config_for_test_get_boot_volume_kms_key'):
                    os.remove('tests/resources/config_for_test_get_boot_volume_kms_key')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetBootVolumeKmsKey')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_volume(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'GetVolume')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_volume.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_volume', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_volume.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_volume'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_volume.pem'])
            config_file = 'tests/resources/config_for_test_get_volume'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group.command_name', 'volume')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolume')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetVolume', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_volume.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetVolume. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetVolume',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volume',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_volume.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_volume.pem')
                if os.path.exists('tests/resources/config_for_test_get_volume'):
                    os.remove('tests/resources/config_for_test_get_volume')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolume')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_volume_backup(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'GetVolumeBackup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_volume_backup.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_volume_backup', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_volume_backup.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_volume_backup'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_volume_backup.pem'])
            config_file = 'tests/resources/config_for_test_get_volume_backup'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_backup_group.command_name', 'volume_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolumeBackup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetVolumeBackup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_volume_backup.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetVolumeBackup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume_backup.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume_backup.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetVolumeBackup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volumeBackup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_volume_backup.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_volume_backup.pem')
                if os.path.exists('tests/resources/config_for_test_get_volume_backup'):
                    os.remove('tests/resources/config_for_test_get_volume_backup')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolumeBackup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_volume_backup_policy(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetVolumeBackupPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'GetVolumeBackupPolicy')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_volume_backup_policy.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_volume_backup_policy', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_volume_backup_policy.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_volume_backup_policy'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_volume_backup_policy.pem'])
            config_file = 'tests/resources/config_for_test_get_volume_backup_policy'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_backup_policy_group.command_name', 'volume_backup_policy')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolumeBackupPolicy')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetVolumeBackupPolicy', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_volume_backup_policy.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetVolumeBackupPolicy. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume_backup_policy.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume_backup_policy.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetVolumeBackupPolicy',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volumeBackupPolicy',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_volume_backup_policy.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_volume_backup_policy.pem')
                if os.path.exists('tests/resources/config_for_test_get_volume_backup_policy'):
                    os.remove('tests/resources/config_for_test_get_volume_backup_policy')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolumeBackupPolicy')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_volume_backup_policy_asset_assignment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetVolumeBackupPolicyAssetAssignment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'GetVolumeBackupPolicyAssetAssignment')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_volume_backup_policy_asset_assignment.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_volume_backup_policy_asset_assignment', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_volume_backup_policy_asset_assignment.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_volume_backup_policy_asset_assignment'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_volume_backup_policy_asset_assignment.pem'])
            config_file = 'tests/resources/config_for_test_get_volume_backup_policy_asset_assignment'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_backup_policy_assignment_group.command_name', 'volume_backup_policy_assignment')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolumeBackupPolicyAssetAssignment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetVolumeBackupPolicyAssetAssignment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_volume_backup_policy_asset_assignment.command_name', 'get-volume-backup-policy-asset-assignment'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetVolumeBackupPolicyAssetAssignment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume_backup_policy_asset_assignment.command_name', 'get-volume-backup-policy-asset-assignment'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume_backup_policy_asset_assignment.command_name', 'get-volume-backup-policy-asset-assignment')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetVolumeBackupPolicyAssetAssignment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_volume_backup_policy_asset_assignment.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_volume_backup_policy_asset_assignment.pem')
                if os.path.exists('tests/resources/config_for_test_get_volume_backup_policy_asset_assignment'):
                    os.remove('tests/resources/config_for_test_get_volume_backup_policy_asset_assignment')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolumeBackupPolicyAssetAssignment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_volume_backup_policy_assignment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetVolumeBackupPolicyAssignment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'GetVolumeBackupPolicyAssignment')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_volume_backup_policy_assignment.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_volume_backup_policy_assignment', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_volume_backup_policy_assignment.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_volume_backup_policy_assignment'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_volume_backup_policy_assignment.pem'])
            config_file = 'tests/resources/config_for_test_get_volume_backup_policy_assignment'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_backup_policy_assignment_group.command_name', 'volume_backup_policy_assignment')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolumeBackupPolicyAssignment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetVolumeBackupPolicyAssignment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_volume_backup_policy_assignment.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetVolumeBackupPolicyAssignment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume_backup_policy_assignment.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume_backup_policy_assignment.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetVolumeBackupPolicyAssignment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volumeBackupPolicyAssignment',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_volume_backup_policy_assignment.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_volume_backup_policy_assignment.pem')
                if os.path.exists('tests/resources/config_for_test_get_volume_backup_policy_assignment'):
                    os.remove('tests/resources/config_for_test_get_volume_backup_policy_assignment')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolumeBackupPolicyAssignment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_volume_group(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetVolumeGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'GetVolumeGroup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_volume_group.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_volume_group', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_volume_group.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_volume_group'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_volume_group.pem'])
            config_file = 'tests/resources/config_for_test_get_volume_group'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group_group.command_name', 'volume_group')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolumeGroup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetVolumeGroup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_volume_group.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetVolumeGroup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume_group.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume_group.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetVolumeGroup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volumeGroup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_volume_group.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_volume_group.pem')
                if os.path.exists('tests/resources/config_for_test_get_volume_group'):
                    os.remove('tests/resources/config_for_test_get_volume_group')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolumeGroup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_volume_group_backup(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetVolumeGroupBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'GetVolumeGroupBackup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_volume_group_backup.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_volume_group_backup', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_volume_group_backup.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_volume_group_backup'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_volume_group_backup.pem'])
            config_file = 'tests/resources/config_for_test_get_volume_group_backup'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group_backup_group.command_name', 'volume_group_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolumeGroupBackup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetVolumeGroupBackup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_volume_group_backup.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetVolumeGroupBackup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume_group_backup.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume_group_backup.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetVolumeGroupBackup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volumeGroupBackup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_volume_group_backup.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_volume_group_backup.pem')
                if os.path.exists('tests/resources/config_for_test_get_volume_group_backup'):
                    os.remove('tests/resources/config_for_test_get_volume_group_backup')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolumeGroupBackup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_volume_kms_key(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetVolumeKmsKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'GetVolumeKmsKey')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_volume_kms_key.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_volume_kms_key', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_volume_kms_key.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_volume_kms_key'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_volume_kms_key.pem'])
            config_file = 'tests/resources/config_for_test_get_volume_kms_key'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_kms_key_group.command_name', 'volume_kms_key')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolumeKmsKey')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetVolumeKmsKey', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_volume_kms_key.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetVolumeKmsKey. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume_kms_key.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_volume_kms_key.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetVolumeKmsKey',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volumeKmsKey',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_volume_kms_key.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_volume_kms_key.pem')
                if os.path.exists('tests/resources/config_for_test_get_volume_kms_key'):
                    os.remove('tests/resources/config_for_test_get_volume_kms_key')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVolumeKmsKey')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_boot_volume_backups(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListBootVolumeBackups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'ListBootVolumeBackups')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_boot_volume_backups.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_boot_volume_backups', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_boot_volume_backups.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_boot_volume_backups'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_boot_volume_backups.pem'])
            config_file = 'tests/resources/config_for_test_list_boot_volume_backups'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('boot_volume_backup_group.command_name', 'boot_volume_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListBootVolumeBackups')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListBootVolumeBackups', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_boot_volume_backups.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListBootVolumeBackups. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_boot_volume_backups.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_boot_volume_backups.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListBootVolumeBackups',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_boot_volume_backups.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_boot_volume_backups.pem')
                if os.path.exists('tests/resources/config_for_test_list_boot_volume_backups'):
                    os.remove('tests/resources/config_for_test_list_boot_volume_backups')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListBootVolumeBackups')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_boot_volumes(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListBootVolumes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'ListBootVolumes')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_boot_volumes.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_boot_volumes', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_boot_volumes.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_boot_volumes'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_boot_volumes.pem'])
            config_file = 'tests/resources/config_for_test_list_boot_volumes'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('boot_volume_group.command_name', 'boot_volume')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListBootVolumes')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListBootVolumes', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_boot_volumes.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListBootVolumes. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_boot_volumes.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_boot_volumes.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListBootVolumes',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_boot_volumes.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_boot_volumes.pem')
                if os.path.exists('tests/resources/config_for_test_list_boot_volumes'):
                    os.remove('tests/resources/config_for_test_list_boot_volumes')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListBootVolumes')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_volume_backup_policies(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListVolumeBackupPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'ListVolumeBackupPolicies')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_volume_backup_policies.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_volume_backup_policies', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_volume_backup_policies.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_volume_backup_policies'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_volume_backup_policies.pem'])
            config_file = 'tests/resources/config_for_test_list_volume_backup_policies'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_backup_policy_group.command_name', 'volume_backup_policy')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVolumeBackupPolicies')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListVolumeBackupPolicies', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_volume_backup_policies.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListVolumeBackupPolicies. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_volume_backup_policies.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_volume_backup_policies.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListVolumeBackupPolicies',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_volume_backup_policies.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_volume_backup_policies.pem')
                if os.path.exists('tests/resources/config_for_test_list_volume_backup_policies'):
                    os.remove('tests/resources/config_for_test_list_volume_backup_policies')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVolumeBackupPolicies')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_volume_backups(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListVolumeBackups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'ListVolumeBackups')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_volume_backups.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_volume_backups', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_volume_backups.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_volume_backups'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_volume_backups.pem'])
            config_file = 'tests/resources/config_for_test_list_volume_backups'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_backup_group.command_name', 'volume_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVolumeBackups')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListVolumeBackups', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_volume_backups.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListVolumeBackups. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_volume_backups.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_volume_backups.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListVolumeBackups',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_volume_backups.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_volume_backups.pem')
                if os.path.exists('tests/resources/config_for_test_list_volume_backups'):
                    os.remove('tests/resources/config_for_test_list_volume_backups')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVolumeBackups')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_volume_group_backups(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListVolumeGroupBackups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'ListVolumeGroupBackups')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_volume_group_backups.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_volume_group_backups', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_volume_group_backups.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_volume_group_backups'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_volume_group_backups.pem'])
            config_file = 'tests/resources/config_for_test_list_volume_group_backups'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group_backup_group.command_name', 'volume_group_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVolumeGroupBackups')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListVolumeGroupBackups', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_volume_group_backups.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListVolumeGroupBackups. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_volume_group_backups.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_volume_group_backups.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListVolumeGroupBackups',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_volume_group_backups.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_volume_group_backups.pem')
                if os.path.exists('tests/resources/config_for_test_list_volume_group_backups'):
                    os.remove('tests/resources/config_for_test_list_volume_group_backups')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVolumeGroupBackups')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_volume_groups(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListVolumeGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'ListVolumeGroups')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_volume_groups.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_volume_groups', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_volume_groups.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_volume_groups'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_volume_groups.pem'])
            config_file = 'tests/resources/config_for_test_list_volume_groups'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group_group.command_name', 'volume_group')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVolumeGroups')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListVolumeGroups', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_volume_groups.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListVolumeGroups. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_volume_groups.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_volume_groups.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListVolumeGroups',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_volume_groups.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_volume_groups.pem')
                if os.path.exists('tests/resources/config_for_test_list_volume_groups'):
                    os.remove('tests/resources/config_for_test_list_volume_groups')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVolumeGroups')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_volumes(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListVolumes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'ListVolumes')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_volumes.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_volumes', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_volumes.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_volumes'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_volumes.pem'])
            config_file = 'tests/resources/config_for_test_list_volumes'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group.command_name', 'volume')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVolumes')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListVolumes', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_volumes.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListVolumes. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_volumes.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_volumes.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListVolumes',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_volumes.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_volumes.pem')
                if os.path.exists('tests/resources/config_for_test_list_volumes'):
                    os.remove('tests/resources/config_for_test_list_volumes')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVolumes')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_boot_volume(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateBootVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'UpdateBootVolume')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_boot_volume.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_boot_volume', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_boot_volume.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_boot_volume'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_boot_volume.pem'])
            config_file = 'tests/resources/config_for_test_update_boot_volume'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('boot_volume_group.command_name', 'boot_volume')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateBootVolume')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateBootVolumeDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateBootVolume', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_boot_volume.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateBootVolume. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_boot_volume.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_boot_volume.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateBootVolume',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'bootVolume',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_boot_volume.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_boot_volume.pem')
                if os.path.exists('tests/resources/config_for_test_update_boot_volume'):
                    os.remove('tests/resources/config_for_test_update_boot_volume')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateBootVolume')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_boot_volume_backup(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateBootVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'UpdateBootVolumeBackup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_boot_volume_backup.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_boot_volume_backup', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_boot_volume_backup.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_boot_volume_backup'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_boot_volume_backup.pem'])
            config_file = 'tests/resources/config_for_test_update_boot_volume_backup'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('boot_volume_backup_group.command_name', 'boot_volume_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateBootVolumeBackup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateBootVolumeBackupDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateBootVolumeBackup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_boot_volume_backup.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateBootVolumeBackup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_boot_volume_backup.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_boot_volume_backup.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateBootVolumeBackup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'bootVolumeBackup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_boot_volume_backup.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_boot_volume_backup.pem')
                if os.path.exists('tests/resources/config_for_test_update_boot_volume_backup'):
                    os.remove('tests/resources/config_for_test_update_boot_volume_backup')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateBootVolumeBackup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_boot_volume_kms_key(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateBootVolumeKmsKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'UpdateBootVolumeKmsKey')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_boot_volume_kms_key.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_boot_volume_kms_key', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_boot_volume_kms_key.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_boot_volume_kms_key'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_boot_volume_kms_key.pem'])
            config_file = 'tests/resources/config_for_test_update_boot_volume_kms_key'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('boot_volume_kms_key_group.command_name', 'boot_volume_kms_key')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateBootVolumeKmsKey')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateBootVolumeKmsKeyDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateBootVolumeKmsKey', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_boot_volume_kms_key.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateBootVolumeKmsKey. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_boot_volume_kms_key.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_boot_volume_kms_key.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateBootVolumeKmsKey',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'bootVolumeKmsKey',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_boot_volume_kms_key.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_boot_volume_kms_key.pem')
                if os.path.exists('tests/resources/config_for_test_update_boot_volume_kms_key'):
                    os.remove('tests/resources/config_for_test_update_boot_volume_kms_key')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateBootVolumeKmsKey')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_volume(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'UpdateVolume')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_volume.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_volume', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_volume.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_volume'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_volume.pem'])
            config_file = 'tests/resources/config_for_test_update_volume'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group.command_name', 'volume')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVolume')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateVolumeDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateVolume', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_volume.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateVolume. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_volume.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_volume.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateVolume',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volume',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_volume.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_volume.pem')
                if os.path.exists('tests/resources/config_for_test_update_volume'):
                    os.remove('tests/resources/config_for_test_update_volume')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVolume')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_volume_backup(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'UpdateVolumeBackup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_volume_backup.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_volume_backup', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_volume_backup.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_volume_backup'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_volume_backup.pem'])
            config_file = 'tests/resources/config_for_test_update_volume_backup'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_backup_group.command_name', 'volume_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVolumeBackup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateVolumeBackupDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateVolumeBackup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_volume_backup.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateVolumeBackup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_volume_backup.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_volume_backup.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateVolumeBackup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volumeBackup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_volume_backup.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_volume_backup.pem')
                if os.path.exists('tests/resources/config_for_test_update_volume_backup'):
                    os.remove('tests/resources/config_for_test_update_volume_backup')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVolumeBackup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_volume_group(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateVolumeGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'UpdateVolumeGroup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_volume_group.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_volume_group', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_volume_group.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_volume_group'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_volume_group.pem'])
            config_file = 'tests/resources/config_for_test_update_volume_group'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group_group.command_name', 'volume_group')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVolumeGroup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateVolumeGroupDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateVolumeGroup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_volume_group.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateVolumeGroup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_volume_group.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_volume_group.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateVolumeGroup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volumeGroup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_volume_group.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_volume_group.pem')
                if os.path.exists('tests/resources/config_for_test_update_volume_group'):
                    os.remove('tests/resources/config_for_test_update_volume_group')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVolumeGroup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_volume_group_backup(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateVolumeGroupBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'UpdateVolumeGroupBackup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_volume_group_backup.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_volume_group_backup', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_volume_group_backup.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_volume_group_backup'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_volume_group_backup.pem'])
            config_file = 'tests/resources/config_for_test_update_volume_group_backup'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_group_backup_group.command_name', 'volume_group_backup')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVolumeGroupBackup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateVolumeGroupBackupDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateVolumeGroupBackup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_volume_group_backup.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateVolumeGroupBackup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_volume_group_backup.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_volume_group_backup.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateVolumeGroupBackup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volumeGroupBackup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_volume_group_backup.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_volume_group_backup.pem')
                if os.path.exists('tests/resources/config_for_test_update_volume_group_backup'):
                    os.remove('tests/resources/config_for_test_update_volume_group_backup')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVolumeGroupBackup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_volume_kms_key(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateVolumeKmsKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'Blockstorage', 'UpdateVolumeKmsKey')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_volume_kms_key.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_volume_kms_key', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_volume_kms_key.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_volume_kms_key'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_volume_kms_key.pem'])
            config_file = 'tests/resources/config_for_test_update_volume_kms_key'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('blockstorage_root_group.command_name', 'blockstorage')
    resource_group_command_name = oci_cli.cli_util.override('volume_kms_key_group.command_name', 'volume_kms_key')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVolumeKmsKey')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateVolumeKmsKeyDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateVolumeKmsKey', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_volume_kms_key.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateVolumeKmsKey. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_volume_kms_key.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_volume_kms_key.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateVolumeKmsKey',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'volumeKmsKey',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_volume_kms_key.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_volume_kms_key.pem')
                if os.path.exists('tests/resources/config_for_test_update_volume_kms_key'):
                    os.remove('tests/resources/config_for_test_update_volume_kms_key')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVolumeKmsKey')
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
