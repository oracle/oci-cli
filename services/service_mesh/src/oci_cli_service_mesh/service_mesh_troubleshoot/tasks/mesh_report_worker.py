# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.task_request import TaskRequest, \
    TaskRequestType, TaskConfiguration, NamespacesTaskRequest, CommonTaskRequest, OciCliVersionTaskRequest, \
    ValidateCrdsTaskRequest, WebhooksTaskRequest, ObservabilityTaskRequest, ServicesTaskRequest
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.task_worker import MeshTask


class MeshReportTask(MeshTask):
    def __init__(self, k8s_context=None):
        super(MeshReportTask, self).__init__(TaskRequestType.MESH_REPORT_PROCESSOR)
        self.k8s_context = k8s_context

    def do_work(self, task_request: TaskRequest, kube_command_helper):
        data = task_request.get_task_data()
        mesh_id = data['mesh_id']
        output_events, tasks = [], []
        try:
            # OCI CLI VERSION
            oci_cli_version_task_request = OciCliVersionTaskRequest(TaskRequestType.OCI_CLI_VERSION_PROCESSOR,
                                                                    [],
                                                                    mesh_id)
            tasks.append(oci_cli_version_task_request)

            # OSOK, OLM, CM, METRICS_SERVER and CATALOG_PROCESSOR
            for task_request_identifier in [TaskRequestType.OSOK_PROCESSOR, TaskRequestType.OLM_PROCESSOR,
                                            TaskRequestType.METRICS_PROCESSOR, TaskRequestType.CATALOG_PROCESSOR]:
                task_configurations = [TaskConfiguration.POD_SUMMARY]
                if task_request_identifier in [TaskRequestType.OSOK_PROCESSOR, TaskRequestType.OLM_PROCESSOR,
                                               TaskRequestType.CATALOG_PROCESSOR]:
                    task_configurations.append(TaskConfiguration.LOGS)
                generic_task_request = CommonTaskRequest(TaskRequestType.COMMON_PROCESSOR,
                                                         task_configurations,
                                                         mesh_id,
                                                         task_request_identifier)
                tasks.append(generic_task_request)

            # CRDs installed
            validate_crds_task_request = ValidateCrdsTaskRequest(TaskRequestType.VALIDATE_CRDS_PROCESSOR, [], mesh_id)
            tasks.append(validate_crds_task_request)

            # webhooks
            webhooks_task_request = WebhooksTaskRequest(TaskRequestType.WEBHOOKS_PROCESSOR, [], mesh_id)
            tasks.append(webhooks_task_request)

            # search prometheus and grafana
            observability_task_request = ObservabilityTaskRequest(TaskRequestType.OBSERVABILITY_PROCESSOR, [], mesh_id)
            tasks.append(observability_task_request)

            # check services
            services_task_request = ServicesTaskRequest(TaskRequestType.SERVICES_PROCESSOR, [], mesh_id)
            tasks.append(services_task_request)

            # Sidecar injection enabled namespaces
            namespaces_task_request = NamespacesTaskRequest(TaskRequestType.NAMESPACES_PROCESSOR, [], mesh_id)
            tasks.append(namespaces_task_request)

            return tasks, output_events

        except Exception as error:
            click.echo('MeshReportTask Exception: {}'.format(error))
