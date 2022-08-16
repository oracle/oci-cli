# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import os.path
import sys

import click
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias

from services.service_mesh.src.oci_cli_service_mesh.generated import servicemesh_cli
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.bundle_analyser import BundleAnalyser
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.report_orchestrator \
    import ReportOrchestrator
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.bundle_helper import BundleHelper


@click.command(cli_util.override('service_mesh.debug_group.command_name', 'debug'), cls=CommandGroupWithAlias,
               help="""Debug enables customers to troubleshoot service-mesh resources.""")
@cli_util.help_option_group
def debug_group():
    pass


# oci service-mesh debug
servicemesh_cli.service_mesh_root_group.add_command(debug_group)


# oci service-mesh debug report
# oci service-mesh debug report --resource-id <ocid>
# oci service-mesh debug report --resource-id <ocid> --k8s-context <path_to_config_file>
@debug_group.command(name=cli_util.override('service_mesh.report.command_name', 'report'),
                     help=u"""Generates report to troubleshoot Service Mesh resources and setup.""")
@cli_util.option('--resource-id', required=False, help=u"""The [OCID] of the service-mesh resource.""")
@cli_util.option('--kubeconfig', required=False, help=u"""The filepath of the config file containing the kubernetes config of the Kubernetes Cluster. If not specified default config file will be applied.""")
@cli_util.option('--context', required=False, help=u"""Context to be used in the kube config file. If not specified, the current-context is used by default.""")
@cli_util.option('--thread-pool-size', required=False, help=u"""The Size of thread pool to execute the command""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def generate_mesh(ctx, resource_id, kubeconfig, context, thread_pool_size):
    try:
        report_orchestrator = ReportOrchestrator(resource_id, kubeconfig, context, thread_pool_size)
        result = report_orchestrator.build_report()
        if result is not None:
            click.echo(result, file=sys.stderr)
        else:
            click.echo('Report generation successful.', file=sys.stdout)
            bundle_file_path = os.path.join(BundleHelper.get_home_directory(), BundleHelper.get_bundle_name())
            # click.echo - Bundle file path
            click.echo('\nBundle file path: {}'.format(bundle_file_path))
            # call Analyser
            bundle_analyzer = BundleAnalyser(bundle_file_path=bundle_file_path)
            analyze = bundle_analyzer.analyze()
    except Exception as e:
        click.echo('Report generation unsuccessful. Some problem occurred during report generation. {}'.format(e),
                   file=sys.stderr)
