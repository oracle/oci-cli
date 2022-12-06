# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestChannelsCliExtend(unittest.TestCase):
    def setUp(self):
        pass

    # test removed commands
    def test_removed_commands(self):
        # oci mysql channels channel -> oci mysql channel
        result = util.invoke_command(['mysql', 'channels'])
        assert 'No such command' in result.output
        result = util.invoke_command(['mysql', 'channel'])
        assert 'Usage: oci mysql channel [OPTIONS] COMMAND [ARGS]' in result.output

        # removed create
        result = util.invoke_command(['mysql', 'channel', 'create'])
        assert 'No such command' in result.output

        # removed create-channel-create-channel-target-from-db-system-details
        result = util.invoke_command(['mysql', 'channel', 'create-channel-create-channel-target-from-db-system-details'])
        assert 'No such command' in result.output

        # removed update
        result = util.invoke_command(['mysql', 'channel', 'update'])
        assert 'No such command' in result.output

        # removed update-channel-update-channel-target-from-db-system-details
        result = util.invoke_command(['mysql', 'channel', 'update-channel-update-channel-target-from-db-system-details'])
        assert 'No such command' in result.output

    # test command override create-channel-create-channel-source-from-mysql-details -> oci mysql channel create-from-mysql
    def test_create_from_mysql_required_params(self):
        # test required parameters
        result = util.invoke_command(['mysql', 'channel', 'create-from-mysql'])
        assert 'Error: Missing option(s)' in result.output
        assert 'source-hostname' in result.output
        assert 'source-username' in result.output
        assert 'source-password' in result.output
        assert 'source-ssl-mode' in result.output
        assert 'target-db-system-id' in result.output

        result = util.invoke_command(['mysql', 'channel', 'create-from-mysql',
                                      '--source-hostname', 'dummy',
                                      '--source-username', 'dummy',
                                      '--source-password', 'dummy',
                                      '--source-ssl-mode', 'dummy',
                                      '--target-db-system-id', 'dummy'])

        assert 'Error: Missing option(s)' not in result.output

    def test_create_from_mysql_target_params(self):
        # Test that '--target' param no longer exists
        result = util.invoke_command(['mysql', 'channel', 'create-from-mysql',
                                      '--source-hostname', 'dummy',
                                      '--source-username', 'dummy',
                                      '--source-password', 'dummy',
                                      '--source-ssl-mode', 'dummy',
                                      '--target-db-system-id', 'dummy',
                                      '--target', 'dummy'])
        assert 'Error: no such option: --target  (Possible options:' in result.output

        # test all flattened target parameters
        result = util.invoke_command(['mysql', 'channel', 'create-from-mysql',
                                      '--source-hostname', 'dummy',
                                      '--source-username', 'dummy',
                                      '--source-password', 'dummy',
                                      '--source-ssl-mode', 'dummy',
                                      '--target-db-system-id', 'dummy',
                                      '--target-channel-name', 'dummy',
                                      '--target-applier-username', 'dummy',
                                      '--target-filters', '[]'])
        assert 'Error: Missing option(s)' not in result.output

    # test command override channel update_channel_update_channel_source_from_mysql_details -> oci mysql channel update-from-mysql
    def test_update_from_mysql_params(self):
        # test only --channel-id is required
        result = util.invoke_command(['mysql', 'channel', 'update-from-mysql'])
        assert 'Error: Missing option(s)' in result.output
        assert 'channel-id' in result.output

        result = util.invoke_command(['mysql', 'channel', 'update-from-mysql', '--channel-id', 'dummy'])
        assert 'Error: Missing option(s)' not in result.output

        # test --target-db-system-id is not allowed
        result = util.invoke_command(['mysql', 'channel', 'update-from-mysql', '--target-db-system-id', 'dummy'])
        assert 'Error: no such option: --target-db-system-id' in result.output

        # test flattened target parameters
        result = util.invoke_command(['mysql', 'channel', 'update-from-mysql',
                                      '--channel-id', 'dummy',
                                      '--target-applier-username', 'dummy',
                                      '--target-channel-name', 'dummy',
                                      '--target-filters', '[]'])
        assert 'Error: Missing option(s)' not in result.output

    # test override of WARNING message in update-from-mysql
    def test_update_warning_message(self):
        # test freeform-tags warning
        result = util.invoke_command(['mysql', 'channel', 'update-from-mysql', '--channel-id', 'dummy', '--freeform-tags', 'dummy'])
        assert 'WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue? [y/N]' in result.output

        # test defined-tags warning
        result = util.invoke_command(['mysql', 'channel', 'update-from-mysql', '--channel-id', 'dummy', '--defined-tags', 'dummy'])
        assert 'WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue? [y/N]' in result.output

        # test freeform-tags with --force
        result = util.invoke_command(['mysql', 'channel', 'update-from-mysql', '--channel-id', 'dummy', '--freeform-tags', 'dummy', '--force'])
        assert 'WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue? [y/N]' not in result.output

        # test defined-tags warning with --force
        result = util.invoke_command(['mysql', 'channel', 'update-from-mysql', '--channel-id', 'dummy', '--defined-tags', 'dummy', '--force'])
        assert 'WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue? [y/N]' not in result.output
