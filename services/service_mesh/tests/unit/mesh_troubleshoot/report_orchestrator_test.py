# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import unittest
from unittest.mock import Mock
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.report_orchestrator import ClientHandler
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.handlers.debug_handler import ResultStatus, Result
MESH_ID = 'ocid1.mesh.oc1.iad.valid'


class TestClientHandler(unittest.TestCase):

    def test_handler_valid_ocid(self):
        debug_handler = Mock()
        debug_handler.handle.return_value = Result(status=ResultStatus.OK, data={})
        self.k8s_context = (None, None)
        client_handler = ClientHandler(debug_handler, 'ocid1.mesh.oc1.iad.valid', self.k8s_context)
        actual_result = client_handler.handle()
        self.assertIsNone(actual_result)

    def test_handle_oci_none(self):
        debug_handler = Mock()
        debug_handler.handle.return_value = Result(status=ResultStatus.INTERNAL_ERROR, exception='ocid is none')
        self.k8s_context = (None, None)
        client_handler = ClientHandler(debug_handler, None, self.k8s_context)
        actual_result = client_handler.handle()
        self.assertIsNotNone(actual_result)

    def test_handler_invalid_ocid(self):
        debug_handler = Mock()
        debug_handler.handle.return_value = Result(status=ResultStatus.INTERNAL_ERROR, exception='invalid ocid')
        self.k8s_context = (None, None)
        client_handler = ClientHandler(debug_handler, 'ocid.i.am.invalid', self.k8s_context)
        actual_result = client_handler.handle()
        self.assertIsNotNone(actual_result)
