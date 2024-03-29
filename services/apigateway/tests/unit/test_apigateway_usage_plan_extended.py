# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/apigateway/tests/unit/test_apigateway_usage_plan_extended.py
class TestApiGatewayUsagePlan(unittest.TestCase):
    def setUp(self):
        pass

    def test_usage_plan(self):
        result = util.invoke_command(['api-gateway', 'usage-plan'])
        assert 'create' in result.output
        assert 'delete' in result.output
        assert 'update' in result.output
        assert 'list' in result.output

    def test_create_usage_plan(self):
        result = util.invoke_command(['api-gateway', 'usage-plan', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        assert '--entitlements' in result.output

    def test_update_usage_plan(self):
        result = util.invoke_command(['api-gateway', 'usage-plan', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--usage-plan-id' in result.output
        result = util.invoke_command(['api-gateway', 'usage-plan', 'update', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'usage-plan', 'update', '--entitlements'])
        assert 'Error: Option \'--entitlements\' requires an argument' in result.output

    def test_delete_usage_plan(self):
        result = util.invoke_command(['api-gateway', 'usage-plan', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--usage-plan-id' in result.output

    def test_list_usage_plan(self):
        result = util.invoke_command(['api-gateway', 'usage-plan', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        result = util.invoke_command(['api-gateway', 'usage-plan', 'list', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output

    def test_change_compartment(self):
        result = util.invoke_command(['api-gateway', 'usage-plan', 'change-compartment'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        assert '--usage-plan-id' in result.output
