# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/apigateway/tests/unit/test_apigateway_api_extended.py
class TestApiGatewayApi(unittest.TestCase):
    def setUp(self):
        pass

    def test_api(self):
        result = util.invoke_command(['api-gateway', 'api'])
        assert 'Commands:' in result.output
        assert 'create' in result.output
        assert 'update' in result.output
        assert 'delete' in result.output
        assert 'list' in result.output
        assert 'get' in result.output
        assert 'change-compartment' in result.output
        assert 'content' in result.output
        assert 'deployment-specification' in result.output
        assert 'validations' in result.output

    def test_api_create(self):
        result = util.invoke_command(['api-gateway', 'api', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'create', '--compartment-id'])
        assert 'Error: --compartment-id option requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'create', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'create', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'create', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'create', '--content'])
        assert 'Error: --content option requires an argument' in result.output

    def test_api_update(self):
        result = util.invoke_command(['api-gateway', 'api', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--api-id' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'update', '--api-id'])
        assert 'Error: --api-id option requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'update', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'update', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'update', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'update', '--content'])
        assert 'Error: --content option requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'update', '--if-match'])
        assert 'Error: --if-match option requires an argument' in result.output

    def test_api_delete(self):
        result = util.invoke_command(['api-gateway', 'api', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--api-id' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'delete', '--api-id'])
        assert 'Error: --api-id option requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'delete', '--if-match'])
        assert 'Error: --if-match option requires an argument' in result.output

    def test_api_list(self):
        result = util.invoke_command(['api-gateway', 'api', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'list', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output

    def test_api_get(self):
        result = util.invoke_command(['api-gateway', 'api', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--api-id' in result.output

    def test_api_change_compartment(self):
        result = util.invoke_command(['api-gateway', 'api', 'change-compartment'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        assert '--api-id' in result.output

    def test_api_content(self):
        result = util.invoke_command(['api-gateway', 'api', 'content'])
        assert 'Commands:' in result.output
        assert 'get' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'content', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--api-id' in result.output
        assert '--file' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'content', 'get', '--if-match'])
        assert 'Error: --if-match option requires an argument' in result.output

    def test_api_deployment_specification(self):
        result = util.invoke_command(['api-gateway', 'api', 'deployment-specification'])
        assert 'Commands:' in result.output
        assert 'get' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'deployment-specification', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--api-id' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'deployment-specification', 'get', '--if-match'])
        assert 'Error: --if-match option requires an argument' in result.output

    def test_api_validations(self):
        result = util.invoke_command(['api-gateway', 'api', 'validations'])
        assert 'Commands:' in result.output
        assert 'get' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'validations', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--api-id' in result.output
        result = util.invoke_command(['api-gateway', 'api', 'validations', 'get', '--if-match'])
        assert 'Error: --if-match option requires an argument' in result.output
