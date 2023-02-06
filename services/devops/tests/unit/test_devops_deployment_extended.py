# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/devops/tests/unit/test_devops_deployment_extended.py
class TestDevopsDeployment(unittest.TestCase):
    def setUp(self):
        pass

    def test_devops_deployment_create_pipeline_deployment(self):
        result = util.invoke_command(['devops', 'deployment', 'create-pipeline-deployment'])
        assert 'Error: Missing option(s)' in result.output

    @unittest.skip("Failing")
    def test_devops_deployment_create_pipeline_deployment_dry_run(self):
        result = util.invoke_command(['devops', 'deployment', 'create-pipeline-deployment', '--dry-run'])
        assert 'Error: Option \'--dry-run\' requires an argument' in result.output
