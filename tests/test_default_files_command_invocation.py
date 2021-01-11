# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import pytest
import unittest
from . import test_config_container
from . import util

IPXE_SCRIPT_FILE = 'tests/resources/ipxe_script_example.txt'


class TestDefaultFilesCommandInvocation(unittest.TestCase):

    def test_invoke_with_default_file_global(self):
        with test_config_container.create_vcr().use_cassette(
                'default_files_command_invoke_with_default_file_global.yml'):
            result = self.invoke(['os', 'bucket', 'list', '-c', util.COMPARTMENT_ID, '--defaults-file', 'tests/resources/default_files/global_default'])
            assert result.exit_code == 0
            assert result.output == ''  # The namespace shouldn't exist so we get back a blank result

    def test_invoke_with_default_file_command_group(self):
        with test_config_container.create_vcr().use_cassette(
                'default_files_command_invoke_with_default_file_command_group.yml'):
            result = self.invoke(['os', 'bucket', 'list', '-c', util.COMPARTMENT_ID, '--defaults-file', 'tests/resources/default_files/command_group_default'])
            assert result.exit_code == 0
            assert result.output == ''  # The namespace shouldn't exist so we get back a blank result

    def test_invoke_with_default_file_command_subgroup(self):
        with test_config_container.create_vcr().use_cassette(
                'default_files_command_invoke_with_default_file_command_subgroup.yml'):
            result = self.invoke(['os', 'bucket', 'list', '-c', util.COMPARTMENT_ID, '--defaults-file', 'tests/resources/default_files/command_subgroup_default'])
            print(result.output)
            assert result.exit_code == 0
            assert result.output == ''  # The namespace shouldn't exist so we get back a blank result

    def test_invoke_with_default_file_specific_command(self):
        with test_config_container.create_vcr().use_cassette(
                'default_files_command_invoke_with_default_file_specific_command.yml'):
            result = self.invoke(['os', 'bucket', 'list', '-c', util.COMPARTMENT_ID, '--defaults-file', 'tests/resources/default_files/specific_command_default'])
            assert result.exit_code == 0
            assert result.output == ''  # The namespace shouldn't exist so we get back a blank result

    @util.slow
    def test_invoke_with_file_paths_and_json_in_default_file(self):
        with test_config_container.create_vcr().use_cassette('default_files_command_invoke_with_file_paths.yml'):
            self.create_network_resources()

            try:
                instance_name = util.random_name('cli_test_instance_options')
                image_id = util.oracle_linux_image()
                shape = 'VM.Standard1.2'
                hostname_label = util.random_name('bminstance', insert_underscore=False)
                vnic_display_name = 'vnic_display_name'
                private_ip = '10.0.0.15'
                assign_public_ip = 'true'

                launch_instance_result = util.invoke_command([
                    'compute', 'instance', 'launch',
                    '--compartment-id', util.COMPARTMENT_ID,
                    '--availability-domain', util.availability_domain(),
                    '--display-name', instance_name,
                    '--subnet-id', self.subnet_ocid,
                    '--image-id', image_id,
                    '--shape', shape,
                    '--hostname-label', hostname_label,
                    '--private-ip', private_ip,
                    '--assign-public-ip', assign_public_ip,
                    '--vnic-display-name', vnic_display_name,
                    '--defaults-file', 'tests/resources/default_files/launch_instance_default'
                ])

                if (launch_instance_result.output and 'LimitExceeded' in launch_instance_result.output) or (launch_instance_result.exception and 'LimitExceeded' in str(launch_instance_result.exception)):
                    pytest.skip('Skipping test_launch_instance as we received a limit exceeded error from the service')

                temp_instance_ocid = util.find_id_in_response(launch_instance_result.output)
                util.validate_response(launch_instance_result, expect_etag=True)

                extended_metadata_result = json.loads(launch_instance_result.output)['data']['extended-metadata']
                assert extended_metadata_result['a'] == '1'
                assert extended_metadata_result['b']['c'] == '3'

                content = None
                with open(IPXE_SCRIPT_FILE, mode='r') as file:
                    content = file.read()

                assert 'ipxe-script' in launch_instance_result.output
                # Just look at the first few characters. Once we hit a line break the formatting will differ.
                assert content[:5] in launch_instance_result.output

                self.delete_instance(temp_instance_ocid)
            finally:
                self.clean_up_network_resources()

    def create_network_resources(self):
        vcn_name = util.random_name('cli_test_default_file')
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = util.random_name('vcn', insert_underscore=False)

        result = util.invoke_command(
            ['network', 'vcn', 'create', '--compartment-id', util.COMPARTMENT_ID, '--display-name', vcn_name, '--cidr-block',
             cidr_block, '--dns-label', vcn_dns_label])
        self.vcn_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)
        util.wait_until(['network', 'vcn', 'get', '--vcn-id', self.vcn_ocid], 'AVAILABLE',
                        max_wait_seconds=300)

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

    def delete_instance(self, instance_ocid):
        result = util.invoke_command(['compute', 'instance', 'terminate', '--instance-id', instance_ocid, '--force'])
        util.validate_response(result)
        util.wait_until(['compute', 'instance', 'get', '--instance-id', instance_ocid], 'TERMINATED',
                        max_wait_seconds=600, succeed_if_not_found=True)

    def clean_up_network_resources(self):
        error_count = 0

        if hasattr(self, 'subnet_ocid'):
            try:
                result = util.invoke_command(['network', 'subnet', 'delete', '--subnet-id', self.subnet_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['network', 'subnet', 'get', '--subnet-id', self.subnet_ocid], 'TERMINATED',
                                max_wait_seconds=600, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'vcn_ocid'):
            try:
                result = util.invoke_command(['network', 'vcn', 'delete', '--vcn-id', self.vcn_ocid, '--force'])
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

    def parse_json_response_from_mixed_output(self, output):
        lines = output.split('\n')
        json_str = ''
        object_begun = False
        for line in lines:
            if object_begun or line.startswith('{'):
                object_begun = True
                json_str += line

        return json.loads(json_str)
