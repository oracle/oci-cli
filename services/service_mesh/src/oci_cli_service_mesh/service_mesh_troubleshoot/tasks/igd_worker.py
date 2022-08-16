# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.task_request import TaskRequestType, \
    TaskRequest, PodTaskRequest, TaskConfiguration
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.task_worker import MeshTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.summary import MeshData

TASK_CONFIGURATIONS = [
    TaskConfiguration.LOGS,
    TaskConfiguration.CONFIG_DUMP,
    TaskConfiguration.POD_SUMMARY,
    TaskConfiguration.PROXY_STATS
]


class IgdTask(MeshTask):
    def __init__(self, k8s_context=None):
        super(IgdTask, self).__init__(TaskRequestType.IGD_PROCESSOR)
        self.k8s_context = k8s_context

    def do_work(self, task_request: TaskRequest, kube_command_helper):
        tasks, output_events = [], []
        try:
            data = task_request.get_task_data()
            mesh_dict = data['mesh_dict']
            igd_pods_dict = data['igd_pods_dict']

            # Loop through all the Meshes
            for mesh_id, ig_dict in mesh_dict.items():
                # Loop through all IG under Mesh
                for ig_id, igd_list in ig_dict.items():
                    for igd_name in igd_list:
                        igd_pods_list = igd_pods_dict.get(igd_name)
                        # Iterate through all the pods
                        for pod_summary in igd_pods_list:
                            # Append the pod_task_request to tasks queue
                            mesh_data = MeshData(mesh_id=mesh_id, ig_id=ig_id, igd_key=igd_name)
                            pod_task_request = PodTaskRequest(TaskRequestType.POD_PROCESSOR,
                                                              TASK_CONFIGURATIONS,
                                                              pod_summary,
                                                              mesh_data)
                            tasks.append(pod_task_request)
            return tasks, output_events
        except Exception as error:
            click.echo('IgdTask Exception: {}'.format(error))
