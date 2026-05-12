# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.database_tools.src.oci_cli_database_tools.generated import databasetools_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci database-tools database-tools-connection -> oci database-tools connection
cli_util.rename_command(databasetools_cli, databasetools_cli.dbtools_root_group, databasetools_cli.database_tools_connection_group, "connection")


# oci database-tools database-tools-endpoint-service -> oci database-tools endpoint-service
cli_util.rename_command(databasetools_cli, databasetools_cli.dbtools_root_group, databasetools_cli.database_tools_endpoint_service_group, "endpoint-service")


# oci database-tools database-tools-private-endpoint -> oci database-tools private-endpoint
cli_util.rename_command(databasetools_cli, databasetools_cli.dbtools_root_group, databasetools_cli.database_tools_private_endpoint_group, "private-endpoint")


# oci database-tools database-tools-connection create-database-tools-connection-create-database-tools-connection-oracle-database-details -> oci database-tools database-tools-connection create-oracle-database
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_connection_group, databasetools_cli.create_database_tools_connection_create_database_tools_connection_oracle_database_details, "create-oracle-database")


# oci database-tools database-tools-connection update-database-tools-connection-update-database-tools-connection-oracle-database-details -> oci database-tools database-tools-connection update-oracle-database
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_connection_group, databasetools_cli.update_database_tools_connection_update_database_tools_connection_oracle_database_details, "update-oracle-database")


# oci database-tools database-tools-connection validate-database-tools-connection-validate-database-tools-connection-oracle-database-details -> oci database-tools database-tools-connection validate-oracle-database
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_connection_group, databasetools_cli.validate_database_tools_connection_validate_database_tools_connection_oracle_database_details, "validate-oracle-database")


# oci database-tools work-request-log-entry list-work-request-logs -> oci database-tools work-request-log-entry list
cli_util.rename_command(databasetools_cli, databasetools_cli.work_request_log_entry_group, databasetools_cli.list_work_request_logs, "list")


# Remove create from oci database-tools database-tools-connection
databasetools_cli.database_tools_connection_group.commands.pop(databasetools_cli.create_database_tools_connection.name)


# Remove update from oci database-tools database-tools-connection
databasetools_cli.database_tools_connection_group.commands.pop(databasetools_cli.update_database_tools_connection.name)


# Remove validate from oci database-tools database-tools-connection
databasetools_cli.database_tools_connection_group.commands.pop(databasetools_cli.validate_database_tools_connection.name)


@cli_util.copy_params_from_generated_command(databasetools_cli.change_database_tools_connection_compartment, params_to_exclude=['database_tools_connection_id'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.change_database_tools_connection_compartment.name, help=databasetools_cli.change_database_tools_connection_compartment.help)
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Database Tools connection.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_database_tools_connection_compartment_extended(ctx, **kwargs):
    if 'connection_id' in kwargs:
        kwargs['database_tools_connection_id'] = kwargs['connection_id']
        kwargs.pop('connection_id')

    ctx.invoke(databasetools_cli.change_database_tools_connection_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.delete_database_tools_connection, params_to_exclude=['database_tools_connection_id'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.delete_database_tools_connection.name, help=databasetools_cli.delete_database_tools_connection.help)
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Database Tools connection.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_database_tools_connection_extended(ctx, **kwargs):
    if 'connection_id' in kwargs:
        kwargs['database_tools_connection_id'] = kwargs['connection_id']
        kwargs.pop('connection_id')

    ctx.invoke(databasetools_cli.delete_database_tools_connection, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.get_database_tools_connection, params_to_exclude=['database_tools_connection_id'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.get_database_tools_connection.name, help=databasetools_cli.get_database_tools_connection.help)
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Database Tools connection.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsConnection'})
@cli_util.wrap_exceptions
def get_database_tools_connection_extended(ctx, **kwargs):
    if 'connection_id' in kwargs:
        kwargs['database_tools_connection_id'] = kwargs['connection_id']
        kwargs.pop('connection_id')

    ctx.invoke(databasetools_cli.get_database_tools_connection, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.update_database_tools_connection_update_database_tools_connection_oracle_database_details, params_to_exclude=['database_tools_connection_id', 'user_password'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.update_database_tools_connection_update_database_tools_connection_oracle_database_details.name, help=databasetools_cli.update_database_tools_connection_update_database_tools_connection_oracle_database_details.help)
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Database Tools connection.""")
@cli_util.option('--user-password-secret-id', help="""The [OCID] of the secret containing the user password.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'UpdateDatabaseToolsRelatedResourceDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreDetails]'}, 'proxy-client': {'module': 'database_tools', 'class': 'DatabaseToolsConnectionOracleDatabaseProxyClient'}})
@cli_util.wrap_exceptions
def update_database_tools_connection_update_database_tools_connection_oracle_database_details_extended(ctx, **kwargs):
    if 'connection_id' in kwargs:
        kwargs['database_tools_connection_id'] = kwargs['connection_id']
        kwargs.pop('connection_id')

    # Flattening of user_password complex parameter
    if kwargs['user_password_secret_id']:
        user_password = {
            'value-type': 'SECRETID',
            'secret-id': kwargs['user_password_secret_id']
        }

        kwargs['user_password'] = json.dumps(user_password)

    kwargs.pop('user_password_secret_id', None)

    ctx.invoke(databasetools_cli.update_database_tools_connection_update_database_tools_connection_oracle_database_details, **kwargs)


databasetools_cli.create_database_tools_mcp_toolset_create_database_tools_mcp_toolset_built_in_sql_tools_details.help = """Creates a new Database Tools MCP Toolset for built-in SQL tools. \n[Command Reference](createDatabaseToolsMcpToolset)"""
databasetools_cli.create_database_tools_mcp_toolset_create_database_tools_mcp_toolset_custom_sql_tool_details.help = """Creates a new Database Tools MCP Toolset for a custom SQL tool. \n[Command Reference](createDatabaseToolsMcpToolset)"""
databasetools_cli.create_database_tools_mcp_toolset_create_database_tools_mcp_toolset_customizable_reporting_tools_details.help = """Creates a new Database Tools MCP Toolset for customizable reporting tools. \n[Command Reference](createDatabaseToolsMcpToolset)"""
databasetools_cli.create_database_tools_mcp_toolset_create_database_tools_mcp_toolset_gen_ai_sql_assistant_details.help = """Creates a new Database Tools MCP Toolset for a GenAI SQL assistant. \n[Command Reference](createDatabaseToolsMcpToolset)"""
databasetools_cli.update_database_tools_mcp_toolset_update_database_tools_mcp_toolset_built_in_sql_tools_details.help = """Updates the specified Database Tools MCP Toolset for built-in SQL tools. \n[Command Reference](updateDatabaseToolsMcpToolset)"""
databasetools_cli.update_database_tools_mcp_toolset_update_database_tools_mcp_toolset_custom_sql_tool_details.help = """Updates the specified Database Tools MCP Toolset for a custom SQL tool. \n[Command Reference](updateDatabaseToolsMcpToolset)"""
databasetools_cli.update_database_tools_mcp_toolset_update_database_tools_mcp_toolset_customizable_reporting_tools_details.help = """Updates the specified Database Tools MCP Toolset for customizable reporting tools. \n[Command Reference](updateDatabaseToolsMcpToolset)"""
databasetools_cli.update_database_tools_mcp_toolset_update_database_tools_mcp_toolset_gen_ai_sql_assistant_details.help = """Updates the specified Database Tools MCP Toolset for a GenAI SQL assistant. \n[Command Reference](updateDatabaseToolsMcpToolset)"""
databasetools_cli.database_tools_endpoint_service_group.help = """Provides information about Database Tools endpoint services."""
databasetools_cli.cascading_delete_database_tools_mcp_server.help = """Deletes the Database Tools MCP server resource and its associated assets. \n[Command Reference](cascadingDeleteDatabaseToolsMcpServer)"""
databasetools_cli.change_database_tools_mcp_server_compartment.help = """Moves the specified Database Tools MCP server to a different compartment in the same tenancy. \n[Command Reference](changeDatabaseToolsMcpServerCompartment)"""
databasetools_cli.get_database_tools_mcp_server.help = """Gets details of the specified Database Tools MCP server. \n[Command Reference](getDatabaseToolsMcpServer)"""
databasetools_cli.create_database_tools_database_api_gateway_config.help = """Creates a new Database Tools database API gateway config. \n[Command Reference](createDatabaseToolsDatabaseApiGatewayConfig)"""
databasetools_cli.create_database_tools_database_api_gateway_config_create_database_tools_database_api_gateway_config_default_details.help = """Creates a new default Database Tools database API gateway config. \n[Command Reference](createDatabaseToolsDatabaseApiGatewayConfig)"""
databasetools_cli.create_database_tools_sql_report.help = """Creates a new Database Tools SQL report. \n[Command Reference](createDatabaseToolsSqlReport)"""
databasetools_cli.create_database_tools_sql_report_create_database_tools_sql_report_oracle_database_details.help = """Creates a new Database Tools SQL report for Oracle Database. \n[Command Reference](createDatabaseToolsSqlReport)"""


@cli_util.copy_params_from_generated_command(databasetools_cli.create_database_tools_connection_create_database_tools_connection_oracle_database_details, params_to_exclude=['user_password'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.create_database_tools_connection_create_database_tools_connection_oracle_database_details.name, help=databasetools_cli.create_database_tools_connection_create_database_tools_connection_oracle_database_details.help)
@cli_util.option('--user-password-secret-id', help="""The [OCID] of the secret containing the user password. Required when ``--authentication-type`` is ``PASSWORD``. Not required when ``--authentication-type`` is ``TOKEN``.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'CreateDatabaseToolsRelatedResourceDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreDetails]'}, 'proxy-client': {'module': 'database_tools', 'class': 'DatabaseToolsConnectionOracleDatabaseProxyClient'}, 'locks': {'module': 'database_tools', 'class': 'list[ResourceLock]'}})
@cli_util.wrap_exceptions
def create_database_tools_connection_create_database_tools_connection_oracle_database_details_extended(ctx, **kwargs):
    # Flattening of user_password complex parameter
    if kwargs['user_password_secret_id']:
        user_password = {
            'value-type': 'SECRETID',
            'secret-id': kwargs['user_password_secret_id']
        }

        kwargs['user_password'] = json.dumps(user_password)

    kwargs.pop('user_password_secret_id', None)

    ctx.invoke(databasetools_cli.create_database_tools_connection_create_database_tools_connection_oracle_database_details, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.validate_database_tools_connection_validate_database_tools_connection_oracle_database_details, params_to_exclude=['database_tools_connection_id'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.validate_database_tools_connection_validate_database_tools_connection_oracle_database_details.name, help=databasetools_cli.validate_database_tools_connection_validate_database_tools_connection_oracle_database_details.help)
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Database Tools connection.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'ValidateDatabaseToolsConnectionResult'})
@cli_util.wrap_exceptions
def validate_database_tools_connection_validate_database_tools_connection_oracle_database_details_extended(ctx, **kwargs):
    if 'connection_id' in kwargs:
        kwargs['database_tools_connection_id'] = kwargs['connection_id']
        kwargs.pop('connection_id')

    ctx.invoke(databasetools_cli.validate_database_tools_connection_validate_database_tools_connection_oracle_database_details, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.get_database_tools_endpoint_service, params_to_exclude=['database_tools_endpoint_service_id'])
@databasetools_cli.database_tools_endpoint_service_group.command(name=databasetools_cli.get_database_tools_endpoint_service.name, help=databasetools_cli.get_database_tools_endpoint_service.help)
@cli_util.option('--endpoint-service-id', required=True, help=u"""The [OCID] of a DatabaseToolsEndpointService. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsEndpointService'})
@cli_util.wrap_exceptions
def get_database_tools_endpoint_service_extended(ctx, **kwargs):
    if 'endpoint_service_id' in kwargs:
        kwargs['database_tools_endpoint_service_id'] = kwargs['endpoint_service_id']
        kwargs.pop('endpoint_service_id')

    ctx.invoke(databasetools_cli.get_database_tools_endpoint_service, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.change_database_tools_private_endpoint_compartment, params_to_exclude=['database_tools_private_endpoint_id'])
@databasetools_cli.database_tools_private_endpoint_group.command(name=databasetools_cli.change_database_tools_private_endpoint_compartment.name, help=databasetools_cli.change_database_tools_private_endpoint_compartment.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of a Database Tools private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_database_tools_private_endpoint_compartment_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['database_tools_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')

    ctx.invoke(databasetools_cli.change_database_tools_private_endpoint_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.delete_database_tools_private_endpoint, params_to_exclude=['database_tools_private_endpoint_id'])
@databasetools_cli.database_tools_private_endpoint_group.command(name=databasetools_cli.delete_database_tools_private_endpoint.name, help=databasetools_cli.delete_database_tools_private_endpoint.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of a Database Tools private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_database_tools_private_endpoint_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['database_tools_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')

    ctx.invoke(databasetools_cli.delete_database_tools_private_endpoint, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.get_database_tools_private_endpoint, params_to_exclude=['database_tools_private_endpoint_id'])
@databasetools_cli.database_tools_private_endpoint_group.command(name=databasetools_cli.get_database_tools_private_endpoint.name, help=databasetools_cli.get_database_tools_private_endpoint.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of a Database Tools private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsPrivateEndpoint'})
@cli_util.wrap_exceptions
def get_database_tools_private_endpoint_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['database_tools_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')

    ctx.invoke(databasetools_cli.get_database_tools_private_endpoint, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.update_database_tools_private_endpoint, params_to_exclude=['database_tools_private_endpoint_id'])
@databasetools_cli.database_tools_private_endpoint_group.command(name=databasetools_cli.update_database_tools_private_endpoint.name, help=databasetools_cli.update_database_tools_private_endpoint.help)
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of a Database Tools private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'database_tools', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_database_tools_private_endpoint_extended(ctx, **kwargs):
    if 'private_endpoint_id' in kwargs:
        kwargs['database_tools_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')

    ctx.invoke(databasetools_cli.update_database_tools_private_endpoint, **kwargs)


# oci dbtools connection create-database-tools-connection-create-database-tools-connection-my-sql-details -> oci dbtools connection create-mysql-database
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_connection_group, databasetools_cli.create_database_tools_connection_create_database_tools_connection_my_sql_details, "create-mysql-database")


# oci dbtools connection update-database-tools-connection-update-database-tools-connection-my-sql-details -> oci dbtools connection update-mysql-database
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_connection_group, databasetools_cli.update_database_tools_connection_update_database_tools_connection_my_sql_details, "update-mysql-database")


# oci dbtools connection validate-database-tools-connection-validate-database-tools-connection-my-sql-details -> oci dbtools connection validate-mysql-database
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_connection_group, databasetools_cli.validate_database_tools_connection_validate_database_tools_connection_my_sql_details, "validate-mysql-database")


@cli_util.copy_params_from_generated_command(databasetools_cli.create_database_tools_connection_create_database_tools_connection_my_sql_details, params_to_exclude=['user_password'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.create_database_tools_connection_create_database_tools_connection_my_sql_details.name, help=databasetools_cli.create_database_tools_connection_create_database_tools_connection_my_sql_details.help)
@cli_util.option('--user-password-secret-id', required=True, help="""The [OCID] of the secret containing the user password.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'CreateDatabaseToolsRelatedResourceDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreDetails]'}, 'locks': {'module': 'database_tools', 'class': 'list[ResourceLock]'}})
@cli_util.wrap_exceptions
def create_database_tools_connection_create_database_tools_connection_my_sql_details_extended(ctx, **kwargs):
    # Flattening of user_password complex parameter
    if kwargs['user_password_secret_id']:
        user_password = {
            'value-type': 'SECRETID',
            'secret-id': kwargs['user_password_secret_id']
        }

        kwargs['user_password'] = json.dumps(user_password)

    kwargs.pop('user_password_secret_id', None)

    ctx.invoke(databasetools_cli.create_database_tools_connection_create_database_tools_connection_my_sql_details, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.update_database_tools_connection_update_database_tools_connection_my_sql_details, params_to_exclude=['database_tools_connection_id', 'user_password'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.update_database_tools_connection_update_database_tools_connection_my_sql_details.name, help=databasetools_cli.update_database_tools_connection_update_database_tools_connection_my_sql_details.help)
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Database Tools connection.""")
@cli_util.option('--user-password-secret-id', help="""The [OCID] of the secret containing the user password.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'UpdateDatabaseToolsRelatedResourceMySqlDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreMySqlDetails]'}})
@cli_util.wrap_exceptions
def update_database_tools_connection_update_database_tools_connection_my_sql_details_extended(ctx, **kwargs):
    if 'connection_id' in kwargs:
        kwargs['database_tools_connection_id'] = kwargs['connection_id']
        kwargs.pop('connection_id')

    # Flattening of user_password complex parameter
    if kwargs['user_password_secret_id']:
        user_password = {
            'value-type': 'SECRETID',
            'secret-id': kwargs['user_password_secret_id']
        }

        kwargs['user_password'] = json.dumps(user_password)

    kwargs.pop('user_password_secret_id', None)

    ctx.invoke(databasetools_cli.update_database_tools_connection_update_database_tools_connection_my_sql_details, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.validate_database_tools_connection_validate_database_tools_connection_my_sql_details, params_to_exclude=['database_tools_connection_id'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.validate_database_tools_connection_validate_database_tools_connection_my_sql_details.name, help=databasetools_cli.validate_database_tools_connection_validate_database_tools_connection_my_sql_details.help)
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Database Tools connection.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'ValidateDatabaseToolsConnectionResult'})
@cli_util.wrap_exceptions
def validate_database_tools_connection_validate_database_tools_connection_my_sql_details_extended(ctx, **kwargs):
    if 'connection_id' in kwargs:
        kwargs['database_tools_connection_id'] = kwargs['connection_id']
        kwargs.pop('connection_id')

    ctx.invoke(databasetools_cli.validate_database_tools_connection_validate_database_tools_connection_my_sql_details, **kwargs)


# oci dbtools connection create-database-tools-connection-create-database-tools-connection-postgresql-details -> oci dbtools connection create-postgresql
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_connection_group, databasetools_cli.create_database_tools_connection_create_database_tools_connection_postgresql_details, "create-postgresql")


# oci dbtools connection update-database-tools-connection-update-database-tools-connection-postgresql-details -> oci dbtools connection update-postgresql
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_connection_group, databasetools_cli.update_database_tools_connection_update_database_tools_connection_postgresql_details, "update-postgresql")


# oci dbtools connection create-database-tools-connection-create-database-tools-connection-generic-jdbc-details -> oci dbtools connection create-generic-jdbc
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_connection_group, databasetools_cli.create_database_tools_connection_create_database_tools_connection_generic_jdbc_details, "create-generic-jdbc")


# oci dbtools connection update-database-tools-connection-update-database-tools-connection-generic-jdbc-details -> oci dbtools connection update-generic-jdbc
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_connection_group, databasetools_cli.update_database_tools_connection_update_database_tools_connection_generic_jdbc_details, "update-generic-jdbc")


# oci dbtools connection add -> oci dbtools connection add-lock
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_connection_group, databasetools_cli.add_database_tools_connection_lock, "add-lock")


# oci dbtools connection remove -> oci dbtools connection remove-lock
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_connection_group, databasetools_cli.remove_database_tools_connection_lock, "remove-lock")


# oci dbtools private-endpoint add -> oci dbtools private-endpoint add-lock
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_private_endpoint_group, databasetools_cli.add_database_tools_private_endpoint_lock, "add-lock")


# oci dbtools private-endpoint remove -> oci dbtools private-endpoint remove-lock
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_private_endpoint_group, databasetools_cli.remove_database_tools_private_endpoint_lock, "remove-lock")


# oci dbtools connection validate-database-tools-connection-validate-database-tools-connection-postgresql-details -> oci dbtools connection validate-postgresql
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_connection_group, databasetools_cli.validate_database_tools_connection_validate_database_tools_connection_postgresql_details, "validate-postgresql")


@cli_util.copy_params_from_generated_command(databasetools_cli.validate_database_tools_connection_validate_database_tools_connection_postgresql_details, params_to_exclude=['database_tools_connection_id'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.validate_database_tools_connection_validate_database_tools_connection_postgresql_details.name, help=databasetools_cli.validate_database_tools_connection_validate_database_tools_connection_postgresql_details.help)
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Database Tools connection. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'ValidateDatabaseToolsConnectionResult'})
@cli_util.wrap_exceptions
def validate_database_tools_connection_validate_database_tools_connection_postgresql_details_extended(ctx, **kwargs):

    if 'connection_id' in kwargs:
        kwargs['database_tools_connection_id'] = kwargs['connection_id']
        kwargs.pop('connection_id')

    ctx.invoke(databasetools_cli.validate_database_tools_connection_validate_database_tools_connection_postgresql_details, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.add_database_tools_connection_lock, params_to_exclude=['database_tools_connection_id'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.add_database_tools_connection_lock.name, help="Adds a lock to a Database Tools connection resource. \n[Command Reference](addDatabaseToolsConnectionLock)")
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Database Tools connection. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsConnection'})
@cli_util.wrap_exceptions
def add_database_tools_connection_lock_extended(ctx, **kwargs):

    if 'connection_id' in kwargs:
        kwargs['database_tools_connection_id'] = kwargs['connection_id']
        kwargs.pop('connection_id')

    ctx.invoke(databasetools_cli.add_database_tools_connection_lock, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.remove_database_tools_connection_lock, params_to_exclude=['database_tools_connection_id'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.remove_database_tools_connection_lock.name, help="Removes a lock from a Database Tools connection resource. \n[Command Reference](removeDatabaseToolsConnectionLock)")
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Database Tools connection. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsConnection'})
@cli_util.wrap_exceptions
def remove_database_tools_connection_lock_extended(ctx, **kwargs):

    if 'connection_id' in kwargs:
        kwargs['database_tools_connection_id'] = kwargs['connection_id']
        kwargs.pop('connection_id')

    ctx.invoke(databasetools_cli.remove_database_tools_connection_lock, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.add_database_tools_private_endpoint_lock, params_to_exclude=['database_tools_private_endpoint_id'])
@databasetools_cli.database_tools_private_endpoint_group.command(name=databasetools_cli.add_database_tools_private_endpoint_lock.name, help="Adds a lock to a Database Tools private endpoint resource. \n[Command Reference](addDatabaseToolsPrivateEndpointLock)")
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of a Database Tools private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsPrivateEndpoint'})
@cli_util.wrap_exceptions
def add_database_tools_private_endpoint_lock_extended(ctx, **kwargs):

    if 'private_endpoint_id' in kwargs:
        kwargs['database_tools_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')

    ctx.invoke(databasetools_cli.add_database_tools_private_endpoint_lock, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.remove_database_tools_private_endpoint_lock, params_to_exclude=['database_tools_private_endpoint_id'])
@databasetools_cli.database_tools_private_endpoint_group.command(name=databasetools_cli.remove_database_tools_private_endpoint_lock.name, help="Removes a lock from a Database Tools private endpoint resource. \n[Command Reference](removeDatabaseToolsPrivateEndpointLock)")
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of a Database Tools private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsPrivateEndpoint'})
@cli_util.wrap_exceptions
def remove_database_tools_private_endpoint_lock_extended(ctx, **kwargs):

    if 'private_endpoint_id' in kwargs:
        kwargs['database_tools_private_endpoint_id'] = kwargs['private_endpoint_id']
        kwargs.pop('private_endpoint_id')

    ctx.invoke(databasetools_cli.remove_database_tools_private_endpoint_lock, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.update_database_tools_connection_update_database_tools_connection_generic_jdbc_details, params_to_exclude=['database_tools_connection_id', 'user_password'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.update_database_tools_connection_update_database_tools_connection_generic_jdbc_details.name, help=databasetools_cli.update_database_tools_connection_update_database_tools_connection_generic_jdbc_details.help)
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Database Tools Connection.""")
@cli_util.option('--user-password-secret-id', help="""The [OCID] of the secret containing the user password.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'UpdateDatabaseToolsRelatedResourceDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreDetails]'}})
@cli_util.wrap_exceptions
def update_database_tools_connection_update_database_tools_connection_generic_jdbc_details_extended(ctx, **kwargs):
    if 'connection_id' in kwargs:
        kwargs['database_tools_connection_id'] = kwargs['connection_id']
        kwargs.pop('connection_id')

    # Flattening of user_password complex parameter
    if kwargs['user_password_secret_id']:
        user_password = {
            'value-type': 'SECRETID',
            'secret-id': kwargs['user_password_secret_id']
        }

        kwargs['user_password'] = json.dumps(user_password)

    kwargs.pop('user_password_secret_id', None)

    ctx.invoke(databasetools_cli.update_database_tools_connection_update_database_tools_connection_generic_jdbc_details, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.create_database_tools_connection_create_database_tools_connection_generic_jdbc_details, params_to_exclude=['user_password'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.create_database_tools_connection_create_database_tools_connection_generic_jdbc_details.name, help=databasetools_cli.create_database_tools_connection_create_database_tools_connection_generic_jdbc_details.help)
@cli_util.option('--user-password-secret-id', required=True, help="""The [OCID] of the secret containing the user password.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'CreateDatabaseToolsRelatedResourceDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreDetails]'}, 'locks': {'module': 'database_tools', 'class': 'list[ResourceLock]'}})
@cli_util.wrap_exceptions
def create_database_tools_connection_create_database_tools_connection_generic_jdbc_details_extended(ctx, **kwargs):
    # Flattening of user_password complex parameter
    if kwargs['user_password_secret_id']:
        user_password = {
            'value-type': 'SECRETID',
            'secret-id': kwargs['user_password_secret_id']
        }

        kwargs['user_password'] = json.dumps(user_password)

    kwargs.pop('user_password_secret_id', None)

    ctx.invoke(databasetools_cli.create_database_tools_connection_create_database_tools_connection_generic_jdbc_details, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.update_database_tools_connection_update_database_tools_connection_postgresql_details, params_to_exclude=['database_tools_connection_id', 'user_password'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.update_database_tools_connection_update_database_tools_connection_postgresql_details.name, help=databasetools_cli.update_database_tools_connection_update_database_tools_connection_postgresql_details.help)
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Database Tools connection.""")
@cli_util.option('--user-password-secret-id', help="""The [OCID] of the secret containing the user password.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'UpdateDatabaseToolsRelatedResourceDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreDetails]'}})
@cli_util.wrap_exceptions
def update_database_tools_connection_update_database_tools_connection_postgresql_details_extended(ctx, **kwargs):
    if 'connection_id' in kwargs:
        kwargs['database_tools_connection_id'] = kwargs['connection_id']
        kwargs.pop('connection_id')

    # Flattening of user_password complex parameter
    if kwargs['user_password_secret_id']:
        user_password = {
            'value-type': 'SECRETID',
            'secret-id': kwargs['user_password_secret_id']
        }

        kwargs['user_password'] = json.dumps(user_password)

    kwargs.pop('user_password_secret_id', None)

    ctx.invoke(databasetools_cli.update_database_tools_connection_update_database_tools_connection_postgresql_details, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.create_database_tools_connection_create_database_tools_connection_postgresql_details, params_to_exclude=['user_password'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.create_database_tools_connection_create_database_tools_connection_postgresql_details.name, help=databasetools_cli.create_database_tools_connection_create_database_tools_connection_postgresql_details.help)
@cli_util.option('--user-password-secret-id', required=True, help="""The [OCID] of the secret containing the user password.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'CreateDatabaseToolsRelatedResourceDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreDetails]'}, 'locks': {'module': 'database_tools', 'class': 'list[ResourceLock]'}})
@cli_util.wrap_exceptions
def create_database_tools_connection_create_database_tools_connection_postgresql_details_extended(ctx, **kwargs):
    # Flattening of user_password complex parameter
    if kwargs['user_password_secret_id']:
        user_password = {
            'value-type': 'SECRETID',
            'secret-id': kwargs['user_password_secret_id']
        }

        kwargs['user_password'] = json.dumps(user_password)

    kwargs.pop('user_password_secret_id', None)

    ctx.invoke(databasetools_cli.create_database_tools_connection_create_database_tools_connection_postgresql_details, **kwargs)


# oci dbtools database-tools-identity add -> oci dbtools database-tools-identity add-lock
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_identity_group, databasetools_cli.add_database_tools_identity_lock, "add-lock")


# oci dbtools database-tools-identity remove -> oci dbtools database-tools-identity remove-lock
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_identity_group, databasetools_cli.remove_database_tools_identity_lock, "remove-lock")


# oci dbtools database-tools-identity create-database-tools-identity-create-database-tools-identity-oracle-database-resource-principal-details -> oci dbtools database-tools-identity create-oracle-database-resource-principal
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_identity_group, databasetools_cli.create_database_tools_identity_create_database_tools_identity_oracle_database_resource_principal_details, "create-oracle-database-resource-principal")


# oci dbtools database-tools-identity refresh-database-tools-identity-credential-refresh-database-tools-identity-oracle-database-resource-principal-credential-details -> oci dbtools database-tools-identity refresh-oracle-database-resource-principal-credential
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_identity_group, databasetools_cli.refresh_database_tools_identity_credential_refresh_database_tools_identity_oracle_database_resource_principal_credential_details, "refresh-oracle-database-resource-principal-credential")


# oci dbtools database-tools-identity update-database-tools-identity-update-database-tools-identity-oracle-database-resource-principal-details -> oci dbtools database-tools-identity update-oracle-database-resource-principal
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_identity_group, databasetools_cli.update_database_tools_identity_update_database_tools_identity_oracle_database_resource_principal_details, "update-oracle-database-resource-principal")


# oci dbtools database-tools-identity validate-database-tools-identity-credential-validate-database-tools-identity-credential-oracle-database-resource-principal-details -> oci dbtools database-tools-identity validate-oracle-database-resource-principal-credential
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_identity_group, databasetools_cli.validate_database_tools_identity_credential_validate_database_tools_identity_credential_oracle_database_resource_principal_details, "validate-oracle-database-resource-principal-credential")


# oci dbtools database-tools-identity -> oci dbtools identity
cli_util.rename_command(databasetools_cli, databasetools_cli.dbtools_root_group, databasetools_cli.database_tools_identity_group, "identity")


# Remove create from oci dbtools database-tools-identity
databasetools_cli.database_tools_identity_group.commands.pop(databasetools_cli.create_database_tools_identity.name)


# Remove refresh-database-tools-identity-credential from oci dbtools database-tools-identity
databasetools_cli.database_tools_identity_group.commands.pop(databasetools_cli.refresh_database_tools_identity_credential.name)


# Remove update from oci dbtools database-tools-identity
databasetools_cli.database_tools_identity_group.commands.pop(databasetools_cli.update_database_tools_identity.name)


# Remove validate-database-tools-identity-credential from oci dbtools database-tools-identity
databasetools_cli.database_tools_identity_group.commands.pop(databasetools_cli.validate_database_tools_identity_credential.name)


@cli_util.copy_params_from_generated_command(databasetools_cli.add_database_tools_identity_lock, params_to_exclude=['database_tools_identity_id'])
@databasetools_cli.database_tools_identity_group.command(name=databasetools_cli.add_database_tools_identity_lock.name, help="Adds a lock to a Database Tools identity resource. \n[Command Reference](addDatabaseToolsIdentityLock)")
@cli_util.option('--identity-id', required=True, help=u"""The [OCID] of a Database Tools identity. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsIdentity'})
@cli_util.wrap_exceptions
def add_database_tools_identity_lock_extended(ctx, **kwargs):

    if 'identity_id' in kwargs:
        kwargs['database_tools_identity_id'] = kwargs['identity_id']
        kwargs.pop('identity_id')

    ctx.invoke(databasetools_cli.add_database_tools_identity_lock, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.change_database_tools_identity_compartment, params_to_exclude=['database_tools_identity_id'])
@databasetools_cli.database_tools_identity_group.command(name=databasetools_cli.change_database_tools_identity_compartment.name, help=databasetools_cli.change_database_tools_identity_compartment.help)
@cli_util.option('--identity-id', required=True, help=u"""The [OCID] of a Database Tools identity. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_database_tools_identity_compartment_extended(ctx, **kwargs):

    if 'identity_id' in kwargs:
        kwargs['database_tools_identity_id'] = kwargs['identity_id']
        kwargs.pop('identity_id')

    ctx.invoke(databasetools_cli.change_database_tools_identity_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.create_database_tools_identity_create_database_tools_identity_oracle_database_resource_principal_details, params_to_exclude=['database_tools_connection_id'])
@databasetools_cli.database_tools_identity_group.command(name=databasetools_cli.create_database_tools_identity_create_database_tools_identity_oracle_database_resource_principal_details.name, help=databasetools_cli.create_database_tools_identity_create_database_tools_identity_oracle_database_resource_principal_details.help)
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of the related Database Tools Connection. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'locks': {'module': 'database_tools', 'class': 'list[ResourceLock]'}}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsIdentity'})
@cli_util.wrap_exceptions
def create_database_tools_identity_create_database_tools_identity_oracle_database_resource_principal_details_extended(ctx, **kwargs):

    if 'connection_id' in kwargs:
        kwargs['database_tools_connection_id'] = kwargs['connection_id']
        kwargs.pop('connection_id')

    ctx.invoke(databasetools_cli.create_database_tools_identity_create_database_tools_identity_oracle_database_resource_principal_details, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.delete_database_tools_identity, params_to_exclude=['database_tools_identity_id'])
@databasetools_cli.database_tools_identity_group.command(name=databasetools_cli.delete_database_tools_identity.name, help=databasetools_cli.delete_database_tools_identity.help)
@cli_util.option('--identity-id', required=True, help=u"""The [OCID] of a Database Tools identity. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_database_tools_identity_extended(ctx, **kwargs):

    if 'identity_id' in kwargs:
        kwargs['database_tools_identity_id'] = kwargs['identity_id']
        kwargs.pop('identity_id')

    ctx.invoke(databasetools_cli.delete_database_tools_identity, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.get_database_tools_identity, params_to_exclude=['database_tools_identity_id'])
@databasetools_cli.database_tools_identity_group.command(name=databasetools_cli.get_database_tools_identity.name, help=databasetools_cli.get_database_tools_identity.help)
@cli_util.option('--identity-id', required=True, help=u"""The [OCID] of a Database Tools identity. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsIdentity'})
@cli_util.wrap_exceptions
def get_database_tools_identity_extended(ctx, **kwargs):

    if 'identity_id' in kwargs:
        kwargs['database_tools_identity_id'] = kwargs['identity_id']
        kwargs.pop('identity_id')

    ctx.invoke(databasetools_cli.get_database_tools_identity, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.list_database_tools_identities, params_to_exclude=['database_tools_connection_id'])
@databasetools_cli.database_tools_identity_group.command(name=databasetools_cli.list_database_tools_identities.name, help=databasetools_cli.list_database_tools_identities.help)
@cli_util.option('--connection-id', help=u"""A filter to return only resources their `databaseToolsConnectionId` matches the specified `databaseToolsConnectionId`.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsIdentityCollection'})
@cli_util.wrap_exceptions
def list_database_tools_identities_extended(ctx, **kwargs):

    if 'connection_id' in kwargs:
        kwargs['database_tools_connection_id'] = kwargs['connection_id']
        kwargs.pop('connection_id')

    ctx.invoke(databasetools_cli.list_database_tools_identities, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.refresh_database_tools_identity_credential_refresh_database_tools_identity_oracle_database_resource_principal_credential_details, params_to_exclude=['database_tools_identity_id'])
@databasetools_cli.database_tools_identity_group.command(name=databasetools_cli.refresh_database_tools_identity_credential_refresh_database_tools_identity_oracle_database_resource_principal_credential_details.name, help=databasetools_cli.refresh_database_tools_identity_credential_refresh_database_tools_identity_oracle_database_resource_principal_credential_details.help)
@cli_util.option('--identity-id', required=True, help=u"""The [OCID] of a Database Tools identity. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def refresh_database_tools_identity_credential_refresh_database_tools_identity_oracle_database_resource_principal_credential_details_extended(ctx, **kwargs):

    if 'identity_id' in kwargs:
        kwargs['database_tools_identity_id'] = kwargs['identity_id']
        kwargs.pop('identity_id')

    ctx.invoke(databasetools_cli.refresh_database_tools_identity_credential_refresh_database_tools_identity_oracle_database_resource_principal_credential_details, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.remove_database_tools_identity_lock, params_to_exclude=['database_tools_identity_id'])
@databasetools_cli.database_tools_identity_group.command(name=databasetools_cli.remove_database_tools_identity_lock.name, help="Removes a lock from a Database Tools identity resource. \n[Command Reference](removeDatabaseToolsIdentityLock)")
@cli_util.option('--identity-id', required=True, help=u"""The [OCID] of a Database Tools identity. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsIdentity'})
@cli_util.wrap_exceptions
def remove_database_tools_identity_lock_extended(ctx, **kwargs):

    if 'identity_id' in kwargs:
        kwargs['database_tools_identity_id'] = kwargs['identity_id']
        kwargs.pop('identity_id')

    ctx.invoke(databasetools_cli.remove_database_tools_identity_lock, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.update_database_tools_identity_update_database_tools_identity_oracle_database_resource_principal_details, params_to_exclude=['database_tools_identity_id'])
@databasetools_cli.database_tools_identity_group.command(name=databasetools_cli.update_database_tools_identity_update_database_tools_identity_oracle_database_resource_principal_details.name, help=databasetools_cli.update_database_tools_identity_update_database_tools_identity_oracle_database_resource_principal_details.help)
@cli_util.option('--identity-id', required=True, help=u"""The [OCID] of a Database Tools identity. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}})
@cli_util.wrap_exceptions
def update_database_tools_identity_update_database_tools_identity_oracle_database_resource_principal_details_extended(ctx, **kwargs):

    if 'identity_id' in kwargs:
        kwargs['database_tools_identity_id'] = kwargs['identity_id']
        kwargs.pop('identity_id')

    ctx.invoke(databasetools_cli.update_database_tools_identity_update_database_tools_identity_oracle_database_resource_principal_details, **kwargs)


@cli_util.copy_params_from_generated_command(databasetools_cli.validate_database_tools_identity_credential_validate_database_tools_identity_credential_oracle_database_resource_principal_details, params_to_exclude=['database_tools_identity_id'])
@databasetools_cli.database_tools_identity_group.command(name=databasetools_cli.validate_database_tools_identity_credential_validate_database_tools_identity_credential_oracle_database_resource_principal_details.name, help=databasetools_cli.validate_database_tools_identity_credential_validate_database_tools_identity_credential_oracle_database_resource_principal_details.help)
@cli_util.option('--identity-id', required=True, help=u"""The [OCID] of a Database Tools identity. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'ValidateDatabaseToolsIdentityCredentialResult'})
@cli_util.wrap_exceptions
def validate_database_tools_identity_credential_validate_database_tools_identity_credential_oracle_database_resource_principal_details_extended(ctx, **kwargs):

    if 'identity_id' in kwargs:
        kwargs['database_tools_identity_id'] = kwargs['identity_id']
        kwargs.pop('identity_id')

    ctx.invoke(databasetools_cli.validate_database_tools_identity_credential_validate_database_tools_identity_credential_oracle_database_resource_principal_details, **kwargs)


# oci dbtools database-tools-database-api-gateway-config -> oci dbtools database-api-gateway-config
cli_util.rename_command(databasetools_cli, databasetools_cli.dbtools_root_group, databasetools_cli.database_tools_database_api_gateway_config_group, "database-api-gateway-config")


# oci dbtools database-tools-mcp-server -> oci dbtools mcp-server
cli_util.rename_command(databasetools_cli, databasetools_cli.dbtools_root_group, databasetools_cli.database_tools_mcp_server_group, "mcp-server")


# oci dbtools database-tools-mcp-toolset -> oci dbtools mcp-toolset
cli_util.rename_command(databasetools_cli, databasetools_cli.dbtools_root_group, databasetools_cli.database_tools_mcp_toolset_group, "mcp-toolset")


# oci dbtools database-tools-sql-report -> oci dbtools sql-report
cli_util.rename_command(databasetools_cli, databasetools_cli.dbtools_root_group, databasetools_cli.database_tools_sql_report_group, "sql-report")


# oci dbtools database-tools-mcp-toolset-version-collection -> oci dbtools mcp-toolset-version-collection
cli_util.rename_command(databasetools_cli, databasetools_cli.dbtools_root_group, databasetools_cli.database_tools_mcp_toolset_version_collection_group, "mcp-toolset-version-collection")


# oci dbtools mcp-toolset-version-collection list-database-tools-mcp-toolset-versions -> oci dbtools mcp-toolset-version-collection list-mcp-toolset-version
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_mcp_toolset_version_collection_group, databasetools_cli.list_database_tools_mcp_toolset_versions, "list-mcp-toolset-version")


# oci dbtools database-tools-database-api-gateway-config create-database-tools-database-api-gateway-config-create-database-tools-database-api-gateway-config-default-details -> oci dbtools database-tools-database-api-gateway-config create-database-api-gateway-config-default
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_database_api_gateway_config_group, databasetools_cli.create_database_tools_database_api_gateway_config_create_database_tools_database_api_gateway_config_default_details, "create-database-api-gateway-config-default")


# oci dbtools database-tools-database-api-gateway-config update-database-tools-database-api-gateway-config-update-database-tools-database-api-gateway-config-default-details -> oci dbtools database-tools-database-api-gateway-config update-database-api-gateway-config-default
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_database_api_gateway_config_group, databasetools_cli.update_database_tools_database_api_gateway_config_update_database_tools_database_api_gateway_config_default_details, "update-database-api-gateway-config-default")


# oci dbtools database-tools-database-api-gateway-config add -> oci dbtools database-tools-database-api-gateway-config add-lock
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_database_api_gateway_config_group, databasetools_cli.add_database_tools_database_api_gateway_config_lock, "add-lock")


# oci dbtools database-tools-database-api-gateway-config remove -> oci dbtools database-tools-database-api-gateway-config remove-lock
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_database_api_gateway_config_group, databasetools_cli.remove_database_tools_database_api_gateway_config_lock, "remove-lock")


# oci dbtools database-tools-mcp-server create-database-tools-mcp-server-create-database-tools-mcp-server-default-details -> oci dbtools database-tools-mcp-server create-mcp-server-default
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_mcp_server_group, databasetools_cli.create_database_tools_mcp_server_create_database_tools_mcp_server_default_details, "create-mcp-server-default")


# oci dbtools database-tools-mcp-server update-database-tools-mcp-server-update-database-tools-mcp-server-details-default -> oci dbtools database-tools-mcp-server update-mcp-server-default
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_mcp_server_group, databasetools_cli.update_database_tools_mcp_server_update_database_tools_mcp_server_details_default, "update-mcp-server-default")


# oci dbtools database-tools-mcp-server add -> oci dbtools database-tools-mcp-server add-lock
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_mcp_server_group, databasetools_cli.add_database_tools_mcp_server_lock, "add-lock")


# oci dbtools database-tools-mcp-server remove -> oci dbtools database-tools-mcp-server remove-lock
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_mcp_server_group, databasetools_cli.remove_database_tools_mcp_server_lock, "remove-lock")


# oci dbtools database-tools-mcp-toolset create-database-tools-mcp-toolset-create-database-tools-mcp-toolset-built-in-sql-tools-details -> oci dbtools database-tools-mcp-toolset create-mcp-toolset-built-in-sql-tools
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_mcp_toolset_group, databasetools_cli.create_database_tools_mcp_toolset_create_database_tools_mcp_toolset_built_in_sql_tools_details, "create-mcp-toolset-built-in-sql-tools")


# oci dbtools database-tools-mcp-toolset create-database-tools-mcp-toolset-create-database-tools-mcp-toolset-custom-sql-tool-details -> oci dbtools database-tools-mcp-toolset create-mcp-toolset-custom-sql-tool
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_mcp_toolset_group, databasetools_cli.create_database_tools_mcp_toolset_create_database_tools_mcp_toolset_custom_sql_tool_details, "create-mcp-toolset-custom-sql-tool")


# oci dbtools database-tools-mcp-toolset create-database-tools-mcp-toolset-create-database-tools-mcp-toolset-customizable-reporting-tools-details -> oci dbtools database-tools-mcp-toolset create-mcp-toolset-customizable-reporting-tools
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_mcp_toolset_group, databasetools_cli.create_database_tools_mcp_toolset_create_database_tools_mcp_toolset_customizable_reporting_tools_details, "create-mcp-toolset-customizable-reporting-tools")


# oci dbtools database-tools-mcp-toolset create-database-tools-mcp-toolset-create-database-tools-mcp-toolset-gen-ai-sql-assistant-details -> oci dbtools database-tools-mcp-toolset create-mcp-toolset-gen-ai-sql-assistant
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_mcp_toolset_group, databasetools_cli.create_database_tools_mcp_toolset_create_database_tools_mcp_toolset_gen_ai_sql_assistant_details, "create-mcp-toolset-gen-ai-sql-assistant")


# oci dbtools database-tools-mcp-toolset update-database-tools-mcp-toolset-update-database-tools-mcp-toolset-built-in-sql-tools-details -> oci dbtools database-tools-mcp-toolset update-mcp-toolset-built-in-sql-tools
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_mcp_toolset_group, databasetools_cli.update_database_tools_mcp_toolset_update_database_tools_mcp_toolset_built_in_sql_tools_details, "update-mcp-toolset-built-in-sql-tools")


# oci dbtools database-tools-mcp-toolset update-database-tools-mcp-toolset-update-database-tools-mcp-toolset-custom-sql-tool-details -> oci dbtools database-tools-mcp-toolset update-mcp-toolset-custom-sql-tool
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_mcp_toolset_group, databasetools_cli.update_database_tools_mcp_toolset_update_database_tools_mcp_toolset_custom_sql_tool_details, "update-mcp-toolset-custom-sql-tool")


# oci dbtools database-tools-mcp-toolset update-database-tools-mcp-toolset-update-database-tools-mcp-toolset-customizable-reporting-tools-details -> oci dbtools database-tools-mcp-toolset update-mcp-toolset-customizable-reporting-tools
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_mcp_toolset_group, databasetools_cli.update_database_tools_mcp_toolset_update_database_tools_mcp_toolset_customizable_reporting_tools_details, "update-mcp-toolset-customizable-reporting-tools")


# oci dbtools database-tools-mcp-toolset update-database-tools-mcp-toolset-update-database-tools-mcp-toolset-gen-ai-sql-assistant-details -> oci dbtools database-tools-mcp-toolset update-mcp-toolset-gen-ai-sql-assistant
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_mcp_toolset_group, databasetools_cli.update_database_tools_mcp_toolset_update_database_tools_mcp_toolset_gen_ai_sql_assistant_details, "update-mcp-toolset-gen-ai-sql-assistant")


# oci dbtools database-tools-mcp-toolset add -> oci dbtools database-tools-mcp-toolset add-lock
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_mcp_toolset_group, databasetools_cli.add_database_tools_mcp_toolset_lock, "add-lock")


# oci dbtools database-tools-mcp-toolset remove -> oci dbtools database-tools-mcp-toolset remove-lock
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_mcp_toolset_group, databasetools_cli.remove_database_tools_mcp_toolset_lock, "remove-lock")


# oci dbtools database-tools-sql-report create-database-tools-sql-report-create-database-tools-sql-report-oracle-database-details -> oci dbtools database-tools-sql-report create-sql-report-oracle-database
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_sql_report_group, databasetools_cli.create_database_tools_sql_report_create_database_tools_sql_report_oracle_database_details, "create-sql-report-oracle-database")


# oci dbtools database-tools-sql-report update-database-tools-sql-report-update-database-tools-sql-report-details-oracle-database -> oci dbtools database-tools-sql-report update-sql-report-oracle-database
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_sql_report_group, databasetools_cli.update_database_tools_sql_report_update_database_tools_sql_report_details_oracle_database, "update-sql-report-oracle-database")


# oci dbtools database-tools-sql-report add -> oci dbtools database-tools-sql-report add-lock
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_sql_report_group, databasetools_cli.add_database_tools_sql_report_lock, "add-lock")


# oci dbtools database-tools-sql-report remove -> oci dbtools database-tools-sql-report remove-lock
cli_util.rename_command(databasetools_cli, databasetools_cli.database_tools_sql_report_group, databasetools_cli.remove_database_tools_sql_report_lock, "remove-lock")


# Remove create from oci dbtools database-tools-database-api-gateway-config
databasetools_cli.database_tools_database_api_gateway_config_group.commands.pop(databasetools_cli.create_database_tools_database_api_gateway_config.name)


# Remove update from oci dbtools database-tools-database-api-gateway-config
databasetools_cli.database_tools_database_api_gateway_config_group.commands.pop(databasetools_cli.update_database_tools_database_api_gateway_config.name)


# Remove create from oci dbtools database-tools-mcp-server
databasetools_cli.database_tools_mcp_server_group.commands.pop(databasetools_cli.create_database_tools_mcp_server.name)


# Remove update from oci dbtools database-tools-mcp-server
databasetools_cli.database_tools_mcp_server_group.commands.pop(databasetools_cli.update_database_tools_mcp_server.name)


# Remove create from oci dbtools database-tools-mcp-toolset
databasetools_cli.database_tools_mcp_toolset_group.commands.pop(databasetools_cli.create_database_tools_mcp_toolset.name)


# Remove update from oci dbtools database-tools-mcp-toolset
databasetools_cli.database_tools_mcp_toolset_group.commands.pop(databasetools_cli.update_database_tools_mcp_toolset.name)


# Remove create from oci dbtools database-tools-sql-report
databasetools_cli.database_tools_sql_report_group.commands.pop(databasetools_cli.create_database_tools_sql_report.name)


# Remove update from oci dbtools database-tools-sql-report
databasetools_cli.database_tools_sql_report_group.commands.pop(databasetools_cli.update_database_tools_sql_report.name)
