# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import unittest
from unittest.mock import Mock
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import TaskRequestType, \
    WebhooksTask, WebhooksTaskRequest, OperationType, EventType

MESH_ID = 'ocid1.mesh.oc1.iad.valid'


class TestWebhooksWorker(unittest.TestCase):

    def test_data_in_output_event(self):
        kube_command_helper = Mock()
        expected_list = ["ap-validator.servicemesh.oci.oracle.cloud.com",
                         "ig-validator.servicemesh.oci.oracle.cloud.com",
                         "igd-validator.servicemesh.oci.oracle.cloud.com",
                         "igrt-validator.servicemesh.oci.oracle.cloud.com",
                         "mesh-validator.servicemesh.oci.oracle.cloud.com",
                         "vd-validator.servicemesh.oci.oracle.cloud.com",
                         "vdb-validator.servicemesh.oci.oracle.cloud.com",
                         "vs-validator.servicemesh.oci.oracle.cloud.com",
                         "vsrt-validator.servicemesh.oci.oracle.cloud.com",
                         "proxy-injector.servicemesh.oci.oracle.com"]

        kube_command_helper.get_webhooks_validated.return_value = expected_list

        webhooks_task_request = WebhooksTaskRequest(TaskRequestType.WEBHOOKS_PROCESSOR, [], MESH_ID)
        webhooks_task = WebhooksTask()

        tasks, output_events = webhooks_task.do_work(webhooks_task_request,
                                                     kube_command_helper=kube_command_helper)
        # There should be 0 tasks, 1 output_event
        self.assertTrue(len(tasks) == 0)
        self.assertTrue(len(output_events) == 1)

        # Assert the event content
        output_event = output_events[0]
        self.assertTrue(output_event.event_type == EventType.SERVICE_MESH_WEBHOOKS)
        self.assertTrue(OperationType.STORE_SINGLE_EVENT in output_event.operations)
        self.assertTrue(MESH_ID in output_event.store)
        self.assertIsNotNone(output_event.data)
        actual_webhooks_list = output_event.data
        self.assertTrue(len(actual_webhooks_list) == len(expected_list))
        expected_list.sort()
        actual_webhooks_list.sort()
        self.assertTrue(actual_webhooks_list == expected_list)
