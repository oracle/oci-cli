# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import mock
import unittest
from services.object_storage.src.oci_cli_object_storage.objectstorage_cli_extended import time_delta
from services.object_storage.src.oci_cli_object_storage.objectstorage_cli_extended import _get_progress_bar_label
import oci_cli
from tests import util
import tempfile
import shutil
import os


class TestObjectStorage(unittest.TestCase):
    def setUp(self):
        pass

    def test_time_delta(self):
        assert time_delta(0, 34) == 'less than 1 minute'
        assert time_delta(0, 60 * 60) == '0 days 1 hour 0 mins'
        assert time_delta(1, 0) == '1 day 0 hours 0 mins'
        assert time_delta(2, 12840) == '2 days 3 hours 34 mins'

    @mock.patch('click.termui.get_terminal_size')
    def test_get_progress_bar_label(self, mock_click):
        mock_click.return_value = (40, 80)
        str_long_slash = '0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0' \
                         '123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF/'
        str_long = '0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456' \
                   '789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'
        str_normal = 'filename'
        assert _get_progress_bar_label('', str_long_slash, 'Deleted') == 'Deleted item'
        assert _get_progress_bar_label('', str_long, 'Deleted') == 'Deleted item'
        assert _get_progress_bar_label('', str_normal, 'Deleted') == 'Deleted filename'

    def test_verify_checksum(self):
        td = tempfile.mkdtemp()
        tf = tempfile.NamedTemporaryFile(dir=td, delete=False)
        tmp_file_name = tf.name
        tf.close()
        result = util.invoke_command(['os', 'object', 'put', '--bucket-name', 'test', '--file', tmp_file_name, '--verify-checksum', '--force'])
        assert "ServiceError" in result.output
        assert "BucketNotFound" in result.output
        result = util.invoke_command(['os', 'object', 'bulk-upload', '--bucket-name', 'test', '--src-dir', td, '--verify-checksum'])
        assert "ServiceError" in result.output
        assert "BucketNotFound" in result.output
        os.unlink(tmp_file_name)
        shutil.rmtree(td)

    def test_verify_namespace_name_param(self):
        """ Checks whether all object storage commands have the namespace-name parameter """
        commands = oci_cli.cli_util.collect_commands(oci_cli.cli_root.cli.commands.get('os'))
        for command in commands:
            for param in command.params:
                if any(p in param.opts for p in ['-ns', '--namespace', '--namespace-name']):
                    print(command.parent.name, command.name, param.opts)
                    assert '-ns' in param.opts
                    assert '--namespace' in param.opts
                    assert '--namespace-name' in param.opts
                if any(p in param.opts for p in ['-bn', '--bucket-name']):
                    print(command.parent.name, command.name, param.opts)
                    assert '-bn' in param.opts
                    assert '--bucket-name' in param.opts

    def test_object_put(self):
        result = util.invoke_command(['os', 'object', 'put', '--content-disposition', 'dummy-value', '--cache-control', 'dummy-value'])

        print(result.output)
        assert "Missing option(s)" in result.output

    def test_create_replication_policy(self):
        result = util.invoke_command(['os', 'replication', 'create-replication-policy'])
        assert "Error: Missing option(s)" in result.output
        assert "bucket-name" in result.output
        assert "destination-bucket" in result.output
        assert "destination-region" in result.output
        assert "name" in result.output

    def test_retention_rule_params(self):
        """ Checks whether the time-amount and time-unit params are present for the relevant retention-rule commands """
        # Sorted lists of commands that should support --time-amount and --time-unit
        retention_duration_cmd_list = sorted([
            'retention-rule create', 'retention-rule update'
        ])

        retention_time_amount_param_results = {}
        retention_time_unit_param_results = {}
        retention_duration_param_results = {}

        commands = oci_cli.cli_util.collect_commands(oci_cli.cli_root.cli.commands.get('os'))
        for command in commands:
            key = command.parent.name + ' ' + command.name
            if key in retention_duration_cmd_list:
                for param in command.params:
                    if '--time-amount' in param.opts:
                        retention_time_amount_param_results[key] = True
                    if '--time-unit' in param.opts:
                        retention_time_unit_param_results[key] = True
                    if '--duration' in param.opts:
                        retention_duration_param_results[key] = True
        assert sorted(list(retention_time_amount_param_results.keys())) == retention_duration_cmd_list
        assert sorted(list(retention_time_unit_param_results.keys())) == retention_duration_cmd_list
        assert len(retention_duration_param_results) == 0

    def test_create_retention_rule(self):
        result = util.invoke_command(['os', 'retention-rule', 'create'])
        assert "Error: Missing option(s)" in result.output
        assert "--bucket-name" in result.output

        result = util.invoke_command(['os', 'retention-rule', 'create', '--bucket-name', 'b001', '--namespace-name', 'n001', '--time-amount', '1'])
        assert "UsageError: Parameter --time-unit is required" in result.output

        result = util.invoke_command(['os', 'retention-rule', 'create', '--bucket-name', 'b001', '--namespace-name', 'n001', '--time-amount', '1', '--time-unit', 'INVALID_UNIT'])
        assert "Error: Invalid value" in result.output
        assert "invalid choice: INVALID_UNIT" in result.output

    def test_update_retention_rule(self):
        result = util.invoke_command(['os', 'retention-rule', 'update'])
        assert "Error: Missing option(s)" in result.output
        assert "--bucket-name" in result.output
        assert "--retention-rule-id" in result.output

        result = util.invoke_command(['os', 'retention-rule', 'update', '--bucket-name', 'b001', '--namespace-name', 'n001', '--retention-rule-id', 'r001', '--time-amount', '1'])
        assert "UsageError: Parameter --time-unit is required" in result.output

        result = util.invoke_command(['os', 'retention-rule', 'update', '--bucket-name', 'b001', '--namespace-name', 'n001', '--retention-rule-id', 'r001', '--time-amount', '1', '--time-unit', 'INVALID_UNIT'])
        assert "Error: Invalid value" in result.output
        assert "invalid choice: INVALID_UNIT" in result.output

        result = util.invoke_command(['os', 'retention-rule', 'update', '--bucket-name', 'b001', '--namespace-name', 'n001', '--retention-rule-id', 'r001', '--time-amount', 'abc'])
        assert "BadParameter:" in result.output
        assert "is not a valid integer" in result.output

        result = util.invoke_command(['os', 'retention-rule', 'update', '--bucket-name', 'b001', '--namespace-name', 'n001', '--retention-rule-id', 'r001', '--time-rule-locked', 'abc'])
        assert "BadParameter:" in result.output
        assert "is not in a supported datetime format" in result.output
