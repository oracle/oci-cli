# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestWaas(unittest.TestCase):
    def setUp(self):
        pass

    def test_update_setting_option(self):

        result = util.invoke_command(['waas', 'custom-protection-rule', 'update-setting', '--update-custom-protection-rules-details'])
        assert 'Error: no such option:' in result.output
        assert 'update-custom-protection-rules-details' in result.output

        result = util.invoke_command(['waas', 'custom-protection-rule', 'update-setting', '--custom-protection-rules-details', '{}'])
        assert 'Error: Missing option(s)' in result.output
        assert 'waas-policy-id' in result.output

    def test_update_address_list(self):
        result = util.invoke_command(['waas', 'certificate', 'update-address-list'])
        assert 'Error: Missing option(s)' in result.output

    def test_caching_rules_group(self):
        result = util.invoke_command(['waas', 'caching-rule'])
        assert 'Options:' in result.output

    def test_list_waas_policy(self):
        result = util.invoke_command(['waas', 'waas-policy', 'custom-protection-rule'])
        assert 'list' in result.output

    def test_update_policy_config(self):
        result = util.invoke_command(['waas', 'policy-config', 'update', '--tls-protocols', 'TLS_V1_3', '--tls-protocols', 'TLS_V1_2'])
        assert 'Missing option(s)' in result.output
        assert 'waas-policy-id' in result.output

        result = util.invoke_command(['waas', 'policy-config', 'update', '--load-balancing-method'])
        assert 'option requires an argument' in result.output

        result = util.invoke_command(['waas', 'policy-config', 'update', '--websocket-path-prefixes'])
        assert 'option requires an argument' in result.output

        result = util.invoke_command(['waas', 'policy-config', 'update', '--health-checks'])
        assert 'option requires an argument' in result.output

        result = util.invoke_command(
            ['waas', 'policy-config', 'update', '--waas-policy-id', 'dummy', '--tls-protocols', 'TLS_V1_3'])
        assert 'Updates to tls-protocols, load-balancing-method, websocket-path-prefixes and health-checks will replace any existing values.' in result.output

        result = util.invoke_command(
            ['waas', 'policy-config', 'update', '--waas-policy-id', 'dummy', '--load-balancing-method', 'dummy'])
        assert 'Updates to tls-protocols, load-balancing-method, websocket-path-prefixes and health-checks will replace any existing values.' in result.output

        result = util.invoke_command(
            ['waas', 'policy-config', 'update', '--waas-policy-id', 'dummy', '--websocket-path-prefixes', 'dummy'])
        assert 'Updates to tls-protocols, load-balancing-method, websocket-path-prefixes and health-checks will replace any existing values.' in result.output

        result = util.invoke_command(
            ['waas', 'policy-config', 'update', '--waas-policy-id', 'dummy', '--health-checks', 'dummy'])
        assert 'Updates to tls-protocols, load-balancing-method, websocket-path-prefixes and health-checks will replace any existing values.' in result.output
