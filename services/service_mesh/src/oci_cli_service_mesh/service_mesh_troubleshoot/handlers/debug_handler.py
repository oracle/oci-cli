# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
from abc import abstractmethod, ABC
from enum import Enum
from typing import Dict

import click
import sys

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import TaskOrchestrator, \
    ResourceTaskRequest, TaskRequestType, TaskConfiguration
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.bundle_helper import BundleHelper
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.constants import \
    MESH_CUSTOM_RESOURCE_DICT
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.helper import MeshTaskException
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.messages import Messages


class DebugHandlerRequestType(Enum):
    K8S_CHECK = 'K8S_CHECK'
    K8S_CHECK_CONTEXT = 'K8S_CHECK_CONTEXT'
    OCID_VALIDATION = 'OCID_VALIDATION'
    BUNDLE_NAME = 'BUNDLE_NAME'
    BUNDLE_COMPRESS = 'BUNDLE_COMPRESS'
    BUNDLE_CLEANUP = 'BUNDLE_CLEANUP'
    TASK = 'TASK'


class ResultIdentifier(Enum):
    BUNDLE_NAME = 'bundle_name'
    CURRENT_CONTEXT = 'current_context'
    K8S_CONTEXT = 'k8s_context'


class ResultStatus(Enum):
    OK = '200'
    NOT_FOUND = '404'
    INTERNAL_ERROR = '500'


class Result:
    def __init__(self, status: ResultStatus, data: Dict = None, exception: str = None):
        self.status = status
        self.data = data
        self.exception = exception


class DebugHandler(ABC):
    @abstractmethod
    def set_next(self, debug_handler):
        pass

    @abstractmethod
    def handle(self, request: Dict) -> Result:
        pass


class AbstractDebugHandler(DebugHandler):
    _next_handler: DebugHandler = None

    def set_next(self, debug_handler: DebugHandler) -> DebugHandler:
        self._next_handler = debug_handler
        return debug_handler

    @abstractmethod
    def handle(self, request: Dict) -> Result:
        if self._next_handler:
            return self._next_handler.handle(request)
        return Result(status=ResultStatus.INTERNAL_ERROR, data={})


class OcidValidationHandler(AbstractDebugHandler):
    def handle(self, request: Dict) -> Result:
        request_type = request['type']
        if request_type == DebugHandlerRequestType.OCID_VALIDATION:
            ocid = request['data']['ocid']
            if ocid is None:
                click.echo(Messages.is_none.format('ocid'), file=sys.stderr)
                return Result(status=ResultStatus.NOT_FOUND, exception=Messages.is_none.format('ocid'))

            # Split the token to get the resource type
            ocid_tokens = ocid.split(".")

            # Validate ocid format
            if len(ocid_tokens) < 2:
                # raise click.BadParameter(Messages.invalid_ocid)
                exception = Messages.invalid_ocid
                click.echo(exception, file=sys.stderr)
                return Result(status=ResultStatus.INTERNAL_ERROR, exception=exception)

            # Validate mesh resource type
            resource_type = ocid_tokens[1]
            try:
                MESH_CUSTOM_RESOURCE_DICT[resource_type]
            except Exception as error:
                exception = Messages.invalid_mesh_resource_type.format(resource_type) + '. ' + str(error)
                click.echo(exception, file=sys.stderr)
                return Result(status=ResultStatus.INTERNAL_ERROR, exception=exception)

            # Is a valid ocid
            return Result(status=ResultStatus.OK, data={})
        else:
            return super(OcidValidationHandler, self).handle(request)


class K8sCheckHandler(AbstractDebugHandler):
    def handle(self, request: Dict) -> Result:
        request_type = request['type']
        if request_type == DebugHandlerRequestType.K8S_CHECK:
            kube_command_helper = request['kube_command_helper']
            kube_command_summary = kube_command_helper.is_kubectl_installed()
            if kube_command_summary.return_code == 0:
                return Result(status=ResultStatus.OK, data={})
            else:
                return Result(status=ResultStatus.NOT_FOUND, exception=kube_command_summary.stderr)
        else:
            return super(K8sCheckHandler, self).handle(request)


class K8sCheckContextHandler(AbstractDebugHandler):
    def handle(self, request: Dict) -> Result:
        request_type = request['type']
        if request_type == DebugHandlerRequestType.K8S_CHECK_CONTEXT:
            kube_command_helper = request['kube_command_helper']
            k8s_context = request['data'][ResultIdentifier.K8S_CONTEXT.value]
            k8s_config, use_context = k8s_context
            kube_command_summary = kube_command_helper.check_context(k8s_context)
            if kube_command_summary.return_code != 0:
                return Result(status=ResultStatus.INTERNAL_ERROR, exception=kube_command_summary.stderr)
            else:
                return Result(status=ResultStatus.OK)
        else:
            return super(K8sCheckContextHandler, self).handle(request)


class BundleNameHandler(AbstractDebugHandler):
    def handle(self, request: Dict) -> Result:
        request_type = request['type']
        if request_type == DebugHandlerRequestType.BUNDLE_NAME:
            bundle_name = BundleHelper.get_bundle_name()
            return Result(status=ResultStatus.OK, data={ResultIdentifier.BUNDLE_NAME: bundle_name})
        else:
            return super(BundleNameHandler, self).handle(request)


class BundleCompressHandler(AbstractDebugHandler):
    def handle(self, request: Dict) -> Result:
        request_type = request['type']
        if request_type == DebugHandlerRequestType.BUNDLE_COMPRESS:
            try:
                directory_name = request['data']['directory_name']
                bundle_name = request['data']['bundle_name']
                BundleHelper.compress_bundle(directory_name, bundle_name)
                if BundleHelper.compress_bundle(directory_name, bundle_name) is False:
                    raise MeshTaskException()
                else:
                    return Result(status=ResultStatus.OK)
            except MeshTaskException:
                return Result(status=ResultStatus.INTERNAL_ERROR, exception='***Generating Bundle failed. Directory path not found***')
            except Exception as error:
                exception = Messages.some_exception.format(request_type, error)
                click.echo(exception, file=sys.stderr)
                return Result(status=ResultStatus.INTERNAL_ERROR, exception=exception)
        else:
            return super(BundleCompressHandler, self).handle(request)


class BundleCleanupHandler(AbstractDebugHandler):
    def handle(self, request: Dict) -> Result:
        request_type = request['type']
        if request_type == DebugHandlerRequestType.BUNDLE_CLEANUP:
            try:
                directory_name = request['data']['directory_name']
                bundle_name = request['data']['bundle_name']
                BundleHelper.cleanup(directory_name, bundle_name)
                return Result(status=ResultStatus.OK)
            except Exception as error:
                exception = Messages.some_exception.format(request_type, error)
                click.echo(exception, file=sys.stderr)
                return Result(status=ResultStatus.INTERNAL_ERROR, exception=exception)
        else:
            return super(BundleCleanupHandler, self).handle(request)


class TaskHandler(AbstractDebugHandler):
    def __init__(self, thread_pool_size=None):
        self.thread_pool_size = thread_pool_size

    def handle(self, request: Dict) -> Result:
        request_type = request['type']
        if request_type == DebugHandlerRequestType.TASK:
            ocid = request['data']['ocid']
            k8s_context = request['data']['k8s_context']
            # if ocid is None:
            #     return Result(status=ResultStatus.NOT_FOUND, data={})
            try:
                task_orchestrator = TaskOrchestrator(ocid, k8s_context, self.thread_pool_size)
                resource_task = ResourceTaskRequest(TaskRequestType.RESOURCE_PROCESSOR,
                                                    [TaskConfiguration.CHILD_RESOURCES],
                                                    ocid)
                task_orchestrator.process_tasks([resource_task])
                return Result(status=ResultStatus.OK, data={})
            except Exception as error:
                exception = Messages.some_exception.format(request_type, error)
                click.echo(exception, file=sys.stderr)
                return Result(status=ResultStatus.INTERNAL_ERROR, exception=exception)
        else:
            return super(TaskHandler, self).handle(request)
