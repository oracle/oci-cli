# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from tests import util


class TestLoadBalancer(unittest.TestCase):
    def setUp(self):
        pass

    def test_nsg_id_options(self):

        result = util.invoke_command(['lb', 'nsg', 'update', '--network-security-group-ids'])
        assert 'Error: no such option:' in result.output
        assert 'network-security-group-ids' in result.output

        result = util.invoke_command(['lb', 'nsg', 'update', '--nsg-ids', 'dummy', '--force'])
        assert 'Error: Missing option(s)' in result.output
        assert 'load-balancer-id' in result.output

        result = util.invoke_command(['lb', 'load-balancer', 'create', '--network-security-group-ids'])
        assert 'Error: no such option:' in result.output
        assert 'network-security-group-ids' in result.output

        result = util.invoke_command(['lb', 'load-balancer', 'create', '--nsg-ids', 'dummy'])
        assert 'Error: Missing option(s)' in result.output
        assert 'compartment-id' in result.output
        assert 'display-name' in result.output
        assert 'shape-name' in result.output
        assert 'subnet-ids' in result.output

    def test_connection_config_support(self):
        result = util.invoke_command(
            ['lb', 'listener', 'create', '--connection-configuration-backend-tcp-proxy-protocol-version', '1',
             '--connection-configuration-idle-timeout', '1'])
        assert 'Error: Missing option(s)' in result.output
        assert 'default-backend-set-name' in result.output
        assert 'port' in result.output
        assert 'protocol' in result.output
        assert 'load-balancer-id' in result.output
        assert 'name' in result.output

        result = util.invoke_command(
            ['lb', 'listener', 'update', '--connection-configuration-backend-tcp-proxy-protocol-version', '1',
             '--connection-configuration-idle-timeout', '1'])
        assert 'Error: Missing option(s)' in result.output
        assert 'default-backend-set-name' in result.output
        assert 'port' in result.output
        assert 'protocol' in result.output
        assert 'load-balancer-id' in result.output
        assert 'listener-name' in result.output
