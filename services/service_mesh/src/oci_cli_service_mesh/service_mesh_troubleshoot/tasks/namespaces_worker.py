# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.event import Event, EventType, \
    OperationType
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.task_request import TaskRequest, \
    TaskRequestType
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.task_worker import MeshTask


class NamespacesTask(MeshTask):
    def __init__(self, k8s_context=None):
        super(NamespacesTask, self).__init__(TaskRequestType.NAMESPACES_PROCESSOR)
        self.k8s_context = k8s_context

    def do_work(self, task_request: TaskRequest, kube_command_helper):
        output_events, tasks = [], []
        try:
            data = task_request.get_task_data()
            mesh_id = data['mesh_id']

            sidecar_enabled_namespaces = kube_command_helper.get_namespaces_with_sidecar_injection_enabled()
            event = Event(event_type=EventType.SIDECAR_INJECTION_ENABLED_NAMESPACES,
                          operations={OperationType.STORE_SINGLE_EVENT},
                          data=sidecar_enabled_namespaces,
                          identifications={mesh_id: None},
                          store={mesh_id})
            output_events.append(event)
            return tasks, output_events
        except Exception as error:
            click.echo('NamespacesTask Exception: {}'.format(error))
