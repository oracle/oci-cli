# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestAutoScaling(unittest.TestCase):
    def setUp(self):
        pass

    def test_policy_create(self):
        result = util.invoke_command(['autoscaling', 'policy', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert 'auto-scaling-configuration-id' in result.output
        assert 'policy-type' in result.output
        result = util.invoke_command(['autoscaling', 'policy', 'create', '--auto-scaling-configuration-id', '1', '--capacity', '1', '--policy-type', 'scheduled'])
        assert 'UsageError: If Parameter --policy-type is scheduled, then Parameter --execution-schedule must be provided' in result.output

    def test_policy_update(self):
        result = util.invoke_command(['autoscaling', 'policy', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert 'auto-scaling-configuration-id' in result.output
        assert 'auto-scaling-policy-id' in result.output
        assert 'policy-type' in result.output
        result = util.invoke_command(
            ['autoscaling', 'policy', 'update', '--auto-scaling-configuration-id', '1', '--auto-scaling-policy-id', '1',
             '--policy-type', 'scheduled'])
        assert 'UsageError: If Parameter --policy-type is scheduled, then Parameter --execution-schedule must be provided' in result.output
