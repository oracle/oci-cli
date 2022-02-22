# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.data_connectivity.src.oci_cli_data_connectivity.generated import data_connectivity_service_cli
from services.data_connectivity.src.oci_cli_data_connectivity_management.generated import dataconnectivitymanagement_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.list_connection_validations, params_to_exclude=['query_parameterconflict'])
@dataconnectivitymanagement_cli.connection_validation_group.command(name=dataconnectivitymanagement_cli.list_connection_validations.name, help=dataconnectivitymanagement_cli.list_connection_validations.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_connectivity', 'class': 'list[string]'}}, output_type={'module': 'data_connectivity', 'class': 'ConnectionValidationSummaryCollection'})
@cli_util.wrap_exceptions
def list_connection_validations_extended(ctx, **kwargs):

    ctx.invoke(dataconnectivitymanagement_cli.list_connection_validations, **kwargs)


# oci data-connectivity data-entity create-data-preview-data-entity-from-data-store -> oci data-connectivity data-entity create-data-preview-ds
cli_util.rename_command(dataconnectivitymanagement_cli, dataconnectivitymanagement_cli.data_entity_group, dataconnectivitymanagement_cli.create_data_preview_data_entity_from_data_store, "create-data-preview-ds")


# oci data-connectivity data-entity create-data-preview-data-entity-from-file -> oci data-connectivity data-entity create-data-preview-file
cli_util.rename_command(dataconnectivitymanagement_cli, dataconnectivitymanagement_cli.data_entity_group, dataconnectivitymanagement_cli.create_data_preview_data_entity_from_file, "create-data-preview-file")


# oci data-connectivity data-entity create-data-preview-data-entity-from-sql -> oci data-connectivity data-entity create-data-preview-sql
cli_util.rename_command(dataconnectivitymanagement_cli, dataconnectivitymanagement_cli.data_entity_group, dataconnectivitymanagement_cli.create_data_preview_data_entity_from_sql, "create-data-preview-sql")


# oci data-connectivity data-entity create-data-preview-data-entity-from-table -> oci data-connectivity data-entity create-data-preview-table
cli_util.rename_command(dataconnectivitymanagement_cli, dataconnectivitymanagement_cli.data_entity_group, dataconnectivitymanagement_cli.create_data_preview_data_entity_from_table, "create-data-preview-table")


# oci data-connectivity data-entity create-data-preview-data-entity-from-view -> oci data-connectivity data-entity create-data-preview-view
cli_util.rename_command(dataconnectivitymanagement_cli, dataconnectivitymanagement_cli.data_entity_group, dataconnectivitymanagement_cli.create_data_preview_data_entity_from_view, "create-data-preview-view")


# oci data-connectivity data-entity create-data-profile-data-entity-from-data-store -> oci data-connectivity data-entity create-data-profile-ds
cli_util.rename_command(dataconnectivitymanagement_cli, dataconnectivitymanagement_cli.data_entity_group, dataconnectivitymanagement_cli.create_data_profile_data_entity_from_data_store, "create-data-profile-ds")


# oci data-connectivity data-entity create-data-profile-data-entity-from-file -> oci data-connectivity data-entity create-data-profile-file
cli_util.rename_command(dataconnectivitymanagement_cli, dataconnectivitymanagement_cli.data_entity_group, dataconnectivitymanagement_cli.create_data_profile_data_entity_from_file, "create-data-profile-file")


# oci data-connectivity data-entity create-data-profile-data-entity-from-sql -> oci data-connectivity data-entity create-data-profile-sql
cli_util.rename_command(dataconnectivitymanagement_cli, dataconnectivitymanagement_cli.data_entity_group, dataconnectivitymanagement_cli.create_data_profile_data_entity_from_sql, "create-data-profile-sql")


# oci data-connectivity data-entity create-data-profile-data-entity-from-table -> oci data-connectivity data-entity create-data-profile-table
cli_util.rename_command(dataconnectivitymanagement_cli, dataconnectivitymanagement_cli.data_entity_group, dataconnectivitymanagement_cli.create_data_profile_data_entity_from_table, "create-data-profile-table")


# oci data-connectivity data-entity create-data-profile-data-entity-from-view -> oci data-connectivity data-entity create-data-profile-view
cli_util.rename_command(dataconnectivitymanagement_cli, dataconnectivitymanagement_cli.data_entity_group, dataconnectivitymanagement_cli.create_data_profile_data_entity_from_view, "create-data-profile-view")


# oci data-connectivity data-entity create-entity-shape-create-entity-shape-from-data-store -> oci data-connectivity data-entity create-entity-shape-ds
cli_util.rename_command(dataconnectivitymanagement_cli, dataconnectivitymanagement_cli.data_entity_group, dataconnectivitymanagement_cli.create_entity_shape_create_entity_shape_from_data_store, "create-entity-shape-ds")


# oci data-connectivity data-entity create-entity-shape-create-entity-shape-from-file -> oci data-connectivity data-entity create-entity-shape-file
cli_util.rename_command(dataconnectivitymanagement_cli, dataconnectivitymanagement_cli.data_entity_group, dataconnectivitymanagement_cli.create_entity_shape_create_entity_shape_from_file, "create-entity-shape-file")


# oci data-connectivity data-entity create-entity-shape-create-entity-shape-from-sql -> oci data-connectivity data-entity create-entity-shape-sql
cli_util.rename_command(dataconnectivitymanagement_cli, dataconnectivitymanagement_cli.data_entity_group, dataconnectivitymanagement_cli.create_entity_shape_create_entity_shape_from_sql, "create-entity-shape-sql")


# oci data-connectivity data-entity create-entity-shape-create-entity-shape-from-table -> oci data-connectivity data-entity create-entity-shape-table
cli_util.rename_command(dataconnectivitymanagement_cli, dataconnectivitymanagement_cli.data_entity_group, dataconnectivitymanagement_cli.create_entity_shape_create_entity_shape_from_table, "create-entity-shape-table")


# oci data-connectivity data-entity create-entity-shape-create-entity-shape-from-view -> oci data-connectivity data-entity create-entity-shape-view
cli_util.rename_command(dataconnectivitymanagement_cli, dataconnectivitymanagement_cli.data_entity_group, dataconnectivitymanagement_cli.create_entity_shape_create_entity_shape_from_view, "create-entity-shape-view")


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.delete_connection_validation, params_to_exclude=['connection_validation_key'])
@dataconnectivitymanagement_cli.connection_validation_group.command(name=dataconnectivitymanagement_cli.delete_connection_validation.name, help=dataconnectivitymanagement_cli.delete_connection_validation.help)
@cli_util.option('--key', required=True, help=u"""The key of the connection validation. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_connection_validation_extended(ctx, **kwargs):
    if 'key' in kwargs:
        kwargs['connection_validation_key'] = kwargs['key']
        kwargs.pop('key')

    ctx.invoke(dataconnectivitymanagement_cli.delete_connection_validation, **kwargs)


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.get_connection_validation, params_to_exclude=['connection_validation_key'])
@dataconnectivitymanagement_cli.connection_validation_group.command(name=dataconnectivitymanagement_cli.get_connection_validation.name, help=dataconnectivitymanagement_cli.get_connection_validation.help)
@cli_util.option('--key', required=True, help=u"""The key of the connection validation. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'ConnectionValidation'})
@cli_util.wrap_exceptions
def get_connection_validation_extended(ctx, **kwargs):
    if 'key' in kwargs:
        kwargs['connection_validation_key'] = kwargs['key']
        kwargs.pop('key')

    ctx.invoke(dataconnectivitymanagement_cli.get_connection_validation, **kwargs)


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.create_data_preview_data_entity_from_data_store, params_to_exclude=['data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_is_effective_date_disabled', 'data_entity_is_flex_data_store', 'data_entity_is_silent_error', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name', 'data_entity_supports_incremental', 'data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_is_effective_date_disabled', 'data_entity_is_flex_data_store', 'data_entity_is_silent_error', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name', 'data_entity_supports_incremental'])
@dataconnectivitymanagement_cli.data_entity_group.command(name=dataconnectivitymanagement_cli.create_data_preview_data_entity_from_data_store.name, help=dataconnectivitymanagement_cli.create_data_preview_data_entity_from_data_store.help)
@cli_util.option('--external-key', help="""The external key for the object""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help="""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--effective-date-disabled', type=click.BOOL, help="""It shows whether or not effective date is disabled""")
@cli_util.option('--is-flex', type=click.BOOL, help="""It shows whether the datastore is of flex type""")
@cli_util.option('--is-silent-error', type=click.BOOL, help="""It shows whether the extraction of this datastore will stop on error""")
@cli_util.option('--model-version', help="""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help="""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help="""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--label', help="""Specifies other type label.""")
@cli_util.option('--resource-name', help="""The resource name.""")
@cli_util.option('--supports-incremental', type=click.BOOL, help="""It shows whether the datastore supports Incremental Extract or not.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-date-disabled', type=click.BOOL, help=u"""It shows whether or not effective date is disabled""")
@cli_util.option('--is-flex-data-store', type=click.BOOL, help=u"""It shows whether the datastore is of flex type""")
@cli_util.option('--is-silent-error', type=click.BOOL, help=u"""It shows whether the extraction of this datastore will stop on error""")
@cli_util.option('--model-version', help=u"""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--resource-name', help=u"""The resource name.""")
@cli_util.option('--supports-incremental', type=click.BOOL, help=u"""It shows whether the datastore supports Incremental Extract or not.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataPreview'})
@cli_util.wrap_exceptions
def create_data_preview_data_entity_from_data_store_extended(ctx, **kwargs):

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'effective_date_disabled' in kwargs:
        kwargs['data_entity_is_effective_date_disabled'] = kwargs['effective_date_disabled']
        kwargs.pop('effective_date_disabled')

    if 'is_flex' in kwargs:
        kwargs['data_entity_is_flex_data_store'] = kwargs['is_flex']
        kwargs.pop('is_flex')

    if 'is_silent_error' in kwargs:
        kwargs['data_entity_is_silent_error'] = kwargs['is_silent_error']
        kwargs.pop('is_silent_error')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['label']
        kwargs.pop('label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    if 'supports_incremental' in kwargs:
        kwargs['data_entity_supports_incremental'] = kwargs['supports_incremental']
        kwargs.pop('supports_incremental')

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'is_date_disabled' in kwargs:
        kwargs['data_entity_is_effective_date_disabled'] = kwargs['is_date_disabled']
        kwargs.pop('is_date_disabled')

    if 'is_flex_data_store' in kwargs:
        kwargs['data_entity_is_flex_data_store'] = kwargs['is_flex_data_store']
        kwargs.pop('is_flex_data_store')

    if 'is_silent_error' in kwargs:
        kwargs['data_entity_is_silent_error'] = kwargs['is_silent_error']
        kwargs.pop('is_silent_error')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'other_type_label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['other_type_label']
        kwargs.pop('other_type_label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    if 'supports_incremental' in kwargs:
        kwargs['data_entity_supports_incremental'] = kwargs['supports_incremental']
        kwargs.pop('supports_incremental')

    ctx.invoke(dataconnectivitymanagement_cli.create_data_preview_data_entity_from_data_store, **kwargs)


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.create_data_preview_data_entity_from_file, params_to_exclude=['data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name', 'data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name'])
@dataconnectivitymanagement_cli.data_entity_group.command(name=dataconnectivitymanagement_cli.create_data_preview_data_entity_from_file.name, help=dataconnectivitymanagement_cli.create_data_preview_data_entity_from_file.help)
@cli_util.option('--external-key', help="""The external key for the object.""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help="""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help="""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help="""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help="""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--label', help="""Specifies other type label.""")
@cli_util.option('--resource-name', help="""The resource name.""")
@cli_util.option('--external-key', help=u"""The external key for the object.""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help=u"""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--type-label', help=u"""Specifies other type label.""")
@cli_util.option('--resource-name', help=u"""The resource name.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'data-entity-data-format': {'module': 'data_connectivity', 'class': 'DataFormat'}}, output_type={'module': 'data_connectivity', 'class': 'DataPreview'})
@cli_util.wrap_exceptions
def create_data_preview_data_entity_from_file_extended(ctx, **kwargs):

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['label']
        kwargs.pop('label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'type_label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['type_label']
        kwargs.pop('type_label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    ctx.invoke(dataconnectivitymanagement_cli.create_data_preview_data_entity_from_file, **kwargs)


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.create_data_preview_data_entity_from_sql, params_to_exclude=['data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name', 'data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name'])
@dataconnectivitymanagement_cli.data_entity_group.command(name=dataconnectivitymanagement_cli.create_data_preview_data_entity_from_sql.name, help=dataconnectivitymanagement_cli.create_data_preview_data_entity_from_sql.help)
@cli_util.option('--external-key', help="""The external key for the object""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help="""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help="""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help="""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help="""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--label', help="""Specifies other type label.""")
@cli_util.option('--resource-name', help="""The resource name.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help=u"""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--type-label', help=u"""Specifies other type label.""")
@cli_util.option('--resource-name', help=u"""The resource name.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataPreview'})
@cli_util.wrap_exceptions
def create_data_preview_data_entity_from_sql_extended(ctx, **kwargs):

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['label']
        kwargs.pop('label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'type_label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['type_label']
        kwargs.pop('type_label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    ctx.invoke(dataconnectivitymanagement_cli.create_data_preview_data_entity_from_sql, **kwargs)


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.create_data_preview_data_entity_from_table, params_to_exclude=['data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name', 'data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name'])
@dataconnectivitymanagement_cli.data_entity_group.command(name=dataconnectivitymanagement_cli.create_data_preview_data_entity_from_table.name, help=dataconnectivitymanagement_cli.create_data_preview_data_entity_from_table.help)
@cli_util.option('--external-key', help="""The external key for the object.""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help="""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help="""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help="""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help="""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--label', help="""Specifies other type label.""")
@cli_util.option('--resource-name', help="""The resource name.""")
@cli_util.option('--external-key', help=u"""The external key for the object.""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help=u"""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--type-label', help=u"""Specifies other type label.""")
@cli_util.option('--resource-name', help=u"""The resource name.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataPreview'})
@cli_util.wrap_exceptions
def create_data_preview_data_entity_from_table_extended(ctx, **kwargs):

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['label']
        kwargs.pop('label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'type_label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['type_label']
        kwargs.pop('type_label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    ctx.invoke(dataconnectivitymanagement_cli.create_data_preview_data_entity_from_table, **kwargs)


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.create_data_preview_data_entity_from_view, params_to_exclude=['data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name', 'data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name'])
@dataconnectivitymanagement_cli.data_entity_group.command(name=dataconnectivitymanagement_cli.create_data_preview_data_entity_from_view.name, help=dataconnectivitymanagement_cli.create_data_preview_data_entity_from_view.help)
@cli_util.option('--external-key', help="""The external key for the object""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help="""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help="""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help="""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help="""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--label', help="""Specifies other type label.""")
@cli_util.option('--resource-name', help="""The resource name.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help=u"""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--type-label', help=u"""Specifies other type label.""")
@cli_util.option('--resource-name', help=u"""The resource name.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataPreview'})
@cli_util.wrap_exceptions
def create_data_preview_data_entity_from_view_extended(ctx, **kwargs):

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['label']
        kwargs.pop('label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'type_label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['type_label']
        kwargs.pop('type_label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    ctx.invoke(dataconnectivitymanagement_cli.create_data_preview_data_entity_from_view, **kwargs)


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.create_data_profile_data_entity_from_data_store, params_to_exclude=['data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_is_effective_date_disabled', 'data_entity_is_flex_data_store', 'data_entity_is_silent_error', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name', 'data_entity_supports_incremental', 'data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_is_effective_date_disabled', 'data_entity_is_flex_data_store', 'data_entity_is_silent_error', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name', 'data_entity_supports_incremental'])
@dataconnectivitymanagement_cli.data_entity_group.command(name=dataconnectivitymanagement_cli.create_data_profile_data_entity_from_data_store.name, help=dataconnectivitymanagement_cli.create_data_profile_data_entity_from_data_store.help)
@cli_util.option('--external-key', help="""The external key for the object""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help="""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--effective-date-disabled', type=click.BOOL, help="""It shows whether or not effective date is disabled""")
@cli_util.option('--is-flex', type=click.BOOL, help="""It shows whether the datastore is of flex type""")
@cli_util.option('--is-silent-error', type=click.BOOL, help="""It shows whether the extraction of this datastore will stop on error""")
@cli_util.option('--model-version', help="""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help="""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help="""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--label', help="""Specifies other type label.""")
@cli_util.option('--resource-name', help="""The resource name.""")
@cli_util.option('--supports-incremental', type=click.BOOL, help="""It shows whether the datastore supports Incremental Extract or not.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-date-disabled', type=click.BOOL, help=u"""It shows whether or not effective date is disabled""")
@cli_util.option('--is-flex-data-store', type=click.BOOL, help=u"""It shows whether the datastore is of flex type""")
@cli_util.option('--is-silent-error', type=click.BOOL, help=u"""It shows whether the extraction of this datastore will stop on error""")
@cli_util.option('--model-version', help=u"""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--type-label', help=u"""Specifies other type label.""")
@cli_util.option('--resource-name', help=u"""The resource name.""")
@cli_util.option('--supports-incremental', type=click.BOOL, help=u"""It shows whether the datastore supports Incremental Extract or not.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataProfile'})
@cli_util.wrap_exceptions
def create_data_profile_data_entity_from_data_store_extended(ctx, **kwargs):

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'effective_date_disabled' in kwargs:
        kwargs['data_entity_is_effective_date_disabled'] = kwargs['effective_date_disabled']
        kwargs.pop('effective_date_disabled')

    if 'is_flex' in kwargs:
        kwargs['data_entity_is_flex_data_store'] = kwargs['is_flex']
        kwargs.pop('is_flex')

    if 'is_silent_error' in kwargs:
        kwargs['data_entity_is_silent_error'] = kwargs['is_silent_error']
        kwargs.pop('is_silent_error')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['label']
        kwargs.pop('label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    if 'supports_incremental' in kwargs:
        kwargs['data_entity_supports_incremental'] = kwargs['supports_incremental']
        kwargs.pop('supports_incremental')

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'is_date_disabled' in kwargs:
        kwargs['data_entity_is_effective_date_disabled'] = kwargs['is_date_disabled']
        kwargs.pop('is_date_disabled')

    if 'is_flex_data_store' in kwargs:
        kwargs['data_entity_is_flex_data_store'] = kwargs['is_flex_data_store']
        kwargs.pop('is_flex_data_store')

    if 'is_silent_error' in kwargs:
        kwargs['data_entity_is_silent_error'] = kwargs['is_silent_error']
        kwargs.pop('is_silent_error')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'type_label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['type_label']
        kwargs.pop('type_label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    if 'supports_incremental' in kwargs:
        kwargs['data_entity_supports_incremental'] = kwargs['supports_incremental']
        kwargs.pop('supports_incremental')

    ctx.invoke(dataconnectivitymanagement_cli.create_data_profile_data_entity_from_data_store, **kwargs)


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.create_data_profile_data_entity_from_file, params_to_exclude=['data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name', 'data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name'])
@dataconnectivitymanagement_cli.data_entity_group.command(name=dataconnectivitymanagement_cli.create_data_profile_data_entity_from_file.name, help=dataconnectivitymanagement_cli.create_data_profile_data_entity_from_file.help)
@cli_util.option('--external-key', help="""The external key for the object.""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help="""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help="""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help="""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help="""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--label', help="""Specifies other type label.""")
@cli_util.option('--resource-name', help="""The resource name.""")
@cli_util.option('--external-key', help=u"""The external key for the object.""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help=u"""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--type-label', help=u"""Specifies other type label.""")
@cli_util.option('--resource-name', help=u"""The resource name.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'data-entity-data-format': {'module': 'data_connectivity', 'class': 'DataFormat'}}, output_type={'module': 'data_connectivity', 'class': 'DataProfile'})
@cli_util.wrap_exceptions
def create_data_profile_data_entity_from_file_extended(ctx, **kwargs):

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['label']
        kwargs.pop('label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'type_label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['type_label']
        kwargs.pop('type_label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    ctx.invoke(dataconnectivitymanagement_cli.create_data_profile_data_entity_from_file, **kwargs)


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.create_data_profile_data_entity_from_sql, params_to_exclude=['data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name', 'data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name'])
@dataconnectivitymanagement_cli.data_entity_group.command(name=dataconnectivitymanagement_cli.create_data_profile_data_entity_from_sql.name, help=dataconnectivitymanagement_cli.create_data_profile_data_entity_from_sql.help)
@cli_util.option('--external-key', help="""The external key for the object""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help="""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help="""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help="""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help="""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--label', help="""Specifies other type label.""")
@cli_util.option('--resource-name', help="""The resource name.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help=u"""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--type-label', help=u"""Specifies other type label.""")
@cli_util.option('--resource-name', help=u"""The resource name.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataProfile'})
@cli_util.wrap_exceptions
def create_data_profile_data_entity_from_sql_extended(ctx, **kwargs):

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['label']
        kwargs.pop('label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'type_label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['type_label']
        kwargs.pop('type_label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    ctx.invoke(dataconnectivitymanagement_cli.create_data_profile_data_entity_from_sql, **kwargs)


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.create_data_profile_data_entity_from_table, params_to_exclude=['data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name', 'data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name'])
@dataconnectivitymanagement_cli.data_entity_group.command(name=dataconnectivitymanagement_cli.create_data_profile_data_entity_from_table.name, help=dataconnectivitymanagement_cli.create_data_profile_data_entity_from_table.help)
@cli_util.option('--external-key', help="""The external key for the object.""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help="""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help="""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help="""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help="""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--label', help="""Specifies other type label.""")
@cli_util.option('--resource-name', help="""The resource name.""")
@cli_util.option('--external-key', help=u"""The external key for the object.""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help=u"""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--type-label', help=u"""Specifies other type label.""")
@cli_util.option('--resource-name', help=u"""The resource name.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataProfile'})
@cli_util.wrap_exceptions
def create_data_profile_data_entity_from_table_extended(ctx, **kwargs):

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['label']
        kwargs.pop('label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'type_label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['type_label']
        kwargs.pop('type_label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    ctx.invoke(dataconnectivitymanagement_cli.create_data_profile_data_entity_from_table, **kwargs)


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.create_data_profile_data_entity_from_view, params_to_exclude=['data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name', 'data_entity_external_key', 'data_entity_foreign_keys', 'data_entity_model_version', 'data_entity_object_status', 'data_entity_object_version', 'data_entity_other_type_label', 'data_entity_resource_name'])
@dataconnectivitymanagement_cli.data_entity_group.command(name=dataconnectivitymanagement_cli.create_data_profile_data_entity_from_view.name, help=dataconnectivitymanagement_cli.create_data_profile_data_entity_from_view.help)
@cli_util.option('--external-key', help="""The external key for the object""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help="""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help="""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help="""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help="""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--label', help="""Specifies other type label.""")
@cli_util.option('--resource-name', help="""The resource name.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--model-version', help=u"""The object's model version.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--type-label', help=u"""Specifies other type label.""")
@cli_util.option('--resource-name', help=u"""The resource name.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataProfile'})
@cli_util.wrap_exceptions
def create_data_profile_data_entity_from_view_extended(ctx, **kwargs):

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['label']
        kwargs.pop('label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    if 'external_key' in kwargs:
        kwargs['data_entity_external_key'] = kwargs['external_key']
        kwargs.pop('external_key')

    if 'foreign_keys' in kwargs:
        kwargs['data_entity_foreign_keys'] = kwargs['foreign_keys']
        kwargs.pop('foreign_keys')

    if 'model_version' in kwargs:
        kwargs['data_entity_model_version'] = kwargs['model_version']
        kwargs.pop('model_version')

    if 'object_status' in kwargs:
        kwargs['data_entity_object_status'] = kwargs['object_status']
        kwargs.pop('object_status')

    if 'object_version' in kwargs:
        kwargs['data_entity_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    if 'type_label' in kwargs:
        kwargs['data_entity_other_type_label'] = kwargs['type_label']
        kwargs.pop('type_label')

    if 'resource_name' in kwargs:
        kwargs['data_entity_resource_name'] = kwargs['resource_name']
        kwargs.pop('resource_name')

    ctx.invoke(dataconnectivitymanagement_cli.create_data_profile_data_entity_from_view, **kwargs)


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.get_execute_operation_job, params_to_exclude=['execute_operation_job_key'])
@dataconnectivitymanagement_cli.execute_operation_job_group.command(name=dataconnectivitymanagement_cli.get_execute_operation_job.name, help=dataconnectivitymanagement_cli.get_execute_operation_job.help)
@cli_util.option('--job-key', required=True, help=u"""Job id returned by execute operation job api [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'ExecuteOperationJob'})
@cli_util.wrap_exceptions
def get_execute_operation_job_extended(ctx, **kwargs):
    if 'job_key' in kwargs:
        kwargs['execute_operation_job_key'] = kwargs['job_key']
        kwargs.pop('job_key')

    ctx.invoke(dataconnectivitymanagement_cli.get_execute_operation_job, **kwargs)


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.create_execute_operation_job_operation_from_procedure, params_to_exclude=['operation_object_version'])
@dataconnectivitymanagement_cli.execute_operation_job_details_group.command(name=dataconnectivitymanagement_cli.create_execute_operation_job_operation_from_procedure.name, help=dataconnectivitymanagement_cli.create_execute_operation_job_operation_from_procedure.help)
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'call-operation-config': {'module': 'data_connectivity', 'class': 'CallOperationConfig'}, 'input-records': {'module': 'data_connectivity', 'class': 'list[OperationInputRecord]'}, 'operation-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'operation-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'operation-shape': {'module': 'data_connectivity', 'class': 'Shape'}}, output_type={'module': 'data_connectivity', 'class': 'ExecuteOperationJobDetails'})
@cli_util.wrap_exceptions
def create_execute_operation_job_operation_from_procedure_extended(ctx, **kwargs):
    if 'object_version' in kwargs:
        kwargs['operation_object_version'] = kwargs['object_version']
        kwargs.pop('object_version')

    ctx.invoke(dataconnectivitymanagement_cli.create_execute_operation_job_operation_from_procedure, **kwargs)


@cli_util.copy_params_from_generated_command(dataconnectivitymanagement_cli.delete_network_connectivity_status, params_to_exclude=['network_validation_status_key'])
@dataconnectivitymanagement_cli.test_network_connectivity_group.command(name=dataconnectivitymanagement_cli.delete_network_connectivity_status.name, help=dataconnectivitymanagement_cli.delete_network_connectivity_status.help)
@cli_util.option('--status-key', required=True, help=u"""NetworkValidationStatus key. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_network_connectivity_status_extended(ctx, **kwargs):
    if 'status_key' in kwargs:
        kwargs['network_validation_status_key'] = kwargs['status_key']
        kwargs.pop('status_key')

    ctx.invoke(dataconnectivitymanagement_cli.delete_network_connectivity_status, **kwargs)


# Move commands under 'oci data-connectivity data-connectivity-management' -> 'oci data-connectivity'
data_connectivity_service_cli.data_connectivity_service_group.commands.pop(dataconnectivitymanagement_cli.data_connectivity_management_root_group.name)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.schema_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.full_push_down_task_response_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.connection_validation_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.data_profile_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.work_request_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.type_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.work_request_log_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.endpoint_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.connectivity_validation_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.data_entity_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.execute_operation_job_details_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.types_summary_collection_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.test_network_connectivity_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.operation_summary_collection_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.data_asset_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.work_request_error_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.reference_info_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.connection_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.registry_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.detach_data_asset_info_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.data_preview_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.execute_operation_job_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.reference_artifact_summary_collection_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.folder_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.operation_group)
data_connectivity_service_cli.data_connectivity_service_group.add_command(dataconnectivitymanagement_cli.attach_data_asset_info_group)
