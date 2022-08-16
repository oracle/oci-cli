# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import unittest
from unittest.mock import Mock

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import TaskRequestType, \
    NamespacesTaskRequest, NamespacesTask, OperationType, EventType

MESH_ID = 'ocid1.mesh.oc1.iad.valid'


class TestNamespacesWorker(unittest.TestCase):

    def test_data_in_output_event(self):
        kube_command_helper = Mock()
        expected_namespaces_list = ['long-canary', 'fast-canary', 'slow-canary']
        kube_command_helper.get_namespaces_with_sidecar_injection_enabled.return_value = expected_namespaces_list

        namespaces_task_request = NamespacesTaskRequest(TaskRequestType.NAMESPACES_PROCESSOR, [], MESH_ID)
        namespaces_task = NamespacesTask()

        tasks, output_events = namespaces_task.do_work(namespaces_task_request,
                                                       kube_command_helper=kube_command_helper)
        # There should be 0 tasks, 1 output_event
        self.assertTrue(len(tasks) == 0)
        self.assertTrue(len(output_events) == 1)

        # Assert the event content
        output_event = output_events[0]
        self.assertTrue(output_event.event_type == EventType.SIDECAR_INJECTION_ENABLED_NAMESPACES)
        self.assertTrue(OperationType.STORE_SINGLE_EVENT in output_event.operations)
        self.assertTrue(MESH_ID in output_event.store)
        self.assertIsNotNone(output_event.data)
        actual_namespaces_list = output_event.data
        self.assertTrue(len(actual_namespaces_list) == len(expected_namespaces_list))
        expected_namespaces_list.sort()
        actual_namespaces_list.sort()
        self.assertTrue(actual_namespaces_list == expected_namespaces_list)
