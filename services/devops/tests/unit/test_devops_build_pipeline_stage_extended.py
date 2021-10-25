# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/devops/tests/unit/test_devops_build_pipeline_stage_extended.py
class TestDevopsBuildPipelineStage(unittest.TestCase):
    def setUp(self):
        pass

    def test_build_pipeline_stage(self):
        result = util.invoke_command(['devops', 'build-pipeline-stage'])
        assert 'Commands:' in result.output
        assert 'create-build-stage' in result.output
        assert 'create-wait-stage' in result.output
        assert 'create-deliver-artifact-stage' in result.output
        assert 'create-trigger-deployment-stage' in result.output
        assert 'get' in result.output
        assert 'update-build-stage' in result.output
        assert 'update-wait-stage' in result.output
        assert 'update-deliver-artifact-stage' in result.output
        assert 'update-trigger-deployment-stage' in result.output
        assert 'delete' in result.output
        assert 'list' in result.output

    def test_build_stage_create(self):
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-build-stage'])
        assert 'Error: Missing option(s)' in result.output
        assert '--build-pipeline-id' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-build-stage', '--build-pipeline-id'])
        assert 'Error: --build-pipeline-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-build-stage', '--description'])
        assert 'Error: --description option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-build-stage', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-build-stage', '--build-spec-file'])
        assert 'Error: --build-spec-file option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-build-stage', '--image'])
        assert 'Error: --image option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-build-stage', '--primary-build-source'])
        assert 'Error: --primary-build-source option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-build-stage', '--build-source-collection'])
        assert 'Error: --build-source-collection option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-build-stage', '--stage-predecessor-collection'])
        assert 'Error: --stage-predecessor-collection option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-build-stage', '--stage-execution-timeout-in-seconds'])
        assert 'Error: --stage-execution-timeout-in-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-build-stage', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-build-stage', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-build-stage', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-build-stage', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-build-stage', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_wait_stage_create(self):
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-wait-stage'])
        assert 'Error: Missing option(s)' in result.output
        assert '--build-pipeline-id' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-wait-stage', '--build-pipeline-id'])
        assert 'Error: --build-pipeline-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-wait-stage', '--description'])
        assert 'Error: --description option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-wait-stage', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-wait-stage', '--wait-criteria'])
        assert 'Error: --wait-criteria option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-wait-stage', '--stage-predecessor-collection'])
        assert 'Error: --stage-predecessor-collection option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-wait-stage', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-wait-stage', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-wait-stage', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-wait-stage', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-wait-stage', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_deliver_artifact_stage_create(self):
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-deliver-artifact-stage'])
        assert 'Error: Missing option(s)' in result.output
        assert '--build-pipeline-id' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-deliver-artifact-stage', '--build-pipeline-id'])
        assert 'Error: --build-pipeline-id option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-deliver-artifact-stage', '--description'])
        assert 'Error: --description option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-deliver-artifact-stage', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-deliver-artifact-stage', '--deliver-artifact-collection'])
        assert 'Error: --deliver-artifact-collection option requires an argument' in result.output
        result = util.invoke_command([
            'devops', 'build-pipeline-stage', 'create-deliver-artifact-stage', '--stage-predecessor-collection'])
        assert 'Error: --stage-predecessor-collection option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-deliver-artifact-stage', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-deliver-artifact-stage', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-deliver-artifact-stage', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-deliver-artifact-stage', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-deliver-artifact-stage', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_trigger_deployment_stage_create(self):
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'create-trigger-deployment-stage'])
        assert 'Error: Missing option(s)' in result.output
        assert '--build-pipeline-id' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-trigger-deployment-stage', '--build-pipeline-id'])
        assert 'Error: --build-pipeline-id option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-trigger-deployment-stage', '--deploy-pipeline-id'])
        assert 'Error: --deploy-pipeline-id option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-trigger-deployment-stage', '--description'])
        assert 'Error: --description option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-trigger-deployment-stage', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-trigger-deployment-stage', '--is-pass-all-parameters-enabled'])
        assert 'Error: --is-pass-all-parameters-enabled option requires an argument' in result.output
        result = util.invoke_command([
            'devops', 'build-pipeline-stage', 'create-trigger-deployment-stage', '--stage-predecessor-collection'])
        assert 'Error: --stage-predecessor-collection option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-trigger-deployment-stage', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-trigger-deployment-stage', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-trigger-deployment-stage', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-trigger-deployment-stage', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'create-trigger-deployment-stage', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_build_pipeline_stage_get(self):
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--stage-id' in result.output

    def test_build_stage_update(self):
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-build-stage'])
        assert 'Error: Missing option(s)' in result.output
        assert '--stage-id' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-build-stage', '--stage-id'])
        assert 'Error: --stage-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-build-stage', '--description'])
        assert 'Error: --description option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-build-stage', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-build-stage', '--build-spec-file'])
        assert 'Error: --build-spec-file option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-build-stage', '--image'])
        assert 'Error: --image option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-build-stage', '--primary-build-source'])
        assert 'Error: --primary-build-source option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-build-stage', '--build-source-collection'])
        assert 'Error: --build-source-collection option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-build-stage', '--stage-predecessor-collection'])
        assert 'Error: --stage-predecessor-collection option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-build-stage', '--stage-execution-timeout-in-seconds'])
        assert 'Error: --stage-execution-timeout-in-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-build-stage', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-build-stage', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-build-stage', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-build-stage', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-build-stage', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_wait_stage_update(self):
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-wait-stage'])
        assert 'Error: Missing option(s)' in result.output
        assert '--stage-id' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-wait-stage', '--stage-id'])
        assert 'Error: --stage-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-wait-stage', '--description'])
        assert 'Error: --description option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-wait-stage', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-wait-stage', '--wait-criteria'])
        assert 'Error: --wait-criteria option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-wait-stage', '--stage-predecessor-collection'])
        assert 'Error: --stage-predecessor-collection option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-wait-stage', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-wait-stage', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-wait-stage', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-wait-stage', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-wait-stage', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_deliver_artifact_stage_update(self):
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-deliver-artifact-stage'])
        assert 'Error: Missing option(s)' in result.output
        assert '--stage-id' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-deliver-artifact-stage', '--stage-id'])
        assert 'Error: --stage-id option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-deliver-artifact-stage', '--description'])
        assert 'Error: --description option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-deliver-artifact-stage', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-deliver-artifact-stage', '--deliver-artifact-collection'])
        assert 'Error: --deliver-artifact-collection option requires an argument' in result.output
        result = util.invoke_command([
            'devops', 'build-pipeline-stage', 'update-deliver-artifact-stage', '--stage-predecessor-collection'])
        assert 'Error: --stage-predecessor-collection option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-deliver-artifact-stage', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-deliver-artifact-stage', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-deliver-artifact-stage', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-deliver-artifact-stage', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-deliver-artifact-stage', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_trigger_deployment_stage_update(self):
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'update-trigger-deployment-stage'])
        assert 'Error: Missing option(s)' in result.output
        assert '--stage-id' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-trigger-deployment-stage', '--stage-id'])
        assert 'Error: --stage-id option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-trigger-deployment-stage', '--deploy-pipeline-id'])
        assert 'Error: --deploy-pipeline-id option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-trigger-deployment-stage', '--description'])
        assert 'Error: --description option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-trigger-deployment-stage', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-trigger-deployment-stage', '--is-pass-all-parameters-enabled'])
        assert 'Error: --is-pass-all-parameters-enabled option requires an argument' in result.output
        result = util.invoke_command([
            'devops', 'build-pipeline-stage', 'update-trigger-deployment-stage', '--stage-predecessor-collection'])
        assert 'Error: --stage-predecessor-collection option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-trigger-deployment-stage', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-trigger-deployment-stage', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-trigger-deployment-stage', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-trigger-deployment-stage', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'build-pipeline-stage', 'update-trigger-deployment-stage', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_build_pipeline_stage_delete(self):
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--stage-id' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'delete', '--stage-id'])
        assert 'Error: --stage-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'delete', '--if-match'])
        assert 'Error: --if-match option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'delete', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'delete', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'delete', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output

    def test_build_pipeline_stage_list(self):
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'list', '--id'])
        assert 'Error: --id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'list', '--build-pipeline-id'])
        assert 'Error: --build-pipeline-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'list', '--compartment-id'])
        assert 'Error: --compartment-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'list', '--lifecycle-state'])
        assert 'Error: --lifecycle-state option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'list', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'list', '--limit'])
        assert 'Error: --limit option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'list', '--page'])
        assert 'Error: --page option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'list', '--page-size'])
        assert 'Error: --page-size option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'list', '--sort-order'])
        assert 'Error: --sort-order option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'list', '--sort-by'])
        assert 'Error: --sort-by option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline-stage', 'list', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
