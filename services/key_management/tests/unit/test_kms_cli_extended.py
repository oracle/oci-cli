# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from tests import util


class TestBatch(unittest.TestCase):
    def setUp(self):
        pass

    def test_kms(self):
        result = util.invoke_command(['kms'])
        assert 'crypto' in result.output
        assert 'management' in result.output

    def test_kms_management(self):
        result = util.invoke_command(['kms', 'management'])
        assert 'key' in result.output
        assert 'key-version' in result.output
        assert 'vault' in result.output

    def test_kms_management_key(self):
        result = util.invoke_command(['kms', 'management', 'key'])
        assert 'cancel-deletion' in result.output
        assert 'create' in result.output
        assert 'disable' in result.output
        assert 'enable' in result.output
        assert 'get' in result.output
        assert 'list' in result.output
        assert 'schedule-deletion' in result.output
        assert 'update' in result.output

    def test_kms_management_key_schedule_deletion(self):
        result = util.invoke_command(['kms', 'management', 'key', 'schedule-deletion'])
        assert 'Error: Missing option(s)' in result.output
        assert 'key-id' in result.output
        result = util.invoke_command(['kms', 'management', 'key', 'schedule-deletion', '--time-of-deletion'])
        assert 'Error: --time-of-deletion option requires an argument' in result.output

    def test_kms_management_key_cancel_deletion(self):
        result = util.invoke_command(['kms', 'management', 'key', 'cancel-deletion'])
        assert 'Error: Missing option(s)' in result.output
        assert 'key-id' in result.output

    def test_kms_management_key_version_cancel_deletion(self):
        result = util.invoke_command(['kms', 'management', 'key-version', 'cancel-deletion'])
        assert 'Error: Missing option(s)' in result.output
        assert 'key-id' in result.output

    def test_kms_management_key_version_schedule_deletion(self):
        result = util.invoke_command(['kms', 'management', 'key-version', 'schedule-deletion'])
        assert 'Error: Missing option(s)' in result.output
        assert 'key-id' in result.output
        result = util.invoke_command(['kms', 'management', 'key-version', 'schedule-deletion', '--time-of-deletion'])
        assert 'Error: --time-of-deletion option requires an argument' in result.output

    def test_kms_vault_usage_get(self):
        result = util.invoke_command(['kms', 'management', 'vault-usage'])
        assert 'Error: No such command "vault-usage"' in result.output
        result = util.invoke_command(['kms', 'management', 'vault', 'usage'])
        assert 'Usage: oci kms management vault usage' in result.output
        result = util.invoke_command(['kms', 'management', 'vault', 'usage', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert 'vault-id' in result.output
