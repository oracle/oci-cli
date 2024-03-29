# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/devops/tests/unit/test_devops_connection_extended.py
class TestDevopsConnection(unittest.TestCase):
    def setUp(self):
        pass

    def test_connection(self):
        result = util.invoke_command(['devops', 'connection'])
        assert 'Commands:' in result.output
        assert 'create-github-connection' in result.output
        assert 'create-gitlab-connection' in result.output
        assert 'get' in result.output
        assert 'update-github-connection' in result.output
        assert 'update-gitlab-connection' in result.output
        assert 'delete' in result.output
        assert 'list' in result.output

    def test_github_connection_create(self):
        result = util.invoke_command(['devops', 'connection', 'create-github-connection'])
        assert 'Error: Missing option(s)' in result.output
        assert '--project-id' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-github-connection', '--project-id'])
        assert 'Error: Option \'--project-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-github-connection', '--description'])
        assert 'Error: Option \'--description\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-github-connection', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-github-connection', '--personal-access-token'])
        assert 'Error: Option \'--personal-access-token\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-github-connection', '--max-wait-seconds'])
        assert 'Error: Option \'--max-wait-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-github-connection', '--wait-interval-seconds'])
        assert 'Error: Option \'--wait-interval-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-github-connection', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-github-connection', '--defined-tags'])
        assert 'Error: Option \'--defined-tags\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-github-connection', '--freeform-tags'])
        assert 'Error: Option \'--freeform-tags\' requires an argument' in result.output

    def test_gitlab_connection_create(self):
        result = util.invoke_command(['devops', 'connection', 'create-gitlab-connection'])
        assert 'Error: Missing option(s)' in result.output
        assert '--project-id' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-gitlab-connection', '--project-id'])
        assert 'Error: Option \'--project-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-gitlab-connection', '--description'])
        assert 'Error: Option \'--description\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-gitlab-connection', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-gitlab-connection', '--personal-access-token'])
        assert 'Error: Option \'--personal-access-token\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-gitlab-connection', '--max-wait-seconds'])
        assert 'Error: Option \'--max-wait-seconds\' requires an argument' in result.output
        result = util.invoke_command(
            ['devops', 'connection', 'create-gitlab-connection', '--wait-interval-seconds'])
        assert 'Error: Option \'--wait-interval-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-gitlab-connection', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-gitlab-connection', '--defined-tags'])
        assert 'Error: Option \'--defined-tags\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'create-gitlab-connection', '--freeform-tags'])
        assert 'Error: Option \'--freeform-tags\' requires an argument' in result.output

    def test_connection_get(self):
        result = util.invoke_command(['devops', 'connection', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--connection-id' in result.output

    def test_github_connection_update(self):
        result = util.invoke_command(['devops', 'connection', 'update-github-connection'])
        assert 'Error: Missing option(s)' in result.output
        assert '--connection-id' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-github-connection', '--connection-id'])
        assert 'Error: Option \'--connection-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-github-connection', '--description'])
        assert 'Error: Option \'--description\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-github-connection', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-github-connection', '--personal-access-token'])
        assert 'Error: Option \'--personal-access-token\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-github-connection', '--max-wait-seconds'])
        assert 'Error: Option \'--max-wait-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-github-connection', '--wait-interval-seconds'])
        assert 'Error: Option \'--wait-interval-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-github-connection', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-github-connection', '--defined-tags'])
        assert 'Error: Option \'--defined-tags\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-github-connection', '--freeform-tags'])
        assert 'Error: Option \'--freeform-tags\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-github-connection', '--if-match'])
        assert 'Error: Option \'--if-match\' requires an argument' in result.output

    def test_gitlab_connection_update(self):
        result = util.invoke_command(['devops', 'connection', 'update-gitlab-connection'])
        assert 'Error: Missing option(s)' in result.output
        assert '--connection-id' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-gitlab-connection', '--connection-id'])
        assert 'Error: Option \'--connection-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-gitlab-connection', '--description'])
        assert 'Error: Option \'--description\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-gitlab-connection', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-gitlab-connection', '--personal-access-token'])
        assert 'Error: Option \'--personal-access-token\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-gitlab-connection', '--max-wait-seconds'])
        assert 'Error: Option \'--max-wait-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-gitlab-connection', '--wait-interval-seconds'])
        assert 'Error: Option \'--wait-interval-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-gitlab-connection', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-gitlab-connection', '--defined-tags'])
        assert 'Error: Option \'--defined-tags\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-gitlab-connection', '--freeform-tags'])
        assert 'Error: Option \'--freeform-tags\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'update-gitlab-connection', '--if-match'])
        assert 'Error: Option \'--if-match\' requires an argument' in result.output

    def test_connection_delete(self):
        result = util.invoke_command(['devops', 'connection', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--connection-id' in result.output
        result = util.invoke_command(['devops', 'connection', 'delete', '--connection-id'])
        assert 'Error: Option \'--connection-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'delete', '--if-match'])
        assert 'Error: Option \'--if-match\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'delete', '--max-wait-seconds'])
        assert 'Error: Option \'--max-wait-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'delete', '--wait-interval-seconds'])
        assert 'Error: Option \'--wait-interval-seconds\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'delete', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output

    def test_connection_list(self):
        result = util.invoke_command(['devops', 'connection', 'list', '--id'])
        assert 'Error: Option \'--id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'list', '--project-id'])
        assert 'Error: Option \'--project-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'list', '--compartment-id'])
        assert 'Error: Option \'--compartment-id\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'list', '--lifecycle-state'])
        assert 'Error: Option \'--lifecycle-state\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'list', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'list', '--limit'])
        assert 'Error: Option \'--limit\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'list', '--page'])
        assert 'Error: Option \'--page\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'list', '--page-size'])
        assert 'Error: Option \'--page-size\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'list', '--sort-order'])
        assert 'Error: Option \'--sort-order\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'list', '--sort-by'])
        assert 'Error: Option \'--sort-by\' requires an argument' in result.output
        result = util.invoke_command(['devops', 'connection', 'list', '--from-json'])
        assert 'Error: Option \'--from-json\' requires an argument' in result.output
