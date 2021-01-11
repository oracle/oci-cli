# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import pytest
import unittest
from tests import test_config_container
from tests import util

CASSETTE_LIBRARY_DIR = 'services/core/tests/cassettes'
OPERATING_SYSTEM = 'Oracle Linux'


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('compute_extended.yml'):
        yield


def invoke_command(command, response_expected=True, **kwargs):
    response = util.invoke_command(command, **kwargs)
    assert (response.exit_code == 0)
    data = util.get_json_from_mixed_string(response.output)['data'] if response_expected else None
    return data


class TestComputeCliExtended(unittest.TestCase):

    @util.slow
    @util.log_test
    def test_launch_instance(self):
        try:
            self.launch_instance()
        finally:
            self.terminate_instance()

    @util.slow
    @util.log_test
    def test_launch_instance_in_network_security_group(self):
        network_security_group_ids = [self.network_security_group['id']]

        try:
            self.launch_instance(['--nsg-ids', json.dumps(network_security_group_ids)])
            self.validate_network_security_group()
        finally:
            self.terminate_instance()

    @util.log_test
    def setUp(self):
        self.cidr_block = '10.0.0.0/16'
        self.get_availability_domain()
        self.get_shape()
        self.get_image()

        try:
            self.create_vcn()
            self.create_subnet()
            self.create_internet_gateway()
            self.add_route_rule_to_default_route_table()
            self.create_network_security_group()
            self.add_network_security_group_security_rules()
        except Exception:
            self.tearDown()
            raise

    @util.log_test
    def tearDown(self):
        self.remove_network_security_group_security_rules()
        self.delete_network_security_group()
        self.clear_route_rules_from_default_route_table()
        self.delete_internet_gateway()
        self.delete_subnet()
        self.delete_vcn()

    def get_availability_domain(self):
        availability_domains = invoke_command(['iam', 'availability-domain', 'list'])
        assert (len(availability_domains) > 0)
        self.availability_domain = availability_domains[0]

    def get_shape(self):
        shapes = invoke_command([
            'compute', 'shape', 'list',
            '--availability-domain', self.availability_domain['name'],
            '--compartment-id', util.COMPARTMENT_ID
        ])
        assert (len(shapes) > 0)
        vm_shapes = [shape for shape in shapes if shape['shape'].startswith('VM.')]
        assert (len(vm_shapes) > 0)
        self.shape = vm_shapes[0]

    def get_image(self):
        images = invoke_command([
            'compute', 'image', 'list',
            '--compartment-id', util.COMPARTMENT_ID,
            '--operating-system', OPERATING_SYSTEM,
            '--shape', self.shape['shape']
        ])
        assert (len(images) > 0)
        self.image = images[0]

    def create_vcn(self):
        vcn_name = 'py_cli_test_vcn'
        self.vcn = invoke_command([
            'network', 'vcn', 'create',
            '--cidr-block', self.cidr_block,
            '--compartment-id', util.COMPARTMENT_ID,
            '--display-name', vcn_name,
            '--wait-for-state', 'AVAILABLE'
        ])

    def delete_vcn(self):
        if not hasattr(self, 'vcn'):
            return

        invoke_command([
            'network', 'vcn', 'delete',
            '--force',
            '--vcn-id', self.vcn['id'],
            '--wait-for-state', 'TERMINATED'
        ], response_expected=False)

    def create_subnet(self):
        subnet_name = 'py_cli_test_subnet'
        self.subnet = invoke_command([
            'network', 'subnet', 'create',
            '--availability-domain', self.availability_domain['name'],
            '--cidr-block', self.cidr_block,
            '--compartment-id', util.COMPARTMENT_ID,
            '--display-name', subnet_name,
            '--vcn-id', self.vcn['id'],
            '--wait-for-state', 'AVAILABLE'
        ])

    def delete_subnet(self):
        if not hasattr(self, 'subnet'):
            return

        invoke_command([
            'network', 'subnet', 'delete',
            '--force',
            '--subnet-id', self.subnet['id'],
            '--wait-for-state', 'TERMINATED'
        ], response_expected=False)

    def create_internet_gateway(self):
        internet_gateway_name = 'py_cli_test_internet_gateway'
        self.internet_gateway = invoke_command([
            'network', 'internet-gateway', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--display-name', internet_gateway_name,
            '--is-enabled', 'true',
            '--vcn-id', self.vcn['id'],
            '--wait-for-state', 'AVAILABLE'
        ])

    def delete_internet_gateway(self):
        if not hasattr(self, 'internet_gateway'):
            return

        invoke_command([
            'network', 'internet-gateway', 'delete',
            '--force',
            '--ig-id', self.internet_gateway['id'],
            '--wait-for-state', 'TERMINATED'
        ], response_expected=False)

    def add_route_rule_to_default_route_table(self):
        route_table = invoke_command([
            'network', 'route-table', 'get',
            '--rt-id', self.vcn['default-route-table-id']
        ])
        route_rules = route_table['route-rules']
        route_rules.append({
            'destination': '0.0.0.0/0',
            'destinationType': 'CIDR_BLOCK',
            'networkEntityId': self.internet_gateway['id']
        })
        invoke_command([
            'network', 'route-table', 'update',
            '--force',
            '--route-rules', json.dumps(route_rules),
            '--rt-id', self.vcn['default-route-table-id'],
            '--wait-for-state', 'AVAILABLE'
        ])

    def clear_route_rules_from_default_route_table(self):
        if not hasattr(self, 'internet_gateway'):
            return

        invoke_command([
            'network', 'route-table', 'update',
            '--force',
            '--route-rules', '[]',
            '--rt-id', self.vcn['default-route-table-id'],
            '--wait-for-state', 'AVAILABLE'
        ])

    def create_network_security_group(self):
        network_security_group_name = 'py_cli_test_network_security_group'
        self.network_security_group = invoke_command([
            'network', 'nsg', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--display-name', network_security_group_name,
            '--vcn-id', self.vcn['id'],
            '--wait-for-state', 'AVAILABLE'
        ])

    def delete_network_security_group(self):
        if not hasattr(self, 'network_security_group'):
            return

        invoke_command([
            'network', 'nsg', 'delete',
            '--force',
            '--nsg-id', self.network_security_group['id'],
            '--wait-for-state', 'TERMINATED'
        ], response_expected=False)

    def add_network_security_group_security_rules(self):
        security_rules = [{
            'description': 'Incoming HTTP connections',
            'direction': 'INGRESS',
            'isStateless': 'false',
            'protocol': '6',
            'source': '0.0.0.0/0',
            'sourceType': 'CIDR_BLOCK',
            'tcpOptions': {
                'destinationPortRange': {
                    'min': '80',
                    'max': '80'
                }
            }
        }]
        invoke_command([
            'network', 'nsg', 'rules', 'add',
            '--nsg-id', self.network_security_group['id'],
            '--security-rules', json.dumps(security_rules)
        ])

    def remove_network_security_group_security_rules(self):
        if not hasattr(self, 'network_security_group'):
            return

        security_rules = invoke_command([
            'network', 'nsg', 'rules', 'list',
            '--nsg-id', self.network_security_group['id']
        ])
        security_rule_ids = [security_rule['id'] for security_rule in security_rules]
        invoke_command([
            'network', 'nsg', 'rules', 'remove',
            '--nsg-id', self.network_security_group['id'],
            '--security-rule-ids', json.dumps(security_rule_ids)
        ], response_expected=False)

    def launch_instance(self, options=[]):
        instance_name = 'py_cli_test_instance'
        metadata = {
            'py_cli_test_metadata_key1': 'py_cli_test_metadata_value1'
        }
        extended_metadata = {
            'py_cli_test_extended_metadata_key2': 'py_cli_test_extended_metadata_value2',
            'py_cli_test_extended_metadata_map1': {
                'py_cli_test_extended_metadata_key3': 'py_cli_test_extended_metadata_value3',
                'py_cli_test_extended_metadata_map2': {
                    'py_cli_test_extended_metadata_key4': 'py_cli_test_extended_metadata_value4'
                },
                'py_cli_test_extended_metadata_map3': {}
            }
        }
        launch_instance_details = [
            '--availability-domain', self.availability_domain['name'],
            '--compartment-id', util.COMPARTMENT_ID,
            '--display-name', instance_name,
            '--extended-metadata', json.dumps(extended_metadata),
            '--image-id', self.image['id'],
            '--metadata', json.dumps(metadata),
            '--shape', self.shape['shape'],
            '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
            '--subnet-id', self.subnet['id']
        ]

        launch_instance_command = ['compute', 'instance', 'launch']
        launch_instance_command.extend(launch_instance_details)
        launch_instance_command.extend(options)
        launch_instance_command.extend(['--wait-for-state', 'RUNNING'])
        self.instance = invoke_command(launch_instance_command)

    def terminate_instance(self):
        if not hasattr(self, 'instance'):
            return

        invoke_command([
            'compute', 'instance', 'terminate',
            '--force',
            '--instance-id', self.instance['id'],
            '--wait-for-state', 'TERMINATED'
        ], response_expected=False)

    def validate_network_security_group(self):
        vnics = invoke_command([
            'compute', 'instance', 'list-vnics',
            '--instance-id', self.instance['id']
        ])
        assert (len(vnics) > 0)
        assert (self.network_security_group['id'] in vnics[0]['nsg-ids'])


if __name__ == '__main__':
    unittest.main()
