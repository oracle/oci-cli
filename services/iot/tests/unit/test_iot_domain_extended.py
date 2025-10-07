# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestIotDomain(unittest.TestCase):
    def setUp(self):
        pass

    def test_domain_create(self):
        result = util.invoke_command(['iot', 'domain', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--iot-domain-group-id' in result.output
        assert '--compartment-id' in result.output

    def test_domain_get(self):
        result = util.invoke_command(['iot', 'domain', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--iot-domain-id' in result.output

    def test_domain_delete(self):
        result = util.invoke_command(["iot", "domain", "delete"])
        assert "Error: Missing option(s)" in result.output
        assert "--iot-domain-id" in result.output
        arg_options = [
            "--iot-domain-id",
            "--if-match",
            "--max-wait-seconds",
            "--wait-interval-seconds",
            "--from-json",
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "domain", "delete", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output

    def test_domain_update(self):
        result = util.invoke_command(["iot", "domain", "update"])
        assert "Error: Missing option(s)" in result.output
        assert "--iot-domain-id" in result.output
        arg_options = [
            "--iot-domain-id",
            "--freeform-tags",
            "--defined-tags",
            "--display-name",
            "--description",
            "--if-match",
            "--max-wait-seconds",
            "--wait-interval-seconds",
            "--from-json",
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "domain", "update", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output

    def test_domain_list(self):
        arg_options = [
            "--id",
            "--compartment-id",
            "--iot-domain-group-id",
            "--display-name",
            "--lifecycle-state",
            "--limit",
            "--page",
            "--page-size",
            "--sort-order",
            "--from-json",
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "domain", "list", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output

    def test_domain_change_compartment(self):
        result = util.invoke_command(['iot', 'domain', 'change-compartment'])
        assert 'Error: Missing option(s)' in result.output
        assert '--iot-domain-id' in result.output
        assert '--compartment-id' in result.output

    def test_domain_change_data_retention_period(self):
        result = util.invoke_command(['iot', 'domain', 'change-data-retention-period'])
        assert 'Error: Missing option(s)' in result.output
        assert '--iot-domain-id' in result.output
        assert '--type' in result.output
        assert '--data-retention-period-in-days' in result.output

    def test_domain_configure_data_access(self):
        result = util.invoke_command(['iot', 'domain', 'configure-apex-data-access'])
        assert 'Error: Missing option(s)' in result.output
        assert '--iot-domain-id' in result.output
        assert '--db-workspace-admin-initial-password' in result.output
        result = util.invoke_command(['iot', 'domain', 'configure-direct-data-access'])
        assert 'Error: Missing option(s)' in result.output
        assert '--iot-domain-id' in result.output
        assert '--db-allow-listed-identity-group-names' in result.output
        result = util.invoke_command(['iot', 'domain', 'configure-ords-data-access'])
        assert 'Error: Missing option(s)' in result.output
        assert '--iot-domain-id' in result.output
        assert '--db-allowed-identity-domain-host' in result.output
