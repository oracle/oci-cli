# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/devops/tests/unit/test_devops_build_run_extended.py
class TestDevopsBuildrun(unittest.TestCase):
    def setUp(self):
        pass

    def test_build_run(self):
        result = util.invoke_command(['devops', 'build-run'])
        assert 'Commands:' in result.output
        assert 'create' in result.output
        assert 'get' in result.output
        assert 'update' in result.output
        assert 'cancel' in result.output
        assert 'list' in result.output

    def test_build_run_create(self):
        result = util.invoke_command(['devops', 'build-run', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--build-pipeline-id' in result.output
        result = util.invoke_command(['devops', 'build-run', 'create', '--build-pipeline-id'])
        assert 'Error: --build-pipeline-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'create', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'create', '--commit-info'])
        assert 'Error: --commit-info option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'create', '--build-run-arguments'])
        assert 'Error: --build-run-arguments option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'create', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'create', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'create', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'create', '--if-match'])
        assert 'Error: --if-match option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'create', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'create', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_build_run_get(self):
        result = util.invoke_command(['devops', 'build-run', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--build-run-id' in result.output

    def test_build_run_update(self):
        result = util.invoke_command(['devops', 'build-run', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--build-run-id' in result.output
        result = util.invoke_command(['devops', 'build-run', 'update', '--build-run-id'])
        assert 'Error: --build-run-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'update', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'update', '--if-match'])
        assert 'Error: --if-match option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'update', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'update', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'update', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'update', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'update', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_build_run_cancel(self):
        result = util.invoke_command(['devops', 'build-run', 'cancel'])
        assert 'Error: Missing option(s)' in result.output
        assert '--build-run-id' in result.output
        result = util.invoke_command(['devops', 'build-run', 'cancel', '--build-run-id'])
        assert 'Error: --build-run-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'cancel', '--reason'])
        assert 'Error: --reason option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'cancel', '--if-match'])
        assert 'Error: --if-match option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'cancel', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'cancel', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'cancel', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output

    def test_build_run_list(self):
        result = util.invoke_command(['devops', 'build-run', 'list', '--id'])
        assert 'Error: --id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'list', '--build-pipeline-id'])
        assert 'Error: --build-pipeline-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'list', '--compartment-id'])
        assert 'Error: --compartment-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'list', '--lifecycle-state'])
        assert 'Error: --lifecycle-state option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'list', '--project-id'])
        assert 'Error: --project-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'list', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'list', '--limit'])
        assert 'Error: --limit option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'list', '--page'])
        assert 'Error: --page option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'list', '--page-size'])
        assert 'Error: --page-size option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'list', '--sort-order'])
        assert 'Error: --sort-order option requires an argument' in result.output
        result = util.invoke_command(['devops', 'build-run', 'list', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
