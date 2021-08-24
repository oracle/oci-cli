# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/functions/tests/unit/test_functions_extended.py
class TestFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_fn(self):
        result = util.invoke_command(['fn'])
        assert 'application' in result.output
        assert 'function' in result.output

    def test_fn_application(self):
        result = util.invoke_command(['fn', 'application'])
        assert 'create' in result.output
        assert 'delete' in result.output
        assert 'update' in result.output
        assert 'list' in result.output
        assert 'get' in result.output
        assert 'change-compartment' in result.output

    def test_application_create(self):
        result = util.invoke_command(['fn', 'application', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--display-name' in result.output
        assert '--compartment-id' in result.output
        assert '--subnet-ids' in result.output
        result = util.invoke_command(['fn', 'application', 'create', '--config'])
        assert 'Error: --config option requires an argument' in result.output

    def test_application_delete(self):
        result = util.invoke_command(['fn', 'application', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--application-id' in result.output

    def test_application_update(self):
        result = util.invoke_command(['fn', 'application', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--application-id' in result.output
        result = util.invoke_command(['fn', 'application', 'update', '--config'])
        assert 'Error: --config option requires an argument' in result.output

    def test_application_list(self):
        result = util.invoke_command(['fn', 'application', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output

    def test_application_get(self):
        result = util.invoke_command(['fn', 'application', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--application-id' in result.output

    def test_application_change_compartment(self):
        result = util.invoke_command(['fn', 'application', 'change-compartment'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        assert '--application-id' in result.output

    def test_fn_function(self):
        result = util.invoke_command(['fn', 'function'])
        assert 'create' in result.output
        assert 'delete' in result.output
        assert 'update' in result.output
        assert 'list' in result.output
        assert 'get' in result.output
        assert 'invoke' in result.output

    def test_function_create(self):
        result = util.invoke_command(['fn', 'function', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--display-name' in result.output
        assert '--application-id' in result.output
        assert '--image' in result.output
        assert '--memory-in-mbs' in result.output
        result = util.invoke_command(['fn', 'function', 'create', '--memory-in-mbs', 'x'])
        assert "Error: Invalid value for '--memory-in-mbs': x is not a valid integer" in result.output
        result = util.invoke_command(['fn', 'function', 'create', '--config'])
        assert 'Error: --config option requires an argument' in result.output

    def test_function_delete(self):
        result = util.invoke_command(['fn', 'function', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--function-id' in result.output

    def test_function_update(self):
        result = util.invoke_command(['fn', 'function', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--function-id' in result.output
        result = util.invoke_command(['fn', 'function', 'update', '--memory-in-mbs', 'x'])
        assert "Error: Invalid value for '--memory-in-mbs': x is not a valid integer" in result.output
        result = util.invoke_command(['fn', 'function', 'update', '--image'])
        assert 'Error: --image option requires an argument' in result.output
        result = util.invoke_command(['fn', 'function', 'update', '--config'])
        assert 'Error: --config option requires an argument' in result.output

    def test_function_list(self):
        result = util.invoke_command(['fn', 'function', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--application-id' in result.output

    def test_function_get(self):
        result = util.invoke_command(['fn', 'function', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--function-id' in result.output

    def test_function_invoke(self):
        result = util.invoke_command(['fn', 'function', 'invoke'])
        assert 'Error: Missing option(s)' in result.output
        assert '--function-id' in result.output
        assert '--body' in result.output
        assert '--file' in result.output
        result = util.invoke_command(['fn', 'function', 'invoke', '--fn-intent', 'x'])
        assert "Error: Invalid value for '--fn-intent': invalid choice: x. (choose from httprequest, cloudevent)" in result.output
        result = util.invoke_command(['fn', 'function', 'invoke', '--fn-invoke-type', 'x'])
        assert "Error: Invalid value for '--fn-invoke-type': invalid choice: x. (choose from detached, sync)" in result.output
