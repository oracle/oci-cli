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
    custom_vcr = test_config_container.create_vcr(cassette_library_dir="services/dns/tests/cassettes/for_generated")

    cassette_location = 'dns_{name}.yml'.format(name=request.function.__name__)
    with custom_vcr.use_cassette(cassette_location):
        yield


@pytest.mark.generated
def test_create_steering_policy(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'CreateSteeringPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('steering_policy_group.command_name', 'steering_policy')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='CreateSteeringPolicy')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateSteeringPolicyDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'CreateSteeringPolicy', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_steering_policy.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, CreateSteeringPolicy. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_steering_policy.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_steering_policy.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'CreateSteeringPolicy',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'steeringPolicy',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='CreateSteeringPolicy')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_steering_policy_attachment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'CreateSteeringPolicyAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('steering_policy_attachment_group.command_name', 'steering_policy_attachment')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='CreateSteeringPolicyAttachment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateSteeringPolicyAttachmentDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'CreateSteeringPolicyAttachment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_steering_policy_attachment.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, CreateSteeringPolicyAttachment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_steering_policy_attachment.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_steering_policy_attachment.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'CreateSteeringPolicyAttachment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'steeringPolicyAttachment',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='CreateSteeringPolicyAttachment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_zone(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'CreateZone'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('zone_group.command_name', 'zone')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='CreateZone')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateZoneDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'CreateZone', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_zone.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, CreateZone. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_zone.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_zone.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'CreateZone',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'zone',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='CreateZone')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_domain_records(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'DeleteDomainRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('records_group.command_name', 'records')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='DeleteDomainRecords')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'DeleteDomainRecords', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_domain_records.command_name', 'delete-domain')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, DeleteDomainRecords. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_domain_records.command_name', 'delete-domain'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_domain_records.command_name', 'delete-domain')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'DeleteDomainRecords',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteDomainRecords',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='DeleteDomainRecords')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_rr_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'DeleteRRSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('rr_set_group.command_name', 'rr_set')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='DeleteRRSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'DeleteRRSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_rr_set.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, DeleteRRSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_rr_set.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_rr_set.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'DeleteRRSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteRRSet',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='DeleteRRSet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_steering_policy(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'DeleteSteeringPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('steering_policy_group.command_name', 'steering_policy')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='DeleteSteeringPolicy')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'DeleteSteeringPolicy', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_steering_policy.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, DeleteSteeringPolicy. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_steering_policy.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_steering_policy.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'DeleteSteeringPolicy',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteSteeringPolicy',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='DeleteSteeringPolicy')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_steering_policy_attachment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'DeleteSteeringPolicyAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('steering_policy_attachment_group.command_name', 'steering_policy_attachment')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='DeleteSteeringPolicyAttachment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'DeleteSteeringPolicyAttachment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_steering_policy_attachment.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, DeleteSteeringPolicyAttachment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_steering_policy_attachment.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_steering_policy_attachment.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'DeleteSteeringPolicyAttachment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteSteeringPolicyAttachment',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='DeleteSteeringPolicyAttachment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_zone(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'DeleteZone'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('zone_group.command_name', 'zone')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='DeleteZone')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'DeleteZone', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_zone.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, DeleteZone. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_zone.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_zone.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'DeleteZone',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteZone',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='DeleteZone')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_domain_records(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'GetDomainRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('records_group.command_name', 'records')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='GetDomainRecords')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'GetDomainRecords', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_domain_records.command_name', 'get-domain')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, GetDomainRecords. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_domain_records.command_name', 'get-domain'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_domain_records.command_name', 'get-domain')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'GetDomainRecords',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'recordCollection',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='GetDomainRecords')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_rr_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'GetRRSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('rr_set_group.command_name', 'rr_set')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='GetRRSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'GetRRSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_rr_set.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, GetRRSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_rr_set.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_rr_set.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'GetRRSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'rRSet',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='GetRRSet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_steering_policy(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'GetSteeringPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('steering_policy_group.command_name', 'steering_policy')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='GetSteeringPolicy')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'GetSteeringPolicy', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_steering_policy.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, GetSteeringPolicy. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_steering_policy.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_steering_policy.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'GetSteeringPolicy',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'steeringPolicy',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='GetSteeringPolicy')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_steering_policy_attachment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'GetSteeringPolicyAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('steering_policy_attachment_group.command_name', 'steering_policy_attachment')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='GetSteeringPolicyAttachment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'GetSteeringPolicyAttachment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_steering_policy_attachment.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, GetSteeringPolicyAttachment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_steering_policy_attachment.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_steering_policy_attachment.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'GetSteeringPolicyAttachment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'steeringPolicyAttachment',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='GetSteeringPolicyAttachment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_zone(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'GetZone'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('zones_group.command_name', 'zones')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='GetZone')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'GetZone', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_zone.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, GetZone. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_zone.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_zone.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'GetZone',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'zone',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='GetZone')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_zone_records(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'GetZoneRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('records_group.command_name', 'records')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='GetZoneRecords')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'GetZoneRecords', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_zone_records.command_name', 'get-zone')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, GetZoneRecords. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_zone_records.command_name', 'get-zone'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_zone_records.command_name', 'get-zone')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'GetZoneRecords',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'recordCollection',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='GetZoneRecords')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_steering_policies(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'ListSteeringPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('steering_policy_group.command_name', 'steering_policy')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='ListSteeringPolicies')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'ListSteeringPolicies', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_steering_policies.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, ListSteeringPolicies. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_steering_policies.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_steering_policies.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'ListSteeringPolicies',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='ListSteeringPolicies')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_steering_policy_attachments(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'ListSteeringPolicyAttachments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('steering_policy_attachment_group.command_name', 'steering_policy_attachment')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='ListSteeringPolicyAttachments')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'ListSteeringPolicyAttachments', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_steering_policy_attachments.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, ListSteeringPolicyAttachments. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_steering_policy_attachments.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_steering_policy_attachments.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'ListSteeringPolicyAttachments',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='ListSteeringPolicyAttachments')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_zones(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'ListZones'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('zones_group.command_name', 'zones')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='ListZones')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'ListZones', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_zones.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, ListZones. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_zones.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_zones.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'ListZones',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='ListZones')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_patch_domain_records(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'PatchDomainRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('records_group.command_name', 'records')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='PatchDomainRecords')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'PatchDomainRecordsDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'PatchDomainRecords', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('patch_domain_records.command_name', 'patch-domain')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, PatchDomainRecords. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('patch_domain_records.command_name', 'patch-domain'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('patch_domain_records.command_name', 'patch-domain')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'PatchDomainRecords',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'recordCollection',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='PatchDomainRecords')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_patch_rr_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'PatchRRSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('rr_set_group.command_name', 'rr_set')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='PatchRRSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'PatchRRSetDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'PatchRRSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('patch_rr_set.command_name', 'patch')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, PatchRRSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('patch_rr_set.command_name', 'patch'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('patch_rr_set.command_name', 'patch')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'PatchRRSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'recordCollection',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='PatchRRSet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_patch_zone_records(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'PatchZoneRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('records_group.command_name', 'records')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='PatchZoneRecords')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'PatchZoneRecordsDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'PatchZoneRecords', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('patch_zone_records.command_name', 'patch-zone')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, PatchZoneRecords. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('patch_zone_records.command_name', 'patch-zone'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('patch_zone_records.command_name', 'patch-zone')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'PatchZoneRecords',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'recordCollection',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='PatchZoneRecords')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_domain_records(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'UpdateDomainRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('records_group.command_name', 'records')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='UpdateDomainRecords')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateDomainRecordsDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'UpdateDomainRecords', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_domain_records.command_name', 'update-domain')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, UpdateDomainRecords. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_domain_records.command_name', 'update-domain'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_domain_records.command_name', 'update-domain')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'UpdateDomainRecords',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'recordCollection',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='UpdateDomainRecords')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_rr_set(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'UpdateRRSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('record_collection_group.command_name', 'record_collection')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='UpdateRRSet')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateRRSetDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'UpdateRRSet', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_rr_set.command_name', 'update-rr-set')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, UpdateRRSet. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_rr_set.command_name', 'update-rr-set'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_rr_set.command_name', 'update-rr-set')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'UpdateRRSet',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'recordCollection',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='UpdateRRSet')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_steering_policy(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'UpdateSteeringPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('steering_policy_group.command_name', 'steering_policy')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='UpdateSteeringPolicy')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateSteeringPolicyDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'UpdateSteeringPolicy', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_steering_policy.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, UpdateSteeringPolicy. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_steering_policy.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_steering_policy.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'UpdateSteeringPolicy',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'steeringPolicy',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='UpdateSteeringPolicy')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_steering_policy_attachment(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'UpdateSteeringPolicyAttachment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('steering_policy_attachment_group.command_name', 'steering_policy_attachment')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='UpdateSteeringPolicyAttachment')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateSteeringPolicyAttachmentDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'UpdateSteeringPolicyAttachment', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_steering_policy_attachment.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, UpdateSteeringPolicyAttachment. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_steering_policy_attachment.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_steering_policy_attachment.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'UpdateSteeringPolicyAttachment',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'steeringPolicyAttachment',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='UpdateSteeringPolicyAttachment')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_zone(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'UpdateZone'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('zone_group.command_name', 'zone')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='UpdateZone')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateZoneDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'UpdateZone', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_zone.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, UpdateZone. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_zone.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_zone.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'UpdateZone',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'zone',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='UpdateZone')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_zone_records(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('dns', 'UpdateZoneRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('dns_root_group.command_name', 'dns')
    resource_group_command_name = oci_cli.cli_util.override('records_group.command_name', 'records')
    request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='UpdateZoneRecords')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateZoneRecordsDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('dns', 'UpdateZoneRecords', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_zone_records.command_name', 'update-zone')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: dns, UpdateZoneRecords. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_zone_records.command_name', 'update-zone'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_zone_records.command_name', 'update-zone')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'dns',
                    'UpdateZoneRecords',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'recordCollection',
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
                request_containers = cli_testing_service_client.get_requests(service_name='dns', api_name='UpdateZoneRecords')
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
