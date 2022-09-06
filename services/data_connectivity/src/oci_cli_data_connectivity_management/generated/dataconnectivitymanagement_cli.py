# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.data_connectivity.src.oci_cli_data_connectivity.generated import data_connectivity_service_cli


@click.command(cli_util.override('data_connectivity_management.data_connectivity_management_root_group.command_name', 'data-connectivity-management'), cls=CommandGroupWithAlias, help=cli_util.override('data_connectivity_management.data_connectivity_management_root_group.help', """Use the Data Connectivity Management Service APIs to perform common extract, load, and transform (ETL) tasks."""), short_help=cli_util.override('data_connectivity_management.data_connectivity_management_root_group.short_help', """Data Connectivity Management API"""))
@cli_util.help_option_group
def data_connectivity_management_root_group():
    pass


@click.command(cli_util.override('data_connectivity_management.schema_group.command_name', 'schema'), cls=CommandGroupWithAlias, help="""The schema object.""")
@cli_util.help_option_group
def schema_group():
    pass


@click.command(cli_util.override('data_connectivity_management.full_push_down_task_response_group.command_name', 'full-push-down-task-response'), cls=CommandGroupWithAlias, help="""The full pushdown task.""")
@cli_util.help_option_group
def full_push_down_task_response_group():
    pass


@click.command(cli_util.override('data_connectivity_management.connection_validation_group.command_name', 'connection-validation'), cls=CommandGroupWithAlias, help="""The information about connection validation.""")
@cli_util.help_option_group
def connection_validation_group():
    pass


@click.command(cli_util.override('data_connectivity_management.data_profile_group.command_name', 'data-profile'), cls=CommandGroupWithAlias, help="""The data profile response.""")
@cli_util.help_option_group
def data_profile_group():
    pass


@click.command(cli_util.override('data_connectivity_management.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of the status of the work request.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('data_connectivity_management.type_group.command_name', 'type'), cls=CommandGroupWithAlias, help="""DataAsset and Connection Registry Attributes""")
@cli_util.help_option_group
def type_group():
    pass


@click.command(cli_util.override('data_connectivity_management.work_request_log_group.command_name', 'work-request-log'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_group():
    pass


@click.command(cli_util.override('data_connectivity_management.endpoint_group.command_name', 'endpoint'), cls=CommandGroupWithAlias, help="""An endpoint is an organizational construct to keep multiple data connectivity management solutions and their resources (pe-id, dnsProxyIp, dnsZones, and so on) separate from each other, helping you to stay organized. For example, you could have separate registries for development, testing, and production.""")
@cli_util.help_option_group
def endpoint_group():
    pass


@click.command(cli_util.override('data_connectivity_management.connectivity_validation_group.command_name', 'connectivity-validation'), cls=CommandGroupWithAlias, help="""The information about connectivity validation results.""")
@cli_util.help_option_group
def connectivity_validation_group():
    pass


@click.command(cli_util.override('data_connectivity_management.data_entity_group.command_name', 'data-entity'), cls=CommandGroupWithAlias, help="""The data entity object.""")
@cli_util.help_option_group
def data_entity_group():
    pass


@click.command(cli_util.override('data_connectivity_management.execute_operation_job_details_group.command_name', 'execute-operation-job-details'), cls=CommandGroupWithAlias, help="""Contains details of executeOperationJob.""")
@cli_util.help_option_group
def execute_operation_job_details_group():
    pass


@click.command(cli_util.override('data_connectivity_management.types_summary_collection_group.command_name', 'types-summary-collection'), cls=CommandGroupWithAlias, help="""This is the collection of type summaries.""")
@cli_util.help_option_group
def types_summary_collection_group():
    pass


@click.command(cli_util.override('data_connectivity_management.test_network_connectivity_group.command_name', 'test-network-connectivity'), cls=CommandGroupWithAlias, help="""The network validation response.""")
@cli_util.help_option_group
def test_network_connectivity_group():
    pass


@click.command(cli_util.override('data_connectivity_management.operation_summary_collection_group.command_name', 'operation-summary-collection'), cls=CommandGroupWithAlias, help="""This is the collection of operation summaries, with minimal details of an operation.""")
@cli_util.help_option_group
def operation_summary_collection_group():
    pass


@click.command(cli_util.override('data_connectivity_management.data_asset_group.command_name', 'data-asset'), cls=CommandGroupWithAlias, help="""Represents a data source in the Data Integration service.""")
@cli_util.help_option_group
def data_asset_group():
    pass


@click.command(cli_util.override('data_connectivity_management.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('data_connectivity_management.reference_info_group.command_name', 'reference-info'), cls=CommandGroupWithAlias, help="""Represents reference details of a DCMS artifact.""")
@cli_util.help_option_group
def reference_info_group():
    pass


@click.command(cli_util.override('data_connectivity_management.connection_group.command_name', 'connection'), cls=CommandGroupWithAlias, help="""The connection for a data asset.""")
@cli_util.help_option_group
def connection_group():
    pass


@click.command(cli_util.override('data_connectivity_management.config_details_group.command_name', 'config-details'), cls=CommandGroupWithAlias, help="""The connector-specific engine configurations.""")
@cli_util.help_option_group
def config_details_group():
    pass


@click.command(cli_util.override('data_connectivity_management.derived_entity_group.command_name', 'derived-entity'), cls=CommandGroupWithAlias, help="""The Derive entity object""")
@cli_util.help_option_group
def derived_entity_group():
    pass


@click.command(cli_util.override('data_connectivity_management.registry_group.command_name', 'registry'), cls=CommandGroupWithAlias, help="""A registry is an organizational construct to keep multiple data connectivity management solutions and their resources (data assets, data flows, tasks, and so on) separate from each other, helping you to stay organized. For example, you could have separate registries for development, testing, and production.""")
@cli_util.help_option_group
def registry_group():
    pass


@click.command(cli_util.override('data_connectivity_management.detach_data_asset_info_group.command_name', 'detach-data-asset-info'), cls=CommandGroupWithAlias, help="""The detach DataAsset response.""")
@cli_util.help_option_group
def detach_data_asset_info_group():
    pass


@click.command(cli_util.override('data_connectivity_management.data_preview_group.command_name', 'data-preview'), cls=CommandGroupWithAlias, help="""The data preview response.""")
@cli_util.help_option_group
def data_preview_group():
    pass


@click.command(cli_util.override('data_connectivity_management.execute_operation_job_group.command_name', 'execute-operation-job'), cls=CommandGroupWithAlias, help="""Response of executeOperationJob.""")
@cli_util.help_option_group
def execute_operation_job_group():
    pass


@click.command(cli_util.override('data_connectivity_management.reference_artifact_summary_collection_group.command_name', 'reference-artifact-summary-collection'), cls=CommandGroupWithAlias, help="""This is the collection of reference details summaries; it can be a collection of lightweight details or full definitions.""")
@cli_util.help_option_group
def reference_artifact_summary_collection_group():
    pass


@click.command(cli_util.override('data_connectivity_management.folder_group.command_name', 'folder'), cls=CommandGroupWithAlias, help="""The folder for a data asset.""")
@cli_util.help_option_group
def folder_group():
    pass


@click.command(cli_util.override('data_connectivity_management.operation_group.command_name', 'operation'), cls=CommandGroupWithAlias, help="""The operation object.""")
@cli_util.help_option_group
def operation_group():
    pass


@click.command(cli_util.override('data_connectivity_management.attach_data_asset_info_group.command_name', 'attach-data-asset-info'), cls=CommandGroupWithAlias, help="""The attach DataAsset response.""")
@cli_util.help_option_group
def attach_data_asset_info_group():
    pass


data_connectivity_service_cli.data_connectivity_service_group.add_command(data_connectivity_management_root_group)
data_connectivity_management_root_group.add_command(schema_group)
data_connectivity_management_root_group.add_command(full_push_down_task_response_group)
data_connectivity_management_root_group.add_command(connection_validation_group)
data_connectivity_management_root_group.add_command(data_profile_group)
data_connectivity_management_root_group.add_command(work_request_group)
data_connectivity_management_root_group.add_command(type_group)
data_connectivity_management_root_group.add_command(work_request_log_group)
data_connectivity_management_root_group.add_command(endpoint_group)
data_connectivity_management_root_group.add_command(connectivity_validation_group)
data_connectivity_management_root_group.add_command(data_entity_group)
data_connectivity_management_root_group.add_command(execute_operation_job_details_group)
data_connectivity_management_root_group.add_command(types_summary_collection_group)
data_connectivity_management_root_group.add_command(test_network_connectivity_group)
data_connectivity_management_root_group.add_command(operation_summary_collection_group)
data_connectivity_management_root_group.add_command(data_asset_group)
data_connectivity_management_root_group.add_command(work_request_error_group)
data_connectivity_management_root_group.add_command(reference_info_group)
data_connectivity_management_root_group.add_command(connection_group)
data_connectivity_management_root_group.add_command(config_details_group)
data_connectivity_management_root_group.add_command(derived_entity_group)
data_connectivity_management_root_group.add_command(registry_group)
data_connectivity_management_root_group.add_command(detach_data_asset_info_group)
data_connectivity_management_root_group.add_command(data_preview_group)
data_connectivity_management_root_group.add_command(execute_operation_job_group)
data_connectivity_management_root_group.add_command(reference_artifact_summary_collection_group)
data_connectivity_management_root_group.add_command(folder_group)
data_connectivity_management_root_group.add_command(operation_group)
data_connectivity_management_root_group.add_command(attach_data_asset_info_group)


@endpoint_group.command(name=cli_util.override('data_connectivity_management.change_endpoint_compartment.command_name', 'change-compartment'), help=u"""The endpoint will be moved to the specified compartment. \n[Command Reference](changeEndpointCompartment)""")
@cli_util.option('--endpoint-id', required=True, help=u"""DCMS endpoint ID.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier""")
@cli_util.option('--registry-id', help=u"""DCMS registry ID""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_endpoint_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, endpoint_id, compartment_id, registry_id, if_match):

    if isinstance(endpoint_id, six.string_types) and len(endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if registry_id is not None:
        kwargs['registry_id'] = registry_id
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.change_endpoint_compartment(
        endpoint_id=endpoint_id,
        change_endpoint_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@registry_group.command(name=cli_util.override('data_connectivity_management.change_registry_compartment.command_name', 'change-compartment'), help=u"""The registry will be moved to the specified compartment. \n[Command Reference](changeRegistryCompartment)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_registry_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, registry_id, compartment_id, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.change_registry_compartment(
        registry_id=registry_id,
        change_registry_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@attach_data_asset_info_group.command(name=cli_util.override('data_connectivity_management.create_attach_data_asset.command_name', 'create-attach-data-asset'), help=u"""Attaches a list of data assets to the given endpoint. \n[Command Reference](createAttachDataAsset)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--endpoint-id', required=True, help=u"""DCMS endpoint ID.""")
@cli_util.option('--data-assets', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The array of DataAsset keys.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@json_skeleton_utils.get_cli_json_input_option({'data-assets': {'module': 'data_connectivity', 'class': 'list[DataAsset]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'data-assets': {'module': 'data_connectivity', 'class': 'list[DataAsset]'}}, output_type={'module': 'data_connectivity', 'class': 'AttachDataAssetInfo'})
@cli_util.wrap_exceptions
def create_attach_data_asset(ctx, from_json, registry_id, endpoint_id, data_assets, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(endpoint_id, six.string_types) and len(endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataAssets'] = cli_util.parse_json_parameter("data_assets", data_assets)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_attach_data_asset(
        registry_id=registry_id,
        endpoint_id=endpoint_id,
        create_attach_data_asset_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_connectivity_management.create_connection.command_name', 'create'), help=u"""Creates a connection under an existing data asset. \n[Command Reference](createConnection)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--properties', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""All the properties of the connection in a key-value map format.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', required=True, help=u"""Specific Connection Type""")
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify the connection. In scenarios where reference to the connection is required, a value can be passed in create.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--model-type', help=u"""The type of the object.""")
@cli_util.option('--description', help=u"""User-defined description of the connection.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--primary-schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties of the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-default', type=click.BOOL, help=u"""The default property of the connection.""")
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'primary-schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'connection-properties': {'module': 'data_connectivity', 'class': 'list[ConnectionProperty]'}, 'properties': {'module': 'data_connectivity', 'class': 'dict(str, object)'}, 'metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'registry-metadata': {'module': 'data_connectivity', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'primary-schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'connection-properties': {'module': 'data_connectivity', 'class': 'list[ConnectionProperty]'}, 'properties': {'module': 'data_connectivity', 'class': 'dict(str, object)'}, 'metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'registry-metadata': {'module': 'data_connectivity', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_connectivity', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection(ctx, from_json, registry_id, name, identifier, properties, type, key, model_version, model_type, description, object_version, object_status, primary_schema, connection_properties, is_default, metadata, registry_metadata):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier
    _details['properties'] = cli_util.parse_json_parameter("properties", properties)
    _details['type'] = type

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if model_type is not None:
        _details['modelType'] = model_type

    if description is not None:
        _details['description'] = description

    if object_version is not None:
        _details['objectVersion'] = object_version

    if object_status is not None:
        _details['objectStatus'] = object_status

    if primary_schema is not None:
        _details['primarySchema'] = cli_util.parse_json_parameter("primary_schema", primary_schema)

    if connection_properties is not None:
        _details['connectionProperties'] = cli_util.parse_json_parameter("connection_properties", connection_properties)

    if is_default is not None:
        _details['isDefault'] = is_default

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_connection(
        registry_id=registry_id,
        create_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_validation_group.command(name=cli_util.override('data_connectivity_management.create_connection_validation.command_name', 'create'), help=u"""Creates a connection validation. \n[Command Reference](createConnectionValidation)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({'data-asset': {'module': 'data_connectivity', 'class': 'CreateDataAssetDetails'}, 'connection': {'module': 'data_connectivity', 'class': 'CreateConnectionDetails'}, 'registry-metadata': {'module': 'data_connectivity', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'data-asset': {'module': 'data_connectivity', 'class': 'CreateDataAssetDetails'}, 'connection': {'module': 'data_connectivity', 'class': 'CreateConnectionDetails'}, 'registry-metadata': {'module': 'data_connectivity', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_connectivity', 'class': 'ConnectionValidation'})
@cli_util.wrap_exceptions
def create_connection_validation(ctx, from_json, registry_id, data_asset, connection, registry_metadata, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_connection_validation(
        registry_id=registry_id,
        create_connection_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connectivity_validation_group.command(name=cli_util.override('data_connectivity_management.create_connectivity_validation.command_name', 'create'), help=u"""This endpoint is used to trigger validation of dataAsset, connection, schema, entity, dataOperationConfig \n[Command Reference](createConnectivityValidation)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--model-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SOURCE_OPERATOR", "TARGET_OPERATOR"]), help=u"""The model type of the operator.""")
@cli_util.option('--key', help=u"""The key of the object.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--description', help=u"""Details about the operator.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--input-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of input ports.

This option is a JSON list with items of type InputPort.  For documentation on InputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/InputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of output ports.

This option is a JSON list with items of type OutputPort.  For documentation on OutputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/OutputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of parameters used in the data flow.

This option is a JSON list with items of type Parameter.  For documentation on Parameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/Parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--op-config-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_connectivity', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_connectivity', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_connectivity', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_connectivity', 'class': 'ConfigValues'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_connectivity', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_connectivity', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_connectivity', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_connectivity', 'class': 'ConfigValues'}}, output_type={'module': 'data_connectivity', 'class': 'ConnectivityValidation'})
@cli_util.wrap_exceptions
def create_connectivity_validation(ctx, from_json, registry_id, model_type, key, model_version, parent_ref, name, description, object_version, input_ports, output_ports, object_status, identifier, parameters, op_config_values, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelType'] = model_type

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_version is not None:
        _details['objectVersion'] = object_version

    if input_ports is not None:
        _details['inputPorts'] = cli_util.parse_json_parameter("input_ports", input_ports)

    if output_ports is not None:
        _details['outputPorts'] = cli_util.parse_json_parameter("output_ports", output_ports)

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if op_config_values is not None:
        _details['opConfigValues'] = cli_util.parse_json_parameter("op_config_values", op_config_values)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_connectivity_validation(
        registry_id=registry_id,
        create_connectivity_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connectivity_validation_group.command(name=cli_util.override('data_connectivity_management.create_connectivity_validation_target.command_name', 'create-connectivity-validation-target'), help=u"""This endpoint is used to trigger validation of dataAsset, connection, schema, entity, dataOperationConfig \n[Command Reference](createConnectivityValidation)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--entity', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--key', help=u"""The key of the object.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--description', help=u"""Details about the operator.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--input-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of input ports.

This option is a JSON list with items of type InputPort.  For documentation on InputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/InputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of output ports.

This option is a JSON list with items of type OutputPort.  For documentation on OutputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/OutputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of parameters used in the data flow.

This option is a JSON list with items of type Parameter.  For documentation on Parameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/Parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--op-config-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-read-access', type=click.BOOL, help=u"""Specifies the read access.""")
@cli_util.option('--is-copy-fields', type=click.BOOL, help=u"""Specifies the copy fields.""")
@cli_util.option('--is-predefined-shape', type=click.BOOL, help=u"""Specifies if this uses a predefined shape.""")
@cli_util.option('--data-property', type=custom_types.CliCaseInsensitiveChoice(["TRUNCATE", "MERGE", "BACKUP", "OVERWRITE", "APPEND", "IGNORE"]), help=u"""Specifies the data property.""")
@cli_util.option('--schema-drift-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--fixed-data-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--write-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_connectivity', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_connectivity', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_connectivity', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_connectivity', 'class': 'ConfigValues'}, 'entity': {'module': 'data_connectivity', 'class': 'DataEntity'}, 'schema-drift-config': {'module': 'data_connectivity', 'class': 'SchemaDriftConfig'}, 'fixed-data-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'write-operation-config': {'module': 'data_connectivity', 'class': 'WriteOperationConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_connectivity', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_connectivity', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_connectivity', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_connectivity', 'class': 'ConfigValues'}, 'entity': {'module': 'data_connectivity', 'class': 'DataEntity'}, 'schema-drift-config': {'module': 'data_connectivity', 'class': 'SchemaDriftConfig'}, 'fixed-data-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'write-operation-config': {'module': 'data_connectivity', 'class': 'WriteOperationConfig'}}, output_type={'module': 'data_connectivity', 'class': 'ConnectivityValidation'})
@cli_util.wrap_exceptions
def create_connectivity_validation_target(ctx, from_json, registry_id, entity, key, model_version, parent_ref, name, description, object_version, input_ports, output_ports, object_status, identifier, parameters, op_config_values, is_read_access, is_copy_fields, is_predefined_shape, data_property, schema_drift_config, fixed_data_shape, write_operation_config, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['entity'] = cli_util.parse_json_parameter("entity", entity)

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_version is not None:
        _details['objectVersion'] = object_version

    if input_ports is not None:
        _details['inputPorts'] = cli_util.parse_json_parameter("input_ports", input_ports)

    if output_ports is not None:
        _details['outputPorts'] = cli_util.parse_json_parameter("output_ports", output_ports)

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if op_config_values is not None:
        _details['opConfigValues'] = cli_util.parse_json_parameter("op_config_values", op_config_values)

    if is_read_access is not None:
        _details['isReadAccess'] = is_read_access

    if is_copy_fields is not None:
        _details['isCopyFields'] = is_copy_fields

    if is_predefined_shape is not None:
        _details['isPredefinedShape'] = is_predefined_shape

    if data_property is not None:
        _details['dataProperty'] = data_property

    if schema_drift_config is not None:
        _details['schemaDriftConfig'] = cli_util.parse_json_parameter("schema_drift_config", schema_drift_config)

    if fixed_data_shape is not None:
        _details['fixedDataShape'] = cli_util.parse_json_parameter("fixed_data_shape", fixed_data_shape)

    if write_operation_config is not None:
        _details['writeOperationConfig'] = cli_util.parse_json_parameter("write_operation_config", write_operation_config)

    _details['modelType'] = 'TARGET_OPERATOR'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_connectivity_validation(
        registry_id=registry_id,
        create_connectivity_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connectivity_validation_group.command(name=cli_util.override('data_connectivity_management.create_connectivity_validation_source.command_name', 'create-connectivity-validation-source'), help=u"""This endpoint is used to trigger validation of dataAsset, connection, schema, entity, dataOperationConfig \n[Command Reference](createConnectivityValidation)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--entity', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--key', help=u"""The key of the object.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--description', help=u"""Details about the operator.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--input-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of input ports.

This option is a JSON list with items of type InputPort.  For documentation on InputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/InputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of output ports.

This option is a JSON list with items of type OutputPort.  For documentation on OutputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/OutputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of parameters used in the data flow.

This option is a JSON list with items of type Parameter.  For documentation on Parameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/Parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--op-config-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-read-access', type=click.BOOL, help=u"""Specifies the read access.""")
@cli_util.option('--is-copy-fields', type=click.BOOL, help=u"""Specifies the copy fields.""")
@cli_util.option('--is-predefined-shape', type=click.BOOL, help=u"""Specifies if this uses a predefined shape.""")
@cli_util.option('--schema-drift-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--fixed-data-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--read-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_connectivity', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_connectivity', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_connectivity', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_connectivity', 'class': 'ConfigValues'}, 'entity': {'module': 'data_connectivity', 'class': 'DataEntity'}, 'schema-drift-config': {'module': 'data_connectivity', 'class': 'SchemaDriftConfig'}, 'fixed-data-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_connectivity', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_connectivity', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_connectivity', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_connectivity', 'class': 'ConfigValues'}, 'entity': {'module': 'data_connectivity', 'class': 'DataEntity'}, 'schema-drift-config': {'module': 'data_connectivity', 'class': 'SchemaDriftConfig'}, 'fixed-data-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}}, output_type={'module': 'data_connectivity', 'class': 'ConnectivityValidation'})
@cli_util.wrap_exceptions
def create_connectivity_validation_source(ctx, from_json, registry_id, entity, key, model_version, parent_ref, name, description, object_version, input_ports, output_ports, object_status, identifier, parameters, op_config_values, is_read_access, is_copy_fields, is_predefined_shape, schema_drift_config, fixed_data_shape, read_operation_config, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['entity'] = cli_util.parse_json_parameter("entity", entity)

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_version is not None:
        _details['objectVersion'] = object_version

    if input_ports is not None:
        _details['inputPorts'] = cli_util.parse_json_parameter("input_ports", input_ports)

    if output_ports is not None:
        _details['outputPorts'] = cli_util.parse_json_parameter("output_ports", output_ports)

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if op_config_values is not None:
        _details['opConfigValues'] = cli_util.parse_json_parameter("op_config_values", op_config_values)

    if is_read_access is not None:
        _details['isReadAccess'] = is_read_access

    if is_copy_fields is not None:
        _details['isCopyFields'] = is_copy_fields

    if is_predefined_shape is not None:
        _details['isPredefinedShape'] = is_predefined_shape

    if schema_drift_config is not None:
        _details['schemaDriftConfig'] = cli_util.parse_json_parameter("schema_drift_config", schema_drift_config)

    if fixed_data_shape is not None:
        _details['fixedDataShape'] = cli_util.parse_json_parameter("fixed_data_shape", fixed_data_shape)

    if read_operation_config is not None:
        _details['readOperationConfig'] = cli_util.parse_json_parameter("read_operation_config", read_operation_config)

    _details['modelType'] = 'SOURCE_OPERATOR'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_connectivity_validation(
        registry_id=registry_id,
        create_connectivity_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_connectivity_management.create_data_asset.command_name', 'create'), help=u"""Creates a data asset with default connection. \n[Command Reference](createDataAsset)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--properties', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""All the properties for the data asset in a key-value map format.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', required=True, help=u"""Specific DataAsset Type""")
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify the data asset.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--model-type', help=u"""The type of the object.""")
@cli_util.option('--description', help=u"""User-defined description of the data asset.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--external-key', help=u"""The external key of the object.""")
@cli_util.option('--asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional properties for the data asset.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--native-type-system', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--default-connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--end-points', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of endpoints with which this data asset is associated.

This option is a JSON list with items of type DpEndpoint.  For documentation on DpEndpoint please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/DpEndpoint.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'asset-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'properties': {'module': 'data_connectivity', 'class': 'dict(str, object)'}, 'native-type-system': {'module': 'data_connectivity', 'class': 'TypeSystem'}, 'registry-metadata': {'module': 'data_connectivity', 'class': 'RegistryMetadata'}, 'metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'default-connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'end-points': {'module': 'data_connectivity', 'class': 'list[DpEndpoint]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'properties': {'module': 'data_connectivity', 'class': 'dict(str, object)'}, 'native-type-system': {'module': 'data_connectivity', 'class': 'TypeSystem'}, 'registry-metadata': {'module': 'data_connectivity', 'class': 'RegistryMetadata'}, 'metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'default-connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'end-points': {'module': 'data_connectivity', 'class': 'list[DpEndpoint]'}}, output_type={'module': 'data_connectivity', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def create_data_asset(ctx, from_json, registry_id, name, identifier, properties, type, key, model_version, model_type, description, object_status, object_version, external_key, asset_properties, native_type_system, registry_metadata, metadata, default_connection, end_points):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier
    _details['properties'] = cli_util.parse_json_parameter("properties", properties)
    _details['type'] = type

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if model_type is not None:
        _details['modelType'] = model_type

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if object_version is not None:
        _details['objectVersion'] = object_version

    if external_key is not None:
        _details['externalKey'] = external_key

    if asset_properties is not None:
        _details['assetProperties'] = cli_util.parse_json_parameter("asset_properties", asset_properties)

    if native_type_system is not None:
        _details['nativeTypeSystem'] = cli_util.parse_json_parameter("native_type_system", native_type_system)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if default_connection is not None:
        _details['defaultConnection'] = cli_util.parse_json_parameter("default_connection", default_connection)

    if end_points is not None:
        _details['endPoints'] = cli_util.parse_json_parameter("end_points", end_points)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_data_asset(
        registry_id=registry_id,
        create_data_asset_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_preview_group.command(name=cli_util.override('data_connectivity_management.create_data_preview.command_name', 'create'), help=u"""Provide data preview on live schema. \n[Command Reference](createDataPreview)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--read-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity': {'module': 'data_connectivity', 'class': 'DataEntity'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity': {'module': 'data_connectivity', 'class': 'DataEntity'}}, output_type={'module': 'data_connectivity', 'class': 'DataPreview'})
@cli_util.wrap_exceptions
def create_data_preview(ctx, from_json, registry_id, read_operation_config, data_asset, connection, schema, data_entity, if_match, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if read_operation_config is not None:
        _details['readOperationConfig'] = cli_util.parse_json_parameter("read_operation_config", read_operation_config)

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if schema is not None:
        _details['schema'] = cli_util.parse_json_parameter("schema", schema)

    if data_entity is not None:
        _details['dataEntity'] = cli_util.parse_json_parameter("data_entity", data_entity)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_data_preview(
        registry_id=registry_id,
        create_data_preview_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_preview_group.command(name=cli_util.override('data_connectivity_management.create_data_preview_data_entity_from_table.command_name', 'create-data-preview-data-entity-from-table'), help=u"""Provide data preview on live schema. \n[Command Reference](createDataPreview)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--read-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--data-entity-entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-key', help=u"""The object key.""")
@cli_util.option('--data-entity-model-version', help=u"""The model version of the object.""")
@cli_util.option('--data-entity-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--data-entity-description', help=u"""Detailed description of the object.""")
@cli_util.option('--data-entity-object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--data-entity-external-key', help=u"""The external key of the object.""")
@cli_util.option('--data-entity-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-shape-id', help=u"""The shape ID.""")
@cli_util.option('--data-entity-entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--data-entity-other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--data-entity-unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-resource-name', help=u"""The resource name.""")
@cli_util.option('--data-entity-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--data-entity-identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@json_skeleton_utils.get_cli_json_input_option({'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataPreview'})
@cli_util.wrap_exceptions
def create_data_preview_data_entity_from_table(ctx, from_json, registry_id, read_operation_config, data_asset, connection, schema, if_match, endpoint_id, data_entity_entity_properties, data_entity_metadata, data_entity_key, data_entity_model_version, data_entity_parent_ref, data_entity_name, data_entity_description, data_entity_object_version, data_entity_external_key, data_entity_shape, data_entity_shape_id, data_entity_entity_type, data_entity_other_type_label, data_entity_unique_keys, data_entity_foreign_keys, data_entity_resource_name, data_entity_object_status, data_entity_identifier):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataEntity'] = {}

    if read_operation_config is not None:
        _details['readOperationConfig'] = cli_util.parse_json_parameter("read_operation_config", read_operation_config)

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if schema is not None:
        _details['schema'] = cli_util.parse_json_parameter("schema", schema)

    if data_entity_entity_properties is not None:
        _details['dataEntity']['entityProperties'] = cli_util.parse_json_parameter("data_entity_entity_properties", data_entity_entity_properties)

    if data_entity_metadata is not None:
        _details['dataEntity']['metadata'] = cli_util.parse_json_parameter("data_entity_metadata", data_entity_metadata)

    if data_entity_key is not None:
        _details['dataEntity']['key'] = data_entity_key

    if data_entity_model_version is not None:
        _details['dataEntity']['modelVersion'] = data_entity_model_version

    if data_entity_parent_ref is not None:
        _details['dataEntity']['parentRef'] = cli_util.parse_json_parameter("data_entity_parent_ref", data_entity_parent_ref)

    if data_entity_name is not None:
        _details['dataEntity']['name'] = data_entity_name

    if data_entity_description is not None:
        _details['dataEntity']['description'] = data_entity_description

    if data_entity_object_version is not None:
        _details['dataEntity']['objectVersion'] = data_entity_object_version

    if data_entity_external_key is not None:
        _details['dataEntity']['externalKey'] = data_entity_external_key

    if data_entity_shape is not None:
        _details['dataEntity']['shape'] = cli_util.parse_json_parameter("data_entity_shape", data_entity_shape)

    if data_entity_shape_id is not None:
        _details['dataEntity']['shapeId'] = data_entity_shape_id

    if data_entity_entity_type is not None:
        _details['dataEntity']['entityType'] = data_entity_entity_type

    if data_entity_other_type_label is not None:
        _details['dataEntity']['otherTypeLabel'] = data_entity_other_type_label

    if data_entity_unique_keys is not None:
        _details['dataEntity']['uniqueKeys'] = cli_util.parse_json_parameter("data_entity_unique_keys", data_entity_unique_keys)

    if data_entity_foreign_keys is not None:
        _details['dataEntity']['foreignKeys'] = cli_util.parse_json_parameter("data_entity_foreign_keys", data_entity_foreign_keys)

    if data_entity_resource_name is not None:
        _details['dataEntity']['resourceName'] = data_entity_resource_name

    if data_entity_object_status is not None:
        _details['dataEntity']['objectStatus'] = data_entity_object_status

    if data_entity_identifier is not None:
        _details['dataEntity']['identifier'] = data_entity_identifier

    _details['dataEntity']['modelType'] = 'TABLE_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_data_preview(
        registry_id=registry_id,
        create_data_preview_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_preview_group.command(name=cli_util.override('data_connectivity_management.create_data_preview_data_entity_from_data_store.command_name', 'create-data-preview-data-entity-from-data-store'), help=u"""Provide data preview on live schema. \n[Command Reference](createDataPreview)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--read-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--data-entity-entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-key', help=u"""The object key.""")
@cli_util.option('--data-entity-model-version', help=u"""The model version of the object.""")
@cli_util.option('--data-entity-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--data-entity-description', help=u"""Detailed description of the object.""")
@cli_util.option('--data-entity-object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--data-entity-external-key', help=u"""The external key of the object.""")
@cli_util.option('--data-entity-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-shape-id', help=u"""The shape ID.""")
@cli_util.option('--data-entity-entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--data-entity-other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--data-entity-unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-resource-name', help=u"""The resource name.""")
@cli_util.option('--data-entity-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--data-entity-identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--data-entity-filters', help=u"""Filters present in the datastore. It can be null.""")
@cli_util.option('--data-entity-is-effective-date-disabled', type=click.BOOL, help=u"""It shows whether the effective date is disabled.""")
@cli_util.option('--data-entity-is-flex-data-store', type=click.BOOL, help=u"""It shows whether the datastore is of flex type.""")
@cli_util.option('--data-entity-is-silent-error', type=click.BOOL, help=u"""It shows whether the extraction of this datastore will stop when an error occurs.""")
@cli_util.option('--data-entity-supports-incremental', type=click.BOOL, help=u"""It shows whether the datastore supports incremental extract.""")
@json_skeleton_utils.get_cli_json_input_option({'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataPreview'})
@cli_util.wrap_exceptions
def create_data_preview_data_entity_from_data_store(ctx, from_json, registry_id, read_operation_config, data_asset, connection, schema, if_match, endpoint_id, data_entity_entity_properties, data_entity_metadata, data_entity_key, data_entity_model_version, data_entity_parent_ref, data_entity_name, data_entity_description, data_entity_object_version, data_entity_external_key, data_entity_shape, data_entity_shape_id, data_entity_entity_type, data_entity_other_type_label, data_entity_unique_keys, data_entity_foreign_keys, data_entity_resource_name, data_entity_object_status, data_entity_identifier, data_entity_filters, data_entity_is_effective_date_disabled, data_entity_is_flex_data_store, data_entity_is_silent_error, data_entity_supports_incremental):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataEntity'] = {}

    if read_operation_config is not None:
        _details['readOperationConfig'] = cli_util.parse_json_parameter("read_operation_config", read_operation_config)

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if schema is not None:
        _details['schema'] = cli_util.parse_json_parameter("schema", schema)

    if data_entity_entity_properties is not None:
        _details['dataEntity']['entityProperties'] = cli_util.parse_json_parameter("data_entity_entity_properties", data_entity_entity_properties)

    if data_entity_metadata is not None:
        _details['dataEntity']['metadata'] = cli_util.parse_json_parameter("data_entity_metadata", data_entity_metadata)

    if data_entity_key is not None:
        _details['dataEntity']['key'] = data_entity_key

    if data_entity_model_version is not None:
        _details['dataEntity']['modelVersion'] = data_entity_model_version

    if data_entity_parent_ref is not None:
        _details['dataEntity']['parentRef'] = cli_util.parse_json_parameter("data_entity_parent_ref", data_entity_parent_ref)

    if data_entity_name is not None:
        _details['dataEntity']['name'] = data_entity_name

    if data_entity_description is not None:
        _details['dataEntity']['description'] = data_entity_description

    if data_entity_object_version is not None:
        _details['dataEntity']['objectVersion'] = data_entity_object_version

    if data_entity_external_key is not None:
        _details['dataEntity']['externalKey'] = data_entity_external_key

    if data_entity_shape is not None:
        _details['dataEntity']['shape'] = cli_util.parse_json_parameter("data_entity_shape", data_entity_shape)

    if data_entity_shape_id is not None:
        _details['dataEntity']['shapeId'] = data_entity_shape_id

    if data_entity_entity_type is not None:
        _details['dataEntity']['entityType'] = data_entity_entity_type

    if data_entity_other_type_label is not None:
        _details['dataEntity']['otherTypeLabel'] = data_entity_other_type_label

    if data_entity_unique_keys is not None:
        _details['dataEntity']['uniqueKeys'] = cli_util.parse_json_parameter("data_entity_unique_keys", data_entity_unique_keys)

    if data_entity_foreign_keys is not None:
        _details['dataEntity']['foreignKeys'] = cli_util.parse_json_parameter("data_entity_foreign_keys", data_entity_foreign_keys)

    if data_entity_resource_name is not None:
        _details['dataEntity']['resourceName'] = data_entity_resource_name

    if data_entity_object_status is not None:
        _details['dataEntity']['objectStatus'] = data_entity_object_status

    if data_entity_identifier is not None:
        _details['dataEntity']['identifier'] = data_entity_identifier

    if data_entity_filters is not None:
        _details['dataEntity']['filters'] = data_entity_filters

    if data_entity_is_effective_date_disabled is not None:
        _details['dataEntity']['isEffectiveDateDisabled'] = data_entity_is_effective_date_disabled

    if data_entity_is_flex_data_store is not None:
        _details['dataEntity']['isFlexDataStore'] = data_entity_is_flex_data_store

    if data_entity_is_silent_error is not None:
        _details['dataEntity']['isSilentError'] = data_entity_is_silent_error

    if data_entity_supports_incremental is not None:
        _details['dataEntity']['supportsIncremental'] = data_entity_supports_incremental

    _details['dataEntity']['modelType'] = 'DATA_STORE_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_data_preview(
        registry_id=registry_id,
        create_data_preview_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_preview_group.command(name=cli_util.override('data_connectivity_management.create_data_preview_data_entity_from_view.command_name', 'create-data-preview-data-entity-from-view'), help=u"""Provide data preview on live schema. \n[Command Reference](createDataPreview)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--read-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--data-entity-entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-key', help=u"""The object key.""")
@cli_util.option('--data-entity-model-version', help=u"""The model version of the object.""")
@cli_util.option('--data-entity-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--data-entity-description', help=u"""Detailed description of the object.""")
@cli_util.option('--data-entity-object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--data-entity-external-key', help=u"""The external key of the object.""")
@cli_util.option('--data-entity-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-shape-id', help=u"""The shape ID.""")
@cli_util.option('--data-entity-entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--data-entity-other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--data-entity-unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-resource-name', help=u"""The resource name.""")
@cli_util.option('--data-entity-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--data-entity-identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@json_skeleton_utils.get_cli_json_input_option({'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataPreview'})
@cli_util.wrap_exceptions
def create_data_preview_data_entity_from_view(ctx, from_json, registry_id, read_operation_config, data_asset, connection, schema, if_match, endpoint_id, data_entity_entity_properties, data_entity_metadata, data_entity_key, data_entity_model_version, data_entity_parent_ref, data_entity_name, data_entity_description, data_entity_object_version, data_entity_external_key, data_entity_shape, data_entity_shape_id, data_entity_entity_type, data_entity_other_type_label, data_entity_unique_keys, data_entity_foreign_keys, data_entity_resource_name, data_entity_object_status, data_entity_identifier):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataEntity'] = {}

    if read_operation_config is not None:
        _details['readOperationConfig'] = cli_util.parse_json_parameter("read_operation_config", read_operation_config)

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if schema is not None:
        _details['schema'] = cli_util.parse_json_parameter("schema", schema)

    if data_entity_entity_properties is not None:
        _details['dataEntity']['entityProperties'] = cli_util.parse_json_parameter("data_entity_entity_properties", data_entity_entity_properties)

    if data_entity_metadata is not None:
        _details['dataEntity']['metadata'] = cli_util.parse_json_parameter("data_entity_metadata", data_entity_metadata)

    if data_entity_key is not None:
        _details['dataEntity']['key'] = data_entity_key

    if data_entity_model_version is not None:
        _details['dataEntity']['modelVersion'] = data_entity_model_version

    if data_entity_parent_ref is not None:
        _details['dataEntity']['parentRef'] = cli_util.parse_json_parameter("data_entity_parent_ref", data_entity_parent_ref)

    if data_entity_name is not None:
        _details['dataEntity']['name'] = data_entity_name

    if data_entity_description is not None:
        _details['dataEntity']['description'] = data_entity_description

    if data_entity_object_version is not None:
        _details['dataEntity']['objectVersion'] = data_entity_object_version

    if data_entity_external_key is not None:
        _details['dataEntity']['externalKey'] = data_entity_external_key

    if data_entity_shape is not None:
        _details['dataEntity']['shape'] = cli_util.parse_json_parameter("data_entity_shape", data_entity_shape)

    if data_entity_shape_id is not None:
        _details['dataEntity']['shapeId'] = data_entity_shape_id

    if data_entity_entity_type is not None:
        _details['dataEntity']['entityType'] = data_entity_entity_type

    if data_entity_other_type_label is not None:
        _details['dataEntity']['otherTypeLabel'] = data_entity_other_type_label

    if data_entity_unique_keys is not None:
        _details['dataEntity']['uniqueKeys'] = cli_util.parse_json_parameter("data_entity_unique_keys", data_entity_unique_keys)

    if data_entity_foreign_keys is not None:
        _details['dataEntity']['foreignKeys'] = cli_util.parse_json_parameter("data_entity_foreign_keys", data_entity_foreign_keys)

    if data_entity_resource_name is not None:
        _details['dataEntity']['resourceName'] = data_entity_resource_name

    if data_entity_object_status is not None:
        _details['dataEntity']['objectStatus'] = data_entity_object_status

    if data_entity_identifier is not None:
        _details['dataEntity']['identifier'] = data_entity_identifier

    _details['dataEntity']['modelType'] = 'VIEW_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_data_preview(
        registry_id=registry_id,
        create_data_preview_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_preview_group.command(name=cli_util.override('data_connectivity_management.create_data_preview_data_entity_from_sql.command_name', 'create-data-preview-data-entity-from-sql'), help=u"""Provide data preview on live schema. \n[Command Reference](createDataPreview)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--read-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--data-entity-entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-key', help=u"""The object key.""")
@cli_util.option('--data-entity-model-version', help=u"""The model version of the object.""")
@cli_util.option('--data-entity-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--data-entity-description', help=u"""Detailed description of the object.""")
@cli_util.option('--data-entity-object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--data-entity-external-key', help=u"""The external key of the object.""")
@cli_util.option('--data-entity-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-shape-id', help=u"""The shape ID.""")
@cli_util.option('--data-entity-entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--data-entity-other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--data-entity-unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-resource-name', help=u"""The resource name.""")
@cli_util.option('--data-entity-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--data-entity-identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--data-entity-sql-query', help=u"""sqlQuery""")
@json_skeleton_utils.get_cli_json_input_option({'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataPreview'})
@cli_util.wrap_exceptions
def create_data_preview_data_entity_from_sql(ctx, from_json, registry_id, read_operation_config, data_asset, connection, schema, if_match, endpoint_id, data_entity_entity_properties, data_entity_metadata, data_entity_key, data_entity_model_version, data_entity_parent_ref, data_entity_name, data_entity_description, data_entity_object_version, data_entity_external_key, data_entity_shape, data_entity_shape_id, data_entity_entity_type, data_entity_other_type_label, data_entity_unique_keys, data_entity_foreign_keys, data_entity_resource_name, data_entity_object_status, data_entity_identifier, data_entity_sql_query):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataEntity'] = {}

    if read_operation_config is not None:
        _details['readOperationConfig'] = cli_util.parse_json_parameter("read_operation_config", read_operation_config)

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if schema is not None:
        _details['schema'] = cli_util.parse_json_parameter("schema", schema)

    if data_entity_entity_properties is not None:
        _details['dataEntity']['entityProperties'] = cli_util.parse_json_parameter("data_entity_entity_properties", data_entity_entity_properties)

    if data_entity_metadata is not None:
        _details['dataEntity']['metadata'] = cli_util.parse_json_parameter("data_entity_metadata", data_entity_metadata)

    if data_entity_key is not None:
        _details['dataEntity']['key'] = data_entity_key

    if data_entity_model_version is not None:
        _details['dataEntity']['modelVersion'] = data_entity_model_version

    if data_entity_parent_ref is not None:
        _details['dataEntity']['parentRef'] = cli_util.parse_json_parameter("data_entity_parent_ref", data_entity_parent_ref)

    if data_entity_name is not None:
        _details['dataEntity']['name'] = data_entity_name

    if data_entity_description is not None:
        _details['dataEntity']['description'] = data_entity_description

    if data_entity_object_version is not None:
        _details['dataEntity']['objectVersion'] = data_entity_object_version

    if data_entity_external_key is not None:
        _details['dataEntity']['externalKey'] = data_entity_external_key

    if data_entity_shape is not None:
        _details['dataEntity']['shape'] = cli_util.parse_json_parameter("data_entity_shape", data_entity_shape)

    if data_entity_shape_id is not None:
        _details['dataEntity']['shapeId'] = data_entity_shape_id

    if data_entity_entity_type is not None:
        _details['dataEntity']['entityType'] = data_entity_entity_type

    if data_entity_other_type_label is not None:
        _details['dataEntity']['otherTypeLabel'] = data_entity_other_type_label

    if data_entity_unique_keys is not None:
        _details['dataEntity']['uniqueKeys'] = cli_util.parse_json_parameter("data_entity_unique_keys", data_entity_unique_keys)

    if data_entity_foreign_keys is not None:
        _details['dataEntity']['foreignKeys'] = cli_util.parse_json_parameter("data_entity_foreign_keys", data_entity_foreign_keys)

    if data_entity_resource_name is not None:
        _details['dataEntity']['resourceName'] = data_entity_resource_name

    if data_entity_object_status is not None:
        _details['dataEntity']['objectStatus'] = data_entity_object_status

    if data_entity_identifier is not None:
        _details['dataEntity']['identifier'] = data_entity_identifier

    if data_entity_sql_query is not None:
        _details['dataEntity']['sqlQuery'] = data_entity_sql_query

    _details['dataEntity']['modelType'] = 'SQL_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_data_preview(
        registry_id=registry_id,
        create_data_preview_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_preview_group.command(name=cli_util.override('data_connectivity_management.create_data_preview_data_entity_from_file.command_name', 'create-data-preview-data-entity-from-file'), help=u"""Provide data preview on live schema. \n[Command Reference](createDataPreview)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--read-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--data-entity-entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-key', help=u"""The object key.""")
@cli_util.option('--data-entity-model-version', help=u"""The model version of the object.""")
@cli_util.option('--data-entity-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--data-entity-description', help=u"""Detailed description of the object.""")
@cli_util.option('--data-entity-object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--data-entity-external-key', help=u"""The external key of the object.""")
@cli_util.option('--data-entity-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-shape-id', help=u"""The shape ID.""")
@cli_util.option('--data-entity-entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--data-entity-other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--data-entity-unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-resource-name', help=u"""The resource name.""")
@cli_util.option('--data-entity-data-format', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--data-entity-identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@json_skeleton_utils.get_cli_json_input_option({'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'data-entity-data-format': {'module': 'data_connectivity', 'class': 'DataFormat'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'data-entity-data-format': {'module': 'data_connectivity', 'class': 'DataFormat'}}, output_type={'module': 'data_connectivity', 'class': 'DataPreview'})
@cli_util.wrap_exceptions
def create_data_preview_data_entity_from_file(ctx, from_json, registry_id, read_operation_config, data_asset, connection, schema, if_match, endpoint_id, data_entity_entity_properties, data_entity_metadata, data_entity_key, data_entity_model_version, data_entity_parent_ref, data_entity_name, data_entity_description, data_entity_object_version, data_entity_external_key, data_entity_shape, data_entity_shape_id, data_entity_entity_type, data_entity_other_type_label, data_entity_unique_keys, data_entity_foreign_keys, data_entity_resource_name, data_entity_data_format, data_entity_object_status, data_entity_identifier):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataEntity'] = {}

    if read_operation_config is not None:
        _details['readOperationConfig'] = cli_util.parse_json_parameter("read_operation_config", read_operation_config)

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if schema is not None:
        _details['schema'] = cli_util.parse_json_parameter("schema", schema)

    if data_entity_entity_properties is not None:
        _details['dataEntity']['entityProperties'] = cli_util.parse_json_parameter("data_entity_entity_properties", data_entity_entity_properties)

    if data_entity_metadata is not None:
        _details['dataEntity']['metadata'] = cli_util.parse_json_parameter("data_entity_metadata", data_entity_metadata)

    if data_entity_key is not None:
        _details['dataEntity']['key'] = data_entity_key

    if data_entity_model_version is not None:
        _details['dataEntity']['modelVersion'] = data_entity_model_version

    if data_entity_parent_ref is not None:
        _details['dataEntity']['parentRef'] = cli_util.parse_json_parameter("data_entity_parent_ref", data_entity_parent_ref)

    if data_entity_name is not None:
        _details['dataEntity']['name'] = data_entity_name

    if data_entity_description is not None:
        _details['dataEntity']['description'] = data_entity_description

    if data_entity_object_version is not None:
        _details['dataEntity']['objectVersion'] = data_entity_object_version

    if data_entity_external_key is not None:
        _details['dataEntity']['externalKey'] = data_entity_external_key

    if data_entity_shape is not None:
        _details['dataEntity']['shape'] = cli_util.parse_json_parameter("data_entity_shape", data_entity_shape)

    if data_entity_shape_id is not None:
        _details['dataEntity']['shapeId'] = data_entity_shape_id

    if data_entity_entity_type is not None:
        _details['dataEntity']['entityType'] = data_entity_entity_type

    if data_entity_other_type_label is not None:
        _details['dataEntity']['otherTypeLabel'] = data_entity_other_type_label

    if data_entity_unique_keys is not None:
        _details['dataEntity']['uniqueKeys'] = cli_util.parse_json_parameter("data_entity_unique_keys", data_entity_unique_keys)

    if data_entity_foreign_keys is not None:
        _details['dataEntity']['foreignKeys'] = cli_util.parse_json_parameter("data_entity_foreign_keys", data_entity_foreign_keys)

    if data_entity_resource_name is not None:
        _details['dataEntity']['resourceName'] = data_entity_resource_name

    if data_entity_data_format is not None:
        _details['dataEntity']['dataFormat'] = cli_util.parse_json_parameter("data_entity_data_format", data_entity_data_format)

    if data_entity_object_status is not None:
        _details['dataEntity']['objectStatus'] = data_entity_object_status

    if data_entity_identifier is not None:
        _details['dataEntity']['identifier'] = data_entity_identifier

    _details['dataEntity']['modelType'] = 'FILE_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_data_preview(
        registry_id=registry_id,
        create_data_preview_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_preview_group.command(name=cli_util.override('data_connectivity_management.create_data_preview_derived_entity.command_name', 'create-data-preview-derived-entity'), help=u"""Provide data preview on live schema. \n[Command Reference](createDataPreview)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--data-entity-name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is unique, editable and is restricted to 1000 characters.""")
@cli_util.option('--data-entity-resource-name', required=True, help=u"""The resource name.""")
@cli_util.option('--read-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--data-entity-entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-key', help=u"""The object key.""")
@cli_util.option('--data-entity-model-version', help=u"""The object's model version.""")
@cli_util.option('--data-entity-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--data-entity-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-shape-id', help=u"""The shape ID.""")
@cli_util.option('--data-entity-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.""")
@cli_util.option('--data-entity-identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.""")
@cli_util.option('--data-entity-ref-data-object', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-mode', type=custom_types.CliCaseInsensitiveChoice(["IN", "OUT"]), help=u"""Determines whether entity is treated as source or target""")
@cli_util.option('--data-entity-derived-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Property-bag (key-value pairs where key is Shape Field resource name and value is object)""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-ref-data-object': {'module': 'data_connectivity', 'class': 'ReferencedDataObject'}, 'data-entity-derived-properties': {'module': 'data_connectivity', 'class': 'dict(str, object)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-ref-data-object': {'module': 'data_connectivity', 'class': 'ReferencedDataObject'}, 'data-entity-derived-properties': {'module': 'data_connectivity', 'class': 'dict(str, object)'}}, output_type={'module': 'data_connectivity', 'class': 'DataPreview'})
@cli_util.wrap_exceptions
def create_data_preview_derived_entity(ctx, from_json, registry_id, data_entity_name, data_entity_resource_name, read_operation_config, data_asset, connection, schema, if_match, endpoint_id, data_entity_entity_properties, data_entity_metadata, data_entity_key, data_entity_model_version, data_entity_parent_ref, data_entity_object_version, data_entity_shape, data_entity_shape_id, data_entity_object_status, data_entity_identifier, data_entity_ref_data_object, data_entity_mode, data_entity_derived_properties):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataEntity'] = {}
    _details['dataEntity']['name'] = data_entity_name
    _details['dataEntity']['resourceName'] = data_entity_resource_name

    if read_operation_config is not None:
        _details['readOperationConfig'] = cli_util.parse_json_parameter("read_operation_config", read_operation_config)

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if schema is not None:
        _details['schema'] = cli_util.parse_json_parameter("schema", schema)

    if data_entity_entity_properties is not None:
        _details['dataEntity']['entityProperties'] = cli_util.parse_json_parameter("data_entity_entity_properties", data_entity_entity_properties)

    if data_entity_metadata is not None:
        _details['dataEntity']['metadata'] = cli_util.parse_json_parameter("data_entity_metadata", data_entity_metadata)

    if data_entity_key is not None:
        _details['dataEntity']['key'] = data_entity_key

    if data_entity_model_version is not None:
        _details['dataEntity']['modelVersion'] = data_entity_model_version

    if data_entity_parent_ref is not None:
        _details['dataEntity']['parentRef'] = cli_util.parse_json_parameter("data_entity_parent_ref", data_entity_parent_ref)

    if data_entity_object_version is not None:
        _details['dataEntity']['objectVersion'] = data_entity_object_version

    if data_entity_shape is not None:
        _details['dataEntity']['shape'] = cli_util.parse_json_parameter("data_entity_shape", data_entity_shape)

    if data_entity_shape_id is not None:
        _details['dataEntity']['shapeId'] = data_entity_shape_id

    if data_entity_object_status is not None:
        _details['dataEntity']['objectStatus'] = data_entity_object_status

    if data_entity_identifier is not None:
        _details['dataEntity']['identifier'] = data_entity_identifier

    if data_entity_ref_data_object is not None:
        _details['dataEntity']['refDataObject'] = cli_util.parse_json_parameter("data_entity_ref_data_object", data_entity_ref_data_object)

    if data_entity_mode is not None:
        _details['dataEntity']['mode'] = data_entity_mode

    if data_entity_derived_properties is not None:
        _details['dataEntity']['derivedProperties'] = cli_util.parse_json_parameter("data_entity_derived_properties", data_entity_derived_properties)

    _details['dataEntity']['modelType'] = 'DERIVED_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_data_preview(
        registry_id=registry_id,
        create_data_preview_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_profile_group.command(name=cli_util.override('data_connectivity_management.create_data_profile.command_name', 'create'), help=u"""Execute data profiling on live schema. \n[Command Reference](createDataProfile)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--read-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--profile-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity': {'module': 'data_connectivity', 'class': 'DataEntity'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'data-entity': {'module': 'data_connectivity', 'class': 'DataEntity'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}}, output_type={'module': 'data_connectivity', 'class': 'DataProfile'})
@cli_util.wrap_exceptions
def create_data_profile(ctx, from_json, registry_id, read_operation_config, data_asset, connection, schema, data_entity, profile_config, if_match, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if read_operation_config is not None:
        _details['readOperationConfig'] = cli_util.parse_json_parameter("read_operation_config", read_operation_config)

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if schema is not None:
        _details['schema'] = cli_util.parse_json_parameter("schema", schema)

    if data_entity is not None:
        _details['dataEntity'] = cli_util.parse_json_parameter("data_entity", data_entity)

    if profile_config is not None:
        _details['profileConfig'] = cli_util.parse_json_parameter("profile_config", profile_config)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_data_profile(
        registry_id=registry_id,
        create_data_profile_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_profile_group.command(name=cli_util.override('data_connectivity_management.create_data_profile_data_entity_from_table.command_name', 'create-data-profile-data-entity-from-table'), help=u"""Execute data profiling on live schema. \n[Command Reference](createDataProfile)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--read-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--profile-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--data-entity-entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-key', help=u"""The object key.""")
@cli_util.option('--data-entity-model-version', help=u"""The model version of the object.""")
@cli_util.option('--data-entity-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--data-entity-description', help=u"""Detailed description of the object.""")
@cli_util.option('--data-entity-object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--data-entity-external-key', help=u"""The external key of the object.""")
@cli_util.option('--data-entity-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-shape-id', help=u"""The shape ID.""")
@cli_util.option('--data-entity-entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--data-entity-other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--data-entity-unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-resource-name', help=u"""The resource name.""")
@cli_util.option('--data-entity-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--data-entity-identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@json_skeleton_utils.get_cli_json_input_option({'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataProfile'})
@cli_util.wrap_exceptions
def create_data_profile_data_entity_from_table(ctx, from_json, registry_id, read_operation_config, data_asset, connection, schema, profile_config, if_match, endpoint_id, data_entity_entity_properties, data_entity_metadata, data_entity_key, data_entity_model_version, data_entity_parent_ref, data_entity_name, data_entity_description, data_entity_object_version, data_entity_external_key, data_entity_shape, data_entity_shape_id, data_entity_entity_type, data_entity_other_type_label, data_entity_unique_keys, data_entity_foreign_keys, data_entity_resource_name, data_entity_object_status, data_entity_identifier):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataEntity'] = {}

    if read_operation_config is not None:
        _details['readOperationConfig'] = cli_util.parse_json_parameter("read_operation_config", read_operation_config)

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if schema is not None:
        _details['schema'] = cli_util.parse_json_parameter("schema", schema)

    if profile_config is not None:
        _details['profileConfig'] = cli_util.parse_json_parameter("profile_config", profile_config)

    if data_entity_entity_properties is not None:
        _details['dataEntity']['entityProperties'] = cli_util.parse_json_parameter("data_entity_entity_properties", data_entity_entity_properties)

    if data_entity_metadata is not None:
        _details['dataEntity']['metadata'] = cli_util.parse_json_parameter("data_entity_metadata", data_entity_metadata)

    if data_entity_key is not None:
        _details['dataEntity']['key'] = data_entity_key

    if data_entity_model_version is not None:
        _details['dataEntity']['modelVersion'] = data_entity_model_version

    if data_entity_parent_ref is not None:
        _details['dataEntity']['parentRef'] = cli_util.parse_json_parameter("data_entity_parent_ref", data_entity_parent_ref)

    if data_entity_name is not None:
        _details['dataEntity']['name'] = data_entity_name

    if data_entity_description is not None:
        _details['dataEntity']['description'] = data_entity_description

    if data_entity_object_version is not None:
        _details['dataEntity']['objectVersion'] = data_entity_object_version

    if data_entity_external_key is not None:
        _details['dataEntity']['externalKey'] = data_entity_external_key

    if data_entity_shape is not None:
        _details['dataEntity']['shape'] = cli_util.parse_json_parameter("data_entity_shape", data_entity_shape)

    if data_entity_shape_id is not None:
        _details['dataEntity']['shapeId'] = data_entity_shape_id

    if data_entity_entity_type is not None:
        _details['dataEntity']['entityType'] = data_entity_entity_type

    if data_entity_other_type_label is not None:
        _details['dataEntity']['otherTypeLabel'] = data_entity_other_type_label

    if data_entity_unique_keys is not None:
        _details['dataEntity']['uniqueKeys'] = cli_util.parse_json_parameter("data_entity_unique_keys", data_entity_unique_keys)

    if data_entity_foreign_keys is not None:
        _details['dataEntity']['foreignKeys'] = cli_util.parse_json_parameter("data_entity_foreign_keys", data_entity_foreign_keys)

    if data_entity_resource_name is not None:
        _details['dataEntity']['resourceName'] = data_entity_resource_name

    if data_entity_object_status is not None:
        _details['dataEntity']['objectStatus'] = data_entity_object_status

    if data_entity_identifier is not None:
        _details['dataEntity']['identifier'] = data_entity_identifier

    _details['dataEntity']['modelType'] = 'TABLE_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_data_profile(
        registry_id=registry_id,
        create_data_profile_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_profile_group.command(name=cli_util.override('data_connectivity_management.create_data_profile_data_entity_from_data_store.command_name', 'create-data-profile-data-entity-from-data-store'), help=u"""Execute data profiling on live schema. \n[Command Reference](createDataProfile)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--read-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--profile-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--data-entity-entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-key', help=u"""The object key.""")
@cli_util.option('--data-entity-model-version', help=u"""The model version of the object.""")
@cli_util.option('--data-entity-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--data-entity-description', help=u"""Detailed description of the object.""")
@cli_util.option('--data-entity-object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--data-entity-external-key', help=u"""The external key of the object.""")
@cli_util.option('--data-entity-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-shape-id', help=u"""The shape ID.""")
@cli_util.option('--data-entity-entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--data-entity-other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--data-entity-unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-resource-name', help=u"""The resource name.""")
@cli_util.option('--data-entity-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--data-entity-identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--data-entity-filters', help=u"""Filters present in the datastore. It can be null.""")
@cli_util.option('--data-entity-is-effective-date-disabled', type=click.BOOL, help=u"""It shows whether the effective date is disabled.""")
@cli_util.option('--data-entity-is-flex-data-store', type=click.BOOL, help=u"""It shows whether the datastore is of flex type.""")
@cli_util.option('--data-entity-is-silent-error', type=click.BOOL, help=u"""It shows whether the extraction of this datastore will stop when an error occurs.""")
@cli_util.option('--data-entity-supports-incremental', type=click.BOOL, help=u"""It shows whether the datastore supports incremental extract.""")
@json_skeleton_utils.get_cli_json_input_option({'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataProfile'})
@cli_util.wrap_exceptions
def create_data_profile_data_entity_from_data_store(ctx, from_json, registry_id, read_operation_config, data_asset, connection, schema, profile_config, if_match, endpoint_id, data_entity_entity_properties, data_entity_metadata, data_entity_key, data_entity_model_version, data_entity_parent_ref, data_entity_name, data_entity_description, data_entity_object_version, data_entity_external_key, data_entity_shape, data_entity_shape_id, data_entity_entity_type, data_entity_other_type_label, data_entity_unique_keys, data_entity_foreign_keys, data_entity_resource_name, data_entity_object_status, data_entity_identifier, data_entity_filters, data_entity_is_effective_date_disabled, data_entity_is_flex_data_store, data_entity_is_silent_error, data_entity_supports_incremental):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataEntity'] = {}

    if read_operation_config is not None:
        _details['readOperationConfig'] = cli_util.parse_json_parameter("read_operation_config", read_operation_config)

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if schema is not None:
        _details['schema'] = cli_util.parse_json_parameter("schema", schema)

    if profile_config is not None:
        _details['profileConfig'] = cli_util.parse_json_parameter("profile_config", profile_config)

    if data_entity_entity_properties is not None:
        _details['dataEntity']['entityProperties'] = cli_util.parse_json_parameter("data_entity_entity_properties", data_entity_entity_properties)

    if data_entity_metadata is not None:
        _details['dataEntity']['metadata'] = cli_util.parse_json_parameter("data_entity_metadata", data_entity_metadata)

    if data_entity_key is not None:
        _details['dataEntity']['key'] = data_entity_key

    if data_entity_model_version is not None:
        _details['dataEntity']['modelVersion'] = data_entity_model_version

    if data_entity_parent_ref is not None:
        _details['dataEntity']['parentRef'] = cli_util.parse_json_parameter("data_entity_parent_ref", data_entity_parent_ref)

    if data_entity_name is not None:
        _details['dataEntity']['name'] = data_entity_name

    if data_entity_description is not None:
        _details['dataEntity']['description'] = data_entity_description

    if data_entity_object_version is not None:
        _details['dataEntity']['objectVersion'] = data_entity_object_version

    if data_entity_external_key is not None:
        _details['dataEntity']['externalKey'] = data_entity_external_key

    if data_entity_shape is not None:
        _details['dataEntity']['shape'] = cli_util.parse_json_parameter("data_entity_shape", data_entity_shape)

    if data_entity_shape_id is not None:
        _details['dataEntity']['shapeId'] = data_entity_shape_id

    if data_entity_entity_type is not None:
        _details['dataEntity']['entityType'] = data_entity_entity_type

    if data_entity_other_type_label is not None:
        _details['dataEntity']['otherTypeLabel'] = data_entity_other_type_label

    if data_entity_unique_keys is not None:
        _details['dataEntity']['uniqueKeys'] = cli_util.parse_json_parameter("data_entity_unique_keys", data_entity_unique_keys)

    if data_entity_foreign_keys is not None:
        _details['dataEntity']['foreignKeys'] = cli_util.parse_json_parameter("data_entity_foreign_keys", data_entity_foreign_keys)

    if data_entity_resource_name is not None:
        _details['dataEntity']['resourceName'] = data_entity_resource_name

    if data_entity_object_status is not None:
        _details['dataEntity']['objectStatus'] = data_entity_object_status

    if data_entity_identifier is not None:
        _details['dataEntity']['identifier'] = data_entity_identifier

    if data_entity_filters is not None:
        _details['dataEntity']['filters'] = data_entity_filters

    if data_entity_is_effective_date_disabled is not None:
        _details['dataEntity']['isEffectiveDateDisabled'] = data_entity_is_effective_date_disabled

    if data_entity_is_flex_data_store is not None:
        _details['dataEntity']['isFlexDataStore'] = data_entity_is_flex_data_store

    if data_entity_is_silent_error is not None:
        _details['dataEntity']['isSilentError'] = data_entity_is_silent_error

    if data_entity_supports_incremental is not None:
        _details['dataEntity']['supportsIncremental'] = data_entity_supports_incremental

    _details['dataEntity']['modelType'] = 'DATA_STORE_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_data_profile(
        registry_id=registry_id,
        create_data_profile_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_profile_group.command(name=cli_util.override('data_connectivity_management.create_data_profile_data_entity_from_view.command_name', 'create-data-profile-data-entity-from-view'), help=u"""Execute data profiling on live schema. \n[Command Reference](createDataProfile)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--read-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--profile-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--data-entity-entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-key', help=u"""The object key.""")
@cli_util.option('--data-entity-model-version', help=u"""The model version of the object.""")
@cli_util.option('--data-entity-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--data-entity-description', help=u"""Detailed description of the object.""")
@cli_util.option('--data-entity-object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--data-entity-external-key', help=u"""The external key of the object.""")
@cli_util.option('--data-entity-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-shape-id', help=u"""The shape ID.""")
@cli_util.option('--data-entity-entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--data-entity-other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--data-entity-unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-resource-name', help=u"""The resource name.""")
@cli_util.option('--data-entity-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--data-entity-identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@json_skeleton_utils.get_cli_json_input_option({'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataProfile'})
@cli_util.wrap_exceptions
def create_data_profile_data_entity_from_view(ctx, from_json, registry_id, read_operation_config, data_asset, connection, schema, profile_config, if_match, endpoint_id, data_entity_entity_properties, data_entity_metadata, data_entity_key, data_entity_model_version, data_entity_parent_ref, data_entity_name, data_entity_description, data_entity_object_version, data_entity_external_key, data_entity_shape, data_entity_shape_id, data_entity_entity_type, data_entity_other_type_label, data_entity_unique_keys, data_entity_foreign_keys, data_entity_resource_name, data_entity_object_status, data_entity_identifier):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataEntity'] = {}

    if read_operation_config is not None:
        _details['readOperationConfig'] = cli_util.parse_json_parameter("read_operation_config", read_operation_config)

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if schema is not None:
        _details['schema'] = cli_util.parse_json_parameter("schema", schema)

    if profile_config is not None:
        _details['profileConfig'] = cli_util.parse_json_parameter("profile_config", profile_config)

    if data_entity_entity_properties is not None:
        _details['dataEntity']['entityProperties'] = cli_util.parse_json_parameter("data_entity_entity_properties", data_entity_entity_properties)

    if data_entity_metadata is not None:
        _details['dataEntity']['metadata'] = cli_util.parse_json_parameter("data_entity_metadata", data_entity_metadata)

    if data_entity_key is not None:
        _details['dataEntity']['key'] = data_entity_key

    if data_entity_model_version is not None:
        _details['dataEntity']['modelVersion'] = data_entity_model_version

    if data_entity_parent_ref is not None:
        _details['dataEntity']['parentRef'] = cli_util.parse_json_parameter("data_entity_parent_ref", data_entity_parent_ref)

    if data_entity_name is not None:
        _details['dataEntity']['name'] = data_entity_name

    if data_entity_description is not None:
        _details['dataEntity']['description'] = data_entity_description

    if data_entity_object_version is not None:
        _details['dataEntity']['objectVersion'] = data_entity_object_version

    if data_entity_external_key is not None:
        _details['dataEntity']['externalKey'] = data_entity_external_key

    if data_entity_shape is not None:
        _details['dataEntity']['shape'] = cli_util.parse_json_parameter("data_entity_shape", data_entity_shape)

    if data_entity_shape_id is not None:
        _details['dataEntity']['shapeId'] = data_entity_shape_id

    if data_entity_entity_type is not None:
        _details['dataEntity']['entityType'] = data_entity_entity_type

    if data_entity_other_type_label is not None:
        _details['dataEntity']['otherTypeLabel'] = data_entity_other_type_label

    if data_entity_unique_keys is not None:
        _details['dataEntity']['uniqueKeys'] = cli_util.parse_json_parameter("data_entity_unique_keys", data_entity_unique_keys)

    if data_entity_foreign_keys is not None:
        _details['dataEntity']['foreignKeys'] = cli_util.parse_json_parameter("data_entity_foreign_keys", data_entity_foreign_keys)

    if data_entity_resource_name is not None:
        _details['dataEntity']['resourceName'] = data_entity_resource_name

    if data_entity_object_status is not None:
        _details['dataEntity']['objectStatus'] = data_entity_object_status

    if data_entity_identifier is not None:
        _details['dataEntity']['identifier'] = data_entity_identifier

    _details['dataEntity']['modelType'] = 'VIEW_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_data_profile(
        registry_id=registry_id,
        create_data_profile_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_profile_group.command(name=cli_util.override('data_connectivity_management.create_data_profile_data_entity_from_sql.command_name', 'create-data-profile-data-entity-from-sql'), help=u"""Execute data profiling on live schema. \n[Command Reference](createDataProfile)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--read-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--profile-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--data-entity-entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-key', help=u"""The object key.""")
@cli_util.option('--data-entity-model-version', help=u"""The model version of the object.""")
@cli_util.option('--data-entity-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--data-entity-description', help=u"""Detailed description of the object.""")
@cli_util.option('--data-entity-object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--data-entity-external-key', help=u"""The external key of the object.""")
@cli_util.option('--data-entity-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-shape-id', help=u"""The shape ID.""")
@cli_util.option('--data-entity-entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--data-entity-other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--data-entity-unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-resource-name', help=u"""The resource name.""")
@cli_util.option('--data-entity-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--data-entity-identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--data-entity-sql-query', help=u"""sqlQuery""")
@json_skeleton_utils.get_cli_json_input_option({'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}}, output_type={'module': 'data_connectivity', 'class': 'DataProfile'})
@cli_util.wrap_exceptions
def create_data_profile_data_entity_from_sql(ctx, from_json, registry_id, read_operation_config, data_asset, connection, schema, profile_config, if_match, endpoint_id, data_entity_entity_properties, data_entity_metadata, data_entity_key, data_entity_model_version, data_entity_parent_ref, data_entity_name, data_entity_description, data_entity_object_version, data_entity_external_key, data_entity_shape, data_entity_shape_id, data_entity_entity_type, data_entity_other_type_label, data_entity_unique_keys, data_entity_foreign_keys, data_entity_resource_name, data_entity_object_status, data_entity_identifier, data_entity_sql_query):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataEntity'] = {}

    if read_operation_config is not None:
        _details['readOperationConfig'] = cli_util.parse_json_parameter("read_operation_config", read_operation_config)

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if schema is not None:
        _details['schema'] = cli_util.parse_json_parameter("schema", schema)

    if profile_config is not None:
        _details['profileConfig'] = cli_util.parse_json_parameter("profile_config", profile_config)

    if data_entity_entity_properties is not None:
        _details['dataEntity']['entityProperties'] = cli_util.parse_json_parameter("data_entity_entity_properties", data_entity_entity_properties)

    if data_entity_metadata is not None:
        _details['dataEntity']['metadata'] = cli_util.parse_json_parameter("data_entity_metadata", data_entity_metadata)

    if data_entity_key is not None:
        _details['dataEntity']['key'] = data_entity_key

    if data_entity_model_version is not None:
        _details['dataEntity']['modelVersion'] = data_entity_model_version

    if data_entity_parent_ref is not None:
        _details['dataEntity']['parentRef'] = cli_util.parse_json_parameter("data_entity_parent_ref", data_entity_parent_ref)

    if data_entity_name is not None:
        _details['dataEntity']['name'] = data_entity_name

    if data_entity_description is not None:
        _details['dataEntity']['description'] = data_entity_description

    if data_entity_object_version is not None:
        _details['dataEntity']['objectVersion'] = data_entity_object_version

    if data_entity_external_key is not None:
        _details['dataEntity']['externalKey'] = data_entity_external_key

    if data_entity_shape is not None:
        _details['dataEntity']['shape'] = cli_util.parse_json_parameter("data_entity_shape", data_entity_shape)

    if data_entity_shape_id is not None:
        _details['dataEntity']['shapeId'] = data_entity_shape_id

    if data_entity_entity_type is not None:
        _details['dataEntity']['entityType'] = data_entity_entity_type

    if data_entity_other_type_label is not None:
        _details['dataEntity']['otherTypeLabel'] = data_entity_other_type_label

    if data_entity_unique_keys is not None:
        _details['dataEntity']['uniqueKeys'] = cli_util.parse_json_parameter("data_entity_unique_keys", data_entity_unique_keys)

    if data_entity_foreign_keys is not None:
        _details['dataEntity']['foreignKeys'] = cli_util.parse_json_parameter("data_entity_foreign_keys", data_entity_foreign_keys)

    if data_entity_resource_name is not None:
        _details['dataEntity']['resourceName'] = data_entity_resource_name

    if data_entity_object_status is not None:
        _details['dataEntity']['objectStatus'] = data_entity_object_status

    if data_entity_identifier is not None:
        _details['dataEntity']['identifier'] = data_entity_identifier

    if data_entity_sql_query is not None:
        _details['dataEntity']['sqlQuery'] = data_entity_sql_query

    _details['dataEntity']['modelType'] = 'SQL_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_data_profile(
        registry_id=registry_id,
        create_data_profile_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_profile_group.command(name=cli_util.override('data_connectivity_management.create_data_profile_data_entity_from_file.command_name', 'create-data-profile-data-entity-from-file'), help=u"""Execute data profiling on live schema. \n[Command Reference](createDataProfile)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--read-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--profile-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--data-entity-entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-key', help=u"""The object key.""")
@cli_util.option('--data-entity-model-version', help=u"""The model version of the object.""")
@cli_util.option('--data-entity-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--data-entity-description', help=u"""Detailed description of the object.""")
@cli_util.option('--data-entity-object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--data-entity-external-key', help=u"""The external key of the object.""")
@cli_util.option('--data-entity-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-shape-id', help=u"""The shape ID.""")
@cli_util.option('--data-entity-entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--data-entity-other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--data-entity-unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-resource-name', help=u"""The resource name.""")
@cli_util.option('--data-entity-data-format', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--data-entity-identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@json_skeleton_utils.get_cli_json_input_option({'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'data-entity-data-format': {'module': 'data_connectivity', 'class': 'DataFormat'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'data-entity-foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'data-entity-data-format': {'module': 'data_connectivity', 'class': 'DataFormat'}}, output_type={'module': 'data_connectivity', 'class': 'DataProfile'})
@cli_util.wrap_exceptions
def create_data_profile_data_entity_from_file(ctx, from_json, registry_id, read_operation_config, data_asset, connection, schema, profile_config, if_match, endpoint_id, data_entity_entity_properties, data_entity_metadata, data_entity_key, data_entity_model_version, data_entity_parent_ref, data_entity_name, data_entity_description, data_entity_object_version, data_entity_external_key, data_entity_shape, data_entity_shape_id, data_entity_entity_type, data_entity_other_type_label, data_entity_unique_keys, data_entity_foreign_keys, data_entity_resource_name, data_entity_data_format, data_entity_object_status, data_entity_identifier):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataEntity'] = {}

    if read_operation_config is not None:
        _details['readOperationConfig'] = cli_util.parse_json_parameter("read_operation_config", read_operation_config)

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if schema is not None:
        _details['schema'] = cli_util.parse_json_parameter("schema", schema)

    if profile_config is not None:
        _details['profileConfig'] = cli_util.parse_json_parameter("profile_config", profile_config)

    if data_entity_entity_properties is not None:
        _details['dataEntity']['entityProperties'] = cli_util.parse_json_parameter("data_entity_entity_properties", data_entity_entity_properties)

    if data_entity_metadata is not None:
        _details['dataEntity']['metadata'] = cli_util.parse_json_parameter("data_entity_metadata", data_entity_metadata)

    if data_entity_key is not None:
        _details['dataEntity']['key'] = data_entity_key

    if data_entity_model_version is not None:
        _details['dataEntity']['modelVersion'] = data_entity_model_version

    if data_entity_parent_ref is not None:
        _details['dataEntity']['parentRef'] = cli_util.parse_json_parameter("data_entity_parent_ref", data_entity_parent_ref)

    if data_entity_name is not None:
        _details['dataEntity']['name'] = data_entity_name

    if data_entity_description is not None:
        _details['dataEntity']['description'] = data_entity_description

    if data_entity_object_version is not None:
        _details['dataEntity']['objectVersion'] = data_entity_object_version

    if data_entity_external_key is not None:
        _details['dataEntity']['externalKey'] = data_entity_external_key

    if data_entity_shape is not None:
        _details['dataEntity']['shape'] = cli_util.parse_json_parameter("data_entity_shape", data_entity_shape)

    if data_entity_shape_id is not None:
        _details['dataEntity']['shapeId'] = data_entity_shape_id

    if data_entity_entity_type is not None:
        _details['dataEntity']['entityType'] = data_entity_entity_type

    if data_entity_other_type_label is not None:
        _details['dataEntity']['otherTypeLabel'] = data_entity_other_type_label

    if data_entity_unique_keys is not None:
        _details['dataEntity']['uniqueKeys'] = cli_util.parse_json_parameter("data_entity_unique_keys", data_entity_unique_keys)

    if data_entity_foreign_keys is not None:
        _details['dataEntity']['foreignKeys'] = cli_util.parse_json_parameter("data_entity_foreign_keys", data_entity_foreign_keys)

    if data_entity_resource_name is not None:
        _details['dataEntity']['resourceName'] = data_entity_resource_name

    if data_entity_data_format is not None:
        _details['dataEntity']['dataFormat'] = cli_util.parse_json_parameter("data_entity_data_format", data_entity_data_format)

    if data_entity_object_status is not None:
        _details['dataEntity']['objectStatus'] = data_entity_object_status

    if data_entity_identifier is not None:
        _details['dataEntity']['identifier'] = data_entity_identifier

    _details['dataEntity']['modelType'] = 'FILE_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_data_profile(
        registry_id=registry_id,
        create_data_profile_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_profile_group.command(name=cli_util.override('data_connectivity_management.create_data_profile_derived_entity.command_name', 'create-data-profile-derived-entity'), help=u"""Execute data profiling on live schema. \n[Command Reference](createDataProfile)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--data-entity-name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is unique, editable and is restricted to 1000 characters.""")
@cli_util.option('--data-entity-resource-name', required=True, help=u"""The resource name.""")
@cli_util.option('--read-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--profile-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--data-entity-entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-key', help=u"""The object key.""")
@cli_util.option('--data-entity-model-version', help=u"""The object's model version.""")
@cli_util.option('--data-entity-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--data-entity-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-shape-id', help=u"""The shape ID.""")
@cli_util.option('--data-entity-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.""")
@cli_util.option('--data-entity-identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.""")
@cli_util.option('--data-entity-ref-data-object', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-entity-mode', type=custom_types.CliCaseInsensitiveChoice(["IN", "OUT"]), help=u"""Determines whether entity is treated as source or target""")
@cli_util.option('--data-entity-derived-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Property-bag (key-value pairs where key is Shape Field resource name and value is object)""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-ref-data-object': {'module': 'data_connectivity', 'class': 'ReferencedDataObject'}, 'data-entity-derived-properties': {'module': 'data_connectivity', 'class': 'dict(str, object)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'read-operation-config': {'module': 'data_connectivity', 'class': 'ReadOperationConfig'}, 'data-asset': {'module': 'data_connectivity', 'class': 'DataAsset'}, 'connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'profile-config': {'module': 'data_connectivity', 'class': 'ProfileConfig'}, 'data-entity-entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-entity-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'data-entity-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-entity-shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'data-entity-ref-data-object': {'module': 'data_connectivity', 'class': 'ReferencedDataObject'}, 'data-entity-derived-properties': {'module': 'data_connectivity', 'class': 'dict(str, object)'}}, output_type={'module': 'data_connectivity', 'class': 'DataProfile'})
@cli_util.wrap_exceptions
def create_data_profile_derived_entity(ctx, from_json, registry_id, data_entity_name, data_entity_resource_name, read_operation_config, data_asset, connection, schema, profile_config, if_match, endpoint_id, data_entity_entity_properties, data_entity_metadata, data_entity_key, data_entity_model_version, data_entity_parent_ref, data_entity_object_version, data_entity_shape, data_entity_shape_id, data_entity_object_status, data_entity_identifier, data_entity_ref_data_object, data_entity_mode, data_entity_derived_properties):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataEntity'] = {}
    _details['dataEntity']['name'] = data_entity_name
    _details['dataEntity']['resourceName'] = data_entity_resource_name

    if read_operation_config is not None:
        _details['readOperationConfig'] = cli_util.parse_json_parameter("read_operation_config", read_operation_config)

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if schema is not None:
        _details['schema'] = cli_util.parse_json_parameter("schema", schema)

    if profile_config is not None:
        _details['profileConfig'] = cli_util.parse_json_parameter("profile_config", profile_config)

    if data_entity_entity_properties is not None:
        _details['dataEntity']['entityProperties'] = cli_util.parse_json_parameter("data_entity_entity_properties", data_entity_entity_properties)

    if data_entity_metadata is not None:
        _details['dataEntity']['metadata'] = cli_util.parse_json_parameter("data_entity_metadata", data_entity_metadata)

    if data_entity_key is not None:
        _details['dataEntity']['key'] = data_entity_key

    if data_entity_model_version is not None:
        _details['dataEntity']['modelVersion'] = data_entity_model_version

    if data_entity_parent_ref is not None:
        _details['dataEntity']['parentRef'] = cli_util.parse_json_parameter("data_entity_parent_ref", data_entity_parent_ref)

    if data_entity_object_version is not None:
        _details['dataEntity']['objectVersion'] = data_entity_object_version

    if data_entity_shape is not None:
        _details['dataEntity']['shape'] = cli_util.parse_json_parameter("data_entity_shape", data_entity_shape)

    if data_entity_shape_id is not None:
        _details['dataEntity']['shapeId'] = data_entity_shape_id

    if data_entity_object_status is not None:
        _details['dataEntity']['objectStatus'] = data_entity_object_status

    if data_entity_identifier is not None:
        _details['dataEntity']['identifier'] = data_entity_identifier

    if data_entity_ref_data_object is not None:
        _details['dataEntity']['refDataObject'] = cli_util.parse_json_parameter("data_entity_ref_data_object", data_entity_ref_data_object)

    if data_entity_mode is not None:
        _details['dataEntity']['mode'] = data_entity_mode

    if data_entity_derived_properties is not None:
        _details['dataEntity']['derivedProperties'] = cli_util.parse_json_parameter("data_entity_derived_properties", data_entity_derived_properties)

    _details['dataEntity']['modelType'] = 'DERIVED_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_data_profile(
        registry_id=registry_id,
        create_data_profile_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@reference_info_group.command(name=cli_util.override('data_connectivity_management.create_de_reference_artifact.command_name', 'create-de-reference-artifact'), help=u"""Dereferenced a dcms artifact. \n[Command Reference](createDeReferenceArtifact)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--dcms-artifact-id', required=True, help=u"""The ID of a dcms artifact (DataAsset or Endpoint).""")
@cli_util.option('--service-artifact-id', required=True, help=u"""The unique ID of the service that is referencing a data asset.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'DeReferenceInfo'})
@cli_util.wrap_exceptions
def create_de_reference_artifact(ctx, from_json, registry_id, dcms_artifact_id, service_artifact_id, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(dcms_artifact_id, six.string_types) and len(dcms_artifact_id.strip()) == 0:
        raise click.UsageError('Parameter --dcms-artifact-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['serviceArtifactId'] = service_artifact_id

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_de_reference_artifact(
        registry_id=registry_id,
        dcms_artifact_id=dcms_artifact_id,
        create_de_reference_artifact_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detach_data_asset_info_group.command(name=cli_util.override('data_connectivity_management.create_detach_data_asset.command_name', 'create-detach-data-asset'), help=u"""Detaches a list of data assets to the given endpoint. \n[Command Reference](createDetachDataAsset)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--endpoint-id', required=True, help=u"""DCMS endpoint ID.""")
@cli_util.option('--data-assets', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The array of DataAsset keys.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@json_skeleton_utils.get_cli_json_input_option({'data-assets': {'module': 'data_connectivity', 'class': 'list[DataAsset]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'data-assets': {'module': 'data_connectivity', 'class': 'list[DataAsset]'}}, output_type={'module': 'data_connectivity', 'class': 'DetachDataAssetInfo'})
@cli_util.wrap_exceptions
def create_detach_data_asset(ctx, from_json, registry_id, endpoint_id, data_assets, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(endpoint_id, six.string_types) and len(endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataAssets'] = cli_util.parse_json_parameter("data_assets", data_assets)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_detach_data_asset(
        registry_id=registry_id,
        endpoint_id=endpoint_id,
        create_detach_data_asset_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@endpoint_group.command(name=cli_util.override('data_connectivity_management.create_endpoint.command_name', 'create'), help=u"""Creates a new Data Connectivity Management endpoint ready to perform data connectivity. \n[Command Reference](createEndpoint)""")
@cli_util.option('--display-name', required=True, help=u"""The Data Connectivity Management registry display name; registries can be renamed.""")
@cli_util.option('--vcn-id', help=u"""VCN identifier where the subnet resides.""")
@cli_util.option('--subnet-id', help=u"""Subnet identifier for the customer-connected databases.""")
@cli_util.option('--dns-zones', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of DNS zones to be used by the data assets to be harvested. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Data Connectivity Management Registry description""")
@cli_util.option('--compartment-id', help=u"""Compartment Identifier""")
@cli_util.option('--endpoint-size', type=click.INT, help=u"""Endpoint size for reverse connection capacity.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of NSGs to which the private endpoint VNIC must be added.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-id', help=u"""DCMS registry ID""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'dns-zones': {'module': 'data_connectivity', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_connectivity', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'data_connectivity', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dns-zones': {'module': 'data_connectivity', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_connectivity', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'data_connectivity', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def create_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, vcn_id, subnet_id, dns_zones, freeform_tags, defined_tags, description, compartment_id, endpoint_size, nsg_ids, registry_id):

    kwargs = {}
    if registry_id is not None:
        kwargs['registry_id'] = registry_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name

    if vcn_id is not None:
        _details['vcnId'] = vcn_id

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if dns_zones is not None:
        _details['dnsZones'] = cli_util.parse_json_parameter("dns_zones", dns_zones)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if endpoint_size is not None:
        _details['endpointSize'] = endpoint_size

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_endpoint(
        create_endpoint_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_entity_group.command(name=cli_util.override('data_connectivity_management.create_entity_shape.command_name', 'create-entity-shape'), help=u"""Creates the data entity shape using the shape from the data asset. \n[Command Reference](createEntityShape)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--model-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", "DATA_STORE_ENTITY", "SQL_ENTITY", "MESSAGE_ENTITY"]), help=u"""The data entity type.""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--key', help=u"""The object key.""")
@cli_util.option('--model-version', help=u"""The model version of the object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--external-key', help=u"""The external key of the object.""")
@cli_util.option('--shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--shape-id', help=u"""The shape ID.""")
@cli_util.option('--entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--resource-name', help=u"""The resource name.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--authorization-mode', type=custom_types.CliCaseInsensitiveChoice(["OBO", "USER_PRINCIPAL", "RESOURCE_PRINCIPAL", "INSTANCE_PRINCIPAL", "UNDEFINED"]), help=u"""Authorization mode for communicating with another OCI service relevant for the API.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'types': {'module': 'data_connectivity', 'class': 'TypeLibrary'}, 'entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'types': {'module': 'data_connectivity', 'class': 'TypeLibrary'}, 'entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}}, output_type={'module': 'data_connectivity', 'class': 'EntityShape'})
@cli_util.wrap_exceptions
def create_entity_shape(ctx, from_json, registry_id, connection_key, schema_resource_name, model_type, name, key, model_version, parent_ref, object_version, external_key, shape, shape_id, entity_type, other_type_label, unique_keys, foreign_keys, resource_name, object_status, identifier, types, entity_properties, if_match, authorization_mode, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if authorization_mode is not None:
        kwargs['authorization_mode'] = authorization_mode
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelType'] = model_type
    _details['name'] = name

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if object_version is not None:
        _details['objectVersion'] = object_version

    if external_key is not None:
        _details['externalKey'] = external_key

    if shape is not None:
        _details['shape'] = cli_util.parse_json_parameter("shape", shape)

    if shape_id is not None:
        _details['shapeId'] = shape_id

    if entity_type is not None:
        _details['entityType'] = entity_type

    if other_type_label is not None:
        _details['otherTypeLabel'] = other_type_label

    if unique_keys is not None:
        _details['uniqueKeys'] = cli_util.parse_json_parameter("unique_keys", unique_keys)

    if foreign_keys is not None:
        _details['foreignKeys'] = cli_util.parse_json_parameter("foreign_keys", foreign_keys)

    if resource_name is not None:
        _details['resourceName'] = resource_name

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if types is not None:
        _details['types'] = cli_util.parse_json_parameter("types", types)

    if entity_properties is not None:
        _details['entityProperties'] = cli_util.parse_json_parameter("entity_properties", entity_properties)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_entity_shape(
        registry_id=registry_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        create_entity_shape_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_entity_group.command(name=cli_util.override('data_connectivity_management.create_entity_shape_create_entity_shape_from_data_store.command_name', 'create-entity-shape-create-entity-shape-from-data-store'), help=u"""Creates the data entity shape using the shape from the data asset. \n[Command Reference](createEntityShape)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--key', help=u"""The object key.""")
@cli_util.option('--model-version', help=u"""The model version of the object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--external-key', help=u"""The external key of the object.""")
@cli_util.option('--shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--shape-id', help=u"""The shape ID.""")
@cli_util.option('--entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--resource-name', help=u"""The resource name.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--authorization-mode', type=custom_types.CliCaseInsensitiveChoice(["OBO", "USER_PRINCIPAL", "RESOURCE_PRINCIPAL", "INSTANCE_PRINCIPAL", "UNDEFINED"]), help=u"""Authorization mode for communicating with another OCI service relevant for the API.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'types': {'module': 'data_connectivity', 'class': 'TypeLibrary'}, 'entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'types': {'module': 'data_connectivity', 'class': 'TypeLibrary'}, 'entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}}, output_type={'module': 'data_connectivity', 'class': 'EntityShape'})
@cli_util.wrap_exceptions
def create_entity_shape_create_entity_shape_from_data_store(ctx, from_json, registry_id, connection_key, schema_resource_name, name, key, model_version, parent_ref, object_version, external_key, shape, shape_id, entity_type, other_type_label, unique_keys, foreign_keys, resource_name, object_status, identifier, types, entity_properties, if_match, authorization_mode, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if authorization_mode is not None:
        kwargs['authorization_mode'] = authorization_mode
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if object_version is not None:
        _details['objectVersion'] = object_version

    if external_key is not None:
        _details['externalKey'] = external_key

    if shape is not None:
        _details['shape'] = cli_util.parse_json_parameter("shape", shape)

    if shape_id is not None:
        _details['shapeId'] = shape_id

    if entity_type is not None:
        _details['entityType'] = entity_type

    if other_type_label is not None:
        _details['otherTypeLabel'] = other_type_label

    if unique_keys is not None:
        _details['uniqueKeys'] = cli_util.parse_json_parameter("unique_keys", unique_keys)

    if foreign_keys is not None:
        _details['foreignKeys'] = cli_util.parse_json_parameter("foreign_keys", foreign_keys)

    if resource_name is not None:
        _details['resourceName'] = resource_name

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if types is not None:
        _details['types'] = cli_util.parse_json_parameter("types", types)

    if entity_properties is not None:
        _details['entityProperties'] = cli_util.parse_json_parameter("entity_properties", entity_properties)

    _details['modelType'] = 'DATA_STORE_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_entity_shape(
        registry_id=registry_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        create_entity_shape_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_entity_group.command(name=cli_util.override('data_connectivity_management.create_entity_shape_create_entity_shape_from_message.command_name', 'create-entity-shape-create-entity-shape-from-message'), help=u"""Creates the data entity shape using the shape from the data asset. \n[Command Reference](createEntityShape)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--key', help=u"""The object key.""")
@cli_util.option('--model-version', help=u"""The model version of the object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--external-key', help=u"""The external key of the object.""")
@cli_util.option('--shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--shape-id', help=u"""The shape ID.""")
@cli_util.option('--entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--resource-name', help=u"""The resource name.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-format', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--authorization-mode', type=custom_types.CliCaseInsensitiveChoice(["OBO", "USER_PRINCIPAL", "RESOURCE_PRINCIPAL", "INSTANCE_PRINCIPAL", "UNDEFINED"]), help=u"""Authorization mode for communicating with another OCI service relevant for the API.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'types': {'module': 'data_connectivity', 'class': 'TypeLibrary'}, 'entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-format': {'module': 'data_connectivity', 'class': 'DataFormat'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'types': {'module': 'data_connectivity', 'class': 'TypeLibrary'}, 'entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-format': {'module': 'data_connectivity', 'class': 'DataFormat'}}, output_type={'module': 'data_connectivity', 'class': 'EntityShape'})
@cli_util.wrap_exceptions
def create_entity_shape_create_entity_shape_from_message(ctx, from_json, registry_id, connection_key, schema_resource_name, name, key, model_version, parent_ref, object_version, external_key, shape, shape_id, entity_type, other_type_label, unique_keys, foreign_keys, resource_name, object_status, identifier, types, entity_properties, data_format, if_match, authorization_mode, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if authorization_mode is not None:
        kwargs['authorization_mode'] = authorization_mode
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if object_version is not None:
        _details['objectVersion'] = object_version

    if external_key is not None:
        _details['externalKey'] = external_key

    if shape is not None:
        _details['shape'] = cli_util.parse_json_parameter("shape", shape)

    if shape_id is not None:
        _details['shapeId'] = shape_id

    if entity_type is not None:
        _details['entityType'] = entity_type

    if other_type_label is not None:
        _details['otherTypeLabel'] = other_type_label

    if unique_keys is not None:
        _details['uniqueKeys'] = cli_util.parse_json_parameter("unique_keys", unique_keys)

    if foreign_keys is not None:
        _details['foreignKeys'] = cli_util.parse_json_parameter("foreign_keys", foreign_keys)

    if resource_name is not None:
        _details['resourceName'] = resource_name

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if types is not None:
        _details['types'] = cli_util.parse_json_parameter("types", types)

    if entity_properties is not None:
        _details['entityProperties'] = cli_util.parse_json_parameter("entity_properties", entity_properties)

    if data_format is not None:
        _details['dataFormat'] = cli_util.parse_json_parameter("data_format", data_format)

    _details['modelType'] = 'MESSAGE_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_entity_shape(
        registry_id=registry_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        create_entity_shape_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_entity_group.command(name=cli_util.override('data_connectivity_management.create_entity_shape_create_entity_shape_from_table.command_name', 'create-entity-shape-create-entity-shape-from-table'), help=u"""Creates the data entity shape using the shape from the data asset. \n[Command Reference](createEntityShape)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--key', help=u"""The object key.""")
@cli_util.option('--model-version', help=u"""The model version of the object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--external-key', help=u"""The external key of the object.""")
@cli_util.option('--shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--shape-id', help=u"""The shape ID.""")
@cli_util.option('--entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--resource-name', help=u"""The resource name.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--authorization-mode', type=custom_types.CliCaseInsensitiveChoice(["OBO", "USER_PRINCIPAL", "RESOURCE_PRINCIPAL", "INSTANCE_PRINCIPAL", "UNDEFINED"]), help=u"""Authorization mode for communicating with another OCI service relevant for the API.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'types': {'module': 'data_connectivity', 'class': 'TypeLibrary'}, 'entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'types': {'module': 'data_connectivity', 'class': 'TypeLibrary'}, 'entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}}, output_type={'module': 'data_connectivity', 'class': 'EntityShape'})
@cli_util.wrap_exceptions
def create_entity_shape_create_entity_shape_from_table(ctx, from_json, registry_id, connection_key, schema_resource_name, name, key, model_version, parent_ref, object_version, external_key, shape, shape_id, entity_type, other_type_label, unique_keys, foreign_keys, resource_name, object_status, identifier, types, entity_properties, if_match, authorization_mode, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if authorization_mode is not None:
        kwargs['authorization_mode'] = authorization_mode
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if object_version is not None:
        _details['objectVersion'] = object_version

    if external_key is not None:
        _details['externalKey'] = external_key

    if shape is not None:
        _details['shape'] = cli_util.parse_json_parameter("shape", shape)

    if shape_id is not None:
        _details['shapeId'] = shape_id

    if entity_type is not None:
        _details['entityType'] = entity_type

    if other_type_label is not None:
        _details['otherTypeLabel'] = other_type_label

    if unique_keys is not None:
        _details['uniqueKeys'] = cli_util.parse_json_parameter("unique_keys", unique_keys)

    if foreign_keys is not None:
        _details['foreignKeys'] = cli_util.parse_json_parameter("foreign_keys", foreign_keys)

    if resource_name is not None:
        _details['resourceName'] = resource_name

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if types is not None:
        _details['types'] = cli_util.parse_json_parameter("types", types)

    if entity_properties is not None:
        _details['entityProperties'] = cli_util.parse_json_parameter("entity_properties", entity_properties)

    _details['modelType'] = 'TABLE_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_entity_shape(
        registry_id=registry_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        create_entity_shape_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_entity_group.command(name=cli_util.override('data_connectivity_management.create_entity_shape_create_entity_shape_from_sql.command_name', 'create-entity-shape-create-entity-shape-from-sql'), help=u"""Creates the data entity shape using the shape from the data asset. \n[Command Reference](createEntityShape)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--key', help=u"""The object key.""")
@cli_util.option('--model-version', help=u"""The model version of the object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--external-key', help=u"""The external key of the object.""")
@cli_util.option('--shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--shape-id', help=u"""The shape ID.""")
@cli_util.option('--entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--resource-name', help=u"""The resource name.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--sql-query', help=u"""sqlQuery""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--authorization-mode', type=custom_types.CliCaseInsensitiveChoice(["OBO", "USER_PRINCIPAL", "RESOURCE_PRINCIPAL", "INSTANCE_PRINCIPAL", "UNDEFINED"]), help=u"""Authorization mode for communicating with another OCI service relevant for the API.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'types': {'module': 'data_connectivity', 'class': 'TypeLibrary'}, 'entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'types': {'module': 'data_connectivity', 'class': 'TypeLibrary'}, 'entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}}, output_type={'module': 'data_connectivity', 'class': 'EntityShape'})
@cli_util.wrap_exceptions
def create_entity_shape_create_entity_shape_from_sql(ctx, from_json, registry_id, connection_key, schema_resource_name, name, key, model_version, parent_ref, object_version, external_key, shape, shape_id, entity_type, other_type_label, unique_keys, foreign_keys, resource_name, object_status, identifier, types, entity_properties, sql_query, if_match, authorization_mode, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if authorization_mode is not None:
        kwargs['authorization_mode'] = authorization_mode
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if object_version is not None:
        _details['objectVersion'] = object_version

    if external_key is not None:
        _details['externalKey'] = external_key

    if shape is not None:
        _details['shape'] = cli_util.parse_json_parameter("shape", shape)

    if shape_id is not None:
        _details['shapeId'] = shape_id

    if entity_type is not None:
        _details['entityType'] = entity_type

    if other_type_label is not None:
        _details['otherTypeLabel'] = other_type_label

    if unique_keys is not None:
        _details['uniqueKeys'] = cli_util.parse_json_parameter("unique_keys", unique_keys)

    if foreign_keys is not None:
        _details['foreignKeys'] = cli_util.parse_json_parameter("foreign_keys", foreign_keys)

    if resource_name is not None:
        _details['resourceName'] = resource_name

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if types is not None:
        _details['types'] = cli_util.parse_json_parameter("types", types)

    if entity_properties is not None:
        _details['entityProperties'] = cli_util.parse_json_parameter("entity_properties", entity_properties)

    if sql_query is not None:
        _details['sqlQuery'] = sql_query

    _details['modelType'] = 'SQL_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_entity_shape(
        registry_id=registry_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        create_entity_shape_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_entity_group.command(name=cli_util.override('data_connectivity_management.create_entity_shape_create_entity_shape_from_file.command_name', 'create-entity-shape-create-entity-shape-from-file'), help=u"""Creates the data entity shape using the shape from the data asset. \n[Command Reference](createEntityShape)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--key', help=u"""The object key.""")
@cli_util.option('--model-version', help=u"""The model version of the object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--external-key', help=u"""The external key of the object.""")
@cli_util.option('--shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--shape-id', help=u"""The shape ID.""")
@cli_util.option('--entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--resource-name', help=u"""The resource name.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-format', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--authorization-mode', type=custom_types.CliCaseInsensitiveChoice(["OBO", "USER_PRINCIPAL", "RESOURCE_PRINCIPAL", "INSTANCE_PRINCIPAL", "UNDEFINED"]), help=u"""Authorization mode for communicating with another OCI service relevant for the API.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'types': {'module': 'data_connectivity', 'class': 'TypeLibrary'}, 'entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-format': {'module': 'data_connectivity', 'class': 'DataFormat'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'types': {'module': 'data_connectivity', 'class': 'TypeLibrary'}, 'entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'data-format': {'module': 'data_connectivity', 'class': 'DataFormat'}}, output_type={'module': 'data_connectivity', 'class': 'EntityShape'})
@cli_util.wrap_exceptions
def create_entity_shape_create_entity_shape_from_file(ctx, from_json, registry_id, connection_key, schema_resource_name, name, key, model_version, parent_ref, object_version, external_key, shape, shape_id, entity_type, other_type_label, unique_keys, foreign_keys, resource_name, object_status, identifier, types, entity_properties, data_format, if_match, authorization_mode, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if authorization_mode is not None:
        kwargs['authorization_mode'] = authorization_mode
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if object_version is not None:
        _details['objectVersion'] = object_version

    if external_key is not None:
        _details['externalKey'] = external_key

    if shape is not None:
        _details['shape'] = cli_util.parse_json_parameter("shape", shape)

    if shape_id is not None:
        _details['shapeId'] = shape_id

    if entity_type is not None:
        _details['entityType'] = entity_type

    if other_type_label is not None:
        _details['otherTypeLabel'] = other_type_label

    if unique_keys is not None:
        _details['uniqueKeys'] = cli_util.parse_json_parameter("unique_keys", unique_keys)

    if foreign_keys is not None:
        _details['foreignKeys'] = cli_util.parse_json_parameter("foreign_keys", foreign_keys)

    if resource_name is not None:
        _details['resourceName'] = resource_name

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if types is not None:
        _details['types'] = cli_util.parse_json_parameter("types", types)

    if entity_properties is not None:
        _details['entityProperties'] = cli_util.parse_json_parameter("entity_properties", entity_properties)

    if data_format is not None:
        _details['dataFormat'] = cli_util.parse_json_parameter("data_format", data_format)

    _details['modelType'] = 'FILE_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_entity_shape(
        registry_id=registry_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        create_entity_shape_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_entity_group.command(name=cli_util.override('data_connectivity_management.create_entity_shape_create_entity_shape_from_view.command_name', 'create-entity-shape-create-entity-shape-from-view'), help=u"""Creates the data entity shape using the shape from the data asset. \n[Command Reference](createEntityShape)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--key', help=u"""The object key.""")
@cli_util.option('--model-version', help=u"""The model version of the object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--external-key', help=u"""The external key of the object.""")
@cli_util.option('--shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--shape-id', help=u"""The shape ID.""")
@cli_util.option('--entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]), help=u"""The entity type.""")
@cli_util.option('--other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--resource-name', help=u"""The resource name.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--entity-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map<String, String> for entity properties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--authorization-mode', type=custom_types.CliCaseInsensitiveChoice(["OBO", "USER_PRINCIPAL", "RESOURCE_PRINCIPAL", "INSTANCE_PRINCIPAL", "UNDEFINED"]), help=u"""Authorization mode for communicating with another OCI service relevant for the API.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'types': {'module': 'data_connectivity', 'class': 'TypeLibrary'}, 'entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'shape': {'module': 'data_connectivity', 'class': 'Shape'}, 'unique-keys': {'module': 'data_connectivity', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_connectivity', 'class': 'list[ForeignKey]'}, 'types': {'module': 'data_connectivity', 'class': 'TypeLibrary'}, 'entity-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}}, output_type={'module': 'data_connectivity', 'class': 'EntityShape'})
@cli_util.wrap_exceptions
def create_entity_shape_create_entity_shape_from_view(ctx, from_json, registry_id, connection_key, schema_resource_name, name, key, model_version, parent_ref, object_version, external_key, shape, shape_id, entity_type, other_type_label, unique_keys, foreign_keys, resource_name, object_status, identifier, types, entity_properties, if_match, authorization_mode, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if authorization_mode is not None:
        kwargs['authorization_mode'] = authorization_mode
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if object_version is not None:
        _details['objectVersion'] = object_version

    if external_key is not None:
        _details['externalKey'] = external_key

    if shape is not None:
        _details['shape'] = cli_util.parse_json_parameter("shape", shape)

    if shape_id is not None:
        _details['shapeId'] = shape_id

    if entity_type is not None:
        _details['entityType'] = entity_type

    if other_type_label is not None:
        _details['otherTypeLabel'] = other_type_label

    if unique_keys is not None:
        _details['uniqueKeys'] = cli_util.parse_json_parameter("unique_keys", unique_keys)

    if foreign_keys is not None:
        _details['foreignKeys'] = cli_util.parse_json_parameter("foreign_keys", foreign_keys)

    if resource_name is not None:
        _details['resourceName'] = resource_name

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if types is not None:
        _details['types'] = cli_util.parse_json_parameter("types", types)

    if entity_properties is not None:
        _details['entityProperties'] = cli_util.parse_json_parameter("entity_properties", entity_properties)

    _details['modelType'] = 'VIEW_ENTITY'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_entity_shape(
        registry_id=registry_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        create_entity_shape_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@execute_operation_job_details_group.command(name=cli_util.override('data_connectivity_management.create_execute_operation_job.command_name', 'create-execute-operation-job'), help=u"""Call the operation to execute \n[Command Reference](createExecuteOperationJob)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--operation', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--call-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--input-records', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Collection of the input parameters supplied.

This option is a JSON list with items of type OperationInputRecord.  For documentation on OperationInputRecord please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/OperationInputRecord.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({'operation': {'module': 'data_connectivity', 'class': 'Operation'}, 'call-operation-config': {'module': 'data_connectivity', 'class': 'CallOperationConfig'}, 'input-records': {'module': 'data_connectivity', 'class': 'list[OperationInputRecord]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'operation': {'module': 'data_connectivity', 'class': 'Operation'}, 'call-operation-config': {'module': 'data_connectivity', 'class': 'CallOperationConfig'}, 'input-records': {'module': 'data_connectivity', 'class': 'list[OperationInputRecord]'}}, output_type={'module': 'data_connectivity', 'class': 'ExecuteOperationJobDetails'})
@cli_util.wrap_exceptions
def create_execute_operation_job(ctx, from_json, registry_id, connection_key, schema_resource_name, operation, call_operation_config, input_records, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if operation is not None:
        _details['operation'] = cli_util.parse_json_parameter("operation", operation)

    if call_operation_config is not None:
        _details['callOperationConfig'] = cli_util.parse_json_parameter("call_operation_config", call_operation_config)

    if input_records is not None:
        _details['inputRecords'] = cli_util.parse_json_parameter("input_records", input_records)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_execute_operation_job(
        registry_id=registry_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        create_execute_operation_job_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@execute_operation_job_details_group.command(name=cli_util.override('data_connectivity_management.create_execute_operation_job_operation_from_procedure.command_name', 'create-execute-operation-job-operation-from-procedure'), help=u"""Call the operation to execute \n[Command Reference](createExecuteOperationJob)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--call-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--input-records', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Collection of the input parameters supplied.

This option is a JSON list with items of type OperationInputRecord.  For documentation on OperationInputRecord please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/OperationInputRecord.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--operation-operation-attributes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--operation-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--operation-key', help=u"""The object key.""")
@cli_util.option('--operation-model-version', help=u"""The model version of the object.""")
@cli_util.option('--operation-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--operation-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--operation-name', help=u"""The operation name.""")
@cli_util.option('--operation-object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--operation-external-key', help=u"""The external key of the object.""")
@cli_util.option('--operation-resource-name', help=u"""The resource name.""")
@cli_util.option('--operation-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.""")
@json_skeleton_utils.get_cli_json_input_option({'call-operation-config': {'module': 'data_connectivity', 'class': 'CallOperationConfig'}, 'input-records': {'module': 'data_connectivity', 'class': 'list[OperationInputRecord]'}, 'operation-operation-attributes': {'module': 'data_connectivity', 'class': 'AbstractOperationAttributes'}, 'operation-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'operation-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'operation-shape': {'module': 'data_connectivity', 'class': 'Shape'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'call-operation-config': {'module': 'data_connectivity', 'class': 'CallOperationConfig'}, 'input-records': {'module': 'data_connectivity', 'class': 'list[OperationInputRecord]'}, 'operation-operation-attributes': {'module': 'data_connectivity', 'class': 'AbstractOperationAttributes'}, 'operation-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'operation-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'operation-shape': {'module': 'data_connectivity', 'class': 'Shape'}}, output_type={'module': 'data_connectivity', 'class': 'ExecuteOperationJobDetails'})
@cli_util.wrap_exceptions
def create_execute_operation_job_operation_from_procedure(ctx, from_json, registry_id, connection_key, schema_resource_name, call_operation_config, input_records, endpoint_id, operation_operation_attributes, operation_metadata, operation_key, operation_model_version, operation_parent_ref, operation_shape, operation_name, operation_object_version, operation_external_key, operation_resource_name, operation_object_status):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['operation'] = {}

    if call_operation_config is not None:
        _details['callOperationConfig'] = cli_util.parse_json_parameter("call_operation_config", call_operation_config)

    if input_records is not None:
        _details['inputRecords'] = cli_util.parse_json_parameter("input_records", input_records)

    if operation_operation_attributes is not None:
        _details['operation']['operationAttributes'] = cli_util.parse_json_parameter("operation_operation_attributes", operation_operation_attributes)

    if operation_metadata is not None:
        _details['operation']['metadata'] = cli_util.parse_json_parameter("operation_metadata", operation_metadata)

    if operation_key is not None:
        _details['operation']['key'] = operation_key

    if operation_model_version is not None:
        _details['operation']['modelVersion'] = operation_model_version

    if operation_parent_ref is not None:
        _details['operation']['parentRef'] = cli_util.parse_json_parameter("operation_parent_ref", operation_parent_ref)

    if operation_shape is not None:
        _details['operation']['shape'] = cli_util.parse_json_parameter("operation_shape", operation_shape)

    if operation_name is not None:
        _details['operation']['name'] = operation_name

    if operation_object_version is not None:
        _details['operation']['objectVersion'] = operation_object_version

    if operation_external_key is not None:
        _details['operation']['externalKey'] = operation_external_key

    if operation_resource_name is not None:
        _details['operation']['resourceName'] = operation_resource_name

    if operation_object_status is not None:
        _details['operation']['objectStatus'] = operation_object_status

    _details['operation']['modelType'] = 'PROCEDURE'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_execute_operation_job(
        registry_id=registry_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        create_execute_operation_job_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@execute_operation_job_details_group.command(name=cli_util.override('data_connectivity_management.create_execute_operation_job_operation_from_api.command_name', 'create-execute-operation-job-operation-from-api'), help=u"""Call the operation to execute \n[Command Reference](createExecuteOperationJob)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--operation-name', required=True, help=u"""The operation name. This value is unique.""")
@cli_util.option('--operation-resource-name', required=True, help=u"""The resource name.""")
@cli_util.option('--call-operation-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--input-records', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Collection of the input parameters supplied.

This option is a JSON list with items of type OperationInputRecord.  For documentation on OperationInputRecord please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/OperationInputRecord.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--operation-operation-attributes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--operation-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--operation-key', help=u"""The object key.""")
@cli_util.option('--operation-model-version', help=u"""The model version of the object.""")
@cli_util.option('--operation-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--operation-shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--operation-object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--operation-external-key', help=u"""The external key for the object.""")
@cli_util.option('--operation-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.""")
@json_skeleton_utils.get_cli_json_input_option({'call-operation-config': {'module': 'data_connectivity', 'class': 'CallOperationConfig'}, 'input-records': {'module': 'data_connectivity', 'class': 'list[OperationInputRecord]'}, 'operation-operation-attributes': {'module': 'data_connectivity', 'class': 'AbstractOperationAttributes'}, 'operation-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'operation-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'operation-shape': {'module': 'data_connectivity', 'class': 'Shape'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'call-operation-config': {'module': 'data_connectivity', 'class': 'CallOperationConfig'}, 'input-records': {'module': 'data_connectivity', 'class': 'list[OperationInputRecord]'}, 'operation-operation-attributes': {'module': 'data_connectivity', 'class': 'AbstractOperationAttributes'}, 'operation-metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'operation-parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'operation-shape': {'module': 'data_connectivity', 'class': 'Shape'}}, output_type={'module': 'data_connectivity', 'class': 'ExecuteOperationJobDetails'})
@cli_util.wrap_exceptions
def create_execute_operation_job_operation_from_api(ctx, from_json, registry_id, connection_key, schema_resource_name, operation_name, operation_resource_name, call_operation_config, input_records, endpoint_id, operation_operation_attributes, operation_metadata, operation_key, operation_model_version, operation_parent_ref, operation_shape, operation_object_version, operation_external_key, operation_object_status):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['operation'] = {}
    _details['operation']['name'] = operation_name
    _details['operation']['resourceName'] = operation_resource_name

    if call_operation_config is not None:
        _details['callOperationConfig'] = cli_util.parse_json_parameter("call_operation_config", call_operation_config)

    if input_records is not None:
        _details['inputRecords'] = cli_util.parse_json_parameter("input_records", input_records)

    if operation_operation_attributes is not None:
        _details['operation']['operationAttributes'] = cli_util.parse_json_parameter("operation_operation_attributes", operation_operation_attributes)

    if operation_metadata is not None:
        _details['operation']['metadata'] = cli_util.parse_json_parameter("operation_metadata", operation_metadata)

    if operation_key is not None:
        _details['operation']['key'] = operation_key

    if operation_model_version is not None:
        _details['operation']['modelVersion'] = operation_model_version

    if operation_parent_ref is not None:
        _details['operation']['parentRef'] = cli_util.parse_json_parameter("operation_parent_ref", operation_parent_ref)

    if operation_shape is not None:
        _details['operation']['shape'] = cli_util.parse_json_parameter("operation_shape", operation_shape)

    if operation_object_version is not None:
        _details['operation']['objectVersion'] = operation_object_version

    if operation_external_key is not None:
        _details['operation']['externalKey'] = operation_external_key

    if operation_object_status is not None:
        _details['operation']['objectStatus'] = operation_object_status

    _details['operation']['modelType'] = 'API'

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_execute_operation_job(
        registry_id=registry_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        create_execute_operation_job_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@folder_group.command(name=cli_util.override('data_connectivity_management.create_folder.command_name', 'create'), help=u"""Creates a folder under a specified registry. \n[Command Reference](createFolder)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--model-type', help=u"""The type of the folder.""")
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify the folder. In scenarios where reference to the folder is required, a value can be passed in create.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""User-defined description of the folder.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--data-assets', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of data assets that belong to the folder.

This option is a JSON list with items of type DataAsset.  For documentation on DataAsset please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/DataAsset.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-assets': {'module': 'data_connectivity', 'class': 'list[DataAsset]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-assets': {'module': 'data_connectivity', 'class': 'list[DataAsset]'}}, output_type={'module': 'data_connectivity', 'class': 'Folder'})
@cli_util.wrap_exceptions
def create_folder(ctx, from_json, registry_id, name, identifier, model_type, key, model_version, parent_ref, description, object_version, object_status, data_assets):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier

    if model_type is not None:
        _details['modelType'] = model_type

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if description is not None:
        _details['description'] = description

    if object_version is not None:
        _details['objectVersion'] = object_version

    if object_status is not None:
        _details['objectStatus'] = object_status

    if data_assets is not None:
        _details['dataAssets'] = cli_util.parse_json_parameter("data_assets", data_assets)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_folder(
        registry_id=registry_id,
        create_folder_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@full_push_down_task_response_group.command(name=cli_util.override('data_connectivity_management.create_full_push_down_task.command_name', 'create-full-push-down-task'), help=u"""This endpoint is used to create a connectivity task (such as PushdownTask). \n[Command Reference](createFullPushDownTask)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--model-type', required=True, help=u"""The type of FullPushDownTask.""")
@cli_util.option('--source', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({'source': {'module': 'data_connectivity', 'class': 'Source'}, 'target': {'module': 'data_connectivity', 'class': 'Target'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source': {'module': 'data_connectivity', 'class': 'Source'}, 'target': {'module': 'data_connectivity', 'class': 'Target'}}, output_type={'module': 'data_connectivity', 'class': 'FullPushDownTaskResponse'})
@cli_util.wrap_exceptions
def create_full_push_down_task(ctx, from_json, registry_id, model_type, source, target, if_match, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelType'] = model_type

    if source is not None:
        _details['source'] = cli_util.parse_json_parameter("source", source)

    if target is not None:
        _details['target'] = cli_util.parse_json_parameter("target", target)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_full_push_down_task(
        registry_id=registry_id,
        create_full_push_down_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@reference_info_group.command(name=cli_util.override('data_connectivity_management.create_reference_artifact.command_name', 'create-reference-artifact'), help=u"""Reference a data asset. \n[Command Reference](createReferenceArtifact)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--dcms-artifact-id', required=True, help=u"""The ID of a dcms artifact (DataAsset or Endpoint).""")
@cli_util.option('--service-artifact-id', required=True, help=u"""The unique ID of the service that is referencing a data asset.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'ReferenceInfo'})
@cli_util.wrap_exceptions
def create_reference_artifact(ctx, from_json, registry_id, dcms_artifact_id, service_artifact_id, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(dcms_artifact_id, six.string_types) and len(dcms_artifact_id.strip()) == 0:
        raise click.UsageError('Parameter --dcms-artifact-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['serviceArtifactId'] = service_artifact_id

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_reference_artifact(
        registry_id=registry_id,
        dcms_artifact_id=dcms_artifact_id,
        create_reference_artifact_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@registry_group.command(name=cli_util.override('data_connectivity_management.create_registry.command_name', 'create'), help=u"""Creates a new Data Connectivity Management registry ready to perform data connectivity management. \n[Command Reference](createRegistry)""")
@cli_util.option('--display-name', required=True, help=u"""The Data Connectivity Management Registry display name; registries can be renamed.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Data Connectivity Management Registry description""")
@cli_util.option('--compartment-id', help=u"""Compartment Identifier""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_connectivity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_connectivity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_registry(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, freeform_tags, defined_tags, description, compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_registry(
        create_registry_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@test_network_connectivity_group.command(name=cli_util.override('data_connectivity_management.create_test_network_connectivity.command_name', 'create'), help=u"""Execute network validation on the selected data assets associated with the provided private endpoint. \n[Command Reference](createTestNetworkConnectivity)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Data Asset key""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'TestNetworkConnectivity'})
@cli_util.wrap_exceptions
def create_test_network_connectivity(ctx, from_json, registry_id, data_asset_key, endpoint_id, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataAssetKey'] = data_asset_key

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.create_test_network_connectivity(
        registry_id=registry_id,
        create_test_network_connectivity_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_connectivity_management.delete_connection.command_name', 'delete'), help=u"""Removes a connection using the specified identifier. \n[Command Reference](deleteConnection)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_connection(ctx, from_json, registry_id, connection_key, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.delete_connection(
        registry_id=registry_id,
        connection_key=connection_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_connectivity_management.delete_data_asset.command_name', 'delete'), help=u"""Removes a data asset using the specified identifier. \n[Command Reference](deleteDataAsset)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--data-asset-key', required=True, help=u"""The data asset key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_data_asset(ctx, from_json, registry_id, data_asset_key, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.delete_data_asset(
        registry_id=registry_id,
        data_asset_key=data_asset_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@endpoint_group.command(name=cli_util.override('data_connectivity_management.delete_endpoint.command_name', 'delete'), help=u"""Deletes a Data Connectivity Management endpoint resource by its identifier. \n[Command Reference](deleteEndpoint)""")
@cli_util.option('--endpoint-id', required=True, help=u"""DCMS endpoint ID.""")
@cli_util.option('--registry-id', help=u"""DCMS registry ID""")
@cli_util.option('--is-force-operation', type=click.BOOL, help=u"""Try to delete forcefully after drain timeout.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, endpoint_id, registry_id, is_force_operation, if_match):

    if isinstance(endpoint_id, six.string_types) and len(endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if registry_id is not None:
        kwargs['registry_id'] = registry_id
    if is_force_operation is not None:
        kwargs['is_force_operation'] = is_force_operation
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.delete_endpoint(
        endpoint_id=endpoint_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@folder_group.command(name=cli_util.override('data_connectivity_management.delete_folder.command_name', 'delete'), help=u"""Removes a folder using the specified identifier. \n[Command Reference](deleteFolder)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--folder-key', required=True, help=u"""The folder ID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_folder(ctx, from_json, registry_id, folder_key, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(folder_key, six.string_types) and len(folder_key.strip()) == 0:
        raise click.UsageError('Parameter --folder-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.delete_folder(
        registry_id=registry_id,
        folder_key=folder_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@test_network_connectivity_group.command(name=cli_util.override('data_connectivity_management.delete_network_connectivity_status.command_name', 'delete-network-connectivity-status'), help=u"""This api is used to delete a persisted NetworkValidationStatus by its key \n[Command Reference](deleteNetworkConnectivityStatus)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--network-validation-status-key', required=True, help=u"""NetworkValidationStatus key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_network_connectivity_status(ctx, from_json, registry_id, network_validation_status_key, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(network_validation_status_key, six.string_types) and len(network_validation_status_key.strip()) == 0:
        raise click.UsageError('Parameter --network-validation-status-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.delete_network_connectivity_status(
        registry_id=registry_id,
        network_validation_status_key=network_validation_status_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@registry_group.command(name=cli_util.override('data_connectivity_management.delete_registry.command_name', 'delete'), help=u"""Deletes a Data Connectivity Management registry resource by its identifier. \n[Command Reference](deleteRegistry)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--is-force-operation', type=click.BOOL, help=u"""Try to delete forcefully after drain timeout.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_registry(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, registry_id, is_force_operation, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if is_force_operation is not None:
        kwargs['is_force_operation'] = is_force_operation
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.delete_registry(
        registry_id=registry_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@derived_entity_group.command(name=cli_util.override('data_connectivity_management.derive_entities.command_name', 'derive-entities'), help=u"""Get the Derived Entities from the EntityFlowMode and reference key of DataObject \n[Command Reference](deriveEntities)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--items', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The array of DeriveEntitiesRequestItem""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'data_connectivity', 'class': 'list[DeriveEntitiesItem]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'data_connectivity', 'class': 'list[DeriveEntitiesItem]'}}, output_type={'module': 'data_connectivity', 'class': 'DeriveEntities'})
@cli_util.wrap_exceptions
def derive_entities(ctx, from_json, registry_id, items):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.derive_entities(
        registry_id=registry_id,
        derive_entities_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_connectivity_management.get_connection.command_name', 'get'), help=u"""Retrieves the connection details using the specified identifier. \n[Command Reference](getConnection)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'Connection'})
@cli_util.wrap_exceptions
def get_connection(ctx, from_json, registry_id, connection_key):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.get_connection(
        registry_id=registry_id,
        connection_key=connection_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_connectivity_management.get_data_asset.command_name', 'get'), help=u"""Retrieves details of a data asset using the specified identifier. \n[Command Reference](getDataAsset)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--data-asset-key', required=True, help=u"""The data asset key.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def get_data_asset(ctx, from_json, registry_id, data_asset_key):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.get_data_asset(
        registry_id=registry_id,
        data_asset_key=data_asset_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_entity_group.command(name=cli_util.override('data_connectivity_management.get_data_entity.command_name', 'get'), help=u"""Retrieves the data entity details with the given name from live schema. \n[Command Reference](getDataEntity)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--data-entity-key', required=True, help=u"""The key of the data entity.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'DataEntity'})
@cli_util.wrap_exceptions
def get_data_entity(ctx, from_json, registry_id, connection_key, schema_resource_name, data_entity_key, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    if isinstance(data_entity_key, six.string_types) and len(data_entity_key.strip()) == 0:
        raise click.UsageError('Parameter --data-entity-key cannot be whitespace or empty string')

    kwargs = {}
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.get_data_entity(
        registry_id=registry_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        data_entity_key=data_entity_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@endpoint_group.command(name=cli_util.override('data_connectivity_management.get_endpoint.command_name', 'get'), help=u"""Gets a Data Connectivity Management endpoint by its identifier. \n[Command Reference](getEndpoint)""")
@cli_util.option('--endpoint-id', required=True, help=u"""DCMS endpoint ID.""")
@cli_util.option('--registry-id', help=u"""DCMS registry ID""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'Endpoint'})
@cli_util.wrap_exceptions
def get_endpoint(ctx, from_json, endpoint_id, registry_id):

    if isinstance(endpoint_id, six.string_types) and len(endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if registry_id is not None:
        kwargs['registry_id'] = registry_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.get_endpoint(
        endpoint_id=endpoint_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@config_details_group.command(name=cli_util.override('data_connectivity_management.get_engine_configurations.command_name', 'get-engine-configurations'), help=u"""This endpoint is used to fetch connector-specific engine configurations. \n[Command Reference](getEngineConfigurations)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--engine-type-query-param', type=custom_types.CliCaseInsensitiveChoice(["SPARK"]), help=u"""Specifies the runtime engine for the bulk read/write operation. Default is SPARK.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'ConfigDetails'})
@cli_util.wrap_exceptions
def get_engine_configurations(ctx, from_json, registry_id, connection_key, engine_type_query_param):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    kwargs = {}
    if engine_type_query_param is not None:
        kwargs['engine_type_query_param'] = engine_type_query_param
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.get_engine_configurations(
        registry_id=registry_id,
        connection_key=connection_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@execute_operation_job_group.command(name=cli_util.override('data_connectivity_management.get_execute_operation_job.command_name', 'get'), help=u"""Get the status or the result of the execution. \n[Command Reference](getExecuteOperationJob)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--execute-operation-job-key', required=True, help=u"""Job ID returned by the execute operation job API.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'ExecuteOperationJob'})
@cli_util.wrap_exceptions
def get_execute_operation_job(ctx, from_json, registry_id, connection_key, schema_resource_name, execute_operation_job_key, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    if isinstance(execute_operation_job_key, six.string_types) and len(execute_operation_job_key.strip()) == 0:
        raise click.UsageError('Parameter --execute-operation-job-key cannot be whitespace or empty string')

    kwargs = {}
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.get_execute_operation_job(
        registry_id=registry_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        execute_operation_job_key=execute_operation_job_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@folder_group.command(name=cli_util.override('data_connectivity_management.get_folder.command_name', 'get'), help=u"""Retrieves the folder details using the specified identifier. \n[Command Reference](getFolder)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--folder-key', required=True, help=u"""The folder ID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'Folder'})
@cli_util.wrap_exceptions
def get_folder(ctx, from_json, registry_id, folder_key):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(folder_key, six.string_types) and len(folder_key.strip()) == 0:
        raise click.UsageError('Parameter --folder-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.get_folder(
        registry_id=registry_id,
        folder_key=folder_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@test_network_connectivity_group.command(name=cli_util.override('data_connectivity_management.get_network_connectivity_status.command_name', 'get-network-connectivity-status'), help=u"""Get the status of network reachability check, with the timestamp of when the status was last checked, for a given PrivateEndpoint-DataAsset pair. \n[Command Reference](getNetworkConnectivityStatus)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--data-asset-key', required=True, help=u"""The data asset key.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'NetworkConnectivityStatus'})
@cli_util.wrap_exceptions
def get_network_connectivity_status(ctx, from_json, registry_id, data_asset_key, endpoint_id, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.get_network_connectivity_status(
        registry_id=registry_id,
        data_asset_key=data_asset_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@operation_group.command(name=cli_util.override('data_connectivity_management.get_operation.command_name', 'get'), help=u"""Retrieves the details of operation with the given resource name. \n[Command Reference](getOperation)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--operation-resource-name', required=True, help=u"""The operation resource name used for retrieving the details of operation.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'Operation'})
@cli_util.wrap_exceptions
def get_operation(ctx, from_json, registry_id, connection_key, schema_resource_name, operation_resource_name, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    if isinstance(operation_resource_name, six.string_types) and len(operation_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --operation-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.get_operation(
        registry_id=registry_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        operation_resource_name=operation_resource_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@registry_group.command(name=cli_util.override('data_connectivity_management.get_registry.command_name', 'get'), help=u"""Retrieves a Data Connectivity Management registry using the specified identifier. \n[Command Reference](getRegistry)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'Registry'})
@cli_util.wrap_exceptions
def get_registry(ctx, from_json, registry_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.get_registry(
        registry_id=registry_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@schema_group.command(name=cli_util.override('data_connectivity_management.get_schema.command_name', 'get'), help=u"""Retrieves a schema that can be accessed using the specified connection. \n[Command Reference](getSchema)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'Schema'})
@cli_util.wrap_exceptions
def get_schema(ctx, from_json, registry_id, connection_key, schema_resource_name, endpoint_id):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.get_schema(
        registry_id=registry_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@type_group.command(name=cli_util.override('data_connectivity_management.get_type.command_name', 'get'), help=u"""This endpoint retrieves dataAsset and connection attributes from DataAssetRegistry. \n[Command Reference](getType)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--type-key', required=True, help=u"""Key of the a specific type.""")
@cli_util.option('--fields', multiple=True, help=u"""Specifies the fields to get for an object.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_connectivity', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_connectivity', 'class': 'list[string]'}}, output_type={'module': 'data_connectivity', 'class': 'Type'})
@cli_util.wrap_exceptions
def get_type(ctx, from_json, registry_id, type_key, fields):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(type_key, six.string_types) and len(type_key.strip()) == 0:
        raise click.UsageError('Parameter --type-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.get_type(
        registry_id=registry_id,
        type_key=type_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('data_connectivity_management.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_connectivity_management.list_connections.command_name', 'list'), help=u"""Retrieves a list of all connections. \n[Command Reference](listConnections)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Used to filter by the data asset key of the object.""")
@cli_util.option('--name', help=u"""Used to filter by the name of the object.""")
@cli_util.option('--page', help=u"""For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""Sets the maximum number of results per page, or items to return in a paginated `List` call. See [List Pagination].""")
@cli_util.option('--fields', multiple=True, help=u"""Specifies the fields to get for an object.""")
@cli_util.option('--type', help=u"""Type of the object to filter the results with.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order are by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--favorites-query-param', type=custom_types.CliCaseInsensitiveChoice(["FAVORITES_ONLY", "NON_FAVORITES_ONLY", "ALL"]), help=u"""If value is FAVORITES_ONLY, then only objects marked as favorite by the requesting user will be included in result. If value is NON_FAVORITES_ONLY, then objects marked as favorites by the requesting user will be skipped. If value is ALL or if not specified, all objects, irrespective of favorites or not will be returned. Default is ALL.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_connectivity', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_connectivity', 'class': 'list[string]'}}, output_type={'module': 'data_connectivity', 'class': 'ConnectionSummaryCollection'})
@cli_util.wrap_exceptions
def list_connections(ctx, from_json, all_pages, page_size, registry_id, data_asset_key, name, page, limit, fields, type, sort_by, sort_order, favorites_query_param):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if type is not None:
        kwargs['type'] = type
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if favorites_query_param is not None:
        kwargs['favorites_query_param'] = favorites_query_param
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_connections,
            registry_id=registry_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_connections,
            limit,
            page_size,
            registry_id=registry_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    else:
        result = client.list_connections(
            registry_id=registry_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_connectivity_management.list_data_assets.command_name', 'list'), help=u"""Retrieves a list of all data asset summaries. \n[Command Reference](listDataAssets)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--page', help=u"""For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""Sets the maximum number of results per page, or items to return in a paginated `List` call. See [List Pagination].""")
@cli_util.option('--fields', multiple=True, help=u"""Specifies the fields to get for an object.""")
@cli_util.option('--include-types', multiple=True, help=u"""Artifact type which needs to be listed while listing Artifacts.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order are by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--name', help=u"""Used to filter by the name of the object.""")
@cli_util.option('--exclude-types', multiple=True, help=u"""The types that will be excluded from the list of data assets/connections.""")
@cli_util.option('--favorites-query-param', type=custom_types.CliCaseInsensitiveChoice(["FAVORITES_ONLY", "NON_FAVORITES_ONLY", "ALL"]), help=u"""If value is FAVORITES_ONLY, then only objects marked as favorite by the requesting user will be included in result. If value is NON_FAVORITES_ONLY, then objects marked as favorites by the requesting user will be skipped. If value is ALL or if not specified, all objects, irrespective of favorites or not will be returned. Default is ALL.""")
@cli_util.option('--folder-id', help=u"""Unique key of the folder.""")
@cli_util.option('--endpoint-ids', multiple=True, help=u"""Endpoint IDs used for data-plane APIs to filter or prefer specific endpoint.""")
@cli_util.option('--exclude-endpoint-ids', multiple=True, help=u"""Endpoints which will be excluded while listing data assets.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_connectivity', 'class': 'list[string]'}, 'include-types': {'module': 'data_connectivity', 'class': 'list[string]'}, 'exclude-types': {'module': 'data_connectivity', 'class': 'list[string]'}, 'endpoint-ids': {'module': 'data_connectivity', 'class': 'list[string]'}, 'exclude-endpoint-ids': {'module': 'data_connectivity', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_connectivity', 'class': 'list[string]'}, 'include-types': {'module': 'data_connectivity', 'class': 'list[string]'}, 'exclude-types': {'module': 'data_connectivity', 'class': 'list[string]'}, 'endpoint-ids': {'module': 'data_connectivity', 'class': 'list[string]'}, 'exclude-endpoint-ids': {'module': 'data_connectivity', 'class': 'list[string]'}}, output_type={'module': 'data_connectivity', 'class': 'DataAssetSummaryCollection'})
@cli_util.wrap_exceptions
def list_data_assets(ctx, from_json, all_pages, page_size, registry_id, page, limit, fields, include_types, sort_by, sort_order, name, exclude_types, favorites_query_param, folder_id, endpoint_ids, exclude_endpoint_ids):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if include_types is not None and len(include_types) > 0:
        kwargs['include_types'] = include_types
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if name is not None:
        kwargs['name'] = name
    if exclude_types is not None and len(exclude_types) > 0:
        kwargs['exclude_types'] = exclude_types
    if favorites_query_param is not None:
        kwargs['favorites_query_param'] = favorites_query_param
    if folder_id is not None:
        kwargs['folder_id'] = folder_id
    if endpoint_ids is not None and len(endpoint_ids) > 0:
        kwargs['endpoint_ids'] = endpoint_ids
    if exclude_endpoint_ids is not None and len(exclude_endpoint_ids) > 0:
        kwargs['exclude_endpoint_ids'] = exclude_endpoint_ids
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_assets,
            registry_id=registry_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_assets,
            limit,
            page_size,
            registry_id=registry_id,
            **kwargs
        )
    else:
        result = client.list_data_assets(
            registry_id=registry_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@data_entity_group.command(name=cli_util.override('data_connectivity_management.list_data_entities.command_name', 'list'), help=u"""Lists a summary of data entities from the data asset using the specified connection. \n[Command Reference](listDataEntities)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--name', help=u"""Used to filter by the name of the object.""")
@cli_util.option('--page', help=u"""For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See [List Pagination].""")
@cli_util.option('--type', help=u"""Type of the object to filter the results with.""")
@cli_util.option('--limit', type=click.INT, help=u"""Sets the maximum number of results per page, or items to return in a paginated `List` call. See [List Pagination].""")
@cli_util.option('--fields', multiple=True, help=u"""Specifies the fields to get for an object.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order are by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--api-mode', type=custom_types.CliCaseInsensitiveChoice(["PREVIEW", "ALL"]), help=u"""This parameter can be used to set the api response type to preview.""")
@cli_util.option('--name-list', multiple=True, help=u"""Used to filter by the name of the object.""")
@cli_util.option('--is-pattern', type=click.BOOL, help=u"""This parameter can be used to specify whether entity search type is a pattern search.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--include-types', multiple=True, help=u"""Artifact type which needs to be listed while listing Artifacts.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_connectivity', 'class': 'list[string]'}, 'name-list': {'module': 'data_connectivity', 'class': 'list[string]'}, 'include-types': {'module': 'data_connectivity', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_connectivity', 'class': 'list[string]'}, 'name-list': {'module': 'data_connectivity', 'class': 'list[string]'}, 'include-types': {'module': 'data_connectivity', 'class': 'list[string]'}}, output_type={'module': 'data_connectivity', 'class': 'DataEntitySummaryCollection'})
@cli_util.wrap_exceptions
def list_data_entities(ctx, from_json, all_pages, page_size, registry_id, connection_key, schema_resource_name, name, page, type, limit, fields, sort_by, sort_order, api_mode, name_list, is_pattern, endpoint_id, include_types):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if page is not None:
        kwargs['page'] = page
    if type is not None:
        kwargs['type'] = type
    if limit is not None:
        kwargs['limit'] = limit
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if api_mode is not None:
        kwargs['api_mode'] = api_mode
    if name_list is not None and len(name_list) > 0:
        kwargs['name_list'] = name_list
    if is_pattern is not None:
        kwargs['is_pattern'] = is_pattern
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    if include_types is not None and len(include_types) > 0:
        kwargs['include_types'] = include_types
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_entities,
            registry_id=registry_id,
            connection_key=connection_key,
            schema_resource_name=schema_resource_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_entities,
            limit,
            page_size,
            registry_id=registry_id,
            connection_key=connection_key,
            schema_resource_name=schema_resource_name,
            **kwargs
        )
    else:
        result = client.list_data_entities(
            registry_id=registry_id,
            connection_key=connection_key,
            schema_resource_name=schema_resource_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@endpoint_group.command(name=cli_util.override('data_connectivity_management.list_endpoints.command_name', 'list'), help=u"""Returns a list of Data Connectivity Management endpoints. \n[Command Reference](listEndpoints)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment containing the resources you want to list.""")
@cli_util.option('--registry-id', help=u"""DCMS registry ID""")
@cli_util.option('--name', help=u"""Used to filter by the name of the object.""")
@cli_util.option('--limit', type=click.INT, help=u"""Sets the maximum number of results per page, or items to return in a paginated `List` call. See [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See [List Pagination].""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "STARTING", "STOPPING", "STOPPED"]), help=u"""Lifecycle state of the resource.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME", "TIMEUPDATED"]), help=u"""This parameter allows users to specify a sort field. Default sort order is the descending order of `timeCreated` (most recently created objects at the top). Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'EndpointSummaryCollection'})
@cli_util.wrap_exceptions
def list_endpoints(ctx, from_json, all_pages, page_size, compartment_id, registry_id, name, limit, page, lifecycle_state, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if registry_id is not None:
        kwargs['registry_id'] = registry_id
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_endpoints,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_endpoints,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_endpoints(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@folder_group.command(name=cli_util.override('data_connectivity_management.list_folders.command_name', 'list'), help=u"""Retrieves a list of all the folders. \n[Command Reference](listFolders)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--name', help=u"""Used to filter by the name of the object.""")
@cli_util.option('--page', help=u"""For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""Sets the maximum number of results per page, or items to return in a paginated `List` call. See [List Pagination].""")
@cli_util.option('--fields', multiple=True, help=u"""Specifies the fields to get for an object.""")
@cli_util.option('--type', help=u"""Type of the object to filter the results with.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order are by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--favorites-query-param', type=custom_types.CliCaseInsensitiveChoice(["FAVORITES_ONLY", "NON_FAVORITES_ONLY", "ALL"]), help=u"""If value is FAVORITES_ONLY, then only objects marked as favorite by the requesting user will be included in result. If value is NON_FAVORITES_ONLY, then objects marked as favorites by the requesting user will be skipped. If value is ALL or if not specified, all objects, irrespective of favorites or not will be returned. Default is ALL.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_connectivity', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_connectivity', 'class': 'list[string]'}}, output_type={'module': 'data_connectivity', 'class': 'FolderSummaryCollection'})
@cli_util.wrap_exceptions
def list_folders(ctx, from_json, all_pages, page_size, registry_id, name, page, limit, fields, type, sort_by, sort_order, favorites_query_param):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if type is not None:
        kwargs['type'] = type
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if favorites_query_param is not None:
        kwargs['favorites_query_param'] = favorites_query_param
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_folders,
            registry_id=registry_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_folders,
            limit,
            page_size,
            registry_id=registry_id,
            **kwargs
        )
    else:
        result = client.list_folders(
            registry_id=registry_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@operation_summary_collection_group.command(name=cli_util.override('data_connectivity_management.list_operations.command_name', 'list-operations'), help=u"""Lists the summary of operations that are present in the schema, identified by the schema name. \n[Command Reference](listOperations)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--schema-resource-name', required=True, help=u"""The schema resource name used for retrieving schemas.""")
@cli_util.option('--name', help=u"""Used to filter by the name of the object.""")
@cli_util.option('--page', help=u"""For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""Sets the maximum number of results per page, or items to return in a paginated `List` call. See [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order are by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'OperationSummaryCollection'})
@cli_util.wrap_exceptions
def list_operations(ctx, from_json, all_pages, page_size, registry_id, connection_key, schema_resource_name, name, page, limit, sort_by, sort_order, endpoint_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_operations,
            registry_id=registry_id,
            connection_key=connection_key,
            schema_resource_name=schema_resource_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_operations,
            limit,
            page_size,
            registry_id=registry_id,
            connection_key=connection_key,
            schema_resource_name=schema_resource_name,
            **kwargs
        )
    else:
        result = client.list_operations(
            registry_id=registry_id,
            connection_key=connection_key,
            schema_resource_name=schema_resource_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@reference_artifact_summary_collection_group.command(name=cli_util.override('data_connectivity_management.list_reference_artifacts.command_name', 'list-reference-artifacts'), help=u"""Retrieves a list of all reference info of a dcms artifact. \n[Command Reference](listReferenceArtifacts)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--dcms-artifact-id', required=True, help=u"""The ID of a dcms artifact (DataAsset or Endpoint).""")
@cli_util.option('--page', help=u"""For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""Sets the maximum number of results per page, or items to return in a paginated `List` call. See [List Pagination].""")
@cli_util.option('--fields', multiple=True, help=u"""Specifies the fields to get for an object.""")
@cli_util.option('--type', help=u"""Type of the object to filter the results with.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order are by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--name', help=u"""Used to filter by the name of the object.""")
@cli_util.option('--exclude-types', multiple=True, help=u"""The types that will be excluded from the list of data assets/connections.""")
@cli_util.option('--favorites-query-param', type=custom_types.CliCaseInsensitiveChoice(["FAVORITES_ONLY", "NON_FAVORITES_ONLY", "ALL"]), help=u"""If value is FAVORITES_ONLY, then only objects marked as favorite by the requesting user will be included in result. If value is NON_FAVORITES_ONLY, then objects marked as favorites by the requesting user will be skipped. If value is ALL or if not specified, all objects, irrespective of favorites or not will be returned. Default is ALL.""")
@cli_util.option('--service-artifact-id', help=u"""Unique key of the service.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_connectivity', 'class': 'list[string]'}, 'exclude-types': {'module': 'data_connectivity', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_connectivity', 'class': 'list[string]'}, 'exclude-types': {'module': 'data_connectivity', 'class': 'list[string]'}}, output_type={'module': 'data_connectivity', 'class': 'ReferenceArtifactSummaryCollection'})
@cli_util.wrap_exceptions
def list_reference_artifacts(ctx, from_json, all_pages, page_size, registry_id, dcms_artifact_id, page, limit, fields, type, sort_by, sort_order, name, exclude_types, favorites_query_param, service_artifact_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(dcms_artifact_id, six.string_types) and len(dcms_artifact_id.strip()) == 0:
        raise click.UsageError('Parameter --dcms-artifact-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if type is not None:
        kwargs['type'] = type
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if name is not None:
        kwargs['name'] = name
    if exclude_types is not None and len(exclude_types) > 0:
        kwargs['exclude_types'] = exclude_types
    if favorites_query_param is not None:
        kwargs['favorites_query_param'] = favorites_query_param
    if service_artifact_id is not None:
        kwargs['service_artifact_id'] = service_artifact_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_reference_artifacts,
            registry_id=registry_id,
            dcms_artifact_id=dcms_artifact_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_reference_artifacts,
            limit,
            page_size,
            registry_id=registry_id,
            dcms_artifact_id=dcms_artifact_id,
            **kwargs
        )
    else:
        result = client.list_reference_artifacts(
            registry_id=registry_id,
            dcms_artifact_id=dcms_artifact_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@registry_group.command(name=cli_util.override('data_connectivity_management.list_registries.command_name', 'list'), help=u"""Retrieves a list of Data Connectivity Management registries. \n[Command Reference](listRegistries)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment containing the resources you want to list.""")
@cli_util.option('--name', help=u"""Used to filter by the name of the object.""")
@cli_util.option('--limit', type=click.INT, help=u"""Sets the maximum number of results per page, or items to return in a paginated `List` call. See [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See [List Pagination].""")
@cli_util.option('--is-deep-lookup', type=click.BOOL, help=u"""This parameter allows list registries to deep look at the whole tenancy.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "STARTING", "STOPPING", "STOPPED"]), help=u"""Lifecycle state of the resource.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'RegistrySummaryCollection'})
@cli_util.wrap_exceptions
def list_registries(ctx, from_json, all_pages, page_size, compartment_id, name, limit, page, is_deep_lookup, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if is_deep_lookup is not None:
        kwargs['is_deep_lookup'] = is_deep_lookup
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_registries,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_registries,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_registries(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@schema_group.command(name=cli_util.override('data_connectivity_management.list_schemas.command_name', 'list'), help=u"""Retrieves a list of all the schemas that can be accessed using the specified connection. \n[Command Reference](listSchemas)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--page', help=u"""For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""Sets the maximum number of results per page, or items to return in a paginated `List` call. See [List Pagination].""")
@cli_util.option('--fields', multiple=True, help=u"""Specifies the fields to get for an object.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order are by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--schema-resource-key', help=u"""Schema resource name used for retrieving schemas.""")
@cli_util.option('--name', help=u"""Used to filter by the name of the object.""")
@cli_util.option('--name-list', multiple=True, help=u"""Used to filter by the name of the object.""")
@cli_util.option('--endpoint-id', help=u"""Endpoint ID used for getDataAssetFullDetails.""")
@cli_util.option('--include-types', multiple=True, help=u"""Artifact type which needs to be listed while listing Artifacts.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_connectivity', 'class': 'list[string]'}, 'name-list': {'module': 'data_connectivity', 'class': 'list[string]'}, 'include-types': {'module': 'data_connectivity', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_connectivity', 'class': 'list[string]'}, 'name-list': {'module': 'data_connectivity', 'class': 'list[string]'}, 'include-types': {'module': 'data_connectivity', 'class': 'list[string]'}}, output_type={'module': 'data_connectivity', 'class': 'SchemaSummaryCollection'})
@cli_util.wrap_exceptions
def list_schemas(ctx, from_json, all_pages, page_size, registry_id, connection_key, page, limit, fields, sort_by, sort_order, schema_resource_key, name, name_list, endpoint_id, include_types):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if schema_resource_key is not None:
        kwargs['schema_resource_key'] = schema_resource_key
    if name is not None:
        kwargs['name'] = name
    if name_list is not None and len(name_list) > 0:
        kwargs['name_list'] = name_list
    if endpoint_id is not None:
        kwargs['endpoint_id'] = endpoint_id
    if include_types is not None and len(include_types) > 0:
        kwargs['include_types'] = include_types
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_schemas,
            registry_id=registry_id,
            connection_key=connection_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_schemas,
            limit,
            page_size,
            registry_id=registry_id,
            connection_key=connection_key,
            **kwargs
        )
    else:
        result = client.list_schemas(
            registry_id=registry_id,
            connection_key=connection_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@types_summary_collection_group.command(name=cli_util.override('data_connectivity_management.list_types.command_name', 'list-types'), help=u"""This endpoint retrieves a list of all the supported connector types. \n[Command Reference](listTypes)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--page', help=u"""For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""Sets the maximum number of results per page, or items to return in a paginated `List` call. See [List Pagination].""")
@cli_util.option('--type', help=u"""Type of the object to filter the results with.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order are by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--name', help=u"""Used to filter by the name of the object.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'TypesSummaryCollection'})
@cli_util.wrap_exceptions
def list_types(ctx, from_json, all_pages, page_size, registry_id, page, limit, type, sort_by, sort_order, name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if type is not None:
        kwargs['type'] = type
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if name is not None:
        kwargs['name'] = name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_types,
            registry_id=registry_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_types,
            limit,
            page_size,
            registry_id=registry_id,
            **kwargs
        )
    else:
        result = client.list_types(
            registry_id=registry_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('data_connectivity_management.list_work_request_errors.command_name', 'list'), help=u"""Returns a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""Sets the maximum number of results per page, or items to return in a paginated `List` call. See [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_group.command(name=cli_util.override('data_connectivity_management.list_work_request_logs.command_name', 'list'), help=u"""Returns a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""Sets the maximum number of results per page, or items to return in a paginated `List` call. See [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'WorkRequestLogCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('data_connectivity_management.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment containing the resources you want to list.""")
@cli_util.option('--registry-id', help=u"""DCMS registry ID""")
@cli_util.option('--work-request-status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""Work request status.""")
@cli_util.option('--page', help=u"""For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""Sets the maximum number of results per page, or items to return in a paginated `List` call. See [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_connectivity', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, registry_id, work_request_status, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if registry_id is not None:
        kwargs['registry_id'] = registry_id
    if work_request_status is not None:
        kwargs['work_request_status'] = work_request_status
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_connectivity_management.update_connection.command_name', 'update'), help=u"""Updates a connection under a data asset. \n[Command Reference](updateConnection)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key.""")
@cli_util.option('--properties', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""All the properties of the connection in a key-value map format.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', required=True, help=u"""Specific Connection Type""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--model-type', help=u"""The type of the object.""")
@cli_util.option('--name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--description', help=u"""User-defined description for the connection.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--primary-schema', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties of the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-default', type=click.BOOL, help=u"""The default property of the connection.""")
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'primary-schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'connection-properties': {'module': 'data_connectivity', 'class': 'list[ConnectionProperty]'}, 'properties': {'module': 'data_connectivity', 'class': 'dict(str, object)'}, 'metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'registry-metadata': {'module': 'data_connectivity', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'primary-schema': {'module': 'data_connectivity', 'class': 'Schema'}, 'connection-properties': {'module': 'data_connectivity', 'class': 'list[ConnectionProperty]'}, 'properties': {'module': 'data_connectivity', 'class': 'dict(str, object)'}, 'metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'registry-metadata': {'module': 'data_connectivity', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_connectivity', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection(ctx, from_json, force, registry_id, connection_key, properties, type, model_version, model_type, name, description, object_version, object_status, identifier, primary_schema, connection_properties, is_default, metadata, registry_metadata, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')
    if not force:
        if primary_schema or connection_properties or properties or metadata or registry_metadata:
            if not click.confirm("WARNING: Updates to primary-schema and connection-properties and properties and metadata and registry-metadata will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['properties'] = cli_util.parse_json_parameter("properties", properties)
    _details['type'] = type

    if model_version is not None:
        _details['modelVersion'] = model_version

    if model_type is not None:
        _details['modelType'] = model_type

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_version is not None:
        _details['objectVersion'] = object_version

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if primary_schema is not None:
        _details['primarySchema'] = cli_util.parse_json_parameter("primary_schema", primary_schema)

    if connection_properties is not None:
        _details['connectionProperties'] = cli_util.parse_json_parameter("connection_properties", connection_properties)

    if is_default is not None:
        _details['isDefault'] = is_default

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.update_connection(
        registry_id=registry_id,
        connection_key=connection_key,
        update_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_connectivity_management.update_data_asset.command_name', 'update'), help=u"""Updates a specific data asset with default connection. \n[Command Reference](updateDataAsset)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--data-asset-key', required=True, help=u"""The data asset key.""")
@cli_util.option('--properties', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""All the properties of the data asset in a key-value map format.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', required=True, help=u"""Specific DataAsset Type""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--model-type', help=u"""The type of the object.""")
@cli_util.option('--name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--description', help=u"""User-defined description of the data asset.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--external-key', help=u"""The external key of the object.""")
@cli_util.option('--asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional properties of the data asset.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--native-type-system', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--default-connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--end-points', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of endpoints with which this data asset is associated.

This option is a JSON list with items of type DpEndpoint.  For documentation on DpEndpoint please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/DpEndpoint.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'asset-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'properties': {'module': 'data_connectivity', 'class': 'dict(str, object)'}, 'native-type-system': {'module': 'data_connectivity', 'class': 'TypeSystem'}, 'registry-metadata': {'module': 'data_connectivity', 'class': 'RegistryMetadata'}, 'metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'default-connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'end-points': {'module': 'data_connectivity', 'class': 'list[DpEndpoint]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-properties': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'properties': {'module': 'data_connectivity', 'class': 'dict(str, object)'}, 'native-type-system': {'module': 'data_connectivity', 'class': 'TypeSystem'}, 'registry-metadata': {'module': 'data_connectivity', 'class': 'RegistryMetadata'}, 'metadata': {'module': 'data_connectivity', 'class': 'ObjectMetadata'}, 'default-connection': {'module': 'data_connectivity', 'class': 'Connection'}, 'end-points': {'module': 'data_connectivity', 'class': 'list[DpEndpoint]'}}, output_type={'module': 'data_connectivity', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def update_data_asset(ctx, from_json, force, registry_id, data_asset_key, properties, type, model_version, model_type, name, description, object_status, object_version, identifier, external_key, asset_properties, native_type_system, registry_metadata, metadata, default_connection, end_points, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')
    if not force:
        if asset_properties or properties or native_type_system or registry_metadata or metadata or default_connection or end_points:
            if not click.confirm("WARNING: Updates to asset-properties and properties and native-type-system and registry-metadata and metadata and default-connection and end-points will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['properties'] = cli_util.parse_json_parameter("properties", properties)
    _details['type'] = type

    if model_version is not None:
        _details['modelVersion'] = model_version

    if model_type is not None:
        _details['modelType'] = model_type

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if object_version is not None:
        _details['objectVersion'] = object_version

    if identifier is not None:
        _details['identifier'] = identifier

    if external_key is not None:
        _details['externalKey'] = external_key

    if asset_properties is not None:
        _details['assetProperties'] = cli_util.parse_json_parameter("asset_properties", asset_properties)

    if native_type_system is not None:
        _details['nativeTypeSystem'] = cli_util.parse_json_parameter("native_type_system", native_type_system)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if default_connection is not None:
        _details['defaultConnection'] = cli_util.parse_json_parameter("default_connection", default_connection)

    if end_points is not None:
        _details['endPoints'] = cli_util.parse_json_parameter("end_points", end_points)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.update_data_asset(
        registry_id=registry_id,
        data_asset_key=data_asset_key,
        update_data_asset_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@endpoint_group.command(name=cli_util.override('data_connectivity_management.update_endpoint.command_name', 'update'), help=u"""Updates the Data Connectivity Management endpoint. \n[Command Reference](updateEndpoint)""")
@cli_util.option('--endpoint-id', required=True, help=u"""DCMS endpoint ID.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Data Connectivity Management Registry description""")
@cli_util.option('--display-name', help=u"""The Data Connectivity Management registry display name; registries can be renamed.""")
@cli_util.option('--endpoint-size', type=click.INT, help=u"""Update endpoint size for reverse connection capacity.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of NSGs to which the Private Endpoint VNIC must be added.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dns-zones', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of DNS zones to be used by the data assets. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-id', help=u"""DCMS registry ID""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_connectivity', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'data_connectivity', 'class': 'list[string]'}, 'dns-zones': {'module': 'data_connectivity', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_connectivity', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'data_connectivity', 'class': 'list[string]'}, 'dns-zones': {'module': 'data_connectivity', 'class': 'list[string]'}}, output_type={'module': 'data_connectivity', 'class': 'Endpoint'})
@cli_util.wrap_exceptions
def update_endpoint(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, endpoint_id, freeform_tags, defined_tags, description, display_name, endpoint_size, nsg_ids, dns_zones, registry_id, if_match):

    if isinstance(endpoint_id, six.string_types) and len(endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --endpoint-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or nsg_ids or dns_zones:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and nsg-ids and dns-zones will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if registry_id is not None:
        kwargs['registry_id'] = registry_id
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if endpoint_size is not None:
        _details['endpointSize'] = endpoint_size

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if dns_zones is not None:
        _details['dnsZones'] = cli_util.parse_json_parameter("dns_zones", dns_zones)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.update_endpoint(
        endpoint_id=endpoint_id,
        update_endpoint_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@folder_group.command(name=cli_util.override('data_connectivity_management.update_folder.command_name', 'update'), help=u"""Updates a folder under a specified registry. \n[Command Reference](updateFolder)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--folder-key', required=True, help=u"""The folder ID.""")
@cli_util.option('--model-type', required=True, help=u"""The type of the folder.""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify the folder. In scenarios where reference to the folder is required, a value can be passed in create.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.""")
@cli_util.option('--description', help=u"""User-defined description of the folder.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.""")
@cli_util.option('--data-assets', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of data assets that belong to the folder.

This option is a JSON list with items of type DataAsset.  For documentation on DataAsset please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataconnectivitymanagement/20210217/datatypes/DataAsset.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-assets': {'module': 'data_connectivity', 'class': 'list[DataAsset]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_connectivity', 'class': 'ParentReference'}, 'data-assets': {'module': 'data_connectivity', 'class': 'list[DataAsset]'}}, output_type={'module': 'data_connectivity', 'class': 'Folder'})
@cli_util.wrap_exceptions
def update_folder(ctx, from_json, force, registry_id, folder_key, model_type, key, object_version, model_version, parent_ref, name, description, object_status, identifier, data_assets, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')

    if isinstance(folder_key, six.string_types) and len(folder_key.strip()) == 0:
        raise click.UsageError('Parameter --folder-key cannot be whitespace or empty string')
    if not force:
        if parent_ref or data_assets:
            if not click.confirm("WARNING: Updates to parent-ref and data-assets will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelType'] = model_type
    _details['key'] = key
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if data_assets is not None:
        _details['dataAssets'] = cli_util.parse_json_parameter("data_assets", data_assets)

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.update_folder(
        registry_id=registry_id,
        folder_key=folder_key,
        update_folder_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@registry_group.command(name=cli_util.override('data_connectivity_management.update_registry.command_name', 'update'), help=u"""Updates the Data Connectivity Management Registry. \n[Command Reference](updateRegistry)""")
@cli_util.option('--registry-id', required=True, help=u"""The registry OCID.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or registry. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a registry. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Data Connectivity Management Registry description.""")
@cli_util.option('--display-name', help=u"""Data Connectivity Management Registry display name, registries can be renamed.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_connectivity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_connectivity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_connectivity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_connectivity', 'class': 'Registry'})
@cli_util.wrap_exceptions
def update_registry(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, registry_id, freeform_tags, defined_tags, description, display_name, if_match):

    if isinstance(registry_id, six.string_types) and len(registry_id.strip()) == 0:
        raise click.UsageError('Parameter --registry-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.update_registry(
        registry_id=registry_id,
        update_registry_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@endpoint_group.command(name=cli_util.override('data_connectivity_management.validate_data_asset_network_reachablity.command_name', 'validate-data-asset-network-reachablity'), help=u"""Validates the dataAsset network reachability. \n[Command Reference](validateDataAssetNetworkReachablity)""")
@cli_util.option('--endpoint-id', required=True, help=u"""DCMS endpoint ID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@cli_util.option('--registry-id', help=u"""DCMS registry ID""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def validate_data_asset_network_reachablity(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, endpoint_id, if_match, registry_id):

    if isinstance(endpoint_id, six.string_types) and len(endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if registry_id is not None:
        kwargs['registry_id'] = registry_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_connectivity', 'data_connectivity_management', ctx)
    result = client.validate_data_asset_network_reachablity(
        endpoint_id=endpoint_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
