# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import unittest
from tests import test_config_container
from tests import util
import time

CASSETTE_LIBRARY_DIR = 'services/core/tests/cassettes'


class TestVnicSkipSourceDest(unittest.TestCase):

    @util.slow
    def test_vnic_skip_source_dest(self):
        with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('vnic_skip_source_dest.yml'):
            try:
                self.set_up_resources()
                self.subtest_do_source_dest_operations()
            finally:
                self.clean_up_resources()

    @util.log_test
    def subtest_do_source_dest_operations(self):
        # Launch an instance without specifying any skip-source-dest-check value and check that skip-source-dest-check defaults to false
        instance_name = util.random_name('cli_test_instance')
        image_id = 'ocid1.image.oc1.phx.aaaaaaaamv5wg7ffvaxaba3orhpuya7x7opz24hd6m7epmwfqbeudi6meepq'  # ol6.8-base-0.0.2
        shape = 'VM.Standard1.1'

        print("subtest_do_source_dest_operations: starting instance")
        result = self.invoke(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', instance_name,
             '--subnet-id', self.subnet_ocid,
             '--image-id', image_id,
             '--shape', shape])
        self.instance_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)
        print("subtest_do_source_dest_operations: instance=" + self.instance_ocid)
        util.wait_until(['compute', 'instance', 'get', '--instance-id', self.instance_ocid], 'RUNNING', max_wait_seconds=600)

        result = self.invoke(
            ['compute', 'instance', 'list-vnics',
             '--instance-id', self.instance_ocid])
        vnics = json.loads(result.output)
        primary_vnic_id = vnics['data'][0]['id']
        self.assertEqual(1, len(vnics['data']))
        self.assertFalse(vnics['data'][0]['skip-source-dest-check'])

        # Attach a VNIC without specifying any skip-source-dest-check value and check that skip-source-dest-check defaults to false
        self.attach_update_then_detach_secondary_vnic_with_skip_source_dest_value(primary_vnic_id, False, None)

        # Attach a VNIC with specifying skip-source-dest-check explicitly to true
        self.attach_update_then_detach_secondary_vnic_with_skip_source_dest_value(primary_vnic_id, False, True)

        # Attach a VNIC with specifying skip-source-dest-check explicitly to false
        self.attach_update_then_detach_secondary_vnic_with_skip_source_dest_value(primary_vnic_id, False, False)

        self.update_source_dest_on_vnic(primary_vnic_id)

        # Terminate our instance and spin up one with a specified skip-source-dest-check value
        print("subtest_do_source_dest_operations: terminating instance " + self.instance_ocid)
        self.invoke(['compute', 'instance', 'terminate', '--instance-id', self.instance_ocid, '--force'])
        self.previous_instance_ocid = self.instance_ocid

        print("subtest_do_source_dest_operations: starting second instance ")
        result = self.invoke(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', instance_name,
             '--subnet-id', self.subnet_ocid,
             '--image-id', image_id,
             '--skip-source-dest-check', 'true',
             '--shape', shape])
        self.instance_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)
        print("subtest_do_source_dest_operations: second instance=" + self.instance_ocid)
        util.wait_until(['compute', 'instance', 'get', '--instance-id', self.instance_ocid], 'RUNNING', max_wait_seconds=600)

        result = self.invoke(
            ['compute', 'instance', 'list-vnics',
             '--instance-id', self.instance_ocid])
        vnics = json.loads(result.output)
        self.assertEqual(1, len(vnics['data']))
        self.assertTrue(vnics['data'][0]['skip-source-dest-check'])

    def attach_update_then_detach_secondary_vnic_with_skip_source_dest_value(self, primary_vnic_id, primary_vnic_skip_check_value, skip_source_dest_check_value):
        if skip_source_dest_check_value is None:
            result = self.invoke(
                ['compute', 'instance', 'attach-vnic',
                 '--instance-id', self.instance_ocid,
                 '--subnet-id', self.subnet_ocid,
                 '--wait'])
            expected_skip_check_value = False
        else:
            if skip_source_dest_check_value:
                skip_check_param_value = 'true'
            else:
                skip_check_param_value = 'false'

            result = self.invoke(
                ['compute', 'instance', 'attach-vnic',
                 '--instance-id', self.instance_ocid,
                 '--subnet-id', self.subnet_ocid,
                 '--skip-source-dest-check', skip_check_param_value,
                 '--wait'])
            expected_skip_check_value = skip_source_dest_check_value

        attach_vnic_output = json.loads(result.output)
        secondary_vnic_id = attach_vnic_output['data']['id']
        self.assertEqual(expected_skip_check_value, attach_vnic_output['data']['skip-source-dest-check'])

        result = self.invoke(
            ['compute', 'instance', 'list-vnics',
             '--instance-id', self.instance_ocid])
        vnics = json.loads(result.output)
        self.assertEqual(2, len(vnics['data']))
        self.find_vnic_and_check_skip_source_dest_value(vnics['data'], primary_vnic_id, primary_vnic_skip_check_value)
        self.find_vnic_and_check_skip_source_dest_value(vnics['data'], secondary_vnic_id, expected_skip_check_value)

        result = self.invoke(
            ['network', 'vnic', 'get',
             '--vnic-id', secondary_vnic_id])
        vnic_from_get = json.loads(result.output)
        self.assertEqual(expected_skip_check_value, vnic_from_get['data']['skip-source-dest-check'])

        self.update_source_dest_on_vnic(secondary_vnic_id)

        result = self.invoke(
            ['compute', 'vnic-attachment', 'list',
             '--compartment-id', util.COMPARTMENT_ID,
             '--vnic-id', secondary_vnic_id])
        json_data = json.loads(result.output)
        vnic_attachment_id = json_data['data'][0]['id']

        result = self.invoke(
            ['compute', 'instance', 'detach-vnic',
             '--vnic-id', secondary_vnic_id,
             '--compartment-id', util.COMPARTMENT_ID,
             '--force',
             '--wait-for-state', 'DETACHED',
             '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS])
        self.assertEqual(0, result.exit_code)

        time.sleep(5)

    def find_vnic_and_check_skip_source_dest_value(self, vnics, target_vnic_id, skip_source_dest_check_value):
        for vnic in vnics:
            if vnic['id'] == target_vnic_id:
                self.assertEqual(skip_source_dest_check_value, vnic['skip-source-dest-check'])
                break
        else:
            self.fail('Unable to find {} in the list of VNICs'.format(target_vnic_id))

    def update_source_dest_on_vnic(self, vnic_id):
        result = self.invoke(
            ['network', 'vnic', 'update',
             '--vnic-id', vnic_id,
             '--skip-source-dest-check', 'true'])
        vnic_from_update = json.loads(result.output)
        self.assertTrue(vnic_from_update['data']['skip-source-dest-check'])

        result = self.invoke(
            ['network', 'vnic', 'get',
             '--vnic-id', vnic_id])
        vnic_from_get = json.loads(result.output)
        self.assertTrue(vnic_from_get['data']['skip-source-dest-check'])

        # Updating to self is OK
        result = self.invoke(
            ['network', 'vnic', 'update',
             '--vnic-id', vnic_id,
             '--skip-source-dest-check', 'true'])
        vnic_from_update = json.loads(result.output)
        self.assertTrue(vnic_from_update['data']['skip-source-dest-check'])

        result = self.invoke(
            ['network', 'vnic', 'update',
             '--vnic-id', vnic_id,
             '--skip-source-dest-check', 'false'])
        vnic_from_update = json.loads(result.output)
        self.assertFalse(vnic_from_update['data']['skip-source-dest-check'])

        result = self.invoke(
            ['network', 'vnic', 'get',
             '--vnic-id', vnic_id])
        vnic_from_get = json.loads(result.output)
        self.assertFalse(vnic_from_get['data']['skip-source-dest-check'])

    @util.log_test
    def set_up_resources(self):
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
        util.wait_until(['network', 'vcn', 'get', '--vcn-id', self.vcn_ocid], 'AVAILABLE', max_wait_seconds=300)

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
        util.wait_until(['network', 'subnet', 'get', '--subnet-id', self.subnet_ocid], 'AVAILABLE', max_wait_seconds=300)

    @util.log_test
    def clean_up_resources(self):
        print("clean_up_resources")
        error_count = 0

        if hasattr(self, 'instance_ocid'):
            try:
                print("Deleting instance")
                result = self.invoke(['compute', 'instance', 'terminate', '--instance-id', self.instance_ocid, '--force'])
                util.validate_response(result)

                # This check was deferred from earlier b/c it takes a while to terminate an instance
                print("waiting for first instance to terminate " + self.previous_instance_ocid)
                util.wait_until(['compute', 'instance', 'get', '--instance-id', self.previous_instance_ocid], 'TERMINATED', max_wait_seconds=1200, succeed_if_not_found=True)

                util.wait_until(['compute', 'instance', 'get', '--instance-id', self.instance_ocid], 'TERMINATED', max_wait_seconds=1200, succeed_if_not_found=True)
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
