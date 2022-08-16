# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import unittest
from unittest.mock import Mock

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import TaskRequestType, \
    CsvTaskRequest, CsvTask

MESH_ID = 'ocid1.mesh.oc1.iad.valid'


class TestCsvWorker(unittest.TestCase):

    def test_data_in_output_event(self):
        kube_command_helper = Mock()
        kube_command_helper.get_status_of_csv.return_value = '{}'

        csv_task_request = CsvTaskRequest(TaskRequestType.CSV_PROCESSOR,
                                          [],
                                          'oci-service-operator-system',
                                          MESH_ID)
        csv_task = CsvTask()

        tasks, output_events = csv_task.do_work(csv_task_request,
                                                kube_command_helper=kube_command_helper)
        # There should be 0 tasks, 1 output_event
        self.assertTrue(len(tasks) == 1)
        self.assertTrue(len(output_events) == 0)

        # Assert the event content
        task = tasks[0]
        self.assertTrue(task.task_request_type == TaskRequestType.FILE_PROCESSOR)
        self.assertTrue(task.file_name == "csv.json")
