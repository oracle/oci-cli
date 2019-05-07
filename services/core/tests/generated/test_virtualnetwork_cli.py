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
def test_attach_service_id(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'AttachServiceId'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'AttachServiceId')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_attach_service_id.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_attach_service_id', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_attach_service_id.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_attach_service_id'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_attach_service_id.pem'])
            config_file = 'tests/resources/config_for_test_attach_service_id'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('service_gateway_group.command_name', 'service_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='AttachServiceId')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'AttachServiceDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'AttachServiceId', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('attach_service_id.command_name', 'attach'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, AttachServiceId. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('attach_service_id.command_name', 'attach'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('attach_service_id.command_name', 'attach')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'AttachServiceId',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'serviceGateway',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_attach_service_id.pem'):
                    os.remove('tests/resources/keyfile_for_test_attach_service_id.pem')
                if os.path.exists('tests/resources/config_for_test_attach_service_id'):
                    os.remove('tests/resources/config_for_test_attach_service_id')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='AttachServiceId')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_bulk_add_virtual_circuit_public_prefixes(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'BulkAddVirtualCircuitPublicPrefixes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'BulkAddVirtualCircuitPublicPrefixes')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_bulk_add_virtual_circuit_public_prefixes.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_bulk_add_virtual_circuit_public_prefixes', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_bulk_add_virtual_circuit_public_prefixes.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_bulk_add_virtual_circuit_public_prefixes'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_bulk_add_virtual_circuit_public_prefixes.pem'])
            config_file = 'tests/resources/config_for_test_bulk_add_virtual_circuit_public_prefixes'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('virtual_circuit_public_prefix_group.command_name', 'virtual_circuit_public_prefix')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='BulkAddVirtualCircuitPublicPrefixes')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'BulkAddVirtualCircuitPublicPrefixesDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'BulkAddVirtualCircuitPublicPrefixes', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('bulk_add_virtual_circuit_public_prefixes.command_name', 'bulk-add'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, BulkAddVirtualCircuitPublicPrefixes. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('bulk_add_virtual_circuit_public_prefixes.command_name', 'bulk-add'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('bulk_add_virtual_circuit_public_prefixes.command_name', 'bulk-add')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'BulkAddVirtualCircuitPublicPrefixes',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'bulkAddVirtualCircuitPublicPrefixes',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_bulk_add_virtual_circuit_public_prefixes.pem'):
                    os.remove('tests/resources/keyfile_for_test_bulk_add_virtual_circuit_public_prefixes.pem')
                if os.path.exists('tests/resources/config_for_test_bulk_add_virtual_circuit_public_prefixes'):
                    os.remove('tests/resources/config_for_test_bulk_add_virtual_circuit_public_prefixes')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='BulkAddVirtualCircuitPublicPrefixes')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_bulk_delete_virtual_circuit_public_prefixes(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'BulkDeleteVirtualCircuitPublicPrefixes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'BulkDeleteVirtualCircuitPublicPrefixes')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_bulk_delete_virtual_circuit_public_prefixes.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_bulk_delete_virtual_circuit_public_prefixes', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_bulk_delete_virtual_circuit_public_prefixes.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_bulk_delete_virtual_circuit_public_prefixes'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_bulk_delete_virtual_circuit_public_prefixes.pem'])
            config_file = 'tests/resources/config_for_test_bulk_delete_virtual_circuit_public_prefixes'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('virtual_circuit_public_prefix_group.command_name', 'virtual_circuit_public_prefix')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='BulkDeleteVirtualCircuitPublicPrefixes')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'BulkDeleteVirtualCircuitPublicPrefixesDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'BulkDeleteVirtualCircuitPublicPrefixes', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('bulk_delete_virtual_circuit_public_prefixes.command_name', 'bulk-delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, BulkDeleteVirtualCircuitPublicPrefixes. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('bulk_delete_virtual_circuit_public_prefixes.command_name', 'bulk-delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('bulk_delete_virtual_circuit_public_prefixes.command_name', 'bulk-delete')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'BulkDeleteVirtualCircuitPublicPrefixes',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'bulkDeleteVirtualCircuitPublicPrefixes',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_bulk_delete_virtual_circuit_public_prefixes.pem'):
                    os.remove('tests/resources/keyfile_for_test_bulk_delete_virtual_circuit_public_prefixes.pem')
                if os.path.exists('tests/resources/config_for_test_bulk_delete_virtual_circuit_public_prefixes'):
                    os.remove('tests/resources/config_for_test_bulk_delete_virtual_circuit_public_prefixes')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='BulkDeleteVirtualCircuitPublicPrefixes')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_connect_local_peering_gateways(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ConnectLocalPeeringGateways'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ConnectLocalPeeringGateways')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_connect_local_peering_gateways.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_connect_local_peering_gateways', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_connect_local_peering_gateways.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_connect_local_peering_gateways'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_connect_local_peering_gateways.pem'])
            config_file = 'tests/resources/config_for_test_connect_local_peering_gateways'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('local_peering_gateway_group.command_name', 'local_peering_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ConnectLocalPeeringGateways')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'ConnectLocalPeeringGatewaysDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ConnectLocalPeeringGateways', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('connect_local_peering_gateways.command_name', 'connect'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ConnectLocalPeeringGateways. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('connect_local_peering_gateways.command_name', 'connect'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('connect_local_peering_gateways.command_name', 'connect')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ConnectLocalPeeringGateways',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'connectLocalPeeringGateways',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_connect_local_peering_gateways.pem'):
                    os.remove('tests/resources/keyfile_for_test_connect_local_peering_gateways.pem')
                if os.path.exists('tests/resources/config_for_test_connect_local_peering_gateways'):
                    os.remove('tests/resources/config_for_test_connect_local_peering_gateways')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ConnectLocalPeeringGateways')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_connect_remote_peering_connections(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ConnectRemotePeeringConnections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ConnectRemotePeeringConnections')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_connect_remote_peering_connections.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_connect_remote_peering_connections', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_connect_remote_peering_connections.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_connect_remote_peering_connections'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_connect_remote_peering_connections.pem'])
            config_file = 'tests/resources/config_for_test_connect_remote_peering_connections'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('remote_peering_connection_group.command_name', 'remote_peering_connection')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ConnectRemotePeeringConnections')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'ConnectRemotePeeringConnectionsDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ConnectRemotePeeringConnections', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('connect_remote_peering_connections.command_name', 'connect'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ConnectRemotePeeringConnections. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('connect_remote_peering_connections.command_name', 'connect'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('connect_remote_peering_connections.command_name', 'connect')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ConnectRemotePeeringConnections',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'connectRemotePeeringConnections',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_connect_remote_peering_connections.pem'):
                    os.remove('tests/resources/keyfile_for_test_connect_remote_peering_connections.pem')
                if os.path.exists('tests/resources/config_for_test_connect_remote_peering_connections'):
                    os.remove('tests/resources/config_for_test_connect_remote_peering_connections')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ConnectRemotePeeringConnections')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_cpe(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateCpe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateCpe')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_cpe.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_cpe', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_cpe.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_cpe'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_cpe.pem'])
            config_file = 'tests/resources/config_for_test_create_cpe'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cpe_group.command_name', 'cpe')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateCpe')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateCpeDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateCpe', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_cpe.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateCpe. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_cpe.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_cpe.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateCpe',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'cpe',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_cpe.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_cpe.pem')
                if os.path.exists('tests/resources/config_for_test_create_cpe'):
                    os.remove('tests/resources/config_for_test_create_cpe')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateCpe')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_cross_connect(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateCrossConnect'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateCrossConnect')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_cross_connect.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_cross_connect', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_cross_connect.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_cross_connect'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_cross_connect.pem'])
            config_file = 'tests/resources/config_for_test_create_cross_connect'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cross_connect_group.command_name', 'cross_connect')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateCrossConnect')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateCrossConnectDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateCrossConnect', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_cross_connect.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateCrossConnect. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_cross_connect.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_cross_connect.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateCrossConnect',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'crossConnect',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_cross_connect.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_cross_connect.pem')
                if os.path.exists('tests/resources/config_for_test_create_cross_connect'):
                    os.remove('tests/resources/config_for_test_create_cross_connect')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateCrossConnect')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_cross_connect_group(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateCrossConnectGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateCrossConnectGroup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_cross_connect_group.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_cross_connect_group', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_cross_connect_group.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_cross_connect_group'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_cross_connect_group.pem'])
            config_file = 'tests/resources/config_for_test_create_cross_connect_group'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cross_connect_group_group.command_name', 'cross_connect_group')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateCrossConnectGroup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateCrossConnectGroupDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateCrossConnectGroup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_cross_connect_group.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateCrossConnectGroup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_cross_connect_group.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_cross_connect_group.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateCrossConnectGroup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'crossConnectGroup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_cross_connect_group.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_cross_connect_group.pem')
                if os.path.exists('tests/resources/config_for_test_create_cross_connect_group'):
                    os.remove('tests/resources/config_for_test_create_cross_connect_group')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateCrossConnectGroup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_dhcp_options(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateDhcpOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateDhcpOptions')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_dhcp_options.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_dhcp_options', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_dhcp_options.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_dhcp_options'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_dhcp_options.pem'])
            config_file = 'tests/resources/config_for_test_create_dhcp_options'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('dhcp_options_group.command_name', 'dhcp_options')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateDhcpOptions')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateDhcpDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateDhcpOptions', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_dhcp_options.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateDhcpOptions. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_dhcp_options.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_dhcp_options.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateDhcpOptions',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'dhcpOptions',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_dhcp_options.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_dhcp_options.pem')
                if os.path.exists('tests/resources/config_for_test_create_dhcp_options'):
                    os.remove('tests/resources/config_for_test_create_dhcp_options')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateDhcpOptions')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_drg(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateDrg'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateDrg')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_drg.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_drg', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_drg.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_drg'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_drg.pem'])
            config_file = 'tests/resources/config_for_test_create_drg'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('drg_group.command_name', 'drg')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateDrg')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateDrgDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateDrg', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_drg.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateDrg. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_drg.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_drg.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateDrg',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'drg',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_drg.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_drg.pem')
                if os.path.exists('tests/resources/config_for_test_create_drg'):
                    os.remove('tests/resources/config_for_test_create_drg')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateDrg')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_drg_attachment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateDrgAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateDrgAttachment')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_drg_attachment.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_drg_attachment', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_drg_attachment.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_drg_attachment'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_drg_attachment.pem'])
            config_file = 'tests/resources/config_for_test_create_drg_attachment'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('drg_attachment_group.command_name', 'drg_attachment')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateDrgAttachment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateDrgAttachmentDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateDrgAttachment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_drg_attachment.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateDrgAttachment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_drg_attachment.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_drg_attachment.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateDrgAttachment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'drgAttachment',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_drg_attachment.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_drg_attachment.pem')
                if os.path.exists('tests/resources/config_for_test_create_drg_attachment'):
                    os.remove('tests/resources/config_for_test_create_drg_attachment')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateDrgAttachment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_internet_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateInternetGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateInternetGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_internet_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_internet_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_internet_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_internet_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_internet_gateway.pem'])
            config_file = 'tests/resources/config_for_test_create_internet_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('internet_gateway_group.command_name', 'internet_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateInternetGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateInternetGatewayDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateInternetGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_internet_gateway.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateInternetGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_internet_gateway.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_internet_gateway.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateInternetGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'internetGateway',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_internet_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_internet_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_create_internet_gateway'):
                    os.remove('tests/resources/config_for_test_create_internet_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateInternetGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_ip_sec_connection(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateIPSecConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateIPSecConnection')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_ip_sec_connection.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_ip_sec_connection', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_ip_sec_connection.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_ip_sec_connection'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_ip_sec_connection.pem'])
            config_file = 'tests/resources/config_for_test_create_ip_sec_connection'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('ip_sec_connection_group.command_name', 'ip_sec_connection')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateIPSecConnection')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateIPSecConnectionDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateIPSecConnection', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_ip_sec_connection.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateIPSecConnection. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_ip_sec_connection.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_ip_sec_connection.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateIPSecConnection',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'iPSecConnection',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_ip_sec_connection.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_ip_sec_connection.pem')
                if os.path.exists('tests/resources/config_for_test_create_ip_sec_connection'):
                    os.remove('tests/resources/config_for_test_create_ip_sec_connection')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateIPSecConnection')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_local_peering_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateLocalPeeringGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateLocalPeeringGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_local_peering_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_local_peering_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_local_peering_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_local_peering_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_local_peering_gateway.pem'])
            config_file = 'tests/resources/config_for_test_create_local_peering_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('local_peering_gateway_group.command_name', 'local_peering_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateLocalPeeringGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateLocalPeeringGatewayDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateLocalPeeringGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_local_peering_gateway.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateLocalPeeringGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_local_peering_gateway.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_local_peering_gateway.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateLocalPeeringGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'localPeeringGateway',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_local_peering_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_local_peering_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_create_local_peering_gateway'):
                    os.remove('tests/resources/config_for_test_create_local_peering_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateLocalPeeringGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_nat_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateNatGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateNatGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_nat_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_nat_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_nat_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_nat_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_nat_gateway.pem'])
            config_file = 'tests/resources/config_for_test_create_nat_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('nat_gateway_group.command_name', 'nat_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateNatGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateNatGatewayDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateNatGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_nat_gateway.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateNatGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_nat_gateway.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_nat_gateway.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateNatGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'natGateway',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_nat_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_nat_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_create_nat_gateway'):
                    os.remove('tests/resources/config_for_test_create_nat_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateNatGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_private_ip(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreatePrivateIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreatePrivateIp')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_private_ip.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_private_ip', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_private_ip.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_private_ip'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_private_ip.pem'])
            config_file = 'tests/resources/config_for_test_create_private_ip'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('private_ip_group.command_name', 'private_ip')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreatePrivateIp')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreatePrivateIpDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreatePrivateIp', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_private_ip.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreatePrivateIp. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_private_ip.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_private_ip.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreatePrivateIp',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'privateIp',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_private_ip.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_private_ip.pem')
                if os.path.exists('tests/resources/config_for_test_create_private_ip'):
                    os.remove('tests/resources/config_for_test_create_private_ip')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreatePrivateIp')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_public_ip(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreatePublicIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreatePublicIp')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_public_ip.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_public_ip', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_public_ip.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_public_ip'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_public_ip.pem'])
            config_file = 'tests/resources/config_for_test_create_public_ip'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('public_ip_group.command_name', 'public_ip')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreatePublicIp')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreatePublicIpDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreatePublicIp', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_public_ip.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreatePublicIp. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_public_ip.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_public_ip.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreatePublicIp',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'publicIp',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_public_ip.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_public_ip.pem')
                if os.path.exists('tests/resources/config_for_test_create_public_ip'):
                    os.remove('tests/resources/config_for_test_create_public_ip')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreatePublicIp')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_remote_peering_connection(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateRemotePeeringConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateRemotePeeringConnection')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_remote_peering_connection.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_remote_peering_connection', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_remote_peering_connection.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_remote_peering_connection'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_remote_peering_connection.pem'])
            config_file = 'tests/resources/config_for_test_create_remote_peering_connection'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('remote_peering_connection_group.command_name', 'remote_peering_connection')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateRemotePeeringConnection')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateRemotePeeringConnectionDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateRemotePeeringConnection', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_remote_peering_connection.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateRemotePeeringConnection. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_remote_peering_connection.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_remote_peering_connection.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateRemotePeeringConnection',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'remotePeeringConnection',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_remote_peering_connection.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_remote_peering_connection.pem')
                if os.path.exists('tests/resources/config_for_test_create_remote_peering_connection'):
                    os.remove('tests/resources/config_for_test_create_remote_peering_connection')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateRemotePeeringConnection')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_route_table(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateRouteTable')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_route_table.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_route_table', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_route_table.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_route_table'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_route_table.pem'])
            config_file = 'tests/resources/config_for_test_create_route_table'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('route_table_group.command_name', 'route_table')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateRouteTable')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateRouteTableDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateRouteTable', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_route_table.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateRouteTable. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_route_table.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_route_table.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateRouteTable',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'routeTable',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_route_table.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_route_table.pem')
                if os.path.exists('tests/resources/config_for_test_create_route_table'):
                    os.remove('tests/resources/config_for_test_create_route_table')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateRouteTable')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_security_list(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateSecurityList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateSecurityList')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_security_list.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_security_list', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_security_list.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_security_list'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_security_list.pem'])
            config_file = 'tests/resources/config_for_test_create_security_list'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('security_list_group.command_name', 'security_list')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateSecurityList')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateSecurityListDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateSecurityList', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_security_list.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateSecurityList. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_security_list.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_security_list.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateSecurityList',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'securityList',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_security_list.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_security_list.pem')
                if os.path.exists('tests/resources/config_for_test_create_security_list'):
                    os.remove('tests/resources/config_for_test_create_security_list')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateSecurityList')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_service_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateServiceGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateServiceGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_service_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_service_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_service_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_service_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_service_gateway.pem'])
            config_file = 'tests/resources/config_for_test_create_service_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('service_gateway_group.command_name', 'service_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateServiceGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateServiceGatewayDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateServiceGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_service_gateway.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateServiceGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_service_gateway.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_service_gateway.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateServiceGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'serviceGateway',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_service_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_service_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_create_service_gateway'):
                    os.remove('tests/resources/config_for_test_create_service_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateServiceGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_subnet(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateSubnet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateSubnet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_subnet.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_subnet', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_subnet.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_subnet'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_subnet.pem'])
            config_file = 'tests/resources/config_for_test_create_subnet'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('subnet_group.command_name', 'subnet')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateSubnet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateSubnetDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateSubnet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_subnet.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateSubnet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_subnet.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_subnet.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateSubnet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'subnet',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_subnet.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_subnet.pem')
                if os.path.exists('tests/resources/config_for_test_create_subnet'):
                    os.remove('tests/resources/config_for_test_create_subnet')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateSubnet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_vcn(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateVcn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateVcn')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_vcn.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_vcn', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_vcn.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_vcn'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_vcn.pem'])
            config_file = 'tests/resources/config_for_test_create_vcn'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('vcn_group.command_name', 'vcn')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateVcn')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateVcnDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateVcn', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_vcn.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateVcn. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_vcn.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_vcn.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateVcn',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'vcn',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_vcn.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_vcn.pem')
                if os.path.exists('tests/resources/config_for_test_create_vcn'):
                    os.remove('tests/resources/config_for_test_create_vcn')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateVcn')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_virtual_circuit(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateVirtualCircuit'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'CreateVirtualCircuit')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_virtual_circuit.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_virtual_circuit', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_virtual_circuit.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_virtual_circuit'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_virtual_circuit.pem'])
            config_file = 'tests/resources/config_for_test_create_virtual_circuit'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('virtual_circuit_group.command_name', 'virtual_circuit')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateVirtualCircuit')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateVirtualCircuitDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateVirtualCircuit', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_virtual_circuit.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateVirtualCircuit. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_virtual_circuit.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_virtual_circuit.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateVirtualCircuit',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'virtualCircuit',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_virtual_circuit.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_virtual_circuit.pem')
                if os.path.exists('tests/resources/config_for_test_create_virtual_circuit'):
                    os.remove('tests/resources/config_for_test_create_virtual_circuit')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateVirtualCircuit')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_cpe(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteCpe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteCpe')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_cpe.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_cpe', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_cpe.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_cpe'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_cpe.pem'])
            config_file = 'tests/resources/config_for_test_delete_cpe'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cpe_group.command_name', 'cpe')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteCpe')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteCpe', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_cpe.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteCpe. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_cpe.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_cpe.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteCpe',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteCpe',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_cpe.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_cpe.pem')
                if os.path.exists('tests/resources/config_for_test_delete_cpe'):
                    os.remove('tests/resources/config_for_test_delete_cpe')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteCpe')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_cross_connect(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteCrossConnect'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteCrossConnect')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_cross_connect.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_cross_connect', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_cross_connect.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_cross_connect'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_cross_connect.pem'])
            config_file = 'tests/resources/config_for_test_delete_cross_connect'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cross_connect_group.command_name', 'cross_connect')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteCrossConnect')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteCrossConnect', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_cross_connect.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteCrossConnect. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_cross_connect.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_cross_connect.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteCrossConnect',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteCrossConnect',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_cross_connect.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_cross_connect.pem')
                if os.path.exists('tests/resources/config_for_test_delete_cross_connect'):
                    os.remove('tests/resources/config_for_test_delete_cross_connect')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteCrossConnect')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_cross_connect_group(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteCrossConnectGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteCrossConnectGroup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_cross_connect_group.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_cross_connect_group', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_cross_connect_group.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_cross_connect_group'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_cross_connect_group.pem'])
            config_file = 'tests/resources/config_for_test_delete_cross_connect_group'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cross_connect_group_group.command_name', 'cross_connect_group')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteCrossConnectGroup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteCrossConnectGroup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_cross_connect_group.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteCrossConnectGroup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_cross_connect_group.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_cross_connect_group.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteCrossConnectGroup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteCrossConnectGroup',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_cross_connect_group.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_cross_connect_group.pem')
                if os.path.exists('tests/resources/config_for_test_delete_cross_connect_group'):
                    os.remove('tests/resources/config_for_test_delete_cross_connect_group')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteCrossConnectGroup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_dhcp_options(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteDhcpOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteDhcpOptions')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_dhcp_options.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_dhcp_options', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_dhcp_options.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_dhcp_options'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_dhcp_options.pem'])
            config_file = 'tests/resources/config_for_test_delete_dhcp_options'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('dhcp_options_group.command_name', 'dhcp_options')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteDhcpOptions')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteDhcpOptions', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_dhcp_options.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteDhcpOptions. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_dhcp_options.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_dhcp_options.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteDhcpOptions',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteDhcpOptions',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_dhcp_options.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_dhcp_options.pem')
                if os.path.exists('tests/resources/config_for_test_delete_dhcp_options'):
                    os.remove('tests/resources/config_for_test_delete_dhcp_options')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteDhcpOptions')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_drg(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteDrg'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteDrg')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_drg.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_drg', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_drg.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_drg'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_drg.pem'])
            config_file = 'tests/resources/config_for_test_delete_drg'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('drg_group.command_name', 'drg')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteDrg')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteDrg', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_drg.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteDrg. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_drg.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_drg.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteDrg',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteDrg',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_drg.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_drg.pem')
                if os.path.exists('tests/resources/config_for_test_delete_drg'):
                    os.remove('tests/resources/config_for_test_delete_drg')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteDrg')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_drg_attachment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteDrgAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteDrgAttachment')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_drg_attachment.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_drg_attachment', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_drg_attachment.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_drg_attachment'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_drg_attachment.pem'])
            config_file = 'tests/resources/config_for_test_delete_drg_attachment'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('drg_attachment_group.command_name', 'drg_attachment')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteDrgAttachment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteDrgAttachment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_drg_attachment.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteDrgAttachment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_drg_attachment.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_drg_attachment.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteDrgAttachment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteDrgAttachment',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_drg_attachment.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_drg_attachment.pem')
                if os.path.exists('tests/resources/config_for_test_delete_drg_attachment'):
                    os.remove('tests/resources/config_for_test_delete_drg_attachment')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteDrgAttachment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_internet_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteInternetGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteInternetGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_internet_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_internet_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_internet_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_internet_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_internet_gateway.pem'])
            config_file = 'tests/resources/config_for_test_delete_internet_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('internet_gateway_group.command_name', 'internet_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteInternetGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteInternetGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_internet_gateway.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteInternetGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_internet_gateway.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_internet_gateway.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteInternetGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteInternetGateway',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_internet_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_internet_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_delete_internet_gateway'):
                    os.remove('tests/resources/config_for_test_delete_internet_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteInternetGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_ip_sec_connection(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteIPSecConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteIPSecConnection')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_ip_sec_connection.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_ip_sec_connection', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_ip_sec_connection.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_ip_sec_connection'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_ip_sec_connection.pem'])
            config_file = 'tests/resources/config_for_test_delete_ip_sec_connection'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('ip_sec_connection_group.command_name', 'ip_sec_connection')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteIPSecConnection')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteIPSecConnection', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_ip_sec_connection.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteIPSecConnection. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_ip_sec_connection.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_ip_sec_connection.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteIPSecConnection',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteIPSecConnection',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_ip_sec_connection.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_ip_sec_connection.pem')
                if os.path.exists('tests/resources/config_for_test_delete_ip_sec_connection'):
                    os.remove('tests/resources/config_for_test_delete_ip_sec_connection')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteIPSecConnection')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_local_peering_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteLocalPeeringGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteLocalPeeringGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_local_peering_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_local_peering_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_local_peering_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_local_peering_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_local_peering_gateway.pem'])
            config_file = 'tests/resources/config_for_test_delete_local_peering_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('local_peering_gateway_group.command_name', 'local_peering_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteLocalPeeringGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteLocalPeeringGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_local_peering_gateway.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteLocalPeeringGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_local_peering_gateway.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_local_peering_gateway.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteLocalPeeringGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteLocalPeeringGateway',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_local_peering_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_local_peering_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_delete_local_peering_gateway'):
                    os.remove('tests/resources/config_for_test_delete_local_peering_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteLocalPeeringGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_nat_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteNatGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteNatGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_nat_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_nat_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_nat_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_nat_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_nat_gateway.pem'])
            config_file = 'tests/resources/config_for_test_delete_nat_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('nat_gateway_group.command_name', 'nat_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteNatGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteNatGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_nat_gateway.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteNatGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_nat_gateway.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_nat_gateway.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteNatGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteNatGateway',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_nat_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_nat_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_delete_nat_gateway'):
                    os.remove('tests/resources/config_for_test_delete_nat_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteNatGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_private_ip(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeletePrivateIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeletePrivateIp')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_private_ip.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_private_ip', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_private_ip.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_private_ip'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_private_ip.pem'])
            config_file = 'tests/resources/config_for_test_delete_private_ip'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('private_ip_group.command_name', 'private_ip')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeletePrivateIp')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeletePrivateIp', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_private_ip.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeletePrivateIp. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_private_ip.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_private_ip.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeletePrivateIp',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deletePrivateIp',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_private_ip.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_private_ip.pem')
                if os.path.exists('tests/resources/config_for_test_delete_private_ip'):
                    os.remove('tests/resources/config_for_test_delete_private_ip')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeletePrivateIp')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_public_ip(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeletePublicIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeletePublicIp')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_public_ip.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_public_ip', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_public_ip.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_public_ip'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_public_ip.pem'])
            config_file = 'tests/resources/config_for_test_delete_public_ip'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('public_ip_group.command_name', 'public_ip')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeletePublicIp')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeletePublicIp', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_public_ip.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeletePublicIp. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_public_ip.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_public_ip.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeletePublicIp',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deletePublicIp',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_public_ip.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_public_ip.pem')
                if os.path.exists('tests/resources/config_for_test_delete_public_ip'):
                    os.remove('tests/resources/config_for_test_delete_public_ip')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeletePublicIp')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_remote_peering_connection(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteRemotePeeringConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteRemotePeeringConnection')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_remote_peering_connection.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_remote_peering_connection', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_remote_peering_connection.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_remote_peering_connection'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_remote_peering_connection.pem'])
            config_file = 'tests/resources/config_for_test_delete_remote_peering_connection'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('remote_peering_connection_group.command_name', 'remote_peering_connection')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteRemotePeeringConnection')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteRemotePeeringConnection', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_remote_peering_connection.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteRemotePeeringConnection. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_remote_peering_connection.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_remote_peering_connection.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteRemotePeeringConnection',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteRemotePeeringConnection',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_remote_peering_connection.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_remote_peering_connection.pem')
                if os.path.exists('tests/resources/config_for_test_delete_remote_peering_connection'):
                    os.remove('tests/resources/config_for_test_delete_remote_peering_connection')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteRemotePeeringConnection')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_route_table(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteRouteTable')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_route_table.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_route_table', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_route_table.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_route_table'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_route_table.pem'])
            config_file = 'tests/resources/config_for_test_delete_route_table'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('route_table_group.command_name', 'route_table')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteRouteTable')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteRouteTable', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_route_table.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteRouteTable. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_route_table.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_route_table.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteRouteTable',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteRouteTable',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_route_table.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_route_table.pem')
                if os.path.exists('tests/resources/config_for_test_delete_route_table'):
                    os.remove('tests/resources/config_for_test_delete_route_table')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteRouteTable')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_security_list(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteSecurityList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteSecurityList')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_security_list.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_security_list', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_security_list.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_security_list'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_security_list.pem'])
            config_file = 'tests/resources/config_for_test_delete_security_list'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('security_list_group.command_name', 'security_list')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteSecurityList')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteSecurityList', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_security_list.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteSecurityList. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_security_list.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_security_list.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteSecurityList',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteSecurityList',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_security_list.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_security_list.pem')
                if os.path.exists('tests/resources/config_for_test_delete_security_list'):
                    os.remove('tests/resources/config_for_test_delete_security_list')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteSecurityList')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_service_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteServiceGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteServiceGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_service_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_service_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_service_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_service_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_service_gateway.pem'])
            config_file = 'tests/resources/config_for_test_delete_service_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('service_gateway_group.command_name', 'service_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteServiceGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteServiceGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_service_gateway.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteServiceGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_service_gateway.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_service_gateway.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteServiceGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteServiceGateway',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_service_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_service_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_delete_service_gateway'):
                    os.remove('tests/resources/config_for_test_delete_service_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteServiceGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_subnet(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteSubnet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteSubnet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_subnet.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_subnet', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_subnet.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_subnet'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_subnet.pem'])
            config_file = 'tests/resources/config_for_test_delete_subnet'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('subnet_group.command_name', 'subnet')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteSubnet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteSubnet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_subnet.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteSubnet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_subnet.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_subnet.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteSubnet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteSubnet',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_subnet.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_subnet.pem')
                if os.path.exists('tests/resources/config_for_test_delete_subnet'):
                    os.remove('tests/resources/config_for_test_delete_subnet')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteSubnet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_vcn(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteVcn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteVcn')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_vcn.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_vcn', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_vcn.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_vcn'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_vcn.pem'])
            config_file = 'tests/resources/config_for_test_delete_vcn'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('vcn_group.command_name', 'vcn')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVcn')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteVcn', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_vcn.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteVcn. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_vcn.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_vcn.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteVcn',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteVcn',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_vcn.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_vcn.pem')
                if os.path.exists('tests/resources/config_for_test_delete_vcn'):
                    os.remove('tests/resources/config_for_test_delete_vcn')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVcn')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_virtual_circuit(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteVirtualCircuit'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DeleteVirtualCircuit')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_virtual_circuit.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_virtual_circuit', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_virtual_circuit.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_virtual_circuit'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_virtual_circuit.pem'])
            config_file = 'tests/resources/config_for_test_delete_virtual_circuit'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('virtual_circuit_group.command_name', 'virtual_circuit')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVirtualCircuit')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteVirtualCircuit', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_virtual_circuit.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteVirtualCircuit. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_virtual_circuit.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_virtual_circuit.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteVirtualCircuit',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteVirtualCircuit',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_virtual_circuit.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_virtual_circuit.pem')
                if os.path.exists('tests/resources/config_for_test_delete_virtual_circuit'):
                    os.remove('tests/resources/config_for_test_delete_virtual_circuit')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteVirtualCircuit')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_detach_service_id(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DetachServiceId'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'DetachServiceId')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_detach_service_id.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_detach_service_id', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_detach_service_id.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_detach_service_id'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_detach_service_id.pem'])
            config_file = 'tests/resources/config_for_test_detach_service_id'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('service_gateway_group.command_name', 'service_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DetachServiceId')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'DetachServiceDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DetachServiceId', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('detach_service_id.command_name', 'detach'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DetachServiceId. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('detach_service_id.command_name', 'detach'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('detach_service_id.command_name', 'detach')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DetachServiceId',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'serviceGateway',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_detach_service_id.pem'):
                    os.remove('tests/resources/keyfile_for_test_detach_service_id.pem')
                if os.path.exists('tests/resources/config_for_test_detach_service_id'):
                    os.remove('tests/resources/config_for_test_detach_service_id')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DetachServiceId')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_cpe(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetCpe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetCpe')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_cpe.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_cpe', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_cpe.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_cpe'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_cpe.pem'])
            config_file = 'tests/resources/config_for_test_get_cpe'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cpe_group.command_name', 'cpe')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetCpe')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetCpe', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_cpe.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetCpe. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_cpe.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_cpe.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetCpe',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'cpe',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_cpe.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_cpe.pem')
                if os.path.exists('tests/resources/config_for_test_get_cpe'):
                    os.remove('tests/resources/config_for_test_get_cpe')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetCpe')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_cross_connect(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetCrossConnect'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetCrossConnect')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_cross_connect.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_cross_connect', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_cross_connect.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_cross_connect'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_cross_connect.pem'])
            config_file = 'tests/resources/config_for_test_get_cross_connect'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cross_connect_group.command_name', 'cross_connect')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetCrossConnect')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetCrossConnect', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_cross_connect.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetCrossConnect. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_cross_connect.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_cross_connect.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetCrossConnect',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'crossConnect',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_cross_connect.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_cross_connect.pem')
                if os.path.exists('tests/resources/config_for_test_get_cross_connect'):
                    os.remove('tests/resources/config_for_test_get_cross_connect')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetCrossConnect')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_cross_connect_group(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetCrossConnectGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetCrossConnectGroup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_cross_connect_group.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_cross_connect_group', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_cross_connect_group.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_cross_connect_group'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_cross_connect_group.pem'])
            config_file = 'tests/resources/config_for_test_get_cross_connect_group'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cross_connect_group_group.command_name', 'cross_connect_group')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetCrossConnectGroup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetCrossConnectGroup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_cross_connect_group.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetCrossConnectGroup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_cross_connect_group.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_cross_connect_group.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetCrossConnectGroup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'crossConnectGroup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_cross_connect_group.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_cross_connect_group.pem')
                if os.path.exists('tests/resources/config_for_test_get_cross_connect_group'):
                    os.remove('tests/resources/config_for_test_get_cross_connect_group')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetCrossConnectGroup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_cross_connect_letter_of_authority(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetCrossConnectLetterOfAuthority'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetCrossConnectLetterOfAuthority')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_cross_connect_letter_of_authority.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_cross_connect_letter_of_authority', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_cross_connect_letter_of_authority.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_cross_connect_letter_of_authority'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_cross_connect_letter_of_authority.pem'])
            config_file = 'tests/resources/config_for_test_get_cross_connect_letter_of_authority'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('letter_of_authority_group.command_name', 'letter_of_authority')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetCrossConnectLetterOfAuthority')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetCrossConnectLetterOfAuthority', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_cross_connect_letter_of_authority.command_name', 'get-cross-connect'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetCrossConnectLetterOfAuthority. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_cross_connect_letter_of_authority.command_name', 'get-cross-connect'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_cross_connect_letter_of_authority.command_name', 'get-cross-connect')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetCrossConnectLetterOfAuthority',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'letterOfAuthority',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_cross_connect_letter_of_authority.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_cross_connect_letter_of_authority.pem')
                if os.path.exists('tests/resources/config_for_test_get_cross_connect_letter_of_authority'):
                    os.remove('tests/resources/config_for_test_get_cross_connect_letter_of_authority')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetCrossConnectLetterOfAuthority')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_cross_connect_status(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetCrossConnectStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetCrossConnectStatus')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_cross_connect_status.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_cross_connect_status', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_cross_connect_status.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_cross_connect_status'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_cross_connect_status.pem'])
            config_file = 'tests/resources/config_for_test_get_cross_connect_status'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cross_connect_status_group.command_name', 'cross_connect_status')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetCrossConnectStatus')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetCrossConnectStatus', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_cross_connect_status.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetCrossConnectStatus. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_cross_connect_status.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_cross_connect_status.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetCrossConnectStatus',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'crossConnectStatus',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_cross_connect_status.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_cross_connect_status.pem')
                if os.path.exists('tests/resources/config_for_test_get_cross_connect_status'):
                    os.remove('tests/resources/config_for_test_get_cross_connect_status')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetCrossConnectStatus')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_dhcp_options(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetDhcpOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetDhcpOptions')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_dhcp_options.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_dhcp_options', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_dhcp_options.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_dhcp_options'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_dhcp_options.pem'])
            config_file = 'tests/resources/config_for_test_get_dhcp_options'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('dhcp_options_group.command_name', 'dhcp_options')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetDhcpOptions')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetDhcpOptions', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_dhcp_options.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetDhcpOptions. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_dhcp_options.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_dhcp_options.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetDhcpOptions',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'dhcpOptions',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_dhcp_options.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_dhcp_options.pem')
                if os.path.exists('tests/resources/config_for_test_get_dhcp_options'):
                    os.remove('tests/resources/config_for_test_get_dhcp_options')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetDhcpOptions')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_drg(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetDrg'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetDrg')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_drg.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_drg', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_drg.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_drg'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_drg.pem'])
            config_file = 'tests/resources/config_for_test_get_drg'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('drg_group.command_name', 'drg')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetDrg')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetDrg', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_drg.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetDrg. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_drg.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_drg.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetDrg',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'drg',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_drg.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_drg.pem')
                if os.path.exists('tests/resources/config_for_test_get_drg'):
                    os.remove('tests/resources/config_for_test_get_drg')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetDrg')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_drg_attachment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetDrgAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetDrgAttachment')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_drg_attachment.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_drg_attachment', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_drg_attachment.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_drg_attachment'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_drg_attachment.pem'])
            config_file = 'tests/resources/config_for_test_get_drg_attachment'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('drg_attachment_group.command_name', 'drg_attachment')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetDrgAttachment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetDrgAttachment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_drg_attachment.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetDrgAttachment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_drg_attachment.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_drg_attachment.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetDrgAttachment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'drgAttachment',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_drg_attachment.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_drg_attachment.pem')
                if os.path.exists('tests/resources/config_for_test_get_drg_attachment'):
                    os.remove('tests/resources/config_for_test_get_drg_attachment')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetDrgAttachment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_fast_connect_provider_service(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetFastConnectProviderService'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetFastConnectProviderService')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_fast_connect_provider_service.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_fast_connect_provider_service', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_fast_connect_provider_service.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_fast_connect_provider_service'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_fast_connect_provider_service.pem'])
            config_file = 'tests/resources/config_for_test_get_fast_connect_provider_service'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('fast_connect_provider_service_group.command_name', 'fast_connect_provider_service')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetFastConnectProviderService')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetFastConnectProviderService', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_fast_connect_provider_service.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetFastConnectProviderService. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_fast_connect_provider_service.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_fast_connect_provider_service.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetFastConnectProviderService',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'fastConnectProviderService',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_fast_connect_provider_service.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_fast_connect_provider_service.pem')
                if os.path.exists('tests/resources/config_for_test_get_fast_connect_provider_service'):
                    os.remove('tests/resources/config_for_test_get_fast_connect_provider_service')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetFastConnectProviderService')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_fast_connect_provider_service_key(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetFastConnectProviderServiceKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetFastConnectProviderServiceKey')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_fast_connect_provider_service_key.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_fast_connect_provider_service_key', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_fast_connect_provider_service_key.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_fast_connect_provider_service_key'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_fast_connect_provider_service_key.pem'])
            config_file = 'tests/resources/config_for_test_get_fast_connect_provider_service_key'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('fast_connect_provider_service_key_group.command_name', 'fast_connect_provider_service_key')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetFastConnectProviderServiceKey')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetFastConnectProviderServiceKey', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_fast_connect_provider_service_key.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetFastConnectProviderServiceKey. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_fast_connect_provider_service_key.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_fast_connect_provider_service_key.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetFastConnectProviderServiceKey',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'fastConnectProviderServiceKey',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_fast_connect_provider_service_key.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_fast_connect_provider_service_key.pem')
                if os.path.exists('tests/resources/config_for_test_get_fast_connect_provider_service_key'):
                    os.remove('tests/resources/config_for_test_get_fast_connect_provider_service_key')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetFastConnectProviderServiceKey')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_internet_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetInternetGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetInternetGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_internet_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_internet_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_internet_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_internet_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_internet_gateway.pem'])
            config_file = 'tests/resources/config_for_test_get_internet_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('internet_gateway_group.command_name', 'internet_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetInternetGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetInternetGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_internet_gateway.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetInternetGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_internet_gateway.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_internet_gateway.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetInternetGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'internetGateway',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_internet_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_internet_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_get_internet_gateway'):
                    os.remove('tests/resources/config_for_test_get_internet_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetInternetGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_ip_sec_connection(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetIPSecConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetIPSecConnection')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_ip_sec_connection.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_ip_sec_connection', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_ip_sec_connection.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_ip_sec_connection'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_ip_sec_connection.pem'])
            config_file = 'tests/resources/config_for_test_get_ip_sec_connection'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('ip_sec_connection_group.command_name', 'ip_sec_connection')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetIPSecConnection')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetIPSecConnection', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_ip_sec_connection.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetIPSecConnection. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_ip_sec_connection.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_ip_sec_connection.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetIPSecConnection',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'iPSecConnection',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_ip_sec_connection.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_ip_sec_connection.pem')
                if os.path.exists('tests/resources/config_for_test_get_ip_sec_connection'):
                    os.remove('tests/resources/config_for_test_get_ip_sec_connection')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetIPSecConnection')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_ip_sec_connection_device_config(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetIPSecConnectionDeviceConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetIPSecConnectionDeviceConfig')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_ip_sec_connection_device_config.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_ip_sec_connection_device_config', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_ip_sec_connection_device_config.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_ip_sec_connection_device_config'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_ip_sec_connection_device_config.pem'])
            config_file = 'tests/resources/config_for_test_get_ip_sec_connection_device_config'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('ip_sec_connection_device_config_group.command_name', 'ip_sec_connection_device_config')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetIPSecConnectionDeviceConfig')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetIPSecConnectionDeviceConfig', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_ip_sec_connection_device_config.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetIPSecConnectionDeviceConfig. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_ip_sec_connection_device_config.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_ip_sec_connection_device_config.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetIPSecConnectionDeviceConfig',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'iPSecConnectionDeviceConfig',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_ip_sec_connection_device_config.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_ip_sec_connection_device_config.pem')
                if os.path.exists('tests/resources/config_for_test_get_ip_sec_connection_device_config'):
                    os.remove('tests/resources/config_for_test_get_ip_sec_connection_device_config')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetIPSecConnectionDeviceConfig')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_ip_sec_connection_device_status(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetIPSecConnectionDeviceStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetIPSecConnectionDeviceStatus')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_ip_sec_connection_device_status.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_ip_sec_connection_device_status', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_ip_sec_connection_device_status.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_ip_sec_connection_device_status'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_ip_sec_connection_device_status.pem'])
            config_file = 'tests/resources/config_for_test_get_ip_sec_connection_device_status'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('ip_sec_connection_device_status_group.command_name', 'ip_sec_connection_device_status')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetIPSecConnectionDeviceStatus')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetIPSecConnectionDeviceStatus', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_ip_sec_connection_device_status.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetIPSecConnectionDeviceStatus. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_ip_sec_connection_device_status.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_ip_sec_connection_device_status.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetIPSecConnectionDeviceStatus',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'iPSecConnectionDeviceStatus',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_ip_sec_connection_device_status.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_ip_sec_connection_device_status.pem')
                if os.path.exists('tests/resources/config_for_test_get_ip_sec_connection_device_status'):
                    os.remove('tests/resources/config_for_test_get_ip_sec_connection_device_status')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetIPSecConnectionDeviceStatus')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_local_peering_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetLocalPeeringGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetLocalPeeringGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_local_peering_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_local_peering_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_local_peering_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_local_peering_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_local_peering_gateway.pem'])
            config_file = 'tests/resources/config_for_test_get_local_peering_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('local_peering_gateway_group.command_name', 'local_peering_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetLocalPeeringGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetLocalPeeringGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_local_peering_gateway.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetLocalPeeringGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_local_peering_gateway.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_local_peering_gateway.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetLocalPeeringGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'localPeeringGateway',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_local_peering_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_local_peering_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_get_local_peering_gateway'):
                    os.remove('tests/resources/config_for_test_get_local_peering_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetLocalPeeringGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_nat_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetNatGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetNatGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_nat_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_nat_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_nat_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_nat_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_nat_gateway.pem'])
            config_file = 'tests/resources/config_for_test_get_nat_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('nat_gateway_group.command_name', 'nat_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetNatGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetNatGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_nat_gateway.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetNatGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_nat_gateway.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_nat_gateway.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetNatGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'natGateway',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_nat_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_nat_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_get_nat_gateway'):
                    os.remove('tests/resources/config_for_test_get_nat_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetNatGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_private_ip(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetPrivateIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetPrivateIp')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_private_ip.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_private_ip', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_private_ip.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_private_ip'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_private_ip.pem'])
            config_file = 'tests/resources/config_for_test_get_private_ip'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('private_ip_group.command_name', 'private_ip')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetPrivateIp')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetPrivateIp', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_private_ip.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetPrivateIp. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_private_ip.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_private_ip.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetPrivateIp',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'privateIp',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_private_ip.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_private_ip.pem')
                if os.path.exists('tests/resources/config_for_test_get_private_ip'):
                    os.remove('tests/resources/config_for_test_get_private_ip')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetPrivateIp')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_public_ip(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetPublicIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetPublicIp')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_public_ip.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_public_ip', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_public_ip.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_public_ip'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_public_ip.pem'])
            config_file = 'tests/resources/config_for_test_get_public_ip'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('public_ip_group.command_name', 'public_ip')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetPublicIp')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetPublicIp', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_public_ip.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetPublicIp. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_public_ip.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_public_ip.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetPublicIp',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'publicIp',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_public_ip.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_public_ip.pem')
                if os.path.exists('tests/resources/config_for_test_get_public_ip'):
                    os.remove('tests/resources/config_for_test_get_public_ip')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetPublicIp')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_public_ip_by_ip_address(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetPublicIpByIpAddress'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetPublicIpByIpAddress')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_public_ip_by_ip_address.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_public_ip_by_ip_address', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_public_ip_by_ip_address.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_public_ip_by_ip_address'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_public_ip_by_ip_address.pem'])
            config_file = 'tests/resources/config_for_test_get_public_ip_by_ip_address'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('public_ip_group.command_name', 'public_ip')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetPublicIpByIpAddress')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'GetPublicIpByIpAddressDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetPublicIpByIpAddress', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_public_ip_by_ip_address.command_name', 'get-public-ip-by-ip-address'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetPublicIpByIpAddress. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_public_ip_by_ip_address.command_name', 'get-public-ip-by-ip-address'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_public_ip_by_ip_address.command_name', 'get-public-ip-by-ip-address')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetPublicIpByIpAddress',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'publicIp',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_public_ip_by_ip_address.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_public_ip_by_ip_address.pem')
                if os.path.exists('tests/resources/config_for_test_get_public_ip_by_ip_address'):
                    os.remove('tests/resources/config_for_test_get_public_ip_by_ip_address')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetPublicIpByIpAddress')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_public_ip_by_private_ip_id(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetPublicIpByPrivateIpId'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetPublicIpByPrivateIpId')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_public_ip_by_private_ip_id.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_public_ip_by_private_ip_id', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_public_ip_by_private_ip_id.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_public_ip_by_private_ip_id'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_public_ip_by_private_ip_id.pem'])
            config_file = 'tests/resources/config_for_test_get_public_ip_by_private_ip_id'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('public_ip_group.command_name', 'public_ip')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetPublicIpByPrivateIpId')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'GetPublicIpByPrivateIpIdDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetPublicIpByPrivateIpId', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_public_ip_by_private_ip_id.command_name', 'get-public-ip-by-private-ip-id'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetPublicIpByPrivateIpId. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_public_ip_by_private_ip_id.command_name', 'get-public-ip-by-private-ip-id'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_public_ip_by_private_ip_id.command_name', 'get-public-ip-by-private-ip-id')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetPublicIpByPrivateIpId',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'publicIp',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_public_ip_by_private_ip_id.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_public_ip_by_private_ip_id.pem')
                if os.path.exists('tests/resources/config_for_test_get_public_ip_by_private_ip_id'):
                    os.remove('tests/resources/config_for_test_get_public_ip_by_private_ip_id')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetPublicIpByPrivateIpId')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_remote_peering_connection(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetRemotePeeringConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetRemotePeeringConnection')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_remote_peering_connection.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_remote_peering_connection', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_remote_peering_connection.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_remote_peering_connection'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_remote_peering_connection.pem'])
            config_file = 'tests/resources/config_for_test_get_remote_peering_connection'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('remote_peering_connection_group.command_name', 'remote_peering_connection')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetRemotePeeringConnection')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetRemotePeeringConnection', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_remote_peering_connection.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetRemotePeeringConnection. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_remote_peering_connection.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_remote_peering_connection.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetRemotePeeringConnection',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'remotePeeringConnection',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_remote_peering_connection.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_remote_peering_connection.pem')
                if os.path.exists('tests/resources/config_for_test_get_remote_peering_connection'):
                    os.remove('tests/resources/config_for_test_get_remote_peering_connection')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetRemotePeeringConnection')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_route_table(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetRouteTable')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_route_table.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_route_table', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_route_table.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_route_table'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_route_table.pem'])
            config_file = 'tests/resources/config_for_test_get_route_table'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('route_table_group.command_name', 'route_table')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetRouteTable')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetRouteTable', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_route_table.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetRouteTable. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_route_table.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_route_table.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetRouteTable',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'routeTable',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_route_table.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_route_table.pem')
                if os.path.exists('tests/resources/config_for_test_get_route_table'):
                    os.remove('tests/resources/config_for_test_get_route_table')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetRouteTable')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_security_list(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetSecurityList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetSecurityList')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_security_list.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_security_list', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_security_list.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_security_list'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_security_list.pem'])
            config_file = 'tests/resources/config_for_test_get_security_list'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('security_list_group.command_name', 'security_list')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetSecurityList')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetSecurityList', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_security_list.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetSecurityList. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_security_list.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_security_list.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetSecurityList',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'securityList',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_security_list.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_security_list.pem')
                if os.path.exists('tests/resources/config_for_test_get_security_list'):
                    os.remove('tests/resources/config_for_test_get_security_list')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetSecurityList')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_service(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetService'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetService')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_service.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_service', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_service.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_service'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_service.pem'])
            config_file = 'tests/resources/config_for_test_get_service'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('service_group.command_name', 'service')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetService')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetService', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_service.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetService. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_service.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_service.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetService',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'service',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_service.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_service.pem')
                if os.path.exists('tests/resources/config_for_test_get_service'):
                    os.remove('tests/resources/config_for_test_get_service')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetService')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_service_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetServiceGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetServiceGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_service_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_service_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_service_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_service_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_service_gateway.pem'])
            config_file = 'tests/resources/config_for_test_get_service_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('service_gateway_group.command_name', 'service_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetServiceGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetServiceGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_service_gateway.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetServiceGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_service_gateway.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_service_gateway.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetServiceGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'serviceGateway',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_service_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_service_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_get_service_gateway'):
                    os.remove('tests/resources/config_for_test_get_service_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetServiceGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_subnet(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetSubnet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetSubnet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_subnet.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_subnet', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_subnet.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_subnet'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_subnet.pem'])
            config_file = 'tests/resources/config_for_test_get_subnet'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('subnet_group.command_name', 'subnet')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetSubnet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetSubnet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_subnet.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetSubnet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_subnet.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_subnet.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetSubnet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'subnet',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_subnet.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_subnet.pem')
                if os.path.exists('tests/resources/config_for_test_get_subnet'):
                    os.remove('tests/resources/config_for_test_get_subnet')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetSubnet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_vcn(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetVcn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetVcn')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_vcn.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_vcn', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_vcn.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_vcn'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_vcn.pem'])
            config_file = 'tests/resources/config_for_test_get_vcn'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('vcn_group.command_name', 'vcn')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVcn')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetVcn', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_vcn.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetVcn. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_vcn.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_vcn.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetVcn',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'vcn',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_vcn.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_vcn.pem')
                if os.path.exists('tests/resources/config_for_test_get_vcn'):
                    os.remove('tests/resources/config_for_test_get_vcn')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVcn')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_virtual_circuit(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetVirtualCircuit'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetVirtualCircuit')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_virtual_circuit.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_virtual_circuit', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_virtual_circuit.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_virtual_circuit'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_virtual_circuit.pem'])
            config_file = 'tests/resources/config_for_test_get_virtual_circuit'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('virtual_circuit_group.command_name', 'virtual_circuit')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVirtualCircuit')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetVirtualCircuit', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_virtual_circuit.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetVirtualCircuit. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_virtual_circuit.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_virtual_circuit.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetVirtualCircuit',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'virtualCircuit',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_virtual_circuit.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_virtual_circuit.pem')
                if os.path.exists('tests/resources/config_for_test_get_virtual_circuit'):
                    os.remove('tests/resources/config_for_test_get_virtual_circuit')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVirtualCircuit')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_vnic(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetVnic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'GetVnic')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_vnic.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_vnic', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_vnic.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_vnic'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_vnic.pem'])
            config_file = 'tests/resources/config_for_test_get_vnic'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('vnic_group.command_name', 'vnic')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVnic')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetVnic', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_vnic.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetVnic. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_vnic.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_vnic.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetVnic',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'vnic',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_vnic.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_vnic.pem')
                if os.path.exists('tests/resources/config_for_test_get_vnic'):
                    os.remove('tests/resources/config_for_test_get_vnic')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetVnic')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_allowed_peer_regions_for_remote_peering(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListAllowedPeerRegionsForRemotePeering'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListAllowedPeerRegionsForRemotePeering')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_allowed_peer_regions_for_remote_peering.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_allowed_peer_regions_for_remote_peering', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_allowed_peer_regions_for_remote_peering.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_allowed_peer_regions_for_remote_peering'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_allowed_peer_regions_for_remote_peering.pem'])
            config_file = 'tests/resources/config_for_test_list_allowed_peer_regions_for_remote_peering'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('peer_region_for_remote_peering_group.command_name', 'peer_region_for_remote_peering')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListAllowedPeerRegionsForRemotePeering')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListAllowedPeerRegionsForRemotePeering', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_allowed_peer_regions_for_remote_peering.command_name', 'list-allowed-peer-regions-for-remote-peering'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListAllowedPeerRegionsForRemotePeering. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_allowed_peer_regions_for_remote_peering.command_name', 'list-allowed-peer-regions-for-remote-peering'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_allowed_peer_regions_for_remote_peering.command_name', 'list-allowed-peer-regions-for-remote-peering')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListAllowedPeerRegionsForRemotePeering',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_allowed_peer_regions_for_remote_peering.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_allowed_peer_regions_for_remote_peering.pem')
                if os.path.exists('tests/resources/config_for_test_list_allowed_peer_regions_for_remote_peering'):
                    os.remove('tests/resources/config_for_test_list_allowed_peer_regions_for_remote_peering')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListAllowedPeerRegionsForRemotePeering')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_cpes(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListCpes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListCpes')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_cpes.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_cpes', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_cpes.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_cpes'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_cpes.pem'])
            config_file = 'tests/resources/config_for_test_list_cpes'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cpe_group.command_name', 'cpe')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListCpes')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListCpes', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_cpes.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListCpes. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_cpes.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_cpes.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListCpes',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_cpes.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_cpes.pem')
                if os.path.exists('tests/resources/config_for_test_list_cpes'):
                    os.remove('tests/resources/config_for_test_list_cpes')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListCpes')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_cross_connect_groups(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListCrossConnectGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListCrossConnectGroups')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_cross_connect_groups.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_cross_connect_groups', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_cross_connect_groups.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_cross_connect_groups'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_cross_connect_groups.pem'])
            config_file = 'tests/resources/config_for_test_list_cross_connect_groups'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cross_connect_group_group.command_name', 'cross_connect_group')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListCrossConnectGroups')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListCrossConnectGroups', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_cross_connect_groups.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListCrossConnectGroups. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_cross_connect_groups.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_cross_connect_groups.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListCrossConnectGroups',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_cross_connect_groups.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_cross_connect_groups.pem')
                if os.path.exists('tests/resources/config_for_test_list_cross_connect_groups'):
                    os.remove('tests/resources/config_for_test_list_cross_connect_groups')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListCrossConnectGroups')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_cross_connect_locations(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListCrossConnectLocations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListCrossConnectLocations')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_cross_connect_locations.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_cross_connect_locations', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_cross_connect_locations.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_cross_connect_locations'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_cross_connect_locations.pem'])
            config_file = 'tests/resources/config_for_test_list_cross_connect_locations'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cross_connect_location_group.command_name', 'cross_connect_location')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListCrossConnectLocations')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListCrossConnectLocations', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_cross_connect_locations.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListCrossConnectLocations. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_cross_connect_locations.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_cross_connect_locations.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListCrossConnectLocations',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_cross_connect_locations.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_cross_connect_locations.pem')
                if os.path.exists('tests/resources/config_for_test_list_cross_connect_locations'):
                    os.remove('tests/resources/config_for_test_list_cross_connect_locations')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListCrossConnectLocations')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_cross_connects(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListCrossConnects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListCrossConnects')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_cross_connects.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_cross_connects', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_cross_connects.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_cross_connects'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_cross_connects.pem'])
            config_file = 'tests/resources/config_for_test_list_cross_connects'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cross_connect_group.command_name', 'cross_connect')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListCrossConnects')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListCrossConnects', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_cross_connects.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListCrossConnects. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_cross_connects.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_cross_connects.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListCrossConnects',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_cross_connects.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_cross_connects.pem')
                if os.path.exists('tests/resources/config_for_test_list_cross_connects'):
                    os.remove('tests/resources/config_for_test_list_cross_connects')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListCrossConnects')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_crossconnect_port_speed_shapes(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListCrossconnectPortSpeedShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListCrossconnectPortSpeedShapes')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_crossconnect_port_speed_shapes.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_crossconnect_port_speed_shapes', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_crossconnect_port_speed_shapes.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_crossconnect_port_speed_shapes'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_crossconnect_port_speed_shapes.pem'])
            config_file = 'tests/resources/config_for_test_list_crossconnect_port_speed_shapes'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cross_connect_port_speed_shape_group.command_name', 'cross_connect_port_speed_shape')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListCrossconnectPortSpeedShapes')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListCrossconnectPortSpeedShapes', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_crossconnect_port_speed_shapes.command_name', 'list-crossconnect-port-speed-shapes'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListCrossconnectPortSpeedShapes. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_crossconnect_port_speed_shapes.command_name', 'list-crossconnect-port-speed-shapes'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_crossconnect_port_speed_shapes.command_name', 'list-crossconnect-port-speed-shapes')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListCrossconnectPortSpeedShapes',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_crossconnect_port_speed_shapes.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_crossconnect_port_speed_shapes.pem')
                if os.path.exists('tests/resources/config_for_test_list_crossconnect_port_speed_shapes'):
                    os.remove('tests/resources/config_for_test_list_crossconnect_port_speed_shapes')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListCrossconnectPortSpeedShapes')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_dhcp_options(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListDhcpOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListDhcpOptions')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_dhcp_options.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_dhcp_options', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_dhcp_options.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_dhcp_options'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_dhcp_options.pem'])
            config_file = 'tests/resources/config_for_test_list_dhcp_options'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('dhcp_options_group.command_name', 'dhcp_options')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListDhcpOptions')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListDhcpOptions', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_dhcp_options.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListDhcpOptions. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_dhcp_options.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_dhcp_options.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListDhcpOptions',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_dhcp_options.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_dhcp_options.pem')
                if os.path.exists('tests/resources/config_for_test_list_dhcp_options'):
                    os.remove('tests/resources/config_for_test_list_dhcp_options')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListDhcpOptions')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_drg_attachments(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListDrgAttachments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListDrgAttachments')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_drg_attachments.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_drg_attachments', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_drg_attachments.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_drg_attachments'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_drg_attachments.pem'])
            config_file = 'tests/resources/config_for_test_list_drg_attachments'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('drg_attachment_group.command_name', 'drg_attachment')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListDrgAttachments')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListDrgAttachments', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_drg_attachments.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListDrgAttachments. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_drg_attachments.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_drg_attachments.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListDrgAttachments',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_drg_attachments.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_drg_attachments.pem')
                if os.path.exists('tests/resources/config_for_test_list_drg_attachments'):
                    os.remove('tests/resources/config_for_test_list_drg_attachments')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListDrgAttachments')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_drgs(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListDrgs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListDrgs')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_drgs.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_drgs', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_drgs.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_drgs'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_drgs.pem'])
            config_file = 'tests/resources/config_for_test_list_drgs'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('drg_group.command_name', 'drg')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListDrgs')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListDrgs', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_drgs.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListDrgs. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_drgs.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_drgs.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListDrgs',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_drgs.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_drgs.pem')
                if os.path.exists('tests/resources/config_for_test_list_drgs'):
                    os.remove('tests/resources/config_for_test_list_drgs')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListDrgs')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_fast_connect_provider_services(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListFastConnectProviderServices'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListFastConnectProviderServices')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_fast_connect_provider_services.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_fast_connect_provider_services', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_fast_connect_provider_services.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_fast_connect_provider_services'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_fast_connect_provider_services.pem'])
            config_file = 'tests/resources/config_for_test_list_fast_connect_provider_services'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('fast_connect_provider_service_group.command_name', 'fast_connect_provider_service')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListFastConnectProviderServices')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListFastConnectProviderServices', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_fast_connect_provider_services.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListFastConnectProviderServices. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_fast_connect_provider_services.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_fast_connect_provider_services.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListFastConnectProviderServices',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_fast_connect_provider_services.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_fast_connect_provider_services.pem')
                if os.path.exists('tests/resources/config_for_test_list_fast_connect_provider_services'):
                    os.remove('tests/resources/config_for_test_list_fast_connect_provider_services')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListFastConnectProviderServices')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_fast_connect_provider_virtual_circuit_bandwidth_shapes(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListFastConnectProviderVirtualCircuitBandwidthShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListFastConnectProviderVirtualCircuitBandwidthShapes')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_fast_connect_provider_virtual_circuit_bandwidth_shapes.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_fast_connect_provider_virtual_circuit_bandwidth_shapes', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_fast_connect_provider_virtual_circuit_bandwidth_shapes.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_fast_connect_provider_virtual_circuit_bandwidth_shapes'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_fast_connect_provider_virtual_circuit_bandwidth_shapes.pem'])
            config_file = 'tests/resources/config_for_test_list_fast_connect_provider_virtual_circuit_bandwidth_shapes'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('fast_connect_provider_service_group.command_name', 'fast_connect_provider_service')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListFastConnectProviderVirtualCircuitBandwidthShapes')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListFastConnectProviderVirtualCircuitBandwidthShapes', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_fast_connect_provider_virtual_circuit_bandwidth_shapes.command_name', 'list-fast-connect-provider-virtual-circuit-bandwidth-shapes'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListFastConnectProviderVirtualCircuitBandwidthShapes. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_fast_connect_provider_virtual_circuit_bandwidth_shapes.command_name', 'list-fast-connect-provider-virtual-circuit-bandwidth-shapes'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_fast_connect_provider_virtual_circuit_bandwidth_shapes.command_name', 'list-fast-connect-provider-virtual-circuit-bandwidth-shapes')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListFastConnectProviderVirtualCircuitBandwidthShapes',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_fast_connect_provider_virtual_circuit_bandwidth_shapes.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_fast_connect_provider_virtual_circuit_bandwidth_shapes.pem')
                if os.path.exists('tests/resources/config_for_test_list_fast_connect_provider_virtual_circuit_bandwidth_shapes'):
                    os.remove('tests/resources/config_for_test_list_fast_connect_provider_virtual_circuit_bandwidth_shapes')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListFastConnectProviderVirtualCircuitBandwidthShapes')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_internet_gateways(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListInternetGateways'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListInternetGateways')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_internet_gateways.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_internet_gateways', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_internet_gateways.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_internet_gateways'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_internet_gateways.pem'])
            config_file = 'tests/resources/config_for_test_list_internet_gateways'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('internet_gateway_group.command_name', 'internet_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListInternetGateways')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListInternetGateways', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_internet_gateways.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListInternetGateways. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_internet_gateways.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_internet_gateways.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListInternetGateways',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_internet_gateways.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_internet_gateways.pem')
                if os.path.exists('tests/resources/config_for_test_list_internet_gateways'):
                    os.remove('tests/resources/config_for_test_list_internet_gateways')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListInternetGateways')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_ip_sec_connections(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListIPSecConnections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListIPSecConnections')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_ip_sec_connections.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_ip_sec_connections', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_ip_sec_connections.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_ip_sec_connections'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_ip_sec_connections.pem'])
            config_file = 'tests/resources/config_for_test_list_ip_sec_connections'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('ip_sec_connection_group.command_name', 'ip_sec_connection')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListIPSecConnections')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListIPSecConnections', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_ip_sec_connections.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListIPSecConnections. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_ip_sec_connections.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_ip_sec_connections.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListIPSecConnections',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_ip_sec_connections.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_ip_sec_connections.pem')
                if os.path.exists('tests/resources/config_for_test_list_ip_sec_connections'):
                    os.remove('tests/resources/config_for_test_list_ip_sec_connections')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListIPSecConnections')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_local_peering_gateways(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListLocalPeeringGateways'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListLocalPeeringGateways')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_local_peering_gateways.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_local_peering_gateways', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_local_peering_gateways.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_local_peering_gateways'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_local_peering_gateways.pem'])
            config_file = 'tests/resources/config_for_test_list_local_peering_gateways'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('local_peering_gateway_group.command_name', 'local_peering_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListLocalPeeringGateways')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListLocalPeeringGateways', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_local_peering_gateways.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListLocalPeeringGateways. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_local_peering_gateways.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_local_peering_gateways.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListLocalPeeringGateways',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_local_peering_gateways.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_local_peering_gateways.pem')
                if os.path.exists('tests/resources/config_for_test_list_local_peering_gateways'):
                    os.remove('tests/resources/config_for_test_list_local_peering_gateways')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListLocalPeeringGateways')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_nat_gateways(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListNatGateways'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListNatGateways')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_nat_gateways.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_nat_gateways', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_nat_gateways.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_nat_gateways'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_nat_gateways.pem'])
            config_file = 'tests/resources/config_for_test_list_nat_gateways'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('nat_gateway_group.command_name', 'nat_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListNatGateways')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListNatGateways', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_nat_gateways.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListNatGateways. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_nat_gateways.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_nat_gateways.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListNatGateways',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_nat_gateways.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_nat_gateways.pem')
                if os.path.exists('tests/resources/config_for_test_list_nat_gateways'):
                    os.remove('tests/resources/config_for_test_list_nat_gateways')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListNatGateways')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_private_ips(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListPrivateIps'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListPrivateIps')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_private_ips.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_private_ips', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_private_ips.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_private_ips'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_private_ips.pem'])
            config_file = 'tests/resources/config_for_test_list_private_ips'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('private_ip_group.command_name', 'private_ip')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListPrivateIps')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListPrivateIps', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_private_ips.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListPrivateIps. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_private_ips.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_private_ips.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListPrivateIps',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_private_ips.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_private_ips.pem')
                if os.path.exists('tests/resources/config_for_test_list_private_ips'):
                    os.remove('tests/resources/config_for_test_list_private_ips')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListPrivateIps')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_public_ips(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListPublicIps'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListPublicIps')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_public_ips.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_public_ips', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_public_ips.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_public_ips'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_public_ips.pem'])
            config_file = 'tests/resources/config_for_test_list_public_ips'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('public_ip_group.command_name', 'public_ip')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListPublicIps')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListPublicIps', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_public_ips.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListPublicIps. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_public_ips.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_public_ips.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListPublicIps',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_public_ips.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_public_ips.pem')
                if os.path.exists('tests/resources/config_for_test_list_public_ips'):
                    os.remove('tests/resources/config_for_test_list_public_ips')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListPublicIps')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_remote_peering_connections(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListRemotePeeringConnections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListRemotePeeringConnections')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_remote_peering_connections.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_remote_peering_connections', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_remote_peering_connections.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_remote_peering_connections'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_remote_peering_connections.pem'])
            config_file = 'tests/resources/config_for_test_list_remote_peering_connections'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('remote_peering_connection_group.command_name', 'remote_peering_connection')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListRemotePeeringConnections')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListRemotePeeringConnections', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_remote_peering_connections.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListRemotePeeringConnections. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_remote_peering_connections.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_remote_peering_connections.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListRemotePeeringConnections',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_remote_peering_connections.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_remote_peering_connections.pem')
                if os.path.exists('tests/resources/config_for_test_list_remote_peering_connections'):
                    os.remove('tests/resources/config_for_test_list_remote_peering_connections')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListRemotePeeringConnections')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_route_tables(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListRouteTables'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListRouteTables')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_route_tables.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_route_tables', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_route_tables.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_route_tables'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_route_tables.pem'])
            config_file = 'tests/resources/config_for_test_list_route_tables'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('route_table_group.command_name', 'route_table')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListRouteTables')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListRouteTables', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_route_tables.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListRouteTables. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_route_tables.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_route_tables.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListRouteTables',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_route_tables.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_route_tables.pem')
                if os.path.exists('tests/resources/config_for_test_list_route_tables'):
                    os.remove('tests/resources/config_for_test_list_route_tables')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListRouteTables')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_security_lists(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListSecurityLists'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListSecurityLists')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_security_lists.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_security_lists', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_security_lists.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_security_lists'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_security_lists.pem'])
            config_file = 'tests/resources/config_for_test_list_security_lists'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('security_list_group.command_name', 'security_list')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListSecurityLists')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListSecurityLists', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_security_lists.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListSecurityLists. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_security_lists.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_security_lists.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListSecurityLists',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_security_lists.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_security_lists.pem')
                if os.path.exists('tests/resources/config_for_test_list_security_lists'):
                    os.remove('tests/resources/config_for_test_list_security_lists')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListSecurityLists')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_service_gateways(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListServiceGateways'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListServiceGateways')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_service_gateways.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_service_gateways', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_service_gateways.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_service_gateways'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_service_gateways.pem'])
            config_file = 'tests/resources/config_for_test_list_service_gateways'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('service_gateway_group.command_name', 'service_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListServiceGateways')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListServiceGateways', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_service_gateways.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListServiceGateways. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_service_gateways.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_service_gateways.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListServiceGateways',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_service_gateways.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_service_gateways.pem')
                if os.path.exists('tests/resources/config_for_test_list_service_gateways'):
                    os.remove('tests/resources/config_for_test_list_service_gateways')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListServiceGateways')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_services(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListServices'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListServices')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_services.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_services', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_services.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_services'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_services.pem'])
            config_file = 'tests/resources/config_for_test_list_services'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('service_group.command_name', 'service')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListServices')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListServices', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_services.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListServices. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_services.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_services.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListServices',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_services.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_services.pem')
                if os.path.exists('tests/resources/config_for_test_list_services'):
                    os.remove('tests/resources/config_for_test_list_services')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListServices')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_subnets(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListSubnets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListSubnets')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_subnets.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_subnets', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_subnets.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_subnets'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_subnets.pem'])
            config_file = 'tests/resources/config_for_test_list_subnets'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('subnet_group.command_name', 'subnet')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListSubnets')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListSubnets', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_subnets.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListSubnets. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_subnets.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_subnets.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListSubnets',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_subnets.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_subnets.pem')
                if os.path.exists('tests/resources/config_for_test_list_subnets'):
                    os.remove('tests/resources/config_for_test_list_subnets')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListSubnets')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_vcns(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListVcns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListVcns')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_vcns.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_vcns', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_vcns.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_vcns'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_vcns.pem'])
            config_file = 'tests/resources/config_for_test_list_vcns'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('vcn_group.command_name', 'vcn')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVcns')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListVcns', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_vcns.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListVcns. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_vcns.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_vcns.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListVcns',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_vcns.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_vcns.pem')
                if os.path.exists('tests/resources/config_for_test_list_vcns'):
                    os.remove('tests/resources/config_for_test_list_vcns')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVcns')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_virtual_circuit_bandwidth_shapes(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListVirtualCircuitBandwidthShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListVirtualCircuitBandwidthShapes')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_virtual_circuit_bandwidth_shapes.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_virtual_circuit_bandwidth_shapes', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_virtual_circuit_bandwidth_shapes.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_virtual_circuit_bandwidth_shapes'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_virtual_circuit_bandwidth_shapes.pem'])
            config_file = 'tests/resources/config_for_test_list_virtual_circuit_bandwidth_shapes'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('virtual_circuit_bandwidth_shape_group.command_name', 'virtual_circuit_bandwidth_shape')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVirtualCircuitBandwidthShapes')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListVirtualCircuitBandwidthShapes', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_virtual_circuit_bandwidth_shapes.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListVirtualCircuitBandwidthShapes. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_virtual_circuit_bandwidth_shapes.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_virtual_circuit_bandwidth_shapes.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListVirtualCircuitBandwidthShapes',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_virtual_circuit_bandwidth_shapes.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_virtual_circuit_bandwidth_shapes.pem')
                if os.path.exists('tests/resources/config_for_test_list_virtual_circuit_bandwidth_shapes'):
                    os.remove('tests/resources/config_for_test_list_virtual_circuit_bandwidth_shapes')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVirtualCircuitBandwidthShapes')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_virtual_circuit_public_prefixes(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListVirtualCircuitPublicPrefixes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListVirtualCircuitPublicPrefixes')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_virtual_circuit_public_prefixes.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_virtual_circuit_public_prefixes', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_virtual_circuit_public_prefixes.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_virtual_circuit_public_prefixes'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_virtual_circuit_public_prefixes.pem'])
            config_file = 'tests/resources/config_for_test_list_virtual_circuit_public_prefixes'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('virtual_circuit_public_prefix_group.command_name', 'virtual_circuit_public_prefix')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVirtualCircuitPublicPrefixes')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListVirtualCircuitPublicPrefixes', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_virtual_circuit_public_prefixes.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListVirtualCircuitPublicPrefixes. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_virtual_circuit_public_prefixes.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_virtual_circuit_public_prefixes.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListVirtualCircuitPublicPrefixes',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_virtual_circuit_public_prefixes.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_virtual_circuit_public_prefixes.pem')
                if os.path.exists('tests/resources/config_for_test_list_virtual_circuit_public_prefixes'):
                    os.remove('tests/resources/config_for_test_list_virtual_circuit_public_prefixes')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVirtualCircuitPublicPrefixes')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_virtual_circuits(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListVirtualCircuits'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'ListVirtualCircuits')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_virtual_circuits.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_virtual_circuits', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_virtual_circuits.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_virtual_circuits'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_virtual_circuits.pem'])
            config_file = 'tests/resources/config_for_test_list_virtual_circuits'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('virtual_circuit_group.command_name', 'virtual_circuit')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVirtualCircuits')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListVirtualCircuits', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_virtual_circuits.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListVirtualCircuits. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_virtual_circuits.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_virtual_circuits.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListVirtualCircuits',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_virtual_circuits.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_virtual_circuits.pem')
                if os.path.exists('tests/resources/config_for_test_list_virtual_circuits'):
                    os.remove('tests/resources/config_for_test_list_virtual_circuits')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListVirtualCircuits')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_cpe(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateCpe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateCpe')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_cpe.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_cpe', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_cpe.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_cpe'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_cpe.pem'])
            config_file = 'tests/resources/config_for_test_update_cpe'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cpe_group.command_name', 'cpe')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateCpe')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateCpeDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateCpe', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_cpe.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateCpe. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_cpe.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_cpe.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateCpe',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'cpe',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_cpe.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_cpe.pem')
                if os.path.exists('tests/resources/config_for_test_update_cpe'):
                    os.remove('tests/resources/config_for_test_update_cpe')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateCpe')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_cross_connect(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateCrossConnect'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateCrossConnect')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_cross_connect.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_cross_connect', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_cross_connect.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_cross_connect'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_cross_connect.pem'])
            config_file = 'tests/resources/config_for_test_update_cross_connect'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cross_connect_group.command_name', 'cross_connect')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateCrossConnect')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateCrossConnectDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateCrossConnect', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_cross_connect.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateCrossConnect. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_cross_connect.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_cross_connect.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateCrossConnect',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'crossConnect',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_cross_connect.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_cross_connect.pem')
                if os.path.exists('tests/resources/config_for_test_update_cross_connect'):
                    os.remove('tests/resources/config_for_test_update_cross_connect')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateCrossConnect')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_cross_connect_group(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateCrossConnectGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateCrossConnectGroup')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_cross_connect_group.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_cross_connect_group', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_cross_connect_group.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_cross_connect_group'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_cross_connect_group.pem'])
            config_file = 'tests/resources/config_for_test_update_cross_connect_group'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('cross_connect_group_group.command_name', 'cross_connect_group')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateCrossConnectGroup')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateCrossConnectGroupDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateCrossConnectGroup', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_cross_connect_group.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateCrossConnectGroup. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_cross_connect_group.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_cross_connect_group.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateCrossConnectGroup',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'crossConnectGroup',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_cross_connect_group.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_cross_connect_group.pem')
                if os.path.exists('tests/resources/config_for_test_update_cross_connect_group'):
                    os.remove('tests/resources/config_for_test_update_cross_connect_group')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateCrossConnectGroup')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_dhcp_options(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateDhcpOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateDhcpOptions')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_dhcp_options.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_dhcp_options', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_dhcp_options.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_dhcp_options'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_dhcp_options.pem'])
            config_file = 'tests/resources/config_for_test_update_dhcp_options'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('dhcp_options_group.command_name', 'dhcp_options')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateDhcpOptions')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateDhcpDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateDhcpOptions', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_dhcp_options.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateDhcpOptions. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_dhcp_options.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_dhcp_options.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateDhcpOptions',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'dhcpOptions',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_dhcp_options.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_dhcp_options.pem')
                if os.path.exists('tests/resources/config_for_test_update_dhcp_options'):
                    os.remove('tests/resources/config_for_test_update_dhcp_options')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateDhcpOptions')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_drg(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateDrg'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateDrg')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_drg.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_drg', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_drg.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_drg'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_drg.pem'])
            config_file = 'tests/resources/config_for_test_update_drg'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('drg_group.command_name', 'drg')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateDrg')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateDrgDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateDrg', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_drg.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateDrg. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_drg.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_drg.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateDrg',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'drg',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_drg.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_drg.pem')
                if os.path.exists('tests/resources/config_for_test_update_drg'):
                    os.remove('tests/resources/config_for_test_update_drg')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateDrg')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_drg_attachment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateDrgAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateDrgAttachment')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_drg_attachment.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_drg_attachment', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_drg_attachment.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_drg_attachment'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_drg_attachment.pem'])
            config_file = 'tests/resources/config_for_test_update_drg_attachment'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('drg_attachment_group.command_name', 'drg_attachment')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateDrgAttachment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateDrgAttachmentDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateDrgAttachment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_drg_attachment.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateDrgAttachment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_drg_attachment.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_drg_attachment.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateDrgAttachment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'drgAttachment',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_drg_attachment.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_drg_attachment.pem')
                if os.path.exists('tests/resources/config_for_test_update_drg_attachment'):
                    os.remove('tests/resources/config_for_test_update_drg_attachment')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateDrgAttachment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_internet_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateInternetGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateInternetGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_internet_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_internet_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_internet_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_internet_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_internet_gateway.pem'])
            config_file = 'tests/resources/config_for_test_update_internet_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('internet_gateway_group.command_name', 'internet_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateInternetGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateInternetGatewayDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateInternetGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_internet_gateway.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateInternetGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_internet_gateway.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_internet_gateway.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateInternetGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'internetGateway',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_internet_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_internet_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_update_internet_gateway'):
                    os.remove('tests/resources/config_for_test_update_internet_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateInternetGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_ip_sec_connection(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateIPSecConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateIPSecConnection')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_ip_sec_connection.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_ip_sec_connection', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_ip_sec_connection.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_ip_sec_connection'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_ip_sec_connection.pem'])
            config_file = 'tests/resources/config_for_test_update_ip_sec_connection'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('ip_sec_connection_group.command_name', 'ip_sec_connection')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateIPSecConnection')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateIPSecConnectionDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateIPSecConnection', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_ip_sec_connection.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateIPSecConnection. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_ip_sec_connection.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_ip_sec_connection.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateIPSecConnection',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'iPSecConnection',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_ip_sec_connection.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_ip_sec_connection.pem')
                if os.path.exists('tests/resources/config_for_test_update_ip_sec_connection'):
                    os.remove('tests/resources/config_for_test_update_ip_sec_connection')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateIPSecConnection')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_local_peering_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateLocalPeeringGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateLocalPeeringGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_local_peering_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_local_peering_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_local_peering_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_local_peering_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_local_peering_gateway.pem'])
            config_file = 'tests/resources/config_for_test_update_local_peering_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('local_peering_gateway_group.command_name', 'local_peering_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateLocalPeeringGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateLocalPeeringGatewayDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateLocalPeeringGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_local_peering_gateway.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateLocalPeeringGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_local_peering_gateway.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_local_peering_gateway.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateLocalPeeringGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'localPeeringGateway',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_local_peering_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_local_peering_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_update_local_peering_gateway'):
                    os.remove('tests/resources/config_for_test_update_local_peering_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateLocalPeeringGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_nat_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateNatGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateNatGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_nat_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_nat_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_nat_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_nat_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_nat_gateway.pem'])
            config_file = 'tests/resources/config_for_test_update_nat_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('nat_gateway_group.command_name', 'nat_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateNatGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateNatGatewayDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateNatGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_nat_gateway.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateNatGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_nat_gateway.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_nat_gateway.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateNatGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'natGateway',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_nat_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_nat_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_update_nat_gateway'):
                    os.remove('tests/resources/config_for_test_update_nat_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateNatGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_private_ip(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdatePrivateIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdatePrivateIp')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_private_ip.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_private_ip', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_private_ip.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_private_ip'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_private_ip.pem'])
            config_file = 'tests/resources/config_for_test_update_private_ip'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('private_ip_group.command_name', 'private_ip')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdatePrivateIp')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdatePrivateIpDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdatePrivateIp', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_private_ip.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdatePrivateIp. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_private_ip.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_private_ip.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdatePrivateIp',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'privateIp',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_private_ip.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_private_ip.pem')
                if os.path.exists('tests/resources/config_for_test_update_private_ip'):
                    os.remove('tests/resources/config_for_test_update_private_ip')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdatePrivateIp')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_public_ip(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdatePublicIp'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdatePublicIp')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_public_ip.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_public_ip', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_public_ip.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_public_ip'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_public_ip.pem'])
            config_file = 'tests/resources/config_for_test_update_public_ip'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('public_ip_group.command_name', 'public_ip')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdatePublicIp')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdatePublicIpDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdatePublicIp', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_public_ip.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdatePublicIp. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_public_ip.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_public_ip.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdatePublicIp',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'publicIp',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_public_ip.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_public_ip.pem')
                if os.path.exists('tests/resources/config_for_test_update_public_ip'):
                    os.remove('tests/resources/config_for_test_update_public_ip')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdatePublicIp')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_remote_peering_connection(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateRemotePeeringConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateRemotePeeringConnection')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_remote_peering_connection.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_remote_peering_connection', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_remote_peering_connection.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_remote_peering_connection'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_remote_peering_connection.pem'])
            config_file = 'tests/resources/config_for_test_update_remote_peering_connection'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('remote_peering_connection_group.command_name', 'remote_peering_connection')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateRemotePeeringConnection')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateRemotePeeringConnectionDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateRemotePeeringConnection', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_remote_peering_connection.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateRemotePeeringConnection. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_remote_peering_connection.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_remote_peering_connection.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateRemotePeeringConnection',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'remotePeeringConnection',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_remote_peering_connection.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_remote_peering_connection.pem')
                if os.path.exists('tests/resources/config_for_test_update_remote_peering_connection'):
                    os.remove('tests/resources/config_for_test_update_remote_peering_connection')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateRemotePeeringConnection')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_route_table(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateRouteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateRouteTable')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_route_table.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_route_table', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_route_table.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_route_table'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_route_table.pem'])
            config_file = 'tests/resources/config_for_test_update_route_table'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('route_table_group.command_name', 'route_table')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateRouteTable')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateRouteTableDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateRouteTable', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_route_table.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateRouteTable. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_route_table.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_route_table.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateRouteTable',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'routeTable',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_route_table.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_route_table.pem')
                if os.path.exists('tests/resources/config_for_test_update_route_table'):
                    os.remove('tests/resources/config_for_test_update_route_table')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateRouteTable')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_security_list(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateSecurityList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateSecurityList')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_security_list.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_security_list', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_security_list.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_security_list'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_security_list.pem'])
            config_file = 'tests/resources/config_for_test_update_security_list'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('security_list_group.command_name', 'security_list')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateSecurityList')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateSecurityListDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateSecurityList', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_security_list.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateSecurityList. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_security_list.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_security_list.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateSecurityList',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'securityList',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_security_list.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_security_list.pem')
                if os.path.exists('tests/resources/config_for_test_update_security_list'):
                    os.remove('tests/resources/config_for_test_update_security_list')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateSecurityList')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_service_gateway(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateServiceGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateServiceGateway')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_service_gateway.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_service_gateway', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_service_gateway.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_service_gateway'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_service_gateway.pem'])
            config_file = 'tests/resources/config_for_test_update_service_gateway'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('service_gateway_group.command_name', 'service_gateway')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateServiceGateway')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateServiceGatewayDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateServiceGateway', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_service_gateway.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateServiceGateway. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_service_gateway.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_service_gateway.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateServiceGateway',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'serviceGateway',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_service_gateway.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_service_gateway.pem')
                if os.path.exists('tests/resources/config_for_test_update_service_gateway'):
                    os.remove('tests/resources/config_for_test_update_service_gateway')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateServiceGateway')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_subnet(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateSubnet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateSubnet')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_subnet.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_subnet', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_subnet.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_subnet'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_subnet.pem'])
            config_file = 'tests/resources/config_for_test_update_subnet'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('subnet_group.command_name', 'subnet')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateSubnet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateSubnetDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateSubnet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_subnet.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateSubnet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_subnet.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_subnet.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateSubnet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'subnet',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_subnet.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_subnet.pem')
                if os.path.exists('tests/resources/config_for_test_update_subnet'):
                    os.remove('tests/resources/config_for_test_update_subnet')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateSubnet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_vcn(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateVcn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateVcn')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_vcn.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_vcn', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_vcn.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_vcn'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_vcn.pem'])
            config_file = 'tests/resources/config_for_test_update_vcn'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('vcn_group.command_name', 'vcn')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVcn')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateVcnDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateVcn', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_vcn.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateVcn. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_vcn.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_vcn.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateVcn',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'vcn',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_vcn.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_vcn.pem')
                if os.path.exists('tests/resources/config_for_test_update_vcn'):
                    os.remove('tests/resources/config_for_test_update_vcn')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVcn')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_virtual_circuit(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateVirtualCircuit'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateVirtualCircuit')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_virtual_circuit.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_virtual_circuit', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_virtual_circuit.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_virtual_circuit'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_virtual_circuit.pem'])
            config_file = 'tests/resources/config_for_test_update_virtual_circuit'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('virtual_circuit_group.command_name', 'virtual_circuit')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVirtualCircuit')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateVirtualCircuitDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateVirtualCircuit', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_virtual_circuit.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateVirtualCircuit. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_virtual_circuit.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_virtual_circuit.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateVirtualCircuit',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'virtualCircuit',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_virtual_circuit.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_virtual_circuit.pem')
                if os.path.exists('tests/resources/config_for_test_update_virtual_circuit'):
                    os.remove('tests/resources/config_for_test_update_virtual_circuit')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVirtualCircuit')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_vnic(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateVnic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('core', 'VirtualNetwork', 'UpdateVnic')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_vnic.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_vnic', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_vnic.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_vnic'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_vnic.pem'])
            config_file = 'tests/resources/config_for_test_update_vnic'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('virtual_network_root_group.command_name', 'virtual-network')
    resource_group_command_name = oci_cli.cli_util.override('vnic_group.command_name', 'vnic')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVnic')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateVnicDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateVnic', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_vnic.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateVnic. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_vnic.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_vnic.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateVnic',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'vnic',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_vnic.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_vnic.pem')
                if os.path.exists('tests/resources/config_for_test_update_vnic'):
                    os.remove('tests/resources/config_for_test_update_vnic')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateVnic')
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
