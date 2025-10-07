# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestIotDomainGroup(unittest.TestCase):
    def setUp(self):
        pass

    def test_iot(self):
        result = util.invoke_command(['iot'])
        assert 'Commands:' in result.output
        assert 'digital-twin-adapter' in result.output
        assert 'digital-twin-instance' in result.output
        assert 'digital-twin-model' in result.output
        assert 'digital-twin-relationship' in result.output
        assert 'domain' in result.output
        assert 'work-request' in result.output

    def test_domain_group_create(self):
        result = util.invoke_command(['iot', 'domain-group', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output

    def test_domain_group_get(self):
        result = util.invoke_command(['iot', 'domain-group', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--iot-domain-group-id' in result.output

    def test_domain_group_delete(self):
        result = util.invoke_command(["iot", "domain-group", "delete"])
        assert "Error: Missing option(s)" in result.output
        assert "--iot-domain-group-id" in result.output
        arg_options = [
            "--iot-domain-group-id",
            "--if-match",
            "--max-wait-seconds",
            "--wait-interval-seconds",
            "--from-json",
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "domain-group", "delete", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output

    def test_domain_group_update(self):
        result = util.invoke_command(["iot", "domain-group", "update"])
        assert "Error: Missing option(s)" in result.output
        assert "--iot-domain-group-id" in result.output
        arg_options = [
            "--iot-domain-group-id",
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
            result = util.invoke_command(["iot", "domain-group", "update", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output

    def test_domain_group_list(self):
        arg_options = [
            "--id",
            "--compartment-id",
            "--display-name",
            "--lifecycle-state",
            "--limit",
            "--page",
            "--page-size",
            "--sort-order",
            "--from-json",
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "domain-group", "list", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output

    def test_domain_group_change_compartment(self):
        result = util.invoke_command(['iot', 'domain-group', 'change-compartment'])
        assert 'Error: Missing option(s)' in result.output
        assert '--iot-domain-group-id' in result.output
        assert '--compartment-id' in result.output

    def test_domain_group_configure_data_access(self):
        result = util.invoke_command(['iot', 'domain-group', 'configure-data-access'])
        assert 'Error: Missing option(s)' in result.output
        assert '--iot-domain-group-id' in result.output
        assert '--db-allow-listed-vcn-ids' in result.output
