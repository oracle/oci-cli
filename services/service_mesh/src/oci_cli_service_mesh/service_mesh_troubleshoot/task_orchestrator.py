# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import concurrent.futures
import multiprocessing
from typing import List

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.aggregators.aggregation_orchestrator \
    import AggregationOrchestrator
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.task_request import TaskRequest, \
    TaskRequestType
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.common_worker import CommonTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.csv_worker import CsvTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.file_worker import FileTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.mesh_report_worker import \
    MeshReportTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.mesh_resources_worker import \
    MeshResourcesTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.namespaces_worker import \
    NamespacesTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.oci_cli_version_worker import \
    OciCliVersionTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.vdb_worker import \
    VdbTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.igd_worker import IgdTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.pod_worker import PodTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.resource_worker import \
    ResourceTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.validate_crds_worker import ValidateCrdsTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.webhooks_worker import WebhooksTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.observability_worker import ObservabilityTask
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.services_worker import CheckServicesTask


class TaskOrchestrator():
    def __init__(self, ocid, k8s_context=None, thread_pool_size=None):
        self.ocid = ocid
        # Default thread pool size is 25
        self.thread_pool_size = 25 if thread_pool_size is None else thread_pool_size
        self.k8s_context = k8s_context
        self.task_processor_dict = {
            TaskRequestType.POD_PROCESSOR: PodTask(self.k8s_context),
            TaskRequestType.RESOURCE_PROCESSOR: ResourceTask(self.k8s_context),
            TaskRequestType.VDB_PROCESSOR: VdbTask(self.k8s_context),
            TaskRequestType.IGD_PROCESSOR: IgdTask(self.k8s_context),
            TaskRequestType.COMMON_PROCESSOR: CommonTask(self.k8s_context),
            TaskRequestType.NAMESPACES_PROCESSOR: NamespacesTask(self.k8s_context),
            TaskRequestType.OCI_CLI_VERSION_PROCESSOR: OciCliVersionTask(self.k8s_context),
            TaskRequestType.VALIDATE_CRDS_PROCESSOR: ValidateCrdsTask(self.k8s_context),
            TaskRequestType.WEBHOOKS_PROCESSOR: WebhooksTask(self.k8s_context),
            TaskRequestType.SERVICES_PROCESSOR: CheckServicesTask(self.k8s_context),
            TaskRequestType.FILE_PROCESSOR: FileTask(self.k8s_context),
            TaskRequestType.CSV_PROCESSOR: CsvTask(self.k8s_context),
            TaskRequestType.MESH_REPORT_PROCESSOR: MeshReportTask(self.k8s_context),
            TaskRequestType.MESH_RESOURCES_PROCESSOR: MeshResourcesTask(self.k8s_context),
            TaskRequestType.OBSERVABILITY_PROCESSOR: ObservabilityTask(self.k8s_context)
        }

    def process_task(self, task):
        task_worker = self.task_processor_dict[task.task_request_type]
        return task_worker.execute(task, self.output_events, self.tasks_sm)

    def process_tasks(self, tasks: List[TaskRequest]):
        futures_list, done, not_done = [], [], []
        m = multiprocessing.Manager()
        self.tasks_sm, self.output_events = m.Queue(), m.Queue()
        self.tasks_sm.put(tasks.pop())
        while not self.tasks_sm.empty() or len(not_done) > 0:
            done, not_done = concurrent.futures.wait(futures_list)
            task_list = []
            while not self.tasks_sm.empty():
                task_list.append(self.tasks_sm.get())
            executor = concurrent.futures.ThreadPoolExecutor(self.thread_pool_size)
            futures = [executor.submit(self.process_task, item) for item in task_list]
            concurrent.futures.wait(futures)

        aggregation_orchestrator = AggregationOrchestrator(self.ocid)
        aggregation_orchestrator.aggregate_events(self.output_events)
