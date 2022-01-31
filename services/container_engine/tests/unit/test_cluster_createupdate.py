# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestClusterCreate(unittest.TestCase):
    def setUp(self):
        pass

    def test_cluster_create_error_with_public_ip_enabled_and_missing_subnet_id(self):
        result = util.invoke_command(['ce', 'cluster', 'create', '--compartment-id', 'compartment', '--name', 'name', '--defined-tags', 'definedTags', '--freeform-tags', 'freeformTags', '--kubernetes-version', 'version', '--vcn-id', 'id', '--endpoint-public-ip-enabled', 'false'])
        assert 'UsageError' in result.output
        assert 'Cannot specify --endpoint-public-ip-enabled without --endpoint-subnet-id' in result.output

    def test_cluster_create_error_with_nsg_ids_and_missing_subnet_id(self):
        result = util.invoke_command(['ce', 'cluster', 'create', '--compartment-id', 'compartment', '--name', 'name', '--kubernetes-version', 'version', '--vcn-id', 'id', '--endpoint-nsg-ids', '["test"]'])
        assert 'UsageError' in result.output
        assert 'UsageError: Cannot specify --endpoint-nsg-ids without --endpoint-subnet-id' in result.output

    def test_cluster_update_endpoint_config_error_with_empty_cluster(self):
        result = util.invoke_command(['ce', 'cluster', 'update-endpoint-config', '--cluster-id', ''])
        assert 'UsageError' in result.output
        assert 'UsageError: Parameter --cluster-id cannot be whitespace or empty string' in result.output
