# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import unittest
from unittest.mock import Mock

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import TaskConfiguration, \
    TaskRequestType, PodSummary, BasicPodSummary, IgdTask, IgdTaskRequest


class TestIgdWorker(unittest.TestCase):

    def test_data_in_output_event(self):
        kube_command_helper = Mock()

        mesh_igd_dict = {
            'ocid1.mesh.oc1.iad.valid': {
                'ocid1.meshingressgateway.oc1.iad.valid': ['book-info/book-info-ig-deployment']
            }
        }

        igd_pods_dict = {
            'book-info/book-info-ig-deployment': [PodSummary(proxy_version='0.1.348',
                                                             proxy_status='Running',
                                                             pod_json={},
                                                             basic_pod_summary=BasicPodSummary(
                                                                 name='bookinfo-ig-deployment-deployment-5c6d89b',
                                                                 namespace='book-info',
                                                                 version='1.2.3',
                                                                 status='Pending'))]
        }

        igd_task_request = IgdTaskRequest(TaskRequestType.IGD_PROCESSOR,
                                          [TaskConfiguration.CHILD_RESOURCES],
                                          mesh_igd_dict,
                                          igd_pods_dict)
        igd_task = IgdTask()

        tasks, output_events = igd_task.do_work(igd_task_request,
                                                kube_command_helper=kube_command_helper)
        # There should be 1 tasks, 0 output_events
        self.assertTrue(len(tasks) == 1)
        self.assertTrue(len(output_events) == 0)

        expected_task_request_type = TaskRequestType.POD_PROCESSOR
        for task in tasks:
            self.assertTrue(task.task_request_type.value == expected_task_request_type.value)
