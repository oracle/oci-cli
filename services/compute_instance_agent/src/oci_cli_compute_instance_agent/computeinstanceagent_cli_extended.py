# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from services.compute_instance_agent.src.oci_cli_compute_instance_agent.generated import instance_agent_service_cli
from services.compute_instance_agent.src.oci_cli_compute_instance_agent.generated import computeinstanceagent_cli

instance_agent_service_cli.instance_agent_service_group.commands.pop(computeinstanceagent_cli.compute_instance_agent_root_group.name)

instance_agent_service_cli.instance_agent_service_group.help = "Compute Instance Agent Service CLI"
instance_agent_service_cli.instance_agent_service_group.short_help = "Compute Instance Agent Service"

cli_util.rename_command(instance_agent_service_cli, instance_agent_service_cli.instance_agent_service_group, computeinstanceagent_cli.instance_agent_command_group, "command")
cli_util.rename_command(instance_agent_service_cli, instance_agent_service_cli.instance_agent_service_group, computeinstanceagent_cli.instance_agent_command_execution_group, "command-execution")


@cli_util.copy_params_from_generated_command(computeinstanceagent_cli.cancel_instance_agent_command, params_to_exclude=['instance_agent_command_id'])
@computeinstanceagent_cli.instance_agent_command_group.command(name=cli_util.override('instance_agent.cancel_instance_agent_command.command_name', 'cancel'), help=computeinstanceagent_cli.cancel_instance_agent_command.help)
@cli_util.option('--command-id', required=True, help=u"""The OCID of the command.""")
@cli_util.confirm_delete_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_instance_agent_command(ctx, **kwargs):
    kwargs['instance_agent_command_id'] = kwargs['command_id']
    del kwargs['command_id']
    ctx.invoke(computeinstanceagent_cli.cancel_instance_agent_command, **kwargs)


@cli_util.copy_params_from_generated_command(computeinstanceagent_cli.create_instance_agent_command, params_to_exclude=['execution_time_out_in_seconds'])
@computeinstanceagent_cli.instance_agent_command_group.command(name=cli_util.override('instance_agent.create_instance_agent_command.command_name', 'create'), help=computeinstanceagent_cli.create_instance_agent_command.help)
@cli_util.option('--timeout-in-seconds', required=True, help=u"""Command execution time limit. Zero means no timeout.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'target': {'module': 'compute_instance_agent', 'class': 'InstanceAgentCommandTarget'}, 'content': {'module': 'compute_instance_agent', 'class': 'InstanceAgentCommandContent'}}, output_type={'module': 'compute_instance_agent', 'class': 'InstanceAgentCommand'})
@cli_util.wrap_exceptions
def create_instance_agent_command(ctx, **kwargs):
    kwargs['execution_time_out_in_seconds'] = kwargs['timeout_in_seconds']
    del kwargs['timeout_in_seconds']
    ctx.invoke(computeinstanceagent_cli.create_instance_agent_command, **kwargs)


@cli_util.copy_params_from_generated_command(computeinstanceagent_cli.get_instance_agent_command, params_to_exclude=['instance_agent_command_id'])
@computeinstanceagent_cli.instance_agent_command_group.command(name=cli_util.override('instance_agent.get_instance_agent_command.command_name', 'get'), help=computeinstanceagent_cli.get_instance_agent_command.help)
@cli_util.option('--command-id', required=True, help=u"""The OCID of the command.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'compute_instance_agent', 'class': 'InstanceAgentCommand'})
@cli_util.wrap_exceptions
def get_instance_agent_command(ctx, **kwargs):
    kwargs['instance_agent_command_id'] = kwargs['command_id']
    del kwargs['command_id']
    ctx.invoke(computeinstanceagent_cli.get_instance_agent_command, **kwargs)


@cli_util.copy_params_from_generated_command(computeinstanceagent_cli.get_instance_agent_command_execution, params_to_exclude=['instance_agent_command_id'])
@computeinstanceagent_cli.instance_agent_command_execution_group.command(name=cli_util.override('instance_agent.get_instance_agent_command_execution.command_name', 'get'), help=computeinstanceagent_cli.get_instance_agent_command_execution.help)
@cli_util.option('--command-id', required=True, help=u"""The OCID of the command.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'compute_instance_agent', 'class': 'InstanceAgentCommandExecution'})
@cli_util.wrap_exceptions
def get_instance_agent_command_execution(ctx, **kwargs):
    kwargs['instance_agent_command_id'] = kwargs['command_id']
    del kwargs['command_id']
    ctx.invoke(computeinstanceagent_cli.get_instance_agent_command_execution, **kwargs)
