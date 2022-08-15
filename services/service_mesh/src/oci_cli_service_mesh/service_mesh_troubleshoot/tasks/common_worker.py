# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.event import Event, EventType, \
    OperationType
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.task_request import TaskRequest, \
    TaskRequestType, TaskConfiguration, FileTaskRequest, CsvTaskRequest
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.task_worker import MeshTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.bundle_helper import \
    BundleHelper
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.constants import \
    OLM_LABEL, OPERATOR_ANNOTATION, METRICS_SERVER_LABEL, CATALOG_OPERATOR_LABEL
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.summary import MeshData


class CommonTask(MeshTask):
    def __init__(self, k8s_context=None):
        super(CommonTask, self).__init__(TaskRequestType.COMMON_PROCESSOR)
        self.k8s_context = k8s_context

    def do_work(self, task_request: TaskRequest, kube_command_helper):
        tasks, output_events = [], []
        try:
            data = task_request.get_task_data()
            mesh_id = data['mesh_id']
            task_request_identifier = data['task_request_identifier']
            if mesh_id is None:
                relative_path = ""
            else:
                relative_path = MeshData(mesh_id=mesh_id).get_mesh_hierarchy()
            pod_summary = None

            for task_configuration in task_request.configurations:
                # Queue POD_SUMMARY Event
                if task_configuration == TaskConfiguration.POD_SUMMARY:
                    event_type = None
                    if task_request_identifier == TaskRequestType.OSOK_PROCESSOR:
                        pod_summary = kube_command_helper.get_operator_pod_details(OPERATOR_ANNOTATION)
                        event_type = EventType.OSOK
                    elif task_request_identifier == TaskRequestType.OLM_PROCESSOR:
                        pod_summary = kube_command_helper.get_pod_details_by_label_selector(OLM_LABEL)
                        event_type = EventType.OLM
                    elif task_request_identifier == TaskRequestType.METRICS_PROCESSOR:
                        pod_summary = kube_command_helper.get_pod_details_by_label_selector(METRICS_SERVER_LABEL)
                        event_type = EventType.METRICS_SERVER
                    elif task_request_identifier == TaskRequestType.CATALOG_PROCESSOR:
                        pod_summary = kube_command_helper.get_pod_details_by_label_selector(CATALOG_OPERATOR_LABEL)
                        event_type = EventType.CATALOG_OPERATOR
                    if pod_summary is not None:
                        event = Event(event_type=event_type,
                                      operations={OperationType.STORE_SINGLE_EVENT},
                                      data=pod_summary.__dict__,
                                      identifications={mesh_id: None},
                                      store={mesh_id})
                        output_events.append(event)

                        # Queue CsvTask if OSOK
                        if task_request_identifier == TaskRequestType.OSOK_PROCESSOR:
                            csv_task_request = CsvTaskRequest(TaskRequestType.CSV_PROCESSOR,
                                                              [],
                                                              pod_summary.namespace,
                                                              mesh_id)
                            tasks.append(csv_task_request)

                # Queue FileTask Event
                if task_configuration == TaskConfiguration.LOGS and pod_summary is not None:
                    file_name = None
                    if task_request_identifier == TaskRequestType.OSOK_PROCESSOR:
                        file_name = BundleHelper.get_osok_log_file_name()
                    elif task_request_identifier == TaskRequestType.OLM_PROCESSOR:
                        file_name = BundleHelper.get_olm_log_file_name()
                    elif task_request_identifier == TaskRequestType.CATALOG_PROCESSOR:
                        file_name = BundleHelper.get_catalog_operator_log_file_name()
                    if file_name is not None:
                        logs = kube_command_helper.get_pod_logs(pod_summary.name, pod_summary.namespace)
                        file_task_request = FileTaskRequest(TaskRequestType.FILE_PROCESSOR,
                                                            [],
                                                            relative_path,
                                                            file_name,
                                                            logs)
                        tasks.append(file_task_request)
            if pod_summary is not None:
                # Queue install plan
                install_plan = kube_command_helper.get_install_plan(pod_summary.namespace)
                file_task_request = FileTaskRequest(TaskRequestType.FILE_PROCESSOR,
                                                    [],
                                                    relative_path,
                                                    BundleHelper.get_install_plan_name(),
                                                    install_plan)
                tasks.append(file_task_request)

                # Queue subscription
                subscription = kube_command_helper.get_subscription(pod_summary.namespace)
                file_task_request = FileTaskRequest(TaskRequestType.FILE_PROCESSOR,
                                                    [],
                                                    relative_path,
                                                    BundleHelper.get_subscription_file_name(),
                                                    subscription)
                tasks.append(file_task_request)

                # Queue catalog_source
                catalog_source = kube_command_helper.get_catalog_source(pod_summary.namespace)

                file_task_request = FileTaskRequest(TaskRequestType.FILE_PROCESSOR,
                                                    [],
                                                    relative_path,
                                                    BundleHelper.get_catalog_source_file_name(),
                                                    catalog_source)

                tasks.append(file_task_request)

            return tasks, output_events
        except Exception as error:
            click.echo('GenericTask Exception: {}'.format(error))
