# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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
