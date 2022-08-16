# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import unittest
from unittest.mock import Mock
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import TaskRequestType, \
    ValidateCrdsTask, ValidateCrdsTaskRequest, OperationType, EventType

MESH_ID = 'ocid1.mesh.oc1.iad.valid'


class TestValidateCrdsWorker(unittest.TestCase):

    def test_data_in_output_event(self):
        kube_command_helper = Mock()
        expected_crds_list = ['accesspolicies.servicemesh.oci.oracle.com',
                              'ingressgatewaydeployments.servicemesh.oci.oracle.com',
                              'ingressgatewayroutetables.servicemesh.oci.oracle.com',
                              'ingressgateways.servicemesh.oci.oracle.com',
                              'meshes.servicemesh.oci.oracle.com',
                              'virtualdeploymentbindings.servicemesh.oci.oracle.com',
                              'virtualdeployments.servicemesh.oci.oracle.com',
                              'virtualserviceroutetables.servicemesh.oci.oracle.com',
                              'virtualservices.servicemesh.oci.oracle.com']
        kube_command_helper.get_crds_validated.return_value = expected_crds_list

        validate_crds_task_request = ValidateCrdsTaskRequest(TaskRequestType.VALIDATE_CRDS_PROCESSOR, [], MESH_ID)
        validate_crds_task = ValidateCrdsTask()

        tasks, output_events = validate_crds_task.do_work(validate_crds_task_request,
                                                          kube_command_helper=kube_command_helper)
        # There should be 0 tasks, 1 output_event
        self.assertTrue(len(tasks) == 0)
        self.assertTrue(len(output_events) == 1)

        # Assert the event content
        output_event = output_events[0]
        self.assertTrue(output_event.event_type == EventType.SERVICE_MESH_CRDS)
        self.assertTrue(OperationType.STORE_SINGLE_EVENT in output_event.operations)
        self.assertTrue(MESH_ID in output_event.store)
        self.assertIsNotNone(output_event.data)
        actual_crds_list = output_event.data
        self.assertTrue(len(actual_crds_list) == len(expected_crds_list))
        expected_crds_list.sort()
        actual_crds_list.sort()
        self.assertTrue(actual_crds_list == expected_crds_list)
