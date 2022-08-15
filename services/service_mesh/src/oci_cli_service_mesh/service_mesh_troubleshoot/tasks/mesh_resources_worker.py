# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.task_request import TaskRequest, \
    TaskRequestType
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.task_worker import MeshTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.bundle_helper import \
    save_custom_resource_as_yaml


class MeshResourcesTask(MeshTask):
    def __init__(self, k8s_context=None):
        super(MeshResourcesTask, self).__init__(TaskRequestType.MESH_RESOURCES_PROCESSOR)
        self.k8s_context = k8s_context

    def do_work(self, task_request: TaskRequest, kube_command_helper):
        tasks, output_events = [], []
        try:
            data = task_request.get_task_data()
            mesh_id = data['mesh_id']

            # Fetch all the mesh resources and save as yaml
            mesh_resources = kube_command_helper.parallel_filter_mesh_resources(mesh_id)
            all_crds = []
            for mesh_id, crd_list in mesh_resources.mesh_dict.items():
                all_crds.extend(crd_list)
            for vs_id, crd_list in mesh_resources.vs_dict.items():
                all_crds.extend(crd_list)
            for vd_id, crd_list in mesh_resources.vd_dict.items():
                all_crds.extend(crd_list)
            for vdb_id, crd_list in mesh_resources.vdb_dict.items():
                all_crds.extend(crd_list)
            for vsrt_id, crd_list in mesh_resources.vsrt_dict.items():
                all_crds.extend(crd_list)
            for ig_id, crd_list in mesh_resources.ig_dict.items():
                all_crds.extend(crd_list)
            for igrt_id, crd_list in mesh_resources.igrt_dict.items():
                all_crds.extend(crd_list)
            for ap_id, crd_list in mesh_resources.ap_dict.items():
                all_crds.extend(crd_list)

            for crd in all_crds:
                save_custom_resource_as_yaml(mesh_id, crd)
            return tasks, output_events

        except Exception as error:
            click.echo('MeshResourcesTask Exception: {}'.format(error))
