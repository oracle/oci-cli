# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/apigateway/tests/unit/test_apigateway_deployment_extended.py
class TestApiGatewayDeployment(unittest.TestCase):
    def setUp(self):
        pass

    def test_deployment(self):
        result = util.invoke_command(['api-gateway', 'deployment'])
        assert 'create' in result.output
        assert 'delete' in result.output
        assert 'update' in result.output
        assert 'list' in result.output

    def test_create_deployment(self):
        result = util.invoke_command(['api-gateway', 'deployment', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--gateway-id' in result.output
        assert '--compartment-id' in result.output
        assert '--path-prefix' in result.output

    def test_update_deployment(self):
        result = util.invoke_command(['api-gateway', 'deployment', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--deployment-id' in result.output
        result = util.invoke_command(['api-gateway', 'deployment', 'update', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'deployment', 'update', '--specification'])
        assert 'Error: --specification option requires an argument' in result.output

    def test_delete_deployment(self):
        result = util.invoke_command(['api-gateway', 'deployment', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--deployment-id' in result.output

    def test_list_deployment(self):
        result = util.invoke_command(['api-gateway', 'deployment', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        result = util.invoke_command(['api-gateway', 'deployment', 'list', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'deployment', 'list', '--gateway-id'])
        assert 'Error: --gateway-id option requires an argument' in result.output

    def test_change_compartment(self):
        result = util.invoke_command(['api-gateway', 'deployment', 'change-compartment'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        assert '--deployment-id' in result.output
