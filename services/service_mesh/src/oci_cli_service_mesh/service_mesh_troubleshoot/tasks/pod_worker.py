# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.event import Event, EventType, \
    OperationType
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.task_request import TaskRequestType, \
    TaskConfiguration, TaskRequest, FileTaskRequest
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.task_worker import MeshTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.bundle_helper import \
    BundleHelper
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.summary import MeshData, PodSummary


class PodTask(MeshTask):
    def __init__(self, k8s_context=None):
        super(PodTask, self).__init__(TaskRequestType.POD_PROCESSOR)
        self.k8s_context = k8s_context

    def do_work(self, task_request: TaskRequest, kube_command_helper):
        output_events, tasks = [], []
        try:
            data = task_request.get_task_data()
            pod_summary = data['pod_summary']
            mesh_data = data['mesh_data']
            name = pod_summary.basic_pod_summary.name
            namespace = pod_summary.basic_pod_summary.namespace
            relative_path = None
            if mesh_data.vdb_key is not None:
                relative_path = mesh_data.get_virtual_deployment_binding_hierarchy()
            elif mesh_data.igd_key is not None:
                relative_path = mesh_data.get_ingress_gateway_deployment_hierarchy()

            # Run the relevant configurations
            for task_configuration in task_request.configurations:
                if task_configuration == TaskConfiguration.LOGS:
                    proxy_logs = kube_command_helper.get_proxy_logs(name, namespace)
                    proxy_log_file_name = BundleHelper.get_proxy_log_file_name(name, namespace)
                    if proxy_logs is not None:
                        logs_file_task_request = FileTaskRequest(TaskRequestType.FILE_PROCESSOR,
                                                                 [],
                                                                 relative_path,
                                                                 proxy_log_file_name,
                                                                 proxy_logs)
                        tasks.append(logs_file_task_request)

                if task_configuration == TaskConfiguration.CONFIG_DUMP:
                    config_dump = kube_command_helper.get_config_dump(name, namespace)
                    config_dump_file_name = BundleHelper.get_config_dump_file_name(name, namespace)
                    if config_dump is not None:
                        config_dump_file_task_request = FileTaskRequest(TaskRequestType.FILE_PROCESSOR,
                                                                        [],
                                                                        relative_path,
                                                                        config_dump_file_name,
                                                                        config_dump)

                        tasks.append(config_dump_file_task_request)
                        pod_summary.dynamic_config_version = self.get_dynamic_cluster_version_from_config(config_dump)

                # Proxy Stats
                if task_configuration == TaskConfiguration.PROXY_STATS:
                    proxy_stats = kube_command_helper.get_proxy_stats(name, namespace)
                    proxy_stats_file_name = BundleHelper.get_proxy_stats_file_name(name, namespace)
                    if proxy_stats is not None:
                        proxy_stats_file_task_request = FileTaskRequest(TaskRequestType.FILE_PROCESSOR,
                                                                        [],
                                                                        relative_path,
                                                                        proxy_stats_file_name,
                                                                        proxy_stats)
                        tasks.append(proxy_stats_file_task_request)

                    # Queue output events
                    output_events = output_events + self.generate_and_queue_output_events(pod_summary, mesh_data)

            return tasks, output_events
        except Exception as error:
            click.echo('PodTask Exception: {}'.format(error))

    def get_dynamic_cluster_version_from_config(self, config_dump):
        version_info = None
        if config_dump is None or config_dump["configs"] is None:
            return None

        for dump in config_dump["configs"]:
            if dump["@type"] == "type.googleapis.com/envoy.admin.v3.ClustersConfigDump":
                dynamic_active_clusters = dump["dynamic_active_clusters"]
                if len(dynamic_active_clusters) > 0:
                    version_info = dynamic_active_clusters[0]["version_info"]
                    break
        return version_info

    @staticmethod
    def generate_and_queue_output_events(pod_summary: PodSummary,
                                         mesh_data: MeshData):
        output_events = []
        if pod_summary is None or mesh_data is None:
            return

        store = {}
        if mesh_data.ig_id is not None:
            store = {mesh_data.mesh_id, mesh_data.ig_id}
        elif mesh_data.vd_id is not None:
            store = {mesh_data.mesh_id, mesh_data.vs_id, mesh_data.vd_id}
        event = Event(event_type=EventType.POD_SUMMARY,
                      operations={OperationType.STORE_MULTI_EVENT},
                      data=pod_summary.to_dict(mesh_data),
                      identifications=mesh_data.get_hierarchy_as_dict(),
                      store=store)
        output_events.append(event)
        return output_events
