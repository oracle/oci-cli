# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestBastionCliExtended(unittest.TestCase):
    def setUp(self):
        pass

    # create_session_create_managed_ssh_session_target_resource_details command renamed
    def test_create_managed_ssh_renamed_command(self):
        result = util.invoke_command(['bastion', 'session',
                                      'create_session_create_managed_ssh_session_target_resource_details'])
        assert 'No such command' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh'])
        assert """Usage: oci bastion session create-managed-ssh [OPTIONS]""" in result.output

    # create-session-create-port-forwarding-session-target-resource-details command renamed
    def test_create_port_forwarding_renamed_command(self):
        result = util.invoke_command(['bastion', 'session',
                                      'create-session-create-port-forwarding-session-target-resource-details'])
        assert 'No such command' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding'])
        assert """Usage: oci bastion session create-port-forwarding [OPTIONS]""" in result.output

    # key_details flattened params
    def test_key_details_flattened_params(self):
        result = util.invoke_command(['bastion', 'session', 'create', '--key-details'])
        assert 'Error: no such option: --key-details' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--key-details'])
        assert 'Error: no such option: --key-details' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--key-details'])
        assert 'Error: no such option: --key-details' in result.output

        result = util.invoke_command(['bastion', 'session', 'create', '--ssh-public-key-file'])
        assert 'Error: --ssh-public-key-file option requires an argument' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--ssh-public-key-file'])
        assert 'Error: --ssh-public-key-file option requires an argument' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--ssh-public-key-file'])
        assert 'Error: --ssh-public-key-file option requires an argument' in result.output

    # renamed params in create bastion
    def test_create_bastion_renamed_params(self):
        result = util.invoke_command(['bastion', 'bastion', 'create', '--max-session-ttl-in-seconds'])
        assert 'Error: no such option: --max-session-ttl-in-seconds' in result.output

        result = util.invoke_command(['bastion', 'bastion', 'create', '--static-jump-host-ip-addresses'])
        assert 'Error: no such option: --static-jump-host-ip-addresses' in result.output

        result = util.invoke_command(['bastion', 'bastion', 'create', '--client-cidr-block-allow-list'])
        assert 'Error: no such option: --client-cidr-block-allow-list' in result.output

        result = util.invoke_command(['bastion', 'bastion', 'create', '--max-session-ttl'])
        assert 'Error: --max-session-ttl option requires an argument' in result.output

        result = util.invoke_command(['bastion', 'bastion', 'create', '--jump-host-ips'])
        assert 'Error: --jump-host-ips option requires an argument' in result.output

        result = util.invoke_command(['bastion', 'bastion', 'create', '--client-cidr-list'])
        assert 'Error: --client-cidr-list option requires an argument' in result.output

    # renamed params in update bastion
    def test_update_bastion_renamed_params(self):
        result = util.invoke_command(['bastion', 'bastion', 'update', '--max-session-ttl-in-seconds'])
        assert 'Error: no such option: --max-session-ttl-in-seconds' in result.output

        result = util.invoke_command(['bastion', 'bastion', 'update', '--static-jump-host-ip-addresses'])
        assert 'Error: no such option: --static-jump-host-ip-addresses' in result.output

        result = util.invoke_command(['bastion', 'bastion', 'update', '--client-cidr-block-allow-list'])
        assert 'Error: no such option: --client-cidr-block-allow-list' in result.output

        result = util.invoke_command(['bastion', 'bastion', 'update', '--max-session-ttl'])
        assert 'Error: --max-session-ttl option requires an argument' in result.output

        result = util.invoke_command(['bastion', 'bastion', 'update', '--jump-host-ips'])
        assert 'Error: --jump-host-ips option requires an argument' in result.output

        result = util.invoke_command(['bastion', 'bastion', 'update', '--client-cidr-list'])
        assert 'Error: --client-cidr-list option requires an argument' in result.output

    # renamed params in create-managed-ssh session
    def test_create_managed_ssh_session_renamed_params(self):
        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--session-ttl-in-seconds'])
        assert 'Error: no such option: --session-ttl-in-seconds' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--session-ttl'])
        assert 'Error: --session-ttl option requires an argument' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh',
                                      '--target-resource-details-target-resource-id'])
        assert 'Error: no such option: --target-resource-details-target-resource-id' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--target-resource-id'])
        assert 'Error: --target-resource-id option requires an argument' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh',
                                      '--target-resource-details-target-resource-operating-system-user-name'])
        assert 'Error: no such option: --target-resource-details-target-resource-operating-system-user-name' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--target-os-username'])
        assert 'Error: --target-os-username option requires an argument' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh',
                                      '--target-resource-details-target-resource-port'])
        assert 'Error: no such option: --target-resource-details-target-resource-port' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--target-port'])
        assert 'Error: --target-port option requires an argument' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh',
                                      '--target-resource-details-target-resource-private-ip-address'])
        assert 'Error: no such option: --target-resource-details-target-resource-private-ip-address' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--target-private-ip'])
        assert 'Error: --target-private-ip option requires an argument' in result.output

    # renamed params in create-port-forwarding session
    def test_create_port_forwarding_session_renamed_params(self):
        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--session-ttl-in-seconds'])
        assert 'Error: no such option: --session-ttl-in-seconds' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--session-ttl'])
        assert 'Error: --session-ttl option requires an argument' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding',
                                      '--target-resource-details-target-resource-id'])
        assert 'Error: no such option: --target-resource-details-target-resource-id' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--target-resource-id'])
        assert 'Error: --target-resource-id option requires an argument' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding',
                                      '--target-resource-details-target-resource-port'])
        assert 'Error: no such option: --target-resource-details-target-resource-port' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--target-port'])
        assert 'Error: --target-port option requires an argument' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding',
                                      '--target-resource-details-target-resource-private-ip-address'])
        assert 'Error: no such option: --target-resource-details-target-resource-private-ip-address' in result.output

        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--target-private-ip'])
        assert 'Error: --target-private-ip option requires an argument' in result.output
