# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/bastion/tests/unit/test_work_request_api_extended.py
class TestWorkRequestApi(unittest.TestCase):
    def setUp(self):
        pass

    def test_work_request_api_options(self):
        result = util.invoke_command(['bastion', 'work-request'])
        assert 'get' in result.output
        assert 'list' in result.output
        assert '--help' in result.output

    def test_work_request_get(self):
        result = util.invoke_command(['bastion', 'work-request', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--work-request-id' in result.output
        result = util.invoke_command(['bastion', 'work-request', 'get', '--work-request-id'])
        assert 'Error: --work-request-id option requires an argument' in result.output

    def test_work_request_list(self):
        result = util.invoke_command(['bastion', 'work-request', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        result = util.invoke_command(['bastion', 'work-request', 'list', '--compartment-id'])
        assert 'Error: --compartment-id option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'work-request', 'list', '--limit'])
        assert 'Error: --limit option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'work-request', 'list', '--page'])
        assert 'Error: --page option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'work-request', 'list', '--page-size'])
        assert 'Error: --page-size option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'work-request', 'list', '--all'])
        result = util.invoke_command(['bastion', 'work-request', 'list', '--all_pages'])
