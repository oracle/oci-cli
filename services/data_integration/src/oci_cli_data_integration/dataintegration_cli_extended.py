# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli.cli_util import get_param, copy_help_from_generated_code
from services.data_integration.src.oci_cli_data_integration.generated import dataintegration_cli
from oci_cli import custom_types  # noqa: F401

dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_object_storage.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_atp.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_adwc.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_oracle.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_lake.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_rest_basic_auth.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_rest_no_auth.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_hdfs.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_my_sql_heat_wave.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_oracle_ebs.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_oracle_people_soft.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_oracle_siebel.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_o_auth2.name)

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
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_LAKEHOUSE_CONNECTION':
        oracle_lakehouse_args = {}
        oracle_lakehouse_args.update(common_args)
        oracle_lakehouse_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_lake, **oracle_db_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_REST_BASIC_AUTH_CONNECTION':
        oracle_rest_auth_args = {}
        oracle_rest_auth_args.update(common_args)
        oracle_rest_auth_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_rest_basic_auth, **oracle_db_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_REST_NO_AUTH_CONNECTION':
        oracle_rest_no_auth_args = {}
        oracle_rest_no_auth_args.update(common_args)
        oracle_rest_no_auth_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_rest_no_auth, **oracle_db_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'HDFS_CONNECTION':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'hdfs_principal': kwargs['hdfs_principal'],
                'data_node_principal': kwargs['data_node_principal'],
                'name_node_principal': kwargs['name_node_principal'],
                'connection_properties': kwargs['connection_properties']
            }
        )
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_hdfs, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'MYSQL_HEATWAVE_CONNECTION':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password'],
                'connection_properties': kwargs['connection_properties']
            }
        )
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_my_sql_heat_wave, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_OEBS_CONNECTION':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password'],
                'connection_properties': kwargs['connection_properties']
            }
        )
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_oracle_ebs, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_PEOPLESOFT_CONNECTION':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password'],
                'connection_properties': kwargs['connection_properties']
            }
        )
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_oracle_people_soft, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_SIEBEL_CONNECTION':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password'],
                'connection_properties': kwargs['connection_properties']
            }
        )
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_oracle_siebel, **temp_args)
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_rest_no_auth, **oracle_rest_no_auth_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'OAUTH2_CONNECTION':
        oracle_o_auth2_auth_args = {}
        oracle_o_auth2_auth_args.update(common_args)
        oracle_o_auth2_auth_args.update(
            {
                'access_token_url': kwargs['access_token_url'],
                'client_id': kwargs['client_id'],
                'client_secret': kwargs['client_secret'],
                'scope': kwargs['scope']
            }
        )
        ctx.invoke(dataintegration_cli.create_connection_create_connection_from_o_auth2, **oracle_o_auth2_auth_args)


dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_object_storage.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_atp.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_adwc.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_oracle.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_lake.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_rest_basic_auth.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_rest_no_auth.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_hdfs.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_my_sql_heat_wave.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_oracle_ebs.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_oracle_people_soft.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_oracle_siebel.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_o_auth2.name)

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
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_LAKEHOUSE_CONNECTION':
        oracle_lakehouse_args = {}
        oracle_lakehouse_args.update(common_args)
        oracle_lakehouse_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_lake, **oracle_db_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_REST_BASIC_AUTH_CONNECTION':
        oracle_rest_auth_args = {}
        oracle_rest_auth_args.update(common_args)
        oracle_rest_auth_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_rest_basic_auth, **oracle_db_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_REST_NO_AUTH_CONNECTION':
        oracle_rest_no_auth_args = {}
        oracle_rest_no_auth_args.update(common_args)
        oracle_rest_no_auth_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password']
            }
        )
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_rest_no_auth, **oracle_db_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'HDFS_CONNECTION':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'hdfs_principal': kwargs['hdfs_principal'],
                'data_node_principal': kwargs['data_node_principal'],
                'name_node_principal': kwargs['name_node_principal'],
                'connection_properties': kwargs['connection_properties']
            }
        )
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_hdfs, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'MYSQL_HEATWAVE_CONNECTION':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password'],
                'connection_properties': kwargs['connection_properties']
            }
        )
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_my_sql_heat_wave, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_OEBS_CONNECTION':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password'],
                'connection_properties': kwargs['connection_properties']
            }
        )
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_oracle_ebs, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_PEOPLESOFT_CONNECTION':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password'],
                'connection_properties': kwargs['connection_properties']
            }
        )
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_oracle_people_soft, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_SIEBEL_CONNECTION':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'username': kwargs['username'],
                'password': kwargs['password'],
                'connection_properties': kwargs['connection_properties']
            }
        )
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_oracle_siebel, **temp_args)
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_rest_no_auth, **oracle_rest_no_auth_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'OAUTH2_CONNECTION':
        oracle_o_auth2_auth_args = {}
        oracle_o_auth2_auth_args.update(common_args)
        oracle_o_auth2_auth_args.update(
            {
                'access_token_url': kwargs['access_token_url'],
                'client_id': kwargs['client_id'],
                'client_secret': kwargs['client_secret'],
                'scope': kwargs['scope']
            }
        )
        ctx.invoke(dataintegration_cli.update_connection_update_connection_from_o_auth2, **oracle_o_auth2_auth_args)


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
    elif 'model_type' in kwargs and kwargs['model_type'] == 'HDFS_DATA_ASSET':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'protocol': kwargs['protocol'],
                'default_connection': kwargs['default_connection'],
                'asset-properties': kwargs['asset-properties']
            }
        )
        ctx.invoke(dataintegration_cli.create_data_asset_create_data_asset_from_hdfs, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'MYSQL_HEATWAVE_DATA_ASSET':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'service_name': kwargs['service_name'],
                'default_connection': kwargs['default_connection'],
                'asset-properties': kwargs['asset-properties']
            }
        )
        ctx.invoke(dataintegration_cli.create_data_asset_create_data_asset_from_my_sql_heat_wave, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_OEBS_DATA_ASSET':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'service_name': kwargs['service_name'],
                'default_connection': kwargs['default_connection'],
                'asset-properties': kwargs['asset-properties']
            }
        )
        ctx.invoke(dataintegration_cli.create_data_asset_create_data_asset_from_oracle_ebs, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_PEOPLESOFT_DATA_ASSET':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'service_name': kwargs['service_name'],
                'default_connection': kwargs['default_connection'],
                'asset-properties': kwargs['asset-properties']
            }
        )
        ctx.invoke(dataintegration_cli.create_data_asset_create_data_asset_from_oracle_people_soft, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_SIEBEL_DATA_ASSET':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'service_name': kwargs['service_name'],
                'default_connection': kwargs['default_connection'],
                'asset-properties': kwargs['asset-properties']
            }
        )
        ctx.invoke(dataintegration_cli.create_data_asset_create_data_asset_from_oracle_siebel, **temp_args)


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
    elif 'model_type' in kwargs and kwargs['model_type'] == 'HDFS_DATA_ASSET':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'protocol': kwargs['protocol'],
                'default_connection': kwargs['default_connection'],
                'asset-properties': kwargs['asset-properties']
            }
        )
        ctx.invoke(dataintegration_cli.update_data_asset_update_data_asset_from_hdfs, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'MYSQL_HEATWAVE_DATA_ASSET':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'service_name': kwargs['service_name'],
                'default_connection': kwargs['default_connection'],
                'asset-properties': kwargs['asset-properties']
            }
        )
        ctx.invoke(dataintegration_cli.update_data_asset_update_data_asset_from_my_sql_heat_wave, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_OEBS_DATA_ASSET':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'service_name': kwargs['service_name'],
                'default_connection': kwargs['default_connection'],
                'asset-properties': kwargs['asset-properties']
            }
        )
        ctx.invoke(dataintegration_cli.update_data_asset_update_data_asset_from_oracle_ebs, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_PEOPLESOFT_DATA_ASSET':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'service_name': kwargs['service_name'],
                'default_connection': kwargs['default_connection'],
                'asset-properties': kwargs['asset-properties']
            }
        )
        ctx.invoke(dataintegration_cli.update_data_asset_update_data_asset_from_oracle_people_soft, **temp_args)
    elif 'model_type' in kwargs and kwargs['model_type'] == 'ORACLE_SIEBEL_DATA_ASSET':
        temp_args = {}
        temp_args.update(common_args)
        temp_args.update(
            {
                'host': kwargs['host'],
                'port': kwargs['port'],
                'service_name': kwargs['service_name'],
                'default_connection': kwargs['default_connection'],
                'asset-properties': kwargs['asset-properties']
            }
        )
        ctx.invoke(dataintegration_cli.update_data_asset_update_data_asset_from_oracle_siebel, **temp_args)


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
cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_group, dataintegration_cli.update_task_update_task_from_pipeline_task, "update-pipeline-task")
cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_group, dataintegration_cli.create_task_create_task_from_pipeline_task, "create-pipeline-task")
cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_validation_group, dataintegration_cli.create_task_validation_create_task_validation_from_pipeline_task, "create-from-pipeline-task")


@cli_util.copy_params_from_generated_command(dataintegration_cli.create_task_create_task_from_pipeline_task, params_to_exclude=['config_provider_delegate'])
@cli_util.option('--config-provider', type=get_param(dataintegration_cli.create_task_create_task_from_pipeline_task, 'config_provider_delegate').type, help=get_param(dataintegration_cli.create_task_create_task_from_pipeline_task, 'config_provider_delegate').help)
@dataintegration_cli.task_group.command(name=cli_util.override('data_integration.create_task_create_task_from_pipeline_task.command_name', 'create-task-create-task-from-pipeline-task'), help=u"""Creates a new task ready for performing data integrations. There are specialized types of tasks that include data loader and integration tasks. \n[Command Reference](createTask)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'CreateConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'pipeline': {'module': 'data_integration', 'class': 'Pipeline'}}, output_type={'module': 'data_integration', 'class': 'Task'})
@cli_util.wrap_exceptions
def create_task_create_task_from_pipeline_task_extended(ctx, **kwargs):
    if 'config_provider' in kwargs:
        kwargs['config_provider_delegate'] = kwargs['config_provider']
        kwargs.pop('config_provider')
    ctx.invoke(dataintegration_cli.create_task_create_task_from_pipeline_task, **kwargs)


@cli_util.copy_params_from_generated_command(dataintegration_cli.update_task_update_task_from_pipeline_task, params_to_exclude=['config_provider_delegate'])
@cli_util.option('--config-provider', type=get_param(dataintegration_cli.update_task_update_task_from_pipeline_task, 'config_provider_delegate').type, help=get_param(dataintegration_cli.update_task_update_task_from_pipeline_task, 'config_provider_delegate').help)
@dataintegration_cli.task_group.command(name=cli_util.override('data_integration.update_task_update_task_from_pipeline_task.command_name', 'update-task-update-task-from-pipeline-task'), help=u"""Updates a specific task. For example, you can update the task description or move the task to a different folder by changing the `aggregatorKey` to a different folder in the registry. \n[Command Reference](updateTask)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'pipeline': {'module': 'data_integration', 'class': 'Pipeline'}}, output_type={'module': 'data_integration', 'class': 'Task'})
@cli_util.wrap_exceptions
def update_task_update_task_from_pipeline_task_extended(ctx, **kwargs):
    if 'config_provider' in kwargs:
        kwargs['config_provider_delegate'] = kwargs['config_provider']
        kwargs.pop('config_provider')
    ctx.invoke(dataintegration_cli.update_task_update_task_from_pipeline_task, **kwargs)


@cli_util.copy_params_from_generated_command(dataintegration_cli.create_task_validation_create_task_validation_from_pipeline_task, params_to_exclude=['config_provider_delegate'])
@cli_util.option('--config-provider', type=get_param(dataintegration_cli.create_task_validation_create_task_validation_from_pipeline_task, 'config_provider_delegate').type, help=get_param(dataintegration_cli.create_task_validation_create_task_validation_from_pipeline_task, 'config_provider_delegate').help)
@dataintegration_cli.task_validation_group.command(name=cli_util.override('data_integration.create_task_validation_create_task_validation_from_pipeline_task.command_name', 'create-from-pipeline-task'), help=u"""Validates a specific task. \n[Command Reference](createTaskValidation)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'metadata': {'module': 'data_integration', 'class': 'ObjectMetadata'}, 'pipeline': {'module': 'data_integration', 'class': 'Pipeline'}}, output_type={'module': 'data_integration', 'class': 'TaskValidation'})
@cli_util.wrap_exceptions
def create_task_validation_create_task_validation_from_pipeline_task(ctx, **kwargs):
    if 'config_provider' in kwargs:
        kwargs['config_provider_delegate'] = kwargs['config_provider']
        kwargs.pop('config_provider')
    ctx.invoke(dataintegration_cli.create_task_validation_create_task_validation_from_pipeline_task, **kwargs)


@cli_util.copy_params_from_generated_command(dataintegration_cli.create_schedule, params_to_exclude=['is_daylight_adjustment_enabled'])
@cli_util.option('--is-daylight-adj-enabled', type=get_param(dataintegration_cli.create_schedule, 'is_daylight_adjustment_enabled').type, help=get_param(dataintegration_cli.create_schedule, 'is_daylight_adjustment_enabled').help)
@dataintegration_cli.schedule_group.command(name=cli_util.override('data_integration.create_schedule.command_name', 'create'), help=u"""Endpoint to create a new schedule \n[Command Reference](createSchedule)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'frequency-details': {'module': 'data_integration', 'class': 'AbstractFrequencyDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def create_schedule_extended(ctx, **kwargs):
    if 'is_daylight_adj_enabled' in kwargs:
        kwargs['is_daylight_adjustment_enabled'] = kwargs['is_daylight_adj_enabled']
        kwargs.pop('is_daylight_adj_enabled')
    ctx.invoke(dataintegration_cli.create_schedule, **kwargs)


@cli_util.copy_params_from_generated_command(dataintegration_cli.update_schedule, params_to_exclude=['is_daylight_adjustment_enabled'])
@cli_util.option('--is-daylight-adj-enabled', type=get_param(dataintegration_cli.update_schedule, 'is_daylight_adjustment_enabled').type, help=get_param(dataintegration_cli.update_schedule, 'is_daylight_adjustment_enabled').help)
@dataintegration_cli.schedule_group.command(name=cli_util.override('data_integration.update_schedule.command_name', 'update'), help=u"""Endpoint used to update the schedule \n[Command Reference](updateSchedule)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'frequency-details': {'module': 'data_integration', 'class': 'AbstractFrequencyDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def update_schedule_extended(ctx, **kwargs):
    if 'is_daylight_adj_enabled' in kwargs:
        kwargs['is_daylight_adjustment_enabled'] = kwargs['is_daylight_adj_enabled']
        kwargs.pop('is_daylight_adj_enabled')
    ctx.invoke(dataintegration_cli.update_schedule, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.schedule_group, dataintegration_cli.create_schedule_custom_frequency_details, "create-custom-frequency")


@cli_util.copy_params_from_generated_command(dataintegration_cli.create_schedule_custom_frequency_details, params_to_exclude=['is_daylight_adjustment_enabled', 'frequency_details_custom_expression', 'frequency_details_frequency'])
@cli_util.option('--is-daylight-adj-enabled', type=get_param(dataintegration_cli.create_schedule_custom_frequency_details, 'is_daylight_adjustment_enabled').type, help=get_param(dataintegration_cli.create_schedule_custom_frequency_details, 'is_daylight_adjustment_enabled').help)
@cli_util.option('--frequency', type=get_param(dataintegration_cli.create_schedule_custom_frequency_details, 'frequency_details_frequency').type, help=get_param(dataintegration_cli.create_schedule_custom_frequency_details, 'frequency_details_frequency').help)
@cli_util.option('--custom-expression', type=get_param(dataintegration_cli.create_schedule_custom_frequency_details, 'frequency_details_custom_expression').type, help=get_param(dataintegration_cli.create_schedule_custom_frequency_details, 'frequency_details_custom_expression').help)
@dataintegration_cli.schedule_group.command(name=cli_util.override('data_integration.create_schedule_custom_frequency_details.command_name', 'create-custom-frequency'), help=u"""Endpoint to create a new schedule \n[Command Reference](createSchedule)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def create_schedule_custom_frequency_details_extended(ctx, **kwargs):
    if 'is_daylight_adj_enabled' in kwargs:
        kwargs['is_daylight_adjustment_enabled'] = kwargs['is_daylight_adj_enabled']
        kwargs.pop('is_daylight_adj_enabled')

    if 'frequency' in kwargs:
        kwargs['frequency_details_frequency'] = kwargs['frequency']
        kwargs.pop('frequency')

    if 'custom_expression' in kwargs:
        kwargs['frequency_details_custom_expression'] = kwargs['custom_expression']
        kwargs.pop('custom_expression')

    ctx.invoke(dataintegration_cli.create_schedule_custom_frequency_details, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.schedule_group, dataintegration_cli.update_schedule_custom_frequency_details, "update-custom-frequency")


@cli_util.copy_params_from_generated_command(dataintegration_cli.update_schedule_custom_frequency_details, params_to_exclude=['is_daylight_adjustment_enabled', 'frequency_details_custom_expression', 'frequency_details_frequency'])
@cli_util.option('--is-daylight-adj-enabled', type=get_param(dataintegration_cli.update_schedule_custom_frequency_details, 'is_daylight_adjustment_enabled').type, help=get_param(dataintegration_cli.update_schedule_custom_frequency_details, 'is_daylight_adjustment_enabled').help)
@cli_util.option('--frequency', type=get_param(dataintegration_cli.update_schedule_custom_frequency_details, 'frequency_details_frequency').type, help=get_param(dataintegration_cli.update_schedule_custom_frequency_details, 'frequency_details_frequency').help)
@cli_util.option('--custom-expression', type=get_param(dataintegration_cli.update_schedule_custom_frequency_details, 'frequency_details_custom_expression').type, help=get_param(dataintegration_cli.create_schedule_custom_frequency_details, 'frequency_details_custom_expression').help)
@dataintegration_cli.schedule_group.command(name=cli_util.override('data_integration.update_schedule_custom_frequency_details.command_name', 'update-custom-frequency'), help=u"""Endpoint to create a new schedule \n[Command Reference](createSchedule)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def update_schedule_custom_frequency_details_extended(ctx, **kwargs):
    if 'is_daylight_adj_enabled' in kwargs:
        kwargs['is_daylight_adjustment_enabled'] = kwargs['is_daylight_adj_enabled']
        kwargs.pop('is_daylight_adj_enabled')

    if 'frequency' in kwargs:
        kwargs['frequency_details_frequency'] = kwargs['frequency']
        kwargs.pop('frequency')

    if 'custom_expression' in kwargs:
        kwargs['frequency_details_custom_expression'] = kwargs['custom_expression']
        kwargs.pop('custom_expression')

    ctx.invoke(dataintegration_cli.update_schedule_custom_frequency_details, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.schedule_group, dataintegration_cli.create_schedule_daily_frequency_details, "create-daily-frequency")


@cli_util.copy_params_from_generated_command(dataintegration_cli.create_schedule_daily_frequency_details, params_to_exclude=['is_daylight_adjustment_enabled', 'frequency_details_frequency', 'frequency_details_interval'])
@cli_util.option('--is-daylight-adj-enabled', type=get_param(dataintegration_cli.create_schedule_daily_frequency_details, 'is_daylight_adjustment_enabled').type, help=get_param(dataintegration_cli.create_schedule_daily_frequency_details, 'is_daylight_adjustment_enabled').help)
@cli_util.option('--frequency', type=get_param(dataintegration_cli.create_schedule_daily_frequency_details, 'frequency_details_frequency').type, help=get_param(dataintegration_cli.create_schedule_daily_frequency_details, 'frequency_details_frequency').help)
@cli_util.option('--interval', type=get_param(dataintegration_cli.create_schedule_daily_frequency_details, 'frequency_details_interval').type, help=get_param(dataintegration_cli.create_schedule_daily_frequency_details, 'frequency_details_interval').help)
@dataintegration_cli.schedule_group.command(name=cli_util.override('data_integration.create_schedule_daily_frequency_details.command_name', 'create-daily-frequency'), help=u"""Endpoint to create a new schedule \n[Command Reference](createSchedule)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'frequency-details-time': {'module': 'data_integration', 'class': 'Time'}}, output_type={'module': 'data_integration', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def create_schedule_daily_frequency_details_extended(ctx, **kwargs):
    if 'is_daylight_adj_enabled' in kwargs:
        kwargs['is_daylight_adjustment_enabled'] = kwargs['is_daylight_adj_enabled']
        kwargs.pop('is_daylight_adj_enabled')

    if 'frequency' in kwargs:
        kwargs['frequency_details_frequency'] = kwargs['frequency']
        kwargs.pop('frequency')

    if 'interval' in kwargs:
        kwargs['frequency_details_interval'] = kwargs['interval']
        kwargs.pop('interval')

    ctx.invoke(dataintegration_cli.create_schedule_daily_frequency_details, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.schedule_group, dataintegration_cli.update_schedule_daily_frequency_details, "update-daily-frequency")


@cli_util.copy_params_from_generated_command(dataintegration_cli.update_schedule_daily_frequency_details, params_to_exclude=['is_daylight_adjustment_enabled', 'frequency_details_frequency', 'frequency_details_interval'])
@cli_util.option('--is-daylight-adj-enabled', type=get_param(dataintegration_cli.update_schedule_daily_frequency_details, 'is_daylight_adjustment_enabled').type, help=get_param(dataintegration_cli.update_schedule_daily_frequency_details, 'is_daylight_adjustment_enabled').help)
@cli_util.option('--frequency', type=get_param(dataintegration_cli.update_schedule_daily_frequency_details, 'frequency_details_frequency').type, help=get_param(dataintegration_cli.update_schedule_daily_frequency_details, 'frequency_details_frequency').help)
@cli_util.option('--interval', type=get_param(dataintegration_cli.update_schedule_daily_frequency_details, 'frequency_details_interval').type, help=get_param(dataintegration_cli.update_schedule_daily_frequency_details, 'frequency_details_interval').help)
@dataintegration_cli.schedule_group.command(name=cli_util.override('data_integration.update_schedule_daily_frequency_details.command_name', 'update-daily-frequency'), help=u"""Endpoint used to update the schedule \n[Command Reference](updateSchedule)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'frequency-details-time': {'module': 'data_integration', 'class': 'Time'}}, output_type={'module': 'data_integration', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def update_schedule_daily_frequency_details_extended(ctx, **kwargs):
    if 'is_daylight_adj_enabled' in kwargs:
        kwargs['is_daylight_adjustment_enabled'] = kwargs['is_daylight_adj_enabled']
        kwargs.pop('is_daylight_adj_enabled')

    if 'frequency' in kwargs:
        kwargs['frequency_details_frequency'] = kwargs['frequency']
        kwargs.pop('frequency')

    if 'interval' in kwargs:
        kwargs['frequency_details_interval'] = kwargs['interval']
        kwargs.pop('interval')

    ctx.invoke(dataintegration_cli.update_schedule_daily_frequency_details, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.schedule_group, dataintegration_cli.create_schedule_hourly_frequency_details, "create-hourly-frequency")


@cli_util.copy_params_from_generated_command(dataintegration_cli.create_schedule_hourly_frequency_details, params_to_exclude=['is_daylight_adjustment_enabled', 'frequency_details_frequency', 'frequency_details_interval'])
@cli_util.option('--is-daylight-adj-enabled', type=get_param(dataintegration_cli.create_schedule_hourly_frequency_details, 'is_daylight_adjustment_enabled').type, help=get_param(dataintegration_cli.create_schedule_hourly_frequency_details, 'is_daylight_adjustment_enabled').help)
@cli_util.option('--frequency', type=get_param(dataintegration_cli.create_schedule_hourly_frequency_details, 'frequency_details_frequency').type, help=get_param(dataintegration_cli.create_schedule_hourly_frequency_details, 'frequency_details_frequency').help)
@cli_util.option('--interval', type=get_param(dataintegration_cli.create_schedule_hourly_frequency_details, 'frequency_details_interval').type, help=get_param(dataintegration_cli.create_schedule_hourly_frequency_details, 'frequency_details_interval').help)
@dataintegration_cli.schedule_group.command(name=cli_util.override('data_integration.create_schedule_hourly_frequency_details.command_name', 'create-hourly-frequency'), help=u"""Endpoint to create a new schedule \n[Command Reference](createSchedule)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'frequency-details-time': {'module': 'data_integration', 'class': 'Time'}}, output_type={'module': 'data_integration', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def create_schedule_hourly_frequency_details_extended(ctx, **kwargs):
    if 'is_daylight_adj_enabled' in kwargs:
        kwargs['is_daylight_adjustment_enabled'] = kwargs['is_daylight_adj_enabled']
        kwargs.pop('is_daylight_adj_enabled')

    if 'frequency' in kwargs:
        kwargs['frequency_details_frequency'] = kwargs['frequency']
        kwargs.pop('frequency')

    if 'interval' in kwargs:
        kwargs['frequency_details_interval'] = kwargs['interval']
        kwargs.pop('interval')

    ctx.invoke(dataintegration_cli.create_schedule_hourly_frequency_details, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.schedule_group, dataintegration_cli.update_schedule_hourly_frequency_details, "update-hourly-frequency")

cli_util.rename_command(dataintegration_cli, dataintegration_cli.schedule_group, dataintegration_cli.create_schedule_weekly_frequency_details, "create-weekly-frequency")


@cli_util.copy_params_from_generated_command(dataintegration_cli.create_schedule_weekly_frequency_details, params_to_exclude=['is_daylight_adjustment_enabled', 'frequency_details_frequency', 'frequency_details_days'])
@cli_util.option('--is-daylight-adj-enabled', type=get_param(dataintegration_cli.create_schedule_weekly_frequency_details, 'is_daylight_adjustment_enabled').type, help=get_param(dataintegration_cli.create_schedule_weekly_frequency_details, 'is_daylight_adjustment_enabled').help)
@cli_util.option('--frequency', type=get_param(dataintegration_cli.create_schedule_weekly_frequency_details, 'frequency_details_frequency').type, help=get_param(dataintegration_cli.create_schedule_weekly_frequency_details, 'frequency_details_frequency').help)
@cli_util.option('--days', type=custom_types.CLI_COMPLEX_TYPE, help=get_param(dataintegration_cli.create_schedule_weekly_frequency_details, 'frequency_details_days').help)
@dataintegration_cli.schedule_group.command(name=cli_util.override('data_integration.create_schedule_weekly_frequency_details.command_name', 'create-weekly-frequency'), help=u"""Endpoint to create a new schedule \n[Command Reference](createSchedule)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'days': {'module': 'data_integration', 'class': 'list[str]'}, 'frequency-details-time': {'module': 'data_integration', 'class': 'Time'}}, output_type={'module': 'data_integration', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def create_schedule_weekly_frequency_details_extended(ctx, **kwargs):
    if 'is_daylight_adj_enabled' in kwargs:
        kwargs['is_daylight_adjustment_enabled'] = kwargs['is_daylight_adj_enabled']
        kwargs.pop('is_daylight_adj_enabled')

    if 'frequency' in kwargs:
        kwargs['frequency_details_frequency'] = kwargs['frequency']
        kwargs.pop('frequency')

    if 'days' in kwargs:
        kwargs['frequency_details_days'] = kwargs['days']
        kwargs.pop('days')

    ctx.invoke(dataintegration_cli.create_schedule_weekly_frequency_details, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.schedule_group, dataintegration_cli.update_schedule_weekly_frequency_details, "update-weekly-frequency")


@cli_util.copy_params_from_generated_command(dataintegration_cli.update_schedule_weekly_frequency_details, params_to_exclude=['is_daylight_adjustment_enabled', 'frequency_details_frequency', 'frequency_details_days'])
@cli_util.option('--is-daylight-adj-enabled', type=get_param(dataintegration_cli.update_schedule_weekly_frequency_details, 'is_daylight_adjustment_enabled').type, help=get_param(dataintegration_cli.update_schedule_weekly_frequency_details, 'is_daylight_adjustment_enabled').help)
@cli_util.option('--frequency', type=get_param(dataintegration_cli.update_schedule_weekly_frequency_details, 'frequency_details_frequency').type, help=get_param(dataintegration_cli.update_schedule_weekly_frequency_details, 'frequency_details_frequency').help)
@cli_util.option('--days', type=custom_types.CLI_COMPLEX_TYPE, help=get_param(dataintegration_cli.update_schedule_weekly_frequency_details, 'frequency_details_days').help)
@dataintegration_cli.schedule_group.command(name=cli_util.override('data_integration.update_schedule_weekly_frequency_details.command_name', 'update-weekly-frequency'), help=u"""Endpoint to create a new schedule \n[Command Reference](createSchedule)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'frequency-details-time': {'module': 'data_integration', 'class': 'Time'}, 'days': {'module': 'data_integration', 'class': 'list[str]'}}, output_type={'module': 'data_integration', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def update_schedule_weekly_frequency_details_extended(ctx, **kwargs):
    if 'is_daylight_adj_enabled' in kwargs:
        kwargs['is_daylight_adjustment_enabled'] = kwargs['is_daylight_adj_enabled']
        kwargs.pop('is_daylight_adj_enabled')

    if 'frequency' in kwargs:
        kwargs['frequency_details_frequency'] = kwargs['frequency']
        kwargs.pop('frequency')

    if 'days' in kwargs:
        kwargs['frequency_details_days'] = kwargs['days']
        kwargs.pop('days')

    ctx.invoke(dataintegration_cli.update_schedule_weekly_frequency_details, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.schedule_group, dataintegration_cli.create_schedule_monthly_rule_frequency_details, "create-monthly-rule-frequency")


@cli_util.copy_params_from_generated_command(dataintegration_cli.create_schedule_monthly_rule_frequency_details, params_to_exclude=['is_daylight_adjustment_enabled', 'frequency_details_day_of_week', 'frequency_details_frequency', 'frequency_details_interval', 'frequency_details_week_of_month'])
@cli_util.option('--is-daylight-adj-enabled', type=get_param(dataintegration_cli.create_schedule_monthly_rule_frequency_details, 'is_daylight_adjustment_enabled').type, help=get_param(dataintegration_cli.create_schedule_monthly_rule_frequency_details, 'is_daylight_adjustment_enabled').help)
@cli_util.option('--day-of-week', type=get_param(dataintegration_cli.create_schedule_monthly_rule_frequency_details, 'frequency_details_day_of_week').type, help=get_param(dataintegration_cli.create_schedule_monthly_rule_frequency_details, 'frequency_details_day_of_week').help)
@cli_util.option('--frequency', type=get_param(dataintegration_cli.create_schedule_monthly_rule_frequency_details, 'frequency_details_frequency').type, help=get_param(dataintegration_cli.create_schedule_monthly_rule_frequency_details, 'frequency_details_frequency').help)
@cli_util.option('--interval', type=get_param(dataintegration_cli.create_schedule_monthly_rule_frequency_details, 'frequency_details_interval').type, help=get_param(dataintegration_cli.create_schedule_monthly_rule_frequency_details, 'frequency_details_interval').help)
@cli_util.option('--week-of-month', type=get_param(dataintegration_cli.create_schedule_monthly_rule_frequency_details, 'frequency_details_week_of_month').type, help=get_param(dataintegration_cli.create_schedule_monthly_rule_frequency_details, 'frequency_details_week_of_month').help)
@dataintegration_cli.schedule_group.command(name=cli_util.override('data_integration.create_schedule_monthly_rule_frequency_details.command_name', 'create-monthly-rule-frequency'), help=u"""Endpoint to create a new schedule \n[Command Reference](createSchedule)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'frequency-details-time': {'module': 'data_integration', 'class': 'Time'}}, output_type={'module': 'data_integration', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def create_schedule_monthly_rule_frequency_details_extended(ctx, **kwargs):
    if 'is_daylight_adj_enabled' in kwargs:
        kwargs['is_daylight_adjustment_enabled'] = kwargs['is_daylight_adj_enabled']
        kwargs.pop('is_daylight_adj_enabled')

    if 'frequency' in kwargs:
        kwargs['frequency_details_frequency'] = kwargs['frequency']
        kwargs.pop('frequency')

    if 'day_of_week' in kwargs:
        kwargs['frequency_details_day_of_week'] = kwargs['day_of_week']
        kwargs.pop('day_of_week')

    if 'interval' in kwargs:
        kwargs['frequency_details_interval'] = kwargs['interval']
        kwargs.pop('interval')

    if 'week_of_month' in kwargs:
        kwargs['frequency_details_week_of_month'] = kwargs['week_of_month']
        kwargs.pop('week_of_month')

    ctx.invoke(dataintegration_cli.create_schedule_monthly_rule_frequency_details, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.schedule_group, dataintegration_cli.update_schedule_monthly_rule_frequency_details, "update-monthly-rule-frequency")


@cli_util.copy_params_from_generated_command(dataintegration_cli.update_schedule_monthly_rule_frequency_details, params_to_exclude=['is_daylight_adjustment_enabled', 'frequency_details_day_of_week', 'frequency_details_frequency', 'frequency_details_interval', 'frequency_details_week_of_month'])
@cli_util.option('--is-daylight-adj-enabled', type=get_param(dataintegration_cli.update_schedule_monthly_rule_frequency_details, 'is_daylight_adjustment_enabled').type, help=get_param(dataintegration_cli.update_schedule_monthly_rule_frequency_details, 'is_daylight_adjustment_enabled').help)
@cli_util.option('--day-of-week', type=get_param(dataintegration_cli.update_schedule_monthly_rule_frequency_details, 'frequency_details_day_of_week').type, help=get_param(dataintegration_cli.update_schedule_monthly_rule_frequency_details, 'frequency_details_day_of_week').help)
@cli_util.option('--frequency', type=get_param(dataintegration_cli.update_schedule_monthly_rule_frequency_details, 'frequency_details_frequency').type, help=get_param(dataintegration_cli.update_schedule_monthly_rule_frequency_details, 'frequency_details_frequency').help)
@cli_util.option('--interval', type=get_param(dataintegration_cli.update_schedule_monthly_rule_frequency_details, 'frequency_details_interval').type, help=get_param(dataintegration_cli.update_schedule_monthly_rule_frequency_details, 'frequency_details_interval').help)
@cli_util.option('--week-of-month', type=get_param(dataintegration_cli.update_schedule_monthly_rule_frequency_details, 'frequency_details_week_of_month').type, help=get_param(dataintegration_cli.update_schedule_monthly_rule_frequency_details, 'frequency_details_week_of_month').help)
@dataintegration_cli.schedule_group.command(name=cli_util.override('data_integration.update_schedule_monthly_rule_frequency_details.command_name', 'update-monthly-rule-frequency'), help=u"""Endpoint to create a new schedule \n[Command Reference](createSchedule)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'frequency-details-time': {'module': 'data_integration', 'class': 'Time'}}, output_type={'module': 'data_integration', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def update_schedule_monthly_rule_frequency_details_extended(ctx, **kwargs):
    if 'is_daylight_adj_enabled' in kwargs:
        kwargs['is_daylight_adjustment_enabled'] = kwargs['is_daylight_adj_enabled']
        kwargs.pop('is_daylight_adj_enabled')

    if 'frequency' in kwargs:
        kwargs['frequency_details_frequency'] = kwargs['frequency']
        kwargs.pop('frequency')

    if 'day_of_week' in kwargs:
        kwargs['frequency_details_day_of_week'] = kwargs['day_of_week']
        kwargs.pop('day_of_week')

    if 'interval' in kwargs:
        kwargs['frequency_details_interval'] = kwargs['interval']
        kwargs.pop('interval')

    if 'week_of_month' in kwargs:
        kwargs['frequency_details_week_of_month'] = kwargs['week_of_month']
        kwargs.pop('week_of_month')

    ctx.invoke(dataintegration_cli.update_schedule_monthly_rule_frequency_details, **kwargs)


@cli_util.copy_params_from_generated_command(dataintegration_cli.update_schedule_hourly_frequency_details, params_to_exclude=['is_daylight_adjustment_enabled', 'frequency_details_frequency', 'frequency_details_interval'])
@cli_util.option('--is-daylight-adj-enabled', type=get_param(dataintegration_cli.update_schedule_hourly_frequency_details, 'is_daylight_adjustment_enabled').type, help=get_param(dataintegration_cli.update_schedule_hourly_frequency_details, 'is_daylight_adjustment_enabled').help)
@cli_util.option('--frequency', type=get_param(dataintegration_cli.update_schedule_hourly_frequency_details, 'frequency_details_frequency').type, help=get_param(dataintegration_cli.update_schedule_hourly_frequency_details, 'frequency_details_frequency').help)
@cli_util.option('--interval', type=get_param(dataintegration_cli.update_schedule_hourly_frequency_details, 'frequency_details_interval').type, help=get_param(dataintegration_cli.update_schedule_hourly_frequency_details, 'frequency_details_interval').help)
@dataintegration_cli.schedule_group.command(name=cli_util.override('data_integration.update_schedule_hourly_frequency_details.command_name', 'update-hourly-frequency'), help=u"""Endpoint to create a new schedule \n[Command Reference](createSchedule)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'frequency-details-time': {'module': 'data_integration', 'class': 'Time'}}, output_type={'module': 'data_integration', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def update_schedule_hourly_frequency_details_extended(ctx, **kwargs):
    if 'is_daylight_adj_enabled' in kwargs:
        kwargs['is_daylight_adjustment_enabled'] = kwargs['is_daylight_adj_enabled']
        kwargs.pop('is_daylight_adj_enabled')

    if 'frequency' in kwargs:
        kwargs['frequency_details_frequency'] = kwargs['frequency']
        kwargs.pop('frequency')

    if 'interval' in kwargs:
        kwargs['frequency_details_interval'] = kwargs['interval']
        kwargs.pop('interval')

    ctx.invoke(dataintegration_cli.update_schedule_hourly_frequency_details, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.schedule_group, dataintegration_cli.create_schedule_monthly_frequency_details, "create-monthly-frequency")


@cli_util.copy_params_from_generated_command(dataintegration_cli.create_schedule_monthly_frequency_details, params_to_exclude=['is_daylight_adjustment_enabled', 'frequency_details_frequency', 'frequency_details_interval'])
@cli_util.option('--is-daylight-adj-enabled', type=get_param(dataintegration_cli.create_schedule_monthly_frequency_details, 'is_daylight_adjustment_enabled').type, help=get_param(dataintegration_cli.create_schedule_monthly_frequency_details, 'is_daylight_adjustment_enabled').help)
@cli_util.option('--frequency', type=get_param(dataintegration_cli.create_schedule_monthly_frequency_details, 'frequency_details_frequency').type, help=get_param(dataintegration_cli.create_schedule_monthly_frequency_details, 'frequency_details_frequency').help)
@cli_util.option('--interval', type=get_param(dataintegration_cli.create_schedule_monthly_frequency_details, 'frequency_details_interval').type, help=get_param(dataintegration_cli.create_schedule_monthly_frequency_details, 'frequency_details_interval').help)
@dataintegration_cli.schedule_group.command(name=cli_util.override('data_integration.create_schedule_monthly_frequency_details.command_name', 'create-monthly-frequency'), help=u"""Endpoint to create a new schedule \n[Command Reference](createSchedule)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'frequency-details-time': {'module': 'data_integration', 'class': 'Time'}, 'frequency-details-days': {'module': 'data_integration', 'class': 'list[integer]'}}, output_type={'module': 'data_integration', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def create_schedule_monthly_frequency_details_extended(ctx, **kwargs):
    if 'is_daylight_adj_enabled' in kwargs:
        kwargs['is_daylight_adjustment_enabled'] = kwargs['is_daylight_adj_enabled']
        kwargs.pop('is_daylight_adj_enabled')

    if 'frequency' in kwargs:
        kwargs['frequency_details_frequency'] = kwargs['frequency']
        kwargs.pop('frequency')

    if 'interval' in kwargs:
        kwargs['frequency_details_interval'] = kwargs['interval']
        kwargs.pop('interval')

    ctx.invoke(dataintegration_cli.create_schedule_monthly_frequency_details, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.schedule_group, dataintegration_cli.update_schedule_monthly_frequency_details, "update-monthly-frequency")


@cli_util.copy_params_from_generated_command(dataintegration_cli.update_schedule_monthly_frequency_details, params_to_exclude=['is_daylight_adjustment_enabled', 'frequency_details_frequency', 'frequency_details_interval'])
@cli_util.option('--is-daylight-adj-enabled', type=get_param(dataintegration_cli.update_schedule_monthly_frequency_details, 'is_daylight_adjustment_enabled').type, help=get_param(dataintegration_cli.update_schedule_monthly_frequency_details, 'is_daylight_adjustment_enabled').help)
@cli_util.option('--frequency', type=get_param(dataintegration_cli.update_schedule_monthly_frequency_details, 'frequency_details_frequency').type, help=get_param(dataintegration_cli.update_schedule_monthly_frequency_details, 'frequency_details_frequency').help)
@cli_util.option('--interval', type=get_param(dataintegration_cli.update_schedule_monthly_frequency_details, 'frequency_details_interval').type, help=get_param(dataintegration_cli.update_schedule_monthly_frequency_details, 'frequency_details_interval').help)
@dataintegration_cli.schedule_group.command(name=cli_util.override('data_integration.update_schedule_monthly_frequency_details.command_name', 'update-monthly-frequency'), help=u"""Endpoint used to update the schedule \n[Command Reference](updateSchedule)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'frequency-details-time': {'module': 'data_integration', 'class': 'Time'}, 'frequency-details-days': {'module': 'data_integration', 'class': 'list[integer]'}}, output_type={'module': 'data_integration', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def update_schedule_monthly_frequency_details_extended(ctx, **kwargs):
    if 'is_daylight_adj_enabled' in kwargs:
        kwargs['is_daylight_adjustment_enabled'] = kwargs['is_daylight_adj_enabled']
        kwargs.pop('is_daylight_adj_enabled')

    if 'frequency' in kwargs:
        kwargs['frequency_details_frequency'] = kwargs['frequency']
        kwargs.pop('frequency')

    if 'interval' in kwargs:
        kwargs['frequency_details_interval'] = kwargs['interval']
        kwargs.pop('interval')

    ctx.invoke(dataintegration_cli.update_schedule_monthly_frequency_details, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_group, dataintegration_cli.create_task_create_task_from_sql_task, "create-task-from-sql-task")


@cli_util.copy_params_from_generated_command(dataintegration_cli.create_task_create_task_from_sql_task, params_to_exclude=['config_provider_delegate'])
@cli_util.option('--config-provider', type=get_param(dataintegration_cli.create_task_create_task_from_sql_task, 'config_provider_delegate').type, help=get_param(dataintegration_cli.create_task_create_task_from_sql_task, 'config_provider_delegate').help)
@dataintegration_cli.task_group.command(name=cli_util.override('data_integration.create_task_create_task_from_sql_task.command_name', 'create-task-from-sql-task'), help=u"""Creates a new task ready for performing data integrations. There are specialized types of tasks that include data loader and integration tasks. \n[Command Reference](createTask)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider': {'module': 'data_integration', 'class': 'CreateConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'script': {'module': 'data_integration', 'class': 'Script'}, 'operation': {'module': 'data_integration', 'class': 'object'}}, output_type={'module': 'data_integration', 'class': 'Task'})
@cli_util.wrap_exceptions
def create_task_create_task_from_sql_task_extended(ctx, **kwargs):
    if 'config_provider' in kwargs:
        kwargs['config_provider_delegate'] = kwargs['config_provider']
        kwargs.pop('config_provider')
    ctx.invoke(dataintegration_cli.create_task_create_task_from_sql_task, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_group, dataintegration_cli.update_task_update_task_from_sql_task, "update-task-from-sql-task")


@cli_util.copy_params_from_generated_command(dataintegration_cli.update_task_update_task_from_sql_task, params_to_exclude=['config_provider_delegate'])
@cli_util.option('--config-provider', type=get_param(dataintegration_cli.update_task_update_task_from_sql_task, 'config_provider_delegate').type, help=get_param(dataintegration_cli.update_task_update_task_from_sql_task, 'config_provider_delegate').help)
@dataintegration_cli.task_group.command(name=cli_util.override('data_integration.update_task_update_task_from_sql_task.command_name', 'update-task-update-task-from-sql-task'), help=u"""Updates a specific task. For example, you can update the task description or move the task to a different folder by changing the `aggregatorKey` to a different folder in the registry. \n[Command Reference](updateTask)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'script': {'module': 'data_integration', 'class': 'Script'}, 'operation': {'module': 'data_integration', 'class': 'object'}}, output_type={'module': 'data_integration', 'class': 'Task'})
@cli_util.wrap_exceptions
def update_task_update_task_from_sql_task_extended(ctx, **kwargs):
    if 'config_provider' in kwargs:
        kwargs['config_provider_delegate'] = kwargs['config_provider']
        kwargs.pop('config_provider')
    ctx.invoke(dataintegration_cli.update_task_update_task_from_sql_task, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_group, dataintegration_cli.create_task_create_task_from_rest_task, "create-task-from-rest-task")


@cli_util.copy_params_from_generated_command(dataintegration_cli.create_task_create_task_from_rest_task, params_to_exclude=['endpoint_parameterconflict', 'execute_rest_call_config', 'cancel_rest_call_config'])
@cli_util.option('--apiendpoint', type=get_param(dataintegration_cli.create_task_create_task_from_rest_task, 'endpoint_parameterconflict').type, help=get_param(dataintegration_cli.create_task_create_task_from_rest_task, 'endpoint_parameterconflict').help)
@cli_util.option('--execute-rest-config', type=get_param(dataintegration_cli.create_task_create_task_from_rest_task, 'execute_rest_call_config').type, help=get_param(dataintegration_cli.create_task_create_task_from_rest_task, 'execute_rest_call_config').help)
@cli_util.option('--cancel-rest-config', type=get_param(dataintegration_cli.create_task_create_task_from_rest_task, 'cancel_rest_call_config').type, help=get_param(dataintegration_cli.create_task_create_task_from_rest_task, 'cancel_rest_call_config').help)
@dataintegration_cli.task_group.command(name=cli_util.override('data_integration.create_task_create_task_from_rest_task.command_name', 'create-task-create-task-from-rest-task'), help=u"""Creates a new task ready for performing data integrations. There are specialized types of tasks that include data loader and integration tasks. \n[Command Reference](createTask)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'CreateConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'auth-details': {'module': 'data_integration', 'class': 'AuthDetails'}, 'apiendpoint': {'module': 'data_integration', 'class': 'Expression'}, 'headers': {'module': 'data_integration', 'class': 'object'}, 'cancel-endpoint': {'module': 'data_integration', 'class': 'Expression'}, 'execute-rest-config': {'module': 'data_integration', 'class': 'ExecuteRestCallConfig'}, 'cancel-rest-config': {'module': 'data_integration', 'class': 'CancelRestCallConfig'}}, output_type={'module': 'data_integration', 'class': 'Task'})
@cli_util.wrap_exceptions
def create_task_create_task_from_rest_task_extended(ctx, **kwargs):
    if 'apiendpoint' in kwargs:
        kwargs['endpoint_parameterconflict'] = kwargs['apiendpoint']
        kwargs.pop('apiendpoint')

    if 'execute_rest_config' in kwargs:
        kwargs['execute_rest_call_config'] = kwargs['execute_rest_config']
        kwargs.pop('execute_rest_config')

    if 'cancel_rest_config' in kwargs:
        kwargs['cancel_rest_call_config'] = kwargs['cancel_rest_config']
        kwargs.pop('cancel_rest_config')

    ctx.invoke(dataintegration_cli.create_task_create_task_from_rest_task, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_group, dataintegration_cli.update_task_update_task_from_rest_task, "update-task-from-rest-task")


@cli_util.copy_params_from_generated_command(dataintegration_cli.update_task_update_task_from_rest_task, params_to_exclude=['endpoint_parameterconflict', 'execute_rest_call_config', 'cancel_rest_call_config'])
@cli_util.option('--apiendpoint', type=get_param(dataintegration_cli.update_task_update_task_from_rest_task, 'endpoint_parameterconflict').type, help=get_param(dataintegration_cli.update_task_update_task_from_rest_task, 'endpoint_parameterconflict').help)
@cli_util.option('--execute-rest-config', type=get_param(dataintegration_cli.update_task_update_task_from_rest_task, 'execute_rest_call_config').type, help=get_param(dataintegration_cli.update_task_update_task_from_rest_task, 'execute_rest_call_config').help)
@cli_util.option('--cancel-rest-config', type=get_param(dataintegration_cli.update_task_update_task_from_rest_task, 'cancel_rest_call_config').type, help=get_param(dataintegration_cli.update_task_update_task_from_rest_task, 'cancel_rest_call_config').help)
@dataintegration_cli.task_group.command(name=cli_util.override('data_integration.update_task_update_task_from_rest_task.command_name', 'update-task-update-task-from-rest-task'), help=u"""Updates a specific task. For example, you can update the task description or move the task to a different folder by changing the `aggregatorKey` to a different folder in the registry. \n[Command Reference](updateTask)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'auth-details': {'module': 'data_integration', 'class': 'AuthDetails'}, 'apiendpoint': {'module': 'data_integration', 'class': 'Expression'}, 'headers': {'module': 'data_integration', 'class': 'object'}, 'cancel-endpoint': {'module': 'data_integration', 'class': 'Expression'}, 'execute-rest-config': {'module': 'data_integration', 'class': 'ExecuteRestCallConfig'}, 'cancel-rest-config': {'module': 'data_integration', 'class': 'CancelRestCallConfig'}}, output_type={'module': 'data_integration', 'class': 'Task'})
@cli_util.wrap_exceptions
def update_task_update_task_from_rest_task_extended(ctx, **kwargs):
    if 'apiendpoint' in kwargs:
        kwargs['endpoint_parameterconflict'] = kwargs['apiendpoint']
        kwargs.pop('apiendpoint')

    if 'execute_rest_config' in kwargs:
        kwargs['execute_rest_call_config'] = kwargs['execute_rest_config']
        kwargs.pop('execute_rest_config')

    if 'cancel_rest_config' in kwargs:
        kwargs['cancel_rest_call_config'] = kwargs['cancel_rest_config']
        kwargs.pop('cancel_rest_config')

    ctx.invoke(dataintegration_cli.update_task_update_task_from_rest_task, **kwargs)


cli_util.rename_command(dataintegration_cli, dataintegration_cli.data_entity_group, dataintegration_cli.create_entity_shape_create_entity_shape_from_file, "create-entity-shape-from-file")

cli_util.rename_command(dataintegration_cli, dataintegration_cli.data_entity_group, dataintegration_cli.create_entity_shape_create_entity_shape_from_sql, "create-entity-shape-from-sql")


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
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_lake.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_rest.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_hdfs.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_my_sql_heat_wave.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_oracle_ebs.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_oracle_people_soft.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_oracle_siebel.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_atp.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_adwc.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_oracle.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_object_storage.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_my_sql.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_jdbc.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_lake.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_rest_basic_auth.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_rest_no_auth.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_hdfs.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_my_sql_heat_wave.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_oracle_ebs.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_oracle_people_soft.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_oracle_siebel.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_my_sql.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_jdbc.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_o_auth2.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_jdbc.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_my_sql.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_jdbc.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_my_sql.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_jdbc.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_my_sql.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_lake.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_rest.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_jdbc.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_my_sql.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_lake.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_rest.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_amazon_s3.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_amazon_s3.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.create_connection_create_connection_from_bicc.name)
dataintegration_cli.connection_group.commands.pop(dataintegration_cli.update_connection_update_connection_from_bicc.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_amazon_s3.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_connection_from_bicc.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_fusion_app.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_fusion_app.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_hdfs.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_my_sql_heat_wave.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_oracle_ebs.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_oracle_people_soft.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_oracle_siebel.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_amazon_s3.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_fusion_app.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_hdfs.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_my_sql_heat_wave.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_oracle_ebs.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_oracle_people_soft.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.update_data_asset_update_data_asset_from_oracle_siebel.name)
dataintegration_cli.connection_validation_group.commands.pop(dataintegration_cli.create_connection_validation_create_data_asset_from_amazon_s3.name)
dataintegration_cli.data_asset_group.commands.pop(dataintegration_cli.create_data_asset_create_data_asset_from_amazon_s3.name)

cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_group, dataintegration_cli.create_task_create_task_from_oci_dataflow_task, "create-task-from-dataflow-task")
cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_group, dataintegration_cli.update_task_update_task_from_oci_dataflow_task, "update-task-from-dataflow-task")

cli_util.rename_command(dataintegration_cli, dataintegration_cli.data_integration_root_group, dataintegration_cli.runtime_pipeline_summary_collection_group, "runtime-pipelines")
cli_util.rename_command(dataintegration_cli, dataintegration_cli.data_integration_root_group, dataintegration_cli.runtime_operator_summary_collection_group, "runtime-operators")

cli_util.rename_command(dataintegration_cli, dataintegration_cli.data_integration_root_group, dataintegration_cli.task_run_lineage_summary_collection_group, "task-run-lineage")
cli_util.rename_command(dataintegration_cli, dataintegration_cli.task_run_lineage_summary_collection_group, dataintegration_cli.list_dis_application_task_run_lineages, "list_taskrun_lineages")


@cli_util.copy_params_from_generated_command(dataintegration_cli.list_dis_application_task_run_lineages, params_to_exclude=['time_upated_less_than_or_equal_to', 'time_updated_greater_than', 'time_updated_greater_than_or_equal_to'])
@cli_util.option('--time-upated-lte', type=custom_types.CLI_DATETIME, help=u"""This parameter allows users to get objects which were updated before and at a certain time. The format of timeUpatedLessThanOrEqualTo is \"YYYY-MM-dd'T'HH:mm:ss.SSS'Z'\"""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated-gt', type=custom_types.CLI_DATETIME, help=u"""This parameter allows users to get objects which were updated after a certain time. The format of timeUpdatedGreaterThan is \"YYYY-MM-dd'T'HH:mm:ss.SSS'Z'\"""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated-gte', type=custom_types.CLI_DATETIME, help=u"""This parameter allows users to get objects which were updated after and at a certain time. The format of timeUpdatedGreaterThanOrEqualTo is \"YYYY-MM-dd'T'HH:mm:ss.SSS'Z'\"""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@dataintegration_cli.task_run_lineage_summary_collection_group.command(name=cli_util.override('data_integration.list_dis_application_task_run_lineages.command_name', 'list-dis-application-task-run-lineages'), help=u"""This endpoint can be used to list Task Run Lineages within a given time window. \n[Command Reference](listDisApplicationTaskRunLineages)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'filter': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def list_dis_application_task_run_lineages_extended(ctx, **kwargs):
    if 'time_upated_lte' in kwargs:
        kwargs['time_upated_less_than_or_equal_to'] = kwargs['time_upated_lte']
        kwargs.pop('time_upated_lte')

    if 'time_updated_gt' in kwargs:
        kwargs['time_updated_greater_than'] = kwargs['time_updated_gt']
        kwargs.pop('time_updated_gt')

    if 'time_updated_gte' in kwargs:
        kwargs['time_updated_greater_than_or_equal_to'] = kwargs['time_updated_gte']
        kwargs.pop('time_updated_gte')

    ctx.invoke(dataintegration_cli.list_dis_application_task_run_lineages, **kwargs)


@cli_util.copy_params_from_generated_command(dataintegration_cli.list_task_run_lineages, params_to_exclude=['time_upated_less_than_or_equal_to', 'time_updated_greater_than', 'time_updated_greater_than_or_equal_to'])
@cli_util.option('--time-upated-lte', type=custom_types.CLI_DATETIME, help=u"""This parameter allows users to get objects which were updated before and at a certain time. The format of timeUpatedLessThanOrEqualTo is \"YYYY-MM-dd'T'HH:mm:ss.SSS'Z'\"""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated-gt', type=custom_types.CLI_DATETIME, help=u"""This parameter allows users to get objects which were updated after a certain time. The format of timeUpdatedGreaterThan is \"YYYY-MM-dd'T'HH:mm:ss.SSS'Z'\"""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated-gte', type=custom_types.CLI_DATETIME, help=u"""This parameter allows users to get objects which were updated after and at a certain time. The format of timeUpdatedGreaterThanOrEqualTo is \"YYYY-MM-dd'T'HH:mm:ss.SSS'Z'\"""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@dataintegration_cli.task_run_lineage_summary_collection_group.command(name=cli_util.override('data_integration.list_task_run_lineages.command_name', 'list-task-run-lineages'), help=u"""This endpoint can be used to list Task Run Lineages within a given time window. \n[Command Reference](listTaskRunLineages)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'filter': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def list_task_run_lineages_extended(ctx, **kwargs):
    if 'time_upated_lte' in kwargs:
        kwargs['time_upated_less_than_or_equal_to'] = kwargs['time_upated_lte']
        kwargs.pop('time_upated_lte')

    if 'time_updated_gt' in kwargs:
        kwargs['time_updated_greater_than'] = kwargs['time_updated_gt']
        kwargs.pop('time_updated_gt')

    if 'time_updated_gte' in kwargs:
        kwargs['time_updated_greater_than_or_equal_to'] = kwargs['time_updated_gte']
        kwargs.pop('time_updated_gte')

    ctx.invoke(dataintegration_cli.list_task_run_lineages, **kwargs)
