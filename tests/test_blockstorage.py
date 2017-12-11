# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import json
import unittest
from . import command_coverage_validator
from . import util
from .test_list_filter import retrieve_list_and_ensure_sorted
import oci_cli


class TestBlockStorage(unittest.TestCase):

    @util.slow
    @command_coverage_validator.CommandCoverageValidator(oci_cli.blockstorage_cli.blockstorage_group, expected_not_called_count=4)
    def test_all_operations(self, validator):
        """Successfully calls every operation with basic options."""
        self.validator = validator

        try:
            self.subtest_volume_operations()
            self.subtest_clone_operations()
            self.subtest_volume_backup_operations()
        finally:
            self.subtest_delete()

    def test_volume_create_validations(self):
        result = self.invoke(['volume', 'create', '--source-volume-id', 'unit-test', '--volume-backup-id', 'unit-test', '--availability-domain', 'unit-test', '--compartment-id', 'unit-test'])
        assert 'You cannot specify both the --volume-backup-id and --source-volume-id options' in result.output

        result = self.invoke(['volume', 'create', '-c', util.COMPARTMENT_ID, '--size-in-gbs', '50'])
        assert 'An availability domain must be specified when creating an empty volume or restoring a volume from a backup' in result.output

        result = self.invoke(['volume', 'create', '-c', util.COMPARTMENT_ID, '--volume-backup-id', 'unit-test'])
        assert 'An availability domain must be specified when creating an empty volume or restoring a volume from a backup' in result.output

        result = self.invoke(['volume', 'create', '--availability-domain', util.availability_domain()])
        assert 'A compartment ID must be specified when creating an empty volume' in result.output

        result = self.invoke(['volume', 'create', '--source-volume-id', 'unit-test', '--size-in-mbs', '51200'])
        assert 'You cannot specify a size when cloning a volume or restoring a volume from a backup' in result.output

        result = self.invoke(['volume', 'create', '--source-volume-id', 'unit-test', '--size-in-gbs', '50'])
        assert 'You cannot specify a size when cloning a volume or restoring a volume from a backup' in result.output

        result = self.invoke(['volume', 'create', '--availability-domain', util.availability_domain(), '--volume-backup-id', 'unit-test', '--size-in-mbs', '51200'])
        assert 'You cannot specify a size when cloning a volume or restoring a volume from a backup' in result.output

        result = self.invoke(['volume', 'create', '--availability-domain', util.availability_domain(), '--volume-backup-id', 'unit-test', '--size-in-gbs', '50'])
        assert 'You cannot specify a size when cloning a volume or restoring a volume from a backup' in result.output

        result = self.invoke(['volume', 'create', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(), '--size-in-gbs', '50', '--size-in-mbs', '51200'])
        assert 'You cannot specify both --size-in-mbs and --size-in-gbs' in result.output

    @util.log_test
    def subtest_volume_operations(self):
        volume_name = util.random_name('cli_test_volume')
        params = ['volume', 'create', '--availability-domain', util.availability_domain(), '--compartment-id', util.COMPARTMENT_ID, '--display-name', volume_name]

        self.volume_id = self.volume_operations_internal(volume_name, params, None, str(50 * 1024))
        self.volume_id_two = self.volume_operations_internal(volume_name, params, '50', None)

        retrieve_list_and_ensure_sorted(
            ['bv', 'volume', 'list', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(), '--sort-by', 'DISPLAYNAME', '--sort-order', 'asc'],
            'display-name',
            'asc'
        )
        retrieve_list_and_ensure_sorted(
            ['bv', 'volume', 'list', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(), '--sort-by', 'DISPLAYNAME', '--sort-order', 'desc'],
            'display-name',
            'desc'
        )
        retrieve_list_and_ensure_sorted(
            ['bv', 'volume', 'list', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(), '--sort-by', 'TIMECREATED', '--sort-order', 'asc', '--all'],
            'time-created',
            'asc'
        )
        retrieve_list_and_ensure_sorted(
            ['bv', 'volume', 'list', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(), '--sort-by', 'TIMECREATED', '--sort-order', 'desc', '--all'],
            'time-created',
            'desc'
        )

    def volume_operations_internal(self, volume_name, command_params, size_gb, size_mb):
        params_to_use = list(command_params)
        if size_gb:
            params_to_use.extend(['--size-in-gbs', size_gb])
        elif size_mb:
            params_to_use.extend(['--size-in-mbs', size_mb])

        result = self.invoke(params_to_use)
        util.validate_response(result)
        parsed_result = json.loads(result.output)
        if size_gb:
            assert str(parsed_result['data']['size-in-gbs']) == size_gb
        elif size_mb:
            assert str(parsed_result['data']['size-in-mbs']) == size_mb

        volume_id = util.find_id_in_response(result.output)
        util.wait_until(['bv', 'volume', 'get', '--volume-id', volume_id], 'AVAILABLE', max_wait_seconds=180)

        result = self.invoke(['volume', 'get', '--volume-id', volume_id])
        util.validate_response(result)
        parsed_result = json.loads(result.output)
        if size_gb:
            assert str(parsed_result['data']['size-in-gbs']) == size_gb
        elif size_mb:
            assert str(parsed_result['data']['size-in-mbs']) == size_mb

        result = self.invoke(['volume', 'list', '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)

        volume_name = volume_name + "_UPDATED"
        result = self.invoke(['volume', 'update', '--volume-id', volume_id, '--display-name', volume_name])
        util.validate_response(result)

        return volume_id

    @util.log_test
    def subtest_clone_operations(self):
        volume_name = util.random_name('cli_test_clone_vol')
        params = ['volume', 'create', '--source-volume-id', self.volume_id, '--display-name', volume_name]

        result = self.invoke(params)
        util.validate_response(result)

        parsed_result = json.loads(result.output)
        source_details = {'id': self.volume_id, 'type': 'volume'}
        assert source_details == parsed_result['data']['source-details']
        assert util.COMPARTMENT_ID == parsed_result['data']['compartment-id']
        assert util.availability_domain() == parsed_result['data']['availability-domain']
        assert 50 == int(parsed_result['data']['size-in-gbs'])  # We initially created a 50GB volume

        volume_id = util.find_id_in_response(result.output)
        util.wait_until(['bv', 'volume', 'get', '--volume-id', volume_id], 'AVAILABLE', max_wait_seconds=180)
        util.wait_until(['bv', 'volume', 'get', '--volume-id', volume_id], True, max_wait_seconds=360, state_property_name="is-hydrated")

        result = self.invoke(['volume', 'delete', '--volume-id', volume_id, '--force'])
        util.validate_response(result)

    @util.log_test
    def subtest_volume_backup_operations(self):
        backup_name = util.random_name('cli_test_backup')
        result = self.invoke(['backup', 'create', '--volume-id', self.volume_id, '--display-name', backup_name])
        util.validate_response(result)
        self.backup_id = util.find_id_in_response(result.output)

        util.wait_until(['bv', 'backup', 'get', '--volume-backup-id', self.backup_id], 'AVAILABLE',
                        max_wait_seconds=600)

        result = self.invoke(['backup', 'get', '--volume-backup-id', self.backup_id])
        util.validate_response(result)
        parsed_result = json.loads(result.output)
        assert parsed_result['data']['size-in-gbs'] is not None
        assert parsed_result['data']['size-in-mbs'] is not None
        assert parsed_result['data']['unique-size-in-gbs'] is not None
        assert parsed_result['data']['unique-size-in-mbs'] is not None

        result = self.invoke(['backup', 'list', '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)

        result = self.invoke(
            ['backup', 'list', '--compartment-id', util.COMPARTMENT_ID, '--volume-id', self.volume_id])
        util.validate_response(result)
        self.assertEquals(1, len(json.loads(result.output)['data']))

        retrieve_list_and_ensure_sorted(
            ['bv', 'backup', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'DISPLAYNAME', '--sort-order', 'asc'],
            'display-name',
            'asc'
        )
        retrieve_list_and_ensure_sorted(
            ['bv', 'backup', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'DISPLAYNAME', '--sort-order', 'desc'],
            'display-name',
            'desc'
        )
        retrieve_list_and_ensure_sorted(
            ['bv', 'backup', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'TIMECREATED', '--sort-order', 'asc', '--all'],
            'time-created',
            'asc'
        )
        retrieve_list_and_ensure_sorted(
            ['bv', 'backup', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'TIMECREATED', '--sort-order', 'desc', '--all'],
            'time-created',
            'desc'
        )

        backup_name = backup_name + "_UPDATED"
        result = self.invoke(
            ['backup', 'update', '--volume-backup-id', self.backup_id, '--display-name', backup_name])
        util.validate_response(result)

        result = self.invoke(['volume', 'create', '--volume-backup-id', self.backup_id, '--availability-domain', util.second_availability_domain()])
        util.validate_response(result)

        parsed_result = json.loads(result.output)
        source_details = {'id': self.backup_id, 'type': 'volumeBackup'}
        assert source_details == parsed_result['data']['source-details']
        assert util.COMPARTMENT_ID == parsed_result['data']['compartment-id']
        assert util.second_availability_domain() == parsed_result['data']['availability-domain']
        assert 50 == int(parsed_result['data']['size-in-gbs'])  # We initially created a 50GB volume

        volume_id = util.find_id_in_response(result.output)
        util.wait_until(['bv', 'volume', 'get', '--volume-id', volume_id], 'AVAILABLE', max_wait_seconds=180)

        result = self.invoke(['volume', 'delete', '--volume-id', volume_id, '--force'])
        util.validate_response(result)

        # Make sure we're still in a good state before deleting.
        util.wait_until(['bv', 'backup', 'get', '--volume-backup-id', self.backup_id], 'AVAILABLE',
                        max_interval_seconds=180)

    @util.log_test
    def subtest_delete(self):
        error_count = 0

        if hasattr(self, 'backup_id'):
            try:
                result = self.invoke(['backup', 'delete', '--volume-backup-id', self.backup_id, '--force'])
                util.validate_response(result)
                util.wait_until(['bv', 'backup', 'get', '--volume-backup-id', self.backup_id], 'TERMINATED',
                                max_interval_seconds=180)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'volume_id'):
            try:
                result = self.invoke(['volume', 'delete', '--volume-id', self.volume_id, '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'volume_id_two'):
            try:
                result = self.invoke(['volume', 'delete', '--volume-id', self.volume_id_two, '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        self.assertEquals(0, error_count)

    def invoke(self, params, debug=False, ** args):
        commands = ['bv'] + params

        if hasattr(self, 'validator'):
            self.validator.register_call(commands)

        if debug is True:
            commands = ['--debug'] + commands

        return util.invoke_command(commands, ** args)


if __name__ == '__main__':
    unittest.main()
