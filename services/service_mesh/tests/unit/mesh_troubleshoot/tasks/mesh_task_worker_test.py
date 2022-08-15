# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import multiprocessing
import unittest
from unittest import mock
from unittest.mock import Mock

# Mock requests to control its behavior
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import CsvTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.task_request import ResourceTaskRequest, \
    TaskRequestType, TaskConfiguration
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.resource_worker import \
    ResourceTask


class TestResourceWorker(unittest.TestCase):
    def test_do_work(self):
        tests = [
            (
                {
                    "name": "VDB and IGD test ",
                    "task-request": ResourceTaskRequest(TaskRequestType.RESOURCE_PROCESSOR,
                                                        [TaskConfiguration.CHILD_RESOURCES],
                                                        "ocid1.mesh.oc1.iad.valid"),
                    "taskWorker": ResourceTask(),

                },
                {
                    "err": None
                }
            ),
            (
                {
                    "name": "VDB and IGD test ",
                    "task-request": ResourceTaskRequest(TaskRequestType.RESOURCE_PROCESSOR,
                                                        [TaskConfiguration.CHILD_RESOURCES],
                                                        "ocid1.mesh.oc1.iad.valid"),
                    "task-worker": CsvTask(),

                },
                {
                    "err": "Wrong request Type routed"
                }

            )

        ]
        for test_input, test_output in tests:
            try:
                taskWorker = test_input["task-worker"]
                m = multiprocessing.Manager()
                output_events, tasks = m.Queue(), m.Queue()

                taskWorker.execute(test_input["task-request"], output_events, tasks)
                assert output_events.empty() is True
                assert tasks.empty() is True
            except Exception as ex:
                if test_output["err"] is not None:
                    assert str(ex) == test_output["err"]


kube_command_helper = Mock()
task_request = Mock()

with mock.patch(
        'services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.resource_worker.ResourceTask.do_work') as MockClass:  # replace f1 with MockClass
    MockClass.side_effect = [], []  # Change the return value
