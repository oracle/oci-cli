# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from tests import util


class TestNodePoolCreateUpdate(unittest.TestCase):
    def setUp(self):
        pass

    def test_nodepool_create(self):
        result = util.invoke_command(['ce', 'node-pool', 'create', '--size', '1', '--placement-configs', 'config'])
        assert 'Error: Missing option(s)' in result.output

    def test_nodepool_update(self):
        result = util.invoke_command(['ce', 'node-pool', 'update', '--size', '1', '--placement-configs', 'config'])
        assert 'Error: Missing option(s) --node-pool-id.' in result.output
