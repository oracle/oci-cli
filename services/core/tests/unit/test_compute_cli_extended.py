# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestCompute(unittest.TestCase):
    def setUp(self):
        pass

    def test_launch_instance(self):
        result = util.invoke_command(['compute', 'instance', 'launch', '--nsg-ids', 'dummy'])
        assert 'Error: Missing option(s)' in result.output
        assert 'availability-domain' in result.output
        assert 'compartment-id' in result.output
        assert 'shape' in result.output

    def test_attach_vnic(self):
        result = util.invoke_command(['compute', 'instance', 'attach-vnic', '--nsg-ids', 'dummy'])
        assert 'Error: Missing option(s)' in result.output
        assert 'instance-id' in result.output
        assert 'subnet-id' in result.output

    def test_volume_attachment(self):
        result = util.invoke_command(['compute', 'volume-attachment', 'attach-paravirtualized-volume'])
        assert 'Error: Missing option(s)' in result.output

        result = util.invoke_command(['compute', 'volume-attachment', 'attach'])
        assert 'Error: Missing option(s)' in result.output

        result = util.invoke_command(['compute', 'volume-attachment', 'attach', '--type', 'x'])
        assert 'Error: Invalid value for "--type":' in result.output
        assert '(choose from service_determined, emulated, iscsi, paravirtualized)' in result.output

        result = util.invoke_command(['compute', 'volume-attachment', 'attach', '--type', 'service_determined'])
        assert 'Error: Missing option(s)' in result.output
        result = util.invoke_command(['compute', 'volume-attachment', 'attach', '--type', 'emulated'])
        assert 'Error: Missing option(s)' in result.output
        result = util.invoke_command(['compute', 'volume-attachment', 'attach', '--type', 'iscsi'])
        assert 'Error: Missing option(s)' in result.output
        result = util.invoke_command(['compute', 'volume-attachment', 'attach', '--type', 'paravirtualized'])
        assert 'Error: Missing option(s)' in result.output

    def test_attach_iscsi_volume(self):
        result = util.invoke_command(['compute', 'volume-attachment'])
        assert 'attach-iscsi-volume' in result.output

        result = util.invoke_command(['compute', 'volume-attachment', 'attach-iscsi-volume'])
        assert 'Error: Missing option(s) --instance-id, --volume-id.' in result.output

    # verify if change-compartment takes --wait-for-state option
    def test_change_compartment(self):
        result = util.invoke_command(['compute', 'instance'])
        assert 'change-compartment' in result.output
        result = util.invoke_command(['compute', 'instance', 'change-compartment', '--instance-id', 'dummy',
                                      '--compartment-id', 'dummy', '--wait-for-state', 'ACCEPTED'])
        assert 'ServiceError' in result.output

    def test_dedicated_vm_host_commands(self):
        result = util.invoke_command(['compute'])
        assert 'dedicated-vm-host' in result.output
        result = util.invoke_command(['compute', 'dedicated-vm-host'])

        assert 'host-shape' in result.output
        assert 'instance-shape' in result.output

        result = util.invoke_command(['compute', 'dedicated-vm-host', 'host-shape', 'list'])
        assert 'Error: Missing option(s)' in result.output

        result = util.invoke_command(['compute', 'dedicated-vm-host', 'instance-shape', 'list'])
        assert 'Error: Missing option(s)' in result.output

    def test_list_volume_attachment(self):
        result = util.invoke_command(['compute', 'volume-attachment', 'list'])
        assert 'UsageError' in result.output
        assert '--compartment-id' in result.output
        assert '--instance-id' in result.output

        result = util.invoke_command(['compute', 'volume-attachment', 'list', '--compartment-id', 'dummy',
                                      '--instance-id', 'dummy'])
        assert 'ServiceError' in result.output

    def test_list_vnics(self):
        result = util.invoke_command(['compute', 'instance', 'list-vnics'])
        assert 'UsageError' in result.output
        assert '--compartment-id' in result.output
        assert '--instance-id' in result.output
