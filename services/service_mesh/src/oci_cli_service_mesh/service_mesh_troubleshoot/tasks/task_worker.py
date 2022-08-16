# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import queue
from abc import abstractmethod
from typing import List

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import Event
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.task_request import TaskRequestType, \
    TaskRequest
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.kubectl_command_helper import \
    KubeCommandHelper


class MeshTask(object):
    def __init__(self, task_request_type: TaskRequestType, k8s_context=None):
        self.task_request_type = task_request_type
        self.k8s_context = k8s_context

    @abstractmethod
    def do_work(self, task_request: TaskRequest, kube_command_helper: KubeCommandHelper) -> (
            List[TaskRequest], List[Event]):
        raise NotImplementedError('do_work() is not implemented')

    def execute(self, task_request: TaskRequest, output_events: queue.Queue, tasks: queue.Queue):
        if self.task_request_type != task_request.task_request_type:
            raise RuntimeError("Wrong request Type routed")
        kube_command_helper = KubeCommandHelper(self.k8s_context)
        next_tasks, events = self.do_work(task_request, kube_command_helper)
        for task in next_tasks:
            tasks.put(task)
        for event in events:
            output_events.put(event)
