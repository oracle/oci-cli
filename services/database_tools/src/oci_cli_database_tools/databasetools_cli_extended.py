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
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a DatabaseToolsConnection.""")
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
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a DatabaseToolsConnection.""")
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
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a DatabaseToolsConnection.""")
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
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a DatabaseToolsConnection.""")
@cli_util.option('--user-password-secret-id', help="""The [OCID] of the secret containing the user password.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'UpdateDatabaseToolsRelatedResourceDetails'}, 'user-password': {'module': 'database_tools', 'class': 'DatabaseToolsUserPasswordDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreDetails]'}})
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


@cli_util.copy_params_from_generated_command(databasetools_cli.create_database_tools_connection_create_database_tools_connection_oracle_database_details, params_to_exclude=['user_password'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.create_database_tools_connection_create_database_tools_connection_oracle_database_details.name, help=databasetools_cli.create_database_tools_connection_create_database_tools_connection_oracle_database_details.help)
@cli_util.option('--user-password-secret-id', required=True, help="""The [OCID] of the secret containing the user password.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'CreateDatabaseToolsRelatedResourceDetails'}, 'user-password': {'module': 'database_tools', 'class': 'DatabaseToolsUserPasswordDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreDetails]'}})
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
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a DatabaseToolsConnection.""")
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
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of a DatabaseToolsPrivateEndpoint. [required]""")
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
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of a DatabaseToolsPrivateEndpoint. [required]""")
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
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of a DatabaseToolsPrivateEndpoint. [required]""")
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
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of a DatabaseToolsPrivateEndpoint. [required]""")
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'CreateDatabaseToolsRelatedResourceDetails'}, 'user-password': {'module': 'database_tools', 'class': 'DatabaseToolsUserPasswordDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreDetails]'}})
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


@cli_util.copy_params_from_generated_command(databasetools_cli.update_database_tools_connection_update_database_tools_connection_my_sql_details, params_to_exclude=['database_tools_connection_id'])
@databasetools_cli.database_tools_connection_group.command(name=databasetools_cli.update_database_tools_connection_update_database_tools_connection_my_sql_details.name, help=databasetools_cli.update_database_tools_connection_update_database_tools_connection_my_sql_details.help)
@cli_util.option('--connection-id', required=True, help=u"""The [OCID] of a Database Tools connection.""")
@cli_util.option('--user-password-secret-id', help="""The [OCID] of the secret containing the user password.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'UpdateDatabaseToolsRelatedResourceMySqlDetails'}, 'user-password': {'module': 'database_tools', 'class': 'DatabaseToolsUserPasswordDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreMySqlDetails]'}})
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
