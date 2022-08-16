# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
from enum import Enum
from typing import List

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.summary import PodSummary, MeshData


class TaskRequestType(Enum):
    OCI_CLI_VERSION_PROCESSOR = 'OCI_CLI_VERSION_PROCESSOR'
    POD_PROCESSOR = 'POD_PROCESSOR'
    RESOURCE_PROCESSOR = 'RESOURCE_PROCESSOR'
    VDB_PROCESSOR = 'VDB_PROCESSOR'
    IGD_PROCESSOR = 'IGD_PROCESSOR'
    OSOK_PROCESSOR = 'OSOK_PROCESSOR'
    OLM_PROCESSOR = 'OLM_PROCESSOR'
    METRICS_PROCESSOR = 'METRICS_PROCESSOR'
    NAMESPACES_PROCESSOR = 'NAMESPACES_PROCESSOR'
    SIDECAR_PROCESSOR = 'SIDECAR_PROCESSOR'
    FILE_PROCESSOR = 'FILE_PROCESSOR'
    CSV_PROCESSOR = 'CSV_PROCESSOR'
    VD_WITHOUT_VDB_PROCESSOR = 'VD_WITHOUT_VDB_PROCESSOR'
    MESH_REPORT_PROCESSOR = 'MESH_REPORT_PROCESSOR'
    MESH_RESOURCES_PROCESSOR = 'MESH_RESOURCES_PROCESSOR'
    COMMON_PROCESSOR = 'COMMON_PROCESSOR'
    CATALOG_PROCESSOR = 'CATALOG_OPERATOR_PROCESSOR'
    INSTALL_PLAN_PROCESSOR = 'INSTALL_PLAN_PROCESSOR'
    CATALOG_SOURCE_PROCESSOR = 'CATALOG_SOURCE_PROCESSOR'
    SUBSCRIPTION_PROCESSOR = 'SUBSCRIPTION_PROCESSOR'
    VALIDATE_CRDS_PROCESSOR = 'VALIDATE_CRDS_PROCESSOR'
    WEBHOOKS_PROCESSOR = 'WEBHOOKS_PROCESSOR'
    OBSERVABILITY_PROCESSOR = 'OBSERVABILITY_PROCESSOR'
    SERVICES_PROCESSOR = 'SERVICES_PROCESSOR'


class TaskConfiguration(Enum):
    LOGS = 'LOGS'
    CONFIG_DUMP = 'CONFIG_DUMP'
    PROXY_STATS = 'PROXY_STATS'
    STATUS = 'STATUS'
    POD_SUMMARY = 'POD_SUMMARY'
    ACCESS_LOGGING_DISABLED = 'ACCESS_LOGGING_DISABLED'
    PROXY_LOGGING_DISABLED = 'PROXY_LOGGING_DISABLED'
    POD_UPGRADE_DISABLED = 'POD_UPGRADE_DISABLED'
    UNHEALTHY_PROXY = 'UNHEALTHY_PROXY'
    POD_HIERARCHY = 'POD_HIERARCHY'
    CHILD_RESOURCES = 'CHILD_RESOURCES'


class TaskRequest(object):
    def __init__(self, task_request_type: TaskRequestType, configurations: List[TaskConfiguration]):
        self.task_request_type = task_request_type
        self.configurations = configurations

    def get_task_data(self):
        raise NotImplementedError('This should be Implemented')


class PodTaskRequest(TaskRequest):
    def __init__(self,
                 task_request_type: TaskRequestType,
                 configurations: List[TaskConfiguration],
                 pod_summary: PodSummary,
                 mesh_data: MeshData):
        super(PodTaskRequest, self).__init__(task_request_type, configurations)
        self.pod_summary = pod_summary
        self.mesh_data = mesh_data

    def get_task_data(self):
        return {'pod_summary': self.pod_summary, 'mesh_data': self.mesh_data}


class ResourceTaskRequest(TaskRequest):
    def __init__(self, task_request_type: TaskRequestType, configurations: List[TaskConfiguration], resource_id: str):
        super(ResourceTaskRequest, self).__init__(task_request_type, configurations)
        self.resource_id = resource_id

    def get_task_data(self):
        return {'resource_id': self.resource_id}


class MeshReportTaskRequest(TaskRequest):
    def __init__(self,
                 task_request_type: TaskRequestType,
                 configurations: List[TaskConfiguration],
                 mesh_id: str):
        super(MeshReportTaskRequest, self).__init__(task_request_type, configurations)
        self.mesh_id = mesh_id

    def get_task_data(self):
        return {'mesh_id': self.mesh_id}


class VdbTaskRequest(TaskRequest):
    def __init__(self,
                 task_request_type: TaskRequestType,
                 configurations: List[TaskConfiguration],
                 mesh_dict: dict,
                 vdb_pods_dict: dict):
        super(VdbTaskRequest, self).__init__(task_request_type, configurations)
        self.mesh_dict = mesh_dict
        self.vdb_pods_dict = vdb_pods_dict

    def get_task_data(self):
        return {'mesh_dict': self.mesh_dict, 'vdb_pods_dict': self.vdb_pods_dict}


class IgdTaskRequest(TaskRequest):
    def __init__(self,
                 task_request_type: TaskRequestType,
                 configurations: List[TaskConfiguration],
                 mesh_dict: dict,
                 igd_pods_dict: dict):
        super(IgdTaskRequest, self).__init__(task_request_type, configurations)
        self.mesh_dict = mesh_dict
        self.igd_pods_dict = igd_pods_dict

    def get_task_data(self):
        return {'mesh_dict': self.mesh_dict, 'igd_pods_dict': self.igd_pods_dict}


class NamespacesTaskRequest(TaskRequest):
    def __init__(self,
                 task_request_type: TaskRequestType,
                 configurations: List[TaskConfiguration],
                 mesh_id: str):
        super(NamespacesTaskRequest, self).__init__(task_request_type, configurations)
        self.mesh_id = mesh_id

    def get_task_data(self):
        return {'mesh_id': self.mesh_id}


class OciCliVersionTaskRequest(TaskRequest):
    def __init__(self,
                 task_request_type: TaskRequestType,
                 configurations: List[TaskConfiguration],
                 mesh_id: str):
        super(OciCliVersionTaskRequest, self).__init__(task_request_type, configurations)
        self.mesh_id = mesh_id

    def get_task_data(self):
        return {'mesh_id': self.mesh_id}


class ObservabilityTaskRequest(TaskRequest):
    def __init__(self,
                 task_request_type: TaskRequestType,
                 configurations: List[TaskConfiguration],
                 mesh_id: str):
        super(ObservabilityTaskRequest, self).__init__(task_request_type, configurations)
        self.mesh_id = mesh_id

    def get_task_data(self):
        return {'mesh_id': self.mesh_id}


class ValidateCrdsTaskRequest(TaskRequest):
    def __init__(self, task_request_type: TaskRequestType,
                 configurations: List[TaskConfiguration],
                 mesh_id: str):
        super(ValidateCrdsTaskRequest, self).__init__(task_request_type, configurations)
        self.mesh_id = mesh_id

    def get_task_data(self):
        return {'mesh_id': self.mesh_id}


class WebhooksTaskRequest(TaskRequest):
    def __init__(self, task_request_type: TaskRequestType,
                 configurations: List[TaskConfiguration],
                 mesh_id: str):
        super(WebhooksTaskRequest, self).__init__(task_request_type, configurations)
        self.mesh_id = mesh_id

    def get_task_data(self):
        return {'mesh_id': self.mesh_id}


class ServicesTaskRequest(TaskRequest):
    def __init__(self, task_request_type: TaskRequestType,
                 configurations: List[TaskConfiguration],
                 mesh_id: str):
        super(ServicesTaskRequest, self).__init__(task_request_type, configurations)
        self.mesh_id = mesh_id

    def get_task_data(self):
        return {'mesh_id': self.mesh_id}


class FileTaskRequest(TaskRequest):
    def __init__(self,
                 task_request_type: TaskRequestType,
                 configurations: List[TaskConfiguration],
                 relative_path: str,
                 file_name: str,
                 contents: str):
        super(FileTaskRequest, self).__init__(task_request_type, configurations)
        self.relative_path = relative_path
        self.file_name = file_name
        self.contents = contents

    def get_task_data(self):
        return {'relative_path': self.relative_path, 'file_name': self.file_name, 'contents': self.contents}


class CsvTaskRequest(TaskRequest):
    def __init__(self,
                 task_request_type: TaskRequestType,
                 configurations: List[TaskConfiguration],
                 operator_namespace: str,
                 mesh_id: str):
        super(CsvTaskRequest, self).__init__(task_request_type, configurations)
        self.operator_namespace = operator_namespace
        self.mesh_id = mesh_id

    def get_task_data(self):
        return {'operator_namespace': self.operator_namespace, 'mesh_id': self.mesh_id}


class MeshResourcesTaskRequest(TaskRequest):
    def __init__(self,
                 task_request_type: TaskRequestType,
                 configurations: List[TaskConfiguration],
                 mesh_id: str):
        super(MeshResourcesTaskRequest, self).__init__(task_request_type, configurations)
        self.mesh_id = mesh_id

    def get_task_data(self):
        return {'mesh_id': self.mesh_id}


class CommonTaskRequest(TaskRequest):
    def __init__(self,
                 task_request_type: TaskRequestType,
                 configurations: List[TaskConfiguration],
                 mesh_id: str,
                 task_request_identifier: TaskRequestType):
        super(CommonTaskRequest, self).__init__(task_request_type, configurations)
        self.mesh_id = mesh_id
        self.task_request_identifier = task_request_identifier

    def get_task_data(self):
        return {'mesh_id': self.mesh_id, 'task_request_identifier': self.task_request_identifier}
