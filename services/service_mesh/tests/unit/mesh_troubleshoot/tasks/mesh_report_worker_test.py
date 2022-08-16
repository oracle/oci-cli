# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import unittest
from unittest.mock import Mock

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import TaskRequestType, \
    MeshReportTaskRequest, MeshReportTask

MESH_ID = 'ocid1.mesh.oc1.iad.valid'


class TestMeshReportWorker(unittest.TestCase):

    def test_data_in_output_event(self):
        kube_command_helper = Mock()

        mesh_report_task_request = MeshReportTaskRequest(TaskRequestType.MESH_REPORT_PROCESSOR, [], MESH_ID)
        mesh_report_task = MeshReportTask()

        tasks, output_events = mesh_report_task.do_work(mesh_report_task_request,
                                                        kube_command_helper=kube_command_helper)
        # There should be 6 tasks, 0 output_events
        self.assertTrue(len(tasks) == 10)
        self.assertTrue(len(output_events) == 0)

        expected_task_request_types = [TaskRequestType.COMMON_PROCESSOR.value,
                                       TaskRequestType.COMMON_PROCESSOR.value,
                                       TaskRequestType.COMMON_PROCESSOR.value,
                                       TaskRequestType.COMMON_PROCESSOR.value,
                                       TaskRequestType.NAMESPACES_PROCESSOR.value,
                                       TaskRequestType.OCI_CLI_VERSION_PROCESSOR.value,
                                       TaskRequestType.OBSERVABILITY_PROCESSOR.value,
                                       TaskRequestType.SERVICES_PROCESSOR.value,
                                       TaskRequestType.VALIDATE_CRDS_PROCESSOR.value,
                                       TaskRequestType.WEBHOOKS_PROCESSOR.value
                                       ]
        actual_task_request_types = []
        for task in tasks:
            actual_task_request_types.append(task.task_request_type.value)
        # Assert the task types
        expected_task_request_types.sort()
        actual_task_request_types.sort()
        self.assertTrue(actual_task_request_types == expected_task_request_types)
