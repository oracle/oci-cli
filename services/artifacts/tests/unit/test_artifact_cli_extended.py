# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestArtifact(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_container_configuration(self):
        result = util.invoke_command(['artifacts', 'container', 'configuration', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert 'compartment-id' in result.output

    def test_update_container_configuration(self):
        result = util.invoke_command(['artifacts', 'container', 'configuration', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert 'compartment-id' in result.output

    def test_delete_container_image(self):
        result = util.invoke_command(['artifacts', 'container', 'image', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert 'image-id' in result.output

    def test_get_container_image(self):
        result = util.invoke_command(['artifacts', 'container', 'image', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert 'image-id' in result.output

    def test_list_container_image(self):
        result = util.invoke_command(['artifacts', 'container', 'image', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'compartment-id' in result.output

    def test_remove_version_container_image(self):
        result = util.invoke_command(['artifacts', 'container', 'image', 'remove-version'])
        assert 'Error: Missing option(s)' in result.output
        assert 'image-id' in result.output
        assert 'image-version' in result.output
        result = util.invoke_command(['artifacts', 'container', 'image', 'remove-version',
                                      '--image-id', 'dummy'])
        assert 'Error: Missing option(s)' in result.output
        assert 'image-version' in result.output
        result = util.invoke_command(['artifacts', 'container', 'image', 'remove-version',
                                      '--image-version', 'dummy'])
        assert 'Error: Missing option(s)' in result.output
        assert 'image-id' in result.output

    def test_restore_container_image(self):
        result = util.invoke_command(['artifacts', 'container', 'image', 'restore'])
        assert 'Error: Missing option(s)' in result.output
        assert 'image-id' in result.output

    def test_change_compartment_container_repository(self):
        result = util.invoke_command(['artifacts', 'container', 'repository', 'change-compartment'])
        assert 'Error: Missing option(s)' in result.output
        assert 'compartment-id' in result.output
        assert 'repository-id' in result.output

        result = util.invoke_command(['artifacts', 'container', 'repository', 'change-compartment',
                                      '--compartment-id', 'dummy'])
        assert 'Error: Missing option(s)' in result.output
        assert 'repository-id' in result.output

        result = util.invoke_command(['artifacts', 'container', 'repository', 'change-compartment',
                                      '--repository-id', 'dummy'])
        assert 'Error: Missing option(s)' in result.output
        assert 'compartment-id' in result.output

    def test_create_container_repository(self):
        result = util.invoke_command(['artifacts', 'container', 'repository', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert 'compartment-id' in result.output
        assert 'display-name' in result.output
        result = util.invoke_command(['artifacts', 'container', 'repository', 'create',
                                      '--display-name', 'dummy'])
        assert 'Error: Missing option(s)' in result.output
        assert 'compartment-id' in result.output

        result = util.invoke_command(['artifacts', 'container', 'repository', 'create',
                                      '--compartment-id', 'dummy'])
        assert 'Error: Missing option(s)' in result.output
        assert 'display-name' in result.output

    def test_delete_container_repository(self):
        result = util.invoke_command(['artifacts', 'container', 'repository', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert 'repository-id' in result.output

    def test_get_container_repository(self):
        result = util.invoke_command(['artifacts', 'container', 'repository', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert 'repository-id' in result.output

    def test_list_container_repository(self):
        result = util.invoke_command(['artifacts', 'container', 'repository', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'compartment-id' in result.output

    def test_update_container_repository(self):
        result = util.invoke_command(['artifacts', 'container', 'repository', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert 'repository-id' in result.output

    def test_create_container_image_signature(self):
        result = util.invoke_command((['artifacts', 'container', 'image-signature', 'create']))
        assert 'Error: Missing option(s)' in result.output
        assert 'compartment-id' in result.output

    def test_delete_container_image_signature(self):
        result = util.invoke_command((['artifacts', 'container', 'image-signature', 'delete']))
        assert 'Error: Missing option(s)' in result.output
        assert 'image-signature-id' in result.output

    def test_get_container_image_signature(self):
        result = util.invoke_command((['artifacts', 'container', 'image-signature', 'get']))
        assert 'Error: Missing option(s)' in result.output
        assert 'image-signature-id' in result.output

    def test_list_container_image_signature(self):
        result = util.invoke_command((['artifacts', 'container', 'image-signature', 'list']))
        assert 'Error: Missing option(s)' in result.output
        assert 'compartment-id' in result.output

    def test_sign_and_upload_container_image_signature_metadata(self):
        command = ["artifacts", "container", "image-signature", "sign-upload"]
        result = util.invoke_command(command)
        assert 'Error: Missing option(s)' in result.output
        assert 'kms-key-id' in result.output
        assert 'kms-key-version-id' in result.output
        assert 'compartment-id' in result.output
        assert 'image-id' in result.output
        assert 'signing-algorithm' in result.output

    def test_get_and_verify_image_signature_metadata(self):
        result = util.invoke_command((['artifacts', 'container', 'image-signature', 'get-verify', '--trusted-keys', 'ocid.key.1', '--trusted-keys', 'ocid.key.2']))
        assert 'Error: Missing option(s)' in result.output
        assert 'compartment-id' in result.output
        assert 'repo-name' in result.output
        assert 'image-digest' in result.output
