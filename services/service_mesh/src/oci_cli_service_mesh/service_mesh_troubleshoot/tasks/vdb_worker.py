# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.task_request import TaskRequestType, \
    PodTaskRequest, TaskConfiguration
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.task_worker import MeshTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.summary import MeshData

TASK_CONFIGURATIONS = [
    TaskConfiguration.LOGS,
    TaskConfiguration.CONFIG_DUMP,
    TaskConfiguration.PROXY_STATS,
    TaskConfiguration.POD_SUMMARY
]


class VdbTask(MeshTask):
    def __init__(self, k8s_context=None):
        super(VdbTask, self).__init__(TaskRequestType.VDB_PROCESSOR)
        self.k8s_context = k8s_context

    def do_work(self, task_request, kube_command_helper):
        output_events, tasks = [], []
        try:
            data = task_request.get_task_data()
            mesh_dict = data['mesh_dict']
            vdb_pods_dict = data['vdb_pods_dict']

            # Loop through all the Meshes
            for mesh_id, vs_dict in mesh_dict.items():
                # Loop through all VS under Mesh
                for vs_id, vd_dict in vs_dict.items():
                    # Loop through all VD under VS
                    for vd_id, vdb_list in vd_dict.items():
                        # Loop through the VDBs
                        for vdb_ref in vdb_list:
                            vdb_pods_list = vdb_pods_dict.get(vdb_ref)
                            # Iterate through all the pods
                            for pod_summary in vdb_pods_list:
                                # Append the pod_task_request to tasks queue
                                mesh_data = MeshData(mesh_id=mesh_id, vs_id=vs_id, vd_id=vd_id, vdb_key=vdb_ref)
                                pod_task_request = PodTaskRequest(TaskRequestType.POD_PROCESSOR,
                                                                  TASK_CONFIGURATIONS,
                                                                  pod_summary,
                                                                  mesh_data)
                                tasks.append(pod_task_request)
            return tasks, output_events
        except Exception as error:
            click.echo('VdbTask Exception: {}'.format(error))
