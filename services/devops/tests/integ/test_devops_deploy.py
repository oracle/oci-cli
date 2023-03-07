# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import oci_cli
import pytest

from tests import test_config_container
from tests import util
from conftest import runner

CASSETTE_LIBRARY_DIR = 'services/devops/tests/cassettes/devops_deploy'
runner = runner()


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('devops_deploy_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.fixture(scope='module')
def project_and_pipeline(config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('devops_deploy_test_project_and_pipeline_fixture.yml'):
        # create project
        notification_topic_id = 'ocid1.onstopic.oc1.phx.aaaaaaaa3kvkxuoaqazlomtuu4xdfdsjtlph3uyopf4y6zmv72wilmw6egsq'
        notification_config = {
            'topicId': notification_topic_id
        }
        project_name = util.random_name('cli_devops_deploy_test_project')
        params = [
            'devops', 'project', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--name', project_name,
            '--notification-config', json.dumps(notification_config)
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        project_id = json.loads(result.output)['data']['id']
        util.wait_until(['devops', 'project', 'get', '--project-id', project_id], 'ACTIVE', max_wait_seconds=300)
        deploy_pipeline_name = util.random_name('cli_devops_deploy_test_deploy_pipeline')
        params = [
            'devops', 'deploy-pipeline', 'create',
            '--display-name', deploy_pipeline_name,
            '--project-id', project_id
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        deploy_pipeline_id = json.loads(result.output)['data']['id']
        util.wait_until(['devops', 'deploy-pipeline', 'get', '--pipeline-id', deploy_pipeline_id], 'ACTIVE', max_wait_seconds=300)
    yield project_id, deploy_pipeline_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('devops_deploy_test_project_and_pipeline_fixture_cleanup.yml'):
        # delete deploy-pipeline
        params = ['devops', 'deploy-pipeline', 'delete', '--pipeline-id', deploy_pipeline_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        # delete project
        params = ['devops', 'project', 'delete', '--project-id', project_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


@pytest.fixture(scope='module')
def deploy_helm_repository_artifact(project_and_pipeline, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_deploy_artifact_helm_repository_artifact_fixture.yml'):
        # create deploy artifact
        project_id = project_and_pipeline[0]
        deploy_helm_artifact_name = util.random_name('cli_devops_deploy_test_deploy_artifact_helm_repository_artifact')
        params = [
            'devops', 'deploy-artifact', 'create-helm-repository-artifact',
            '--project-id', project_id,
            '--display-name', deploy_helm_artifact_name,
            '--artifact-type', 'HELM_CHART',
            '--artifact-chart-url', 'oci://us-ashburn-1.ocir.io/axrygfx06rk2/helm-test-chart',
            '--artifact-version', '0.0.1',
            '--argument-substitution-mode', 'NONE'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        deploy_artifact_id = json.loads(result.output)['data']['id']
    yield deploy_artifact_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('devops_deploy_artifact_helm_repository_artifact_fixture_cleanup.yml'):
        # delete deploy artifact
        params = ['devops', 'deploy-artifact', 'delete', '--artifact-id', deploy_artifact_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_get_helm_repository_artifact(deploy_helm_repository_artifact, config_file, config_profile):
    deploy_artifact_id = deploy_helm_repository_artifact
    params = ['devops', 'deploy-artifact', 'get', '--artifact-id', deploy_artifact_id]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert deploy_artifact_id == json.loads(result.output)['data']['id'], \
        "Get Deploy Artifact API should return correct deploy artifact id"


@pytest.fixture(scope='module')
def deploy_helm_repository_artifact_verification_key_source(project_and_pipeline, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_deploy_artifact_helm_repository_artifact_verification_key_source_fixture.yml'):
        # create deploy artifact
        project_id = project_and_pipeline[0]
        params = [
            'devops', 'deploy-artifact', 'create-helm-repository-artifact',
            '--project-id', project_id,
            '--artifact-type', 'HELM_CHART',
            '--artifact-chart-url', 'oci://us-ashburn-1.ocir.io/axrygfx06rk2/helm-test-chart',
            '--artifact-version', '0.0.1',
            '--argument-substitution-mode', 'NONE',
            '--helm-verification-key-source'
        ]
        # create artifact with inline verification key source
        inlineVerificationKeySource = {
            'currentPublicKey': 'string',
            'previousPublicKey': 'string',
            'verificationKeySourceType': 'INLINE_PUBLIC_KEY'
        }
        params.append(json.dumps(inlineVerificationKeySource))
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        inline_artifact_id = json.loads(result.output)['data']['id']
        vaultVerificationKeySource = {
            'vaultSecretId': 'ocid1.vaultsecret.oc1.phx.amaaaaaawk2b2fiakgyn3l3qsxjwtkupvac7gd26gyxsexrqxi26opjudwxa',
            'verificationKeySourceType': 'VAULT_SECRET'
        }
        # remove inline verification key source and replace with vault verification key source
        params.pop()
        params.append(json.dumps(vaultVerificationKeySource))
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        vault_artifact_id = json.loads(result.output)['data']['id']
    yield inline_artifact_id, vault_artifact_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('devops_deploy_artifact_helm_repository_artifact_verification_key_source_fixture_cleanup.yml'):
        # delete deploy artifact
        params = ['devops', 'deploy-artifact', 'delete', '--artifact-id', inline_artifact_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        params = ['devops', 'deploy-artifact', 'delete', '--artifact-id', vault_artifact_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_get_helm_repository_artifact_verification_source(deploy_helm_repository_artifact_verification_key_source, config_file, config_profile):
    inline_artifact_id = deploy_helm_repository_artifact_verification_key_source[0]
    params = ['devops', 'deploy-artifact', 'get', '--artifact-id', inline_artifact_id]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    output = json.loads(result.output)
    assert inline_artifact_id == output['data']['id'], \
        "Get Deploy Artifact API should return correct Deploy Artifact ID"
    assert 'INLINE_PUBLIC_KEY' == output['data']['deploy-artifact-source']['helm-verification-key-source']['verification-key-source-type'], \
        "Get Deploy Artifact API should return correct InlineVerificationKeySource"
    assert 'string' == output['data']['deploy-artifact-source']['helm-verification-key-source']['current-public-key'], \
        "Get Deploy Artifact API should return correct current public key"
    assert 'string' == output['data']['deploy-artifact-source']['helm-verification-key-source']['previous-public-key'], \
        "Get Deploy Artifact API should return correct previous public key"

    # remove inline verification key source OCID and replace with vault verification key source OCID
    vault_artifact_id = deploy_helm_repository_artifact_verification_key_source[1]
    params.pop()
    params.append(vault_artifact_id)
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    output = json.loads(result.output)
    assert vault_artifact_id == output['data']['id'], \
        "Get Deploy Artifact API should return correct Deploy Artifact ID"
    assert 'VAULT_SECRET' == output['data']['deploy-artifact-source']['helm-verification-key-source']['verification-key-source-type'], \
        "Get Deploy Artifact API should return correct VaultVerificationKeySource"
    assert 'ocid1.vaultsecret.oc1.phx.amaaaaaawk2b2fiakgyn3l3qsxjwtkupvac7gd26gyxsexrqxi26opjudwxa' == output['data']['deploy-artifact-source']['helm-verification-key-source']['vault-secret-id'], \
        "Get Deploy Artifact API should return correct vault secret OCID"


@pytest.fixture(scope='module')
def deploy_oke_cluster_environment(project_and_pipeline, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_deploy_environment_oke_cluster_environment_fixture.yml'):
        # create deploy environment
        project_id = project_and_pipeline[0]
        params = [
            'devops', 'deploy-environment', 'create-oke-cluster-environment',
            '--project-id', project_id,
            '--cluster-id', 'ocid1.cluster.oc1.iad.aaaaaaaaxf62ez6wa75gd3bg4ntf2x2knn7m6u4n7kgrrzfsocelgugbbd7q'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        deploy_environment_id = json.loads(result.output)['data']['id']
    yield deploy_environment_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_deploy_environment_oke_cluster_environment_fixture_cleanup.yml'):
        # delete deploy environment
        params = ['devops', 'deploy-environment', 'delete', '--environment-id', deploy_environment_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_get_oke_cluster_environment(deploy_oke_cluster_environment, config_file, config_profile):
    deploy_environment_id = deploy_oke_cluster_environment
    params = ['devops', 'deploy-environment', 'get', '--environment-id', deploy_environment_id]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert deploy_environment_id == json.loads(result.output)['data']['id'], \
        "Get Deploy Environment API should return correct deploy environment id"


@pytest.fixture(scope='module')
def deploy_oke_helm_chart_stage(project_and_pipeline, deploy_helm_repository_artifact, deploy_oke_cluster_environment, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_deploy_stage_oke_helm_chart_stage_fixture.yml'):
        # create deploy stage
        deploy_pipeline_id = project_and_pipeline[1]
        deploy_artifact_id = deploy_helm_repository_artifact
        deploy_environment_id = deploy_oke_cluster_environment
        deploy_stage_name = util.random_name('cli_devops_deploy_test_deploy_stage_oke_helm_chart_stage')
        stage_predecessor_collection = {
            'items': [
                {
                    'id': deploy_pipeline_id
                }
            ]
        }
        params = [
            'devops', 'deploy-stage', 'create-oke-helm-chart-stage',
            '--pipeline-id', deploy_pipeline_id,
            '--display-name', deploy_stage_name,
            '--oke-cluster-environment-id', deploy_environment_id,
            '--helm-chart-artifact-id', deploy_artifact_id,
            '--release-name', 'cli-test-release',
            '--stage-predecessor-collection', json.dumps(stage_predecessor_collection),
            '--history-max', '15',
            '--reuse-values', 'True',
            '--reset-values', 'True',
            '--debug-helm', 'True',
            '--force-helm', 'True',
            '--wait-helm', 'True',
            '--cleanup-on-fail', 'True'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        deploy_stage_id = json.loads(result.output)['data']['id']
    yield deploy_stage_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_deploy_stage_oke_helm_chart_stage_fixture_cleanup.yml'):
        # delete deploy stage
        params = ['devops', 'deploy-stage', 'delete', '--stage-id', deploy_stage_id, '--force']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_get_deploy_oke_helm_chart_stage(deploy_oke_helm_chart_stage, config_file, config_profile):
    deploy_helm_chart_stage_id = deploy_oke_helm_chart_stage
    params = ['devops', 'deploy-stage', 'get', '--stage-id', deploy_helm_chart_stage_id]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    output = json.loads(result.output)
    assert deploy_helm_chart_stage_id == output['data']['id'], \
        "Get Deploy Stage API should return correct deploy stage id"
    assert 15 == output['data']['max-history'], \
        "Get Deploy Stage API should return correct max-history value"
    assert output['data']['should-reuse-values'] is True, \
        "Get Deploy Stage API should return correct should-reuse-values value"
    assert output['data']['should-reset-values'] is True, \
        "Get Deploy Stage API should return correct should-reset-values value"
    assert output['data']['should-skip-crds'] is False, \
        "Get Deploy Stage API should return correct should-skip-crds value"
    assert output['data']['should-skip-render-subchart-notes'] is True, \
        "Get Deploy Stage API should return correct should-skip-render-subchart-notes value"
    assert output['data']['should-not-wait'] is False, \
        "Get Deploy Stage API should return correct should-not-wait value"
    assert output['data']['is-force-enabled'] is True, \
        "Get Deploy Stage API should return correct is-force-enabled value"
    assert output['data']['is-debug-enabled'] is True, \
        "Get Deploy Stage API should return correct is-debug-enabled value"
    assert output['data']['should-cleanup-on-fail'] is True, \
        "Get Deploy Stage API should return correct should-cleanup-on-fail value"


@pytest.fixture(scope='module')
def dry_run_pipeline_deployment(project_and_pipeline, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'devops_deploy_deployment_dry_run_fixture.yml'):
        pipeline_id = project_and_pipeline[1]
        deployment_arguments = {
            'items': [{
                'name': 'foo',
                'value': 'bar'
            }]
        }
        params = ['devops', 'deployment', 'create-pipeline-deployment',
                  '--pipeline-id', pipeline_id,
                  '--deployment-arguments', json.dumps(deployment_arguments),
                  '--dry-run', 'True']
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        deployment_id = json.loads(result.output)['data']['id']
        yield deployment_id


@pytest.mark.skip('failed in validation')
def test_dry_run_pipeline_deployment(dry_run_pipeline_deployment, config_file, config_profile):
    deployment_id = dry_run_pipeline_deployment
    params = ['devops', 'deployment', 'get', '--deployment-id', deployment_id]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    output = json.loads(result.output)
    assert deployment_id == output['data']['id'], \
        "Get Deployment API should return correct deployment id"
    assert "True" == output['data']['deployment-arguments']['items'][1]['value'], \
        "Get Deployment API should have dry_run value set as false in deployment arguments"
    assert 'dry_run' == output['data']['deployment-arguments']['items'][1]['name'], \
        "Get Deployment API should have dry_run argument name in deployment arguments"


def invoke(runner, config_file, config_profile, params, debug=False, ** args):
    all_params = params + ['--config-file', config_file, '--profile', config_profile]
    if debug is True:
        all_params = all_params + ['--debug']
    result = runner.invoke(oci_cli.cli, all_params, **args)
    return result
