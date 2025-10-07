# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestDigitalTwinModel(unittest.TestCase):
    def setUp(self):
        pass

    def test_model_create(self):
        result = util.invoke_command(['iot', 'digital-twin-model', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--iot-domain-id' in result.output
        assert '--spec' in result.output

    def test_model_get(self):
        result = util.invoke_command(['iot', 'digital-twin-model', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--digital-twin-model-id' in result.output

    def test_model_get_spec(self):
        result = util.invoke_command(['iot', 'digital-twin-model', 'get-spec'])
        assert 'Error: Missing option(s)' in result.output
        assert '--digital-twin-model-id' in result.output

    def test_model_delete(self):
        result = util.invoke_command(["iot", "digital-twin-model", "delete"])
        assert "Error: Missing option(s)" in result.output
        assert "--digital-twin-model-id" in result.output
        arg_options = [
            "--digital-twin-model-id",
            "--if-match",
            "--from-json",
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "digital-twin-model", "delete", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output

    def test_model_update(self):
        result = util.invoke_command(["iot", "digital-twin-model", "update"])
        assert "Error: Missing option(s)" in result.output
        assert "--digital-twin-model-id" in result.output
        arg_options = [
            "--digital-twin-model-id",
            "--freeform-tags",
            "--defined-tags",
            "--display-name",
            "--description",
            "--if-match",
            "--from-json",
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "digital-twin-model", "update", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output

    def test_model_list(self):
        arg_options = [
            "--id",
            "--iot-domain-id",
            "--spec-uri-starts-with",
            "--display-name",
            "--lifecycle-state",
            "--limit",
            "--page",
            "--page-size",
            "--sort-order",
            "--from-json",
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "digital-twin-model", "list", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output
