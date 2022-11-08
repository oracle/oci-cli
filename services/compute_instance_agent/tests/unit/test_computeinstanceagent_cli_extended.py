# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestComputeInstanceAgent(unittest.TestCase):
    def setUp(self):
        pass

    def test_instance_agent_invoke(self):
        result = util.invoke_command(['instance-agent', 'command'])
        assert 'Usage: oci instance-agent command' in result.output

        result = util.invoke_command(['instance-agent', 'command-execution'])
        assert 'Usage: oci instance-agent command-execution' in result.output

    def test_instance_agent_command_cancel_invoke(self):
        result = util.invoke_command(['instance-agent', 'command', 'cancel'])
        assert 'Missing option(s) --command-id' in result.output

    def test_instance_agent_command_get_invoke(self):
        result = util.invoke_command(['instance-agent', 'command', 'get'])
        assert 'Missing option(s) --command-id' in result.output

    def test_instance_agent_command_create_invoke(self):
        result = util.invoke_command(['instance-agent', 'command', 'create', '--timeout-in-seconds'])
        assert 'Error: --timeout-in-seconds option requires an argument' in result.output

    def test_instance_agent_command_exec_get_invoke(self):
        result = util.invoke_command(['instance-agent', 'command-execution', 'get'])
        assert '--command-id' in result.output
