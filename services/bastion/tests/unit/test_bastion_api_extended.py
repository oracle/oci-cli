# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/bastion/tests/unit/test_bastion_api_extended.py
class TestBastionApi(unittest.TestCase):
    def setUp(self):
        pass

    def test_bastion_api_options(self):
        result = util.invoke_command(['bastion', 'bastion'])
        assert 'change-compartment' in result.output
        assert 'create' in result.output
        assert 'delete' in result.output
        assert 'get' in result.output
        assert 'list' in result.output
        assert 'update' in result.output
        assert '--help' in result.output

    def test_bastion_create(self):
        result = util.invoke_command(['bastion', 'bastion', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        assert '--target-subnet-id' in result.output
        assert '--bastion-type' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'create', '--compartment-id'])
        assert 'Error: --compartment-id option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'create', '--name'])
        assert 'Error: --name option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'create', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'create', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'create', '--wait-for-state'])
        assert 'Error: --wait-for-state option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'create', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'create', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output

    def test_bastion_get(self):
        result = util.invoke_command(['bastion', 'bastion', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--bastion-id' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'get', '--bastion-id'])
        assert 'Error: --bastion-id option requires an argument' in result.output

    def test_bastion_delete(self):
        result = util.invoke_command(['bastion', 'bastion', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--bastion-id' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'delete', '--bastion-id'])
        assert 'Error: --bastion-id option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'delete', '--if-match'])
        assert 'Error: --if-match option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'delete', '--wait-for-state'])
        assert 'Error: --wait-for-state option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'delete', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'delete', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output

    def test_bastion_list(self):
        result = util.invoke_command(['bastion', 'bastion', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'list', '--compartment-id'])
        assert 'Error: --compartment-id option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'list', '--bastion-id'])
        assert 'Error: --bastion-id option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'list', '--bastion-lifecycle-state'])
        assert 'Error: --bastion-lifecycle-state option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'list', '--name'])
        assert 'Error: --name option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'list', '--limit'])
        assert 'Error: --limit option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'list', '--page'])
        assert 'Error: --page option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'list', '--sort-order'])
        assert 'Error: --sort-order option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'list', '--sort-order', 'desc'])
        result = util.invoke_command(['bastion', 'bastion', 'list', '--sort-order', 'ASC'])
        result = util.invoke_command(['bastion', 'bastion', 'list', '--sort-by'])
        assert 'Error: --sort-by option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'list', '--sort-by', 'DISPLAYNAME'])
        result = util.invoke_command(['bastion', 'bastion', 'list', '--sort-by', 'timeCreated'])
        result = util.invoke_command(['bastion', 'bastion', 'list', '--page-size'])
        assert 'Error: --page-size option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'list', '--all'])

    def test_bastion_update(self):
        result = util.invoke_command(['bastion', 'bastion', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--bastion-id' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'update', '--if-match'])
        assert 'Error: --if-match option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'update', '--defined-tags'])
        assert 'Error: --defined-tags option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'update', '--freeform-tags'])
        assert 'Error: --freeform-tags option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'update', '--wait-for-state'])
        assert 'Error: --wait-for-state option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'update', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'update', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'bastion', 'update', '--force'])
