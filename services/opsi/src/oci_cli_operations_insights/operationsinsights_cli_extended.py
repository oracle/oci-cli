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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'operationsinsights', 'class': 'DatabaseConfigurationCollection'})
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'host-type': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'operationsinsights', 'class': 'HostConfigurationCollection'})
@cli_util.wrap_exceptions
def list_host_configurations_extended(ctx, **kwargs):
    if 'em_bridge_id' in kwargs:
        kwargs['enterprise_manager_bridge_id'] = kwargs['em_bridge_id']
        kwargs.pop('em_bridge_id')

    ctx.invoke(operationsinsights_cli.list_host_configurations, **kwargs)


# oci opsi operations-insights-private-endpoint -> oci opsi opsi-private-endpoint
cli_util.rename_command(operationsinsights_cli, operationsinsights_cli.opsi_root_group, operationsinsights_cli.operations_insights_private_endpoint_group, "opsi-private-endpoint")


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
