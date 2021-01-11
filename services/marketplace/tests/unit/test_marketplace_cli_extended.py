# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
