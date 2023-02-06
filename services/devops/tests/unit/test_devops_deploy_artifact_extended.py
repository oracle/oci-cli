# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/devops/tests/unit/test_devops_deploy_artifact_extended.py
class TestDevopsDeployArtifact(unittest.TestCase):
    def setUp(self):
        pass

    @unittest.skip("Failing master")
    def test_devops_deploy_artifact_create_helm_repository_artifact(self):
        result = util.invoke_command(['devops', 'deploy-artifact', 'create-helm-repository-artifact'])
        assert 'Error: Missing option(s)' in result.output
        result = util.invoke_command(['devops', 'deploy-artifact', 'create-helm-repository-artifact', '--artifact-type'])
        assert 'Error: Option \'--artifact-type\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-artifact', 'create-helm-repository-artifact', '--project-id'])
        assert 'Error: Option \'--project-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-artifact', 'create-helm-repository-artifact', '--argument-substitution-mode'])
        assert 'Error: Option \'--argument-substitution-mode\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-artifact', 'create-helm-repository-artifact', '--artifact-chart-url'])
        assert 'Error: Option \'--artifact-chart-url\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-artifact', 'create-helm-repository-artifact', '--artifact-version'])
        assert 'Error: Option \'--artifact-version\' requires an argument' in result.output

    @unittest.skip("Failing")
    def test_devops_deploy_artifact_create_helm_repository_artifact_verification_key_source(self):
        result = util.invoke_command(['devops', 'deploy-artifact', 'create-helm-repository-artifact', '--helm-verification-key-source'])
        assert 'Error: Option \'--helm-verification-key-source\' requires an argument' in result.output

    @unittest.skip("Failing")
    def test_devops_deploy_artifact_update_helm_repository_artifact(self):
        result = util.invoke_command(['devops', 'deploy-artifact', 'update-helm-repository-artifact'])
        assert 'Error: Missing option(s)' in result.output
        result = util.invoke_command(['devops', 'deploy-artifact', 'update-helm-repository-artifact', '--artifact-id'])
        assert 'Error: Option \'--artifact-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-artifact', 'update-helm-repository-artifact', '--artifact-chart-url'])
        assert 'Error: Option \'--artifact-chart-url\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-artifact', 'update-helm-repository-artifact', '--artifact-version'])
        assert 'Error: Option \'--artifact-version\' requires an argument' in result.output

    @unittest.skip("Failing")
    def test_devops_deploy_artifact_update_helm_repository_artifact_verification_key_source(self):
        result = util.invoke_command(['devops', 'deploy-artifact', 'update-helm-repository-artifact', '--helm-verification-key-source'])
        assert 'Error: Option \'--helm-verification-key-source\' requires an argument' in result.output
