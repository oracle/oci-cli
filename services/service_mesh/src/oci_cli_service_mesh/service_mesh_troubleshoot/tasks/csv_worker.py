# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates. All rights reserved.
import click

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.task_request import TaskRequest, \
    TaskRequestType, FileTaskRequest
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.task_worker import MeshTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.bundle_helper import \
    BundleHelper
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.summary import MeshData


class CsvTask(MeshTask):
    def __init__(self, k8s_context=None):
        super(CsvTask, self).__init__(TaskRequestType.CSV_PROCESSOR)
        self.k8s_context = k8s_context

    def do_work(self, task_request: TaskRequest, kube_command_helper):
        try:
            output_events, tasks = [], []
            data = task_request.get_task_data()
            operator_namespace = data['operator_namespace']
            mesh_id = data['mesh_id']

            csv = kube_command_helper.get_csv(operator_namespace)

            if mesh_id is None:
                relative_path = ""
            else:
                relative_path = MeshData(mesh_id=mesh_id).get_mesh_hierarchy()
            file_task_request = FileTaskRequest(TaskRequestType.FILE_PROCESSOR,
                                                [],
                                                relative_path,
                                                BundleHelper.get_csv_file_name(),
                                                csv)
            tasks.append(file_task_request)
            return tasks, output_events
        except Exception as error:
            click.echo('CsvTask Exception: {}'.format(error))
