# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestComputeManagement(unittest.TestCase):
    def setUp(self):
        pass

    def test_compute_management(self):
        result = util.invoke_command(['compute-management'])
        assert 'instance-configuration' in result.output
        assert 'instance-pool' in result.output

    def test_instance_pool(self):
        result = util.invoke_command(['compute-management', 'instance-pool'])
        assert 'attach-lb' in result.output
        assert 'detach-lb' in result.output
        assert 'lb-attachment' in result.output

    def test_instance_pool_lb_attachment(self):
        result = util.invoke_command(['compute-management', 'instance-pool', 'lb-attachment'])
        assert 'attach' in result.output
        assert 'detach' in result.output
        assert 'get' in result.output

    def test_lb_attachment_get(self):
        result = util.invoke_command(['compute-management', 'instance-pool', 'lb-attachment', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--instance-pool-id' in result.output
        assert '--lb-attachment-id' in result.output

    def test_lb_attachment_attach(self):
        result = util.invoke_command(['compute-management', 'instance-pool', 'lb-attachment', 'attach'])
        assert 'Error: Missing option(s)' in result.output
        assert '--instance-pool-id' in result.output
        assert '--load-balancer-id' in result.output
        assert '--port' in result.output
        assert '--backend-set-name' in result.output
        assert '--vnic-selection' in result.output

    def test_lb_attachment_detach(self):
        result = util.invoke_command(['compute-management', 'instance-pool', 'lb-attachment', 'detach'])
        assert 'Error: Missing option(s)' in result.output
        assert '--instance-pool-id' in result.output
        assert '--load-balancer-id' in result.output
        assert '--backend-set-name' in result.output

    def test_attach_lb(self):
        result = util.invoke_command(['compute-management', 'instance-pool', 'lb-attachment', 'attach'])
        assert 'Error: Missing option(s)' in result.output
        assert '--instance-pool-id' in result.output
        assert '--load-balancer-id' in result.output
        assert '--port' in result.output
        assert '--backend-set-name' in result.output
        assert '--vnic-selection' in result.output

    def test_detach_lb(self):
        result = util.invoke_command(['compute-management', 'instance-pool', 'lb-attachment', 'detach'])
        assert 'Error: Missing option(s)' in result.output
        assert '--instance-pool-id' in result.output
        assert '--load-balancer-id' in result.output
        assert '--backend-set-name' in result.output
