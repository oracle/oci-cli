# coding: utf-8
# Copyright (c) 2026, Oracle and/or its affiliates.

import unittest

from click.testing import CliRunner
from oci_cli.cli_root import cli


class TestDatabaseMigrationCliExtended(unittest.TestCase):
    def test_data_verification_group(self):
        result = CliRunner().invoke(cli, ['database-migration', 'migration', 'data-verification', '--help'])

        assert result.exit_code == 0
        assert 'get-detail' in result.output
        assert 'list-object-statuses' in result.output
        assert 'list-object-type-counts' in result.output
        assert 'list-table-row-counts' in result.output
        assert 'run' in result.output
        assert 'run-default' in result.output
