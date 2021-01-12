# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
