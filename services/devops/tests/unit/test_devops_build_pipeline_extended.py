# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/devops/tests/unit/test_devops_build_pipeline_extended.py
class TestDevopsBuildPipeline(unittest.TestCase):
    def setUp(self):
        pass

    def test_devops_build(self):
        result = util.invoke_command(['devops'])
        assert 'Commands:' in result.output
        assert 'build-pipeline' in result.output
        assert 'build-run' in result.output
        assert 'build-pipeline-stage' in result.output
        assert 'connection' in result.output
        assert 'trigger' in result.output

    def test_build_pipeline(self):
        result = util.invoke_command(['devops', 'build-pipeline'])
        assert 'Commands:' in result.output
        assert 'create' in result.output
        assert 'get' in result.output
        assert 'update' in result.output
        assert 'delete' in result.output
        assert 'list' in result.output

    def test_build_pipeline_create(self):
        result = util.invoke_command(['devops', 'build-pipeline', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--project-id' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'create', '--project-id'])
        assert 'Error: Option \'--project-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'create', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'create', '--description'])
        assert 'Error: Option \'--description\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'create', '--build-pipeline-parameters'])
        assert 'Error: Option \'--build-pipeline-parameters\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'create', '--max-wait-seconds'])
        assert 'Error: Option \'--max-wait-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'create', '--wait-interval-seconds'])
        assert 'Error: Option \'--wait-interval-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'create', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'create', '--defined-tags'])
        assert 'Error: Option \'--defined-tags\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'create', '--freeform-tags'])
        assert 'Error: Option \'--freeform-tags\' requires an argument' in result.output

    def test_build_pipeline_get(self):
        result = util.invoke_command(['devops', 'build-pipeline', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--build-pipeline-id' in result.output

    def test_build_pipeline_update(self):
        result = util.invoke_command(['devops', 'build-pipeline', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--build-pipeline-id' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'update', '--build-pipeline-id'])
        assert 'Error: Option \'--build-pipeline-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'update', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'update', '--description'])
        assert 'Error: Option \'--description\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'update', '--build-pipeline-parameters'])
        assert 'Error: Option \'--build-pipeline-parameters\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'update', '--max-wait-seconds'])
        assert 'Error: Option \'--max-wait-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'update', '--wait-interval-seconds'])
        assert 'Error: Option \'--wait-interval-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'update', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'update', '--defined-tags'])
        assert 'Error: Option \'--defined-tags\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'update', '--freeform-tags'])
        assert 'Error: Option \'--freeform-tags\' requires an argument' in result.output

    def test_build_pipeline_delete(self):
        result = util.invoke_command(['devops', 'build-pipeline', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--build-pipeline-id' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'delete', '--build-pipeline-id'])
        assert 'Error: Option \'--build-pipeline-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'delete', '--if-match'])
        assert 'Error: Option \'--if-match\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'delete', '--max-wait-seconds'])
        assert 'Error: Option \'--max-wait-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'delete', '--wait-interval-seconds'])
        assert 'Error: Option \'--wait-interval-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'delete', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output

    def test_build_pipeline_list(self):
        result = util.invoke_command(['devops', 'build-pipeline', 'list', '--id'])
        assert 'Error: Option \'--id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'list', '--compartment-id'])
        assert 'Error: Option \'--compartment-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'list', '--project-id'])
        assert 'Error: Option \'--project-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'list', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'list', '--limit'])
        assert 'Error: Option \'--limit\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'list', '--page'])
        assert 'Error: Option \'--page\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'list', '--page-size'])
        assert 'Error: Option \'--page-size\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'list', '--sort-order'])
        assert 'Error: Option \'--sort-order\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-pipeline', 'list', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output
