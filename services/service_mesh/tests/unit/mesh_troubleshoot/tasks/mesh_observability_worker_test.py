# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import unittest
from unittest.mock import Mock

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import TaskRequestType, \
    ObservabilityTaskRequest, ObservabilityTask, OperationType, EventType

MESH_ID = 'ocid1.mesh.oc1.iad.valid'


class TestObservabilityWorker(unittest.TestCase):

    def test_data_in_output_event(self):
        kube_command_helper = Mock()
        result_dict = {"prometheus-version": "v2.31.1", "grafana-version": '7.5.2'}
        kube_command_helper.get_observability.return_value = result_dict
        observability_task_request = ObservabilityTaskRequest(TaskRequestType.OBSERVABILITY_PROCESSOR, [], MESH_ID)
        observability_task = ObservabilityTask()
        tasks, output_events = observability_task.do_work(observability_task_request,
                                                          kube_command_helper=kube_command_helper)
        # There should be 0 tasks and 2 output events
        self.assertTrue(len(tasks) == 0)
        self.assertTrue(len(output_events) == 2)
        actual_version_dict = {}
        # Assert the event content
        output_event_1 = output_events[0]
        self.assertTrue(output_event_1.event_type == EventType.PROMETHEUS_VERSION)
        self.assertTrue(OperationType.STORE_SINGLE_EVENT in output_event_1.operations)
        self.assertTrue(MESH_ID in output_event_1.store)
        self.assertIsNotNone(output_event_1.data)
        actual_version_dict["prometheus-version"] = output_event_1.data
        output_event_2 = output_events[1]
        self.assertTrue(output_event_2.event_type == EventType.GRAFANA_VERSION)
        self.assertTrue(OperationType.STORE_SINGLE_EVENT in output_event_2.operations)
        self.assertTrue(MESH_ID in output_event_2.store)
        self.assertIsNotNone(output_event_2.data)
        actual_version_dict["grafana-version"] = output_event_2.data
        self.assertTrue(actual_version_dict == result_dict)
