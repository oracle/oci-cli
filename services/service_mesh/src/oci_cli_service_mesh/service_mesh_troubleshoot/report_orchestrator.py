# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import sys

import click

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot import KubeCommandHelper
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.handlers.debug_handler import \
    OcidValidationHandler, TaskHandler, DebugHandler, DebugHandlerRequestType, K8sCheckContextHandler, \
    BundleNameHandler, \
    BundleCompressHandler, BundleCleanupHandler, K8sCheckHandler, ResultStatus
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.bundle_helper import BundleHelper


class ReportOrchestrator:
    def __init__(self, ocid=None, k8s_config=None, use_context=None, thread_pool_size=None):
        self.ocid = ocid
        self.k8s_context = (k8s_config, use_context)
        self.thread_pool_size = thread_pool_size

    def build_report(self):
        k8s_check_handler = K8sCheckHandler()
        k8s_check_context_handler = K8sCheckContextHandler()
        validation_handler = OcidValidationHandler()
        bundle_name_handler = BundleNameHandler()
        task_handler = TaskHandler(self.thread_pool_size)
        bundle_compress_handler = BundleCompressHandler()
        bundle_cleanup_handler = BundleCleanupHandler()

        k8s_check_handler.set_next(k8s_check_context_handler).\
            set_next(validation_handler).\
            set_next(bundle_name_handler).\
            set_next(task_handler).\
            set_next(bundle_compress_handler).\
            set_next(bundle_cleanup_handler)

        client_handler = ClientHandler(k8s_check_handler, self.ocid, self.k8s_context)
        return client_handler.handle()


class ClientHandler:
    def __init__(self, debug_handler: DebugHandler, ocid, k8s_context):
        self.debug_handler = debug_handler
        self.ocid = ocid
        self.k8s_context = k8s_context

    def handle(self):
        mesh_bundle_name = BundleHelper.get_bundle_name()
        click.echo('Generating Mesh Bundle: {}'.format(mesh_bundle_name), file=sys.stdout)
        kube_command_helper = KubeCommandHelper(self.k8s_context)
        request_data = {
            'ocid': self.ocid,
            'k8s_context': self.k8s_context,
            'directory_name': BundleHelper.get_home_directory(),
            'bundle_name': mesh_bundle_name
        }
        if self.ocid is None:
            request_types = [DebugHandlerRequestType.K8S_CHECK, DebugHandlerRequestType.K8S_CHECK_CONTEXT,
                             DebugHandlerRequestType.BUNDLE_NAME, DebugHandlerRequestType.TASK,
                             DebugHandlerRequestType.BUNDLE_COMPRESS,
                             DebugHandlerRequestType.BUNDLE_CLEANUP]
        else:
            request_types = [DebugHandlerRequestType.K8S_CHECK, DebugHandlerRequestType.K8S_CHECK_CONTEXT,
                             DebugHandlerRequestType.OCID_VALIDATION,
                             DebugHandlerRequestType.BUNDLE_NAME, DebugHandlerRequestType.TASK,
                             DebugHandlerRequestType.BUNDLE_COMPRESS,
                             DebugHandlerRequestType.BUNDLE_CLEANUP]

        for request_type in request_types:
            request = {
                'type': request_type,
                'data': request_data,
                'kube_command_helper': kube_command_helper
            }
            result = self.debug_handler.handle(request)
            if not result.status == ResultStatus.OK:
                return result.exception

        click.echo('\nMesh Bundle generated: {}.zip'.format(mesh_bundle_name), file=sys.stdout)
        return None
