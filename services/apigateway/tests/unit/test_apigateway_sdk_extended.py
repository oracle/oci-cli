# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/apigateway/tests/unit/test_apigateway_api_extended.py
class TestApiGatewaySdk(unittest.TestCase):
    def setUp(self):
        pass

    def test_api(self):
        result = util.invoke_command(['api-gateway', 'sdk'])
        assert 'Commands:' in result.output
        assert 'create' in result.output
        assert 'update' in result.output
        assert 'delete' in result.output
        assert 'list' in result.output
        assert 'get' in result.output

    def test_sdk_create(self):
        result = util.invoke_command(['api-gateway', 'sdk', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--target-language' in result.output
        assert '--api-id' in result.output
        result = util.invoke_command(['api-gateway', 'sdk', 'create', '--target-language'])
        assert 'Error: Option \'--target-language\' requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'sdk', 'create', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'sdk', 'create', '--defined-tags'])
        assert 'Error: Option \'--defined-tags\' requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'sdk', 'create', '--freeform-tags'])
        assert 'Error: Option \'--freeform-tags\' requires an argument' in result.output

    def test_sdk_update(self):
        result = util.invoke_command(['api-gateway', 'sdk', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--sdk-id' in result.output
        result = util.invoke_command(['api-gateway', 'sdk', 'update', '--sdk-id'])
        assert 'Error: Option \'--sdk-id\' requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'sdk', 'update', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'sdk', 'update', '--defined-tags'])
        assert 'Error: Option \'--defined-tags\' requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'sdk', 'update', '--freeform-tags'])
        assert 'Error: Option \'--freeform-tags\' requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'sdk', 'update', '--if-match'])
        assert 'Error: Option \'--if-match\' requires an argument' in result.output

    def test_sdk_delete(self):
        result = util.invoke_command(['api-gateway', 'sdk', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--sdk-id' in result.output
        result = util.invoke_command(['api-gateway', 'sdk', 'delete', '--sdk-id'])
        assert 'Error: Option \'--sdk-id\' requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'sdk', 'delete', '--if-match'])
        assert 'Error: Option \'--if-match\' requires an argument' in result.output

    def test_sdk_list(self):
        result = util.invoke_command(['api-gateway', 'sdk', 'list', '--display-name'])
        assert 'Error: Option \'--display-name\' requires an argument' in result.output

    def test_sdk_get(self):
        result = util.invoke_command(['api-gateway', 'sdk', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--sdk-id' in result.output
