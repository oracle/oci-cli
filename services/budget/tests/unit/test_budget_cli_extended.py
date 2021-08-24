# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestBudget(unittest.TestCase):
    def setUp(self):
        pass

    def test_top_level_name(self):
        result = util.invoke_command(['budget'])
        assert "Error: No such command 'budget'" in result.output
        result = util.invoke_command(['budgets'])
        assert 'Usage: oci budgets' in result.output

    def test_budgets_budget(self):
        result = util.invoke_command(['budgets', 'budget'])
        assert 'Usage: oci budgets budget' in result.output

    def test_budgets_budget_create(self):
        result = util.invoke_command(['budgets', 'budget', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        assert '--amount' in result.output
        assert '--reset-period' in result.output

    def test_budgets_budget_delete(self):
        result = util.invoke_command(['budgets', 'budget', 'delete'])
        assert 'Error: Missing option(s) --budget-id' in result.output

    def test_budgets_budget_get(self):
        result = util.invoke_command(['budgets', 'budget', 'get'])
        assert 'Error: Missing option(s) --budget-id' in result.output

    def test_budgets_budget_list(self):
        result = util.invoke_command(['budgets', 'budget', 'list'])
        assert 'Error: Missing option(s) --compartment-id' in result.output

    def test_budgets_budget_update(self):
        result = util.invoke_command(['budgets', 'budget', 'update'])
        assert 'Error: Missing option(s) --budget-id' in result.output

    def test_budgets_alert_rule(self):
        result = util.invoke_command(['budgets', 'alert-rule'])
        assert 'Usage: oci budgets alert-rule' in result.output

    def test_budgets_alert_rule_create(self):
        result = util.invoke_command(['budgets', 'alert-rule', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--budget-id' in result.output
        assert '--type' in result.output
        assert '--threshold-type' in result.output

    def test_budgets_alert_rule_delete(self):
        result = util.invoke_command(['budgets', 'alert-rule', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--budget-id' in result.output
        assert '--alert-rule-id' in result.output

    def test_budgets_alert_rule_get(self):
        result = util.invoke_command(['budgets', 'alert-rule', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--budget-id' in result.output
        assert '--alert-rule-id' in result.output

    def test_budgets_alert_rule_list(self):
        result = util.invoke_command(['budgets', 'alert-rule', 'list'])
        assert 'Error: Missing option(s) --budget-id' in result.output

    def test_budgets_alert_rule_update(self):
        result = util.invoke_command(['budgets', 'alert-rule', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--budget-id' in result.output
        assert '--alert-rule-id' in result.output
