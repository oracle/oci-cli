# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.disaster_recovery.src.oci_cli_disaster_recovery.generated import disasterrecovery_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci disaster-recovery dr-plan-execution create-dr-plan-execution-failover-execution-option-details -> oci disaster-recovery dr-plan-execution create-failover
cli_util.rename_command(disasterrecovery_cli, disasterrecovery_cli.dr_plan_execution_group, disasterrecovery_cli.create_dr_plan_execution_failover_execution_option_details, "create-failover")


# oci disaster-recovery dr-plan-execution create-dr-plan-execution-failover-precheck-execution-option-details -> oci disaster-recovery dr-plan-execution create-failover-precheck
cli_util.rename_command(disasterrecovery_cli, disasterrecovery_cli.dr_plan_execution_group, disasterrecovery_cli.create_dr_plan_execution_failover_precheck_execution_option_details, "create-failover-precheck")


# oci disaster-recovery dr-plan-execution create-dr-plan-execution-switchover-execution-option-details -> oci disaster-recovery dr-plan-execution create-switchover
cli_util.rename_command(disasterrecovery_cli, disasterrecovery_cli.dr_plan_execution_group, disasterrecovery_cli.create_dr_plan_execution_switchover_execution_option_details, "create-switchover")


# oci disaster-recovery dr-plan-execution create-dr-plan-execution-switchover-precheck-execution-option-details -> oci disaster-recovery dr-plan-execution create-switchover-precheck
cli_util.rename_command(disasterrecovery_cli, disasterrecovery_cli.dr_plan_execution_group, disasterrecovery_cli.create_dr_plan_execution_switchover_precheck_execution_option_details, "create-switchover-precheck")


# oci disaster-recovery work-request-log-entry list-work-request-logs -> oci disaster-recovery work-request-log-entry list
cli_util.rename_command(disasterrecovery_cli, disasterrecovery_cli.work_request_log_entry_group, disasterrecovery_cli.list_work_request_logs, "list")


# oci disaster-recovery work-request-log-entry -> oci disaster-recovery work-request-logs
cli_util.rename_command(disasterrecovery_cli, disasterrecovery_cli.disaster_recovery_root_group, disasterrecovery_cli.work_request_log_entry_group, "work-request-logs")


# oci disaster-recovery dr-protection-group update-dr-protection-group-role -> oci disaster-recovery dr-protection-group update-role
cli_util.rename_command(disasterrecovery_cli, disasterrecovery_cli.dr_protection_group_group, disasterrecovery_cli.update_dr_protection_group_role, "update-role")


# Remove disassociate-dr-protection-group-disassociate-dr-protection-group-default-details from oci disaster-recovery dr-protection-group
disasterrecovery_cli.dr_protection_group_group.commands.pop(disasterrecovery_cli.disassociate_dr_protection_group_disassociate_dr_protection_group_default_details.name)


@cli_util.copy_params_from_generated_command(disasterrecovery_cli.create_dr_plan_execution_failover_execution_option_details, params_to_exclude=['execution_options_are_prechecks_enabled', 'execution_options_are_warnings_ignored'])
@disasterrecovery_cli.dr_plan_execution_group.command(name=disasterrecovery_cli.create_dr_plan_execution_failover_execution_option_details.name, help=disasterrecovery_cli.create_dr_plan_execution_failover_execution_option_details.help)
@cli_util.option('--prechecks-enabled', type=click.BOOL, help=u"""A flag indicating whether a precheck should be executed before the plan.

Example: `true`""")
@cli_util.option('--warnings-ignored', type=click.BOOL, help=u"""A flag indicating whether warnings should be ignored during the failover.

Example: `false`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'disaster_recovery', 'class': 'DrPlanExecution'})
@cli_util.wrap_exceptions
def create_dr_plan_execution_failover_execution_option_details_extended(ctx, **kwargs):

    if 'prechecks_enabled' in kwargs:
        kwargs['execution_options_are_prechecks_enabled'] = kwargs['prechecks_enabled']
        kwargs.pop('prechecks_enabled')

    if 'warnings_ignored' in kwargs:
        kwargs['execution_options_are_warnings_ignored'] = kwargs['warnings_ignored']
        kwargs.pop('warnings_ignored')

    ctx.invoke(disasterrecovery_cli.create_dr_plan_execution_failover_execution_option_details, **kwargs)


@cli_util.copy_params_from_generated_command(disasterrecovery_cli.create_dr_plan_execution_failover_precheck_execution_option_details, params_to_exclude=['execution_options_are_warnings_ignored'])
@disasterrecovery_cli.dr_plan_execution_group.command(name=disasterrecovery_cli.create_dr_plan_execution_failover_precheck_execution_option_details.name, help=disasterrecovery_cli.create_dr_plan_execution_failover_precheck_execution_option_details.help)
@cli_util.option('--warnings-ignored', type=click.BOOL, help=u"""A flag indicating whether warnings should be ignored during the failover.

Example: `false`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'disaster_recovery', 'class': 'DrPlanExecution'})
@cli_util.wrap_exceptions
def create_dr_plan_execution_failover_precheck_execution_option_details_extended(ctx, **kwargs):

    if 'warnings_ignored' in kwargs:
        kwargs['execution_options_are_warnings_ignored'] = kwargs['warnings_ignored']
        kwargs.pop('warnings_ignored')

    ctx.invoke(disasterrecovery_cli.create_dr_plan_execution_failover_precheck_execution_option_details, **kwargs)


@cli_util.copy_params_from_generated_command(disasterrecovery_cli.create_dr_plan_execution_switchover_execution_option_details, params_to_exclude=['execution_options_are_prechecks_enabled', 'execution_options_are_warnings_ignored'])
@disasterrecovery_cli.dr_plan_execution_group.command(name=disasterrecovery_cli.create_dr_plan_execution_switchover_execution_option_details.name, help=disasterrecovery_cli.create_dr_plan_execution_switchover_execution_option_details.help)
@cli_util.option('--prechecks-enabled', type=click.BOOL, help=u"""A flag indicating whether a precheck should be executed before the plan.

Example: `false`""")
@cli_util.option('--warnings-ignored', type=click.BOOL, help=u"""A flag indicating whether warnings should be ignored during the switchover.

Example: `true`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'disaster_recovery', 'class': 'DrPlanExecution'})
@cli_util.wrap_exceptions
def create_dr_plan_execution_switchover_execution_option_details_extended(ctx, **kwargs):

    if 'prechecks_enabled' in kwargs:
        kwargs['execution_options_are_prechecks_enabled'] = kwargs['prechecks_enabled']
        kwargs.pop('prechecks_enabled')

    if 'warnings_ignored' in kwargs:
        kwargs['execution_options_are_warnings_ignored'] = kwargs['warnings_ignored']
        kwargs.pop('warnings_ignored')

    ctx.invoke(disasterrecovery_cli.create_dr_plan_execution_switchover_execution_option_details, **kwargs)


@cli_util.copy_params_from_generated_command(disasterrecovery_cli.create_dr_plan_execution_switchover_precheck_execution_option_details, params_to_exclude=['execution_options_are_warnings_ignored'])
@disasterrecovery_cli.dr_plan_execution_group.command(name=disasterrecovery_cli.create_dr_plan_execution_switchover_precheck_execution_option_details.name, help=disasterrecovery_cli.create_dr_plan_execution_switchover_precheck_execution_option_details.help)
@cli_util.option('--warnings-ignored', type=click.BOOL, help=u"""A flag indicating whether warnings should be ignored during the switchover.

Example: `true`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'disaster_recovery', 'class': 'DrPlanExecution'})
@cli_util.wrap_exceptions
def create_dr_plan_execution_switchover_precheck_execution_option_details_extended(ctx, **kwargs):

    if 'warnings_ignored' in kwargs:
        kwargs['execution_options_are_warnings_ignored'] = kwargs['warnings_ignored']
        kwargs.pop('warnings_ignored')

    ctx.invoke(disasterrecovery_cli.create_dr_plan_execution_switchover_precheck_execution_option_details, **kwargs)
