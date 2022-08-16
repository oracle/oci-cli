# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import os
import shutil
import tempfile
import unittest
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.bundle_helper import BundleHelper

MESH_ID = 'ocid1.mesh.oc1.iad.valid'


class TestBundleHelper(unittest.TestCase):

    def test_bundle_name(self):
        self.assertIsNotNone(BundleHelper.get_bundle_name())

    def test_home_directory(self):
        self.assertEqual(os.path.expanduser('~'), BundleHelper.get_home_directory())

    def test_report_file_name(self):
        expected_file_name = 'report-{}.json'.format(MESH_ID)
        self.assertEqual(expected_file_name, BundleHelper.get_report_file_name(MESH_ID))

    def test_config_dump_file_name(self):
        name = 'ratings-123'
        namespace = 'book-info'
        expected_file_name = 'config_dump-{}_{}.json'.format(name, namespace)
        self.assertEqual(expected_file_name,
                         BundleHelper.get_config_dump_file_name(name, namespace))

    def test_custom_resource_file_name(self):
        name = 'ratings'
        namespace = 'book-info'
        kind = 'VirtualService'
        expected_file_name = 'cr_{}-{}_{}.yaml'.format(kind, name, namespace)
        self.assertEqual(expected_file_name,
                         BundleHelper.get_custom_resource_file_name(name, namespace, kind))

    def test_compress_bundle(self):
        directory_name = tempfile.gettempdir()
        bundle_name = BundleHelper.get_bundle_name()
        complete_path = os.path.join(directory_name, bundle_name)
        # Create a bundle directory
        os.makedirs(complete_path, exist_ok=True)
        self.assertTrue(os.path.exists(complete_path))
        # Zip using compress bundle
        BundleHelper.compress_bundle(directory_name, bundle_name)
        # Assert for the existence of the bundle zip
        self.assertTrue(os.path.exists(complete_path + '.zip'))
        # Cleanup
        shutil.rmtree(complete_path)
        os.remove(complete_path + '.zip')
        self.assertFalse(os.path.exists(complete_path + '.zip'))

    def test_cleanup(self):
        directory_name = tempfile.gettempdir()
        bundle_name = BundleHelper.get_bundle_name()
        complete_path = os.path.join(directory_name, bundle_name)
        # Create a bundle directory
        os.makedirs(complete_path, exist_ok=True)
        self.assertTrue(os.path.exists(complete_path))
        # Delete using BundleHelper
        BundleHelper.cleanup(directory_name, bundle_name)
        # Assert the non-existence of the bundle
        self.assertFalse(os.path.exists(complete_path))

    def test_dump_contents_to_file(self):
        directory_name = tempfile.gettempdir()
        file_name = 'osok.log'
        expected_contents = 'This contains osok logs'
        # Dump using BundleHelper
        BundleHelper.dump_contents_to_file(directory_name, file_name, expected_contents)
        complete_path = os.path.join(directory_name, file_name)
        # Assert the existence and the contents
        self.assertTrue(os.path.exists(complete_path))
        with open(complete_path) as f:
            actual_contents = f.read()
            # print('Actual: {}'.format(actual_contents))
            self.assertTrue(expected_contents in actual_contents)
        # Cleanup
        os.remove(complete_path)
        self.assertFalse(os.path.exists(complete_path))

    def test_save_contents_as_json(self):
        directory_name = tempfile.gettempdir()
        file_name = 'pod-ratings_bookinfo.json'
        expected_contents = '{\'name\': \'ratings\'}'
        # Dump using BundleHelper
        BundleHelper.save_contents_as_json(directory_name, file_name, expected_contents)
        complete_path = os.path.join(directory_name, file_name)
        # Assert the existence and the contents
        self.assertTrue(os.path.exists(complete_path))
        with open(complete_path) as f:
            actual_contents = f.read()
            # print('Actual: {}'.format(actual_contents))
            self.assertTrue(expected_contents in actual_contents)
        # Cleanup
        os.remove(complete_path)
        self.assertFalse(os.path.exists(complete_path))
