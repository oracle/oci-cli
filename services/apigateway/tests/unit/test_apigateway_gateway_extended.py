# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/apigateway/tests/unit/test_apigateway_gateway_extended.py
class TestApiGatewayDeployment(unittest.TestCase):
    def setUp(self):
        pass

    def test_gateway(self):
        result = util.invoke_command(['api-gateway', 'gateway'])
        assert 'create' in result.output
        assert 'delete' in result.output
        assert 'update' in result.output
        assert 'list' in result.output

    def test_create_gateway(self):
        result = util.invoke_command(['api-gateway', 'gateway', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        assert '--endpoint-type' in result.output
        assert '--subnet-id' in result.output

    def test_update_gateway(self):
        result = util.invoke_command(['api-gateway', 'gateway', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--gateway-id' in result.output
        result = util.invoke_command(['api-gateway', 'gateway', 'update', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output

    def test_delete_gateway(self):
        result = util.invoke_command(['api-gateway', 'gateway', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--gateway-id' in result.output

    def test_list_gateway(self):
        result = util.invoke_command(['api-gateway', 'gateway', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        result = util.invoke_command(['api-gateway', 'gateway', 'list', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output

    def test_change_compartment(self):
        result = util.invoke_command(['api-gateway', 'gateway', 'change-compartment'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        assert '--gateway-id' in result.output
