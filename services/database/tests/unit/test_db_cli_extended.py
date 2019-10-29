# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from tests import util


class TestDBCliExtended(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_wallet(self):
        result = util.invoke_command(['db', 'autonomous-database-wallet'])
        assert 'get-regional-wallet-metadata' in result.output
        assert 'get-autonomous-database-regional-wallet' not in result.output

    def test_get_regional_wallet(self):
        result = util.invoke_command(['db', 'autonomous-database-wallet'])
        assert 'rotate' in result.output
        assert 'update' not in result.output
        result = util.invoke_command(['db', 'autonomous-database-wallet', 'rotate'])
        assert 'Error: Missing option(s) --id' in result.output
        assert '--autonomous-database-id' not in result.output

    def test_update_wallet(self):
        result = util.invoke_command(['db', 'autonomous-database-wallet'])
        assert 'rotate' in result.output
        assert 'update' not in result.output
        result = util.invoke_command(['db', 'autonomous-database-wallet', 'rotate'])
        assert 'Error: Missing option(s) --id' in result.output
        assert '--autonomous-database-id' not in result.output

    def test_update_regional_wallet(self):
        result = util.invoke_command(['db', 'autonomous-database-wallet'])
        assert 'rotate-regional-wallet' in result.output
        assert 'update-autonomous-database-regional-wallet' not in result.output
