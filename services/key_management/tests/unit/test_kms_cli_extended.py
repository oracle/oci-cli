# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestKMS(unittest.TestCase):
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
        assert 'backup' in result.output
        assert 'cancel-deletion' in result.output
        assert 'create' in result.output
        assert 'disable' in result.output
        assert 'enable' in result.output
        assert 'get' in result.output
        assert 'import' in result.output
        assert 'list' in result.output
        assert 'restore' in result.output
        assert 'restore-from-file' in result.output
        assert 'schedule-deletion' in result.output
        assert 'update' in result.output

    def test_kms_management_vault(self):
        result = util.invoke_command(['kms', 'management', 'vault'])
        assert 'backup' in result.output
        assert 'cancel-deletion' in result.output
        assert 'change-compartment' in result.output
        assert 'create' in result.output
        assert 'get' in result.output
        assert 'list' in result.output
        assert 'restore' in result.output
        assert 'restore-from-file' in result.output
        assert 'schedule-deletion' in result.output
        assert 'update' in result.output
        assert 'usage' in result.output

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
        assert "Error: No such command 'vault-usage'" in result.output
        result = util.invoke_command(['kms', 'management', 'vault', 'usage'])
        assert 'Usage: oci kms management vault usage' in result.output
        result = util.invoke_command(['kms', 'management', 'vault', 'usage', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert 'vault-id' in result.output

    def test_kms_key_backup(self):
        result = util.invoke_command(['kms', 'management', 'key', 'backup'])
        assert 'Error: Missing option(s)' in result.output
        assert 'key-id' in result.output
        result = util.invoke_command(['kms', 'management', 'key', 'backup', '--key-id', 'dummy'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output
        result = util.invoke_command(['kms', 'management', 'key', 'backup', '--key-id', 'dummy', '--bucket-name', 'dummy'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output
        result = util.invoke_command(
            ['kms', 'management', 'key', 'backup', '--key-id', 'dummy', '--namespace', 'dummy'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output
        result = util.invoke_command(
            ['kms', 'management', 'key', 'backup', '--key-id', 'dummy', '--namespace', 'dummy', '--bucket-name', 'dummy'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output

    def test_kms_key_restore(self):
        result = util.invoke_command(['kms', 'management', 'key', 'restore'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output
        result = util.invoke_command(
            ['kms', 'management', 'key', 'restore', '--bucket-name', 'dummy'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output
        result = util.invoke_command(
            ['kms', 'management', 'key', 'restore', '--namespace', 'dummy'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output
        result = util.invoke_command(
            ['kms', 'management', 'key', 'restore', '--namespace', 'dummy', '--bucket-name', 'dummy'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output

    def test_kms_key_restore_from_file(self):
        result = util.invoke_command(['kms', 'management', 'key', 'restore-from-file'])
        assert 'Error: Missing option(s)' in result.output
        assert 'restore-key-from-file-location' in result.output

    def test_kms_vault_backup(self):
        result = util.invoke_command(['kms', 'management', 'vault', 'backup'])
        assert 'Error: Missing option(s)' in result.output
        assert 'vault-id' in result.output
        result = util.invoke_command(['kms', 'management', 'vault', 'backup', '--vault-id', 'dummy'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output
        result = util.invoke_command(['kms', 'management', 'vault', 'backup', '--vault-id', 'dummy', '--bucket-name', 'dummy'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output
        result = util.invoke_command(
            ['kms', 'management', 'vault', 'backup', '--vault-id', 'dummy', '--namespace', 'dummy'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output
        result = util.invoke_command(
            ['kms', 'management', 'vault', 'backup', '--vault-id', 'dummy', '--namespace', 'dummy', '--bucket-name', 'dummy'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output

    def test_kms_vault_restore(self):
        result = util.invoke_command(['kms', 'management', 'vault', 'restore'])
        assert 'Error: Missing option(s)' in result.output
        assert 'compartment-id' in result.output
        result = util.invoke_command(['kms', 'management', 'vault', 'restore', '--compartment-id', 'dummy'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output
        result = util.invoke_command(
            ['kms', 'management', 'vault', 'restore', '--compartment-id', 'dummy', '--bucket-name', 'dummy'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output
        result = util.invoke_command(
            ['kms', 'management', 'vault', 'restore', '--compartment-id', 'dummy', '--namespace', 'dummy'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output
        result = util.invoke_command(
            ['kms', 'management', 'vault', 'restore', '--compartment-id', 'dummy', '--namespace', 'dummy', '--bucket-name', 'dummy'])
        assert 'UsageError: either --uri or all of (--bucket-name, --object-name and --namespace) must be provided' in result.output

    def test_kms_vault_restore_from_file(self):
        result = util.invoke_command(['kms', 'management', 'vault', 'restore-from-file'])
        assert 'Error: Missing option(s)' in result.output
        assert 'compartment-id' in result.output
        assert 'restore-vault-from-file-location' in result.output
