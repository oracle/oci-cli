# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


import click
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli.cli_util import get_param, copy_help_from_generated_code
from services.data_integration.src.oci_cli_data_integration.generated import dataintegration_cli

dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_object_storage.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_atp.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_adwc.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_oracle.name)

create_connection_args = [
    'workspace_id',
    'name',
    'identifier',
    'key',
    'model_version',
    'parent_ref',
    'description',
    'object_status',
    'connection_properties',
    'registry_metadata'
]


@cli_util.copy_params_from_generated_command(dataintegration_cli.create_connection)
@cli_util.option('--username', help=copy_help_from_generated_code(dataintegration_cli.create_connection_create_connection_from_oracle, 'username', remove_required=True))
@cli_util.option('--password', help=copy_help_from_generated_code(dataintegration_cli.create_connection_create_connection_from_oracle, 'password', remove_required=True))
@cli_util.option('--credential-file-content', help=copy_help_from_generated_code(dataintegration_cli.create_connection_create_connection_from_object_storage, 'credential_file_content', remove_required=True))
@cli_util.option('--user-id', help=copy_help_from_generated_code(dataintegration_cli.create_connection_create_connection_from_object_storage, 'user_id', remove_required=True))
@cli_util.option('--finger-print', help=copy_help_from_generated_code(dataintegration_cli.create_connection_create_connection_from_object_storage, 'finger_print', remove_required=True))
@cli_util.option('--pass-phrase', help=copy_help_from_generated_code(dataintegration_cli.create_connection_create_connection_from_object_storage, 'pass_phrase', remove_required=True))
@dataintegration_cli.connection_group.command(name=cli_util.override('data_integration.create_connection.command_name', 'create'), help=u"""Creates a connection under an existing data asset.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_extended(ctx, **kwargs):
    common_args = dict([(k, kwargs[k]) for k in create_connection_args])
    if 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_ADWC_CONNECTION':
        adwc_args = {}
        adwc_args.update(common_args)
        adwc_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_adwc, **adwc_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_ATP_CONNECTION':
        atp_args = {}
        atp_args.update(common_args)
        atp_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_atp, **atp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_OBJECT_STORAGE_CONNECTION':
        object_storage_args = {}
        object_storage_args.update(common_args)
        object_storage_args.update(
            {
                'credential_file_content': kwargs['credential_file_content'],
                'user_id': kwargs['user_id'],
                'finger_print': kwargs['finger_print'],
                'pass_phrase': kwargs['pass_phrase']
            }
        )
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_object_storage, **object_storage_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLEDB_CONNECTION':
        oracle_db_args = {}
        oracle_db_args.update(common_args)
        oracle_db_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_oracle, **oracle_db_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'MYSQL_CONNECTION':
        mysql_args = {}
        mysql_args.update(common_args)
        mysql_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_my_sql, **mysql_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'GENERIC_JDBC_CONNECTION':
        generic_jdbc_args = {}
        generic_jdbc_args.update(common_args)
        generic_jdbc_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_jdbc, **generic_jdbc_args)


dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_object_storage.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_atp.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_adwc.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_oracle.name)

update_connection_args = [
    'workspace_id',
    'connection_key',
    'key',
    'object_version',
    'model_version',
    'parent_ref',
    'name',
    'description',
    'object_status',
    'identifier',
    'connection_properties',
    'registry_metadata',
    'if_match',
    'force'
]


@cli_util.copy_params_from_generated_command(dataintegration_cli.update_connection)
@cli_util.option('--username', help=copy_help_from_generated_code(dataintegration_cli.update_connection_update_connection_from_oracle, 'username', remove_required=True))
@cli_util.option('--password', help=copy_help_from_generated_code(dataintegration_cli.update_connection_update_connection_from_oracle, 'password', remove_required=True))
@cli_util.option('--credential-file-content', help=copy_help_from_generated_code(dataintegration_cli.update_connection_update_connection_from_object_storage, 'credential_file_content', remove_required=True))
@cli_util.option('--user-id', help=copy_help_from_generated_code(dataintegration_cli.update_connection_update_connection_from_object_storage, 'user_id', remove_required=True))
@cli_util.option('--finger-print', help=copy_help_from_generated_code(dataintegration_cli.update_connection_update_connection_from_object_storage, 'finger_print', remove_required=True))
@cli_util.option('--pass-phrase', help=copy_help_from_generated_code(dataintegration_cli.update_connection_update_connection_from_object_storage, 'pass_phrase', remove_required=True))
@cli_util.copy_params_from_generated_command(dataintegration_cli.update_connection_update_connection_from_adwc, update_connection_args)
@cli_util.copy_params_from_generated_command(dataintegration_cli.update_connection_update_connection_from_object_storage, update_connection_args)
@dataintegration_cli.connection_group.command(name=cli_util.override('data_integration.update_connection.command_name', 'update'), help=u"""Updates a connection under a data asset.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection_extended(ctx, **kwargs):
    common_args = dict([(k, kwargs[k]) for k in update_connection_args])
    if 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_ADWC_CONNECTION':
        adwc_args = {}
        adwc_args.update(common_args)
        adwc_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_adwc, **adwc_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_ATP_CONNECTION':
        atp_args = {}
        atp_args.update(common_args)
        atp_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_atp, **atp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_OBJECT_STORAGE_CONNECTION':
        object_storage_args = {}
        object_storage_args.update(common_args)
        object_storage_args.update(
            {
                'credential_file_content': kwargs['credential_file_content'],
                'user_id': kwargs['user_id'],
                'finger_print': kwargs['finger_print'],
                'pass_phrase': kwargs['pass_phrase']
            }
        )
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_object_storage, **object_storage_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLEDB_CONNECTION':
        oracle_db_args = {}
        oracle_db_args.update(common_args)
        oracle_db_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_oracle, **oracle_db_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'MYSQL_CONNECTION':
        mysql_args = {}
        mysql_args.update(common_args)
        mysql_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_my_sql, **mysql_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'GENERIC_JDBC_CONNECTION':
        generic_jdbc_args = {}
        generic_jdbc_args.update(common_args)
        generic_jdbc_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_jdbc, **generic_jdbc_args)


dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_object_storage.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_atp.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_adwc.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_oracle.name)

create_data_asset_args = [
    'workspace_id',
    'name',
    'identifier',
    'key',
    'model_version',
    'description',
    'object_status',
    'external_key',
    'asset_properties',
    'registry_metadata'
]


@cli_util.copy_params_from_generated_command(dataintegration_cli.create_data_asset)
@cli_util.option('--service-name', help=copy_help_from_generated_code(dataintegration_cli.create_data_asset_create_data_asset_from_adwc, 'service_name', remove_required=True))
@cli_util.option('--driver-class', help=copy_help_from_generated_code(dataintegration_cli.create_data_asset_create_data_asset_from_adwc, 'driver_class', remove_required=True))
@cli_util.option('--credential-file-content', help=copy_help_from_generated_code(dataintegration_cli.create_data_asset_create_data_asset_from_adwc, 'credential_file_content', remove_required=True))
@cli_util.option('--default-connection', help=copy_help_from_generated_code(dataintegration_cli.create_data_asset_create_data_asset_from_adwc, 'default_connection', remove_required=True))
@cli_util.option('--url', help=copy_help_from_generated_code(dataintegration_cli.create_data_asset_create_data_asset_from_object_storage, 'url', remove_required=True))
@cli_util.option('--tenancy-id', help=copy_help_from_generated_code(dataintegration_cli.create_data_asset_create_data_asset_from_object_storage, 'tenancy_id', remove_required=True))
@cli_util.option('--namespace', help=copy_help_from_generated_code(dataintegration_cli.create_data_asset_create_data_asset_from_object_storage, 'namespace', remove_required=True))
@cli_util.option('--host', help=copy_help_from_generated_code(dataintegration_cli.create_data_asset_create_data_asset_from_oracle, 'host', remove_required=True))
@cli_util.option('--port', help=copy_help_from_generated_code(dataintegration_cli.create_data_asset_create_data_asset_from_oracle, 'port', remove_required=True))
@cli_util.option('--sid', help=copy_help_from_generated_code(dataintegration_cli.create_data_asset_create_data_asset_from_oracle, 'sid', remove_required=True))
@cli_util.option('--data-asset-type', help=u"""The data asset type for the generic JDBC data asset.""")
@dataintegration_cli.data_asset_group.command(name=cli_util.override('data_integration.create_data_asset.command_name', 'create'), help=u"""Creates a data asset with default connection.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromObjectStorage'}}, output_type={'module': 'data_integration', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def create_data_asset_extended(ctx, **kwargs):
    adwc_args = {}
    common_args = dict([(k, kwargs[k]) for k in create_data_asset_args])
    if 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_ADWC_DATA_ASSET':
        adwc_args.update(common_args)
        adwc_args.update(
            {
                'service_name': kwargs['service_name'],
                'driver_class': kwargs['driver_class'],
                'credential_file_content': kwargs['credential_file_content'],
                'default_connection': kwargs['default_connection']
            }
        )
        ctx.invoke(dataintegration_cli.create_data_asset_create_data_asset_from_adwc, **adwc_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_ATP_DATA_ASSET':
        atp_args = {}
        atp_args.update(common_args)
        atp_args.update(
            {
                'service_name': kwargs['service_name'],
                'driver_class': kwargs['driver_class'],
                'credential_file_content': kwargs['credential_file_content'],
                'default_connection': kwargs['default_connection']
            }
        )
        ctx.invoke(dataintegration_cli.create_data_asset_create_data_asset_from_atp, **atp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_OBJECT_STORAGE_DATA_ASSET':
        object_storage_args = {}
        object_storage_args.update(common_args)
        object_storage_args.update(
            {
                'url': kwargs['url'],
                'tenancy_id': kwargs['tenancy_id'],
                'namespace': kwargs['namespace'],
                'default_connection': kwargs['default_connection']
            }
        )
        ctx.invoke(dataintegration_cli.create_data_asset_create_data_asset_from_object_storage, **object_storage_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_DATA_ASSET':
        oracle_db_args = {}
        oracle_db_args.update(common_args)
        oracle_db_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'service_name': kwargs['service_name'],
                'driver_class': kwargs['driver_class'],
                'sid': kwargs['sid'],
                'credential_file_content': kwargs['credential_file_content'],
                'default_connection': kwargs['default_connection']
            }
        )
        ctx.invoke(dataintegration_cli.create_data_asset_create_data_asset_from_oracle, **oracle_db_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'MYSQL_DATA_ASSET':
        mysql_args = {}
        mysql_args.update(common_args)
        mysql_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'service_name': kwargs['service_name'],
                'default_connection': kwargs['default_connection']
            }
        )
        ctx.invoke(dataintegration_cli.create_data_asset_create_data_asset_from_my_sql, **mysql_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'GENERIC_JDBC_DATA_ASSET':
        generic_jdbc_args = {}
        generic_jdbc_args.update(common_args)
        generic_jdbc_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'data_asset_type': kwargs['data_asset_type'],
                'default_connection': kwargs['default_connection']
            }
        )
        ctx.invoke(dataintegration_cli.create_data_asset_create_data_asset_from_jdbc, **generic_jdbc_args)


dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_object_storage.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_atp.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_adwc.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_oracle.name)


update_data_asset_args = [
    'force',
    'workspace_id',
    'data_asset_key',
    'key',
    'object_version',
    'model_version',
    'name',
    'description',
    'object_status',
    'identifier',
    'external_key',
    'asset_properties',
    'registry_metadata',
    'if_match'
]


@cli_util.copy_params_from_generated_command(dataintegration_cli.update_data_asset)
@cli_util.option('--service-name', help=copy_help_from_generated_code(dataintegration_cli.update_data_asset_update_data_asset_from_adwc, 'service_name', remove_required=True))
@cli_util.option('--driver-class', help=copy_help_from_generated_code(dataintegration_cli.update_data_asset_update_data_asset_from_adwc, 'driver_class', remove_required=True))
@cli_util.option('--credential-file-content', help=copy_help_from_generated_code(dataintegration_cli.update_data_asset_update_data_asset_from_adwc, 'credential_file_content', remove_required=True))
@cli_util.option('--default-connection', help=copy_help_from_generated_code(dataintegration_cli.update_data_asset_update_data_asset_from_adwc, 'default_connection', remove_required=True))
@cli_util.option('--url', help=copy_help_from_generated_code(dataintegration_cli.update_data_asset_update_data_asset_from_object_storage, 'url', remove_required=True))
@cli_util.option('--tenancy-id', help=copy_help_from_generated_code(dataintegration_cli.update_data_asset_update_data_asset_from_object_storage, 'tenancy_id', remove_required=True))
@cli_util.option('--namespace', help=copy_help_from_generated_code(dataintegration_cli.update_data_asset_update_data_asset_from_object_storage, 'namespace', remove_required=True))
@cli_util.option('--host', help=copy_help_from_generated_code(dataintegration_cli.update_data_asset_update_data_asset_from_oracle, 'host', remove_required=True))
@cli_util.option('--port', help=copy_help_from_generated_code(dataintegration_cli.update_data_asset_update_data_asset_from_oracle, 'port', remove_required=True))
@cli_util.option('--sid', help=copy_help_from_generated_code(dataintegration_cli.update_data_asset_update_data_asset_from_oracle, 'sid', remove_required=True))
@cli_util.option('--data-asset-type', help=u"""The data asset type for the generic JDBC data asset.""")
@dataintegration_cli.data_asset_group.command(name=cli_util.override('data_integration.update_data_asset.command_name', 'update'), help=u"""Updates a specific data asset with default connection.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromObjectStorage'}}, output_type={'module': 'data_integration', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def update_data_asset_extended(ctx, **kwargs):
    common_args = dict([(k, kwargs[k]) for k in update_data_asset_args])
    if 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_ADWC_DATA_ASSET':
        adwc_args = {}
        adwc_args.update(common_args)
        adwc_args.update(
            {
                'service_name': kwargs['service_name'],
                'driver_class': kwargs['driver_class'],
                'credential_file_content': kwargs['credential_file_content'],
                'default_connection': kwargs['default_connection']
            }
        )
        ctx.invoke(dataintegration_cli.update_data_asset_update_data_asset_from_adwc, **adwc_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_ATP_DATA_ASSET':
        atp_args = {}
        atp_args.update(common_args)
        atp_args.update(
            {
                'service_name': kwargs['service_name'],
                'driver_class': kwargs['driver_class'],
                'credential_file_content': kwargs['credential_file_content'],
                'default_connection': kwargs['default_connection']
            }
        )
        ctx.invoke(dataintegration_cli.update_data_asset_update_data_asset_from_atp, **atp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_OBJECT_STORAGE_DATA_ASSET':
        object_storage_args = {}
        object_storage_args.update(common_args)
        object_storage_args.update(
            {
                'url': kwargs['url'],
                'tenancy_id': kwargs['tenancy_id'],
                'namespace': kwargs['namespace'],
                'default_connection': kwargs['default_connection']
            }
        )
        ctx.invoke(dataintegration_cli.update_data_asset_update_data_asset_from_object_storage, **object_storage_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_DATA_ASSET':
        oracle_db_args = {}
        oracle_db_args.update(common_args)
        oracle_db_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'service_name': kwargs['service_name'],
                'driver_class': kwargs['driver_class'],
                'sid': kwargs['sid'],
                'credential_file_content': kwargs['credential_file_content'],
                'default_connection': kwargs['default_connection']
            }
        )
        ctx.invoke(dataintegration_cli.update_data_asset_update_data_asset_from_oracle, **oracle_db_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'MYSQL_DATA_ASSET':
        mysql_args = {}
        mysql_args.update(common_args)
        mysql_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'service_name': kwargs['service_name'],
                'default_connection': kwargs['default_connection']
            }
        )
        ctx.invoke(dataintegration_cli.update_data_asset_update_data_asset_from_my_sql, **mysql_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'GENERIC_JDBC_DATA_ASSET':
        generic_jdbc_args = {}
        generic_jdbc_args.update(common_args)
        generic_jdbc_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'data_asset_type': kwargs['data_asset_type'],
                'default_connection': kwargs['default_connection']
            }
        )
        ctx.invoke(dataintegration_cli.update_data_asset_update_data_asset_from_jdbc, **generic_jdbc_args)


@cli_util.copy_params_from_generated_command(dataintegration_cli.delete_connection_validation, params_to_exclude=['connection_validation_key'])
@cli_util.option('--con-validation-key', required=True, type=get_param(dataintegration_cli.delete_connection_validation, 'connection_validation_key').type, help=get_param(dataintegration_cli.delete_connection_validation, 'connection_validation_key').help)
@dataintegration_cli.connection_validation_group.command(name=cli_util.override('data_integration.delete_connection_validation.command_name', 'delete'), help=u"""Successfully accepted the delete request. The connection validation will be deleted.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_connection_validation_extended(ctx, **kwargs):
    if 'con_validation_key' in kwargs:
        kwargs['connection_validation_key'] = kwargs['con_validation_key']
        kwargs.pop('con_validation_key')
    ctx.invoke(dataintegration_cli.delete_connection_validation, **kwargs)


@cli_util.copy_params_from_generated_command(dataintegration_cli.get_connection_validation, params_to_exclude=['connection_validation_key'])
@cli_util.option('--con-validation-key', required=True, type=get_param(dataintegration_cli.get_connection_validation, 'connection_validation_key').type, help=get_param(dataintegration_cli.get_connection_validation, 'connection_validation_key').help)
@dataintegration_cli.connection_validation_group.command(name=cli_util.override('data_integration.get_connection_validation.command_name', 'get'), help=u"""Retrieves a connection validation using the specified identifier.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'ConnectionValidation'})
@cli_util.wrap_exceptions
def get_connection_validation_extended(ctx, **kwargs):
    if 'con_validation_key' in kwargs:
        kwargs['connection_validation_key'] = kwargs['con_validation_key']
        kwargs.pop('con_validation_key')
    ctx.invoke(dataintegration_cli.get_connection_validation, **kwargs)


@cli_util.copy_params_from_generated_command(dataintegration_cli.delete_data_flow_validation, params_to_exclude=['data_flow_validation_key'])
@cli_util.option('--df-validation-key', required=True, type=get_param(dataintegration_cli.delete_data_flow_validation, 'data_flow_validation_key').type, help=get_param(dataintegration_cli.delete_data_flow_validation, 'data_flow_validation_key').help)
@dataintegration_cli.data_flow_validation_group.command(name=cli_util.override('data_integration.delete_data_flow_validation.command_name', 'delete'), help=u"""Removes a data flow validation using the specified identifier.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_data_flow_validation_extended(ctx, **kwargs):
    if 'df_validation_key' in kwargs:
        kwargs['data_flow_validation_key'] = kwargs['df_validation_key']
        kwargs.pop('df_validation_key')
    ctx.invoke(dataintegration_cli.delete_data_flow_validation, **kwargs)


@cli_util.copy_params_from_generated_command(dataintegration_cli.get_data_flow_validation, params_to_exclude=['data_flow_validation_key'])
@cli_util.option('--df-validation-key', required=True, type=get_param(dataintegration_cli.get_data_flow_validation, 'data_flow_validation_key').type, help=get_param(dataintegration_cli.get_data_flow_validation, 'data_flow_validation_key').help)
@dataintegration_cli.data_flow_validation_group.command(name=cli_util.override('data_integration.get_data_flow_validation.command_name', 'get'), help=u"""Retrieves a data flow validation using the specified identifier.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'DataFlowValidation'})
@cli_util.wrap_exceptions
def get_data_flow_validation_extended(ctx, **kwargs):
    if 'df_validation_key' in kwargs:
        kwargs['data_flow_validation_key'] = kwargs['df_validation_key']
        kwargs.pop('df_validation_key')
    ctx.invoke(dataintegration_cli.get_data_flow_validation, **kwargs)


@cli_util.copy_params_from_generated_command(dataintegration_cli.create_workspace, params_to_exclude=['is_private_network_enabled'])
@cli_util.option('--is-private-network', required=True, type=get_param(dataintegration_cli.create_workspace, 'is_private_network_enabled').type, help=get_param(dataintegration_cli.create_workspace, 'is_private_network_enabled').help)
@dataintegration_cli.workspace_group.command(name=cli_util.override('data_integration.create_workspace.command_name', 'create'), help=u"""Creates a new Data Integration Workspace ready for performing data integration.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_integration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_workspace_extended(ctx, **kwargs):
    if 'is_private_network' in kwargs:
        kwargs['is_private_network_enabled'] = kwargs['is_private_network']
        kwargs.pop('is_private_network')
    ctx.invoke(dataintegration_cli.create_workspace, **kwargs)


dataintegration_cli.data_entity_group.commands.pop(dataintegration_cli.create_entity_shape.name)
cli_util.rename_command(dataintegration_cli, dataintegration_cli.data_entity_group, dataintegration_cli.create_entity_shape_create_entity_shape_from_file, "create-entity-shape-from-file")

dataintegration_cli.task_validation_group.commands.pop(dataintegration_cli.create_task_validation.name)
cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_validation_group, dataintegration_cli.create_task_validation_create_task_validation_from_integration_task, "create-from-integration-task")
cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_validation_group, dataintegration_cli.create_task_validation_create_task_validation_from_data_loader_task, "create-from-data-loader-task")

dataintegration_cli.task_group.commands.pop(dataintegration_cli.create_task.name)
cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_group, dataintegration_cli.create_task_create_task_from_integration_task, "create-integration-task")
cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_group, dataintegration_cli.create_task_create_task_from_data_loader_task, "create-data-loader-task")

dataintegration_cli.task_group.commands.pop(dataintegration_cli.update_task.name)
cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_group, dataintegration_cli.update_task_update_task_from_integration_task, "update-integration-task")
cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_group, dataintegration_cli.update_task_update_task_from_data_loader_task, "update-data-loader-task")


dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_oracle.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_adwc.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_atp.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_object_storage.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_atp.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_adwc.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_oracle.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_object_storage.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_my_sql.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_jdbc.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_my_sql.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_jdbc.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_jdbc.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_my_sql.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_jdbc.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_my_sql.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_jdbc.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_my_sql.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_jdbc.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_my_sql.name)
