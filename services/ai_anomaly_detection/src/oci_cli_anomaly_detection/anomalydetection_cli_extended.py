# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.ai_anomaly_detection.src.oci_cli_anomaly_detection.generated import anomalydetection_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci anomaly-detection ai-private-endpoint -> oci anomaly-detection pe
cli_util.rename_command(anomalydetection_cli, anomalydetection_cli.anomaly_detection_root_group, anomalydetection_cli.ai_private_endpoint_group, "pe")

# oci anomaly-detection data-asset create-data-asset-data-source-details-atp -> oci anomaly-detection data-asset create-data-source-atp
cli_util.rename_command(anomalydetection_cli, anomalydetection_cli.data_asset_group, anomalydetection_cli.create_data_asset_data_source_details_atp, "create-data-source-atp")


# oci anomaly-detection data-asset create-data-asset-data-source-details-influx -> oci anomaly-detection data-asset create-data-source-influx
cli_util.rename_command(anomalydetection_cli, anomalydetection_cli.data_asset_group, anomalydetection_cli.create_data_asset_data_source_details_influx, "create-data-source-influx")


# oci anomaly-detection data-asset create-data-asset-data-source-details-object-storage -> oci anomaly-detection data-asset create-data-source-os
cli_util.rename_command(anomalydetection_cli, anomalydetection_cli.data_asset_group, anomalydetection_cli.create_data_asset_data_source_details_object_storage, "create-data-source-os")


# oci anomaly-detection data-asset-collection list-data-assets -> oci anomaly-detection data-asset-collection list
cli_util.rename_command(anomalydetection_cli, anomalydetection_cli.data_asset_collection_group, anomalydetection_cli.list_data_assets, "list")


# oci anomaly-detection ai-private-endpoint-collection list-ai-private-endpoints -> oci anomaly-detection ai-private-endpoint-collection list
cli_util.rename_command(anomalydetection_cli, anomalydetection_cli.ai_private_endpoint_collection_group, anomalydetection_cli.list_ai_private_endpoints, "list")


# oci anomaly-detection model detect-anomalies-embedded-detect-anomalies-request -> oci anomaly-detection model detect-anomalies-embedded
cli_util.rename_command(anomalydetection_cli, anomalydetection_cli.model_group, anomalydetection_cli.detect_anomalies_embedded_detect_anomalies_request, "detect-anomalies-embedded")


# oci anomaly-detection model detect-anomalies-inline-detect-anomalies-request -> oci anomaly-detection model detect-anomalies-inline
cli_util.rename_command(anomalydetection_cli, anomalydetection_cli.model_group, anomalydetection_cli.detect_anomalies_inline_detect_anomalies_request, "detect-anomalies-inline")


# Move commands under 'oci anomaly-detection ai-private-endpoint-collection' -> 'oci anomaly-detection ai-private-endpoint'
anomalydetection_cli.anomaly_detection_root_group.commands.pop(anomalydetection_cli.ai_private_endpoint_collection_group.name)
anomalydetection_cli.ai_private_endpoint_group.add_command(anomalydetection_cli.list_ai_private_endpoints)


# Move commands under 'oci anomaly-detection data-asset-collection' -> 'oci anomaly-detection data-asset'
anomalydetection_cli.anomaly_detection_root_group.commands.pop(anomalydetection_cli.data_asset_collection_group.name)
anomalydetection_cli.data_asset_group.add_command(anomalydetection_cli.list_data_assets)


@cli_util.copy_params_from_generated_command(anomalydetection_cli.change_ai_private_endpoint_compartment, params_to_exclude=['ai_private_endpoint_id'])
@anomalydetection_cli.ai_private_endpoint_group.command(name=anomalydetection_cli.change_ai_private_endpoint_compartment.name, help=anomalydetection_cli.change_ai_private_endpoint_compartment.help)
@cli_util.option('--pe-id', required=True, help=u"""Unique private reverse connection identifier. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_ai_private_endpoint_compartment_extended(ctx, **kwargs):
    if 'pe_id' in kwargs:
        kwargs['ai_private_endpoint_id'] = kwargs['pe_id']
        kwargs.pop('pe_id')

    ctx.invoke(anomalydetection_cli.change_ai_private_endpoint_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(anomalydetection_cli.delete_ai_private_endpoint, params_to_exclude=['ai_private_endpoint_id'])
@anomalydetection_cli.ai_private_endpoint_group.command(name=anomalydetection_cli.delete_ai_private_endpoint.name, help=anomalydetection_cli.delete_ai_private_endpoint.help)
@cli_util.option('--pe-id', required=True, help=u"""Unique private reverse connection identifier. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_ai_private_endpoint_extended(ctx, **kwargs):
    if 'pe_id' in kwargs:
        kwargs['ai_private_endpoint_id'] = kwargs['pe_id']
        kwargs.pop('pe_id')

    ctx.invoke(anomalydetection_cli.delete_ai_private_endpoint, **kwargs)


@cli_util.copy_params_from_generated_command(anomalydetection_cli.get_ai_private_endpoint, params_to_exclude=['ai_private_endpoint_id'])
@anomalydetection_cli.ai_private_endpoint_group.command(name=anomalydetection_cli.get_ai_private_endpoint.name, help=anomalydetection_cli.get_ai_private_endpoint.help)
@cli_util.option('--pe-id', required=True, help=u"""Unique private reverse connection identifier. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'AiPrivateEndpoint'})
@cli_util.wrap_exceptions
def get_ai_private_endpoint_extended(ctx, **kwargs):
    if 'pe_id' in kwargs:
        kwargs['ai_private_endpoint_id'] = kwargs['pe_id']
        kwargs.pop('pe_id')

    ctx.invoke(anomalydetection_cli.get_ai_private_endpoint, **kwargs)


@cli_util.copy_params_from_generated_command(anomalydetection_cli.update_ai_private_endpoint, params_to_exclude=['ai_private_endpoint_id'])
@anomalydetection_cli.ai_private_endpoint_group.command(name=anomalydetection_cli.update_ai_private_endpoint.name, help=anomalydetection_cli.update_ai_private_endpoint.help)
@cli_util.option('--pe-id', required=True, help=u"""Unique private reverse connection identifier. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dns-zones': {'module': 'ai_anomaly_detection', 'class': 'list[string]'}, 'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_ai_private_endpoint_extended(ctx, **kwargs):
    if 'pe_id' in kwargs:
        kwargs['ai_private_endpoint_id'] = kwargs['pe_id']
        kwargs.pop('pe_id')

    ctx.invoke(anomalydetection_cli.update_ai_private_endpoint, **kwargs)


@cli_util.copy_params_from_generated_command(anomalydetection_cli.create_data_asset_data_source_details_atp, params_to_exclude=['data_source_details_atp_password_secret_id', 'data_source_details_atp_user_name', 'data_source_details_cwallet_file_secret_id', 'data_source_details_database_name', 'data_source_details_ewallet_file_secret_id', 'data_source_details_key_store_file_secret_id', 'data_source_details_ojdbc_file_secret_id', 'data_source_details_table_name', 'data_source_details_tnsnames_file_secret_id', 'data_source_details_truststore_file_secret_id', 'data_source_details_wallet_password_secret_id'])
@anomalydetection_cli.data_asset_group.command(name=anomalydetection_cli.create_data_asset_data_source_details_atp.name, help=anomalydetection_cli.create_data_asset_data_source_details_atp.help)
@cli_util.option('--atp-password-secret-id', help=u"""atp db password Secret Id""")
@cli_util.option('--atp-user-name', help=u"""atp db user name""")
@cli_util.option('--cwallet-file-secret-id', help=u"""OCID of the secret containing the containers certificates of ATP wallet""")
@cli_util.option('--database-name', help=u"""atp database name""")
@cli_util.option('--ewallet-file-secret-id', help=u"""OCID of the secret containing the PDB'S certificates of ATP wallet""")
@cli_util.option('--key-store-file-secret-id', help=u"""OCID of the secret containing Keystore.jks file of the ATP wallet""")
@cli_util.option('--ojdbc-file-secret-id', help=u"""OCID of the secret that contains jdbc properties file of ATP wallet""")
@cli_util.option('--table-name', help=u"""atp database table name""")
@cli_util.option('--tnsnames-file-secret-id', help=u"""OCID of the secret that contains the tnsnames file of ATP wallet""")
@cli_util.option('--truststore-file-secret-id', help=u"""OCID of the secret containing truststore.jks file of the ATP wallet""")
@cli_util.option('--wallet-password-secret-id', help=u"""wallet password Secret ID in String format""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_anomaly_detection', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def create_data_asset_data_source_details_atp_extended(ctx, **kwargs):
    if 'atp_password_secret_id' in kwargs:
        kwargs['data_source_details_atp_password_secret_id'] = kwargs['atp_password_secret_id']
        kwargs.pop('atp_password_secret_id')

    if 'atp_user_name' in kwargs:
        kwargs['data_source_details_atp_user_name'] = kwargs['atp_user_name']
        kwargs.pop('atp_user_name')

    if 'cwallet_file_secret_id' in kwargs:
        kwargs['data_source_details_cwallet_file_secret_id'] = kwargs['cwallet_file_secret_id']
        kwargs.pop('cwallet_file_secret_id')

    if 'database_name' in kwargs:
        kwargs['data_source_details_database_name'] = kwargs['database_name']
        kwargs.pop('database_name')

    if 'ewallet_file_secret_id' in kwargs:
        kwargs['data_source_details_ewallet_file_secret_id'] = kwargs['ewallet_file_secret_id']
        kwargs.pop('ewallet_file_secret_id')

    if 'key_store_file_secret_id' in kwargs:
        kwargs['data_source_details_key_store_file_secret_id'] = kwargs['key_store_file_secret_id']
        kwargs.pop('key_store_file_secret_id')

    if 'ojdbc_file_secret_id' in kwargs:
        kwargs['data_source_details_ojdbc_file_secret_id'] = kwargs['ojdbc_file_secret_id']
        kwargs.pop('ojdbc_file_secret_id')

    if 'table_name' in kwargs:
        kwargs['data_source_details_table_name'] = kwargs['table_name']
        kwargs.pop('table_name')

    if 'tnsnames_file_secret_id' in kwargs:
        kwargs['data_source_details_tnsnames_file_secret_id'] = kwargs['tnsnames_file_secret_id']
        kwargs.pop('tnsnames_file_secret_id')

    if 'truststore_file_secret_id' in kwargs:
        kwargs['data_source_details_truststore_file_secret_id'] = kwargs['truststore_file_secret_id']
        kwargs.pop('truststore_file_secret_id')

    if 'wallet_password_secret_id' in kwargs:
        kwargs['data_source_details_wallet_password_secret_id'] = kwargs['wallet_password_secret_id']
        kwargs.pop('wallet_password_secret_id')

    ctx.invoke(anomalydetection_cli.create_data_asset_data_source_details_atp, **kwargs)


@cli_util.copy_params_from_generated_command(anomalydetection_cli.create_data_asset_data_source_details_influx, params_to_exclude=['data_source_details_measurement_name', 'data_source_details_password_secret_id', 'data_source_details_url', 'data_source_details_user_name', 'data_source_details_version_specific_details'])
@anomalydetection_cli.data_asset_group.command(name=anomalydetection_cli.create_data_asset_data_source_details_influx.name, help=anomalydetection_cli.create_data_asset_data_source_details_influx.help)
@cli_util.option('--measurement-name', required=True, help=u"""Measurement name for influx [required]""")
@cli_util.option('--password-secret-id', required=True, help=u"""Password Secret Id for the influx connection [required]""")
@cli_util.option('--url', required=True, help=u"""public IP address and port to influx DB [required]""")
@cli_util.option('--user-name', required=True, help=u"""Username for connection to Influx [required]""")
@cli_util.option('--version-specific-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}, 'version-specific-details': {'module': 'ai_anomaly_detection', 'class': 'InfluxDetails'}}, output_type={'module': 'ai_anomaly_detection', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def create_data_asset_data_source_details_influx_extended(ctx, **kwargs):
    if 'measurement_name' in kwargs:
        kwargs['data_source_details_measurement_name'] = kwargs['measurement_name']
        kwargs.pop('measurement_name')

    if 'password_secret_id' in kwargs:
        kwargs['data_source_details_password_secret_id'] = kwargs['password_secret_id']
        kwargs.pop('password_secret_id')

    if 'url' in kwargs:
        kwargs['data_source_details_url'] = kwargs['url']
        kwargs.pop('url')

    if 'user_name' in kwargs:
        kwargs['data_source_details_user_name'] = kwargs['user_name']
        kwargs.pop('user_name')

    if 'version_specific_details' in kwargs:
        kwargs['data_source_details_version_specific_details'] = kwargs['version_specific_details']
        kwargs.pop('version_specific_details')

    ctx.invoke(anomalydetection_cli.create_data_asset_data_source_details_influx, **kwargs)


@cli_util.copy_params_from_generated_command(anomalydetection_cli.create_data_asset_data_source_details_object_storage, params_to_exclude=['data_source_details_bucket_name', 'data_source_details_namespace', 'data_source_details_object_name'])
@anomalydetection_cli.data_asset_group.command(name=anomalydetection_cli.create_data_asset_data_source_details_object_storage.name, help=anomalydetection_cli.create_data_asset_data_source_details_object_storage.help)
@cli_util.option('--bucket-name', help=u"""Object storage bucket name""")
@cli_util.option('--namespace', help=u"""Object storage namespace""")
@cli_util.option('--object-name', help=u"""File name""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_anomaly_detection', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def create_data_asset_data_source_details_object_storage_extended(ctx, **kwargs):
    if 'bucket_name' in kwargs:
        kwargs['data_source_details_bucket_name'] = kwargs['bucket_name']
        kwargs.pop('bucket_name')

    if 'namespace' in kwargs:
        kwargs['data_source_details_namespace'] = kwargs['namespace']
        kwargs.pop('namespace')

    if 'object_name' in kwargs:
        kwargs['data_source_details_object_name'] = kwargs['object_name']
        kwargs.pop('object_name')

    ctx.invoke(anomalydetection_cli.create_data_asset_data_source_details_object_storage, **kwargs)
