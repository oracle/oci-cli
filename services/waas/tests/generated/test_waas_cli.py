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
    custom_vcr = test_config_container.create_vcr(cassette_library_dir="services/waas/tests/cassettes/for_generated")

    cassette_location = 'waas_{name}.yml'.format(name=request.function.__name__)
    with custom_vcr.use_cassette(cassette_location):
        yield


@pytest.mark.generated
def test_accept_recommendations(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'AcceptRecommendations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('recommendation_group.command_name', 'recommendation')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='AcceptRecommendations')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'AcceptRecommendations', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('accept_recommendations.command_name', 'accept')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, AcceptRecommendations. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('accept_recommendations.command_name', 'accept'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('accept_recommendations.command_name', 'accept')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'AcceptRecommendations',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'acceptRecommendations',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='AcceptRecommendations')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_cancel_work_request(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'CancelWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('work_request_group.command_name', 'work_request')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='CancelWorkRequest')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'CancelWorkRequest', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('cancel_work_request.command_name', 'cancel')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, CancelWorkRequest. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('cancel_work_request.command_name', 'cancel'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('cancel_work_request.command_name', 'cancel')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'CancelWorkRequest',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'cancelWorkRequest',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='CancelWorkRequest')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_certificate(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'CreateCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('certificate_group.command_name', 'certificate')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='CreateCertificate')
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'CreateCertificate', request)

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
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, CreateCertificate. '
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
                    'waas',
                    'CreateCertificate',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'certificate',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='CreateCertificate')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_waas_policy(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'CreateWaasPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('waas_policy_group.command_name', 'waas_policy')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='CreateWaasPolicy')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateWaasPolicyDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'CreateWaasPolicy', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_waas_policy.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, CreateWaasPolicy. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_waas_policy.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_waas_policy.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'CreateWaasPolicy',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'createWaasPolicy',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='CreateWaasPolicy')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_certificate(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'DeleteCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('certificate_group.command_name', 'certificate')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='DeleteCertificate')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'DeleteCertificate', request)

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
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, DeleteCertificate. '
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
                    'waas',
                    'DeleteCertificate',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteCertificate',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='DeleteCertificate')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_waas_policy(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'DeleteWaasPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('waas_policy_group.command_name', 'waas_policy')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='DeleteWaasPolicy')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'DeleteWaasPolicy', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_waas_policy.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, DeleteWaasPolicy. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_waas_policy.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_waas_policy.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'DeleteWaasPolicy',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteWaasPolicy',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='DeleteWaasPolicy')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_certificate(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'GetCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('certificate_group.command_name', 'certificate')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetCertificate')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'GetCertificate', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_certificate.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, GetCertificate. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_certificate.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_certificate.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'GetCertificate',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'certificate',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetCertificate')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_device_fingerprint_challenge(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'GetDeviceFingerprintChallenge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('device_fingerprint_challenge_group.command_name', 'device_fingerprint_challenge')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetDeviceFingerprintChallenge')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'GetDeviceFingerprintChallenge', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_device_fingerprint_challenge.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, GetDeviceFingerprintChallenge. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_device_fingerprint_challenge.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_device_fingerprint_challenge.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'GetDeviceFingerprintChallenge',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deviceFingerprintChallenge',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetDeviceFingerprintChallenge')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_human_interaction_challenge(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'GetHumanInteractionChallenge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('human_interaction_challenge_group.command_name', 'human_interaction_challenge')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetHumanInteractionChallenge')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'GetHumanInteractionChallenge', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_human_interaction_challenge.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, GetHumanInteractionChallenge. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_human_interaction_challenge.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_human_interaction_challenge.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'GetHumanInteractionChallenge',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'humanInteractionChallenge',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetHumanInteractionChallenge')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_js_challenge(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'GetJsChallenge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('js_challenge_group.command_name', 'js_challenge')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetJsChallenge')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'GetJsChallenge', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_js_challenge.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, GetJsChallenge. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_js_challenge.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_js_challenge.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'GetJsChallenge',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'jsChallenge',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetJsChallenge')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_policy_config(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'GetPolicyConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('policy_config_group.command_name', 'policy_config')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetPolicyConfig')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'GetPolicyConfig', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_policy_config.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, GetPolicyConfig. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_policy_config.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_policy_config.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'GetPolicyConfig',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'policyConfig',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetPolicyConfig')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_protection_rule(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'GetProtectionRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('protection_rule_group.command_name', 'protection_rule')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetProtectionRule')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'GetProtectionRule', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_protection_rule.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, GetProtectionRule. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_protection_rule.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_protection_rule.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'GetProtectionRule',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'protectionRule',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetProtectionRule')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_protection_settings(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'GetProtectionSettings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('protection_settings_group.command_name', 'protection_settings')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetProtectionSettings')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'GetProtectionSettings', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_protection_settings.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, GetProtectionSettings. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_protection_settings.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_protection_settings.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'GetProtectionSettings',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'protectionSettings',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetProtectionSettings')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_waas_policy(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'GetWaasPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('waas_policy_group.command_name', 'waas_policy')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetWaasPolicy')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'GetWaasPolicy', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_waas_policy.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, GetWaasPolicy. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_waas_policy.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_waas_policy.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'GetWaasPolicy',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'waasPolicy',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetWaasPolicy')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_waf_address_rate_limiting(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'GetWafAddressRateLimiting'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('address_rate_limiting_group.command_name', 'address_rate_limiting')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetWafAddressRateLimiting')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'GetWafAddressRateLimiting', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_waf_address_rate_limiting.command_name', 'get-waf')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, GetWafAddressRateLimiting. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_waf_address_rate_limiting.command_name', 'get-waf'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_waf_address_rate_limiting.command_name', 'get-waf')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'GetWafAddressRateLimiting',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'addressRateLimiting',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetWafAddressRateLimiting')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_waf_config(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'GetWafConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('waf_config_group.command_name', 'waf_config')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetWafConfig')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'GetWafConfig', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_waf_config.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, GetWafConfig. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_waf_config.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_waf_config.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'GetWafConfig',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'wafConfig',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetWafConfig')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_work_request(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('work_request_group.command_name', 'work_request')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetWorkRequest')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'GetWorkRequest', request)

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
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, GetWorkRequest. '
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
                    'waas',
                    'GetWorkRequest',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'workRequest',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='GetWorkRequest')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_access_rules(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'ListAccessRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('access_rule_group.command_name', 'access_rule')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListAccessRules')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'ListAccessRules', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_access_rules.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, ListAccessRules. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_access_rules.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_access_rules.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'ListAccessRules',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListAccessRules')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_captchas(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'ListCaptchas'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('captcha_group.command_name', 'captcha')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListCaptchas')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'ListCaptchas', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_captchas.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, ListCaptchas. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_captchas.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_captchas.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'ListCaptchas',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListCaptchas')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_certificates(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'ListCertificates'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('certificate_group.command_name', 'certificate')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListCertificates')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'ListCertificates', request)

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
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, ListCertificates. '
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
                    'waas',
                    'ListCertificates',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListCertificates')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_edge_subnets(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'ListEdgeSubnets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('edge_subnet_group.command_name', 'edge_subnet')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListEdgeSubnets')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'ListEdgeSubnets', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_edge_subnets.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, ListEdgeSubnets. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_edge_subnets.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_edge_subnets.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'ListEdgeSubnets',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListEdgeSubnets')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_good_bots(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'ListGoodBots'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('good_bot_group.command_name', 'good_bot')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListGoodBots')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'ListGoodBots', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_good_bots.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, ListGoodBots. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_good_bots.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_good_bots.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'ListGoodBots',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListGoodBots')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_protection_rules(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'ListProtectionRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('protection_rule_group.command_name', 'protection_rule')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListProtectionRules')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'ListProtectionRules', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_protection_rules.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, ListProtectionRules. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_protection_rules.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_protection_rules.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'ListProtectionRules',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListProtectionRules')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_recommendations(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'ListRecommendations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('recommendation_group.command_name', 'recommendation')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListRecommendations')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'ListRecommendations', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_recommendations.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, ListRecommendations. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_recommendations.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_recommendations.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'ListRecommendations',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListRecommendations')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_threat_feeds(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'ListThreatFeeds'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('threat_feed_group.command_name', 'threat_feed')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListThreatFeeds')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'ListThreatFeeds', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_threat_feeds.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, ListThreatFeeds. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_threat_feeds.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_threat_feeds.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'ListThreatFeeds',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListThreatFeeds')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_waas_policies(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'ListWaasPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('waas_policy_group.command_name', 'waas_policy')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListWaasPolicies')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'ListWaasPolicies', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_waas_policies.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, ListWaasPolicies. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_waas_policies.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_waas_policies.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'ListWaasPolicies',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListWaasPolicies')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_waf_blocked_requests(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'ListWafBlockedRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('waf_blocked_request_group.command_name', 'waf_blocked_request')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListWafBlockedRequests')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'ListWafBlockedRequests', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_waf_blocked_requests.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, ListWafBlockedRequests. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_waf_blocked_requests.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_waf_blocked_requests.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'ListWafBlockedRequests',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListWafBlockedRequests')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_waf_logs(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'ListWafLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('waf_log_group.command_name', 'waf_log')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListWafLogs')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'ListWafLogs', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_waf_logs.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, ListWafLogs. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_waf_logs.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_waf_logs.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'ListWafLogs',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListWafLogs')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_waf_requests(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'ListWafRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('waf_request_group.command_name', 'waf_request')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListWafRequests')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'ListWafRequests', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_waf_requests.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, ListWafRequests. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_waf_requests.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_waf_requests.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'ListWafRequests',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListWafRequests')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_waf_traffic(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'ListWafTraffic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('waf_traffic_datum_group.command_name', 'waf_traffic_datum')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListWafTraffic')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'ListWafTraffic', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_waf_traffic.command_name', 'list-waf-traffic')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, ListWafTraffic. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_waf_traffic.command_name', 'list-waf-traffic'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_waf_traffic.command_name', 'list-waf-traffic')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'ListWafTraffic',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListWafTraffic')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_whitelists(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'ListWhitelists'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('whitelist_group.command_name', 'whitelist')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListWhitelists')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'ListWhitelists', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_whitelists.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, ListWhitelists. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_whitelists.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_whitelists.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'ListWhitelists',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListWhitelists')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_work_requests(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('work_request_group.command_name', 'work_request')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListWorkRequests')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'ListWorkRequests', request)

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
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, ListWorkRequests. '
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
                    'waas',
                    'ListWorkRequests',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='ListWorkRequests')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_access_rules(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'UpdateAccessRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('access_rule_group.command_name', 'access_rule')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateAccessRules')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'UpdateAccessRules', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_access_rules.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, UpdateAccessRules. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_access_rules.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_access_rules.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'UpdateAccessRules',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateAccessRules',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateAccessRules')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_captchas(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'UpdateCaptchas'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('captcha_group.command_name', 'captcha')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateCaptchas')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'UpdateCaptchas', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_captchas.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, UpdateCaptchas. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_captchas.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_captchas.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'UpdateCaptchas',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateCaptchas',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateCaptchas')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_certificate(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'UpdateCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('certificate_group.command_name', 'certificate')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateCertificate')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateCertificateDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'UpdateCertificate', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_certificate.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, UpdateCertificate. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_certificate.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_certificate.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'UpdateCertificate',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'certificate',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateCertificate')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_device_fingerprint_challenge(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'UpdateDeviceFingerprintChallenge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('device_fingerprint_challenge_group.command_name', 'device_fingerprint_challenge')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateDeviceFingerprintChallenge')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateDeviceFingerprintChallengeDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'UpdateDeviceFingerprintChallenge', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_device_fingerprint_challenge.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, UpdateDeviceFingerprintChallenge. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_device_fingerprint_challenge.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_device_fingerprint_challenge.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'UpdateDeviceFingerprintChallenge',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateDeviceFingerprintChallenge',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateDeviceFingerprintChallenge')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_good_bots(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'UpdateGoodBots'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('good_bot_group.command_name', 'good_bot')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateGoodBots')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'UpdateGoodBots', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_good_bots.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, UpdateGoodBots. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_good_bots.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_good_bots.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'UpdateGoodBots',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateGoodBots',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateGoodBots')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_human_interaction_challenge(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'UpdateHumanInteractionChallenge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('human_interaction_challenge_group.command_name', 'human_interaction_challenge')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateHumanInteractionChallenge')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateHumanInteractionChallengeDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'UpdateHumanInteractionChallenge', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_human_interaction_challenge.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, UpdateHumanInteractionChallenge. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_human_interaction_challenge.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_human_interaction_challenge.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'UpdateHumanInteractionChallenge',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateHumanInteractionChallenge',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateHumanInteractionChallenge')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_js_challenge(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'UpdateJsChallenge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('js_challenge_group.command_name', 'js_challenge')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateJsChallenge')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateJsChallengeDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'UpdateJsChallenge', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_js_challenge.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, UpdateJsChallenge. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_js_challenge.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_js_challenge.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'UpdateJsChallenge',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateJsChallenge',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateJsChallenge')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_policy_config(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'UpdatePolicyConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('policy_config_group.command_name', 'policy_config')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdatePolicyConfig')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdatePolicyConfigDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'UpdatePolicyConfig', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_policy_config.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, UpdatePolicyConfig. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_policy_config.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_policy_config.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'UpdatePolicyConfig',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updatePolicyConfig',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdatePolicyConfig')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_protection_rules(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'UpdateProtectionRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('protection_rule_group.command_name', 'protection_rule')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateProtectionRules')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'UpdateProtectionRules', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_protection_rules.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, UpdateProtectionRules. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_protection_rules.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_protection_rules.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'UpdateProtectionRules',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateProtectionRules',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateProtectionRules')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_protection_settings(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'UpdateProtectionSettings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('protection_settings_group.command_name', 'protection_settings')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateProtectionSettings')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateProtectionSettingsDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'UpdateProtectionSettings', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_protection_settings.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, UpdateProtectionSettings. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_protection_settings.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_protection_settings.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'UpdateProtectionSettings',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateProtectionSettings',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateProtectionSettings')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_threat_feeds(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'UpdateThreatFeeds'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('threat_feed_group.command_name', 'threat_feed')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateThreatFeeds')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'UpdateThreatFeeds', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_threat_feeds.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, UpdateThreatFeeds. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_threat_feeds.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_threat_feeds.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'UpdateThreatFeeds',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateThreatFeeds',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateThreatFeeds')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_waas_policy(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'UpdateWaasPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('waas_policy_group.command_name', 'waas_policy')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateWaasPolicy')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateWaasPolicyDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'UpdateWaasPolicy', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_waas_policy.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, UpdateWaasPolicy. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_waas_policy.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_waas_policy.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'UpdateWaasPolicy',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateWaasPolicy',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateWaasPolicy')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_waf_address_rate_limiting(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'UpdateWafAddressRateLimiting'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('address_rate_limiting_group.command_name', 'address_rate_limiting')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateWafAddressRateLimiting')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateWafAddressRateLimitingDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'UpdateWafAddressRateLimiting', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_waf_address_rate_limiting.command_name', 'update-waf')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, UpdateWafAddressRateLimiting. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_waf_address_rate_limiting.command_name', 'update-waf'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_waf_address_rate_limiting.command_name', 'update-waf')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'UpdateWafAddressRateLimiting',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateWafAddressRateLimiting',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateWafAddressRateLimiting')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_waf_config(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'UpdateWafConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('waf_config_group.command_name', 'waf_config')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateWafConfig')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateWafConfigDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'UpdateWafConfig', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_waf_config.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, UpdateWafConfig. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_waf_config.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_waf_config.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'UpdateWafConfig',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateWafConfig',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateWafConfig')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_whitelists(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('waas', 'UpdateWhitelists'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('waas_root_group.command_name', 'waas')
    resource_group_command_name = oci_cli.cli_util.override('whitelist_group.command_name', 'whitelist')
    request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateWhitelists')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('waas', 'UpdateWhitelists', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_whitelists.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: waas, UpdateWhitelists. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_whitelists.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_whitelists.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'waas',
                    'UpdateWhitelists',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateWhitelists',
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
                request_containers = cli_testing_service_client.get_requests(service_name='waas', api_name='UpdateWhitelists')
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
