# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import unittest
from tests import test_config_container
from tests import util
from tests.test_list_filter import retrieve_list_and_ensure_sorted
CASSETTE_LIBRARY_DIR = 'services/core/tests/cassettes'


class TestBlockStorage(unittest.TestCase):

    @util.slow
    @test_config_container.RecordReplay('blockstorage', cassette_library_dir=CASSETTE_LIBRARY_DIR)
    def test_all_operations(self):
        """Successfully calls every operation with basic options."""
        self.volumes = []

        try:
            self.test_volume_create_validations()
            self.subtest_volume_operations()
            self.subtest_clone_operations()
            self.subtest_volume_backup_operations()
            self.subtest_volume_group_operations()
            self.subtest_volume_group_clone_operations()
            self.subtest_volume_group_backup_operations()
        finally:
            self.subtest_delete()

    @util.log_test
    def test_volume_create_validations(self):
        result = self.invoke(['volume', 'create', '--source-volume-id', 'unit-test', '--volume-backup-id', 'unit-test',
                              '--availability-domain', 'unit-test', '--compartment-id', 'unit-test'])
        assert 'You can only specify one of either --volume-backup-id, --source-volume-id or --source-volume-replica-id option' in result.output

        result = self.invoke(
            ['volume', 'create', '--source-volume-replica-id', 'unit-test', '--volume-backup-id', 'unit-test',
             '--availability-domain', 'unit-test', '--compartment-id', 'unit-test'])
        assert 'You can only specify one of either --volume-backup-id, --source-volume-id or --source-volume-replica-id option' in result.output

        result = self.invoke(['volume', 'create', '-c', util.COMPARTMENT_ID, '--size-in-gbs', '50'])
        assert 'An availability domain must be specified when creating an empty volume or restoring a volume from a backup' in result.output

        result = self.invoke(['volume', 'create', '-c', util.COMPARTMENT_ID, '--volume-backup-id', 'unit-test'])
        assert 'An availability domain must be specified when creating an empty volume or restoring a volume from a backup' in result.output

        result = self.invoke(['volume', 'create', '--availability-domain', util.availability_domain()])
        assert 'A compartment ID must be specified when creating an empty volume' in result.output

        result = self.invoke(
            ['volume', 'create', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(),
             '--size-in-gbs', '50', '--size-in-mbs', '51200'])
        assert 'You cannot specify both --size-in-mbs and --size-in-gbs' in result.output

    @util.log_test
    def subtest_volume_operations(self):
        volume_name = util.random_name('cli_test_volume')
        params = ['volume', 'create', '--availability-domain', util.availability_domain(), '--compartment-id',
                  util.COMPARTMENT_ID, '--display-name', volume_name]

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

    @util.log_test
    def subtest_volume_group_operations(self):
        # create volumes to add to a volume group
        for volume_num in range(0, 3):
            volume_name = util.random_name('cli_test_volume')
            params = ['volume', 'create', '--availability-domain', util.availability_domain(), '--compartment-id',
                      util.COMPARTMENT_ID, '--display-name', volume_name]
            volume = self.volume_operations_internal(volume_name, params, '50', None)
            self.volumes.append(volume)

        volume_group_name = util.random_name('cli_test_volume_group')
        source_details = {'type': 'volumeIds', 'volumeIds': self.volumes}
        params = ['volume-group', 'create', '--availability-domain', util.availability_domain(), '--compartment-id',
                  util.COMPARTMENT_ID, '--display-name', volume_group_name,
                  '--source-details', json.dumps(source_details)]
        self.volume_group, self.volume_ids = self.volume_group_operations_internal(volume_group_name, params)

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

        if size_gb:
            new_size_gb = int(size_gb) + 10

            volume_name = volume_name + "_UPDATED"
            result = self.invoke(['volume', 'update', '--volume-id', volume_id, '--display-name', volume_name,
                                  '--size-in-gbs', str(new_size_gb)])
            util.validate_response(result)

            util.wait_until(['bv', 'volume', 'get', '--volume-id', volume_id],
                            'AVAILABLE', max_wait_seconds=180)

            result = self.invoke(['volume', 'get', '--volume-id', volume_id])
            util.validate_response(result)
            parsed_result = json.loads(result.output)
            assert str(parsed_result['data']['size-in-gbs']) == str(new_size_gb)

        return volume_id

    @util.log_test
    def subtest_clone_operations(self):
        volume_name = util.random_name('cli_test_clone_vol')
        params = ['volume', 'create', '--source-volume-id', self.volume_id, '--display-name', volume_name,
                  '--size-in-gbs', '60']

        result = self.invoke(params)
        util.validate_response(result)

        parsed_result = json.loads(result.output)
        source_details = {'id': self.volume_id, 'type': 'volume'}
        assert source_details == parsed_result['data']['source-details']
        assert util.availability_domain() == parsed_result['data']['availability-domain']
        assert 60 == int(parsed_result['data']['size-in-gbs'])  # We initially created a 50GB volume, now increasing to 60

        volume_id = util.find_id_in_response(result.output)
        util.wait_until(['bv', 'volume', 'get', '--volume-id', volume_id], 'AVAILABLE', max_wait_seconds=180)
        util.wait_until(['bv', 'volume', 'get', '--volume-id', volume_id], True, max_wait_seconds=360,
                        state_property_name="is-hydrated")

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

        result = self.invoke(['volume', 'create', '--volume-backup-id', self.backup_id, '--availability-domain',
                              util.second_availability_domain()])
        util.validate_response(result)

        parsed_result = json.loads(result.output)
        source_details = {'id': self.backup_id, 'type': 'volumeBackup'}
        assert source_details == parsed_result['data']['source-details']
        assert util.second_availability_domain() == parsed_result['data']['availability-domain']
        assert 50 == int(parsed_result['data']['size-in-gbs'])  # We initially created a 50GB volume

        volume_id = util.find_id_in_response(result.output)
        util.wait_until(['bv', 'volume', 'get', '--volume-id', volume_id], 'AVAILABLE', max_wait_seconds=600)

        result = self.invoke(['volume', 'delete', '--volume-id', volume_id, '--force'])
        util.validate_response(result)

        # Make sure we're still in a good state before deleting.
        util.wait_until(['bv', 'backup', 'get', '--volume-backup-id', self.backup_id], 'AVAILABLE',
                        max_interval_seconds=180)

    @util.log_test
    def subtest_volume_group_clone_operations(self):
        # clone a volume group
        volume_group_name = util.random_name('cli_test_volume_group_clone')
        source_details = {'type': 'volumeGroupId', 'volumeGroupId': self.volume_group}
        params = ['volume-group', 'create', '--availability-domain', util.availability_domain(), '--compartment-id',
                  util.COMPARTMENT_ID, '--display-name', volume_group_name,
                  '--source-details', json.dumps(source_details)]
        self.volume_group_clone, self.volume_clones = self.volume_group_operations_internal(volume_group_name, params)

    @util.log_test
    def subtest_volume_group_backup_operations(self):
        # create a volume group backup, perform get & list, update it & restore from it
        backup_name = util.random_name('cli_test_volume_group_backup')
        result = self.invoke(['volume-group-backup', 'create', '--volume-group-id', self.volume_group,
                              '--display-name', backup_name])
        util.validate_response(result)
        self.volume_group_backup_id = util.find_id_in_response(result.output)

        util.wait_until(['bv', 'volume-group-backup', 'get', '--volume-group-backup-id', self.volume_group_backup_id],
                        'AVAILABLE',
                        max_wait_seconds=600)

        result = self.invoke(['volume-group-backup', 'get', '--volume-group-backup-id', self.volume_group_backup_id])
        util.validate_response(result)
        parsed_result = json.loads(result.output)
        assert parsed_result['data']['size-in-mbs'] is not None
        assert parsed_result['data']['unique-size-in-mbs'] is not None

        result = self.invoke(['volume-group-backup', 'list', '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)

        result = self.invoke(
            ['volume-group-backup', 'list', '--compartment-id', util.COMPARTMENT_ID, '--volume-group-id',
             self.volume_group])
        util.validate_response(result)
        self.assertEquals(1, len(json.loads(result.output)['data']))

        backup_name = backup_name + "_UPDATED"
        result = self.invoke(
            ['volume-group-backup', 'update', '--volume-group-backup-id', self.volume_group_backup_id, '--display-name',
             backup_name])
        util.validate_response(result)

        volume_group_name = util.random_name('cli_test_volume_group_restore')
        source_details = {'type': 'volumeGroupBackupId', 'volumeGroupBackupId': self.volume_group_backup_id}
        params = ['volume-group', 'create', '--availability-domain', util.availability_domain(), '--compartment-id',
                  util.COMPARTMENT_ID, '--display-name', volume_group_name,
                  '--source-details', json.dumps(source_details)]
        self.volume_group_restored, self.restored_volumes = self.volume_group_operations_internal(volume_group_name,
                                                                                                  params)

    def volume_group_operations_internal(self, volume_group_name, command_params):
        params_to_use = list(command_params)

        result = self.invoke(params_to_use)
        util.validate_response(result)
        parsed_result = json.loads(result.output)
        volume_group_id = util.find_id_in_response(result.output)
        volume_ids = parsed_result['data']['volume-ids']
        assert len(volume_ids) > 0

        util.wait_until(['bv', 'volume-group', 'get', '--volume-group-id', volume_group_id], 'AVAILABLE',
                        max_wait_seconds=180)

        result = self.invoke(['volume-group', 'get', '--volume-group-id', volume_group_id])
        util.validate_response(result)
        parsed_result = json.loads(result.output)
        assert parsed_result['data']['size-in-mbs'] is not None
        assert parsed_result['data']['time-created'] is not None

        result = self.invoke(['volume-group', 'list', '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)

        volume_group_name = volume_group_name + "_UPDATED"
        # if we have more than a single volume in the group, remove one and update
        if len(volume_ids) > 1:
            volume_ids.remove(volume_ids[len(volume_ids) - 1])
            result = self.invoke(
                ['volume-group', 'update', '--volume-group-id', volume_group_id, '--display-name', volume_group_name,
                 '--volume-ids', json.dumps(volume_ids), '--force'])
            util.validate_response(result)
            parsed_result = json.loads(result.output)
            assert len(parsed_result['data']['volume-ids']) == len(volume_ids)
        else:
            result = self.invoke(
                ['volume-group', 'update', '--volume-group-id', volume_group_id, '--display-name', volume_group_name])
            util.validate_response(result)

        return volume_group_id, volume_ids

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

        if hasattr(self, 'volume_group_backup_id'):
            try:
                result = self.invoke(
                    ['volume-group-backup', 'delete', '--volume-group-backup-id', self.volume_group_backup_id,
                     '--force'])
                util.validate_response(result)
                util.wait_until(
                    ['bv', 'volume-group-backup', 'get', '--volume-group-backup-id', self.volume_group_backup_id],
                    'TERMINATED', max_interval_seconds=180)
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

        if hasattr(self, 'volume_group'):
            try:
                result = self.invoke(['volume-group', 'delete', '--volume-group-id', self.volume_group, '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'volume_group_clone'):
            try:
                result = self.invoke(
                    ['volume-group', 'delete', '--volume-group-id', self.volume_group_clone, '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'volume_group_restored'):
            try:
                result = self.invoke(
                    ['volume-group', 'delete', '--volume-group-id', self.volume_group_restored, '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'volumes'):
            for volume in self.volumes:
                try:
                    result = self.invoke(['volume', 'delete', '--volume-id', volume, '--force'])
                    util.validate_response(result)
                except Exception as error:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'volume_clones'):
            for volume in self.volume_clones:
                try:
                    result = self.invoke(['volume', 'delete', '--volume-id', volume, '--force'])
                    util.validate_response(result)
                except Exception as error:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'restored_volumes'):
            for volume in self.restored_volumes:
                try:
                    result = self.invoke(['volume', 'delete', '--volume-id', volume, '--force'])
                    util.validate_response(result)
                except Exception as error:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        self.assertEquals(0, error_count)

    def invoke(self, params, debug=False, **args):
        commands = ['bv'] + params

        if debug is True:
            commands = ['--debug'] + commands

        return util.invoke_command(commands, **args)


if __name__ == '__main__':
    unittest.main()
