# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    def test_integration_instance_change_compartment(self):
        result = util.invoke_command(
            ['integration', 'integration-instance', 'change-compartment'])
        assert 'Error: Missing option(s)' in result.output
        assert '--id' in result.output

    def test_integration_instance_stop(self):
        result = util.invoke_command(
            ['integration', 'integration-instance', 'stop'])
        assert 'Error: Missing option(s)' in result.output
        assert '--id' in result.output

    def test_integration_instance_start(self):
        result = util.invoke_command(
            ['integration', 'integration-instance', 'start'])
        assert 'Error: Missing option(s)' in result.output
        assert '--id' in result.output

    def test_integration_instance_delete(self):
        result = util.invoke_command(
            ['integration', 'integration-instance', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--id' in result.output

    def test_integration_instance_get(self):
        result = util.invoke_command(
            ['integration', 'integration-instance', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--id' in result.output

    def test_integration_instance_update(self):
        result = util.invoke_command(
            ['integration', 'integration-instance', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--id' in result.output
        result = util.invoke_command(
            ['integration', 'integration-instance', 'update', '--type'])
        assert 'Error: --type option requires an argument' in result.output

    def test_integration_instance_create(self):
        result = util.invoke_command(
            ['integration', 'integration-instance', 'create', '--type'])
        assert 'Error: --type option requires an argument' in result.output

    def test_work_request_list(self):
        result = util.invoke_command(
            ['integration', 'work-request', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--id' in result.output
