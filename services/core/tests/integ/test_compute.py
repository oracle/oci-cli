# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import os
import pytest
import re
import unittest
from tests import tag_data_container
from tests import test_config_container
from tests import util
import services.core.src.oci_cli_compute as oci_cli_compute

CASSETTE_LIBRARY_DIR = 'services/core/tests/cassettes'
CONSOLE_HISTORY_FILENAME = 'tests/output/console_history_output.txt'


@pytest.mark.usefixtures("tag_namespace_and_tags")
class TestCompute(unittest.TestCase):

    @util.slow
    @test_config_container.RecordReplay('compute', cassette_library_dir=CASSETTE_LIBRARY_DIR)
    def test_all_operations(self):
        """Successfully calls every operation with basic options.  The exceptions are the image import and export
        commands as they are handled by test_image_import_export.py
        """
        try:
            self.subtest_setup()
            self.subtest_instance_operations()
            self.subtest_list_vnics()
            self.subtest_vnic_operations()
            self.subtest_public_ip_operations()
            self.subtest_volume_attachment_operations()
            self.subtest_shape_operations()
            self.subtest_console_history_operations()
            self.subtest_instance_console_connections()
            self.subtest_instance_console_connections_tagging()
            # TODO: afbrock to fix (dexreq 3682)
            # self.subtest_instance_action_operations()
            self.subtest_image_operations()
            self.subtest_delete_instance()
            self.subtest_windows_instance_operations()
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
             '--availability-domain', util.availability_domain(),
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
        result = self.invoke(['bv', 'volume', 'create', '--availability-domain', util.availability_domain(), '--compartment-id',
                              util.COMPARTMENT_ID, '--display-name', volume_name])
        util.validate_response(result)
        self.volume_ocid = util.find_id_in_response(result.output)
        util.wait_until(['bv', 'volume', 'get', '--volume-id', self.volume_ocid], 'AVAILABLE', max_wait_seconds=180)

    @util.log_test
    def subtest_instance_operations(self):
        instance_name = util.random_name('cli_test_instance')
        fault_domain = 'FAULT-DOMAIN-1'
        image_id = util.oracle_linux_image()
        shape = 'VM.Standard1.1'

        result = self.invoke(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', instance_name,
             '--fault-domain', fault_domain,
             '--subnet-id', self.subnet_ocid,
             '--image-id', image_id,
             '--shape', shape,
             '--metadata', util.remove_outer_quotes(oci_cli_compute.compute_cli_extended.compute_instance_launch_metadata_example)])
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

        result = self.invoke(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', instance_name + "_2",
             '--fault-domain', fault_domain,
             '--subnet-id', self.subnet_ocid,
             '--image-id', image_id,
             '--shape', shape,
             '--metadata',
             util.remove_outer_quotes(oci_cli_compute.compute_cli_extended.compute_instance_launch_metadata_example),
             '--wait-for-state', 'RUNNING',
             '--max-wait-seconds', '20',
             '--wait-interval-seconds', '5'])
        self.instance_ocid_2 = util.find_id_in_response(result.output[result.output.index('{'):])
        assert result.exit_code != 0

    @util.log_test
    def subtest_windows_instance_operations(self):
        instance_name = util.random_name('cli_test_instance')
        image_id = util.windows_vm_image()
        shape = 'VM.Standard1.1'

        result = self.invoke(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
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

        result = self.invoke(
            ['compute', 'instance', 'terminate', '--instance-id', self.windows_instance_ocid, '--force'])
        util.validate_response(result)

    @util.log_test
    def subtest_list_vnics(self):
        result = self.invoke(['compute', 'instance', 'list-vnics', '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)
        json_data = json.loads(result.output)
        assert (len(json_data['data']) > 0)

        # Check that the command works with the --availability-domain option
        result = self.invoke(['compute', 'instance', 'list-vnics', '--compartment-id', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain()])
        util.validate_response(result)
        json_data = json.loads(result.output)
        assert (len(json_data['data']) > 0)

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

        # Grab all the things
        result = self.invoke(['compute', 'instance', 'list-vnics', '--instance-id', self.instance_ocid, '--all'])
        util.validate_response(result)
        json_data = json.loads(result.output)
        assert ('data' not in json_data or len(json_data['data']) == 1)
        assert ('opc-next-page' not in json_data)

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

        # Attach a new vnic with --wait and all params set.
        vnic_display_name = 'mysecondvnic'
        vnic_hostname_label = 'myotherhostname'
        vnic_private_ip = '10.0.0.121'
        result = self.invoke(
            ['compute', 'instance', 'attach-vnic', '--instance-id', self.instance_ocid, '--subnet-id', self.subnet_ocid,
             '--vnic-display-name', vnic_display_name, '--assign-public-ip', 'false', '--private-ip', vnic_private_ip,
             '--hostname-label', vnic_hostname_label, '--nic-index', '0', '--wait'])
        util.validate_response(result)
        second_vnic = json.loads(result.output)['data']
        second_vnic_id = second_vnic['id']

        # Ensure that all properties set in attach-vnic were set.
        result = self.invoke(
            ['network', 'vnic', 'get', '--vnic-id', second_vnic_id])
        util.validate_response(result)
        second_vnic = json.loads(result.output)['data']
        self.assertEquals(vnic_hostname_label, second_vnic['hostname-label'])
        self.assertEquals(vnic_private_ip, second_vnic['private-ip'])
        self.assertEquals(vnic_display_name, second_vnic['display-name'])
        self.assertEquals(None, second_vnic['public-ip'])

        # Some extra time is needed after VNIC CRUD operations for state to stabilize.
        util.vcr_mode_aware_sleep(5)

        # Ensure that new attachments are listed.
        result = self.invoke(
            ['compute', 'vnic-attachment', 'list', '--compartment-id', util.COMPARTMENT_ID, '--instance-id',
             self.instance_ocid])
        util.validate_response(result)
        json_data = json.loads(result.output)
        self.assertEquals(2, len(json_data['data']))

        # Update vnic
        result = self.invoke(
            ['network', 'vnic', 'update', '--vnic-id', second_vnic_id, '--display-name', 'newdisplayname', '--hostname-label', 'newhostnamelabel'])
        util.validate_response(result)

        # Get the secondary attachment ID
        result = self.invoke(['compute', 'vnic-attachment', 'list', '--compartment-id', util.COMPARTMENT_ID, '--vnic-id', second_vnic_id])
        util.validate_response(result)
        json_data = json.loads(result.output)
        self.assertEquals(1, len(json_data['data']))
        second_vnic_attachment_id = json_data['data'][0]['id']

        result = self.invoke(['compute', 'vnic-attachment', 'get', '--vnic-attachment-id', second_vnic_attachment_id])
        util.validate_response(result)

        util.vcr_mode_aware_sleep(10)

        # Detach vnic
        result = self.invoke(
            ['compute', 'instance', 'detach-vnic', '--vnic-id', second_vnic_id, '--compartment-id', util.COMPARTMENT_ID, '--force'])
        util.validate_response(result)
        util.wait_until(['compute', 'vnic-attachment', 'get', '--vnic-attachment-id', second_vnic_attachment_id], 'DETACHED', max_wait_seconds=300, succeed_if_not_found=True)

        util.vcr_mode_aware_sleep(10)

    @util.log_test
    def subtest_public_ip_operations(self):
        # Attach a new vnic
        vnic_display_name = 'myfloatingipvnic'
        vnic_private_ip = '10.0.0.200'
        result = self.invoke(
            ['compute', 'instance', 'attach-vnic', '--instance-id', self.instance_ocid, '--subnet-id', self.subnet_ocid,
             '--vnic-display-name', vnic_display_name, '--assign-public-ip', 'true', '--private-ip', vnic_private_ip,
             '--wait'])
        util.validate_response(result)
        second_vnic = json.loads(result.output)['data']
        second_vnic_id = second_vnic['id']

        # Extract the properties of the new secondary vnic.
        result = self.invoke(
            ['network', 'vnic', 'get', '--vnic-id', second_vnic_id])
        util.validate_response(result)
        second_vnic = json.loads(result.output)['data']
        vnic_resp_private_ip = second_vnic['private-ip']
        vnic_resp_public_ip = second_vnic['public-ip']
        self.assertEquals(vnic_private_ip, vnic_resp_private_ip)
        self.assertNotEquals(None, vnic_resp_public_ip)

        # Some extra time is needed after VNIC operations for state to stabilize.
        util.vcr_mode_aware_sleep(5)

        # Verify the public IP operations. Verify that each get below returns the same values for
        # public-ip-address, public-ip-id and private-ip-id since it is for the same public IP object
        # 1. get --public-ip-address
        result = self.invoke(['network', 'public-ip', 'get',
                              '--public-ip-address', vnic_resp_public_ip])
        util.validate_response(result)
        public_ip_obj = json.loads(result.output)['data']
        resp_public_ip_id = public_ip_obj['id']
        resp_private_ip_id = public_ip_obj['private-ip-id']
        resp_public_ip_addr = public_ip_obj['ip-address']
        self.assertEquals(vnic_resp_public_ip, resp_public_ip_addr)

        # 2. get --public-ip-id
        result = self.invoke(['network', 'public-ip', 'get',
                              '--public-ip-id', resp_public_ip_id])
        util.validate_response(result)
        public_ip_obj = json.loads(result.output)['data']
        resp_private_ip_id_2 = public_ip_obj['private-ip-id']
        resp_public_ip_addr_2 = public_ip_obj['ip-address']
        self.assertEquals(resp_private_ip_id, resp_private_ip_id_2)
        self.assertEquals(resp_public_ip_addr, resp_public_ip_addr_2)

        # 3. get --private-ip-id
        result = self.invoke(['network', 'public-ip', 'get',
                              '--private-ip-id', resp_private_ip_id])
        util.validate_response(result)
        public_ip_obj = json.loads(result.output)['data']
        resp_public_ip_id_3 = public_ip_obj['id']
        resp_public_ip_addr_3 = public_ip_obj['ip-address']
        self.assertEquals(resp_public_ip_id, resp_public_ip_id_3)
        self.assertEquals(resp_public_ip_addr, resp_public_ip_addr_3)

        # Get the secondary attachment ID
        result = self.invoke(['compute', 'vnic-attachment', 'list', '--compartment-id', util.COMPARTMENT_ID, '--vnic-id', second_vnic_id])
        util.validate_response(result)
        json_data = json.loads(result.output)
        self.assertEquals(1, len(json_data['data']))
        second_vnic_attachment_id = json_data['data'][0]['id']

        # Detach vnic
        result = self.invoke(
            ['compute', 'instance', 'detach-vnic', '--vnic-id', second_vnic_id, '--compartment-id', util.COMPARTMENT_ID, '--force'])
        util.validate_response(result)
        util.wait_until(['compute', 'vnic-attachment', 'get', '--vnic-attachment-id', second_vnic_attachment_id], 'DETACHED', max_wait_seconds=300, succeed_if_not_found=True)

        util.vcr_mode_aware_sleep(10)

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

        result = self.invoke(['compute', 'volume-attachment', 'list', '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)

        result = self.invoke(['compute', 'volume-attachment', 'list', '--instance-id', self.instance_ocid])
        util.validate_response(result)

        result = self.invoke(['compute', 'volume-attachment', 'get', '--volume-attachment-id', self.va_ocid])
        util.validate_response(result, expect_etag=True)

        result = self.invoke(['compute', 'volume-attachment', 'detach', '--volume-attachment-id', self.va_ocid, '--force'])
        util.validate_response(result)
        util.wait_until(['compute', 'volume-attachment', 'get', '--volume-attachment-id', self.va_ocid],
                        'DETACHED', max_wait_seconds=300)

        result = self.invoke(
            ['compute', 'volume-attachment', 'attach',
             '--display-name', va_name,
             '--type', 'iscsi',
             '--instance-id', self.instance_ocid,
             '--volume-id', self.volume_ocid,
             '--wait-for-state', 'ATTACHED',
             '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS])
        util.validate_response(result, expect_etag=True, json_response_expected=False)
        self.va_ocid = util.get_json_from_mixed_string(result.output)['data']['id']

        result = self.invoke([
            'compute', 'volume-attachment', 'detach',
            '--volume-attachment-id', self.va_ocid,
            '--force',
            '--wait-for-state', 'DETACHED',
            '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS
        ])
        util.validate_response(result, json_response_expected=False)

    @util.log_test
    def subtest_shape_operations(self):
        result = self.invoke(
            ['compute', 'shape', 'list', '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)

    @util.log_test
    def subtest_console_history_operations(self):
        result = self.invoke(['compute', 'console-history', 'capture', '--instance-id', self.instance_ocid, '--display-name', 'Original'])
        parsed_result = json.loads(result.output)
        self.assertEquals('Original', parsed_result['data']['display-name'])

        self.ch_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)
        util.wait_until(['compute', 'console-history', 'get', '--instance-console-history-id', self.ch_ocid], 'SUCCEEDED', max_wait_seconds=300)

        result = self.invoke(['compute', 'console-history', 'update', '--instance-console-history-id', self.ch_ocid, '--display-name', 'Updated'])
        parsed_result = json.loads(result.output)
        self.assertEquals('Updated', parsed_result['data']['display-name'])

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
        util.vcr_mode_aware_sleep(10)
        util.wait_until(['compute', 'instance', 'get', '--instance-id', self.instance_ocid], 'RUNNING',
                        max_wait_seconds=300)
        util.vcr_mode_aware_sleep(5)

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
    def subtest_instance_console_connections(self):
        result = self.invoke(['compute', 'instance-console-connection', 'create', '--instance-id', self.instance_ocid, '--ssh-public-key-file', util.SSH_AUTHORIZED_KEYS_FILE])
        util.validate_response(result)

        instance_console_connection_details = json.loads(result.output)
        self.assertIsNotNone(instance_console_connection_details['data']['connection-string'])
        self.assertIsNotNone(instance_console_connection_details['data']['id'])
        self.assertIsNotNone(instance_console_connection_details['data']['lifecycle-state'])
        self.assertEquals(self.instance_ocid, instance_console_connection_details['data']['instance-id'])
        self.assertIsNotNone(instance_console_connection_details['data']['fingerprint'])

        result = self.invoke(['compute', 'instance-console-connection', 'get', '--instance-console-connection-id', instance_console_connection_details['data']['id']])
        parsed_result = json.loads(result.output)
        self.assertEquals(instance_console_connection_details['data']['id'], parsed_result['data']['id'])
        self.assertEquals(instance_console_connection_details['data']['instance-id'], parsed_result['data']['instance-id'])
        self.assertEquals(instance_console_connection_details['data']['fingerprint'], parsed_result['data']['fingerprint'])
        self.assertEquals(instance_console_connection_details['data']['compartment-id'], parsed_result['data']['compartment-id'])
        self.assertEquals(instance_console_connection_details['data']['connection-string'], parsed_result['data']['connection-string'])
        self.assertEquals({}, instance_console_connection_details['data']['freeform-tags'])
        self.assertEquals({}, instance_console_connection_details['data']['defined-tags'])
        self.assertIsNotNone(parsed_result['data']['lifecycle-state'])

        private_key_file = 'C:\\Users\\oci\console.ppk'  # noqa: W605
        params = [
            'compute', 'instance-console-connection', 'get-plink-connection-string',
            '--instance-console-connection-id', instance_console_connection_details['data']['id'],
            '--private-key-file', private_key_file
        ]

        result = self.invoke(params)

        util.validate_response(result, json_response_expected=False)

        m = re.search(oci_cli_compute.compute_cli_extended.INSTANCE_CONSOLE_CONNECTION_STRING_INTERMEDIATE_HOST_REGEX, instance_console_connection_details['data']['connection-string'])
        intermediate_host = m.group(0)

        connection_template = 'Start-Job {{echo N | plink -ssh -N -i "{3}" -P 443 -l {1} {2} -L 5905:{0}:5905}}; sleep 5 ; plink -L 5900:localhost:5900 localhost -P 5905 -N -i "{3}" -l {1}'
        expected_plink_connection_string = connection_template.format(instance_console_connection_details['data']['instance-id'], instance_console_connection_details['data']['id'], intermediate_host, private_key_file)
        assert expected_plink_connection_string == result.output.strip()

        # confirm that error from internal call to GetConsoleConnection returns service error and non-zero status code
        params = [
            'compute', 'instance-console-connection', 'get-plink-connection-string',
            '--instance-console-connection-id', 'fake-instance-console-connection-id',
            '--private-key-file', private_key_file
        ]

        result = self.invoke(params)
        util.validate_service_error(result, error_message='ServiceError')

        keep_paginating = True
        next_page = None
        all_connections = []
        while keep_paginating:
            if next_page:
                result = self.invoke(['compute', 'instance-console-connection', 'list', '--compartment-id', util.COMPARTMENT_ID, '--page', next_page])
            else:
                result = self.invoke(['compute', 'instance-console-connection', 'list', '--compartment-id', util.COMPARTMENT_ID])

            if result.output:
                parsed_result = json.loads(result.output)
                all_connections.extend(parsed_result['data'])
                if 'opc-next-page' in parsed_result:
                    next_page = parsed_result['opc-next-page']
                    keep_paginating = next_page is not None
                else:
                    keep_paginating = False
            else:
                keep_paginating = False

        match_found = False
        for conn in all_connections:
            if conn['id'] == instance_console_connection_details['data']['id']:
                match_found = True
                self.assertEquals(instance_console_connection_details['data']['instance-id'], conn['instance-id'])
                self.assertEquals(instance_console_connection_details['data']['fingerprint'], conn['fingerprint'])
                self.assertEquals(instance_console_connection_details['data']['compartment-id'], conn['compartment-id'])
                self.assertEquals(instance_console_connection_details['data']['connection-string'], conn['connection-string'])
                self.assertIsNotNone(conn['lifecycle-state'])
                break

        self.assertTrue(match_found)

        self.invoke(['compute', 'instance-console-connection', 'delete', '--instance-console-connection-id', instance_console_connection_details['data']['id'], '--force'])

        result = self.invoke(['compute', 'instance-console-connection', 'get', '--instance-console-connection-id', instance_console_connection_details['data']['id']])
        parsed_result = json.loads(result.output)
        if 'DELET' not in parsed_result['data']['lifecycle-state']:
            print("parsed_result=" + str(parsed_result) + ", lifecycle-state=" + str(parsed_result['data']['lifecycle-state']))
            util.vcr_mode_aware_sleep(60)
            result = self.invoke(['compute', 'instance-console-connection', 'get', '--instance-console-connection-id', instance_console_connection_details['data']['id']])
            parsed_result = json.loads(result.output)
        self.assertTrue(parsed_result['data']['lifecycle-state'] == 'DELETED' or parsed_result['data']['lifecycle-state'] == 'DELETING')

    @util.log_test
    def subtest_instance_console_connections_tagging(self):
        tag_names_to_values = {}
        for t in tag_data_container.tags:
            tag_names_to_values[t.name] = 'somevalue {}'.format(t.name)
        tag_data_container.write_defined_tags_to_file(
            os.path.join('tests', 'temp', 'defined_tags_compute.json'),
            tag_data_container.tag_namespace,
            tag_names_to_values
        )

        result = self.invoke([
            'compute', 'instance-console-connection', 'create',
            '--instance-id', self.instance_ocid,
            '--ssh-public-key-file', util.SSH_AUTHORIZED_KEYS_FILE,
            '--freeform-tags', 'file://tests/resources/tagging/freeform_tags_1.json',
            '--defined-tags', 'file://tests/temp/defined_tags_compute.json'
        ])
        util.validate_response(result)
        instance_console_connection_details = json.loads(result.output)
        expected_freeform = {'tagOne': 'value1', 'tag_Two': 'value two'}
        expected_defined = {tag_data_container.tag_namespace.name: tag_names_to_values}
        self.assertEquals(expected_freeform, instance_console_connection_details['data']['freeform-tags'])
        self.assertEquals(expected_defined, instance_console_connection_details['data']['defined-tags'])

        self.invoke(['compute', 'instance-console-connection', 'delete', '--instance-console-connection-id', instance_console_connection_details['data']['id'], '--force'])
        result = self.invoke(['compute', 'instance-console-connection', 'get', '--instance-console-connection-id', instance_console_connection_details['data']['id']])
        parsed_result = json.loads(result.output)
        if 'DELET' not in parsed_result['data']['lifecycle-state']:
            print("parsed_result=" + str(parsed_result) + ", lifecycle-state=" + str(parsed_result['data']['lifecycle-state']))
            util.vcr_mode_aware_sleep(60)
            result = self.invoke(['compute', 'instance-console-connection', 'get', '--instance-console-connection-id', instance_console_connection_details['data']['id']])
            parsed_result = json.loads(result.output)
        self.assertTrue(parsed_result['data']['lifecycle-state'] == 'DELETED' or parsed_result['data']['lifecycle-state'] == 'DELETING')

    # This was pulled-out separately b/c it has been taking so darn long
    @util.log_test
    def subtest_delete_instance(self):
        if hasattr(self, 'instance_ocid'):
            print("Deleting instance " + self.instance_ocid)
            result = self.invoke(['compute', 'instance', 'terminate', '--instance-id', self.instance_ocid, '--force'])
            util.validate_response(result)
        if hasattr(self, 'instance_ocid_2'):
            print("Deleting instance " + self.instance_ocid_2)
            result = self.invoke(['compute', 'instance', 'terminate', '--instance-id', self.instance_ocid_2, '--force'])
            util.validate_response(result)

    @util.log_test
    def subtest_delete(self):
        error_count = 0
        if hasattr(self, 'image_ocid'):
            try:
                print("Deleting image")
                result = self.invoke(['compute', 'image', 'delete', '--image-id', self.image_ocid, '--force'])
                util.validate_response(result)
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
                print("Checking instance terminated " + self.instance_ocid)
                util.wait_until(['compute', 'instance', 'get', '--instance-id', self.instance_ocid], 'TERMINATED',
                                max_wait_seconds=1200, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'instance_ocid_2'):
            try:
                print("Checking instance 2 terminated " + self.instance_ocid_2)
                util.wait_until(['compute', 'instance', 'get', '--instance-id', self.instance_ocid_2], 'TERMINATED',
                                max_wait_seconds=1200, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'windows_instance_ocid'):
            try:
                print("Checking windows instance terminated " + self.windows_instance_ocid)
                util.wait_until(['compute', 'instance', 'get', '--instance-id', self.windows_instance_ocid],
                                'TERMINATED',
                                max_wait_seconds=1200, succeed_if_not_found=True)
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
        if debug is True:
            commands = ['--debug'] + commands

        return util.invoke_command(commands, ** args)


if __name__ == '__main__':
    unittest.main()
