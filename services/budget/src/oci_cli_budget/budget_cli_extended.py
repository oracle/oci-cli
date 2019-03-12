# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from oci_cli import cli_util
from oci_cli.cli_root import cli
from oci_cli_budget.generated import budget_cli

'''
From:
oci budget budget . . .

To:
oci budgets budget
'''

cli_util.rename_command(cli, budget_cli.budget_root_group, "budgets")
