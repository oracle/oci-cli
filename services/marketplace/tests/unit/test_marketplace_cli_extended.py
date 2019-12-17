# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from tests import util
import pytest


class TestMarketplace(unittest.TestCase):
    def setUp(self):
        pass

    def test_marketplace_package(self):
        result = util.invoke_command(
            ['marketplace', 'package', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--listing-id' in result.output
        result = util.invoke_command(
            ['marketplace', 'package', 'get'])
        assert 'Error: Missing option(s)' in result.output

    @pytest.mark.skip("Failing image tests")
    def test_marketplace_category(self):
        result = util.invoke_command(
            ['marketplace', 'category', 'list', '--help'])
        assert 'Usage: oci marketplace category list' in result.output
