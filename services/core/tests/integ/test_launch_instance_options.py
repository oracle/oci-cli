# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import unittest
from tests import test_config_container
from tests import util
import services.core.src.oci_cli_compute as oci_cli_compute

CASSETTE_LIBRARY_DIR = 'services/core/tests/cassettes'
IPXE_SCRIPT_FILE = 'tests/resources/ipxe_script_example.txt'
USER_DATA_FILE = 'tests/resources/user_data.sh'


class TestLaunchInstanceOptions(unittest.TestCase):

    @util.slow
    @test_config_container.RecordReplayWithNoClickContext('launch_instance_options', cassette_library_dir=CASSETTE_LIBRARY_DIR)
    def test_main(self):
        self.instance_ocids = []

        try:
            self.subtest_setup()
            self.subtest_launch_instance_with_assign_private_dns()
            self.subtest_launch_instance_ipxe_script_file_and_extended_metadata()
            self.subtest_launch_instance_ssh_authorized_keys_in_param_and_in_metadata_throws_error()
            self.subtest_launch_instance_user_data_in_param_and_in_metadata_throws_error()
            self.subtest_launch_instance_user_data_file_and_ssh_authorized_users_file()
            self.subtest_launch_instance_merges_user_data_file_param_with_metadata()
        finally:
            self.subtest_delete()

    @util.log_test
    def subtest_setup(self):
        # Create a VCN
        vcn_name = util.random_name('cli_test_compute_vcn')
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = util.random_name('vcn', insert_underscore=False)

        result = util.invoke_command(
            ['network', 'vcn', 'create', '--compartment-id', util.COMPARTMENT_ID, '--display-name', vcn_name, '--cidr-block',
             cidr_block, '--dns-label', vcn_dns_label])
        self.vcn_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)
        util.wait_until(['network', 'vcn', 'get', '--vcn-id', self.vcn_ocid], 'AVAILABLE',
                        max_wait_seconds=300)

        # Create a subnet
        subnet_name = util.random_name('cli_test_compute_subnet')
        subnet_dns_label = util.random_name('subnet', insert_underscore=False)

        result = util.invoke_command(
            ['network', 'subnet', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', subnet_name,
             '--vcn-id', self.vcn_ocid,
             '--cidr-block', cidr_block,
             '--dns-label', subnet_dns_label
             ])
        self.subnet_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)
        util.wait_until(['network', 'subnet', 'get', '--subnet-id', self.subnet_ocid], 'AVAILABLE',
                        max_wait_seconds=300)

    @util.log_test
    def subtest_launch_instance_ipxe_script_file_and_extended_metadata(self):
        instance_name = util.random_name('cli_test_instance_options')
        image_id = util.oracle_linux_image()
        shape = 'VM.Standard1.2'
        hostname_label = util.random_name('bminstance', insert_underscore=False)
        vnic_display_name = 'vnic_display_name'
        private_ip = '10.0.0.15'
        assign_public_ip = 'true'

        extended_metadata = '{"a": "1", "b": {"c": "3", "d": {}}}'

        launch_instance_result = util.invoke_command(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', instance_name,
             '--subnet-id', self.subnet_ocid,
             '--image-id', image_id,
             '--shape', shape,
             '--ipxe-script-file', IPXE_SCRIPT_FILE,
             '--hostname-label', hostname_label + "1",
             '--private-ip', private_ip,
             '--assign-public-ip', assign_public_ip,
             '--vnic-display-name', vnic_display_name,
             '--extended-metadata', extended_metadata])

        temp_instance_ocid = util.find_id_in_response(launch_instance_result.output)
        self.instance_ocids.append(temp_instance_ocid)
        util.validate_response(launch_instance_result, expect_etag=True)

        extended_metadata_result = json.loads(launch_instance_result.output)['data']['extended-metadata']
        assert extended_metadata_result['a'] == '1'
        assert extended_metadata_result['b']['c'] == '3'

        # This can be in ATTACHING state for some time
        try:
            util.wait_until(['compute', 'vnic-attachment', 'list', '--compartment-id', util.COMPARTMENT_ID, '--instance-id',
                            temp_instance_ocid], 'ATTACHED', max_wait_seconds=60, item_index_in_list_response=0)
        except Exception:
            try:
                # If it is ATTACHING we will consider it good enough
                util.wait_until(['compute', 'vnic-attachment', 'list', '--compartment-id', util.COMPARTMENT_ID, '--instance-id',
                                temp_instance_ocid], 'ATTACHING', max_wait_seconds=30, item_index_in_list_response=0)
            except Exception:
                # If it is not ATTACHING, double check that it didn't go to ATTACHED
                util.wait_until(['compute', 'vnic-attachment', 'list', '--compartment-id', util.COMPARTMENT_ID, '--instance-id',
                                temp_instance_ocid], 'ATTACHED', max_wait_seconds=30, item_index_in_list_response=0)

        # get vnic attachments for given instance
        list_vnics_result = util.invoke_command(
            ['compute', 'vnic-attachment', 'list',
             '--compartment-id', util.COMPARTMENT_ID,
             '--instance-id', temp_instance_ocid
             ])

        vnic_id = json.loads(list_vnics_result.output)['data'][0]['vnic-id']

        # get full data for vnic attached to new instance (which includes hostname-label)
        get_vnic_result = util.invoke_command(
            ['network', 'vnic', 'get',
             '--vnic-id', vnic_id
             ])

        vnic = json.loads(get_vnic_result.output)['data']

        assert vnic['hostname-label'] == hostname_label + "1"
        assert vnic['display-name'] == vnic_display_name
        assert vnic['public-ip']

        content = None
        with open(IPXE_SCRIPT_FILE, mode='r') as file:
            content = file.read()

        assert 'ipxe-script' in launch_instance_result.output
        # Just look at the first few characters. Once we hit a line break the formatting will differ.
        assert content[:5] in launch_instance_result.output

        self.delete_instance(temp_instance_ocid)

    @util.log_test
    def subtest_launch_instance_with_assign_private_dns(self):
        instance_name = util.random_name('cli_test_instance_options_optout_dns')
        image_id = util.oracle_linux_image()
        shape = 'VM.Standard1.2'
        vnic_display_name = 'vnic_display_name'
        assign_private_dns_record = 'true'

        extended_metadata = '{"a": "1", "b": {"c": "3", "d": {}}}'

        launch_instance_result = util.invoke_command(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', instance_name,
             '--subnet-id', self.subnet_ocid,
             '--image-id', image_id,
             '--shape', shape,
             '--ipxe-script-file', IPXE_SCRIPT_FILE,
             '--assign-private-dns-record', assign_private_dns_record,
             '--vnic-display-name', vnic_display_name,
             '--extended-metadata', extended_metadata])

        temp_instance_ocid = util.find_id_in_response(launch_instance_result.output)
        self.instance_ocids.append(temp_instance_ocid)
        util.validate_response(launch_instance_result, expect_etag=True)

        extended_metadata_result = json.loads(launch_instance_result.output)['data']['extended-metadata']
        assert extended_metadata_result['a'] == '1'
        assert extended_metadata_result['b']['c'] == '3'

        # This can be in ATTACHING state for some time
        try:
            util.wait_until(
                ['compute', 'vnic-attachment', 'list', '--compartment-id', util.COMPARTMENT_ID, '--instance-id',
                 temp_instance_ocid], 'ATTACHED', max_wait_seconds=60, item_index_in_list_response=0)
        except Exception:
            try:
                # If it is ATTACHING we will consider it good enough
                util.wait_until(
                    ['compute', 'vnic-attachment', 'list', '--compartment-id', util.COMPARTMENT_ID, '--instance-id',
                     temp_instance_ocid], 'ATTACHING', max_wait_seconds=30, item_index_in_list_response=0)
            except Exception:
                # If it is not ATTACHING, double check that it didn't go to ATTACHED
                util.wait_until(
                    ['compute', 'vnic-attachment', 'list', '--compartment-id', util.COMPARTMENT_ID, '--instance-id',
                     temp_instance_ocid], 'ATTACHED', max_wait_seconds=30, item_index_in_list_response=0)

        # get vnic attachments for given instance
        list_vnics_result = util.invoke_command(
            ['compute', 'vnic-attachment', 'list',
             '--compartment-id', util.COMPARTMENT_ID,
             '--instance-id', temp_instance_ocid
             ])

        vnic_id = json.loads(list_vnics_result.output)['data'][0]['vnic-id']

        # get full data for vnic attached to new instance
        get_vnic_result = util.invoke_command(
            ['network', 'vnic', 'get',
             '--vnic-id', vnic_id
             ])

        vnic = json.loads(get_vnic_result.output)['data']

        assert vnic['display-name'] == vnic_display_name
        assert vnic['public-ip']

        content = None
        with open(IPXE_SCRIPT_FILE, mode='r') as file:
            content = file.read()

        assert 'ipxe-script' in launch_instance_result.output
        # Just look at the first few characters. Once we hit a line break the formatting will differ.
        assert content[:5] in launch_instance_result.output

        self.delete_instance(temp_instance_ocid)

    @util.log_test
    def subtest_launch_instance_ssh_authorized_keys_in_param_and_in_metadata_throws_error(self):
        instance_name = util.random_name('cli_test_instance_options')
        image_id = util.oracle_linux_image()
        shape = 'VM.Standard1.2'
        hostname_label = util.random_name('bminstance', insert_underscore=False)

        launch_instance_result = util.invoke_command(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', instance_name,
             '--subnet-id', self.subnet_ocid,
             '--image-id', image_id,
             '--shape', shape,
             '--hostname-label', hostname_label + "2",
             '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
             '--metadata', util.remove_outer_quotes(oci_cli_compute.compute_cli_extended.compute_instance_launch_metadata_example)])

        assert launch_instance_result.exit_code != 0

    @util.log_test
    def subtest_launch_instance_user_data_in_param_and_in_metadata_throws_error(self):
        instance_name = util.random_name('cli_test_instance_options')
        image_id = util.oracle_linux_image()
        shape = 'VM.Standard1.2'
        hostname_label = util.random_name('bminstance', insert_underscore=False)

        metadata = """{"user_data": "IyEvYmluL2Jhc2gKCm1rZGlyIC90bXAvbXlkaXIKdG91Y2ggL3RtcC9teWRpci9teXR4dC50eHQ="}"""

        launch_instance_result = util.invoke_command(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', instance_name,
             '--subnet-id', self.subnet_ocid,
             '--image-id', image_id,
             '--shape', shape,
             '--hostname-label', hostname_label,
             '--user-data-file', USER_DATA_FILE,
             '--metadata', metadata])

        assert launch_instance_result.exit_code != 0

    @util.log_test
    def subtest_launch_instance_user_data_file_and_ssh_authorized_users_file(self):
        instance_name = util.random_name('cli_test_instance_options')
        image_id = util.oracle_linux_image()
        shape = 'VM.Standard1.2'
        hostname_label = util.random_name('bminstance', insert_underscore=False)

        launch_instance_result = util.invoke_command(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', instance_name,
             '--subnet-id', self.subnet_ocid,
             '--image-id', image_id,
             '--shape', shape,
             '--hostname-label', hostname_label + "3",
             '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
             '--user-data-file', USER_DATA_FILE
             ])

        util.validate_response(launch_instance_result, expect_etag=True)
        temp_instance_ocid = util.find_id_in_response(launch_instance_result.output)
        self.instance_ocids.append(temp_instance_ocid)

        response = json.loads(launch_instance_result.output)
        instance_metadata = response['data']['metadata']
        assert instance_metadata['user_data']
        assert instance_metadata['ssh_authorized_keys']

        self.delete_instance(temp_instance_ocid)

    @util.log_test
    def subtest_launch_instance_merges_user_data_file_param_with_metadata(self):
        instance_name = util.random_name('cli_test_instance_options')
        image_id = util.oracle_linux_image()
        shape = 'VM.Standard1.2'
        hostname_label = util.random_name('bminstance', insert_underscore=False)

        launch_instance_result = util.invoke_command(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', instance_name,
             '--subnet-id', self.subnet_ocid,
             '--image-id', image_id,
             '--shape', shape,
             '--hostname-label', hostname_label + "4",
             '--user-data-file', USER_DATA_FILE,
             '--metadata', util.remove_outer_quotes(oci_cli_compute.compute_cli_extended.compute_instance_launch_metadata_example)])

        util.validate_response(launch_instance_result, expect_etag=True)
        temp_instance_ocid = util.find_id_in_response(launch_instance_result.output)
        self.instance_ocids.append(temp_instance_ocid)

        response = json.loads(launch_instance_result.output)
        instance_metadata = response['data']['metadata']
        assert instance_metadata['user_data']
        assert instance_metadata['ssh_authorized_keys']

        self.delete_instance(temp_instance_ocid)

    @util.log_test
    def subtest_delete(self):
        error_count = 0

        if len(self.instance_ocids) > 0:
            for ocid in self.instance_ocids:
                try:
                    print("checking TERMINATED for " + ocid)
                    util.wait_until(['compute', 'instance', 'get', '--instance-id', ocid], 'TERMINATED', max_wait_seconds=1200, succeed_if_not_found=True)
                except Exception as error:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'subnet_ocid'):
            try:
                print("Deleting subnet")
                result = util.invoke_command(['network', 'subnet', 'delete', '--subnet-id', self.subnet_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['network', 'subnet', 'get', '--subnet-id', self.subnet_ocid], 'TERMINATED',
                                max_wait_seconds=600, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'vcn_ocid'):
            try:
                print("Deleting vcn")
                result = util.invoke_command(['network', 'vcn', 'delete', '--vcn-id', self.vcn_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['network', 'vcn', 'get', '--vcn-id', self.vcn_ocid], 'TERMINATED',
                                max_wait_seconds=600, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        self.assertEquals(0, error_count)

    def delete_instance(self, instance_ocid):
        print("Deleting instance " + instance_ocid)
        util.wait_until(['compute', 'instance', 'get', '--instance-id', instance_ocid], 'RUNNING', max_wait_seconds=600, succeed_if_not_found=True)
        result = util.invoke_command(['compute', 'instance', 'terminate', '--instance-id', instance_ocid, '--force'])
        util.validate_response(result)


if __name__ == '__main__':
    unittest.main()
