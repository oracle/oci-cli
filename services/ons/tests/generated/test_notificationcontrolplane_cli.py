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
    custom_vcr = test_config_container.create_vcr(cassette_library_dir="services/ons/tests/cassettes/for_generated")

    cassette_location = 'ons_{name}.yml'.format(name=request.function.__name__)
    with custom_vcr.use_cassette(cassette_location):
        yield


@pytest.mark.generated
def test_create_topic(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('ons', 'CreateTopic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('notification_control_plane_root_group.command_name', 'notification-control-plane')
    resource_group_command_name = oci_cli.cli_util.override('notification_topic_group.command_name', 'notification_topic')
    request_containers = cli_testing_service_client.get_requests(service_name='ons', api_name='CreateTopic')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateTopicDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('ons', 'CreateTopic', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_topic.command_name', 'create-topic'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: ons, CreateTopic. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_topic.command_name', 'create-topic'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_topic.command_name', 'create-topic')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'ons',
                    'CreateTopic',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'notificationTopic',
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
                request_containers = cli_testing_service_client.get_requests(service_name='ons', api_name='CreateTopic')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_topic(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('ons', 'DeleteTopic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('notification_control_plane_root_group.command_name', 'notification-control-plane')
    resource_group_command_name = oci_cli.cli_util.override('topic_group.command_name', 'topic')
    request_containers = cli_testing_service_client.get_requests(service_name='ons', api_name='DeleteTopic')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('ons', 'DeleteTopic', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_topic.command_name', 'delete'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: ons, DeleteTopic. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_topic.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_topic.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'ons',
                    'DeleteTopic',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteTopic',
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
                request_containers = cli_testing_service_client.get_requests(service_name='ons', api_name='DeleteTopic')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_topic(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('ons', 'GetTopic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('notification_control_plane_root_group.command_name', 'notification-control-plane')
    resource_group_command_name = oci_cli.cli_util.override('notification_topic_group.command_name', 'notification_topic')
    request_containers = cli_testing_service_client.get_requests(service_name='ons', api_name='GetTopic')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('ons', 'GetTopic', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_topic.command_name', 'get-topic'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: ons, GetTopic. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_topic.command_name', 'get-topic'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_topic.command_name', 'get-topic')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'ons',
                    'GetTopic',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'notificationTopic',
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
                request_containers = cli_testing_service_client.get_requests(service_name='ons', api_name='GetTopic')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_topics(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('ons', 'ListTopics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('notification_control_plane_root_group.command_name', 'notification-control-plane')
    resource_group_command_name = oci_cli.cli_util.override('notification_topic_group.command_name', 'notification_topic')
    request_containers = cli_testing_service_client.get_requests(service_name='ons', api_name='ListTopics')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('ons', 'ListTopics', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_topics.command_name', 'list-topics'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: ons, ListTopics. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_topics.command_name', 'list-topics'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_topics.command_name', 'list-topics')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'ons',
                    'ListTopics',
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
                request_containers = cli_testing_service_client.get_requests(service_name='ons', api_name='ListTopics')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_topic(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('ons', 'UpdateTopic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    root_command_name = oci_cli.cli_util.override('notification_control_plane_root_group.command_name', 'notification-control-plane')
    resource_group_command_name = oci_cli.cli_util.override('notification_topic_group.command_name', 'notification_topic')
    request_containers = cli_testing_service_client.get_requests(service_name='ons', api_name='UpdateTopic')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'TopicAttributesDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('ons', 'UpdateTopic', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_topic.command_name', 'update-topic'),
                    True
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: ons, UpdateTopic. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_topic.command_name', 'update-topic'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_topic.command_name', 'update-topic')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'ons',
                    'UpdateTopic',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'notificationTopic',
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
                request_containers = cli_testing_service_client.get_requests(service_name='ons', api_name='UpdateTopic')
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
