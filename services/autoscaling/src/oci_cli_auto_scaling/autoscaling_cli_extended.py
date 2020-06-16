# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


import click
from oci_cli import cli_util
from services.autoscaling.src.oci_cli_auto_scaling.generated import autoscaling_cli
from oci_cli import json_skeleton_utils

autoscaling_cli.auto_scaling_policy_group.commands.pop(autoscaling_cli.create_auto_scaling_policy_create_threshold_policy_details.name)
autoscaling_cli.auto_scaling_policy_group.commands.pop(autoscaling_cli.update_auto_scaling_policy_update_threshold_policy_details.name)

# Removing oci autoscaling policy create-auto-scaling-policy-create-scheduled-policy-details
autoscaling_cli.auto_scaling_policy_group.commands.pop(autoscaling_cli.create_auto_scaling_policy_create_scheduled_policy_details.name)

# Removing oci autoscaling policy update-auto-scaling-policy-update-scheduled-policy-details
autoscaling_cli.auto_scaling_policy_group.commands.pop(autoscaling_cli.update_auto_scaling_policy_update_scheduled_policy_details.name)

# Removing oci autoscaling auto-scaling-policy-summary list-auto-scaling-policies
autoscaling_cli.autoscaling_root_group.commands.pop(autoscaling_cli.auto_scaling_policy_summary_group.name)

autoscaling_cli.auto_scaling_configuration_group.commands.pop(autoscaling_cli.create_auto_scaling_configuration_instance_pool_resource.name)

cli_util.rename_command(autoscaling_cli, autoscaling_cli.autoscaling_root_group, autoscaling_cli.auto_scaling_configuration_group, "configuration")
cli_util.rename_command(autoscaling_cli, autoscaling_cli.autoscaling_root_group, autoscaling_cli.auto_scaling_policy_group, "policy")


@cli_util.copy_params_from_generated_command(autoscaling_cli.create_auto_scaling_policy)
@autoscaling_cli.auto_scaling_policy_group.command(name=cli_util.override('autoscaling_cli.create_auto_scaling_policy_extended.command_name', 'create'), help=autoscaling_cli.create_auto_scaling_policy.help)
@cli_util.option('--execution-schedule', type=cli_util.get_param(autoscaling_cli.create_auto_scaling_policy_create_scheduled_policy_details, 'execution_schedule').type, help=cli_util.copy_help_from_generated_code(autoscaling_cli.create_auto_scaling_policy_create_scheduled_policy_details, 'execution_schedule', remove_required=True))
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'autoscaling', 'class': 'Capacity'}, 'execution-schedule': {'module': 'autoscaling', 'class': 'ExecutionSchedule'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingPolicy'})
@cli_util.wrap_exceptions
def create_auto_scaling_policy_extended(ctx, **kwargs):
    if kwargs['policy_type'] is not None and str(kwargs['policy_type']).lower() == 'scheduled':
        if kwargs['execution_schedule'] is None:
            raise click.UsageError('If Parameter --policy-type is scheduled, then Parameter --execution-schedule must be provided')
        else:
            # Since autoscaling_cli.create_auto_scaling_policy_create_scheduled_policy_details doesn't expect the parameter policy_type
            del(kwargs['policy_type'])
            ctx.invoke(autoscaling_cli.create_auto_scaling_policy_create_scheduled_policy_details, **kwargs)
    else:
        # Since autoscaling_cli.create_auto_scaling_policy doesn't expect the parameter execution_schedule
        del(kwargs['execution_schedule'])
        ctx.invoke(autoscaling_cli.create_auto_scaling_policy, **kwargs)


@cli_util.copy_params_from_generated_command(autoscaling_cli.update_auto_scaling_policy)
@autoscaling_cli.auto_scaling_policy_group.command(name=cli_util.override('autoscaling_cli.update_auto_scaling_policy_extended.command_name', 'update'), help=autoscaling_cli.update_auto_scaling_policy.help)
@cli_util.option('--execution-schedule', type=cli_util.get_param(autoscaling_cli.update_auto_scaling_policy_update_scheduled_policy_details, 'execution_schedule').type, help=cli_util.copy_help_from_generated_code(autoscaling_cli.update_auto_scaling_policy_update_scheduled_policy_details, 'execution_schedule', remove_required=True))
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'autoscaling', 'class': 'Capacity'}, 'execution-schedule': {'module': 'autoscaling', 'class': 'ExecutionSchedule'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingPolicy'})
@cli_util.wrap_exceptions
def update_auto_scaling_policy_extended(ctx, **kwargs):
    if kwargs['policy_type'] is not None and str(kwargs['policy_type']).lower() == 'scheduled':
        if kwargs['execution_schedule'] is None:
            raise click.UsageError('If Parameter --policy-type is scheduled, then Parameter --execution-schedule must be provided')
        else:
            # Since autoscaling_cli.update_auto_scaling_policy_update_scheduled_policy_details doesn't expect the parameter policy_type
            del(kwargs['policy_type'])
            ctx.invoke(autoscaling_cli.update_auto_scaling_policy_update_scheduled_policy_details, **kwargs)
    else:
        # Since autoscaling_cli.update_auto_scaling_policy doesn't expect the parameter execution_schedule
        del(kwargs['execution_schedule'])
        ctx.invoke(autoscaling_cli.update_auto_scaling_policy, **kwargs)
