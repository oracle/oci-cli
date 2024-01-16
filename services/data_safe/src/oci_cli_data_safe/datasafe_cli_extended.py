# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from services.data_safe.src.oci_cli_data_safe.generated import datasafe_cli

# 1 :
# From: oci data-safe data-safe-configuration get --compartment-id | -c, -? | -h | --help
# To: oci data-safe configuration get --compartment-id | -c, -? | -h | --help

cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.data_safe_configuration_group, "configuration")


# 2:
# From: oci data-safe data-safe-private-endpoint change-compartment --data-safe-private-endpoint-id, --compartment-id | -c, -? | -h | --help
# To: oci data-safe private-endpoint change-compartment --private-endpoint-id, --compartment-id | -c, -? | -h | --help
# Step 1: Rename data-safe-private-endpoint to  private-endpoint. This applies for all the commands
cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.data_safe_private_endpoint_group, "private-endpoint")


# Step 2: Change --data-safe-private-endpoint-id to --private-endpoint-id
@cli_util.copy_params_from_generated_command(datasafe_cli.change_data_safe_private_endpoint_compartment, params_to_exclude=['data_safe_private_endpoint_id'])
@datasafe_cli.data_safe_private_endpoint_group.command(name='change-compartment', help=datasafe_cli.change_data_safe_private_endpoint_compartment.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""unique data safe private endpoint identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_data_safe_private_endpoint_compartment_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['data_safe_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')
    ctx.invoke(datasafe_cli.change_data_safe_private_endpoint_compartment, **kwargs)

# 3:
# From: oci data-safe data-safe-private-endpoint delete --data-safe-private-endpoint-id, --force, -? | -h | --help
# To: oci data-safe private-endpoint delete --private-endpoint-id, --force, -? | -h | --help
# cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.data_safe_private_endpoint_group, "private-endpoint")


# Step 2:
@cli_util.copy_params_from_generated_command(datasafe_cli.delete_data_safe_private_endpoint, params_to_exclude=['data_safe_private_endpoint_id'])
@datasafe_cli.data_safe_private_endpoint_group.command(name='delete', help=datasafe_cli.delete_data_safe_private_endpoint.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""unique data safe private endpoint identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_data_safe_private_endpoint_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['data_safe_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')
    ctx.invoke(datasafe_cli.delete_data_safe_private_endpoint, **kwargs)

# 4
# From: oci data-safe data-safe-private-endpoint get --data-safe-private-endpoint-id, -? | -h | --help
# To: oci data-safe private-endpoint get --private-endpoint-id, -? | -h | --help
# Step 2:


@cli_util.copy_params_from_generated_command(datasafe_cli.get_data_safe_private_endpoint, params_to_exclude=['data_safe_private_endpoint_id'])
@datasafe_cli.data_safe_private_endpoint_group.command(name='get', help=datasafe_cli.get_data_safe_private_endpoint.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""unique data safe private endpoint identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_safe', 'class': 'DataSafePrivateEndpoint'})
@cli_util.wrap_exceptions
def get_data_safe_private_endpoint_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['data_safe_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')

    ctx.invoke(datasafe_cli.get_data_safe_private_endpoint, **kwargs)

# 5 :
# From: oci data-safe data-safe-private-endpoint update --data-safe-private-endpoint-id, --display-name, --defined-tags, --description, --force, --freeform-tags, -? | -h | --help, --nsg-ids
# To: oci data-safe private-endpoint update --private-endpoint-id, --display-name, --defined-tags, --description, --force, --freeform-tags, -? | -h | --help, --nsg-ids
# Step 2;


@cli_util.copy_params_from_generated_command(datasafe_cli.update_data_safe_private_endpoint, params_to_exclude=['data_safe_private_endpoint_id'])
@datasafe_cli.data_safe_private_endpoint_group.command(name='update', help=datasafe_cli.update_data_safe_private_endpoint.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""unique data safe private endpoint identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'data_safe', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_data_safe_private_endpoint_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['data_safe_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')
    ctx.invoke(datasafe_cli.update_data_safe_private_endpoint, **kwargs)


# 6 :
# From:
# oci data-safe enable-data-safe-configuration-details enable-data-safe-configuration --compartment-id | -c, --defined-tags, --force, --freeform-tags, -? | -h | --help, --is-enabled
# To: oci data-safe service enable --compartment-id | -c, --defined-tags, --force, --freeform-tags, -? | -h | --help, --is-enabled


cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.data_safe_configuration_group, "service")

cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_configuration_group, datasafe_cli.enable_data_safe_configuration, "enable")


# 7:
# From:  oci data-safe work-request-log-entry list-work-request-logs --work-request-id, --all, -? | -h | --help
# To: oci data-safe work-request-log-entry list --work-request-id, --all, -? | -h | --help
cli_util.rename_command(datasafe_cli, datasafe_cli.work_request_log_entry_group, datasafe_cli.list_work_request_logs, "list")


# Remove create-target-database-autonomous-database-details from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.create_target_database_autonomous_database_details.name)


# Remove create-target-database-database-cloud-service-details from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.create_target_database_database_cloud_service_details.name)


# Remove create-target-database-installed-database-details from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.create_target_database_installed_database_details.name)


# Remove create-target-database-on-premise-connector from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.create_target_database_on_premise_connector.name)


# Remove create-target-database-private-endpoint from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.create_target_database_private_endpoint.name)


# Remove update-target-database-autonomous-database-details from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.update_target_database_autonomous_database_details.name)


# Remove update-target-database-database-cloud-service-details from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.update_target_database_database_cloud_service_details.name)


# Remove update-target-database-installed-database-details from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.update_target_database_installed_database_details.name)


# Remove update-target-database-on-premise-connector from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.update_target_database_on_premise_connector.name)


# Remove update-target-database-private-endpoint from oci data-safe target-database
datasafe_cli.target_database_group.commands.pop(datasafe_cli.update_target_database_private_endpoint.name)


# oci data-safe masking-schema-collection list-masking-schemas -> oci data-safe masking-schema-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.masking_schema_collection_group, datasafe_cli.list_masking_schemas, "list")


# oci data-safe masking-object-collection list-masking-objects -> oci data-safe masking-object-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.masking_object_collection_group, datasafe_cli.list_masking_objects, "list")


# oci data-safe sensitive-schema-collection list-sensitive-schemas -> oci data-safe sensitive-schema-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.sensitive_schema_collection_group, datasafe_cli.list_sensitive_schemas, "list")


# oci data-safe sensitive-object-collection list-sensitive-objects -> oci data-safe sensitive-object-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.sensitive_object_collection_group, datasafe_cli.list_sensitive_objects, "list")


# oci data-safe masking-schema-collection -> oci data-safe masking-schema
cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.masking_schema_collection_group, "masking-schema")


# oci data-safe masking-object-collection -> oci data-safe masking-object
cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.masking_object_collection_group, "masking-object")


# oci data-safe sensitive-schema-collection -> oci data-safe sensitive-schema
cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.sensitive_schema_collection_group, "sensitive-schema")


# oci data-safe sensitive-object-collection -> oci data-safe sensitive-object
cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.sensitive_object_collection_group, "sensitive-object")


# oci data-safe audit-policy-analytic-collection list-audit-policy-analytics -> oci data-safe audit-policy-analytic-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.audit_policy_analytic_collection_group, datasafe_cli.list_audit_policy_analytics, "list")


# oci data-safe audit-policy-analytic-collection -> oci data-safe audit-policy-analytics
cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.audit_policy_analytic_collection_group, "audit-policy-analytics")


# oci data-safe database-security-config-collection list-database-security-configs -> oci data-safe database-security-config-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.database_security_config_collection_group, datasafe_cli.list_database_security_configs, "list")


# oci data-safe security-policy-collection list-security-policies -> oci data-safe security-policy-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.security_policy_collection_group, datasafe_cli.list_security_policies, "list")


# oci data-safe security-policy-deployment-collection list-security-policy-deployments -> oci data-safe security-policy-deployment-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.security_policy_deployment_collection_group, datasafe_cli.list_security_policy_deployments, "list")


# oci data-safe security-policy-entry-state-collection list-security-policy-entry-states -> oci data-safe security-policy-entry-state-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.security_policy_entry_state_collection_group, datasafe_cli.list_security_policy_entry_states, "list")


# oci data-safe sql-collection-analytics-collection list-sql-collection-analytics -> oci data-safe sql-collection-analytics-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.sql_collection_analytics_collection_group, datasafe_cli.list_sql_collection_analytics, "list")


# oci data-safe sql-collection-analytics-collection -> oci data-safe sql-collection-analytics
cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.sql_collection_analytics_collection_group, "sql-collection-analytics")


# oci data-safe sql-collection-collection list-sql-collections -> oci data-safe sql-collection-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.sql_collection_collection_group, datasafe_cli.list_sql_collections, "list")


# oci data-safe sql-collection-log-insights-collection list-sql-collection-log-insights -> oci data-safe sql-collection-log-insights-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.sql_collection_log_insights_collection_group, datasafe_cli.list_sql_collection_log_insights, "list")


# oci data-safe sql-collection-log-insights-collection -> oci data-safe sql-collection-log-insights
cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.sql_collection_log_insights_collection_group, "sql-collection-log-insights")


# oci data-safe sql-firewall-allowed-sql-analytics-collection list-sql-firewall-allowed-sql-analytics -> oci data-safe sql-firewall-allowed-sql-analytics-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.sql_firewall_allowed_sql_analytics_collection_group, datasafe_cli.list_sql_firewall_allowed_sql_analytics, "list")


# oci data-safe sql-firewall-allowed-sql-analytics-collection -> oci data-safe sql-firewall-allowed-sql-analytics
cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.sql_firewall_allowed_sql_analytics_collection_group, "sql-firewall-allowed-sql-analytics")


# oci data-safe sql-firewall-allowed-sql-collection list-sql-firewall-allowed-sqls -> oci data-safe sql-firewall-allowed-sql-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.sql_firewall_allowed_sql_collection_group, datasafe_cli.list_sql_firewall_allowed_sqls, "list")


# oci data-safe sql-firewall-allowed-sql-collection -> oci data-safe sql-firewall-allowed-sql
cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.sql_firewall_allowed_sql_collection_group, "sql-firewall-allowed-sql")


# oci data-safe sql-firewall-policy-analytics-collection list-sql-firewall-policy-analytics -> oci data-safe sql-firewall-policy-analytics-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.sql_firewall_policy_analytics_collection_group, datasafe_cli.list_sql_firewall_policy_analytics, "list")


# oci data-safe sql-firewall-policy-analytics-collection -> oci data-safe sql-firewall-policy-analytics
cli_util.rename_command(datasafe_cli, datasafe_cli.data_safe_root_group, datasafe_cli.sql_firewall_policy_analytics_collection_group, "sql-firewall-policy-analytics")


# oci data-safe sql-firewall-policy-collection list-sql-firewall-policies -> oci data-safe sql-firewall-policy-collection list
cli_util.rename_command(datasafe_cli, datasafe_cli.sql_firewall_policy_collection_group, datasafe_cli.list_sql_firewall_policies, "list")


# oci data-safe database-security-config-collection list-database-security-configs -> oci data-safe database-security-config
datasafe_cli.database_security_config_collection_group.commands.pop(datasafe_cli.list_database_security_configs.name)
datasafe_cli.database_security_config_group.add_command(datasafe_cli.list_database_security_configs)


# oci data-safe security-policy-collection list-security-policies -> oci data-safe security-policy
datasafe_cli.security_policy_collection_group.commands.pop(datasafe_cli.list_security_policies.name)
datasafe_cli.security_policy_group.add_command(datasafe_cli.list_security_policies)


# oci data-safe security-policy-deployment-collection list-security-policy-deployments -> oci data-safe security-policy-deployment
datasafe_cli.security_policy_deployment_collection_group.commands.pop(datasafe_cli.list_security_policy_deployments.name)
datasafe_cli.security_policy_deployment_group.add_command(datasafe_cli.list_security_policy_deployments)


# oci data-safe security-policy-entry-state-collection list-security-policy-entry-states -> oci data-safe security-policy-entry-state
datasafe_cli.security_policy_entry_state_collection_group.commands.pop(datasafe_cli.list_security_policy_entry_states.name)
datasafe_cli.security_policy_entry_state_group.add_command(datasafe_cli.list_security_policy_entry_states)


# oci data-safe sql-collection-collection list-sql-collections -> oci data-safe sql-collection
datasafe_cli.sql_collection_collection_group.commands.pop(datasafe_cli.list_sql_collections.name)
datasafe_cli.sql_collection_group.add_command(datasafe_cli.list_sql_collections)


# oci data-safe sql-firewall-policy-collection list-sql-firewall-policies -> oci data-safe sql-firewall-policy
datasafe_cli.sql_firewall_policy_collection_group.commands.pop(datasafe_cli.list_sql_firewall_policies.name)
datasafe_cli.sql_firewall_policy_group.add_command(datasafe_cli.list_sql_firewall_policies)


# removed command-less groups
datasafe_cli.data_safe_root_group.commands.pop(datasafe_cli.database_security_config_collection_group.name)
datasafe_cli.data_safe_root_group.commands.pop(datasafe_cli.security_policy_collection_group.name)
datasafe_cli.data_safe_root_group.commands.pop(datasafe_cli.security_policy_deployment_collection_group.name)
datasafe_cli.data_safe_root_group.commands.pop(datasafe_cli.security_policy_entry_state_collection_group.name)
datasafe_cli.data_safe_root_group.commands.pop(datasafe_cli.sql_collection_collection_group.name)
datasafe_cli.data_safe_root_group.commands.pop(datasafe_cli.sql_firewall_policy_collection_group.name)


# Remove create-peer-target-database-autonomous-database-details from oci data-safe peer-target-database
datasafe_cli.peer_target_database_group.commands.pop(datasafe_cli.create_peer_target_database_autonomous_database_details.name)


# Remove create-peer-target-database-installed-database-details from oci data-safe peer-target-database
datasafe_cli.peer_target_database_group.commands.pop(datasafe_cli.create_peer_target_database_installed_database_details.name)


# Remove update-peer-target-database-autonomous-database-details from oci data-safe peer-target-database
datasafe_cli.peer_target_database_group.commands.pop(datasafe_cli.update_peer_target_database_autonomous_database_details.name)


# Remove update-peer-target-database-installed-database-details from oci data-safe peer-target-database
datasafe_cli.peer_target_database_group.commands.pop(datasafe_cli.update_peer_target_database_installed_database_details.name)
