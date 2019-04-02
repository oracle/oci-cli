# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import json
import pytest
from tests import generated_test_request_transformers
from tests import test_config_container  # noqa: F401
from tests import util

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
def test_attach_load_balancer(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'AttachLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_pool_group.command_name', 'instance_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='AttachLoadBalancer')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'AttachLoadBalancerDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'AttachLoadBalancer', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('attach_load_balancer.command_name', 'attach'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, AttachLoadBalancer. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('attach_load_balancer.command_name', 'attach'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('attach_load_balancer.command_name', 'attach')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'AttachLoadBalancer',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'instancePool',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='AttachLoadBalancer')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_instance_configuration(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateInstanceConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_configuration_group.command_name', 'instance_configuration')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateInstanceConfiguration')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateInstanceConfiguration'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateInstanceConfiguration', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_instance_configuration.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateInstanceConfiguration. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_instance_configuration.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_instance_configuration.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateInstanceConfiguration',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'instanceConfiguration',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateInstanceConfiguration')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_instance_pool(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'CreateInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_pool_group.command_name', 'instance_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateInstancePool')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateInstancePoolDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'CreateInstancePool', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_instance_pool.command_name', 'create'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, CreateInstancePool. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_instance_pool.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_instance_pool.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'CreateInstancePool',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'instancePool',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='CreateInstancePool')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_instance_configuration(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DeleteInstanceConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_configuration_group.command_name', 'instance_configuration')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteInstanceConfiguration')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DeleteInstanceConfiguration', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_instance_configuration.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DeleteInstanceConfiguration. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_instance_configuration.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_instance_configuration.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DeleteInstanceConfiguration',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteInstanceConfiguration',
                    True
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DeleteInstanceConfiguration')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_detach_load_balancer(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'DetachLoadBalancer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_pool_group.command_name', 'instance_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DetachLoadBalancer')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'DetachLoadBalancerDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'DetachLoadBalancer', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('detach_load_balancer.command_name', 'detach'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, DetachLoadBalancer. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('detach_load_balancer.command_name', 'detach'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('detach_load_balancer.command_name', 'detach')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'DetachLoadBalancer',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'instancePool',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='DetachLoadBalancer')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_instance_configuration(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetInstanceConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_configuration_group.command_name', 'instance_configuration')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetInstanceConfiguration')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetInstanceConfiguration', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_instance_configuration.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetInstanceConfiguration. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_instance_configuration.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_instance_configuration.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetInstanceConfiguration',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'instanceConfiguration',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetInstanceConfiguration')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_instance_pool(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'GetInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_pool_group.command_name', 'instance_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetInstancePool')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'GetInstancePool', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_instance_pool.command_name', 'get'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, GetInstancePool. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_instance_pool.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_instance_pool.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'GetInstancePool',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'instancePool',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='GetInstancePool')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_launch_instance_configuration(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'LaunchInstanceConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_group.command_name', 'instance')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='LaunchInstanceConfiguration')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'InstanceConfiguration'
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

            if request.get('instanceType') == 'compute':
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('launch_instance_configuration_compute_instance_details.command_name', 'launch-instance-configuration-compute-instance-details')
                )

                if params:
                    del request['instanceType']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'LaunchInstanceConfiguration', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('launch_instance_configuration.command_name', 'launch-instance-configuration'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, LaunchInstanceConfiguration. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('launch_instance_configuration.command_name', 'launch-instance-configuration'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('launch_instance_configuration.command_name', 'launch-instance-configuration')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'LaunchInstanceConfiguration',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'instance',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='LaunchInstanceConfiguration')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_instance_configurations(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListInstanceConfigurations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_configuration_group.command_name', 'instance_configuration')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListInstanceConfigurations')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListInstanceConfigurations', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_instance_configurations.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListInstanceConfigurations. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_instance_configurations.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_instance_configurations.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListInstanceConfigurations',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListInstanceConfigurations')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_instance_pool_instances(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListInstancePoolInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_group.command_name', 'instance')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListInstancePoolInstances')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListInstancePoolInstances', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_instance_pool_instances.command_name', 'list-instance-pool-instances'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListInstancePoolInstances. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_instance_pool_instances.command_name', 'list-instance-pool-instances'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_instance_pool_instances.command_name', 'list-instance-pool-instances')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListInstancePoolInstances',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListInstancePoolInstances')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_instance_pools(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ListInstancePools'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_pool_group.command_name', 'instance_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListInstancePools')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ListInstancePools', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_instance_pools.command_name', 'list'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ListInstancePools. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_instance_pools.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_instance_pools.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ListInstancePools',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ListInstancePools')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_reset_instance_pool(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'ResetInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_pool_group.command_name', 'instance_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ResetInstancePool')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'ResetInstancePool', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('reset_instance_pool.command_name', 'reset'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, ResetInstancePool. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('reset_instance_pool.command_name', 'reset'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('reset_instance_pool.command_name', 'reset')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'ResetInstancePool',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'instancePool',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='ResetInstancePool')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_softreset_instance_pool(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'SoftresetInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_pool_group.command_name', 'instance_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='SoftresetInstancePool')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'SoftresetInstancePool', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('softreset_instance_pool.command_name', 'softreset'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, SoftresetInstancePool. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('softreset_instance_pool.command_name', 'softreset'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('softreset_instance_pool.command_name', 'softreset')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'SoftresetInstancePool',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'instancePool',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='SoftresetInstancePool')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_start_instance_pool(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'StartInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_pool_group.command_name', 'instance_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='StartInstancePool')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'StartInstancePool', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('start_instance_pool.command_name', 'start'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, StartInstancePool. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('start_instance_pool.command_name', 'start'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('start_instance_pool.command_name', 'start')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'StartInstancePool',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'instancePool',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='StartInstancePool')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_stop_instance_pool(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'StopInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_pool_group.command_name', 'instance_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='StopInstancePool')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'StopInstancePool', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('stop_instance_pool.command_name', 'stop'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, StopInstancePool. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('stop_instance_pool.command_name', 'stop'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('stop_instance_pool.command_name', 'stop')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'StopInstancePool',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'instancePool',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='StopInstancePool')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_terminate_instance_pool(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'TerminateInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_pool_group.command_name', 'instance_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='TerminateInstancePool')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'TerminateInstancePool', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('terminate_instance_pool.command_name', 'terminate'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, TerminateInstancePool. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('terminate_instance_pool.command_name', 'terminate'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('terminate_instance_pool.command_name', 'terminate')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'TerminateInstancePool',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'terminateInstancePool',
                    True
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='TerminateInstancePool')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_instance_configuration(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateInstanceConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_configuration_group.command_name', 'instance_configuration')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateInstanceConfiguration')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateInstanceConfigurationDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateInstanceConfiguration', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_instance_configuration.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateInstanceConfiguration. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_instance_configuration.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_instance_configuration.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateInstanceConfiguration',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'instanceConfiguration',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateInstanceConfiguration')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_instance_pool(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('core', 'UpdateInstancePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('compute_management_root_group.command_name', 'compute-management')
    resource_group_command_name = oci_cli.cli_util.override('instance_pool_group.command_name', 'instance_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateInstancePool')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateInstancePoolDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('core', 'UpdateInstancePool', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_instance_pool.command_name', 'update'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: core, UpdateInstancePool. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_instance_pool.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_instance_pool.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'core',
                    'UpdateInstancePool',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'instancePool',
                    False
                )
            finally:
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='core', api_name='UpdateInstancePool')
                request = request_containers[i]['request'].copy()


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = ['--config-file', os.environ['OCI_CLI_CONFIG_FILE']]

    if config_profile:
        root_params.extend(['--profile', config_profile])

    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug'] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + params, ** args)

    return result
