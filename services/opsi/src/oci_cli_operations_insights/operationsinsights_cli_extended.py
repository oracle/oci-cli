# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
import os
import os.path
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


# oci opsi exadata-insights add-exadata-insight-members-add-em-managed-external-exadata-insight-members-details -> oci opsi exadata-insights add-em-external-exadata-members
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.exadata_insights_group, operationsinsights_cli.add_exadata_insight_members_add_em_managed_external_exadata_insight_members_details, "add-em-external-exadata-members")


# oci opsi exadata-insights create-exadata-insight-create-em-managed-external-exadata-insight-details -> oci opsi exadata-insights create-em-external-exadata
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.exadata_insights_group, operationsinsights_cli.create_exadata_insight_create_em_managed_external_exadata_insight_details, "create-em-external-exadata")


# oci opsi exadata-insights enable-exadata-insight-enable-em-managed-external-exadata-insight-details -> oci opsi exadata-insights enable-em-external-exadata
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.exadata_insights_group, operationsinsights_cli.enable_exadata_insight_enable_em_managed_external_exadata_insight_details, "enable-em-external-exadata")


# oci opsi exadata-insights update-exadata-insight-update-em-managed-external-exadata-insight-details -> oci opsi exadata-insights update-em-external-exadata
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.exadata_insights_group, operationsinsights_cli.update_exadata_insight_update_em_managed_external_exadata_insight_details, "update-em-external-exadata")


# oci opsi host-insights create-host-insight-create-em-managed-external-host-insight-details -> oci opsi host-insights create-em-external-host
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.create_host_insight_create_em_managed_external_host_insight_details, "create-em-external-host")


# oci opsi host-insights create-host-insight-create-macs-managed-external-host-insight-details -> oci opsi host-insights create-macs-external-host
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.create_host_insight_create_macs_managed_external_host_insight_details, "create-macs-external-host")


# oci opsi host-insights enable-host-insight-enable-em-managed-external-host-insight-details -> oci opsi host-insights enable-em-external-host
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.enable_host_insight_enable_em_managed_external_host_insight_details, "enable-em-external-host")


# oci opsi host-insights enable-host-insight-enable-macs-managed-external-host-insight-details -> oci opsi host-insights enable-macs-external-host
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.enable_host_insight_enable_macs_managed_external_host_insight_details, "enable-macs-external-host")


# oci opsi host-insights update-host-insight-update-em-managed-external-host-insight-details -> oci opsi host-insights update-em-external-host
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.update_host_insight_update_em_managed_external_host_insight_details, "update-em-external-host")


# oci opsi host-insights update-host-insight-update-macs-managed-external-host-insight-details -> oci opsi host-insights update-macs-external-host
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.update_host_insight_update_macs_managed_external_host_insight_details, "update-macs-external-host")


# Remove create from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.create_database_insight.name)


# Remove update from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.update_database_insight.name)


# Remove enable from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.enable_database_insight.name)


# Remove add from oci opsi exadata-insights
operationsinsights_cli.exadata_insights_group.commands.pop(operationsinsights_cli.add_exadata_insight_members.name)


# Remove create from oci opsi exadata-insights
operationsinsights_cli.exadata_insights_group.commands.pop(operationsinsights_cli.create_exadata_insight.name)


# Remove enable from oci opsi exadata-insights
operationsinsights_cli.exadata_insights_group.commands.pop(operationsinsights_cli.enable_exadata_insight.name)


# Remove update from oci opsi exadata-insights
operationsinsights_cli.exadata_insights_group.commands.pop(operationsinsights_cli.update_exadata_insight.name)


# Remove create from oci opsi host-insights
operationsinsights_cli.host_insights_group.commands.pop(operationsinsights_cli.create_host_insight.name)


# Remove update from oci opsi host-insights
operationsinsights_cli.host_insights_group.commands.pop(operationsinsights_cli.update_host_insight.name)


# Remove enable from oci opsi host-insights
operationsinsights_cli.host_insights_group.commands.pop(operationsinsights_cli.enable_host_insight.name)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.list_database_configurations, params_to_exclude=['enterprise_manager_bridge_id'])
@operationsinsights_cli.database_insights_group.command(name=operationsinsights_cli.list_database_configurations.name, help=operationsinsights_cli.list_database_configurations.help)
@cli_util.option('--em-bridge-id', help=u"""OPSI Enterprise Manager Bridge OCID""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'vmcluster-name': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'DatabaseConfigurationCollection'})
@cli_util.wrap_exceptions
def list_database_configurations_extended(ctx, **kwargs):
    if 'em_bridge_id' in kwargs:
        kwargs['enterprise_manager_bridge_id'] = kwargs['em_bridge_id']
        kwargs.pop('em_bridge_id')

    ctx.invoke(operationsinsights_cli.list_database_configurations, **kwargs)


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
@cli_util.option('--em-bridge-id', help=u"""OPSI Enterprise Manager Bridge OCID""")
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


@cli_util.copy_params_from_generated_command(operationsinsights_cli.create_exadata_insight_create_em_managed_external_exadata_insight_details, params_to_exclude=['enterprise_manager_bridge_id', 'enterprise_manager_entity_identifier', 'enterprise_manager_identifier'])
@operationsinsights_cli.exadata_insights_group.command(name=operationsinsights_cli.create_exadata_insight_create_em_managed_external_exadata_insight_details.name, help="""Create an External EM Exadata insight resource for an Exadata system in Operations Insights. The Exadata system will be enabled in Operations Insights. Exadata-related metric collection and analysis will be started.""")
@cli_util.option('--em-id', required=True, help="""Enterprise Manager Unqiue Identifier [required]""")
@cli_util.option('--em-entity-id', required=True, help="""Enterprise Manager Entity Unique Identifier [required]""")
@cli_util.option('--em-bridge-id', required=True, help=u"""OPSI Enterprise Manager Bridge OCID [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'operationsinsights', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operationsinsights', 'class': 'dict(str, dict(str, object))'}, 'member-entity-details': {'module': 'operationsinsights', 'class': 'list[CreateEmManagedExternalExadataMemberEntityDetails]'}}, output_type={'module': 'operationsinsights', 'class': 'ExadataInsight'})
@cli_util.wrap_exceptions
def create_exadata_insight_create_em_managed_external_exadata_insight_details_extended(ctx, **kwargs):

    if 'em_id' in kwargs:
        kwargs['enterprise_manager_identifier'] = kwargs['em_id']
        kwargs.pop('em_id')

    if 'em_entity_id' in kwargs:
        kwargs['enterprise_manager_entity_identifier'] = kwargs['em_entity_id']
        kwargs.pop('em_entity_id')

    if 'em_bridge_id' in kwargs:
        kwargs['enterprise_manager_bridge_id'] = kwargs['em_bridge_id']
        kwargs.pop('em_bridge_id')

    ctx.invoke(operationsinsights_cli.create_exadata_insight_create_em_managed_external_exadata_insight_details, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.list_exadata_insights, params_to_exclude=['enterprise_manager_bridge_id'])
@operationsinsights_cli.exadata_insights_group.command(name=operationsinsights_cli.list_exadata_insights.name, help=operationsinsights_cli.list_exadata_insights.help)
@cli_util.option('--em-bridge-id', help=u"""OPSI Enterprise Manager Bridge OCID""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'operationsinsights', 'class': 'list[string]'}, 'exadata-type': {'module': 'operationsinsights', 'class': 'list[string]'}}, output_type={'module': 'operationsinsights', 'class': 'ExadataInsightSummaryCollection'})
@cli_util.wrap_exceptions
def list_exadata_insights_extended(ctx, **kwargs):
    if 'em_bridge_id' in kwargs:
        kwargs['enterprise_manager_bridge_id'] = kwargs['em_bridge_id']
        kwargs.pop('em_bridge_id')

    ctx.invoke(operationsinsights_cli.list_exadata_insights, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.create_host_insight_create_em_managed_external_host_insight_details, params_to_exclude=['enterprise_manager_bridge_id', 'enterprise_manager_entity_identifier', 'enterprise_manager_identifier'])
@operationsinsights_cli.host_insights_group.command(name=operationsinsights_cli.create_host_insight_create_em_managed_external_host_insight_details.name, help="""Create an Enterprise Mananger External Host Insight resource for a host in Operations Insights. The host will be enabled in Operations Insights. Host metric collection and analysis will be started.""")
@cli_util.option('--em-id', required=True, help="""Enterprise Manager Unqiue Identifier [required]""")
@cli_util.option('--em-entity-id', required=True, help="""Enterprise Manager Entity Unique Identifier [required]""")
@cli_util.option('--em-bridge-id', required=True, help=u"""OPSI Enterprise Manager Bridge OCID [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'operationsinsights', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operationsinsights', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'operationsinsights', 'class': 'HostInsight'})
@cli_util.wrap_exceptions
def create_host_insight_create_em_managed_external_host_insight_details_extended(ctx, **kwargs):

    if 'em_id' in kwargs:
        kwargs['enterprise_manager_identifier'] = kwargs['em_id']
        kwargs.pop('em_id')

    if 'em_entity_id' in kwargs:
        kwargs['enterprise_manager_entity_identifier'] = kwargs['em_entity_id']
        kwargs.pop('em_entity_id')

    if 'em_bridge_id' in kwargs:
        kwargs['enterprise_manager_bridge_id'] = kwargs['em_bridge_id']
        kwargs.pop('em_bridge_id')

    ctx.invoke(operationsinsights_cli.create_host_insight_create_em_managed_external_host_insight_details, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.create_host_insight_create_macs_managed_external_host_insight_details, params_to_exclude=[])
@operationsinsights_cli.host_insights_group.command(name=operationsinsights_cli.create_host_insight_create_macs_managed_external_host_insight_details.name, help="""Create an MACS Managed External Host Insight resource for a host in Operations Insights. The host will be enabled in Operations Insights. Host metric collection and analysis will be started.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'operationsinsights', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operationsinsights', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'operationsinsights', 'class': 'HostInsight'})
@cli_util.wrap_exceptions
def create_host_insight_create_macs_managed_external_host_insight_details_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.create_host_insight_create_macs_managed_external_host_insight_details, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.enable_host_insight_enable_em_managed_external_host_insight_details, params_to_exclude=[])
@operationsinsights_cli.host_insights_group.command(name=operationsinsights_cli.enable_host_insight_enable_em_managed_external_host_insight_details.name, help="""Enable an Enterprise Manager External Host in Operations Insights. Host metric collection and analysis will be started.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_host_insight_enable_em_managed_external_host_insight_details_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.enable_host_insight_enable_em_managed_external_host_insight_details, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.enable_host_insight_enable_macs_managed_external_host_insight_details, params_to_exclude=[])
@operationsinsights_cli.host_insights_group.command(name=operationsinsights_cli.enable_host_insight_enable_macs_managed_external_host_insight_details.name, help="""Enable a MACS Managed External Host in Operations Insights. Host metric collection and analysis will be started.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_host_insight_enable_macs_managed_external_host_insight_details_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.enable_host_insight_enable_macs_managed_external_host_insight_details, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.list_host_insights, params_to_exclude=['enterprise_manager_bridge_id'])
@operationsinsights_cli.host_insights_group.command(name=operationsinsights_cli.list_host_insights.name, help=operationsinsights_cli.list_host_insights.help)
@cli_util.option('--em-bridge-id', help=u"""OPSI Enterprise Manager Bridge OCID""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'operationsinsights', 'class': 'list[string]'}, 'host-type': {'module': 'operationsinsights', 'class': 'list[string]'}}, output_type={'module': 'operationsinsights', 'class': 'HostInsightSummaryCollection'})
@cli_util.wrap_exceptions
def list_host_insights_extended(ctx, **kwargs):
    if 'em_bridge_id' in kwargs:
        kwargs['enterprise_manager_bridge_id'] = kwargs['em_bridge_id']
        kwargs.pop('em_bridge_id')

    ctx.invoke(operationsinsights_cli.list_host_insights, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.update_host_insight_update_em_managed_external_host_insight_details, params_to_exclude=[])
@operationsinsights_cli.host_insights_group.command(name=operationsinsights_cli.update_host_insight_update_em_managed_external_host_insight_details.name, help="""Update tags for an EM Managed External Host Insight resource in Operations Insights.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'operationsinsights', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operationsinsights', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_host_insight_update_em_managed_external_host_insight_details_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.update_host_insight_update_em_managed_external_host_insight_details, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.update_host_insight_update_macs_managed_external_host_insight_details, params_to_exclude=[])
@operationsinsights_cli.host_insights_group.command(name=operationsinsights_cli.update_host_insight_update_macs_managed_external_host_insight_details.name, help="""Update tags for a MACS Managed External Host Insight resource in Operations Insights.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'operationsinsights', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operationsinsights', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_host_insight_update_macs_managed_external_host_insight_details_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.update_host_insight_update_macs_managed_external_host_insight_details, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.list_importable_enterprise_manager_entities, params_to_exclude=['enterprise_manager_entity_type', 'enterprise_manager_identifier', 'enterprise_manager_parent_entity_identifier'])
@operationsinsights_cli.enterprise_manager_bridges_group.command(name=operationsinsights_cli.list_importable_enterprise_manager_entities.name, help=operationsinsights_cli.list_importable_enterprise_manager_entities.help)
@cli_util.option('--em-entity-type', help=u"""Filter by one or more Enterprise Manager entity types. Currently, the supported types are "oracle_pdb", "oracle_database", "host", "oracle_dbmachine", "oracle_exa_cloud_service", and "oracle_oci_exadata_cloud_service". If this parameter is not specified, targets of all supported entity types are returned by default.""")
@cli_util.option('--em-id', help=u"""The unique Enterprise Manager identifier. Used in combination with emParentId to return the members of a particular Enterprise Manager parent entity. Both emId and emParentId must be specified to identify a particular Enterprise Manager parent entity.""")
@cli_util.option('--em-parent-id', help=u"""The unique Enterprise Manager Entity identifier of the parent EM entity (the Exadata for instance). Used in combination with emId parameter to return the members of a particular Enterprise Manager parent entity. Both emId and emParentId must be specified to identify a particular Enterprise Manager parent entity.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'enterprise-manager-entity-type': {'module': 'operationsinsights', 'class': 'list[string]'}}, output_type={'module': 'operationsinsights', 'class': 'ImportableEnterpriseManagerEntityCollection'})
@cli_util.wrap_exceptions
def list_importable_enterprise_manager_entities_extended(ctx, **kwargs):
    if 'em_entity_type' in kwargs:
        kwargs['enterprise_manager_entity_type'] = kwargs['em_entity_type']
        kwargs.pop('em_entity_type')

    if 'em_id' in kwargs:
        kwargs['enterprise_manager_identifier'] = kwargs['em_id']
        kwargs.pop('em_id')

    if 'em_parent_id' in kwargs:
        kwargs['enterprise_manager_parent_entity_identifier'] = kwargs['em_parent_id']
        kwargs.pop('em_parent_id')

    ctx.invoke(operationsinsights_cli.list_importable_enterprise_manager_entities, **kwargs)


# oci opsi operations-insights-warehouses download -> oci opsi operations-insights-warehouses download-warehouse-wallet
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.operations_insights_warehouses_group, operationsinsights_cli.download_operations_insights_warehouse_wallet, "download-warehouse-wallet")


# oci opsi operations-insights-warehouses rotate -> oci opsi operations-insights-warehouses rotate-warehouse-wallet
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.operations_insights_warehouses_group, operationsinsights_cli.rotate_operations_insights_warehouse_wallet, "rotate-warehouse-wallet")


@cli_util.copy_params_from_generated_command(operationsinsights_cli.list_host_configurations, params_to_exclude=['enterprise_manager_bridge_id'])
@operationsinsights_cli.host_insights_group.command(name=operationsinsights_cli.list_host_configurations.name, help=operationsinsights_cli.list_host_configurations.help)
@cli_util.option('--em-bridge-id', help=u"""Unique Enterprise Manager bridge identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'host-type': {'module': 'opsi', 'class': 'list[string]'}, 'vmcluster-name': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'HostConfigurationCollection'})
@cli_util.wrap_exceptions
def list_host_configurations_extended(ctx, **kwargs):
    if 'em_bridge_id' in kwargs:
        kwargs['enterprise_manager_bridge_id'] = kwargs['em_bridge_id']
        kwargs.pop('em_bridge_id')

    ctx.invoke(operationsinsights_cli.list_host_configurations, **kwargs)


# oci opsi operations-insights-private-endpoint -> oci opsi opsi-private-endpoint
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.opsi_root_group, operationsinsights_cli.operations_insights_private_endpoint_group, "opsi-private-endpoint")


# oci opsi host-insights summarize-host-insight-io-usage-trend -> oci opsi host-insights summarize-io-usage-trend
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.summarize_host_insight_io_usage_trend, "summarize-io-usage-trend")


# oci opsi database-insights create-database-insight-create-pe-comanaged-database-insight-details -> oci opsi database-insights create-pe-comanged-database
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.create_database_insight_create_pe_comanaged_database_insight_details, "create-pe-comanged-database")


# oci opsi database-insights enable-database-insight-enable-pe-comanaged-database-insight-details -> oci opsi database-insights enable-pe-comanaged-database
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.enable_database_insight_enable_pe_comanaged_database_insight_details, "enable-pe-comanaged-database")


# oci opsi database-insights update-database-insight-update-pe-comanaged-database-insight-details -> oci opsi database-insights update-pe-comanaged-database
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.update_database_insight_update_pe_comanaged_database_insight_details, "update-pe-comanaged-database")


# oci opsi database-insights change-pe-comanaged-database-insight-credential-by-vault -> oci opsi database-insights change-pe-comanaged-database-detail
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.change_pe_comanaged_database_insight_credential_by_vault, "change-pe-comanaged-database-detail")


# Remove change-pe-comanaged from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.change_pe_comanaged_database_insight.name)


# Remove change-pe-comanaged-database-insight-credentials-by-source from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.change_pe_comanaged_database_insight_credentials_by_source.name)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.change_operations_insights_private_endpoint_compartment, params_to_exclude=['operations_insights_private_endpoint_id'])
@operationsinsights_cli.operations_insights_private_endpoint_group.command(name=operationsinsights_cli.change_operations_insights_private_endpoint_compartment.name, help=operationsinsights_cli.change_operations_insights_private_endpoint_compartment.help)
@cli_util.option('--opsi-private-endpoint-id', required=True, help=u"""The [OCID] of the Operation Insights private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_operations_insights_private_endpoint_compartment_extended(ctx, **kwargs):
    if 'opsi_private_endpoint_id' in kwargs:
        kwargs['operations_insights_private_endpoint_id'] = kwargs['opsi_private_endpoint_id']
        kwargs.pop('opsi_private_endpoint_id')

    ctx.invoke(operationsinsights_cli.change_operations_insights_private_endpoint_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.delete_operations_insights_private_endpoint, params_to_exclude=['operations_insights_private_endpoint_id'])
@operationsinsights_cli.operations_insights_private_endpoint_group.command(name=operationsinsights_cli.delete_operations_insights_private_endpoint.name, help=operationsinsights_cli.delete_operations_insights_private_endpoint.help)
@cli_util.option('--opsi-private-endpoint-id', required=True, help=u"""The [OCID] of the Operation Insights private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_operations_insights_private_endpoint_extended(ctx, **kwargs):
    if 'opsi_private_endpoint_id' in kwargs:
        kwargs['operations_insights_private_endpoint_id'] = kwargs['opsi_private_endpoint_id']
        kwargs.pop('opsi_private_endpoint_id')

    ctx.invoke(operationsinsights_cli.delete_operations_insights_private_endpoint, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.get_operations_insights_private_endpoint, params_to_exclude=['operations_insights_private_endpoint_id'])
@operationsinsights_cli.operations_insights_private_endpoint_group.command(name=operationsinsights_cli.get_operations_insights_private_endpoint.name, help=operationsinsights_cli.get_operations_insights_private_endpoint.help)
@cli_util.option('--opsi-private-endpoint-id', required=True, help=u"""The [OCID] of the Operation Insights private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'operationsinsights', 'class': 'OperationsInsightsPrivateEndpoint'})
@cli_util.wrap_exceptions
def get_operations_insights_private_endpoint_extended(ctx, **kwargs):
    if 'opsi_private_endpoint_id' in kwargs:
        kwargs['operations_insights_private_endpoint_id'] = kwargs['opsi_private_endpoint_id']
        kwargs.pop('opsi_private_endpoint_id')

    ctx.invoke(operationsinsights_cli.get_operations_insights_private_endpoint, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.update_operations_insights_private_endpoint, params_to_exclude=['operations_insights_private_endpoint_id'])
@operationsinsights_cli.operations_insights_private_endpoint_group.command(name=operationsinsights_cli.update_operations_insights_private_endpoint.name, help=operationsinsights_cli.update_operations_insights_private_endpoint.help)
@cli_util.option('--opsi-private-endpoint-id', required=True, help=u"""The [OCID] of the Operation Insights private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'operationsinsights', 'class': 'list[string]'}, 'freeform-tags': {'module': 'operationsinsights', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operationsinsights', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_operations_insights_private_endpoint_extended(ctx, **kwargs):
    if 'opsi_private_endpoint_id' in kwargs:
        kwargs['operations_insights_private_endpoint_id'] = kwargs['opsi_private_endpoint_id']
        kwargs.pop('opsi_private_endpoint_id')

    ctx.invoke(operationsinsights_cli.update_operations_insights_private_endpoint, **kwargs)


# oci opsi host-insights summarize-host-insight-top-processes-usage-trend -> oci opsi host-insights summarize-top-processes-usage-trend
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.summarize_host_insight_top_processes_usage_trend, "summarize-top-processes-usage-trend")

# oci opsi opsi-data-objects query-opsi-data-object-data-data-object-templatized-query -> oci opsi opsi-data-objects query-data-templatized-query
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.opsi_data_objects_group, operationsinsights_cli.query_opsi_data_object_data_data_object_templatized_query, "query-data-templatized-query")

# Remove query from oci opsi opsi-data-objects
operationsinsights_cli.opsi_data_objects_group.commands.pop(operationsinsights_cli.query_opsi_data_object_data.name)

# oci opsi host-insights create-host-insight-create-macs-managed-cloud-host-insight-details -> oci opsi host-insights create-macs-cloud-host
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.create_host_insight_create_macs_managed_cloud_host_insight_details, "create-macs-cloud-host")


# oci opsi host-insights enable-host-insight-enable-macs-managed-cloud-host-insight-details -> oci opsi host-insights enable-macs-cloud-host
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.enable_host_insight_enable_macs_managed_cloud_host_insight_details, "enable-macs-cloud-host")


# oci opsi host-insights update-host-insight-update-macs-managed-cloud-host-insight-details -> oci opsi host-insights update-macs-cloud-host
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.update_host_insight_update_macs_managed_cloud_host_insight_details, "update-macs-cloud-host")


# oci opsi host-insights list-importable-compute-entities -> oci opsi host-insights list-macs-cloud-hosts
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.list_importable_compute_entities, "list-macs-cloud-hosts")


# oci opsi exadata-insights add-exadata-insight-members-add-pe-comanaged-exadata-insight-members-details -> oci opsi exadata-insights add-pe-comanaged-exadata-members
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.exadata_insights_group, operationsinsights_cli.add_exadata_insight_members_add_pe_comanaged_exadata_insight_members_details, "add-pe-comanaged-exadata-members")


# oci opsi exadata-insights create-exadata-insight-create-pe-comanaged-exadata-insight-details -> oci opsi exadata-insights create-pe-comanaged-exadata
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.exadata_insights_group, operationsinsights_cli.create_exadata_insight_create_pe_comanaged_exadata_insight_details, "create-pe-comanaged-exadata")


# oci opsi exadata-insights enable-exadata-insight-enable-pe-comanaged-exadata-insight-details -> oci opsi exadata-insights enable-pe-comanaged-exadata
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.exadata_insights_group, operationsinsights_cli.enable_exadata_insight_enable_pe_comanaged_exadata_insight_details, "enable-pe-comanaged-exadata")


# oci opsi exadata-insights update-exadata-insight-update-pe-comanaged-exadata-insight-details -> oci opsi exadata-insights update-pe-comanaged-exadata
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.exadata_insights_group, operationsinsights_cli.update_exadata_insight_update_pe_comanaged_exadata_insight_details, "update-pe-comanaged-exadata")


# oci opsi opsi-configurations create-opsi-configuration-create-opsi-ux-configuration-details -> oci opsi opsi-configurations create-opsi-ux-configuration-details
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.opsi_configurations_group, operationsinsights_cli.create_opsi_configuration_create_opsi_ux_configuration_details, "create-opsi-ux-configuration-details")


# oci opsi opsi-configurations update-opsi-configuration-update-opsi-ux-configuration-details -> oci opsi opsi-configurations update-opsi-ux-configuration-details
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.opsi_configurations_group, operationsinsights_cli.update_opsi_configuration_update_opsi_ux_configuration_details, "update-opsi-ux-configuration-details")


# Remove create from oci opsi opsi-configurations
operationsinsights_cli.opsi_configurations_group.commands.pop(operationsinsights_cli.create_opsi_configuration.name)


# Remove update from oci opsi opsi-configurations
operationsinsights_cli.opsi_configurations_group.commands.pop(operationsinsights_cli.update_opsi_configuration.name)


# oci opsi host-insights summarize-host-insight-network-usage-trend -> oci opsi host-insights summarize-network-usage-trend
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.summarize_host_insight_network_usage_trend, "summarize-network-usage-trend")


# oci opsi host-insights summarize-host-insight-storage-usage-trend -> oci opsi host-insights summarize-storage-usage-trend
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.summarize_host_insight_storage_usage_trend, "summarize-storage-usage-trend")


# oci opsi host-insights summarize-host-insight-disk-statistics -> oci opsi host-insights summarize-disk-statistics
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.summarize_host_insight_disk_statistics, "summarize-disk-statistics")


# oci opsi host-insights summarize-host-insight-host-recommendation -> oci opsi host-insights summarize-host-recommendation
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.summarize_host_insight_host_recommendation, "summarize-host-recommendation")

# Remove change-autonomous-database-insight-advanced-features from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.change_autonomous_database_insight_advanced_features.name)


# Remove change-autonomous-database-insight-advanced-features-credentials-by-source from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.change_autonomous_database_insight_advanced_features_credentials_by_source.name)


# Remove enable-autonomous-database-insight-advanced-features from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.enable_autonomous_database_insight_advanced_features.name)


# Remove enable-autonomous-database-insight-advanced-features-credentials-by-source from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.enable_autonomous_database_insight_advanced_features_credentials_by_source.name)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.change_autonomous_database_insight_advanced_features_credential_by_vault, params_to_exclude=['credential_details_credential_source_name', 'credential_details_password_secret_id', 'credential_details_role', 'credential_details_user_name'])
@operationsinsights_cli.database_insights_group.command(name=operationsinsights_cli.change_autonomous_database_insight_advanced_features_credential_by_vault.name, help=operationsinsights_cli.change_autonomous_database_insight_advanced_features_credential_by_vault.help)
@cli_util.option('--password-secret-id', help=u"""The secret [OCID] mapping to the database credentials.""")
@cli_util.option('--role', type=custom_types.CliCaseInsensitiveChoice(["NORMAL"]), help=u"""database user role.""")
@cli_util.option('--user-name', help=u"""database user name.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection-details': {'module': 'operationsinsights', 'class': 'ConnectionDetails'}})
@cli_util.wrap_exceptions
def change_autonomous_database_insight_advanced_features_credential_by_vault_extended(ctx, **kwargs):
    if 'password_secret_id' in kwargs:
        kwargs['credential_details_password_secret_id'] = kwargs['password_secret_id']
        kwargs.pop('password_secret_id')

    if 'role' in kwargs:
        kwargs['credential_details_role'] = kwargs['role']
        kwargs.pop('role')

    if 'user_name' in kwargs:
        kwargs['credential_details_user_name'] = kwargs['user_name']
        kwargs.pop('user_name')

    ctx.invoke(operationsinsights_cli.change_autonomous_database_insight_advanced_features_credential_by_vault, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.enable_autonomous_database_insight_advanced_features_credential_by_vault, params_to_exclude=['credential_details_credential_source_name', 'credential_details_password_secret_id', 'credential_details_role', 'credential_details_user_name'])
@operationsinsights_cli.database_insights_group.command(name=operationsinsights_cli.enable_autonomous_database_insight_advanced_features_credential_by_vault.name, help=operationsinsights_cli.enable_autonomous_database_insight_advanced_features_credential_by_vault.help)
@cli_util.option('--password-secret-id', help=u"""The secret [OCID] mapping to the database credentials.""")
@cli_util.option('--role', type=custom_types.CliCaseInsensitiveChoice(["NORMAL"]), help=u"""database user role.""")
@cli_util.option('--user-name', help=u"""database user name.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection-details': {'module': 'operationsinsights', 'class': 'ConnectionDetails'}})
@cli_util.wrap_exceptions
def enable_autonomous_database_insight_advanced_features_credential_by_vault_extended(ctx, **kwargs):
    if 'password_secret_id' in kwargs:
        kwargs['credential_details_password_secret_id'] = kwargs['password_secret_id']
        kwargs.pop('password_secret_id')

    if 'role' in kwargs:
        kwargs['credential_details_role'] = kwargs['role']
        kwargs.pop('role')

    if 'user_name' in kwargs:
        kwargs['credential_details_user_name'] = kwargs['user_name']
        kwargs.pop('user_name')

    ctx.invoke(operationsinsights_cli.enable_autonomous_database_insight_advanced_features_credential_by_vault, **kwargs)


# oci opsi opsi-data-objects query-opsi-data-object-data-data-object-standard-query -> oci opsi opsi-data-objects query-data-standard-query
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.opsi_data_objects_group, operationsinsights_cli.query_opsi_data_object_data_data_object_standard_query, "query-data-standard-query")


# oci opsi opsi-warehouse-data-objects list-warehouse-data-objects -> oci opsi opsi-warehouse-data-objects list
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.opsi_warehouse_data_objects_group, operationsinsights_cli.list_warehouse_data_objects, "list")


# oci opsi opsi-warehouse-data-objects query-warehouse-data-object-data-data-object-standard-query -> oci opsi opsi-warehouse-data-objects query-warehouse-data-standard-query
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.opsi_warehouse_data_objects_group, operationsinsights_cli.query_warehouse_data_object_data_data_object_standard_query, "query-warehouse-data-standard-query")


# oci opsi opsi-warehouse-data-objects query-warehouse-data-object-data-data-object-templatized-query -> oci opsi opsi-warehouse-data-objects query-warehouse-data-templatized-query
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.opsi_warehouse_data_objects_group, operationsinsights_cli.query_warehouse_data_object_data_data_object_templatized_query, "query-warehouse-data-templatized-query")


# Remove query-warehouse-data-object-data from oci opsi opsi-warehouse-data-objects
operationsinsights_cli.opsi_warehouse_data_objects_group.commands.pop(operationsinsights_cli.query_warehouse_data_object_data.name)


# Fixing auto generated tests by python cli, which was prefixing parameterconflict in many parameters
@cli_util.copy_params_from_generated_command(operationsinsights_cli.query_opsi_data_object_data_data_object_templatized_query)
@operationsinsights_cli.opsi_data_objects_group.command(name=cli_util.override('opsi.query_opsi_data_object_data_data_object_templatized_query.command_name', 'query-opsi-data-object-data-data-object-templatized-query'), help=u"""Queries an OPSI data object with the inputs provided and sends the result set back. Either analysisTimeInterval or timeIntervalStart and timeIntervalEnd parameters need to be passed as well. \n[Command Reference](queryOpsiDataObjectData)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'query-bind-params': {'module': 'operationsinsights', 'class': 'list[DataObjectBindParameter]'}, 'query-select-list': {'module': 'operationsinsights', 'class': 'list[string]'}, 'query-where-conditions-list': {'module': 'operationsinsights', 'class': 'list[string]'}, 'query-group-by-list': {'module': 'operationsinsights', 'class': 'list[string]'}, 'query-having-conditions-list': {'module': 'operationsinsights', 'class': 'list[string]'}, 'query-order-by-list': {'module': 'operationsinsights', 'class': 'list[string]'}, 'resource-filters': {'module': 'operationsinsights', 'class': 'ResourceFilters'}, 'data-objects': {'module': 'operationsinsights', 'class': 'list[OpsiDataObjectDetailsInQuery]'}, 'query-time-filters': {'module': 'operationsinsights', 'class': 'DataObjectQueryTimeFilters'}}, output_type={'module': 'operationsinsights', 'class': 'QueryDataObjectResultSetRowsCollection'})
@cli_util.wrap_exceptions
def query_opsi_data_object_data_data_object_templatized_query_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.query_opsi_data_object_data_data_object_templatized_query, **kwargs)


# Fixing auto generated tests by python cli, which was prefixing parameterconflict in many parameters
@cli_util.copy_params_from_generated_command(operationsinsights_cli.query_opsi_data_object_data_data_object_standard_query)
@operationsinsights_cli.opsi_data_objects_group.command(name=cli_util.override('opsi.query_opsi_data_object_data_data_object_standard_query.command_name', 'query-opsi-data-object-data-data-object-standard-query'), help=u"""Queries an OPSI data object with the inputs provided and sends the result set back. Either analysisTimeInterval or timeIntervalStart and timeIntervalEnd parameters need to be passed as well. \n[Command Reference](queryOpsiDataObjectData)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'query-bind-params': {'module': 'operationsinsights', 'class': 'list[DataObjectBindParameter]'}, 'resource-filters': {'module': 'operationsinsights', 'class': 'ResourceFilters'}, 'data-objects': {'module': 'operationsinsights', 'class': 'list[OpsiDataObjectDetailsInQuery]'}, 'query-time-filters': {'module': 'operationsinsights', 'class': 'DataObjectQueryTimeFilters'}}, output_type={'module': 'operationsinsights', 'class': 'QueryDataObjectResultSetRowsCollection'})
@cli_util.wrap_exceptions
def query_opsi_data_object_data_data_object_standard_query_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.query_opsi_data_object_data_data_object_standard_query, **kwargs)


# Fixing auto generated tests by python cli, which was prefixing parameterconflict in many parameters
@cli_util.copy_params_from_generated_command(operationsinsights_cli.query_warehouse_data_object_data_data_object_templatized_query)
@operationsinsights_cli.opsi_warehouse_data_objects_group.command(name=cli_util.override('opsi.query_warehouse_data_object_data_data_object_templatized_query.command_name', 'query-warehouse-data-object-data-data-object-templatized-query'), help=u"""Queries Warehouse data objects (e.g: views, tables) with the inputs provided and sends the result set back. Any data to which an OperationsInsightsWarehouseUser with a permission to the corresponding Warehouse can be queried. \n[Command Reference](queryWarehouseDataObjectData)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'query-bind-params': {'module': 'operationsinsights', 'class': 'list[DataObjectBindParameter]'}, 'query-select-list': {'module': 'operationsinsights', 'class': 'list[string]'}, 'query-where-conditions-list': {'module': 'operationsinsights', 'class': 'list[string]'}, 'query-group-by-list': {'module': 'operationsinsights', 'class': 'list[string]'}, 'query-having-conditions-list': {'module': 'operationsinsights', 'class': 'list[string]'}, 'query-order-by-list': {'module': 'operationsinsights', 'class': 'list[string]'}, 'query-time-filters': {'module': 'operationsinsights', 'class': 'DataObjectQueryTimeFilters'}}, output_type={'module': 'operationsinsights', 'class': 'QueryDataObjectResultSetRowsCollection'})
@cli_util.wrap_exceptions
def query_warehouse_data_object_data_data_object_templatized_query_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.query_warehouse_data_object_data_data_object_templatized_query, **kwargs)


# Fixing auto generated tests by python cli, which was prefixing parameterconflict in many parameters
@cli_util.copy_params_from_generated_command(operationsinsights_cli.query_warehouse_data_object_data_data_object_standard_query)
@operationsinsights_cli.opsi_warehouse_data_objects_group.command(name=cli_util.override('opsi.query_warehouse_data_object_data_data_object_standard_query.command_name', 'query-warehouse-data-object-data-data-object-standard-query'), help=u"""Queries Warehouse data objects (e.g: views, tables) with the inputs provided and sends the result set back. Any data to which an OperationsInsightsWarehouseUser with a permission to the corresponding Warehouse can be queried. \n[Command Reference](queryWarehouseDataObjectData)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'query-bind-params': {'module': 'operationsinsights', 'class': 'list[DataObjectBindParameter]'}, 'query-time-filters': {'module': 'operationsinsights', 'class': 'DataObjectQueryTimeFilters'}}, output_type={'module': 'operationsinsights', 'class': 'QueryDataObjectResultSetRowsCollection'})
@cli_util.wrap_exceptions
def query_warehouse_data_object_data_data_object_standard_query_extended(ctx, **kwargs):
    ctx.invoke(operationsinsights_cli.query_warehouse_data_object_data_data_object_standard_query, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.delete_awr_hub_object, params_to_exclude=['object_name'])
@operationsinsights_cli.awr_hub_objects_group.command(name=operationsinsights_cli.delete_awr_hub_object.name, help=operationsinsights_cli.delete_awr_hub_object.help)
@cli_util.option('--name', required=True, help=u"""Unique Awr Hub Object identifier [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_awr_hub_object_extended(ctx, **kwargs):

    if 'name' in kwargs:
        kwargs['object_name'] = kwargs['name']
        kwargs.pop('name')

    ctx.invoke(operationsinsights_cli.delete_awr_hub_object, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.get_awr_hub_object, params_to_exclude=['object_name'])
@operationsinsights_cli.awr_hub_objects_group.command(name=operationsinsights_cli.get_awr_hub_object.name, help=operationsinsights_cli.get_awr_hub_object.help)
@cli_util.option('--name', required=True, help=u"""Unique Awr Hub Object identifier [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_awr_hub_object_extended(ctx, **kwargs):

    if 'name' in kwargs:
        kwargs['object_name'] = kwargs['name']
        kwargs.pop('name')

    ctx.invoke(operationsinsights_cli.get_awr_hub_object, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.head_awr_hub_object, params_to_exclude=['object_name'])
@operationsinsights_cli.awr_hub_objects_group.command(name=operationsinsights_cli.head_awr_hub_object.name, help=operationsinsights_cli.head_awr_hub_object.help)
@cli_util.option('--name', required=True, help=u"""Unique Awr Hub Object identifier [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def head_awr_hub_object_extended(ctx, **kwargs):

    if 'name' in kwargs:
        kwargs['object_name'] = kwargs['name']
        kwargs.pop('name')

    ctx.invoke(operationsinsights_cli.head_awr_hub_object, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.put_awr_hub_object, params_to_exclude=['object_name', 'put_awr_hub_object_body'])
@operationsinsights_cli.awr_hub_objects_group.command(name=operationsinsights_cli.put_awr_hub_object.name, help=operationsinsights_cli.put_awr_hub_object.help)
@cli_util.option('--name', help='The name of the object. Default value is the filename excluding the path. Required if reading object from STDIN.')
@cli_util.option('--file', type=click.File(mode='rb'), required=True,
                 help="The file to load as the content of the object, or '-' to read from STDIN.")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def put_awr_hub_object_extended(ctx, **kwargs):

    file = kwargs['file']

    # default object name is filename without path
    if kwargs['name'] is None:
        if not hasattr(file, 'name') or file.name == '<stdin>':
            raise click.UsageError('Option "--name" must be provided when reading object from stdin')
        kwargs['object_name'] = os.path.basename(file.name)

    if kwargs['name'] is not None:
        kwargs['object_name'] = kwargs['name']

    kwargs.pop('name')

    if 'file' in kwargs and kwargs['file']:
        content = kwargs['file'].read()
        kwargs['put_awr_hub_object_body'] = content

    del kwargs['file']

    ctx.invoke(operationsinsights_cli.put_awr_hub_object, **kwargs)


# oci opsi database-insights create-database-insight-create-mds-my-sql-database-insight-details -> oci opsi database-insights create-mds-my-sql-database
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.create_database_insight_create_mds_my_sql_database_insight_details, "create-mds-my-sql-database")


# oci opsi database-insights enable-database-insight-enable-mds-my-sql-database-insight-details -> oci opsi database-insights enable-mds-my-sql-database
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.enable_database_insight_enable_mds_my_sql_database_insight_details, "enable-mds-my-sql-database")


# oci opsi database-insights update-database-insight-update-mds-my-sql-database-insight -> oci opsi database-insights update-mds-my-sql-database
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.update_database_insight_update_mds_my_sql_database_insight, "update-mds-my-sql-database")


# oci opsi database-insights create-database-insight-create-macs-managed-cloud-database-insight-details -> oci opsi database-insights create-macs-managed-cloud-database-insight
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.create_database_insight_create_macs_managed_cloud_database_insight_details, "create-macs-managed-cloud-database-insight")


# oci opsi database-insights enable-database-insight-enable-macs-managed-cloud-database-insight-details -> oci opsi database-insights enable-macs-managed-cloud-database-insight
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.enable_database_insight_enable_macs_managed_cloud_database_insight_details, "enable-macs-managed-cloud-database-insight")


# oci opsi database-insights update-database-insight-update-macs-managed-cloud-database-insight-details -> oci opsi database-insights update-macs-managed-cloud-database-insight
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.update_database_insight_update_macs_managed_cloud_database_insight_details, "update-macs-managed-cloud-database-insight")


# oci opsi exadata-insights add-exadata-insight-members-add-macs-managed-cloud-exadata-insight-members-details -> oci opsi exadata-insights add-macs-managed-cloud-exadata-insight-members
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.exadata_insights_group, operationsinsights_cli.add_exadata_insight_members_add_macs_managed_cloud_exadata_insight_members_details, "add-macs-managed-cloud-exadata-insight-members")


# oci opsi exadata-insights create-exadata-insight-create-macs-managed-cloud-exadata-insight-details -> oci opsi exadata-insights create-macs-managed-cloud-exadata-insight
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.exadata_insights_group, operationsinsights_cli.create_exadata_insight_create_macs_managed_cloud_exadata_insight_details, "create-macs-managed-cloud-exadata-insight")


# oci opsi exadata-insights enable-exadata-insight-enable-macs-managed-cloud-exadata-insight-details -> oci opsi exadata-insights enable-macs-managed-cloud-exadata-insight
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.exadata_insights_group, operationsinsights_cli.enable_exadata_insight_enable_macs_managed_cloud_exadata_insight_details, "enable-macs-managed-cloud-exadata-insight")


# oci opsi exadata-insights update-exadata-insight-update-macs-managed-cloud-exadata-insight-details -> oci opsi exadata-insights update-macs-managed-cloud-exadata-insight
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.exadata_insights_group, operationsinsights_cli.update_exadata_insight_update_macs_managed_cloud_exadata_insight_details, "update-macs-managed-cloud-exadata-insight")


# oci opsi host-insights update-host-insight-update-macs-managed-cloud-database-host-insight-details -> oci opsi host-insights update-macs-managed-database-host-insight
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.host_insights_group, operationsinsights_cli.update_host_insight_update_macs_managed_cloud_database_host_insight_details, "update-macs-managed-database-host-insight")


# Remove change-macs-managed-cloud from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.change_macs_managed_cloud_database_insight_connection.name)


# Remove change-macs-managed-cloud-database-insight-connection-credentials-by-source from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.change_macs_managed_cloud_database_insight_connection_credentials_by_source.name)


# Remove test-macs-managed-cloud from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.test_macs_managed_cloud_database_insight_connection.name)


# Remove test-macs-managed-cloud-database-insight-connection-credentials-by-source from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.test_macs_managed_cloud_database_insight_connection_credentials_by_source.name)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.change_macs_managed_cloud_database_insight_connection_credential_by_vault, params_to_exclude=['connection_credential_details_credential_source_name', 'connection_credential_details_password_secret_id', 'connection_credential_details_role', 'connection_credential_details_user_name', 'connection_credential_details_wallet_secret_id'])
@operationsinsights_cli.database_insights_group.command(name=operationsinsights_cli.change_macs_managed_cloud_database_insight_connection_credential_by_vault.name, help=operationsinsights_cli.change_macs_managed_cloud_database_insight_connection_credential_by_vault.help)
@cli_util.option('--credential-source-name', required=True, help=u"""Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service. [required]""")
@cli_util.option('--password-secret-id', help=u"""The secret [OCID] mapping to the database credentials.""")
@cli_util.option('--role', type=custom_types.CliCaseInsensitiveChoice(["NORMAL"]), help=u"""database user role.""")
@cli_util.option('--user-name', help=u"""database user name.""")
@cli_util.option('--wallet-secret-id', help=u"""The [OCID] of the Secret where the database keystore contents are stored. This is used for TCPS support in BM/VM/ExaCS cases.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection-details': {'module': 'opsi', 'class': 'ConnectionDetails'}})
@cli_util.wrap_exceptions
def change_macs_managed_cloud_database_insight_connection_credential_by_vault_extended(ctx, **kwargs):

    if 'credential_source_name' in kwargs:
        kwargs['connection_credential_details_credential_source_name'] = kwargs['credential_source_name']
        kwargs.pop('credential_source_name')

    if 'password_secret_id' in kwargs:
        kwargs['connection_credential_details_password_secret_id'] = kwargs['password_secret_id']
        kwargs.pop('password_secret_id')

    if 'role' in kwargs:
        kwargs['connection_credential_details_role'] = kwargs['role']
        kwargs.pop('role')

    if 'user_name' in kwargs:
        kwargs['connection_credential_details_user_name'] = kwargs['user_name']
        kwargs.pop('user_name')

    if 'wallet_secret_id' in kwargs:
        kwargs['connection_credential_details_wallet_secret_id'] = kwargs['wallet_secret_id']
        kwargs.pop('wallet_secret_id')

    ctx.invoke(operationsinsights_cli.change_macs_managed_cloud_database_insight_connection_credential_by_vault, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.test_macs_managed_cloud_database_insight_connection_credential_by_vault, params_to_exclude=['connection_credential_details_credential_source_name', 'connection_credential_details_password_secret_id', 'connection_credential_details_role', 'connection_credential_details_user_name', 'connection_credential_details_wallet_secret_id'])
@operationsinsights_cli.database_insights_group.command(name=operationsinsights_cli.test_macs_managed_cloud_database_insight_connection_credential_by_vault.name, help=operationsinsights_cli.test_macs_managed_cloud_database_insight_connection_credential_by_vault.help)
@cli_util.option('--credential-source-name', required=True, help=u"""Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service. [required]""")
@cli_util.option('--password-secret-id', help=u"""The secret [OCID] mapping to the database credentials.""")
@cli_util.option('--role', type=custom_types.CliCaseInsensitiveChoice(["NORMAL"]), help=u"""database user role.""")
@cli_util.option('--user-name', help=u"""database user name.""")
@cli_util.option('--wallet-secret-id', help=u"""The [OCID] of the Secret where the database keystore contents are stored. This is used for TCPS support in BM/VM/ExaCS cases.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection-details': {'module': 'opsi', 'class': 'ConnectionDetails'}})
@cli_util.wrap_exceptions
def test_macs_managed_cloud_database_insight_connection_credential_by_vault_extended(ctx, **kwargs):

    if 'credential_source_name' in kwargs:
        kwargs['connection_credential_details_credential_source_name'] = kwargs['credential_source_name']
        kwargs.pop('credential_source_name')

    if 'password_secret_id' in kwargs:
        kwargs['connection_credential_details_password_secret_id'] = kwargs['password_secret_id']
        kwargs.pop('password_secret_id')

    if 'role' in kwargs:
        kwargs['connection_credential_details_role'] = kwargs['role']
        kwargs.pop('role')

    if 'user_name' in kwargs:
        kwargs['connection_credential_details_user_name'] = kwargs['user_name']
        kwargs.pop('user_name')

    if 'wallet_secret_id' in kwargs:
        kwargs['connection_credential_details_wallet_secret_id'] = kwargs['wallet_secret_id']
        kwargs.pop('wallet_secret_id')

    ctx.invoke(operationsinsights_cli.test_macs_managed_cloud_database_insight_connection_credential_by_vault, **kwargs)


# oci opsi database-insights create-database-insight-create-autonomous-database-insight-details -> oci opsi database-insights create-autonomous-database
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.create_database_insight_create_autonomous_database_insight_details, "create-autonomous-database")


# oci opsi database-insights enable-database-insight-enable-autonomous-database-insight-details -> oci opsi database-insights enable-autonomous-database
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.enable_database_insight_enable_autonomous_database_insight_details, "enable-autonomous-database")


# Remove change-pe-comanaged-database-insight-credential-by-iam from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.change_pe_comanaged_database_insight_credential_by_iam.name)


# oci opsi database-insights create-database-insight-create-external-mysql-database-insight-details -> oci opsi database-insights create-external-mysql-database-insight
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.create_database_insight_create_external_mysql_database_insight_details, "create-external-mysql-database-insight")


# oci opsi database-insights enable-database-insight-enable-external-mysql-database-insight-details -> oci opsi database-insights enable-external-mysql-database-insight
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.enable_database_insight_enable_external_mysql_database_insight_details, "enable-external-mysql-database-insight")


# oci opsi database-insights update-database-insight-update-external-mysql-database-insight-details -> oci opsi database-insights update-external-mysql-database-insight
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.update_database_insight_update_external_mysql_database_insight_details, "update-external-mysql-database-insight")


# oci opsi database-insights create-database-insight-create-macs-managed-autonomous-database-insight-details -> oci opsi database-insights create-macs-managed-autonomous-database-insight
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.create_database_insight_create_macs_managed_autonomous_database_insight_details, "create-macs-managed-autonomous-database-insight")


# oci opsi database-insights enable-database-insight-enable-macs-managed-autonomous-database-insight-details -> oci opsi database-insights enable-macs-managed-autonomous-database-insight
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.enable_database_insight_enable_macs_managed_autonomous_database_insight_details, "enable-macs-managed-autonomous-database-insight")


# oci opsi database-insights update-database-insight-update-macs-managed-autonomous-database-insight-details -> oci opsi database-insights update-macs-managed-autonomous-database-insight
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.database_insights_group, operationsinsights_cli.update_database_insight_update_macs_managed_autonomous_database_insight_details, "update-macs-managed-autonomous-database-insight")


# Remove change-autonomous-database-insight-advanced-features-credential-by-named-credentials from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.change_autonomous_database_insight_advanced_features_credential_by_named_credentials.name)


# Remove change-macs-managed-autonomous from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.change_macs_managed_autonomous_database_insight_connection.name)


# Remove change-macs-managed-autonomous-database-insight-connection-credential-by-iam from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.change_macs_managed_autonomous_database_insight_connection_credential_by_iam.name)


# Remove change-pe-comanaged-database-insight-credential-by-named-credentials from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.change_pe_comanaged_database_insight_credential_by_named_credentials.name)


# Remove enable-autonomous-database-insight-advanced-features-credential-by-named-credentials from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.enable_autonomous_database_insight_advanced_features_credential_by_named_credentials.name)


# Remove test-macs-managed-autonomous from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.test_macs_managed_autonomous_database_insight_connection.name)


# Remove test-macs-managed-autonomous-database-insight-connection-credential-by-iam from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.test_macs_managed_autonomous_database_insight_connection_credential_by_iam.name)


# Remove test-macs-managed-autonomous-database-insight-connection-credential-by-vault from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.test_macs_managed_autonomous_database_insight_connection_credential_by_vault.name)


# Remove test-macs-managed-autonomous-database-insight-connection-credentials-by-source from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.test_macs_managed_autonomous_database_insight_connection_credentials_by_source.name)


# Remove test-macs-managed-cloud-database-insight-connection-credential-by-named-credentials from oci opsi database-insights
operationsinsights_cli.database_insights_group.commands.pop(operationsinsights_cli.test_macs_managed_cloud_database_insight_connection_credential_by_named_credentials.name)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.change_macs_managed_autonomous_database_insight_connection_credential_by_named_credentials, params_to_exclude=['connection_credential_details_named_credential_id', 'connection_credential_details_credential_source_name'])
@operationsinsights_cli.database_insights_group.command(name=operationsinsights_cli.change_macs_managed_autonomous_database_insight_connection_credential_by_named_credentials.name, help=operationsinsights_cli.change_macs_managed_autonomous_database_insight_connection_credential_by_named_credentials.help)
@cli_util.option('--named-credential-id', help=u"""The credential [OCID] stored in management agent.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection-details': {'module': 'opsi', 'class': 'ConnectionDetails'}})
@cli_util.wrap_exceptions
def change_macs_managed_autonomous_database_insight_connection_credential_by_named_credentials_extended(ctx, **kwargs):

    if 'named_credential_id' in kwargs:
        kwargs['connection_credential_details_named_credential_id'] = kwargs['named_credential_id']
        kwargs.pop('named_credential_id')

    ctx.invoke(operationsinsights_cli.change_macs_managed_autonomous_database_insight_connection_credential_by_named_credentials, **kwargs)


@cli_util.copy_params_from_generated_command(operationsinsights_cli.test_macs_managed_autonomous_database_insight_connection_credential_by_named_credentials, params_to_exclude=['connection_credential_details_named_credential_id'])
@operationsinsights_cli.database_insights_group.command(name=operationsinsights_cli.test_macs_managed_autonomous_database_insight_connection_credential_by_named_credentials.name, help=operationsinsights_cli.test_macs_managed_autonomous_database_insight_connection_credential_by_named_credentials.help)
@cli_util.option('--named-credential-id', help=u"""The credential [OCID] stored in management agent.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection-details': {'module': 'opsi', 'class': 'ConnectionDetails'}})
@cli_util.wrap_exceptions
def test_macs_managed_autonomous_database_insight_connection_credential_by_named_credentials_extended(ctx, **kwargs):

    if 'named_credential_id' in kwargs:
        kwargs['connection_credential_details_named_credential_id'] = kwargs['named_credential_id']
        kwargs.pop('named_credential_id')

    ctx.invoke(operationsinsights_cli.test_macs_managed_autonomous_database_insight_connection_credential_by_named_credentials, **kwargs)
