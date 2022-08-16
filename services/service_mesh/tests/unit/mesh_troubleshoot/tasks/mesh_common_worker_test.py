# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import unittest
from unittest.mock import Mock

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import CommonTaskRequest, TaskRequestType, \
    CommonTask, TaskConfiguration, BasicPodSummary, OperationType, EventType

MESH_ID = 'ocid1.mesh.oc1.iad.valid'


class TestCommonWorker(unittest.TestCase):

    def test_common_worker(self):
        tests = {
            'osok_test': {
                'input': {
                    'task_request_identifier': TaskRequestType.OSOK_PROCESSOR
                },
                'expected_output': {
                    'basic_pod_summary': BasicPodSummary(name='oci-service-operator-controller-manager-123',
                                                         namespace='oci-service-operator-system',
                                                         version='1.10',
                                                         status='Running'),
                    'event_type': EventType.OSOK
                }
            },
            'olm_test': {
                'input': {
                    'task_request_identifier': TaskRequestType.OLM_PROCESSOR
                },
                'expected_output': {
                    'basic_pod_summary': BasicPodSummary(name='olm-123',
                                                         namespace='olm',
                                                         version='1.10',
                                                         status='Running'),
                    'event_type': EventType.OLM
                }
            },
            'metrics_server_tests': {
                'input': {
                    'task_request_identifier': TaskRequestType.METRICS_PROCESSOR
                },
                'expected_output': {
                    'basic_pod_summary': BasicPodSummary(name='metrics-server-123',
                                                         namespace='metrics-server',
                                                         version='1.10',
                                                         status='Running'),
                    'event_type': EventType.METRICS_SERVER
                }
            }
        }

        for test_name, test_payload in tests.items():
            # print('\nTest Name: {}'.format(test_name))
            test_input = test_payload['input']
            task_request_identifier = test_input['task_request_identifier']
            test_expected_output = test_payload['expected_output']

            expected_pod_summary = test_expected_output['basic_pod_summary']
            expected_event_type = test_expected_output['event_type']

            kube_command_helper = Mock()
            if test_name == 'osok_test':
                kube_command_helper.get_operator_pod_details.return_value = expected_pod_summary
            else:
                kube_command_helper.get_pod_details_by_label_selector.return_value = expected_pod_summary

            common_task_request = CommonTaskRequest(TaskRequestType.COMMON_PROCESSOR,
                                                    [TaskConfiguration.POD_SUMMARY],
                                                    MESH_ID,
                                                    task_request_identifier)
            common_task = CommonTask()
            tasks, output_events = common_task.do_work(common_task_request,
                                                       kube_command_helper=kube_command_helper)

            # There should be 0 tasks, 1 output_event
            if task_request_identifier == TaskRequestType.OSOK_PROCESSOR:
                self.assertTrue(len(tasks) == 4)
            else:
                self.assertTrue(len(tasks) == 3)
            self.assertTrue(len(output_events) == 1)

            # Assert the event content
            output_event = output_events[0]
            self.assertTrue(output_event.event_type == expected_event_type)
            self.assertTrue(OperationType.STORE_SINGLE_EVENT in output_event.operations)
            self.assertTrue(MESH_ID in output_event.store)
            self.assertIsNotNone(output_event.data)
            actual_pod_summary = output_event.data
            self.assertTrue(actual_pod_summary['name'] == expected_pod_summary.name)
            self.assertTrue(actual_pod_summary['namespace'] == expected_pod_summary.namespace)
            self.assertTrue(actual_pod_summary['version'] == expected_pod_summary.version)
            self.assertTrue(actual_pod_summary['status'] == expected_pod_summary.status)
