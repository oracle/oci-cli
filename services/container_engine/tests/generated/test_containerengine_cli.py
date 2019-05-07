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
    custom_vcr = test_config_container.create_vcr(cassette_library_dir="services/container_engine/tests/cassettes/for_generated")

    cassette_location = 'container_engine_{name}.yml'.format(name=request.function.__name__)
    with custom_vcr.use_cassette(cassette_location):
        yield


@pytest.mark.generated
def test_create_cluster(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'CreateCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'CreateCluster')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_cluster.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_cluster', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_cluster.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_cluster'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_cluster.pem'])
            config_file = 'tests/resources/config_for_test_create_cluster'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('cluster_group.command_name', 'cluster')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='CreateCluster')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateClusterDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'CreateCluster', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_cluster.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, CreateCluster. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_cluster.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_cluster.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'container_engine',
                    'CreateCluster',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'createCluster',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_cluster.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_cluster.pem')
                if os.path.exists('tests/resources/config_for_test_create_cluster'):
                    os.remove('tests/resources/config_for_test_create_cluster')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='CreateCluster')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_kubeconfig(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'CreateKubeconfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'CreateKubeconfig')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_kubeconfig.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_kubeconfig', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_kubeconfig.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_kubeconfig'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_kubeconfig.pem'])
            config_file = 'tests/resources/config_for_test_create_kubeconfig'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('cluster_group.command_name', 'cluster')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='CreateKubeconfig')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateClusterKubeconfigContentDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'CreateKubeconfig', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_kubeconfig.command_name', 'create-kubeconfig')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, CreateKubeconfig. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_kubeconfig.command_name', 'create-kubeconfig'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_kubeconfig.command_name', 'create-kubeconfig')))

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
                    'container_engine',
                    'CreateKubeconfig',
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
                if os.path.exists('tests/resources/keyfile_for_test_create_kubeconfig.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_kubeconfig.pem')
                if os.path.exists('tests/resources/config_for_test_create_kubeconfig'):
                    os.remove('tests/resources/config_for_test_create_kubeconfig')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='CreateKubeconfig')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_create_node_pool(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'CreateNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'CreateNodePool')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_create_node_pool.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_create_node_pool', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_create_node_pool.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_create_node_pool'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_create_node_pool.pem'])
            config_file = 'tests/resources/config_for_test_create_node_pool'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('node_pool_group.command_name', 'node_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='CreateNodePool')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'CreateNodePoolDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'CreateNodePool', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('create_node_pool.command_name', 'create')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, CreateNodePool. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_node_pool.command_name', 'create'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('create_node_pool.command_name', 'create')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'container_engine',
                    'CreateNodePool',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'createNodePool',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_create_node_pool.pem'):
                    os.remove('tests/resources/keyfile_for_test_create_node_pool.pem')
                if os.path.exists('tests/resources/config_for_test_create_node_pool'):
                    os.remove('tests/resources/config_for_test_create_node_pool')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='CreateNodePool')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_cluster(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'DeleteCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'DeleteCluster')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_cluster.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_cluster', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_cluster.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_cluster'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_cluster.pem'])
            config_file = 'tests/resources/config_for_test_delete_cluster'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('cluster_group.command_name', 'cluster')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='DeleteCluster')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'DeleteCluster', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_cluster.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, DeleteCluster. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_cluster.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_cluster.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'container_engine',
                    'DeleteCluster',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteCluster',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_cluster.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_cluster.pem')
                if os.path.exists('tests/resources/config_for_test_delete_cluster'):
                    os.remove('tests/resources/config_for_test_delete_cluster')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='DeleteCluster')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_node_pool(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'DeleteNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'DeleteNodePool')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_node_pool.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_node_pool', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_node_pool.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_node_pool'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_node_pool.pem'])
            config_file = 'tests/resources/config_for_test_delete_node_pool'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('node_pool_group.command_name', 'node_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='DeleteNodePool')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'DeleteNodePool', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_node_pool.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, DeleteNodePool. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_node_pool.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_node_pool.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'container_engine',
                    'DeleteNodePool',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteNodePool',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_node_pool.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_node_pool.pem')
                if os.path.exists('tests/resources/config_for_test_delete_node_pool'):
                    os.remove('tests/resources/config_for_test_delete_node_pool')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='DeleteNodePool')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_delete_work_request(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'DeleteWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'DeleteWorkRequest')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_delete_work_request.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_delete_work_request', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_delete_work_request.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_delete_work_request'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_delete_work_request.pem'])
            config_file = 'tests/resources/config_for_test_delete_work_request'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('work_request_group.command_name', 'work_request')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='DeleteWorkRequest')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'DeleteWorkRequest', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('delete_work_request.command_name', 'delete')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, DeleteWorkRequest. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_work_request.command_name', 'delete'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('delete_work_request.command_name', 'delete')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'container_engine',
                    'DeleteWorkRequest',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'deleteWorkRequest',
                    True
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_delete_work_request.pem'):
                    os.remove('tests/resources/keyfile_for_test_delete_work_request.pem')
                if os.path.exists('tests/resources/config_for_test_delete_work_request'):
                    os.remove('tests/resources/config_for_test_delete_work_request')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='DeleteWorkRequest')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_cluster(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'GetCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'GetCluster')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_cluster.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_cluster', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_cluster.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_cluster'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_cluster.pem'])
            config_file = 'tests/resources/config_for_test_get_cluster'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('cluster_group.command_name', 'cluster')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='GetCluster')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'GetCluster', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_cluster.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, GetCluster. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_cluster.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_cluster.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'container_engine',
                    'GetCluster',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'cluster',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_cluster.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_cluster.pem')
                if os.path.exists('tests/resources/config_for_test_get_cluster'):
                    os.remove('tests/resources/config_for_test_get_cluster')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='GetCluster')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_cluster_options(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'GetClusterOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'GetClusterOptions')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_cluster_options.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_cluster_options', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_cluster_options.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_cluster_options'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_cluster_options.pem'])
            config_file = 'tests/resources/config_for_test_get_cluster_options'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('cluster_options_group.command_name', 'cluster_options')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='GetClusterOptions')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'GetClusterOptions', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_cluster_options.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, GetClusterOptions. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_cluster_options.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_cluster_options.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'container_engine',
                    'GetClusterOptions',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'clusterOptions',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_cluster_options.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_cluster_options.pem')
                if os.path.exists('tests/resources/config_for_test_get_cluster_options'):
                    os.remove('tests/resources/config_for_test_get_cluster_options')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='GetClusterOptions')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_node_pool(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'GetNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'GetNodePool')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_node_pool.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_node_pool', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_node_pool.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_node_pool'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_node_pool.pem'])
            config_file = 'tests/resources/config_for_test_get_node_pool'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('node_pool_group.command_name', 'node_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='GetNodePool')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'GetNodePool', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_node_pool.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, GetNodePool. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_node_pool.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_node_pool.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'container_engine',
                    'GetNodePool',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'nodePool',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_node_pool.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_node_pool.pem')
                if os.path.exists('tests/resources/config_for_test_get_node_pool'):
                    os.remove('tests/resources/config_for_test_get_node_pool')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='GetNodePool')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_node_pool_options(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'GetNodePoolOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'GetNodePoolOptions')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_get_node_pool_options.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_get_node_pool_options', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_get_node_pool_options.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_get_node_pool_options'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_get_node_pool_options.pem'])
            config_file = 'tests/resources/config_for_test_get_node_pool_options'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('node_pool_options_group.command_name', 'node_pool_options')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='GetNodePoolOptions')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'GetNodePoolOptions', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('get_node_pool_options.command_name', 'get')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, GetNodePoolOptions. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_node_pool_options.command_name', 'get'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('get_node_pool_options.command_name', 'get')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'container_engine',
                    'GetNodePoolOptions',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'nodePoolOptions',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_get_node_pool_options.pem'):
                    os.remove('tests/resources/keyfile_for_test_get_node_pool_options.pem')
                if os.path.exists('tests/resources/config_for_test_get_node_pool_options'):
                    os.remove('tests/resources/config_for_test_get_node_pool_options')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='GetNodePoolOptions')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_get_work_request(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'GetWorkRequest')
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

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('work_request_group.command_name', 'work_request')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='GetWorkRequest')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'GetWorkRequest', request)

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
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, GetWorkRequest. '
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
                    'container_engine',
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
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='GetWorkRequest')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_clusters(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'ListClusters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'ListClusters')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_clusters.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_clusters', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_clusters.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_clusters'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_clusters.pem'])
            config_file = 'tests/resources/config_for_test_list_clusters'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('cluster_group.command_name', 'cluster')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='ListClusters')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'ListClusters', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_clusters.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, ListClusters. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_clusters.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_clusters.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'container_engine',
                    'ListClusters',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_clusters.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_clusters.pem')
                if os.path.exists('tests/resources/config_for_test_list_clusters'):
                    os.remove('tests/resources/config_for_test_list_clusters')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='ListClusters')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_node_pools(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'ListNodePools'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'ListNodePools')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_node_pools.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_node_pools', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_node_pools.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_node_pools'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_node_pools.pem'])
            config_file = 'tests/resources/config_for_test_list_node_pools'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('node_pool_group.command_name', 'node_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='ListNodePools')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'ListNodePools', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_node_pools.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, ListNodePools. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_node_pools.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_node_pools.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'container_engine',
                    'ListNodePools',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_node_pools.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_node_pools.pem')
                if os.path.exists('tests/resources/config_for_test_list_node_pools'):
                    os.remove('tests/resources/config_for_test_list_node_pools')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='ListNodePools')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_work_request_errors(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'ListWorkRequestErrors')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_work_request_errors.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_work_request_errors', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_work_request_errors.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_work_request_errors'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_work_request_errors.pem'])
            config_file = 'tests/resources/config_for_test_list_work_request_errors'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('work_request_error_group.command_name', 'work_request_error')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='ListWorkRequestErrors')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'ListWorkRequestErrors', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_work_request_errors.command_name', 'list')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, ListWorkRequestErrors. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_work_request_errors.command_name', 'list'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_work_request_errors.command_name', 'list')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'container_engine',
                    'ListWorkRequestErrors',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_work_request_errors.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_work_request_errors.pem')
                if os.path.exists('tests/resources/config_for_test_list_work_request_errors'):
                    os.remove('tests/resources/config_for_test_list_work_request_errors')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='ListWorkRequestErrors')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_work_request_logs(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'ListWorkRequestLogs')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_list_work_request_logs.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_list_work_request_logs', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_list_work_request_logs.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_list_work_request_logs'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_list_work_request_logs.pem'])
            config_file = 'tests/resources/config_for_test_list_work_request_logs'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('work_request_log_entry_group.command_name', 'work_request_log_entry')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='ListWorkRequestLogs')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'ListWorkRequestLogs', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('list_work_request_logs.command_name', 'list-work-request-logs')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, ListWorkRequestLogs. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_work_request_logs.command_name', 'list-work-request-logs'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('list_work_request_logs.command_name', 'list-work-request-logs')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'container_engine',
                    'ListWorkRequestLogs',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'items',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_list_work_request_logs.pem'):
                    os.remove('tests/resources/keyfile_for_test_list_work_request_logs.pem')
                if os.path.exists('tests/resources/config_for_test_list_work_request_logs'):
                    os.remove('tests/resources/config_for_test_list_work_request_logs')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='ListWorkRequestLogs')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_list_work_requests(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'ListWorkRequests')
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

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('work_request_group.command_name', 'work_request')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='ListWorkRequests')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:

            if 'opts' in request:
                for key in request['opts']:
                    request[key] = request['opts'][key]
                del request['opts']

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'ListWorkRequests', request)

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
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, ListWorkRequests. '
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
                    'container_engine',
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
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='ListWorkRequests')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_cluster(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'UpdateCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'UpdateCluster')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_cluster.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_cluster', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_cluster.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_cluster'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_cluster.pem'])
            config_file = 'tests/resources/config_for_test_update_cluster'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('cluster_group.command_name', 'cluster')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='UpdateCluster')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateClusterDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'UpdateCluster', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_cluster.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, UpdateCluster. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_cluster.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_cluster.command_name', 'update')))

            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'container_engine',
                    'UpdateCluster',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateCluster',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_cluster.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_cluster.pem')
                if os.path.exists('tests/resources/config_for_test_update_cluster'):
                    os.remove('tests/resources/config_for_test_update_cluster')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='UpdateCluster')
                request = request_containers[i]['request'].copy()


@pytest.mark.generated
def test_update_node_pool(cli_testing_service_client, runner, config_file, config_profile):
    if not cli_testing_service_client.is_api_enabled('container_engine', 'UpdateNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config_file = os.environ['OCI_CLI_CONFIG_FILE']
    if 'USE_TESTING_SERVICE_CONFIG' in os.environ:
        try:
            config_str = cli_testing_service_client.get_config('container_engine', 'ContainerEngine', 'UpdateNodePool')
            config = json.loads(config_str)
            key_file_content = config['keyFileContent']
            with open('tests/resources/keyfile_for_test_update_node_pool.pem', 'w') as f:
                f.write(key_file_content)
            with open('tests/resources/config_for_test_update_node_pool', 'w') as f:
                f.write('[ADMIN]\n')
                f.write('user = ' + config['userId'] + '\n')
                f.write('fingerprint = ' + config['fingerprint'] + '\n')
                f.write('tenancy = ' + config['tenantId'] + '\n')
                f.write('region = ' + config['region'] + '\n')
                f.write('key_file = tests/resources/keyfile_for_test_update_node_pool.pem\n')
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/config_for_test_update_node_pool'])
            runner.invoke(oci_cli.cli, ['setup', 'repair-file-permissions', '--file', 'tests/resources/keyfile_for_test_update_node_pool.pem'])
            config_file = 'tests/resources/config_for_test_update_node_pool'
        except vcr.errors.CannotOverwriteExistingCassetteException:
            pass
        except Exception as e:
            print(e)
            raise e

    root_command_name = oci_cli.cli_util.override('ce_root_group.command_name', 'ce')
    resource_group_command_name = oci_cli.cli_util.override('node_pool_group.command_name', 'node_pool')
    request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='UpdateNodePool')
    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        done = False
        params = []
        while not done:
            # force all details param names to have lower case first letter for consistency with Java models
            param_name = 'UpdateNodePoolDetails'
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

            request, cleanup = generated_test_request_transformers.transform_generated_test_input('container_engine', 'UpdateNodePool', request)

            input_content = json.dumps(request)

            # for operations with polymorphic input types, attempt to find an operation for a specific subtype
            # if one does not exist, fallback to calling base operation
            if not params:
                params = util.get_command_list(
                    root_command_name,
                    resource_group_command_name,
                    oci_cli.cli_util.override('update_node_pool.command_name', 'update')
                )

            if not params:
                raise ValueError(
                    'Failed to find CLI command "oci {} {} {}" for given operation: container_engine, UpdateNodePool. '
                    'This usually happens because generated commands have been manually re-arranged in code for better user '
                    'experience. To allow this test to find the proper command, please add an entry to MOVED_COMMANDS in '
                    'services/<spec_name>/tests/extend_test_<your_service_name>.py to map ({}, {}, {}) to the syntax '
                    'for the new command. If the file does not exist for your service, please create one. You can refer the '
                    'MOVED_COMMANDS map in services/core/tests/extend_test_compute.py as an example.'
                    .format(
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_node_pool.command_name', 'update'),
                        root_command_name, resource_group_command_name,
                        oci_cli.cli_util.override('update_node_pool.command_name', 'update')))

            params.append('--force')
            params.extend(['--from-json', input_content])
            try:
                util.set_admin_pass_phrase()
                result = invoke(runner, config_file, 'ADMIN', params)

                message = cli_testing_service_client.validate_result(
                    'container_engine',
                    'UpdateNodePool',
                    request_containers[i]['containerId'],
                    request_containers[i]['request'],
                    result,
                    'updateNodePool',
                    False
                )
            finally:
                if os.path.exists('tests/resources/keyfile_for_test_update_node_pool.pem'):
                    os.remove('tests/resources/keyfile_for_test_update_node_pool.pem')
                if os.path.exists('tests/resources/config_for_test_update_node_pool'):
                    os.remove('tests/resources/config_for_test_update_node_pool')
                if cleanup:
                    try:
                        next(cleanup)
                    except StopIteration:
                        pass

            if message != "CONT":
                assert len(message) == 0, message
                done = True
            else:
                request_containers = cli_testing_service_client.get_requests(service_name='container_engine', api_name='UpdateNodePool')
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
