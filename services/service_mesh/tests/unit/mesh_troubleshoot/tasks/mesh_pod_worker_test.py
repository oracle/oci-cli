# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import json
import unittest
from unittest.mock import Mock

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import TaskRequestType, \
    PodTaskRequest, PodTask, TaskConfiguration, BasicPodSummary, MeshData, PodSummary

MESH_ID = 'ocid1.mesh.oc1.iad.valid'
VS_ID = 'ocid1.meshvirtualservice.oc1.iad.valid'
VD_ID = 'ocid1.meshvirtualdeployment.oc1.iad.valid'
vdb_key = 'book-info/ratings'


class TestPodWorker(unittest.TestCase):

    def test_data_in_output_event(self):
        kube_command_helper = Mock()
        content = {
            "configs": [
                {
                    "@type": "type.googleapis.com/envoy.admin.v3.ClustersConfigDump",
                    "dynamic_active_clusters": [{
                        "version_info": "5"
                    }]
                }
            ]
        }
        config_content = json.dumps(content)
        config_json_content = json.loads(config_content)
        kube_command_helper.get_proxy_logs.return_value = 'Proxy logs content'
        kube_command_helper.get_config_dump.return_value = config_json_content
        kube_command_helper.get_proxy_stats.return_value = '{}'

        task_configurations = [
            TaskConfiguration.LOGS,
            TaskConfiguration.CONFIG_DUMP,
            TaskConfiguration.POD_SUMMARY,
            TaskConfiguration.PROXY_STATS
        ]

        basic_pod_summary = BasicPodSummary(name='rating-v1-123',
                                            namespace='book-info',
                                            version='1.10',
                                            status='Running')
        mesh_data = MeshData(mesh_id=MESH_ID,
                             vs_id=VS_ID,
                             vd_id=VD_ID,
                             vdb_key=vdb_key)
        pod_summary = PodSummary(basic_pod_summary=basic_pod_summary,
                                 pod_json='{}')

        pod_task_request = PodTaskRequest(TaskRequestType.POD_PROCESSOR,
                                          task_configurations,
                                          pod_summary,
                                          mesh_data)
        pod_task = PodTask()

        tasks, output_events = pod_task.do_work(pod_task_request,
                                                kube_command_helper=kube_command_helper)
        # There should be 3 tasks, 1 output_events
        self.assertTrue(len(tasks) == 3)
        self.assertTrue(len(output_events) == 1)

        expected_task_request_type = TaskRequestType.FILE_PROCESSOR
        for task in tasks:
            self.assertTrue(task.task_request_type.value == expected_task_request_type.value)
