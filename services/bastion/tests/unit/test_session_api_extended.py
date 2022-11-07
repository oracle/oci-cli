# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


# pytest -s services/bastion/tests/unit/test_session_api_extended.py
class TestSessionApi(unittest.TestCase):
    def setUp(self):
        pass

    def test_session_api_options(self):
        result = util.invoke_command(['bastion', 'session'])
        assert 'create-managed-ssh' in result.output
        assert 'create-port-forwarding' in result.output
        assert 'create' in result.output
        assert 'delete' in result.output
        assert 'get' in result.output
        assert 'list' in result.output
        assert 'update' in result.output
        assert '--help' in result.output

    def test_session_create(self):
        result = util.invoke_command(['bastion', 'session', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--target-resource-details' in result.output
        assert '--bastion-id' in result.output
        result = util.invoke_command(['bastion', 'session', 'create', '--target-resource-details'])
        assert 'Error: --target-resource-details option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create', '--bastion-id'])
        assert 'Error: --bastion-id option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create', '--session-ttl-in-seconds'])
        assert 'Error: --session-ttl-in-seconds option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create', '--wait-for-state'])
        assert 'Error: --wait-for-state option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output

    def test_session_create_managed_ssh(self):
        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh'])
        assert 'Error: Missing option(s)' in result.output
        assert '--bastion-id' in result.output
        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--bastion-id'])
        assert 'Error: --bastion-id option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--ssh-public-key-file'])
        assert 'Error: --ssh-public-key-file option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--key-type'])
        assert 'Error: --key-type option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--key-type', 'PUB'])
        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--key-type', 'pub'])
        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--key-type', 'pUb'])
        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--wait-for-state'])
        assert 'Error: --wait-for-state option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create-managed-ssh', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output

    def test_session_create_port_forwarding(self):
        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding'])
        assert 'Error: Missing option(s)' in result.output
        assert '--bastion-id' in result.output
        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--bastion-id'])
        assert 'Error: --bastion-id option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--key-type'])
        assert 'Error: --key-type option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--key-type', 'PUB'])
        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--key-type', 'pub'])
        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--key-type', 'pUb'])
        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--wait-for-state'])
        assert 'Error: --wait-for-state option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'create-port-forwarding', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output

    def test_session_delete(self):
        result = util.invoke_command(['bastion', 'session', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--session-id' in result.output
        result = util.invoke_command(['bastion', 'session', 'delete', '--session-id'])
        assert 'Error: --session-id option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'delete', '--if-match'])
        assert 'Error: --if-match option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'delete', '--wait-for-state'])
        assert 'Error: --wait-for-state option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'delete', '--max-wait-seconds'])
        assert 'Error: --max-wait-seconds option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'delete', '--wait-interval-seconds'])
        assert 'Error: --wait-interval-seconds option requires an argument' in result.output

    def test_session_get(self):
        result = util.invoke_command(['bastion', 'session', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--session-id' in result.output
        result = util.invoke_command(['bastion', 'session', 'get', '--session-id'])
        assert 'Error: --session-id option requires an argument' in result.output

    def test_session_list(self):
        result = util.invoke_command(['bastion', 'session', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--bastion-id' in result.output
        result = util.invoke_command(['bastion', 'session', 'list', '--session-id'])
        assert 'Error: --session-id option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'list', '--bastion-id'])
        assert 'Error: --bastion-id option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'list', '--session-lifecycle-state'])
        assert 'Error: --session-lifecycle-state option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'list', '--display-name'])
        assert 'Error: --display-name option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'list', '--limit'])
        assert 'Error: --limit option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'list', '--page'])
        assert 'Error: --page option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'list', '--sort-order'])
        assert 'Error: --sort-order option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'list', '--sort-order', 'DeSc'])
        result = util.invoke_command(['bastion', 'session', 'list', '--sort-order', 'aSc'])
        result = util.invoke_command(['bastion', 'session', 'list', '--sort-by'])
        assert 'Error: --sort-by option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'list', '--sort-by', 'DisplayName'])
        result = util.invoke_command(['bastion', 'session', 'list', '--sort-by', 'timecreated'])
        result = util.invoke_command(['bastion', 'session', 'list', '--page-size'])
        assert 'Error: --page-size option requires an argument' in result.output
        result = util.invoke_command(['bastion', 'session', 'list', '--all'])
