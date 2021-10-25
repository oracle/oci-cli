# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/devops/tests/unit/test_devops_trigger_extended.py
class TestDevopsBuildApi(unittest.TestCase):
    def setUp(self):
        pass

    def test_trigger(self):
        result = util.invoke_command(['devops', 'trigger'])
        assert 'Commands:' in result.output
        assert 'create-devops-code-repo-trigger' in result.output
        assert 'create-github-trigger' in result.output
        assert 'create-gitlab-trigger' in result.output
        assert 'get' in result.output
        assert 'update-devops-code-repo-trigger' in result.output
        assert 'update-github-trigger' in result.output
        assert 'update-gitlab-trigger' in result.output
        assert 'delete' in result.output
        assert 'list' in result.output

    def test_devops_code_repos_trigger_create(self):
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger'])
        assert 'Error: Missing option(s)' in result.output
        assert '--project-id' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger', '--project-id'])
        assert 'Error: --project-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger', '--description'])
        assert 'Error: --description option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger', '--actions'])
        assert 'Error: --actions option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger', '--repository-id'])
        assert 'Error: --repository-id option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'trigger', 'create-devops-code-repo-trigger', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'trigger', 'create-devops-code-repo-trigger', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_github_trigger_create(self):
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger'])
        assert 'Error: Missing option(s)' in result.output
        assert '--project-id' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--project-id'])
        assert 'Error: --project-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--description'])
        assert 'Error: --description option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--actions'])
        assert 'Error: --actions option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_gitlab_trigger_create(self):
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger'])
        assert 'Error: Missing option(s)' in result.output
        assert '--project-id' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--project-id'])
        assert 'Error: --project-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--description'])
        assert 'Error: --description option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--actions'])
        assert 'Error: --actions option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_trigger_get(self):
        result = util.invoke_command(['devops', 'trigger', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--trigger-id' in result.output

    def test_devops_code_repos_trigger_update(self):
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger'])
        assert 'Error: Missing option(s)' in result.output
        assert '--trigger-id' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--trigger-id'])
        assert 'Error: --trigger-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--description'])
        assert 'Error: --description option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--actions'])
        assert 'Error: --actions option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--repository-id'])
        assert 'Error: --repository-id option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'trigger', 'update-devops-code-repo-trigger', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'trigger', 'update-devops-code-repo-trigger', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_github_trigger_update(self):
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger'])
        assert 'Error: Missing option(s)' in result.output
        assert '--trigger-id' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--trigger-id'])
        assert 'Error: --trigger-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--description'])
        assert 'Error: --description option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--actions'])
        assert 'Error: --actions option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_gitlab_trigger_update(self):
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger'])
        assert 'Error: Missing option(s)' in result.output
        assert '--trigger-id' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--trigger-id'])
        assert 'Error: --trigger-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--description'])
        assert 'Error: --description option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--actions'])
        assert 'Error: --actions option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output

    def test_trigger_delete(self):
        result = util.invoke_command(['devops', 'trigger', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--trigger-id' in result.output
        result = util.invoke_command(['devops', 'trigger', 'delete', '--trigger-id'])
        assert 'Error: --trigger-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'delete', '--if-match'])
        assert 'Error: --if-match option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'delete', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'delete', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'delete', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output

    def test_trigger_list(self):
        result = util.invoke_command(['devops', 'trigger', 'list', '--id'])
        assert 'Error: --id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--project-id'])
        assert 'Error: --project-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--compartment-id'])
        assert 'Error: --compartment-id option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--lifecycle-state'])
        assert 'Error: --lifecycle-state option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--limit'])
        assert 'Error: --limit option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--page'])
        assert 'Error: --page option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--page-size'])
        assert 'Error: --page-size option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--sort-order'])
        assert 'Error: --sort-order option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--sort-by'])
        assert 'Error: --sort-by option requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--from-json'])
        assert 'Error: --from-json option requires an argument' in result.output
