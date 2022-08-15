# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import unittest
from unittest.mock import Mock

# Mock requests to control its behavior
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import PodSummary
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.task_request import ResourceTaskRequest, \
    TaskRequestType, TaskConfiguration
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.tasks.resource_worker import \
    ResourceTask


class TestResourceWorker(unittest.TestCase):

    def test_do_work(self):
        tests = [
            (
                {
                    "name": "IG should not create VD Task ",
                    "task-request": ResourceTaskRequest(TaskRequestType.RESOURCE_PROCESSOR,
                                                        [TaskConfiguration.CHILD_RESOURCES],
                                                        "ocid1.meshingressgateway.oc1.iad.amaaaaaazueyztqabwwty745bied7gczx3qhz5oizpkqrpt36wgsw2pp4qrq"),
                    "filter_vdbs_by_ocid": {
                        'ocid1.mesh.oc1.iad.valid': {
                            'ocid1.meshingressgateway.oc1.iad.valid': [
                                'long-canary-test/bookinfo-ig-deployment']}},
                    "filter_all_pods_related_to_vdbs": {"pet-rescue/ui-binding": PodSummary()},
                    "filter_igds_by_ocid": {
                        'ocid1.mesh.oc1.iad.valid': {
                            'ocid1.meshingressgateway.oc1.iad.valid': [
                                'long-canary-test2/bookinfo-ig-deployment']}},
                    "filter_all_pods_related_to_igds": {}
                },
                {
                    "output_events_len": 0,
                    "next_tasks": {TaskRequestType.VDB_PROCESSOR: 0, TaskRequestType.IGD_PROCESSOR: 1,
                                   TaskRequestType.MESH_REPORT_PROCESSOR: 1, TaskRequestType.MESH_RESOURCES_PROCESSOR: 1},
                }
            ),
            (
                {
                    "name": "VS should not create  IGD Task ",
                    "task-request": ResourceTaskRequest(TaskRequestType.RESOURCE_PROCESSOR,
                                                        [TaskConfiguration.CHILD_RESOURCES],
                                                        "ocid1.meshvirtualservice.oc1.iad.valid"),
                    "filter_vdbs_by_ocid": {
                        'ocid1.mesh.oc1.iad.valid': {
                            'ocid1.meshingressgateway.oc1.iad.valid': [
                                'long-canary-test/bookinfo-ig-deployment']}},
                    "filter_all_pods_related_to_vdbs": {"pet-rescue/ui-binding": PodSummary()},
                    "filter_igds_by_ocid": {
                        'ocid1.mesh.oc1.iad.valid': {
                            'ocid1.meshingressgateway.oc1.iad.valid': [
                                'long-canary-test2/bookinfo-ig-deployment']}},
                    "filter_all_pods_related_to_igds": {}
                },
                {
                    "output_events_len": 0,
                    "next_tasks": {TaskRequestType.VDB_PROCESSOR: 1, TaskRequestType.IGD_PROCESSOR: 0,
                                   TaskRequestType.MESH_REPORT_PROCESSOR: 1, TaskRequestType.MESH_RESOURCES_PROCESSOR: 1},
                }
            ),
            (
                {
                    "name": "VD should not create  IGD Task ",
                    "task-request": ResourceTaskRequest(TaskRequestType.RESOURCE_PROCESSOR,
                                                        [TaskConfiguration.CHILD_RESOURCES],
                                                        "ocid1.meshvirtualdeployment.oc1.iad.amaaaaaazueyztqabwwty745bied7gczx3qhz5oizpkqrpt36wgsw2pp4qrq"),
                    "filter_vdbs_by_ocid": {
                        'ocid1.mesh.oc1.iad.valid': {
                            'ocid1.meshingressgateway.oc1.iad.valid': [
                                'long-canary-test/bookinfo-ig-deployment']}},
                    "filter_all_pods_related_to_vdbs": {"pet-rescue/ui-binding": PodSummary()},
                    "filter_igds_by_ocid": {
                        'ocid1.mesh.oc1.iad.valid': {
                            'ocid1.meshingressgateway.oc1.iad.valid': [
                                'long-canary-test2/bookinfo-ig-deployment']}},
                    "filter_all_pods_related_to_igds": {}
                },
                {
                    "output_events_len": 0,
                    "next_tasks": {TaskRequestType.VDB_PROCESSOR: 1, TaskRequestType.IGD_PROCESSOR: 0,
                                   TaskRequestType.MESH_REPORT_PROCESSOR: 1, TaskRequestType.MESH_RESOURCES_PROCESSOR: 1},
                }
            ),
            (
                {
                    "name": "Only VDB test",
                    "task-request": ResourceTaskRequest(TaskRequestType.RESOURCE_PROCESSOR,
                                                        [TaskConfiguration.CHILD_RESOURCES],
                                                        "ocid1.mesh.oc1.iad.valid"),
                    "filter_vdbs_by_ocid": {
                        'ocid1.mesh.oc1.iad.valid': {
                            'ocid1.meshingressgateway.oc1.iad.valid': [
                                'long-canary-test/bookinfo-ig-deployment']}},
                    "filter_all_pods_related_to_vdbs": {"pet-rescue/ui-binding": PodSummary()},
                    "filter_igds_by_ocid": {},
                    "filter_all_pods_related_to_igds": {}
                },
                {
                    "output_events_len": 0,
                    "next_tasks": {TaskRequestType.VDB_PROCESSOR: 1, TaskRequestType.IGD_PROCESSOR: 0,
                                   TaskRequestType.MESH_REPORT_PROCESSOR: 1, TaskRequestType.MESH_RESOURCES_PROCESSOR: 1},
                }
            ),
            (
                {
                    "name": "VDB and IGD test ",
                    "task-request": ResourceTaskRequest(TaskRequestType.RESOURCE_PROCESSOR,
                                                        [TaskConfiguration.CHILD_RESOURCES],
                                                        "ocid1.mesh.oc1.iad.valid"),
                    "filter_vdbs_by_ocid": {
                        'ocid1.mesh.oc1.iad.valid': {
                            'ocid1.meshingressgateway.oc1.iad.valid': [
                                'long-canary-test/bookinfo-ig-deployment']}},
                    "filter_all_pods_related_to_vdbs": {"pet-rescue/ui-binding": PodSummary()},
                    "filter_igds_by_ocid": {
                        'ocid1.mesh.oc1.iad.valid': {
                            'ocid1.meshingressgateway.oc1.iad.valid': [
                                'long-canary-test2/bookinfo-ig-deployment']}},
                    "filter_all_pods_related_to_igds": {}
                },
                {
                    "output_events_len": 0,
                    "next_tasks": {TaskRequestType.VDB_PROCESSOR: 1, TaskRequestType.IGD_PROCESSOR: 1,
                                   TaskRequestType.MESH_REPORT_PROCESSOR: 1, TaskRequestType.MESH_RESOURCES_PROCESSOR: 1},
                }
            ),

        ]

        for test_input, test_output in tests:
            kube_command_helper = Mock()
            kube_command_helper.filter_vdbs_by_ocid.return_value = test_input["filter_vdbs_by_ocid"]
            kube_command_helper.filter_all_pods_related_to_vdbs.return_value = test_input[
                "filter_all_pods_related_to_vdbs"]
            kube_command_helper.filter_igds_by_ocid.return_value = test_input["filter_igds_by_ocid"]
            kube_command_helper.filter_all_pods_related_to_igds.return_value = test_input[
                "filter_all_pods_related_to_igds"]

            resource_task = ResourceTask()
            tasks, output_events = resource_task.do_work(test_input["task-request"], kube_command_helper=kube_command_helper)
            next_tasks = test_output["next_tasks"]

            # type TaskRequest
            for task in tasks:
                type_count = next_tasks[task.task_request_type]
                assert type_count >= 1
                next_tasks[task.task_request_type] -= 1
            for next_task_type, count in next_tasks.items():
                assert count == 0


if __name__ == '__main__':
    unittest.main()
