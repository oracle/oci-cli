# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.os_management_hub.src.oci_cli_reporting_managed_instance.generated import reportingmanagedinstance_cli
from services.os_management_hub.src.oci_cli_managed_instance.generated import managedinstance_cli
from services.os_management_hub.src.oci_cli_os_management_hub.generated import os_management_hub_service_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci os-management-hub reporting-managed-instance managed-instance get-managed-instance-analytic-content -> oci os-management-hub reporting-managed-instance managed-instance get-analytic-content
cli_util.rename_command(reportingmanagedinstance_cli, reportingmanagedinstance_cli.managed_instance_group, reportingmanagedinstance_cli.get_managed_instance_analytic_content, "get-analytic-content")


# oci os-management-hub reporting-managed-instance managed-instance get-managed-instance-content -> oci os-management-hub reporting-managed-instance managed-instance get-content
cli_util.rename_command(reportingmanagedinstance_cli, reportingmanagedinstance_cli.managed_instance_group, reportingmanagedinstance_cli.get_managed_instance_content, "get-content")


# oci os-management-hub reporting-managed-instance managed-instance-analytic-collection summarize-managed-instance-analytics -> oci os-management-hub reporting-managed-instance managed-instance-analytic-collection summarize-analytics
cli_util.rename_command(reportingmanagedinstance_cli, reportingmanagedinstance_cli.managed_instance_analytic_collection_group, reportingmanagedinstance_cli.summarize_managed_instance_analytics, "summarize-analytics")


@cli_util.copy_params_from_generated_command(reportingmanagedinstance_cli.get_managed_instance_analytic_content, params_to_exclude=['bug_updates_available_equals_to', 'bug_updates_available_greater_than', 'lifecycle_environment_id', 'managed_instance_group_id', 'security_updates_available_equals_to', 'security_updates_available_greater_than', 'lifecycle_stage_id', 'location_not_equal_to', 'is_managed_by_autonomous_linux'])
@managedinstance_cli.managed_instance_group.command(name=reportingmanagedinstance_cli.get_managed_instance_analytic_content.name, help=reportingmanagedinstance_cli.get_managed_instance_analytic_content.help)
@cli_util.option('--bug-updates-eq', type=click.INT, help=u"""A filter to return instances with number of available bug updates equals to the number specified.""")
@cli_util.option('--bug-updates-gt', type=click.INT, help=u"""A filter to return instances with number of available bug updates greater than the number specified.""")
@cli_util.option('--lifecycle-env-id', help=u"""The OCID of the lifecycle environment.""")
@cli_util.option('--group-id', help=u"""The OCID of the managed instance group for which to list resources.""")
@cli_util.option('--security-updates-eq', type=click.INT, help=u"""A filter to return instances with number of available security updates equals to the number specified.""")
@cli_util.option('--security-updates-gt', type=click.INT, help=u"""A filter to return instances with number of available security updates greater than the number specified.""")
@cli_util.option('--stage-id', help=u"""The OCID of the lifecycle stage for which to list resources.""")
@cli_util.option('--location-ne', type=custom_types.CliCaseInsensitiveChoice(["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]), multiple=True, help="""A filter to return only resources whose location does not match the given value.""")
@cli_util.option('--is-managed-by-alx', type=click.BOOL, help="""Indicates whether to list only resources managed by the Autonomous Linux service.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'display-name': {'module': 'os_management_hub', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def get_managed_instance_analytic_content_extended(ctx, **kwargs):

    if 'bug_updates_eq' in kwargs:
        kwargs['bug_updates_available_equals_to'] = kwargs['bug_updates_eq']
        kwargs.pop('bug_updates_eq')

    if 'bug_updates_gt' in kwargs:
        kwargs['bug_updates_available_greater_than'] = kwargs['bug_updates_gt']
        kwargs.pop('bug_updates_gt')

    if 'lifecycle_env_id' in kwargs:
        kwargs['lifecycle_environment_id'] = kwargs['lifecycle_env_id']
        kwargs.pop('lifecycle_env_id')

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    if 'security_updates_eq' in kwargs:
        kwargs['security_updates_available_equals_to'] = kwargs['security_updates_eq']
        kwargs.pop('security_updates_eq')

    if 'security_updates_gt' in kwargs:
        kwargs['security_updates_available_greater_than'] = kwargs['security_updates_gt']
        kwargs.pop('security_updates_gt')

    if 'stage_id' in kwargs:
        kwargs['lifecycle_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    if 'location_ne' in kwargs:
        kwargs['location_not_equal_to'] = kwargs['location_ne']
        kwargs.pop('location_ne')

    if 'is_managed_by_alx' in kwargs:
        kwargs['is_managed_by_autonomous_linux'] = kwargs['is_managed_by_alx']
        kwargs.pop('is_managed_by_alx')

    ctx.invoke(reportingmanagedinstance_cli.get_managed_instance_analytic_content, **kwargs)


@cli_util.copy_params_from_generated_command(reportingmanagedinstance_cli.summarize_managed_instance_analytics, params_to_exclude=['lifecycle_environment_id', 'managed_instance_group_id', 'lifecycle_stage_id', 'location_not_equal_to', 'is_managed_by_autonomous_linux'])
@managedinstance_cli.managed_instance_group.command(name=reportingmanagedinstance_cli.summarize_managed_instance_analytics.name, help=reportingmanagedinstance_cli.summarize_managed_instance_analytics.help)
@cli_util.option('--lifecycle-env-id', help=u"""The OCID of the lifecycle environment.""")
@cli_util.option('--group-id', help=u"""The OCID of the managed instance group for which to list resources.""")
@cli_util.option('--stage-id', help=u"""The OCID of the lifecycle stage for which to list resources.""")
@cli_util.option('--location-ne', type=custom_types.CliCaseInsensitiveChoice(["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]), multiple=True, help="""A filter to return only resources whose location does not match the given value.""")
@cli_util.option('--is-managed-by-alx', type=click.BOOL, help="""Indicates whether to list only resources managed by the Autonomous Linux service.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'display-name': {'module': 'os_management_hub', 'class': 'list[string]'}}, output_type={'module': 'os_management_hub', 'class': 'ManagedInstanceAnalyticCollection'})
@cli_util.wrap_exceptions
def summarize_managed_instance_analytics_extended(ctx, **kwargs):

    if 'lifecycle_env_id' in kwargs:
        kwargs['lifecycle_environment_id'] = kwargs['lifecycle_env_id']
        kwargs.pop('lifecycle_env_id')

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    if 'stage_id' in kwargs:
        kwargs['lifecycle_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    if 'location_ne' in kwargs:
        kwargs['location_not_equal_to'] = kwargs['location_ne']
        kwargs.pop('location_ne')

    if 'is_managed_by_alx' in kwargs:
        kwargs['is_managed_by_autonomous_linux'] = kwargs['is_managed_by_alx']
        kwargs.pop('is_managed_by_alx')

    ctx.invoke(reportingmanagedinstance_cli.summarize_managed_instance_analytics, **kwargs)


# Move commands under 'oci os-management-hub reporting-managed-instance managed-instance-analytic-collection' -> 'oci os-management-hub managed-instance'
reportingmanagedinstance_cli.reporting_managed_instance_root_group.commands.pop(reportingmanagedinstance_cli.managed_instance_analytic_collection_group.name)
managedinstance_cli.managed_instance_group.add_command(summarize_managed_instance_analytics_extended)


# Move commands under 'oci os-management-hub reporting-managed-instance managed-instance' -> 'oci os-management-hub managed-instance'
reportingmanagedinstance_cli.reporting_managed_instance_root_group.commands.pop(reportingmanagedinstance_cli.managed_instance_group.name)
managedinstance_cli.managed_instance_group.add_command(get_managed_instance_analytic_content_extended)
managedinstance_cli.managed_instance_group.add_command(reportingmanagedinstance_cli.get_managed_instance_content)


# Move commands under 'oci os-management-hub reporting-managed-instance' -> 'oci os-management-hub managed-instance'
os_management_hub_service_cli.os_management_hub_service_group.commands.pop(reportingmanagedinstance_cli.reporting_managed_instance_root_group.name)
reportingmanagedinstance_cli.managed_instance_analytic_collection_group.commands.pop(reportingmanagedinstance_cli.summarize_managed_instance_analytics.name)
