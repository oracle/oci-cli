# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import json
import os
import time
import unittest
from . import command_coverage_validator
from . import util
import oraclebmc_cli


CONSOLE_HISTORY_FILENAME = 'tests/output/console_history_output.txt'


class TestCompute(unittest.TestCase):

    @util.slow
    @command_coverage_validator.CommandCoverageValidator(oraclebmc_cli.compute_cli.compute_group, expected_not_called_count=0)
    def test_all_operations(self, validator):
        """Successfully calls every operation with basic options."""
        self.validator = validator

        try:
            self.subtest_setup()
            self.subtest_instance_operations()
            self.subtest_windows_instance_operations()
            self.subtest_vnic_operations()
            self.subtest_list_vnics()
            self.subtest_volume_attachment_operations()
            self.subtest_shape_operations()
            self.subtest_console_history_operations()
            self.subtest_instance_action_operations()
            self.subtest_image_operations()
        finally:
            self.subtest_delete()

    @util.log_test
    def subtest_setup(self):
        # Create a VCN
        vcn_name = util.random_name('cli_test_compute_vcn')
        cidr_block = "10.0.0.0/16"

        result = self.invoke(
            ['network', 'vcn', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--display-name', vcn_name,
             '--dns-label', 'clivcn',
             '--cidr-block', cidr_block])
        self.vcn_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)
        util.wait_until(['network', 'vcn', 'get', '--vcn-id', self.vcn_ocid], 'AVAILABLE',
                        max_wait_seconds=300)

        # Create a subnet
        subnet_name = util.random_name('cli_test_compute_subnet')

        result = self.invoke(
            ['network', 'subnet', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.AVAILABILITY_DOMAIN,
             '--display-name', subnet_name,
             '--dns-label', 'clisubnet',
             '--vcn-id', self.vcn_ocid,
             '--cidr-block', cidr_block,
             ])
        self.subnet_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)
        util.wait_until(['network', 'subnet', 'get', '--subnet-id', self.subnet_ocid], 'AVAILABLE',
                        max_wait_seconds=300)

        # Create a volume
        volume_name = util.random_name('cli_test_compute_volume')
        result = self.invoke(['bv', 'volume', 'create', '--availability-domain', util.AVAILABILITY_DOMAIN, '--compartment-id',
                              util.COMPARTMENT_ID, '--display-name', volume_name])
        util.validate_response(result)
        self.volume_ocid = util.find_id_in_response(result.output)
        util.wait_until(['bv', 'volume', 'get', '--volume-id', self.volume_ocid], 'AVAILABLE', max_wait_seconds=180)

    @util.log_test
    def subtest_instance_operations(self):
        instance_name = util.random_name('cli_test_instance')
        image_id = 'ocid1.image.oc1.phx.aaaaaaaamv5wg7ffvaxaba3orhpuya7x7opz24hd6m7epmwfqbeudi6meepq'  # ol6.8-base-0.0.2
        shape = 'VM.Standard1.8'

        result = self.invoke(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.AVAILABILITY_DOMAIN,
             '--display-name', instance_name,
             '--subnet-id', self.subnet_ocid,
             '--image-id', image_id,
             '--shape', shape,
             '--metadata', util.remove_outer_quotes(oraclebmc_cli.core_cli_extended.compute_instance_launch_metadata_example)])
        self.instance_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)

        util.wait_until(['compute', 'instance', 'get', '--instance-id', self.instance_ocid], 'RUNNING',
                        max_wait_seconds=600)

        result = self.invoke(['compute', 'instance', 'list', '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)

        # list with compartment shortcut
        result = self.invoke(['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID])
        util.validate_response(result)

        instance_name = instance_name + "_updated"
        result = self.invoke(['compute', 'instance', 'update', '--instance-id', self.instance_ocid, '--display-name', instance_name])
        util.validate_response(result, expect_etag=True)

        result = self.invoke(['compute', 'instance', 'get', '--instance-id', self.instance_ocid])
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_windows_instance_operations(self):
        instance_name = util.random_name('cli_test_instance')
        image_id = 'ocid1.image.oc1.phx.aaaaaaaa53cliasgvqmutflwqkafbro2y4ywjebci5szc4eus5byy2e2b7ua'  # Windows2012ServerR2-Standard
        shape = 'VM.Standard1.2'

        result = self.invoke(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.AVAILABILITY_DOMAIN,
             '--display-name', instance_name,
             '--subnet-id', self.subnet_ocid,
             '--image-id', image_id,
             '--shape', shape])
        self.windows_instance_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)

        util.wait_until(['compute', 'instance', 'get', '--instance-id', self.windows_instance_ocid], 'RUNNING',
                        max_wait_seconds=600)

        result = self.invoke(['compute', 'instance', 'get', '--instance-id', self.windows_instance_ocid])
        util.validate_response(result, expect_etag=True)

        result = self.invoke(
            ['compute', 'instance', 'get-windows-initial-creds', '--instance-id', self.windows_instance_ocid])

        util.validate_response(result)

        credentials = json.loads(result.output)['data']
        assert credentials['username'] == 'opc'
        assert 'password' in credentials

    @util.log_test
    def subtest_list_vnics(self):
        result = self.invoke(['compute', 'instance', 'list-vnics', '--instance-id', self.instance_ocid])
        util.validate_response(result)
        json_data = json.loads(result.output)

        assert (len(json_data['data']) == 1)

        # Check that setting limit to 1 will give us a next page token, and calling with that page will give us 0 items.
        result = self.invoke(['compute', 'instance', 'list-vnics', '--instance-id', self.instance_ocid, '--limit', '1'])
        util.validate_response(result)
        json_data = json.loads(result.output)
        assert ('data' not in json_data or len(json_data['data']) == 1)
        assert ('opc-next-page' in json_data)
        next_page = json_data['opc-next-page']

        result = self.invoke(
            ['compute', 'instance', 'list-vnics', '--instance-id', self.instance_ocid, '--page', next_page])
        util.validate_response(result)
        assert (len(result.output) == 0)

    @util.log_test
    def subtest_vnic_operations(self):
        result = self.invoke(
            ['compute', 'vnic-attachment', 'list', '--compartment-id', util.COMPARTMENT_ID, '--instance-id',
             self.instance_ocid])
        util.validate_response(result)
        json_data = json.loads(result.output)
        assert (len(json_data['data']) == 1)
        vnic_id = json_data['data'][0]['vnic-id']

        # Test get vnic, since this is not tested in test_virtualnetwork.py.
        result = self.invoke(
            ['network', 'vnic', 'get', '--vnic-id', vnic_id])
        util.validate_response(result)

    @util.log_test
    def subtest_volume_attachment_operations(self):
        va_name = util.random_name('cli_test_va')

        result = self.invoke(
            ['compute', 'volume-attachment', 'attach',
             '--display-name', va_name,
             '--type', 'iscsi',
             '--instance-id', self.instance_ocid,
             '--volume-id', self.volume_ocid])
        self.va_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)
        util.wait_until(['compute', 'volume-attachment', 'get', '--volume-attachment-id', self.va_ocid], 'ATTACHED', max_wait_seconds=300)

        result = self.invoke(['compute', 'volume-attachment', 'list', '--compartment-id', util.COMPARTMENT_ID, '--instance-id', self.instance_ocid])
        util.validate_response(result)

        result = self.invoke(['compute', 'volume-attachment', 'get', '--volume-attachment-id', self.va_ocid])
        util.validate_response(result, expect_etag=True)

        result = self.invoke(['compute', 'volume-attachment', 'detach', '--volume-attachment-id', self.va_ocid, '--force'])
        util.validate_response(result)
        util.wait_until(['compute', 'volume-attachment', 'get', '--volume-attachment-id', self.va_ocid],
                        'DETACHED', max_wait_seconds=300)

    @util.log_test
    def subtest_shape_operations(self):
        result = self.invoke(
            ['compute', 'shape', 'list', '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)

    @util.log_test
    def subtest_console_history_operations(self):
        result = self.invoke(
            ['compute', 'console-history', 'capture', '--instance-id', self.instance_ocid])
        self.ch_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)
        util.wait_until(['compute', 'console-history', 'get', '--instance-console-history-id', self.ch_ocid], 'SUCCEEDED', max_wait_seconds=300)

        result = self.invoke(['compute', 'console-history', 'list', '--compartment-id', util.COMPARTMENT_ID, '--instance-id', self.instance_ocid])
        util.validate_response(result)

        result = self.invoke(['compute', 'console-history', 'get', '--instance-console-history-id', self.ch_ocid])
        util.validate_response(result, expect_etag=True)

        if os.path.exists(CONSOLE_HISTORY_FILENAME):
            os.remove(CONSOLE_HISTORY_FILENAME)

        result = self.invoke(['compute', 'console-history', 'get-content', '--instance-console-history-id', self.ch_ocid, '--file', CONSOLE_HISTORY_FILENAME])
        util.validate_response(result)

        with open(CONSOLE_HISTORY_FILENAME, 'rb') as file:
            # Make sure that we got at least some minimum amount of content.
            assert (len(file.read()) > 500)

    @util.log_test
    def subtest_instance_action_operations(self):
        result = self.invoke(['compute', 'instance', 'action', '--instance-id', self.instance_ocid, '--action', 'RESET'])
        util.validate_response(result)
        time.sleep(10)
        util.wait_until(['compute', 'instance', 'get', '--instance-id', self.instance_ocid], 'RUNNING',
                        max_wait_seconds=300)
        time.sleep(5)

    @util.log_test
    def subtest_image_operations(self):
        image_name = util.random_name('cli_test_image')

        result = self.invoke(
            ['compute', 'image', 'create',
             '--display-name', image_name,
             '--instance-id', self.instance_ocid,
             '--compartment-id', util.COMPARTMENT_ID])
        self.image_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)

        # Waiting for the image can take 20 or 30 minutes. Instead, we'll just delete the instance
        # while it's still taking the snapshot. Uncomment the wait below to wait for the image to finish.
        # util.wait_until(['compute', 'image', 'get', '--image-id', self.image_ocid], 'AVAILABLE', max_wait_seconds=2700)

        result = self.invoke(
            ['compute', 'image', 'list', '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)

        result = self.invoke(['compute', 'image', 'get', '--image-id', self.image_ocid])
        util.validate_response(result, expect_etag=True)

        image_name = image_name + "_updated"
        result = self.invoke(['compute', 'image', 'update', '--image-id', self.image_ocid, '--display-name', image_name])
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_delete(self):
        error_count = 0

        if hasattr(self, 'image_ocid'):
            try:
                print("Deleting image")
                result = self.invoke(['compute', 'image', 'delete', '--image-id', self.image_ocid, '--force'])
                util.validate_service_error(result, error_message="409")
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'ch_ocid'):
            try:
                print("Deleting console history")
                result = self.invoke(['compute', 'console-history', 'delete', '--instance-console-history-id', self.ch_ocid, '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'instance_ocid'):
            try:
                print("Deleting instance")
                result = self.invoke(['compute', 'instance', 'terminate', '--instance-id', self.instance_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['compute', 'instance', 'get', '--instance-id', self.instance_ocid], 'TERMINATED',
                                max_wait_seconds=600, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'windows_instance_ocid'):
            try:
                print("Deleting windows instance")
                result = self.invoke(
                    ['compute', 'instance', 'terminate', '--instance-id', self.windows_instance_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['compute', 'instance', 'get', '--instance-id', self.windows_instance_ocid],
                                'TERMINATED',
                                max_wait_seconds=600, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'volume_ocid'):
            try:
                print("Deleting volume")
                result = self.invoke(['bv', 'volume', 'delete', '--volume-id', self.volume_ocid, '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'subnet_ocid'):
            try:
                print("Deleting subnet")
                result = self.invoke(['network', 'subnet', 'delete', '--subnet-id', self.subnet_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['network', 'subnet', 'get', '--subnet-id', self.subnet_ocid], 'TERMINATED',
                                max_wait_seconds=600, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'vcn_ocid'):
            try:
                print("Deleting vcn")
                result = self.invoke(['network', 'vcn', 'delete', '--vcn-id', self.vcn_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['network', 'vcn', 'get', '--vcn-id', self.vcn_ocid], 'TERMINATED',
                                max_wait_seconds=600, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        self.assertEquals(0, error_count)

    def invoke(self, commands, debug=False, ** args):
        self.validator.register_call(commands)

        if debug is True:
            commands = ['--debug'] + commands

        return util.invoke_command(commands, ** args)


if __name__ == '__main__':
    unittest.main()
