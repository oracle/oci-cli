# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.datacc.src.oci_cli_baseinfra.generated import baseinfra_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci datacc work-request-log-entry -> oci datacc work-request-log
cli_util.rename_command(baseinfra_cli, baseinfra_cli.datacc_root_group, baseinfra_cli.work_request_log_entry_group, "work-request-log")


# Move commands under 'oci datacc infrastructure-summary' -> 'oci datacc infrastructure'
baseinfra_cli.datacc_root_group.commands.pop(baseinfra_cli.infrastructure_summary_group.name)
baseinfra_cli.infrastructure_group.add_command(baseinfra_cli.list_infrastructures)


# Move commands under 'oci datacc vm-cluster-network-summary' -> 'oci datacc vm-cluster-network'
baseinfra_cli.datacc_root_group.commands.pop(baseinfra_cli.vm_cluster_network_summary_group.name)
baseinfra_cli.vm_cluster_network_group.add_command(baseinfra_cli.list_vm_cluster_networks)


# Move commands under 'oci datacc vm-instance-summary' -> 'oci datacc vm-instance'
baseinfra_cli.datacc_root_group.commands.pop(baseinfra_cli.vm_instance_summary_group.name)
baseinfra_cli.vm_instance_group.add_command(baseinfra_cli.list_vm_instances)


@cli_util.copy_params_from_generated_command(baseinfra_cli.create_infrastructure, params_to_exclude=['cloud_control_plane_server1', 'cloud_control_plane_server2'])
@baseinfra_cli.infrastructure_group.command(name=baseinfra_cli.create_infrastructure.name, help=baseinfra_cli.create_infrastructure.help)
@cli_util.option('--control-plane-server2', required=True, help="""The IP address for the second control plane server. [required]""")
@cli_util.option('--control-plane-server1', required=True, help=u"""The IP address for the first control plane server. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'contacts': {'module': 'datacc', 'class': 'list[InfrastructureContact]'}, 'dns-servers': {'module': 'datacc', 'class': 'list[string]'}, 'ntp-servers': {'module': 'datacc', 'class': 'list[string]'}, 'maintenance-window': {'module': 'datacc', 'class': 'MaintenanceWindow'}, 'freeform-tags': {'module': 'datacc', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'datacc', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'datacc', 'class': 'Infrastructure'})
@cli_util.wrap_exceptions
def create_infrastructure_extended(ctx, **kwargs):

    if 'control_plane_server2' in kwargs:
        kwargs['cloud_control_plane_server2'] = kwargs['control_plane_server2']
        kwargs.pop('control_plane_server2')

    if 'control_plane_server1' in kwargs:
        kwargs['cloud_control_plane_server1'] = kwargs['control_plane_server1']
        kwargs.pop('control_plane_server1')

    ctx.invoke(baseinfra_cli.create_infrastructure, **kwargs)


@cli_util.copy_params_from_generated_command(baseinfra_cli.update_infrastructure, params_to_exclude=['cloud_control_plane_server1', 'cloud_control_plane_server2'])
@baseinfra_cli.infrastructure_group.command(name=baseinfra_cli.update_infrastructure.name, help=baseinfra_cli.update_infrastructure.help)
@cli_util.option('--control-plane-server2', help="""The IP address for the second control plane server.""")
@cli_util.option('--control-plane-server1', help=u"""The IP address for the first control plane server.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'contacts': {'module': 'datacc', 'class': 'list[InfrastructureContact]'}, 'dns-servers': {'module': 'datacc', 'class': 'list[string]'}, 'ntp-servers': {'module': 'datacc', 'class': 'list[string]'}, 'maintenance-window': {'module': 'datacc', 'class': 'MaintenanceWindow'}, 'defined-tags': {'module': 'datacc', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'datacc', 'class': 'dict(str, string)'}}, output_type={'module': 'datacc', 'class': 'Infrastructure'})
@cli_util.wrap_exceptions
def update_infrastructure_extended(ctx, **kwargs):

    if 'control_plane_server2' in kwargs:
        kwargs['cloud_control_plane_server2'] = kwargs['control_plane_server2']
        kwargs.pop('control_plane_server2')

    if 'control_plane_server1' in kwargs:
        kwargs['cloud_control_plane_server1'] = kwargs['control_plane_server1']
        kwargs.pop('control_plane_server1')

    ctx.invoke(baseinfra_cli.update_infrastructure, **kwargs)
