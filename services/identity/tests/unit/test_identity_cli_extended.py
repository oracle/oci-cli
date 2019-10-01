# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from tests import util


class TestIdentityCLI(unittest.TestCase):
    def setUp(self):
        pass

    def test_dex_6794_commands_removed(self):
        result = util.invoke_command(['iam', 'tag', 'create-tag-default-tag-definition-validator'])
        assert 'No such command' in result.output
        result = util.invoke_command(['iam', 'tag', 'create-tag-enum-tag-definition-validator'])
        assert 'No such command' in result.output
        result = util.invoke_command(['iam', 'tag', 'update-tag-default-tag-definition-validator'])
        assert 'No such command' in result.output
        result = util.invoke_command(['iam', 'tag', 'update-tag-enum-tag-definition-validator'])
        assert 'No such command' in result.output
