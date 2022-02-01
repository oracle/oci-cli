# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestNodePoolCreateUpdate(unittest.TestCase):
    def setUp(self):
        pass

    def test_nodepool_create(self):
        result = util.invoke_command(['ce', 'node-pool', 'create', '--size', '1', '--nsg-ids', 'nsgs', '--defined-tags', 'definedTags', '--freeform-tags', 'freeformTags', '--node-defined-tags', 'tag', '--node-freeform-tags', 'tag', '--kms-key-id', 'kmskey', '--is-pv-encryption-in-transit-enabled', 'true', '--placement-configs', 'config'])
        assert 'Error: Missing option(s)' in result.output

    def test_nodepool_update(self):
        result = util.invoke_command(['ce', 'node-pool', 'update', '--size', '1', '--nsg-ids', 'nsgs', '--defined-tags', 'definedTags', '--freeform-tags', 'freeformTags', '--node-defined-tags', 'tag', '--node-freeform-tags', 'tag', '--kms-key-id', 'kmskey', '--is-pv-encryption-in-transit-enabled', 'true', '--placement-configs', 'config', '--node-source-details', '{"foo", "bar"}', '--ssh-public-key', 'key', '--node-shape', 'shape', '--node-metadata', '{"foo", "bar"}'])
        assert 'Error: Missing option(s) --node-pool-id.' in result.output

    def test_nodepool_create_via_imageId_and_bootVolumeSize_shortcuts(self):
        result = util.invoke_command(['ce', 'node-pool', 'create', '--node-image-id', 'id', '--node-boot-volume-size-in-gbs', '100'])
        assert 'Error: Missing option(s)' in result.output

    def test_nodepool_create_error_with_multiple_image_sources(self):
        result = util.invoke_command(['ce', 'node-pool', 'create', '--compartment-id', 'compartment', '--cluster-id', 'id', '--name', 'name', '--node-shape', 'shape', '--kubernetes-version', 'version', '--node-image-id', 'id', '--node-source-details', '{"foo", "bar"}'])
        assert 'UsageError' in result.output
        assert 'Cannot specify --node-source-details with any of: --node-image-id or --node-boot-volume-size-in-gbs' in result.output

    def test_nodepool_create_error_with_multiple_boot_volume_size_sources(self):
        result = util.invoke_command(['ce', 'node-pool', 'create', '--compartment-id', 'compartment', '--cluster-id', 'id', '--name', 'name', '--node-shape', 'shape', '--kubernetes-version', 'version', '--node-boot-volume-size-in-gbs', '100', '--node-source-details', '{"foo", "bar"}'])
        assert 'UsageError' in result.output
        assert 'Cannot specify --node-source-details with any of: --node-image-id or --node-boot-volume-size-in-gbs' in result.output

    def test_nodepool_create_error_bootVolumeSize_shortcut_but_no_image_id(self):
        result = util.invoke_command(['ce', 'node-pool', 'create', '--compartment-id', 'compartment', '--cluster-id', 'id', '--name', 'name', '--node-shape', 'shape', '--kubernetes-version', 'version', '--node-boot-volume-size-in-gbs', '100'])
        assert 'UsageError' in result.output
        assert 'Cannot specify --node-boot-volume-size-in-gbs without --node-image-id' in result.output
