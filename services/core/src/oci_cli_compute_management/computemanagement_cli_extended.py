# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
from services.core.src.oci_cli_compute_management.generated import computemanagement_cli
from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils

cli.add_command(computemanagement_cli.compute_management_root_group)
cli_util.rename_command(computemanagement_cli, computemanagement_cli.instance_pool_group, computemanagement_cli.list_instance_pool_instances, "list-instances")
cli_util.rename_command(computemanagement_cli, computemanagement_cli.instance_configuration_group, computemanagement_cli.launch_instance_configuration_compute_instance_details, "launch-compute-instance")

computemanagement_cli.instance_configuration_group.commands.pop(computemanagement_cli.create_instance_configuration.name)
cli_util.rename_command(computemanagement_cli, computemanagement_cli.instance_configuration_group, computemanagement_cli.create_instance_configuration_create_instance_configuration_details, "create")
cli_util.rename_command(computemanagement_cli, computemanagement_cli.instance_configuration_group, computemanagement_cli.create_instance_configuration_create_instance_configuration_from_instance_details, "create-from-instance")

# hide compute management 'instances' group, commands belong under other groups
computemanagement_cli.compute_management_root_group.commands.pop(computemanagement_cli.instance_group.name)
computemanagement_cli.instance_pool_group.add_command(computemanagement_cli.list_instance_pool_instances)
computemanagement_cli.instance_configuration_group.add_command(computemanagement_cli.launch_instance_configuration_compute_instance_details)

computemanagement_cli.compute_management_root_group.help = "Compute Management Service CLI"
computemanagement_cli.compute_management_root_group.short_help = "Compute Management Service"

cli_util.rename_command(computemanagement_cli, computemanagement_cli.instance_pool_group, computemanagement_cli.attach_load_balancer, "attach-lb")
cli_util.rename_command(computemanagement_cli, computemanagement_cli.instance_pool_group, computemanagement_cli.detach_load_balancer, "detach-lb")

# From: oci compute-management instance-pool-load-balancer-attachment get --instance-pool-id, --instance-pool-load-balancer-attachment-id
# To:   oci compute-management instance-pool lb-attachment get --instance-pool-id, --lb-attachment-id
computemanagement_cli.compute_management_root_group.commands.pop(computemanagement_cli.instance_pool_load_balancer_attachment_group.name)
computemanagement_cli.instance_pool_load_balancer_attachment_group.commands.pop(computemanagement_cli.get_instance_pool_load_balancer_attachment.name)
computemanagement_cli.instance_pool_group.add_command(computemanagement_cli.instance_pool_load_balancer_attachment_group)
cli_util.rename_command(computemanagement_cli, computemanagement_cli.instance_pool_group, computemanagement_cli.instance_pool_load_balancer_attachment_group, "lb-attachment")


# Adding the following 2 manual renames since using the rename_command also renames the existing top level commands (attach-lb, detach-lb)
@cli_util.copy_params_from_generated_command(computemanagement_cli.attach_load_balancer, params_to_exclude=[])
@computemanagement_cli.instance_pool_load_balancer_attachment_group.command(name="attach", help=u"""Attach a load balancer to the instance pool.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstancePool'})
@cli_util.wrap_exceptions
def attach_load_balancer_extended(ctx, **kwargs):
    ctx.invoke(computemanagement_cli.attach_load_balancer, **kwargs)


@cli_util.copy_params_from_generated_command(computemanagement_cli.detach_load_balancer, params_to_exclude=[])
@computemanagement_cli.instance_pool_load_balancer_attachment_group.command(name="detach", help=u"""Detach a load balancer from the instance pool.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstancePool'})
@cli_util.wrap_exceptions
def detach_load_balancer_extended(ctx, **kwargs):
    ctx.invoke(computemanagement_cli.detach_load_balancer, **kwargs)


@cli_util.copy_params_from_generated_command(computemanagement_cli.get_instance_pool_load_balancer_attachment, params_to_exclude=['instance_pool_load_balancer_attachment_id'])
@computemanagement_cli.instance_pool_load_balancer_attachment_group.command(name=cli_util.override('get_instance_pool_load_balancer_attachment.command_name', 'get'), help=computemanagement_cli.get_instance_pool_load_balancer_attachment.help)
@cli_util.option('--lb-attachment-id', required=True, help=u"""The OCID of the load balancer attachment.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstancePoolLoadBalancerAttachment'})
@cli_util.wrap_exceptions
def get_lb_attachment(ctx, **kwargs):
    kwargs['instance_pool_load_balancer_attachment_id'] = kwargs['lb_attachment_id']
    del kwargs['lb_attachment_id']
    ctx.invoke(computemanagement_cli.get_instance_pool_load_balancer_attachment, **kwargs)


# from: oci compute-management cluster-network list-cluster-network-instances
# to:   oci compute-management cluster-network list-instances
cli_util.rename_command(computemanagement_cli, computemanagement_cli.cluster_network_group, computemanagement_cli.list_cluster_network_instances, "list-instances")
