# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from tests import util


class TestNetwork(unittest.TestCase):
    def setUp(self):
        pass

    def test_nsg_id_options(self):
        result = util.invoke_command(['network', 'nsg', 'delete', '--network-security-group-id'])
        assert 'Error: no such option:' in result.output
        assert 'network-security-group-id' in result.output

        result = util.invoke_command(['network', 'nsg', 'delete', '--nsg-id', 'dummy', '--force'])
        assert 'ServiceError' in result.output

        result = util.invoke_command(['network', 'nsg', 'get', '--network-security-group-id'])
        assert 'Error: no such option:' in result.output
        assert 'network-security-group-id' in result.output

        result = util.invoke_command(['network', 'nsg', 'get', '--nsg-id', 'dummy'])
        assert 'ServiceError' in result.output

        result = util.invoke_command(['network', 'nsg', 'rules', 'add', '--network-security-group-id'])
        assert 'Error: no such option:' in result.output
        assert 'network-security-group-id' in result.output

        result = util.invoke_command(['network', 'nsg', 'rules', 'add', '--nsg-id', 'dummy'])
        assert 'ServiceError' in result.output

        result = util.invoke_command(['network', 'nsg', 'rules', 'list', '--network-security-group-id'])
        assert 'Error: no such option:' in result.output
        assert 'network-security-group-id' in result.output

        result = util.invoke_command(['network', 'nsg', 'rules', 'list', '--nsg-id', 'dummy'])
        assert 'ServiceError' in result.output

        result = util.invoke_command(['network', 'nsg', 'rules', 'remove', '--network-security-group-id'])
        assert 'Error: no such option:' in result.output
        assert 'network-security-group-id' in result.output

        result = util.invoke_command(['network', 'nsg', 'rules', 'remove', '--nsg-id', 'dummy'])
        assert 'ServiceError' in result.output

        result = util.invoke_command(['network', 'nsg', 'rules', 'update', '--network-security-group-id'])
        assert 'Error: no such option:' in result.output
        assert 'network-security-group-id' in result.output

        result = util.invoke_command(['network', 'nsg', 'rules', 'update', '--nsg-id', 'dummy'])
        assert 'ServiceError' in result.output

        result = util.invoke_command(['network', 'nsg', 'vnics', 'list', '--network-security-group-id'])
        assert 'Error: no such option:' in result.output
        assert 'network-security-group-id' in result.output

        result = util.invoke_command(['network', 'nsg', 'vnics', 'list', '--nsg-id', 'dummy'])
        assert 'ServiceError' in result.output
