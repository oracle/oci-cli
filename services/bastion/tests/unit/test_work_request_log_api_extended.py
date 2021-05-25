# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/bastion/tests/unit/test_work_request_log_api_extended.py
class TestWorkRequestLogApi(unittest.TestCase):
    def setUp(self):
        pass

    def test_work_request_error_api_options(self):
        result = util.invoke_command(['bastion', 'work-request-log-entry'])
        assert 'list' in result.output
        assert '--help' in result.output

    def test_work_request_error_list(self):
        result = util.invoke_command(['bastion', 'work-request-log-entry', 'list-work-request-logs'])
        assert 'Error: Missing option(s)' in result.output
        assert '--work-request-id' in result.output
        result = util.invoke_command(['bastion', 'work-request-log-entry', 'list-work-request-logs', '--work-request-id'])
        assert 'Error: --work-request-id option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'work-request-log-entry', 'list-work-request-logs', '--limit'])
        assert 'Error: --limit option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'work-request-log-entry', 'list-work-request-logs', '--page'])
        assert 'Error: --page option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'work-request-log-entry', 'list-work-request-logs', '--page-size'])
        assert 'Error: --page-size option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'work-request-log-entry', 'list-work-request-logs', '--all'])
        result = util.invoke_command(['bastion', 'work-request-log-entry', 'list-work-request-logs', '--all_pages'])
