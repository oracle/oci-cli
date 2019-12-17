# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from tests import util


# pytest -s services/apigateway/tests/unit/test_apigateway_work_request_extended.py
class TestApiGatewayWorkRequest(unittest.TestCase):
    def setUp(self):
        pass

    def test_work_request(self):
        result = util.invoke_command(['api-gateway', 'work-request'])
        assert 'get' in result.output
        assert 'list' in result.output

    def test_work_request_log(self):
        result = util.invoke_command(['api-gateway', 'work-request-log'])
        assert 'list' in result.output

    def test_work_request_error(self):
        result = util.invoke_command(['api-gateway', 'work-request-error'])
        assert 'list' in result.output

    def test_get_work_request(self):
        result = util.invoke_command(['api-gateway', 'work-request', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--work-request-id' in result.output

    def test_list_work_request(self):
        result = util.invoke_command(['api-gateway', 'work-request', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output

    def test_list_work_request_log(self):
        result = util.invoke_command(['api-gateway', 'work-request-log', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--work-request-id' in result.output

    def test_list_work_request_error(self):
        result = util.invoke_command(['api-gateway', 'work-request-error', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--work-request-id' in result.output
