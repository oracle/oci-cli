# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/devops/tests/unit/test_devops_deploy_stage_extended.py
class TestDevopsDeployStage(unittest.TestCase):
    def setUp(self):
        pass

    @unittest.skip("Failing")
    def test_devops_deploy_stage_create_oke_helm_chart_stage(self):
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage'])
        assert 'Error: Missing option(s)' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--pipeline-id'])
        assert 'Error: Option \'--pipeline-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--stage-predecessor-collection'])
        assert 'Error: Option \'--stage-predecessor-collection\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--oke-cluster-environment-id'])
        assert 'Error: Option \'--oke-cluster-environment-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--release-name'])
        assert 'Error: Option \'--release-name\' requires an argument' in result.output

    @unittest.skip("Failing")
    def test_devops_deploy_stage_create_oke_helm_chart_stage_args(self):
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '-h'])
        assert '--cleanup-on-fail' in result.output
        assert '--debug-helm' in result.output
        assert '--force-helm' in result.output
        assert '--history-max' in result.output
        assert '--no-hooks' in result.output
        assert '--render-subchart-notes' in result.output
        assert '--reset-values' in result.output
        assert '--reuse-values' in result.output
        assert '--set-values' in result.output
        assert '--set-string' in result.output
        assert '--skip-crds' in result.output
        assert '--wait-helm' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--cleanup-on-fail'])
        assert 'Error: Option \'--cleanup-on-fail\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--debug-helm'])
        assert 'Error: Option \'--debug-helm\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--force-helm'])
        assert 'Error: Option \'--force-helm\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--history-max'])
        assert 'Error: Option \'--history-max\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--no-hooks'])
        assert 'Error: Option \'--no-hooks\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--render-subchart-notes'])
        assert 'Error: Option \'--render-subchart-notes\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--reset-values'])
        assert 'Error: Option \'--reset-values\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--reuse-values'])
        assert 'Error: Option \'--reuse-values\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--set-values'])
        assert 'Error: Option \'--set-values\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--set-string'])
        assert 'Error: Option \'--set-string\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--skip-crds'])
        assert 'Error: Option \'--skip-crds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'create-oke-helm-chart-stage', '--wait-helm'])
        assert 'Error: Option \'--wait-helm\' requires an argument' in result.output

    def test_devops_deploy_stage_update_oke_helm_chart_stage(self):
        result = util.invoke_command(['devops', 'deploy-stage', 'update-oke-helm-chart-stage'])
        assert 'Error: Missing option(s)' in result.output

    @unittest.skip("Failing")
    def test_devops_deploy_stage_update_oke_helm_chart_stage_args(self):
        result = util.invoke_command(['devops', 'deploy-stage', 'update-oke-helm-chart-stage', '-h'])
        assert '--cleanup-on-fail' in result.output
        assert '--debug-helm' in result.output
        assert '--force-helm' in result.output
        assert '--history-max' in result.output
        assert '--no-hooks' in result.output
        assert '--render-subchart-notes' in result.output
        assert '--reset-values' in result.output
        assert '--reuse-values' in result.output
        assert '--set-values' in result.output
        assert '--set-string' in result.output
        assert '--skip-crds' in result.output
        assert '--wait-helm' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'update-oke-helm-chart-stage', '--cleanup-on-fail'])
        assert 'Error: Option \'--cleanup-on-fail\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'update-oke-helm-chart-stage', '--debug-helm'])
        assert 'Error: Option \'--debug-helm\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'update-oke-helm-chart-stage', '--force-helm'])
        assert 'Error: Option \'--force-helm\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'update-oke-helm-chart-stage', '--history-max'])
        assert 'Error: Option \'--history-max\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'update-oke-helm-chart-stage', '--no-hooks'])
        assert 'Error: Option \'--no-hooks\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'update-oke-helm-chart-stage', '--render-subchart-notes'])
        assert 'Error: Option \'--render-subchart-notes\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'update-oke-helm-chart-stage', '--reset-values'])
        assert 'Error: Option \'--reset-values\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'update-oke-helm-chart-stage', '--reuse-values'])
        assert 'Error: Option \'--reuse-values\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'update-oke-helm-chart-stage', '--set-values'])
        assert 'Error: Option \'--set-values\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'update-oke-helm-chart-stage', '--set-string'])
        result = util.invoke_command(['devops', 'deploy-stage', 'update-oke-helm-chart-stage', '--skip-crds'])
        assert 'Error: Option \'--skip-crds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'deploy-stage', 'update-oke-helm-chart-stage', '--wait-helm'])
        assert 'Error: Option \'--wait-helm\' requires an argument' in result.output
