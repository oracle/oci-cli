# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.task_request import TaskRequestType, \
    VdbTaskRequest, TaskConfiguration, IgdTaskRequest, MeshReportTaskRequest, MeshResourcesTaskRequest
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.task_worker import MeshTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.constants import VS_PLURAL, \
    MESH_PLURAL, VD_PLURAL, IG_PLURAL
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.helper import \
    get_resource_type_from_ocid, MeshTaskException
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.messages import Messages


class ResourceTask(MeshTask):
    def __init__(self, k8s_context=None):
        super(ResourceTask, self).__init__(TaskRequestType.RESOURCE_PROCESSOR)
        self.k8s_context = k8s_context

    def do_work(self, task_request, kube_command_helper):
        output_events, tasks = [], []
        try:
            data = task_request.get_task_data()
            resource_id = data['resource_id']
            if resource_id is None:
                # Mesh Report Task
                mesh_report_task_request = MeshReportTaskRequest(TaskRequestType.MESH_REPORT_PROCESSOR, [], resource_id)
                tasks.append(mesh_report_task_request)

            else:
                resource_type = get_resource_type_from_ocid(resource_id)
                meshes_list = []

                # VDBs
                if resource_type in [VS_PLURAL, VD_PLURAL, MESH_PLURAL]:
                    mesh_vdb_dict = kube_command_helper.filter_vdbs_by_ocid(resource_id)
                    vdb_pods_dict = kube_command_helper.filter_all_pods_related_to_vdbs()
                    if len(mesh_vdb_dict) > 0:
                        binding_task_request = VdbTaskRequest(TaskRequestType.VDB_PROCESSOR,
                                                              [TaskConfiguration.CHILD_RESOURCES],
                                                              mesh_vdb_dict,
                                                              vdb_pods_dict)
                        tasks.append(binding_task_request)
                    meshes_list = meshes_list + list(mesh_vdb_dict.keys())

                # IGDs
                if resource_type in [IG_PLURAL, MESH_PLURAL]:
                    mesh_igd_dict = kube_command_helper.filter_igds_by_ocid(resource_id)
                    igd_pods_dict = kube_command_helper.filter_all_pods_related_to_igds()
                    if len(mesh_igd_dict) > 0:
                        igd_task_request = IgdTaskRequest(TaskRequestType.IGD_PROCESSOR,
                                                          [TaskConfiguration.CHILD_RESOURCES],
                                                          mesh_igd_dict,
                                                          igd_pods_dict)
                        tasks.append(igd_task_request)
                    meshes_list = meshes_list + list(mesh_igd_dict.keys())
                meshes = set(meshes_list)
                if len(meshes) > 0:
                    for mesh_id in meshes:
                        # Mesh Report Task
                        mesh_report_task_request = MeshReportTaskRequest(TaskRequestType.MESH_REPORT_PROCESSOR, [], mesh_id)
                        tasks.append(mesh_report_task_request)

                        # Mesh Resources Task
                        mesh_resources_task_request = MeshResourcesTaskRequest(TaskRequestType.MESH_RESOURCES_PROCESSOR,
                                                                               [], mesh_id)
                        tasks.append(mesh_resources_task_request)
            if not tasks and not output_events:
                raise MeshTaskException()
            return tasks, output_events
        except MeshTaskException:
            click.echo(Messages.is_invalid)
        except Exception as error:
            click.echo('ResourceTask Exception: {}'.format(error))
