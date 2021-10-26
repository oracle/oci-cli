# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import time

import oci_cli
import pytest

from tests import test_config_container
from tests import util

CASSETTE_LIBRARY_DIR = 'services/devops/tests/cassettes'


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('devops_build_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.fixture(scope='module')
def project_and_pipeline(runner, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('devops_build_project_and_pipeline_fixture.yml'):
        # create project
        notification_topic_id = 'ocid1.onstopic.oc1.iad.aaaaaaaatklfw3733kbwc2dzus633rb553dt52fdewujfea5tunntmqykmoq'
        notification_config = {
            'topicId': notification_topic_id
        }
        project_name = util.random_name('cli_devops_build_test_project')
        params = [
            'devops', 'project', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--name', project_name,
            '--notification-config', json.dumps(notification_config)
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        project_id = json.loads(result.output)['data']['id']
        wait_until(['devops', 'project', 'get', '--project-id', project_id], 'ACTIVE', 300)

        # create build pipeline
        build_pipeline_name = util.random_name('cli_devops_build_test_build_pipeline')
        params = [
            'devops', 'build-pipeline', 'create',
            '--display-name', build_pipeline_name,
            '--project-id', project_id
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        build_pipeline_id = json.loads(result.output)['data']['id']
        wait_until(['devops', 'build-pipeline', 'get', '--build-pipeline-id', build_pipeline_id], 'ACTIVE', 300)
    yield project_id, build_pipeline_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('devops_build_project_and_pipeline_fixture_cleanup.yml'):
        # delete build-pipeline
        params = ['devops', 'build-pipeline', 'delete', '--build-pipeline-id', build_pipeline_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        # delete project
        params = ['devops', 'project', 'delete', '--project-id', project_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_build_pipeline_get(project_and_pipeline, runner, config_file, config_profile):
    build_pipeline_id = project_and_pipeline[1]
    params = ['devops', 'build-pipeline', 'get', '--build-pipeline-id', build_pipeline_id]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert build_pipeline_id == json.loads(result.output)['data']['id'], \
        "Get API should return correct build pipeline id"


def test_build_pipeline_list(project_and_pipeline, runner, config_file, config_profile):
    params = ['devops', 'build-pipeline', 'list', '--compartment-id', util.COMPARTMENT_ID]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    build_pipelines = json.loads(result.output)['data']['items']
    assert len(build_pipelines) > 0, "List API should return at least one build pipeline"


def test_build_pipeline_update(project_and_pipeline, runner, config_file, config_profile):
    build_pipeline_id = project_and_pipeline[1]
    build_pipeline_description = 'Build Pipeline Description'
    params = [
        'devops', 'build-pipeline', 'update',
        '--build-pipeline-id', build_pipeline_id,
        '--description', build_pipeline_description]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert build_pipeline_id == json.loads(result.output)['data']['id'], \
        "Update API should return correct build pipeline id"
    assert build_pipeline_description == json.loads(result.output)['data']['description'], \
        "Update API should return updated build pipeline description"


@pytest.fixture(scope='module')
def wait_stage(project_and_pipeline, runner, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_wait_stage_fixture.yml'):
        # create wait stage
        build_pipeline_id = project_and_pipeline[1]
        wait_stage_name = util.random_name('cli_devops_build_test_wait_stage')
        wait_criteria = {
            'waitType': 'ABSOLUTE_WAIT',
            'waitDuration': 'PT10S'
        }
        stage_predecessor_collection = {
            'items': [
                {
                    'id': build_pipeline_id
                }
            ]
        }
        params = [
            'devops', 'build-pipeline-stage', 'create-wait-stage',
            '--build-pipeline-id', build_pipeline_id,
            '--display-name', wait_stage_name,
            '--wait-criteria', json.dumps(wait_criteria),
            '--stage-predecessor-collection', json.dumps(stage_predecessor_collection)
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        wait_stage_id = json.loads(result.output)['data']['id']
        wait_until(['devops', 'build-pipeline-stage', 'get', '--stage-id', wait_stage_id], 'ACTIVE', 300)
    yield wait_stage_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_wait_stage_fixture_cleanup.yml'):
        # delete wait stage
        params = ['devops', 'build-pipeline-stage', 'delete', '--stage-id', wait_stage_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_wait_stage_get(project_and_pipeline, wait_stage, runner, config_file, config_profile):
    wait_stage_id = wait_stage
    params = ['devops', 'build-pipeline-stage', 'get', '--stage-id', wait_stage_id]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert wait_stage_id == json.loads(result.output)['data']['id'], \
        "Get API should return correct build pipeline stage id"


def test_wait_stage_list(project_and_pipeline, wait_stage, runner, config_file, config_profile):
    params = ['devops', 'build-pipeline-stage', 'list', '--compartment-id', util.COMPARTMENT_ID]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    build_stages = json.loads(result.output)['data']['items']
    assert len(build_stages) > 0, "List API should return at least one build pipeline stage"


def test_wait_stage_update(project_and_pipeline, wait_stage, runner, config_file, config_profile):
    build_pipeline_id = project_and_pipeline[1]
    wait_stage_id = wait_stage
    wait_stage_description = 'Wait Stage Description'
    wait_criteria = {
        'waitType': 'ABSOLUTE_WAIT',
        'waitDuration': 'PT10S'
    }
    stage_predecessor_collection = {
        'items': [
            {
                'id': build_pipeline_id
            }
        ]
    }
    params = [
        'devops', 'build-pipeline-stage', 'update-wait-stage', '--force',
        '--stage-id', wait_stage_id,
        '--description', wait_stage_description,
        '--wait-criteria', json.dumps(wait_criteria),
        '--stage-predecessor-collection', json.dumps(stage_predecessor_collection)
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert wait_stage_id == json.loads(result.output)['data']['id'], \
        "Update API should return correct build pipeline stage id"
    assert wait_stage_description == json.loads(result.output)['data']['description'], \
        "Update API should return updated build pipeline stage description"


@pytest.fixture(scope='module')
def build_stage(project_and_pipeline, github_connection, runner, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_build_stage_fixture.yml'):
        # create build stage
        build_pipeline_id = project_and_pipeline[1]
        github_connection_id = github_connection
        build_stage_name = util.random_name('cli_devops_build_test_build_stage')
        source_name = 'SdkCliIntegrationTest'
        build_source_collection = {
            'items': [
                {
                    'connectionId': github_connection_id,
                    'connectionType': 'GITHUB',
                    'repositoryUrl': 'https://github.com/dlcbld/SdkCliIntegrationTest.git',
                    'branch': 'main',
                    'name': source_name
                }
            ]
        }
        stage_predecessor_collection = {
            'items': [
                {
                    'id': build_pipeline_id
                }
            ]
        }
        params = [
            'devops', 'build-pipeline-stage', 'create-build-stage',
            '--build-pipeline-id', build_pipeline_id,
            '--display-name', build_stage_name,
            '--build-spec-file', 'build_spec.yml',
            '--primary-build-source', source_name,
            '--image', 'OL7_X86_64_STANDARD_10',
            '--build-source-collection', json.dumps(build_source_collection),
            '--stage-predecessor-collection', json.dumps(stage_predecessor_collection)
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        build_stage_id = json.loads(result.output)['data']['id']
        wait_until(
            ['devops', 'build-pipeline-stage', 'get', '--stage-id', build_stage_id], 'ACTIVE', 300)
    yield build_stage_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_build_stage_fixture_cleanup.yml'):
        # delete build stage
        params = ['devops', 'build-pipeline-stage', 'delete', '--stage-id', build_stage_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_build_stage_get(project_and_pipeline, build_stage, github_connection, runner, config_file, config_profile):
    build_stage_id = build_stage
    params = ['devops', 'build-pipeline-stage', 'get', '--stage-id', build_stage_id]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert build_stage_id == json.loads(result.output)['data']['id'], \
        "Get API should return correct build pipeline stage id"


def test_build_stage_list(project_and_pipeline, build_stage, runner, config_file, config_profile):
    params = ['devops', 'build-pipeline-stage', 'list', '--compartment-id', util.COMPARTMENT_ID]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    build_stages = json.loads(result.output)['data']['items']
    assert len(build_stages) > 0, "List API should return at least one build pipeline stage"


def test_build_stage_update(project_and_pipeline, build_stage, github_connection, runner, config_file, config_profile):
    build_pipeline_id = project_and_pipeline[1]
    build_stage_id = build_stage
    github_connection_id = github_connection
    source_name = 'SdkCliIntegrationTest'
    build_stage_description = 'Build Stage Description'
    build_source_collection = {
        'items': [
            {
                'connectionId': github_connection_id,
                'connectionType': 'GITHUB',
                'repositoryUrl': 'https://github.com/dlcbld/SdkCliIntegrationTest.git',
                'branch': 'main',
                'name': source_name
            }
        ]
    }
    stage_predecessor_collection = {
        'items': [
            {
                'id': build_pipeline_id
            }
        ]
    }
    params = [
        'devops', 'build-pipeline-stage', 'update-build-stage', '--force',
        '--stage-id', build_stage_id,
        '--description', build_stage_description,
        '--build-spec-file', 'build_spec.yml',
        '--primary-build-source', source_name,
        '--image', 'OL7_X86_64_STANDARD_10',
        '--build-source-collection', json.dumps(build_source_collection),
        '--stage-predecessor-collection', json.dumps(stage_predecessor_collection)
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert build_stage_id == json.loads(result.output)['data']['id'], \
        "Update API should return correct build pipeline stage id"
    assert build_stage_description == json.loads(result.output)['data']['description'], \
        "Update API should return updated build pipeline stage description"


@pytest.fixture(scope='module')
def deliver_artifact_stage(project_and_pipeline, build_stage, runner, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_deliver_artifact_stage_fixture.yml'):
        # create deliver artifact stage
        build_pipeline_id = project_and_pipeline[1]
        build_stage_id = build_stage
        deliver_artifact_stage_name = util.random_name('cli_devops_build_test_deliver_artifact_stage')
        deliver_artifact_collection = {
            'items': [
                {
                    'artifactId': 'artifactId',
                    'artifactName': 'artifactName'
                }
            ]
        }
        stage_predecessor_collection = {
            'items': [
                {
                    'id': build_stage_id
                }
            ]
        }
        params = [
            'devops', 'build-pipeline-stage', 'create-deliver-artifact-stage',
            '--build-pipeline-id', build_pipeline_id,
            '--display-name', deliver_artifact_stage_name,
            '--deliver-artifact-collection', json.dumps(deliver_artifact_collection),
            '--stage-predecessor-collection', json.dumps(stage_predecessor_collection)
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        deliver_artifact_stage_id = json.loads(result.output)['data']['id']
        wait_until(['devops', 'build-pipeline-stage', 'get', '--stage-id', deliver_artifact_stage_id], 'ACTIVE', 300)
    yield deliver_artifact_stage_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_deliver_artifact_stage_fixture_cleanup.yml'):
        # delete deliver artifact stage
        params = [
            'devops', 'build-pipeline-stage', 'delete', '--stage-id', deliver_artifact_stage_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_deliver_artifact_stage_get(project_and_pipeline, deliver_artifact_stage, runner, config_file, config_profile):
    deliver_artifact_stage_id = deliver_artifact_stage
    params = ['devops', 'build-pipeline-stage', 'get', '--stage-id', deliver_artifact_stage_id]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert deliver_artifact_stage_id == json.loads(result.output)['data']['id'], \
        "Get API should return correct build pipeline stage id"


def test_deliver_artifact_stage_list(project_and_pipeline, deliver_artifact_stage, runner, config_file, config_profile):
    params = ['devops', 'build-pipeline-stage', 'list', '--compartment-id', util.COMPARTMENT_ID]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    build_stages = json.loads(result.output)['data']['items']
    assert len(build_stages) > 0, "List API should return at least one build pipeline stage"


def test_deliver_artifact_stage_update(
        project_and_pipeline, build_stage, deliver_artifact_stage, runner, config_file, config_profile):
    build_stage_id = build_stage
    deliver_artifact_stage_id = deliver_artifact_stage
    deliver_artifact_stage_description = 'Deliver Artifact Stage Description'
    deliver_artifact_collection = {
        'items': [
            {
                'artifactId': 'artifactId',
                'artifactName': 'artifactName'
            }
        ]
    }
    stage_predecessor_collection = {
        'items': [
            {
                'id': build_stage_id
            }
        ]
    }
    params = [
        'devops', 'build-pipeline-stage', 'update-deliver-artifact-stage', '--force',
        '--stage-id', deliver_artifact_stage_id,
        '--description', deliver_artifact_stage_description,
        '--deliver-artifact-collection', json.dumps(deliver_artifact_collection),
        '--stage-predecessor-collection', json.dumps(stage_predecessor_collection)
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert deliver_artifact_stage_id == json.loads(result.output)['data']['id'], \
        "Update API should return correct build pipeline stage id"
    assert deliver_artifact_stage_description == json.loads(result.output)['data']['description'], \
        "Update API should return updated build pipeline stage description"


@pytest.fixture(scope='module')
def trigger_deployment_stage(project_and_pipeline, build_stage, runner, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_trigger_deployment_stage_fixture.yml'):
        project_id = project_and_pipeline[0]
        build_pipeline_id = project_and_pipeline[1]
        # create deploy pipeline
        deploy_pipeline_name = util.random_name('cli_devops_build_test_deploy_pipeline')
        params = [
            'devops', 'deploy-pipeline', 'create',
            '--project-id', project_id,
            '--display-name', deploy_pipeline_name,
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        deploy_pipeline_id = json.loads(result.output)['data']['id']

        # create trigger deployment stage
        build_stage_id = build_stage
        trigger_deployment_stage_name = util.random_name('cli_devops_build_test_trigger_deployment_stage')
        stage_predecessor_collection = {
            'items': [
                {
                    'id': build_stage_id
                }
            ]
        }
        params = [
            'devops', 'build-pipeline-stage', 'create-trigger-deployment-stage',
            '--build-pipeline-id', build_pipeline_id,
            '--display-name', trigger_deployment_stage_name,
            '--is-pass-all-parameters-enabled', 'false',
            '--deploy-pipeline-id', deploy_pipeline_id,
            '--stage-predecessor-collection', json.dumps(stage_predecessor_collection)
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        trigger_deployment_stage_id = json.loads(result.output)['data']['id']
        wait_until(['devops', 'build-pipeline-stage', 'get', '--stage-id', trigger_deployment_stage_id], 'ACTIVE', 300)
    yield trigger_deployment_stage_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_trigger_deployment_stage_fixture_cleanup.yml'):
        # delete trigger deployment stage
        params = [
            'devops', 'build-pipeline-stage', 'delete', '--stage-id', trigger_deployment_stage_id,
            '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        # delete deploy pipeline
        params = ['devops', 'deploy-pipeline', 'delete', '--pipeline-id', deploy_pipeline_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_trigger_deployment_stage_get(
        project_and_pipeline, trigger_deployment_stage, runner, config_file, config_profile):
    trigger_deployment_stage_id = trigger_deployment_stage
    params = ['devops', 'build-pipeline-stage', 'get', '--stage-id', trigger_deployment_stage_id]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert trigger_deployment_stage_id == json.loads(result.output)['data']['id'], \
        "Get API should return correct build pipeline stage id"


def test_trigger_deployment_stage_list(
        project_and_pipeline, trigger_deployment_stage, runner, config_file, config_profile):
    params = ['devops', 'build-pipeline-stage', 'list', '--compartment-id', util.COMPARTMENT_ID]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    build_stages = json.loads(result.output)['data']['items']
    assert len(build_stages) > 0, "List API should return at least one build pipeline stage"


def test_trigger_deployment_stage_update(
        project_and_pipeline, build_stage, trigger_deployment_stage, runner, config_file, config_profile):
    build_stage_id = build_stage
    trigger_deployment_stage_id = trigger_deployment_stage
    trigger_deployment_stage_description = 'Trigger Deployment Stage Description'
    stage_predecessor_collection = {
        'items': [
            {
                'id': build_stage_id
            }
        ]
    }
    params = [
        'devops', 'build-pipeline-stage', 'update-trigger-deployment-stage', '--force',
        '--stage-id', trigger_deployment_stage_id,
        '--description', trigger_deployment_stage_description,
        '--is-pass-all-parameters-enabled', 'false',
        '--stage-predecessor-collection', json.dumps(stage_predecessor_collection)
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert trigger_deployment_stage_id == json.loads(result.output)['data']['id'], \
        "Update API should return correct build pipeline stage id"
    assert trigger_deployment_stage_description == json.loads(result.output)['data']['description'], \
        "Update API should return updated build pipeline stage description"


@pytest.fixture(scope='module')
def build_run(project_and_pipeline, wait_stage, build_stage, github_connection, runner, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_build_run_fixture.yml'):
        # start build run
        build_pipeline_id = project_and_pipeline[1]
        build_run_name = util.random_name('cli_devops_build_test_build_run')
        commit_info = {
            'repositoryUrl': 'https://github.com/dlcbld/SdkCliIntegrationTest.git',
            'repositoryBranch': 'main',
            'commitHash': '6062c07b44b7da31aa14a4c4b19dac3255a4833a'
        }
        build_run_arguments = {
            'items': [
                {
                    'name': 'MAJOR_VERSION',
                    'value': '1'
                }
            ]
        }
        params = [
            'devops', 'build-run', 'create',
            '--build-pipeline-id', build_pipeline_id,
            '--display-name', build_run_name,
            '--commit-info', json.dumps(commit_info),
            '--build-run-arguments', json.dumps(build_run_arguments)
        ]
        time.sleep(10)
        result = invoke(runner, config_file, config_profile, params)

        util.validate_response(result)
        build_run_id = json.loads(result.output)['data']['id']
        wait_until(['devops', 'build-run', 'get', '--build-run-id', build_run_id], 'ACCEPTED', 300)
        time.sleep(10)
    yield build_run_id


def test_build_run_get(project_and_pipeline, build_run, wait_stage, build_stage, runner, config_file, config_profile):
    build_run_id = build_run
    build_stage_id = build_stage
    wait_stage_id = wait_stage
    params = ['devops', 'build-run', 'get', '--build-run-id', build_run_id]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert build_run_id == json.loads(result.output)['data']['id'], \
        "Get API should return correct build run id"
    stages_run_progress = \
        json.loads(result.output)['data']['build-run-progress']['build-pipeline-stage-run-progress']
    assert stages_run_progress[wait_stage_id] is not None
    assert stages_run_progress[build_stage_id] is not None


def test_build_run_list(project_and_pipeline, build_run, runner, config_file, config_profile):
    params = ['devops', 'build-run', 'list', '--compartment-id', util.COMPARTMENT_ID]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    build_runs = json.loads(result.output)['data']['items']
    assert len(build_runs) > 0, "List API should return at least one build run"


@pytest.fixture(scope='module')
def github_connection(project_and_pipeline, runner, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_github_connection_fixture.yml'):
        # create connection
        project_id = project_and_pipeline[0]
        connection_name = util.random_name('cli_devops_build_test_connection')
        access_token_secret = 'ocid1.vaultsecret.oc1.iad.amaaaaaa34lgq7aa325l6x7exbl5y7c4pk75aodriekuttjkuqatetll35aq'

        params = [
            'devops', 'connection', 'create-github-connection',
            '--display-name', connection_name,
            '--project-id', project_id,
            '--personal-access-token', access_token_secret]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        connection_id = json.loads(result.output)['data']['id']
        wait_until(['devops', 'connection', 'get', '--connection-id', connection_id], 'ACTIVE', 300)
    yield connection_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_github_connection_fixture_cleanup.yml'):
        # delete connection
        params = ['devops', 'connection', 'delete', '--connection-id', connection_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_github_connection_get(project_and_pipeline, github_connection, runner, config_file, config_profile):
    connection_id = github_connection
    params = ['devops', 'connection', 'get', '--connection-id', connection_id]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert connection_id == json.loads(result.output)['data']['id'], \
        "Get API should return correct connection id"


def test_github_connection_list(project_and_pipeline, github_connection, runner, config_file, config_profile):
    params = ['devops', 'connection', 'list', '--compartment-id', util.COMPARTMENT_ID]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    connections = json.loads(result.output)['data']['items']
    assert len(connections) > 0, "List API should return at least one connection"


def test_github_connection_update(project_and_pipeline, github_connection, runner, config_file, config_profile):
    connection_id = github_connection
    connection_description = 'Connection Description'
    params = [
        'devops', 'connection', 'update-github-connection',
        '--connection-id', connection_id,
        '--description', connection_description]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert connection_id == json.loads(result.output)['data']['id'], \
        "Update API should return correct connection id"
    assert connection_description == json.loads(result.output)['data']['description'], \
        "Update API should return updated connection description"


@pytest.fixture(scope='module')
def gitlab_connection(project_and_pipeline, runner, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_gitlab_connection_fixture.yml'):
        # create connection
        project_id = project_and_pipeline[0]
        connection_name = util.random_name('cli_devops_build_test_connection')
        access_token_secret = 'ocid1.vaultsecret.oc1.iad.amaaaaaa34lgq7aarejtkg6o4m5zt5wuscdruhk5hwqkwyzeyfhkxz5zdyia'
        params = [
            'devops', 'connection', 'create-gitlab-connection',
            '--display-name', connection_name,
            '--project-id', project_id,
            '--personal-access-token', access_token_secret]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        connection_id = json.loads(result.output)['data']['id']
        wait_until(['devops', 'connection', 'get', '--connection-id', connection_id], 'ACTIVE', 300)
    yield connection_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_gitlab_connection_fixture_cleanup.yml'):
        # delete connection
        params = ['devops', 'connection', 'delete', '--connection-id', connection_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_gitlab_connection_get(project_and_pipeline, gitlab_connection, runner, config_file, config_profile):
    connection_id = gitlab_connection
    params = ['devops', 'connection', 'get', '--connection-id', connection_id]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert connection_id == json.loads(result.output)['data']['id'], \
        "Get API should return correct connection id"


def test_gitlab_connection_list(project_and_pipeline, gitlab_connection, runner, config_file, config_profile):
    params = ['devops', 'connection', 'list', '--compartment-id', util.COMPARTMENT_ID]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    connections = json.loads(result.output)['data']['items']
    assert len(connections) > 0, "List API should return at least one connection"


def test_gitlab_connection_update(project_and_pipeline, gitlab_connection, runner, config_file, config_profile):
    connection_id = gitlab_connection
    connection_description = 'Connection Description'
    params = [
        'devops', 'connection', 'update-gitlab-connection',
        '--connection-id', connection_id,
        '--description', connection_description]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert connection_id == json.loads(result.output)['data']['id'], \
        "Update API should return correct connection id"
    assert connection_description == json.loads(result.output)['data']['description'], \
        "Update API should return updated connection description"


@pytest.fixture(scope='module')
def github_trigger(project_and_pipeline, runner, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_github_trigger_fixture.yml'):
        # create trigger
        project_id = project_and_pipeline[0]
        build_pipeline_id = project_and_pipeline[1]
        trigger_name = util.random_name('cli_devops_build_test_trigger')
        trigger_source = 'GITHUB'
        actions = [
            {
                'type': 'TRIGGER_BUILD_PIPELINE',
                'filter': {
                    'triggerSource': trigger_source,
                    'events': [
                        'PUSH',
                        'PULL_REQUEST_UPDATED',
                        'PULL_REQUEST_REOPENED',
                        'PULL_REQUEST_MERGED'
                    ],
                    'include': {
                        'headRef': 'feature',
                        'baseRef': 'master'
                    }
                },
                'buildPipelineId': build_pipeline_id
            }
        ]

        params = [
            'devops', 'trigger', 'create-github-trigger',
            '--display-name', trigger_name,
            '--project-id', project_id,
            '--actions', json.dumps(actions)]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        trigger_id = json.loads(result.output)['data']['id']
        wait_until(['devops', 'trigger', 'get', '--trigger-id', trigger_id], 'ACTIVE', 300)
    yield trigger_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_github_trigger_fixture_cleanup.yml'):
        # delete trigger
        params = ['devops', 'trigger', 'delete', '--trigger-id', trigger_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_github_trigger_get(project_and_pipeline, github_trigger, runner, config_file, config_profile):
    trigger_id = github_trigger
    params = ['devops', 'trigger', 'get', '--trigger-id', trigger_id]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert trigger_id == json.loads(result.output)['data']['id'], \
        "Get API should return correct trigger id"


def test_github_trigger_list(project_and_pipeline, github_trigger, runner, config_file, config_profile):
    params = ['devops', 'trigger', 'list', '--compartment-id', util.COMPARTMENT_ID]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    triggers = json.loads(result.output)['data']['items']
    assert len(triggers) > 0, "List API should return at least one trigger"


def test_github_trigger_update(project_and_pipeline, github_trigger, runner, config_file, config_profile):
    trigger_id = github_trigger
    trigger_description = 'Trigger Description'
    params = [
        'devops', 'trigger', 'update-github-trigger',
        '--trigger-id', trigger_id,
        '--description', trigger_description]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert trigger_id == json.loads(result.output)['data']['id'], \
        "Update API should return correct trigger id"
    assert trigger_description == json.loads(result.output)['data']['description'], \
        "Update API should return updated trigger description"


@pytest.fixture(scope='module')
def gitlab_trigger(project_and_pipeline, runner, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_gitlab_trigger_fixture.yml'):
        # create trigger
        project_id = project_and_pipeline[0]
        build_pipeline_id = project_and_pipeline[1]
        trigger_name = util.random_name('cli_devops_build_test_trigger')
        trigger_source = 'GITLAB'
        actions = [
            {
                'type': 'TRIGGER_BUILD_PIPELINE',
                'filter': {
                    'triggerSource': trigger_source,
                    'events': [
                        'PUSH',
                        'PULL_REQUEST_UPDATED',
                        'PULL_REQUEST_REOPENED'
                    ],
                    'include': {
                        'headRef': 'feature',
                        'baseRef': 'master'
                    }
                },
                'buildPipelineId': build_pipeline_id
            }
        ]

        params = [
            'devops', 'trigger', 'create-gitlab-trigger',
            '--display-name', trigger_name,
            '--project-id', project_id,
            '--actions', json.dumps(actions)]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        trigger_id = json.loads(result.output)['data']['id']
        wait_until(['devops', 'trigger', 'get', '--trigger-id', trigger_id], 'ACTIVE', 300)
    yield trigger_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_build_gitlab_trigger_fixture_cleanup.yml'):
        # delete trigger
        params = ['devops', 'trigger', 'delete', '--trigger-id', trigger_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_gitlab_trigger_get(project_and_pipeline, gitlab_trigger, runner, config_file, config_profile):
    trigger_id = gitlab_trigger
    params = ['devops', 'trigger', 'get', '--trigger-id', trigger_id]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert trigger_id == json.loads(result.output)['data']['id'], \
        "Get API should return correct trigger id"


def test_gitlab_trigger_list(project_and_pipeline, gitlab_trigger, runner, config_file, config_profile):
    params = ['devops', 'trigger', 'list', '--compartment-id', util.COMPARTMENT_ID]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    triggers = json.loads(result.output)['data']['items']
    assert len(triggers) > 0, "List API should return at least one trigger"


def test_gitlab_trigger_update(project_and_pipeline, gitlab_trigger, runner, config_file, config_profile):
    trigger_id = gitlab_trigger
    trigger_description = 'Trigger Description'
    params = [
        'devops', 'trigger', 'update-gitlab-trigger',
        '--trigger-id', trigger_id,
        '--description', trigger_description]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert trigger_id == json.loads(result.output)['data']['id'], \
        "Update API should return correct trigger id"
    assert trigger_description == json.loads(result.output)['data']['description'], \
        "Update API should return updated trigger description"


def invoke(runner, config_file, config_profile, params, debug=False, ** args):
    root_params = ['--endpoint', 'https://devops-beta.us-ashburn-1.oci.oc-test.com']
    all_params = root_params + params + ['--config-file', config_file, '--profile', config_profile]
    if debug is True:
        all_params = all_params + ['--debug']
    result = runner.invoke(oci_cli.cli, all_params, **args)
    return result


def wait_until(params, lifecycle_state, time_in_seconds):
    params = params + ['--endpoint', 'https://devops-beta.us-ashburn-1.oci.oc-test.com']
    util.wait_until(params, lifecycle_state, max_wait_seconds=time_in_seconds)
