# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/apigateway/tests/unit/test_apigateway_subscriber_extended.py
class TestApiGatewaySubscriber(unittest.TestCase):
    def setUp(self):
        pass

    def test_subscriber(self):
        result = util.invoke_command(['api-gateway', 'subscriber'])
        assert 'create' in result.output
        assert 'delete' in result.output
        assert 'update' in result.output
        assert 'list' in result.output

    def test_create_subscriber(self):
        result = util.invoke_command(['api-gateway', 'subscriber', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        assert '--clients' in result.output
        assert '--usage-plans' in result.output

    def test_update_subscriber(self):
        result = util.invoke_command(['api-gateway', 'subscriber', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--subscriber-id' in result.output
        result = util.invoke_command(['api-gateway', 'subscriber', 'update', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'subscriber', 'update', '--clients'])
        assert 'Error: --clients option requires an argument' in result.output
        result = util.invoke_command(['api-gateway', 'subscriber', 'update', '--usage-plans'])
        assert 'Error: --usage-plans option requires an argument' in result.output

    def test_delete_subscriber(self):
        result = util.invoke_command(['api-gateway', 'subscriber', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--subscriber-id' in result.output

    def test_list_subscriber(self):
        result = util.invoke_command(['api-gateway', 'subscriber', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        result = util.invoke_command(['api-gateway', 'subscriber', 'list', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output

    def test_change_compartment(self):
        result = util.invoke_command(['api-gateway', 'subscriber', 'change-compartment'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        assert '--subscriber-id' in result.output
