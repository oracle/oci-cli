# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from types import SimpleNamespace
from unittest.mock import patch

from click.testing import CliRunner
from oci_cli.cli_root import cli
from tests import util


class TestNetwork(unittest.TestCase):
    def setUp(self):
        pass

    @patch('oci_cli.cli_util.render_response')
    @patch('oci_cli.cli_util.build_client')
    def test_assign_ipv6_hostname(self, build_client, render_response):
        client = build_client.return_value
        client.get_vnic.return_value.data.subnet_id = 'subnet'
        args = ['network', 'vnic', 'assign-ipv6', '--vnic-id', 'vnic']
        for options, extra_fields in [([], {}), (['--hostname', 'worker'], {'hostname': 'worker'})]:
            with self.subTest(options=options):
                result = CliRunner().invoke(cli, args + options)
                self.assertEqual(result.exit_code, 0, result.exception)
                client.create_ipv6.assert_called_with(dict(vnicId='vnic', subnetId='subnet', **extra_fields))

    @patch('oci_cli.cli_util.render_response')
    @patch('oci_cli.cli_util.build_client')
    def test_reassign_ipv6_hostname(self, build_client, render_response):
        client = build_client.return_value
        client.get_vnic.return_value.data.subnet_id = 'subnet'
        client.list_ipv6s.return_value.data = [SimpleNamespace(id='address', vnic_id='old-vnic')]
        args = ['network', 'vnic', 'assign-ipv6', '--vnic-id', 'vnic', '--ip-address', '2001:db8::1',
                '--unassign-if-already-assigned', '--hostname', 'worker']
        result = CliRunner().invoke(cli, args)
        self.assertEqual(result.exit_code, 0, result.exception)
        client.update_ipv6.assert_called_once_with('address', {'vnicId': 'vnic', 'hostname': 'worker'})
        client.create_ipv6.assert_not_called()

    def nsg_wrong_param_name(self, operation):
        result = util.invoke_command(['network', 'nsg'] + operation + ['--network-security-group-id'])
        assert 'Error: No such option:' in result.output
        assert 'network-security-group-id' in result.output

    def nsg_correct_param_name(self, operation, other_params, force):
        result = util.invoke_command(['network', 'nsg'] + operation + ['--nsg-id', 'dummy'] + other_params + (['--force'] if force else []))
        assert 'ServiceError' in result.output

    def nsg_correct_empty_param_name(self, operation, other_params, force):
        result = util.invoke_command(['network', 'nsg'] + operation + ['--nsg-id', ''] + other_params + (['--force'] if force else []))
        assert 'UsageError: Parameter --nsg-id cannot be whitespace or empty string' in result.output

    def nsg_param_checks(self, operation, other_params=[], force=False):
        self.nsg_wrong_param_name(operation)
        self.nsg_correct_param_name(operation, other_params, force)
        self.nsg_correct_empty_param_name(operation, other_params, force)

    def test_nsg_id_options(self):
        self.nsg_param_checks(['change-compartment'], other_params=['--compartment-id', 'dummy'])
        self.nsg_param_checks(['delete'], force=True)
        self.nsg_param_checks(['get'])
        self.nsg_param_checks(['rules', 'add'])
        self.nsg_param_checks(['rules', 'list'])
        self.nsg_param_checks(['rules', 'remove'])
        self.nsg_param_checks(['rules', 'update'])
        self.nsg_param_checks(['vnics', 'list'])
