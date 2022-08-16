# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import os
import tempfile
import unittest
from unittest.mock import Mock

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import FileTask, FileTaskRequest, \
    TaskRequestType

MESH_ID = 'ocid1.mesh.oc1.iad.valid'


class TestFileWorker(unittest.TestCase):

    def test_data_in_output_event(self):

        tests = {
            'json_content_test': {
                'input': {
                    'file_name': 'pod_xyz-123.json',
                    'contents': '{\'name\': \'xyz-123\'}'
                }
            },
            'non_json_content_test': {
                'input': {
                    'file_name': 'proxy-logs_xyz-123.log',
                    'contents': 'This is a log.'
                }
            },
        }

        for test_name, test_payload in tests.items():
            # print('\nTest Name: {}'.format(test_name))
            test_input = test_payload['input']
            file_name = test_input['file_name']
            contents = test_input['contents']

            temp_dir = tempfile.gettempdir()
            kube_command_helper = Mock()
            file_task_request = FileTaskRequest(TaskRequestType.FILE_PROCESSOR,
                                                [],
                                                temp_dir,
                                                file_name,
                                                contents)
            file_task = FileTask()
            tasks, output_events = file_task.do_work(file_task_request,
                                                     kube_command_helper=kube_command_helper)

            # There should be 0 tasks, 0 output_events
            self.assertTrue(len(tasks) == 0)
            self.assertTrue(len(output_events) == 0)

            # Assert file creation and contents match
            complete_path = os.path.join(temp_dir, file_name)
            self.assertTrue(os.path.exists(complete_path))
            with open(complete_path) as f:
                actual_contents = f.read()
                # print('Actual: {}'.format(actual_contents))
                self.assertTrue(contents in actual_contents)

            # Cleanup
            os.remove(complete_path)
            self.assertFalse(os.path.exists(complete_path))
