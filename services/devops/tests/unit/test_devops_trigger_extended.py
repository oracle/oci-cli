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
        assert 'Error: Option \'--project-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger', '--description'])
        assert 'Error: Option \'--description\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger', '--actions'])
        assert 'Error: Option \'--actions\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger', '--repository-id'])
        assert 'Error: Option \'--repository-id\' requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'trigger', 'create-devops-code-repo-trigger', '--max-wait-seconds'])
        assert 'Error: Option \'--max-wait-seconds\' requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'trigger', 'create-devops-code-repo-trigger', '--wait-interval-seconds'])
        assert 'Error: Option \'--wait-interval-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger', '--defined-tags'])
        assert 'Error: Option \'--defined-tags\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-devops-code-repo-trigger', '--freeform-tags'])
        assert 'Error: Option \'--freeform-tags\' requires an argument' in result.output

    def test_github_trigger_create(self):
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger'])
        assert 'Error: Missing option(s)' in result.output
        assert '--project-id' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--project-id'])
        assert 'Error: Option \'--project-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--description'])
        assert 'Error: Option \'--description\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--actions'])
        assert 'Error: Option \'--actions\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--max-wait-seconds'])
        assert 'Error: Option \'--max-wait-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--wait-interval-seconds'])
        assert 'Error: Option \'--wait-interval-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--defined-tags'])
        assert 'Error: Option \'--defined-tags\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-github-trigger', '--freeform-tags'])
        assert 'Error: Option \'--freeform-tags\' requires an argument' in result.output

    def test_gitlab_trigger_create(self):
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger'])
        assert 'Error: Missing option(s)' in result.output
        assert '--project-id' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--project-id'])
        assert 'Error: Option \'--project-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--description'])
        assert 'Error: Option \'--description\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--actions'])
        assert 'Error: Option \'--actions\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--max-wait-seconds'])
        assert 'Error: Option \'--max-wait-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--wait-interval-seconds'])
        assert 'Error: Option \'--wait-interval-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--defined-tags'])
        assert 'Error: Option \'--defined-tags\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'create-gitlab-trigger', '--freeform-tags'])
        assert 'Error: Option \'--freeform-tags\' requires an argument' in result.output

    def test_trigger_get(self):
        result = util.invoke_command(['devops', 'trigger', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--trigger-id' in result.output

    def test_devops_code_repos_trigger_update(self):
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger'])
        assert 'Error: Missing option(s)' in result.output
        assert '--trigger-id' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--trigger-id'])
        assert 'Error: Option \'--trigger-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--description'])
        assert 'Error: Option \'--description\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--actions'])
        assert 'Error: Option \'--actions\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--repository-id'])
        assert 'Error: Option \'--repository-id\' requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'trigger', 'update-devops-code-repo-trigger', '--max-wait-seconds'])
        assert 'Error: Option \'--max-wait-seconds\' requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'trigger', 'update-devops-code-repo-trigger', '--wait-interval-seconds'])
        assert 'Error: Option \'--wait-interval-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--defined-tags'])
        assert 'Error: Option \'--defined-tags\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-devops-code-repo-trigger', '--freeform-tags'])
        assert 'Error: Option \'--freeform-tags\' requires an argument' in result.output

    def test_github_trigger_update(self):
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger'])
        assert 'Error: Missing option(s)' in result.output
        assert '--trigger-id' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--trigger-id'])
        assert 'Error: Option \'--trigger-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--description'])
        assert 'Error: Option \'--description\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--actions'])
        assert 'Error: Option \'--actions\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--max-wait-seconds'])
        assert 'Error: Option \'--max-wait-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--wait-interval-seconds'])
        assert 'Error: Option \'--wait-interval-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--defined-tags'])
        assert 'Error: Option \'--defined-tags\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-github-trigger', '--freeform-tags'])
        assert 'Error: Option \'--freeform-tags\' requires an argument' in result.output

    def test_gitlab_trigger_update(self):
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger'])
        assert 'Error: Missing option(s)' in result.output
        assert '--trigger-id' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--trigger-id'])
        assert 'Error: Option \'--trigger-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--description'])
        assert 'Error: Option \'--description\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--actions'])
        assert 'Error: Option \'--actions\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--max-wait-seconds'])
        assert 'Error: Option \'--max-wait-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--wait-interval-seconds'])
        assert 'Error: Option \'--wait-interval-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--defined-tags'])
        assert 'Error: Option \'--defined-tags\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'update-gitlab-trigger', '--freeform-tags'])
        assert 'Error: Option \'--freeform-tags\' requires an argument' in result.output

    def test_trigger_delete(self):
        result = util.invoke_command(['devops', 'trigger', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--trigger-id' in result.output
        result = util.invoke_command(['devops', 'trigger', 'delete', '--trigger-id'])
        assert 'Error: Option \'--trigger-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'delete', '--if-match'])
        assert 'Error: Option \'--if-match\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'delete', '--max-wait-seconds'])
        assert 'Error: Option \'--max-wait-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'delete', '--wait-interval-seconds'])
        assert 'Error: Option \'--wait-interval-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'delete', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output

    def test_trigger_list(self):
        result = util.invoke_command(['devops', 'trigger', 'list', '--id'])
        assert 'Error: Option \'--id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--project-id'])
        assert 'Error: Option \'--project-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--compartment-id'])
        assert 'Error: Option \'--compartment-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--lifecycle-state'])
        assert 'Error: Option \'--lifecycle-state\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--limit'])
        assert 'Error: Option \'--limit\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--page'])
        assert 'Error: Option \'--page\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--page-size'])
        assert 'Error: Option \'--page-size\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--sort-order'])
        assert 'Error: Option \'--sort-order\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--sort-by'])
        assert 'Error: Option \'--sort-by\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'trigger', 'list', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output
