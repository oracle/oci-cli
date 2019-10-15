# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from tests import util


class TestDatabase(unittest.TestCase):
    def setUp(self):
        pass

    def test_update_database(self):
        result = util.invoke_command(['db', 'database', 'update', '--backup-destination'])
        assert 'backup-destination' in result.output
        result = util.invoke_command(['db', 'database', 'update', '--backup-destination', 'dummy'])
        assert 'Error: Missing option(s)' in result.output
        assert 'database-id' in result.output
