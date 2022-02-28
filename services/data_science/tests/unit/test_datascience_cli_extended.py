# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import re
import unittest
from tests import util


class TestDatascienceCLI(unittest.TestCase):
    def setUp(self):
        pass

    def test_list_work_request_logs(self):
        result = util.invoke_command(['data-science', 'work-request'])
        assert 'list-work-request-logs' in result.output
        result = util.invoke_command(['data-science', 'work-request', 'list-work-request-logs'])
        assert 'Error: Missing option(s)' in result.output

    def test_create_notebook_session(self):
        result = util.invoke_command(['data-science', 'notebook-session', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--project-id' in result.output
        assert '--compartment-id' in result.output

    def test_get_model_artifact_content(self):
        result = util.invoke_command(['data-science', 'model'])
        assert 'get-model-artifact-content' not in result.output

    def test_get_artifact_content(self):
        result = util.invoke_command(['data-science', 'model'])
        assert 'get-artifact-content' in result.output
        result = util.invoke_command(['data-science', 'model', 'get-artifact-content'])
        assert 'Error: Missing option(s)' in result.output
        assert '--file' in result.output
        assert '--model-id' in result.output

    def test_create_model_artifact_model_artifact(self):
        result = util.invoke_command(['data-science', 'model', 'create-model-artifact'])
        tokens = re.split('[ .]', result.output)
        assert '--model-artifact' not in tokens

    def test_create_model_artifact_model_artifact_file(self):
        result = util.invoke_command(['data-science', 'model', 'create-model-artifact'])
        tokens = re.split('[ .]', result.output)
        assert '--model-artifact-file' in tokens

    def test_create_job_artifact_job_artifact(self):
        result = util.invoke_command(['data-science', 'job', 'create-job-artifact'])
        tokens = re.split('[ .]', result.output)
        assert '--job-artifact' not in tokens

    def test_create_job_artifact_job_artifact_file(self):
        result = util.invoke_command(['data-science', 'job', 'create-job-artifact'])
        tokens = re.split('[ .]', result.output)
        assert '--job-artifact-file' in tokens
