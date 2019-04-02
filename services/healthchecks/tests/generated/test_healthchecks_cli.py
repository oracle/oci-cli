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
    custom_vcr = test_config_container.create_vcr(cassette_library_dir="services/healthchecks/tests/cassettes/for_generated")

    cassette_location = 'healthchecks_{name}.yml'.format(name=request.function.__name__)
    with custom_vcr.use_cassette(cassette_location):
        yield


@pytest.mark.generated
def test_create_http_monitor(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('healthchecks', 'CreateHttpMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('healthchecks_root_group.command_name', 'healthchecks')
    resource_group_command_name = oci_cli.cli_util.override('http_monitor_group.command_name', 'http_monitor')
    request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='CreateHttpMonitor')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateHttpMonitorDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('healthchecks', 'CreateHttpMonitor', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_http_monitor.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: healthchecks, CreateHttpMonitor. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_http_monitor.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_http_monitor.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'healthchecks',
                    'CreateHttpMonitor',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'httpMonitor',
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
                request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='CreateHttpMonitor')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_on_demand_http_probe(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('healthchecks', 'CreateOnDemandHttpProbe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('healthchecks_root_group.command_name', 'healthchecks')
    resource_group_command_name = oci_cli.cli_util.override('http_probe_group.command_name', 'http_probe')
    request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='CreateOnDemandHttpProbe')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateOnDemandHttpProbeDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('healthchecks', 'CreateOnDemandHttpProbe', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_on_demand_http_probe.command_name', 'create-on-demand')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: healthchecks, CreateOnDemandHttpProbe. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_on_demand_http_probe.command_name', 'create-on-demand'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_on_demand_http_probe.command_name', 'create-on-demand')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'healthchecks',
                    'CreateOnDemandHttpProbe',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'httpProbe',
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
                request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='CreateOnDemandHttpProbe')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_on_demand_ping_probe(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('healthchecks', 'CreateOnDemandPingProbe'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('healthchecks_root_group.command_name', 'healthchecks')
    resource_group_command_name = oci_cli.cli_util.override('ping_probe_group.command_name', 'ping_probe')
    request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='CreateOnDemandPingProbe')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateOnDemandPingProbeDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('healthchecks', 'CreateOnDemandPingProbe', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_on_demand_ping_probe.command_name', 'create-on-demand')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: healthchecks, CreateOnDemandPingProbe. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_on_demand_ping_probe.command_name', 'create-on-demand'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_on_demand_ping_probe.command_name', 'create-on-demand')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'healthchecks',
                    'CreateOnDemandPingProbe',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'pingProbe',
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
                request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='CreateOnDemandPingProbe')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_ping_monitor(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('healthchecks', 'CreatePingMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('healthchecks_root_group.command_name', 'healthchecks')
    resource_group_command_name = oci_cli.cli_util.override('ping_monitor_group.command_name', 'ping_monitor')
    request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='CreatePingMonitor')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreatePingMonitorDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('healthchecks', 'CreatePingMonitor', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_ping_monitor.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: healthchecks, CreatePingMonitor. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_ping_monitor.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_ping_monitor.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'healthchecks',
                    'CreatePingMonitor',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'pingMonitor',
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
                request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='CreatePingMonitor')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_http_monitor(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('healthchecks', 'DeleteHttpMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('healthchecks_root_group.command_name', 'healthchecks')
    resource_group_command_name = oci_cli.cli_util.override('http_monitor_group.command_name', 'http_monitor')
    request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='DeleteHttpMonitor')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('healthchecks', 'DeleteHttpMonitor', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_http_monitor.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: healthchecks, DeleteHttpMonitor. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_http_monitor.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_http_monitor.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'healthchecks',
                    'DeleteHttpMonitor',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteHttpMonitor',
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
                request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='DeleteHttpMonitor')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_ping_monitor(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('healthchecks', 'DeletePingMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('healthchecks_root_group.command_name', 'healthchecks')
    resource_group_command_name = oci_cli.cli_util.override('ping_monitor_group.command_name', 'ping_monitor')
    request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='DeletePingMonitor')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('healthchecks', 'DeletePingMonitor', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_ping_monitor.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: healthchecks, DeletePingMonitor. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_ping_monitor.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_ping_monitor.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'healthchecks',
                    'DeletePingMonitor',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deletePingMonitor',
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
                request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='DeletePingMonitor')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_http_monitor(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('healthchecks', 'GetHttpMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('healthchecks_root_group.command_name', 'healthchecks')
    resource_group_command_name = oci_cli.cli_util.override('http_monitor_group.command_name', 'http_monitor')
    request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='GetHttpMonitor')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('healthchecks', 'GetHttpMonitor', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_http_monitor.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: healthchecks, GetHttpMonitor. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_http_monitor.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_http_monitor.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'healthchecks',
                    'GetHttpMonitor',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'httpMonitor',
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
                request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='GetHttpMonitor')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_ping_monitor(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('healthchecks', 'GetPingMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('healthchecks_root_group.command_name', 'healthchecks')
    resource_group_command_name = oci_cli.cli_util.override('ping_monitor_group.command_name', 'ping_monitor')
    request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='GetPingMonitor')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('healthchecks', 'GetPingMonitor', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_ping_monitor.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: healthchecks, GetPingMonitor. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_ping_monitor.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_ping_monitor.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'healthchecks',
                    'GetPingMonitor',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'pingMonitor',
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
                request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='GetPingMonitor')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_health_checks_vantage_points(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('healthchecks', 'ListHealthChecksVantagePoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('healthchecks_root_group.command_name', 'healthchecks')
    resource_group_command_name = oci_cli.cli_util.override('health_checks_vantage_point_group.command_name', 'health_checks_vantage_point')
    request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='ListHealthChecksVantagePoints')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('healthchecks', 'ListHealthChecksVantagePoints', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_health_checks_vantage_points.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: healthchecks, ListHealthChecksVantagePoints. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_health_checks_vantage_points.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_health_checks_vantage_points.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'healthchecks',
                    'ListHealthChecksVantagePoints',
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
                request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='ListHealthChecksVantagePoints')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_http_monitors(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('healthchecks', 'ListHttpMonitors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('healthchecks_root_group.command_name', 'healthchecks')
    resource_group_command_name = oci_cli.cli_util.override('http_monitor_group.command_name', 'http_monitor')
    request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='ListHttpMonitors')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('healthchecks', 'ListHttpMonitors', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_http_monitors.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: healthchecks, ListHttpMonitors. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_http_monitors.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_http_monitors.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'healthchecks',
                    'ListHttpMonitors',
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
                request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='ListHttpMonitors')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_http_probe_results(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('healthchecks', 'ListHttpProbeResults'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('healthchecks_root_group.command_name', 'healthchecks')
    resource_group_command_name = oci_cli.cli_util.override('http_probe_result_group.command_name', 'http_probe_result')
    request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='ListHttpProbeResults')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('healthchecks', 'ListHttpProbeResults', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_http_probe_results.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: healthchecks, ListHttpProbeResults. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_http_probe_results.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_http_probe_results.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'healthchecks',
                    'ListHttpProbeResults',
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
                request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='ListHttpProbeResults')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_ping_monitors(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('healthchecks', 'ListPingMonitors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('healthchecks_root_group.command_name', 'healthchecks')
    resource_group_command_name = oci_cli.cli_util.override('ping_monitor_group.command_name', 'ping_monitor')
    request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='ListPingMonitors')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('healthchecks', 'ListPingMonitors', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_ping_monitors.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: healthchecks, ListPingMonitors. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_ping_monitors.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_ping_monitors.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'healthchecks',
                    'ListPingMonitors',
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
                request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='ListPingMonitors')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_ping_probe_results(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('healthchecks', 'ListPingProbeResults'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('healthchecks_root_group.command_name', 'healthchecks')
    resource_group_command_name = oci_cli.cli_util.override('ping_probe_result_group.command_name', 'ping_probe_result')
    request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='ListPingProbeResults')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('healthchecks', 'ListPingProbeResults', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_ping_probe_results.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: healthchecks, ListPingProbeResults. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_ping_probe_results.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_ping_probe_results.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'healthchecks',
                    'ListPingProbeResults',
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
                request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='ListPingProbeResults')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_http_monitor(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('healthchecks', 'UpdateHttpMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('healthchecks_root_group.command_name', 'healthchecks')
    resource_group_command_name = oci_cli.cli_util.override('http_monitor_group.command_name', 'http_monitor')
    request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='UpdateHttpMonitor')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateHttpMonitorDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('healthchecks', 'UpdateHttpMonitor', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_http_monitor.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: healthchecks, UpdateHttpMonitor. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_http_monitor.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_http_monitor.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'healthchecks',
                    'UpdateHttpMonitor',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'httpMonitor',
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
                request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='UpdateHttpMonitor')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_ping_monitor(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('healthchecks', 'UpdatePingMonitor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('healthchecks_root_group.command_name', 'healthchecks')
    resource_group_command_name = oci_cli.cli_util.override('ping_monitor_group.command_name', 'ping_monitor')
    request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='UpdatePingMonitor')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdatePingMonitorDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('healthchecks', 'UpdatePingMonitor', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_ping_monitor.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: healthchecks, UpdatePingMonitor. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_ping_monitor.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_ping_monitor.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'healthchecks',
                    'UpdatePingMonitor',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'pingMonitor',
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
                request_containers = cli_testing_service_client.get_requests(service_name='healthchecks', api_name='UpdatePingMonitor')
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
