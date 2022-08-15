# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import os
import shutil
import tempfile
import unittest
from unittest.mock import Mock

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.handlers.debug_handler import \
    DebugHandlerRequestType, OcidValidationHandler, Result, ResultStatus, K8sCheckHandler, BundleNameHandler, \
    BundleCompressHandler, BundleCleanupHandler
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.bundle_helper import BundleHelper
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.kubectl_command_helper import \
    KubectlCommandSummary


class TestDebugHandler(unittest.TestCase):
    def test_ocid_validation_handler(self):
        input_ocid_list = [
            None,
            'ocid.i.am.invalid',
            'ocid1.mesh.oc1.iad.valid'
        ]
        expected_result_status_list = [
            ResultStatus.NOT_FOUND,
            ResultStatus.INTERNAL_ERROR,
            ResultStatus.OK
        ]

        for i in range(len(input_ocid_list)):
            data = {'ocid': input_ocid_list[i]}
            request = {'type': DebugHandlerRequestType.OCID_VALIDATION, 'data': data}

            ocid_validation_handler = OcidValidationHandler()
            actual_result: Result = ocid_validation_handler.handle(request)

            # Assert
            self.assertTrue(actual_result.status == expected_result_status_list[i])

    def test_k8s_check_handler(self):
        kube_command_helper = Mock()
        mock_return_value_list = [KubectlCommandSummary(return_code=0, stdout='', stderr=''),
                                  KubectlCommandSummary(return_code=1, stdout='', stderr='')]
        expected_result_status_list = [ResultStatus.OK, ResultStatus.NOT_FOUND]

        for i in range(len(mock_return_value_list)):
            kube_command_helper.is_kubectl_installed.return_value = mock_return_value_list[i]

            request = {'type': DebugHandlerRequestType.K8S_CHECK, 'kube_command_helper': kube_command_helper}
            k8s_check_handler = K8sCheckHandler()
            actual_result: Result = k8s_check_handler.handle(request)

            # Assert
            self.assertTrue(actual_result.status == expected_result_status_list[i])

    def test_bundle_name_handler(self):
        request = {'type': DebugHandlerRequestType.BUNDLE_NAME}
        bundle_name_handler = BundleNameHandler()
        actual_result: Result = bundle_name_handler.handle(request)

        # Assert
        self.assertTrue(actual_result.status == ResultStatus.OK)

    def test_bundle_compress_handler(self):
        # create a directory in temp directory to compress
        directory_name = tempfile.gettempdir()
        bundle_name = BundleHelper.get_bundle_name()
        directory_path = os.path.join(directory_name, bundle_name)
        self.assertFalse(os.path.exists(directory_path))
        os.makedirs(directory_path)
        self.assertTrue(os.path.exists(directory_path))

        # let it compress
        data = {
            'directory_name': directory_name,
            'bundle_name': bundle_name
        }
        request = {'type': DebugHandlerRequestType.BUNDLE_COMPRESS, 'data': data}
        bundle_compress_handler = BundleCompressHandler()
        actual_result: Result = bundle_compress_handler.handle(request)

        # Assert, Validate
        self.assertTrue(actual_result.status == ResultStatus.OK)
        zip_name = BundleHelper.get_bundle_name() + '.zip'
        bundle_path = os.path.join(directory_name, zip_name)
        self.assertTrue(os.path.exists(bundle_path))
        shutil.rmtree(directory_path, ignore_errors=True)
        shutil.rmtree(bundle_path, ignore_errors=True)

    def test_bundle_cleanup_handler(self):
        # create a directory in temp directory to compress
        directory_name = tempfile.gettempdir()
        bundle_name = BundleHelper.get_bundle_name() + '.zip'
        directory_path = os.path.join(directory_name, bundle_name)
        self.assertFalse(os.path.exists(directory_path))
        os.makedirs(directory_path)
        self.assertTrue(os.path.exists(directory_path))

        # Let it delete
        data = {
            'directory_name': directory_name,
            'bundle_name': bundle_name
        }
        request = {'type': DebugHandlerRequestType.BUNDLE_CLEANUP, 'data': data}
        bundle_cleanup_handler = BundleCleanupHandler()
        actual_result: Result = bundle_cleanup_handler.handle(request)

        # Assert
        self.assertTrue(actual_result.status == ResultStatus.OK)
        shutil.rmtree(directory_path, ignore_errors=True)
        self.assertFalse(os.path.exists(directory_path))
