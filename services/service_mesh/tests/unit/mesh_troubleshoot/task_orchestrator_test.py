# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import unittest
from unittest import mock
from unittest.mock import Mock

# Mock requests to control its behavior

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import TaskOrchestrator, BasicPodSummary, \
    MeshData, PodSummary
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.task_request import ResourceTaskRequest, \
    TaskRequestType, TaskConfiguration, CsvTaskRequest, CommonTaskRequest, FileTaskRequest, PodTaskRequest, VdbTaskRequest, \
    IgdTaskRequest, ServicesTaskRequest, WebhooksTaskRequest, ValidateCrdsTaskRequest, ObservabilityTaskRequest, \
    OciCliVersionTaskRequest, NamespacesTaskRequest, MeshReportTaskRequest

MESH_ID = 'ocid1.mesh.oc1.iad.valid'
VS_ID = 'ocid1.meshvirtualservice.oc1.iad.valid'
VD_ID = 'ocid1.meshvirtualdeployment.oc1.iad.valid'
vdb_key = 'book-info/ratings'


class TestTaskOrchestrator(unittest.TestCase):
    def test_do_(self):
        mesh_vdb_dict = {
            'ocid1.mesh.oc1.iad.valid': {
                'ocid1.meshvirtualservice.oc1.iad.valid': {
                    'ocid1.meshvirtualdeployment.oc1.iad.valid':
                        ['long-canary-test4/ratings-v1-binding']
                }
            }
        }

        vdb_pods_dict = {
            'long-canary-test4/ratings-v1-binding': [PodSummary(proxy_version='0.1.348',
                                                                proxy_status='Running',
                                                                pod_json={},
                                                                basic_pod_summary=BasicPodSummary(
                                                                    name='ratings-v1-7c556f669f',
                                                                    namespace='book-info',
                                                                    version='1.2.3',
                                                                    status='Pending'))]
        }
        mesh_igd_dict = {
            'ocid1.mesh.oc1.iad.valid': {
                'ocid1.meshingressgateway.oc1.iad.valid': ['book-info/book-info-ig-deployment']
            }
        }

        igd_pods_dict = {
            'book-info/book-info-ig-deployment': [PodSummary(proxy_version='0.1.348',
                                                             proxy_status='Running',
                                                             pod_json={},
                                                             basic_pod_summary=BasicPodSummary(
                                                                 name='bookinfo-ig-deployment-deployment-5c6d89b',
                                                                 namespace='book-info',
                                                                 version='1.2.3',
                                                                 status='Pending'))]
        }
        tests = [

            {
                "name": "Resource Task ",
                "task-request": ResourceTaskRequest(TaskRequestType.RESOURCE_PROCESSOR,
                                                    [TaskConfiguration.CHILD_RESOURCES],
                                                    "ocid1.mesh.oc1.iad.valid"),

            },
            {
                "name": "Resource Task ",
                "task-request": ResourceTaskRequest(TaskRequestType.RESOURCE_PROCESSOR,
                                                    [TaskConfiguration.CHILD_RESOURCES],
                                                    None),
            },

            {
                "name": "CSV Task ",
                "task-request": CsvTaskRequest(TaskRequestType.CSV_PROCESSOR,
                                               [TaskConfiguration.CHILD_RESOURCES],
                                               "oci-system",
                                               "ocid1.mesh.oc1.iad.valid"),

            },
            {
                "name": "CommonTask OLM",
                "task-request": CommonTaskRequest(TaskRequestType.COMMON_PROCESSOR,
                                                  [TaskConfiguration.CHILD_RESOURCES],
                                                  "ocid1.mesh.oc1.iad.valid",
                                                  TaskRequestType.OLM_PROCESSOR),

            },
            {
                "name": "File Task ",
                "task-request": FileTaskRequest(TaskRequestType.FILE_PROCESSOR,
                                                [TaskConfiguration.CHILD_RESOURCES],
                                                'mesh_ocid1.mesh.oc1.iad.valid',
                                                'file.log',
                                                'This is a file task request'),
            },
            {
                "name": "Pod Task",
                "task-request": PodTaskRequest(TaskRequestType.POD_PROCESSOR,
                                               [TaskConfiguration.CHILD_RESOURCES],
                                               pod_summary=PodSummary(BasicPodSummary(name='rating-v1-123',
                                                                                      namespace='book-info',
                                                                                      version='1.10',
                                                                                      status='Running'),
                                                                      pod_json='{}'),
                                               mesh_data=MeshData(mesh_id=MESH_ID,
                                                                  vs_id=VS_ID,
                                                                  vd_id=VD_ID,
                                                                  vdb_key=vdb_key)),
            },
            {
                "name": "Vdb Task",
                "task-request": VdbTaskRequest(TaskRequestType.VDB_PROCESSOR,
                                               [TaskConfiguration.CHILD_RESOURCES],
                                               mesh_vdb_dict,
                                               vdb_pods_dict),
            },
            {
                "name": "Igd Task",
                "task-request": IgdTaskRequest(TaskRequestType.IGD_PROCESSOR,
                                               [TaskConfiguration.CHILD_RESOURCES],
                                               mesh_igd_dict,
                                               igd_pods_dict),
            },
            {
                "name": "Common Task OSOK",
                "task-request": CommonTaskRequest(TaskRequestType.COMMON_PROCESSOR,
                                                  [TaskConfiguration.CHILD_RESOURCES],
                                                  "ocid1.mesh.oc1.iad.valid",
                                                  TaskRequestType.OSOK_PROCESSOR),
            },
            {
                "name": "Operator services task",
                "task-request": ServicesTaskRequest(TaskRequestType.SERVICES_PROCESSOR,
                                                    [TaskConfiguration.CHILD_RESOURCES],
                                                    "ocid1.mesh.oc1.iad.valid"),
            },
            {
                "name": "Webhooks Task",
                "task-request": WebhooksTaskRequest(TaskRequestType.WEBHOOKS_PROCESSOR,
                                                    [TaskConfiguration.CHILD_RESOURCES],
                                                    "ocid1.mesh.oc1.iad.valid"),
            },
            {
                "name": "Crds Task",
                "task-request": ValidateCrdsTaskRequest(TaskRequestType.VALIDATE_CRDS_PROCESSOR,
                                                        [TaskConfiguration.CHILD_RESOURCES],
                                                        "ocid1.mesh.oc1.iad.valid"),
            },
            {
                "name": "Observability Task",
                "task-request": ObservabilityTaskRequest(TaskRequestType.OBSERVABILITY_PROCESSOR,
                                                         [TaskConfiguration.CHILD_RESOURCES],
                                                         "ocid1.mesh.oc1.iad.valid"),
            },
            {
                "name": "Oci Cli version Task",
                "task-request": OciCliVersionTaskRequest(TaskRequestType.OCI_CLI_VERSION_PROCESSOR,
                                                         [TaskConfiguration.CHILD_RESOURCES],
                                                         "ocid1.mesh.oc1.iad.valid"),
            },
            {
                "name": "Namespaces Task",
                "task-request": NamespacesTaskRequest(TaskRequestType.NAMESPACES_PROCESSOR,
                                                      [TaskConfiguration.CHILD_RESOURCES],
                                                      "ocid1.mesh.oc1.iad.valid"),
            },
            {
                "name": "Mesh Report Task",
                "task-request": MeshReportTaskRequest(TaskRequestType.MESH_REPORT_PROCESSOR,
                                                      [TaskConfiguration.CHILD_RESOURCES],
                                                      "ocid1.mesh.oc1.iad.valid"),
            }
        ]
        for test_input in tests:
            task_orchestrator = TaskOrchestrator(
                "ocid1.mesh.oc1.iad.valid")
            task_orchestrator.process_tasks([test_input["task-request"]])


kube_command_helper = Mock()
task_request = Mock()

with mock.patch(
        'services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.aggregators.aggregation_orchestrator.AggregationOrchestrator.aggregate_events') as MockClass:  # replace f1 with MockClass
    MockClass.side_effect = None  # Change the return value

with mock.patch(
        'services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.resource_worker.ResourceTask.do_work') as MockClass:  # replace f1 with MockClass
    MockClass.side_effect = [], []  # Change the return value

with mock.patch(
        'services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.pod_worker.PodTask.do_work') as MockClass:  # replace f1 with MockClass
    MockClass.side_effect = [], []  # Change the return value

with mock.patch(
        'services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.common_worker.CommonTask.do_work') as MockClass:  # replace f1 with MockClass
    MockClass.side_effect = [], []  # Change the return value

with mock.patch(
        'services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.file_worker.FileTask.do_work') as MockClass:  # replace f1 with MockClass
    MockClass.side_effect = [], []  # Change the return value

with mock.patch(
        'services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.igd_worker.IgdTask.do_work') as MockClass:  # replace f1 with MockClass
    MockClass.side_effect = [], []  # Change the return value

with mock.patch(
        'services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.mesh_report_worker.MeshReportTask.do_work') as MockClass:  # replace f1 with MockClass
    MockClass.side_effect = [], []  # Change the return value

with mock.patch(
        'services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.mesh_resources_worker.MeshResourcesTask.do_work') as MockClass:  # replace f1 with MockClass
    MockClass.side_effect = [], []  # Change the return value

with mock.patch(
        'services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.namespaces_worker.NamespacesTask.do_work') as MockClass:  # replace f1 with MockClass
    MockClass.side_effect = [], []  # Change the return value

with mock.patch(
        'services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.oci_cli_version_worker.OciCliVersionTask.do_work') as MockClass:  # replace f1 with MockClass
    MockClass.side_effect = [], []  # Change the return value

with mock.patch(
        'services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.csv_worker.CsvTask.do_work') as MockClass:  # replace f1 with MockClass
    MockClass.side_effect = [], []  # Change the return value
