# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestDigitalTwinRelationship(unittest.TestCase):
    def setUp(self):
        pass

    def test_relationship_create(self):
        result = util.invoke_command(['iot', 'digital-twin-relationship', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--iot-domain-id' in result.output
        assert '--content-path' in result.output
        assert '--source-digital-twin-instance-id' in result.output
        assert '--target-digital-twin-instance-id' in result.output
        arg_options = [
            "--content"
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "digital-twin-relationship", "create", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output

    def test_relationship_get(self):
        result = util.invoke_command(['iot', 'digital-twin-relationship', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--digital-twin-relationship-id' in result.output

    def test_relationship_delete(self):
        result = util.invoke_command(["iot", "digital-twin-relationship", "delete"])
        assert "Error: Missing option(s)" in result.output
        assert "--digital-twin-relationship-id" in result.output
        arg_options = [
            "--digital-twin-relationship-id",
            "--if-match",
            "--from-json",
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "digital-twin-relationship", "delete", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output

    def test_relationship_update(self):
        result = util.invoke_command(["iot", "digital-twin-relationship", "update"])
        assert "Error: Missing option(s)" in result.output
        assert "--digital-twin-relationship-id" in result.output
        arg_options = [
            "--digital-twin-relationship-id",
            "--content",
            "--freeform-tags",
            "--defined-tags",
            "--display-name",
            "--description",
            "--if-match",
            "--from-json",
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "digital-twin-relationship", "update", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output

    def test_relationship_list(self):
        arg_options = [
            "--id",
            "--iot-domain-id",
            "--source-digital-twin-instance-id",
            "--target-digital-twin-instance-id",
            "--display-name",
            "--lifecycle-state",
            "--limit",
            "--page",
            "--page-size",
            "--sort-order",
            "--from-json",
        ]
        for opt in arg_options:
            result = util.invoke_command(["iot", "digital-twin-relationship", "list", opt])
            assert f"Error: Option '{opt}' requires an argument" in result.output
