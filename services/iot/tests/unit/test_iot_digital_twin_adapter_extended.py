# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestDigitalTwinAdapter(unittest.TestCase):
    def setUp(self):
        pass

    def test_adapter_create(self):
        result = util.invoke_command(['iot', 'digital-twin-adapter', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--iot-domain-id' in result.output
        arg_options = [
            "--inbound-envelope",
            "--inbound-routes"
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "digital-twin-adapter", "create", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output

    def test_adapter_get(self):
        result = util.invoke_command(['iot', 'digital-twin-adapter', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--digital-twin-adapter-id' in result.output

    def test_adapter_delete(self):
        result = util.invoke_command(["iot", "digital-twin-adapter", "delete"])
        assert "Error: Missing option(s)" in result.output
        assert "--digital-twin-adapter-id" in result.output
        arg_options = [
            "--digital-twin-adapter-id",
            "--if-match",
            "--from-json",
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "digital-twin-adapter", "delete", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output

    def test_adapter_update(self):
        result = util.invoke_command(["iot", "digital-twin-adapter", "update"])
        assert "Error: Missing option(s)" in result.output
        assert "--digital-twin-adapter-id" in result.output
        arg_options = [
            "--digital-twin-adapter-id",
            "--inbound-envelope",
            "--inbound-routes",
            "--freeform-tags",
            "--defined-tags",
            "--display-name",
            "--description",
            "--if-match",
            "--from-json",
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "digital-twin-adapter", "update", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output

    def test_adapter_list(self):
        arg_options = [
            "--id",
            "--iot-domain-id",
            "--digital-twin-model-id",
            "--digital-twin-model-spec-uri",
            "--display-name",
            "--lifecycle-state",
            "--limit",
            "--page",
            "--page-size",
            "--sort-order",
            "--from-json",
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "digital-twin-adapter", "list", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output
