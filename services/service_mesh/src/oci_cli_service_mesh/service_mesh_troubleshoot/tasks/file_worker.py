# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.task_request import TaskRequest, \
    TaskRequestType
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.task_worker import MeshTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.bundle_helper import \
    create_directory, BundleHelper


class FileTask(MeshTask):
    def __init__(self, k8s_context=None):
        super(FileTask, self).__init__(TaskRequestType.FILE_PROCESSOR)
        self.k8s_context = k8s_context

    def do_work(self, task_request: TaskRequest, kube_command_helper):

        try:
            data = task_request.get_task_data()
            relative_path = data['relative_path']
            file_name = data['file_name']
            contents = data['contents']
            directory_path = create_directory(relative_path)
            # Save contents to file
            if '.json' in file_name:
                BundleHelper.save_contents_as_json(directory_path, file_name, contents)
            else:
                BundleHelper.dump_contents_to_file(directory_path, file_name, contents)
            return [], []
        except Exception as error:
            click.echo('FileTask Exception: {}'.format(error))
