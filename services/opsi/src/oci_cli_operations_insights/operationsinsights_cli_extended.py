# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.opsi.src.oci_cli_operations_insights.generated import operationsinsights_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci opsi database-insights create-database-insight-create-em-managed-external-database-insight-details -> oci opsi database-insights create-em-external-db
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.create_database_insight_create_em_managed_external_database_insight_details, "create-em-external-db")


# oci opsi database-insights enable-database-insight-enable-em-managed-external-database-insight-details -> oci opsi database-insights enable-em-external-db
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.enable_database_insight_enable_em_managed_external_database_insight_details, "enable-em-external-db")


# oci opsi database-insights update-database-insight-update-autonomous-database-insight-details -> oci opsi database-insights update-autonomous-db
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.update_database_insight_update_autonomous_database_insight_details, "update-autonomous-db")


# oci opsi database-insights update-database-insight-update-em-managed-external-database-insight-details -> oci opsi database-insights update-em-external-db
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.update_database_insight_update_em_managed_external_database_insight_details, "update-em-external-db")


# oci opsi database-insights update-database-insight-update-macs-managed-external-database-insight-details -> oci opsi database-insights update-macs-external-db
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.update_database_insight_update_macs_managed_external_database_insight_details, "update-macs-external-db")


# oci opsi host-insights create-host-insight-create-macs-managed-external-host-insight-details -> oci opsi host-insights create-macs-external-host
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.create_host_insight_create_macs_managed_external_host_insight_details, "create-macs-external-host")


# oci opsi host-insights enable-host-insight-enable-macs-managed-external-host-insight-details -> oci opsi host-insights enable-macs-external-host
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.enable_host_insight_enable_macs_managed_external_host_insight_details, "enable-macs-external-host")


# oci opsi host-insights update-host-insight-update-macs-managed-external-host-insight-details -> oci opsi host-insights update-macs-external-host
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.update_host_insight_update_macs_managed_external_host_insight_details, "update-macs-external-host")


# Remove create from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.create_database_insight.name)


# Remove update from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.update_database_insight.name)


# Remove enable from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.enable_database_insight.name)


# Remove create from oci opsi host-insights
operationsinsights_cli.host_insights_group.commands.pop(operationsinsights_cli.create_host_insight.name)


# Remove update from oci opsi host-insights
operationsinsights_cli.host_insights_group.commands.pop(operationsinsights_cli.update_database_insight.name)


# Remove enable from oci opsi host-insights
operationsinsights_cli.host_insights_group.commands.pop(operationsinsights_cli.enable_database_insight.name)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.create_database_insight_create_em_managed_external_database_insight_details, params_to_exclude=['enterprise_manager_bridge_id', 'enterprise_manager_entity_identifier', 'enterprise_manager_identifier'])
@operationsinsights_cli.database_insights_group.command(name=operationsinsights_cli.create_database_insight_create_em_managed_external_database_insight_details.name, help="""Create an Enterprise Mananger External Database Insight resource for a database in Operations Insights. The database will be enabled in Operations Insights. Database metric collection and analysis will be started.""")
@cli_util.option('--em-id', required=True, help="""Enterprise Manager Unqiue Identifier [required]""")
@cli_util.option('--em-entity-id', required=True, help="""Enterprise Manager Entity Unique Identifier [required]""")
@cli_util.option('--em-bridge-id', required=True, help=u"""OPSI Enterprise Manager Bridge OCID [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'operationsinsights', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operationsinsights', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'operationsinsights', 'class': 'DatabaseInsight'})
@cli_util.wrap_exceptions
def create_database_insight_create_em_managed_external_database_insight_details_extended(ctx, **kwargs):

    if 'em_id' in kwargs:
        kwargs['enterprise_manager_identifier'] = kwargs['em_id']
        kwargs.pop('em_id')

    if 'em_entity_id' in kwargs:
        kwargs['enterprise_manager_entity_identifier'] = kwargs['em_entity_id']
        kwargs.pop('em_entity_id')

    if 'em_bridge_id' in kwargs:
        kwargs['enterprise_manager_bridge_id'] = kwargs['em_bridge_id']
        kwargs.pop('em_bridge_id')

    ctx.invoke(operationsinsights_cli.create_database_insight_create_em_managed_external_database_insight_details, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.list_database_insights, params_to_exclude=['enterprise_manager_bridge_id'])
@operationsinsights_cli.database_insights_group.command(name=operationsinsights_cli.list_database_insights.name, help=operationsinsights_cli.list_database_insights.help)
@cli_util.option('--em-bridge-id', help=u"""Unique Enterprise Manager bridge identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'operationsinsights', 'class': 'list[string]'}, 'database-id': {'module': 'operationsinsights', 'class': 'list[string]'}}, output_type={'module': 'operationsinsights', 'class': 'DatabaseInsightsCollection'})
@cli_util.wrap_exceptions
def list_database_insights_extended(ctx, **kwargs):
    if 'em_bridge_id' in kwargs:
        kwargs['enterprise_manager_bridge_id'] = kwargs['em_bridge_id']
        kwargs.pop('em_bridge_id')

    ctx.invoke(operationsinsights_cli.list_database_insights, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.enable_database_insight_enable_em_managed_external_database_insight_details, params_to_exclude=[])
@operationsinsights_cli.database_insights_group.command(name=operationsinsights_cli.enable_database_insight_enable_em_managed_external_database_insight_details.name, help="""Enable an Enterprise Manager External Database in Operations Insights. Database metric collection and analysis will be started. All other enable calls must be made directly to DBaaS.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_database_insight_enable_em_managed_external_database_insight_details_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.enable_database_insight_enable_em_managed_external_database_insight_details, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.update_database_insight_update_autonomous_database_insight_details, params_to_exclude=[])
@operationsinsights_cli.database_insights_group.command(name=operationsinsights_cli.update_database_insight_update_autonomous_database_insight_details.name, help="""Update tags for an Autonomous Database Insight resource in Operations Insights.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'operationsinsights', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operationsinsights', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_database_insight_update_autonomous_database_insight_details_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.update_database_insight_update_autonomous_database_insight_details, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.update_database_insight_update_em_managed_external_database_insight_details, params_to_exclude=[])
@operationsinsights_cli.database_insights_group.command(name=operationsinsights_cli.update_database_insight_update_em_managed_external_database_insight_details.name, help="""Update tags for an Enterprise Manager External Database Insight resource in Operations Insights.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'operationsinsights', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operationsinsights', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_database_insight_update_em_managed_external_database_insight_details_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.update_database_insight_update_em_managed_external_database_insight_details, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.update_database_insight_update_macs_managed_external_database_insight_details, params_to_exclude=[])
@operationsinsights_cli.database_insights_group.command(name=operationsinsights_cli.update_database_insight_update_macs_managed_external_database_insight_details.name, help="""Update tags for a MACS Agent Managed External Database Insight resource in Operations Insights.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'operationsinsights', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operationsinsights', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_database_insight_update_macs_managed_external_database_insight_details_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.update_database_insight_update_macs_managed_external_database_insight_details, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.create_host_insight_create_macs_managed_external_host_insight_details, params_to_exclude=[])
@operationsinsights_cli.host_insights_group.command(name=operationsinsights_cli.create_host_insight_create_macs_managed_external_host_insight_details.name, help="""Create an MACS Managed External Host Insight resource for a host in Operations Insights. The host will be enabled in Operations Insights. Host metric collection and analysis will be started.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'operationsinsights', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operationsinsights', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'operationsinsights', 'class': 'HostInsight'})
@cli_util.wrap_exceptions
def create_host_insight_create_macs_managed_external_host_insight_details_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.create_host_insight_create_macs_managed_external_host_insight_details, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.enable_host_insight_enable_macs_managed_external_host_insight_details, params_to_exclude=[])
@operationsinsights_cli.host_insights_group.command(name=operationsinsights_cli.enable_host_insight_enable_macs_managed_external_host_insight_details.name, help="""Enable a MACS Managed External Host in Operations Insights. Host metric collection and analysis will be started.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_host_insight_enable_macs_managed_external_host_insight_details_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.enable_host_insight_enable_macs_managed_external_host_insight_details, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.update_host_insight_update_macs_managed_external_host_insight_details, params_to_exclude=[])
@operationsinsights_cli.host_insights_group.command(name=operationsinsights_cli.update_host_insight_update_macs_managed_external_host_insight_details.name, help="""Update tags for a MACS Managed External Host Insight resource in Operations Insights.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'operationsinsights', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operationsinsights', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_host_insight_update_macs_managed_external_host_insight_details_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.update_host_insight_update_macs_managed_external_host_insight_details, **kwargs)
