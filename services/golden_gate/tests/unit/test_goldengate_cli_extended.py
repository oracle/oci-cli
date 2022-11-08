# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util

'''
Tests verifying that moved/renamed commands appear as expected.
'''


class TestGoldenGate(unittest.TestCase):
    def setUp(self):
        pass

    def test_deployment_start_default(self):
        result = util.invoke_command(['goldengate', 'deployment', 'start-deployment-default-start-deployment-details'])
        assert 'Error: No such command ' in result.output

    def test_deployment_stop_default(self):
        result = util.invoke_command(['goldengate', 'deployment', 'stop-deployment-default-stop-deployment-details'])
        assert 'Error: No such command ' in result.output

    def test_deployment_upgrade_default(self):
        result = util.invoke_command(['goldengate', 'deployment', 'upgrade_deployment_upgrade_deployment_current_release_details'])
        assert 'Error: No such command ' in result.output

    def test_deployment_backup_restore_default(self):
        result = util.invoke_command(['goldengate', 'deployment', 'restore_deployment_default_restore_deployment_details'])
        assert 'Error: No such command ' in result.output

    def test_deployment_create_req_params(self):
        result = util.invoke_command(['goldengate', 'deployment', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert 'display-name' in result.output
        assert 'compartment-id' in result.output
        assert 'subnet-id' in result.output
        assert 'cpu-core-count' in result.output
        assert 'is-auto-scaling-enabled' in result.output

    def test_deployment_create_req_params1(self):
        result = util.invoke_command(['goldengate', 'deployment', 'create', '--admin-username'])
        assert 'Error: --admin-username option requires an argument' in result.output

    def test_deployment_create_req_params2(self):
        result = util.invoke_command(['goldengate', 'deployment', 'create', '--admin-password'])
        assert 'Error: --admin-password option requires an argument' in result.output

    def test_deployment_create_req_params3(self):
        result = util.invoke_command(['goldengate', 'deployment', 'create', '--license-model', 'LICENSE_INCLUDED', '--display-name', 'aa', '--compartment-id', 'bb', '--subnet-id', 'cc', '--cpu-core-count', '1', '--is-auto-scaling-enabled', 'true'])
        assert 'Error: Missing option(s)' in result.output
        assert '--deployment-name' in result.output
        assert '--admin-username' in result.output

    def test_deployment_upgrade_req_params(self):
        result = util.invoke_command(['goldengate', 'deployment', 'upgrade'])
        assert 'Error: Missing option(s)' in result.output
        assert 'deployment-id' in result.output
