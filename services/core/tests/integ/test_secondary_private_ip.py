# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import os.path
import pytest
import socket
import string
import struct
import unittest
from tests import test_config_container
from tests import util
from tests import tag_data_container

CASSETTE_LIBRARY_DIR = 'services/core/tests/cassettes'


@pytest.mark.usefixtures("tag_namespace_and_tags")
class TestSecondaryPrivateIp(unittest.TestCase):
    @util.slow
    def test_subnet_secondary_ip_operations(self):
        with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR)\
                .use_cassette('subnet_secondary_ip_operations.yml'):
            # We delegate to an internal method and have a try-catch so that we have
            # an opportunity to clean up resources after the meat of the test is over
            try:
                self.subtest_subnet_secondary_ip_operations()
                self.subtest_tagging_secondary_ip()
            finally:
                self.clean_up_resources()

    @util.slow
    def test_vlan_secondary_ip_operations(self):
        with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR)\
                .use_cassette('vlan_secondary_ip_operations.yml'):
            # We delegate to an internal method and have a try-catch so that we have
            # an opportunity to clean up resources after the meat of the test is over
            try:
                self.subtest_vlan_secondary_ip_operations()
            finally:
                self.clean_up_resources()

    def subtest_vlan_secondary_ip_operations(self):
        self.set_up_vcn_and_vlan("10.0.0.0/20")
        available_ip_addresses = self.get_ip_addresses_from_cidr("10.0.0.0/20")

        # Running the assign command against a non-existent VLAN fails
        fudged_vlan_id = self.fudge_ocid(self.vlan_ocid)
        result = self.invoke(
            ['network', 'vnic', 'assign-private-ip',
             '--vlan-id', fudged_vlan_id])
        assert 'Either Vlan with ID {} does not exist or you are not authorized to access it.'.format(fudged_vlan_id) \
               in result.output
        self.assertNotEqual(0, result.exit_code)

        # Most basic call with vlan only - in this case we assign the IP automatically
        result = self.invoke(
            ['network', 'vnic', 'assign-private-ip',
             '--vlan-id', self.vlan_ocid])
        first_secondary_private_ip_data = json.loads(result.output)['data']
        first_secondary_private_ip_id = first_secondary_private_ip_data['id']
        first_secondary_private_ip_address = first_secondary_private_ip_data['ip-address']
        available_ip_addresses.remove(first_secondary_private_ip_address)

        # Assign a new secondary IP with all parameters given
        second_secondary_private_ip_address = available_ip_addresses.pop()
        result = self.invoke(
            ['network', 'vnic', 'assign-private-ip',
             '--vlan-id', self.vlan_ocid,
             '--ip-address', second_secondary_private_ip_address,
             '--display-name', 'My second secondary',
             '--hostname-label', 'secondary-1',

             # The --unassign-if-already-assigned should not have an impact as the IP address doesn't exist
             '--unassign-if-already-assigned'])
        second_secondary_private_ip_data = json.loads(result.output)['data']
        second_secondary_private_ip_id = second_secondary_private_ip_data['id']
        self.assertEqual(second_secondary_private_ip_address, second_secondary_private_ip_data['ip-address'])

        # Checkpoint by listing the private IPs. Our created secondaries should be there
        result = self.invoke(
            ['network', 'private-ip', 'list',
             '--vlan-id', self.vlan_ocid])
        private_ips = json.loads(result.output)['data']

        self.assertEqual(2, len(private_ips))
        self.find_private_ip_and_do_assertions(private_ips, first_secondary_private_ip_id, first_secondary_private_ip_address, None, None)
        self.find_private_ip_and_do_assertions(private_ips, second_secondary_private_ip_id, second_secondary_private_ip_address, 'My second secondary', None)

        # Trying to assign the same private IP to the same VLAN is a no-op
        result = self.invoke(
            ['network', 'vnic', 'assign-private-ip',
             '--vlan-id', self.vlan_ocid,
             '--ip-address', first_secondary_private_ip_address])
        assert 'Taking no action as IP address {} is already assigned to VLAN {}'.format(first_secondary_private_ip_address, self.vlan_ocid) in result.output

        # Update the display name
        result = self.invoke(
            ['network', 'private-ip', 'update',
             '--private-ip-id', second_secondary_private_ip_id,
             '--display-name', 'Super Sonic IP'])
        updated_private_ip_info = json.loads(result.output)['data']
        self.assertEqual(second_secondary_private_ip_id, updated_private_ip_info['id'])
        self.assertEqual(second_secondary_private_ip_address, updated_private_ip_info['ip-address'])
        self.assertEqual(self.vlan_ocid, updated_private_ip_info['vlan-id'])
        self.assertEqual('Super Sonic IP', updated_private_ip_info['display-name'])

        result = self.invoke(
            ['network', 'private-ip', 'delete',
             '--private-ip-id', first_secondary_private_ip_id,
             '--force'])
        self.assertEqual(0, result.exit_code)

        result = self.invoke(
            ['network', 'private-ip', 'delete',
             '--private-ip-id', second_secondary_private_ip_id,
             '--force'])
        self.assertEqual(0, result.exit_code)

        return

    def subtest_subnet_secondary_ip_operations(self):
        self.set_up_vcn_and_subnet("10.0.0.0/16")
        available_ip_addresses = self.get_ip_addresses_from_cidr("10.0.0.0/16")

        # First we need to launch two instances and get their VNICs. We get two instances
        # so that we can move the secondary private IP around. The instances need to be
        # in the same subnet for the secondary private IP address moves to be valid
        image_id = util.oracle_linux_image()
        shape = 'VM.Standard1.1'

        first_instance_name = util.random_name('cli_test_instance')
        result = self.invoke(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', first_instance_name,
             '--subnet-id', self.subnet_ocid,
             '--image-id', image_id,
             '--shape', shape])
        self.first_instance_id = util.find_id_in_response(result.output)

        second_instance_name = util.random_name('cli_test_instance')
        result = self.invoke(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', second_instance_name,
             '--subnet-id', self.subnet_ocid,
             '--image-id', image_id,
             '--shape', shape])
        self.second_instance_id = util.find_id_in_response(result.output)

        util.wait_until(['compute', 'instance', 'get', '--instance-id', self.first_instance_id], 'RUNNING', max_wait_seconds=600)
        util.wait_until(['compute', 'instance', 'get', '--instance-id', self.second_instance_id], 'RUNNING', max_wait_seconds=600)

        vnics_on_instance_result = self.invoke(
            ['compute', 'instance', 'list-vnics',
             '--instance-id', self.first_instance_id])
        vnics = json.loads(vnics_on_instance_result.output)
        first_vnic_id = vnics['data'][0]['id']
        first_vnic_primary_private_ip = vnics['data'][0]['private-ip']

        # So we don't try and re-use the IP address unintentionally
        available_ip_addresses.remove(first_vnic_primary_private_ip)

        vnics_on_instance_result = self.invoke(
            ['compute', 'instance', 'list-vnics',
             '--instance-id', self.second_instance_id])
        vnics = json.loads(vnics_on_instance_result.output)
        second_vnic_id = vnics['data'][0]['id']
        second_vnic_primary_private_ip = vnics['data'][0]['private-ip']
        available_ip_addresses.remove(second_vnic_primary_private_ip)

        # Running the assign command against a non-existent VNIC fails
        fudged_vnic_id = self.fudge_ocid(first_vnic_id)
        result = self.invoke(
            ['network', 'vnic', 'assign-private-ip',
             '--vnic-id', fudged_vnic_id])
        self.assertNotEqual(0, result.exit_code)
        assert 'Either VNIC with ID {} does not exist or you are not authorized to access it.'.format(fudged_vnic_id) in result.output

        # Most basic call with VNIC only - in this case we assign the IP automatically
        result = self.invoke(
            ['network', 'vnic', 'assign-private-ip',
             '--vnic-id', first_vnic_id])
        first_secondary_private_ip_data = json.loads(result.output)['data']
        first_secondary_private_ip_id = first_secondary_private_ip_data['id']
        first_secondary_private_ip_address = first_secondary_private_ip_data['ip-address']
        available_ip_addresses.remove(first_secondary_private_ip_address)

        # Assign a new secondary IP with all parameters given
        second_secondary_private_ip_address = available_ip_addresses.pop()
        result = self.invoke(
            ['network', 'vnic', 'assign-private-ip',
             '--vnic-id', first_vnic_id,
             '--ip-address', second_secondary_private_ip_address,
             '--display-name', 'My second secondary',
             '--hostname-label', 'secondary-1',

             # The --unassign-if-already-assigned should not have an impact as the IP address doesn't exist
             '--unassign-if-already-assigned'])
        second_secondary_private_ip_data = json.loads(result.output)['data']
        second_secondary_private_ip_id = second_secondary_private_ip_data['id']
        self.assertEqual(second_secondary_private_ip_address, second_secondary_private_ip_data['ip-address'])

        # Checkpoint by listing the private IPs. Our created secondaries should be there
        result = self.invoke(
            ['network', 'private-ip', 'list',
             '--vnic-id', first_vnic_id])
        private_ips = json.loads(result.output)['data']

        self.assertEqual(3, len(private_ips))
        self.find_private_ip_and_do_assertions(private_ips, first_secondary_private_ip_id, first_secondary_private_ip_address, None, None)
        self.find_private_ip_and_do_assertions(private_ips, second_secondary_private_ip_id, second_secondary_private_ip_address, 'My second secondary', 'secondary-1')

        # Trying to assign the same private IP to the same VNIC is a no-op
        result = self.invoke(
            ['network', 'vnic', 'assign-private-ip',
             '--vnic-id', first_vnic_id,
             '--ip-address', first_secondary_private_ip_address])
        assert 'Taking no action as IP address {} is already assigned to VNIC {}'.format(first_secondary_private_ip_address, first_vnic_id) in result.output

        # Trying to move a primary IP fails
        result = self.invoke(
            ['network', 'vnic', 'assign-private-ip',
             '--vnic-id', first_vnic_id,
             '--ip-address', second_vnic_primary_private_ip,
             '--unassign-if-already-assigned'])
        self.assertNotEqual(0, result.exit_code)

        result = self.invoke(
            ['network', 'vnic', 'assign-private-ip',
             '--vnic-id', second_vnic_id,
             '--ip-address', first_vnic_primary_private_ip,
             '--unassign-if-already-assigned'])
        self.assertNotEqual(0, result.exit_code)

        # Trying to move an existing IP address without saying "unassign" fails
        result = self.invoke(
            ['network', 'vnic', 'assign-private-ip',
             '--vnic-id', second_vnic_id,
             '--ip-address', first_secondary_private_ip_address])
        target_message = 'IP address {} is already assigned to a different VNIC: {}. To reassign it, re-run this command with the --unassign-if-already-assigned option'.format(
            first_secondary_private_ip_address, first_vnic_id)
        assert target_message in result.output
        self.assertNotEqual(0, result.exit_code)

        # Move the secondary IP and also update some information
        result = self.invoke(
            ['network', 'vnic', 'assign-private-ip',
             '--vnic-id', second_vnic_id,
             '--ip-address', first_secondary_private_ip_address,
             '--display-name', 'My first secondary',
             '--hostname-label', 'moved-first-secondary-1',
             '--unassign-if-already-assigned'])
        private_ip_data_after_move = json.loads(result.output)['data']
        self.assertEqual(first_secondary_private_ip_id, private_ip_data_after_move['id'])
        self.assertEqual(first_secondary_private_ip_address, private_ip_data_after_move['ip-address'])
        self.assertEqual('My first secondary', private_ip_data_after_move['display-name'])
        self.assertEqual('moved-first-secondary-1', private_ip_data_after_move['hostname-label'])

        # List each VNIC - we expect 2 results per list call (1 x primary private and 1 x secondary private per VNIC) after moving stuff around
        result = self.invoke(
            ['network', 'private-ip', 'list',
             '--vnic-id', first_vnic_id])
        private_ips = json.loads(result.output)['data']
        self.assertEqual(2, len(private_ips))
        self.ensure_private_ip_record_not_present(private_ips, first_secondary_private_ip_id)
        self.find_private_ip_and_do_assertions(private_ips, second_secondary_private_ip_id, second_secondary_private_ip_address, 'My second secondary', 'secondary-1')

        result = self.invoke(
            ['network', 'private-ip', 'list',
             '--vnic-id', second_vnic_id])
        private_ips = json.loads(result.output)['data']
        self.assertEqual(2, len(private_ips))
        self.ensure_private_ip_record_not_present(private_ips, second_secondary_private_ip_id)
        self.find_private_ip_and_do_assertions(private_ips, first_secondary_private_ip_id, first_secondary_private_ip_address, 'My first secondary', 'moved-first-secondary-1')

        # Listing by subnet should give us 4 records (2 x primary private and 2 x secondary private) as it queries across all VNICs in the subnet
        result = self.invoke(
            ['network', 'private-ip', 'list',
             '--subnet-id', self.subnet_ocid])
        private_ips = json.loads(result.output)['data']
        self.assertEqual(4, len(private_ips))
        self.find_private_ip_and_do_assertions(private_ips, first_secondary_private_ip_id, first_secondary_private_ip_address, 'My first secondary', 'moved-first-secondary-1')
        self.find_private_ip_and_do_assertions(private_ips, second_secondary_private_ip_id, second_secondary_private_ip_address, 'My second secondary', 'secondary-1')

        # Update the display name and hostname
        result = self.invoke(
            ['network', 'private-ip', 'update',
             '--private-ip-id', second_secondary_private_ip_id,
             '--display-name', 'batman display name',
             '--hostname-label', 'batman-secondary-1'])
        updated_private_ip_info = json.loads(result.output)['data']
        self.assertEqual(second_secondary_private_ip_id, updated_private_ip_info['id'])
        self.assertEqual(second_secondary_private_ip_address, updated_private_ip_info['ip-address'])
        self.assertEqual(first_vnic_id, updated_private_ip_info['vnic-id'])
        self.assertEqual('batman display name', updated_private_ip_info['display-name'])
        self.assertEqual('batman-secondary-1', updated_private_ip_info['hostname-label'])

        # Do a get and confirm the information which we receive
        result = self.invoke(
            ['network', 'private-ip', 'get',
             '--private-ip-id', second_secondary_private_ip_id])
        private_ip_info_from_get = json.loads(result.output)['data']
        self.assertEqual(second_secondary_private_ip_id, private_ip_info_from_get['id'])
        self.assertEqual(second_secondary_private_ip_address, private_ip_info_from_get['ip-address'])
        self.assertEqual(first_vnic_id, private_ip_info_from_get['vnic-id'])
        self.assertEqual('batman display name', private_ip_info_from_get['display-name'])
        self.assertEqual('batman-secondary-1', private_ip_info_from_get['hostname-label'])

        # Running the unassign command against a non-existent VNIC fails
        # Listing by VNIC should give us one record (the primary private IP) per call
        result = self.invoke(
            ['network', 'vnic', 'unassign-private-ip',
             '--vnic-id', fudged_vnic_id,
             '--ip-address', second_secondary_private_ip_address])
        self.assertNotEqual(0, result.exit_code)
        # The error message from the service is not being sent correctly to the CLI. The Error code is correct.
        # This needs to be investigated
        # assert 'Either VNIC with ID {} does not exist or you are not authorized to access it.'.format(fudged_vnic_id) in result.output

        # Unassigning an IP address not in the VNIC fails
        result = self.invoke(
            ['network', 'vnic', 'unassign-private-ip',
             '--vnic-id', second_vnic_id,
             '--ip-address', second_secondary_private_ip_address])
        assert 'IP address {} was not found on VNIC {}'.format(second_secondary_private_ip_address, second_vnic_id) in result.output
        self.assertNotEqual(0, result.exit_code)

        # Unassigning a primary private IP address is not supported
        result = self.invoke(
            ['network', 'vnic', 'unassign-private-ip',
             '--vnic-id', second_vnic_id,
             '--ip-address', second_vnic_primary_private_ip])
        assert 'Taking no action as {} is the primary private IP on VNIC {}'.format(second_vnic_primary_private_ip, second_vnic_id) in result.output
        self.assertNotEqual(0, result.exit_code)

        # Unassign a secondary private IP
        result = self.invoke(
            ['network', 'vnic', 'unassign-private-ip',
             '--vnic-id', second_vnic_id,
             '--ip-address', first_secondary_private_ip_address])
        assert 'Unassigned IP address {} from VNIC {}'.format(first_secondary_private_ip_address, second_vnic_id) in result.output

        # Delete a secondary private IP (by its OCID)
        result = self.invoke(
            ['network', 'private-ip', 'delete',
             '--private-ip-id', second_secondary_private_ip_id,
             '--force'])
        self.assertEqual(0, result.exit_code)

        # Listing by VNIC should give us one record (the primary private IP) per call
        result = self.invoke(
            ['network', 'private-ip', 'list',
             '--vnic-id', first_vnic_id])
        private_ips = json.loads(result.output)['data']
        self.assertEqual(1, len(private_ips))
        self.assertTrue(private_ips[0]['is-primary'])

        result = self.invoke(
            ['network', 'private-ip', 'list',
             '--vnic-id', second_vnic_id])
        private_ips = json.loads(result.output)['data']
        self.assertEqual(1, len(private_ips))
        self.assertTrue(private_ips[0]['is-primary'])

        # Listing by subnet should give us two records (the primary private IP for each VNIC)
        result = self.invoke(
            ['network', 'private-ip', 'list',
             '--subnet-id', self.subnet_ocid])
        private_ips = json.loads(result.output)['data']
        self.assertEqual(2, len(private_ips))
        self.assertTrue(private_ips[0]['is-primary'])
        self.assertTrue(private_ips[1]['is-primary'])

    def subtest_tagging_secondary_ip(self):
        vnics_on_instance_result = self.invoke(
            ['compute', 'instance', 'list-vnics',
             '--instance-id', self.second_instance_id])
        vnics = json.loads(vnics_on_instance_result.output)
        vnic_id = vnics['data'][0]['id']

        tag_names_to_values = {}
        for t in tag_data_container.tags:
            tag_names_to_values[t.name] = 'somevalue {}'.format(t.name)
        tag_data_container.write_defined_tags_to_file(
            os.path.join('tests', 'temp', 'defined_tags_ip.json'),
            tag_data_container.tag_namespace,
            tag_names_to_values
        )

        # We can set tags on assignment
        result = self.invoke([
            'network', 'vnic', 'assign-private-ip',
            '--vnic-id', vnic_id,
            '--freeform-tags', 'file://tests/resources/tagging/freeform_tags_1.json',
            '--defined-tags', 'file://tests/temp/defined_tags_ip.json'
        ])
        private_ip_data = json.loads(result.output)['data']
        expected_freeform = {'tagOne': 'value1', 'tag_Two': 'value two'}
        expected_defined = {tag_data_container.tag_namespace.name: tag_names_to_values}
        self.assertEqual(expected_freeform, private_ip_data['freeform-tags'])
        self.assertEqual(expected_defined, private_ip_data['defined-tags'])

        result = self.invoke([
            'network', 'private-ip', 'get',
            '--private-ip-id', private_ip_data['id']
        ])
        private_ip_info_from_get = json.loads(result.output)['data']
        self.assertEqual(expected_freeform, private_ip_info_from_get['freeform-tags'])
        self.assertEqual(expected_defined, private_ip_info_from_get['defined-tags'])

        tag_names_to_values = {}
        for t in tag_data_container.tags:
            tag_names_to_values[t.name] = 'somevalue2 {}'.format(t.name)
        tag_data_container.write_defined_tags_to_file(
            os.path.join('tests', 'temp', 'defined_tags_2.json'),
            tag_data_container.tag_namespace,
            tag_names_to_values
        )

        # We can overwrite tags on update
        result = self.invoke([
            'network', 'private-ip', 'update',
            '--private-ip-id', private_ip_data['id'],
            '--freeform-tags', 'file://tests/resources/tagging/freeform_tags_2.json',
            '--defined-tags', 'file://tests/temp/defined_tags_2.json',
            '--force'
        ])
        private_ip_data = json.loads(result.output)['data']
        expected_freeform = {'tagOne': 'value three'}
        expected_defined = {tag_data_container.tag_namespace.name: tag_names_to_values}
        self.assertEqual(expected_freeform, private_ip_data['freeform-tags'])
        self.assertEqual(expected_defined, private_ip_data['defined-tags'])

        result = self.invoke([
            'network', 'private-ip', 'get',
            '--private-ip-id', private_ip_data['id']
        ])
        private_ip_info_from_get = json.loads(result.output)['data']
        self.assertEqual(expected_freeform, private_ip_info_from_get['freeform-tags'])
        self.assertEqual(expected_defined, private_ip_info_from_get['defined-tags'])

        # We can nuke tags by providing an empty JSON object
        result = self.invoke([
            'network', 'private-ip', 'update',
            '--private-ip-id', private_ip_data['id'],
            '--freeform-tags', '{}',
            '--defined-tags', '{}',
            '--force'
        ])
        private_ip_data = json.loads(result.output)['data']
        self.assertEqual({}, private_ip_data['freeform-tags'])
        self.assertEqual({}, private_ip_data['defined-tags'])

        result = self.invoke([
            'network', 'private-ip', 'get',
            '--private-ip-id', private_ip_data['id']
        ])
        private_ip_info_from_get = json.loads(result.output)['data']
        self.assertEqual({}, private_ip_info_from_get['freeform-tags'])
        self.assertEqual({}, private_ip_info_from_get['defined-tags'])

        result = self.invoke([
            'network', 'private-ip', 'delete',
            '--private-ip-id', private_ip_data['id'],
            '--force'
        ])
        self.assertEqual(0, result.exit_code)

    def clean_up_resources(self):
        error_count = 0

        if hasattr(self, 'first_instance_id'):
            try:
                print("Deleting instance " + self.first_instance_id)
                result = self.invoke(['compute', 'instance', 'terminate', '--instance-id', self.first_instance_id, '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'second_instance_id'):
            try:
                print("Deleting instance " + self.second_instance_id)
                result = self.invoke(['compute', 'instance', 'terminate', '--instance-id', self.second_instance_id, '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'first_instance_id'):
            try:
                print("Checking instance terminated " + self.first_instance_id)
                util.wait_until(['compute', 'instance', 'get', '--instance-id', self.first_instance_id], 'TERMINATED',
                                max_wait_seconds=1200, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'second_instance_id'):
            try:
                print("Checking instance terminated " + self.second_instance_id)
                util.wait_until(['compute', 'instance', 'get', '--instance-id', self.second_instance_id], 'TERMINATED',
                                max_wait_seconds=1200, succeed_if_not_found=True)
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

        if hasattr(self, 'vlan_ocid'):
            try:
                print("Deleting vlan")
                result = self.invoke(['network', 'vlan', 'delete', '--vlan-id', self.vlan_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['network', 'vlan', 'get', '--vlan-id', self.vlan_ocid], 'TERMINATED',
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

    def set_up_vcn_and_subnet(self, cidr_block):
        # Create a VCN
        vcn_name = util.random_name('cli_test_compute_vcn')

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

    def set_up_vcn_and_vlan(self, cidr_block):
        # Create a VCN
        vcn_name = util.random_name('cli_test_compute_vcn')

        result = self.invoke(
            ['network', 'vcn', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--display-name', vcn_name,
             '--dns-label', 'clivcn',
             '--cidr-block', cidr_block])
        util.validate_response(result, expect_etag=True)
        self.vcn_ocid = util.find_id_in_response(result.output)
        util.wait_until(['network', 'vcn', 'get', '--vcn-id', self.vcn_ocid], 'AVAILABLE',
                        max_wait_seconds=300)
        # Create a vlan
        vlan_name = util.random_name('cli_test_compute_vlan')

        result = self.invoke(
            ['network', 'vlan', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', vlan_name,
             '--vcn-id', self.vcn_ocid,
             '--cidr-block', cidr_block,
             ])
        util.validate_response(result, expect_etag=True)
        self.vlan_ocid = util.find_id_in_response(result.output)
        util.wait_until(['network', 'vlan', 'get', '--vlan-id', self.vlan_ocid], 'AVAILABLE',
                        max_wait_seconds=300)

    def find_private_ip_and_do_assertions(self, private_ips, target_private_ip_ocid, ip_address, display_name, hostname_label):
        for private_ip in private_ips:
            if private_ip['id'] == target_private_ip_ocid:
                self.assertEqual(ip_address, private_ip['ip-address'])

                # display_name is auto-set if we don't provide one. However, for
                # hostname_label if we don't provide one it will be None
                self.assertIsNotNone(private_ip['display-name'])
                if display_name is not None:
                    self.assertEqual(display_name, private_ip['display-name'])

                if hostname_label is None:
                    self.assertIsNone(private_ip['hostname-label'])
                else:
                    self.assertEqual(hostname_label, private_ip['hostname-label'])
                break
        else:
            self.fail('Private IP record {} not found'.format(target_private_ip_ocid))

    def ensure_private_ip_record_not_present(self, private_ips, target_private_ip_ocid):
        for private_ip in private_ips:
            if private_ip['id'] == target_private_ip_ocid:
                self.fail('Expected {} to not be in the list of private IPs'.format(target_private_ip_ocid))

    # Fudges an OCID by flipping its last character to something different than what it currently is
    def fudge_ocid(self, ocid):
        available_characters = list(string.ascii_lowercase) + list(string.digits)
        available_characters.remove('0')
        available_characters.remove('1')
        available_characters.remove('8')
        available_characters.remove('9')

        ocid_as_list = list(ocid)
        last_char = ocid_as_list[-1]

        available_characters.remove(last_char)
        ocid_as_list[-1] = available_characters.pop()

        return ''.join(ocid_as_list)

    # This will return us the set of all valid addresses for the given CIDR. This is to ensure that
    # we don't unintentionally collide addresses when doing our secondary IP address operations
    def get_ip_addresses_from_cidr(self, cidr_string):
        (ip, cidr) = cidr_string.split('/')
        cidr = int(cidr)
        host_bits = 32 - cidr
        i = struct.unpack('>I', socket.inet_aton(ip))[0]
        start = (i >> host_bits) << host_bits
        end = i | ((1 << host_bits) - 1)

        ip_addresses = set()
        for i in range(start, end):
            ip_addresses.add(socket.inet_ntoa(struct.pack('>I', i)))

        return sorted(list(ip_addresses))

    def invoke(self, commands, debug=False, ** args):
        if debug is True:
            commands = ['--debug'] + commands

        return util.invoke_command(commands, ** args)
