# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/apigateway/tests/unit/test_apigateway_sdk_language_type_extended.py
class TestApiGatewaySdkLanguageType(unittest.TestCase):
    def setUp(self):
        pass

    def test_sdk_language_type(self):
        result = util.invoke_command(['api-gateway', 'sdk-language-type'])
        assert 'Commands:' in result.output
        assert 'list' in result.output

    def test_sdk_language_type_list(self):
        result = util.invoke_command(['api-gateway', 'sdk-language-type', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        result = util.invoke_command(['api-gateway', 'sdk-language-type', 'list', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
