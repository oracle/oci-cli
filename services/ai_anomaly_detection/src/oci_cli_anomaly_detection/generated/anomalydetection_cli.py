# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('anomaly_detection.anomaly_detection_root_group.command_name', 'anomaly-detection'), cls=CommandGroupWithAlias, help=cli_util.override('anomaly_detection.anomaly_detection_root_group.help', """OCI AI Service solutions can help Enterprise customers integrate AI into their products immediately by using our proven,
pre-trained/custom models or containers, and without a need to set up in house team of AI and ML experts.
This allows enterprises to focus on business drivers and development work rather than AI/ML operations, shortening the time to market."""), short_help=cli_util.override('anomaly_detection.anomaly_detection_root_group.short_help', """Oracle Cloud AI Services API"""))
@cli_util.help_option_group
def anomaly_detection_root_group():
    pass


@click.command(cli_util.override('anomaly_detection.data_asset_collection_group.command_name', 'data-asset-collection'), cls=CommandGroupWithAlias, help="""Results of a dataAsset search. Contains both DataAssetSummary items and other data.""")
@cli_util.help_option_group
def data_asset_collection_group():
    pass


@click.command(cli_util.override('anomaly_detection.ai_private_endpoint_collection_group.command_name', 'ai-private-endpoint-collection'), cls=CommandGroupWithAlias, help="""A collection of AI Service PrivateEndpoints Each item is a AI Service PrivateEndpoint Summary object.""")
@cli_util.help_option_group
def ai_private_endpoint_collection_group():
    pass


@click.command(cli_util.override('anomaly_detection.data_asset_group.command_name', 'data-asset'), cls=CommandGroupWithAlias, help="""Description of DataAsset.""")
@cli_util.help_option_group
def data_asset_group():
    pass


@click.command(cli_util.override('anomaly_detection.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('anomaly_detection.project_group.command_name', 'project'), cls=CommandGroupWithAlias, help="""Project enable users to organize their resources.""")
@cli_util.help_option_group
def project_group():
    pass


@click.command(cli_util.override('anomaly_detection.model_group.command_name', 'model'), cls=CommandGroupWithAlias, help="""Description of Model.""")
@cli_util.help_option_group
def model_group():
    pass


@click.command(cli_util.override('anomaly_detection.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('anomaly_detection.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('anomaly_detection.ai_private_endpoint_group.command_name', 'ai-private-endpoint'), cls=CommandGroupWithAlias, help="""A private network reverse connection creates a connection from service to customer subnet over a private network.""")
@cli_util.help_option_group
def ai_private_endpoint_group():
    pass


anomaly_detection_root_group.add_command(data_asset_collection_group)
anomaly_detection_root_group.add_command(ai_private_endpoint_collection_group)
anomaly_detection_root_group.add_command(data_asset_group)
anomaly_detection_root_group.add_command(work_request_error_group)
anomaly_detection_root_group.add_command(project_group)
anomaly_detection_root_group.add_command(model_group)
anomaly_detection_root_group.add_command(work_request_log_entry_group)
anomaly_detection_root_group.add_command(work_request_group)
anomaly_detection_root_group.add_command(ai_private_endpoint_group)


@work_request_group.command(name=cli_util.override('anomaly_detection.cancel_work_request.command_name', 'cancel'), help=u"""Cancel work request with the given ID. \n[Command Reference](cancelWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_work_request(ctx, from_json, work_request_id, if_match):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.cancel_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ai_private_endpoint_group.command(name=cli_util.override('anomaly_detection.change_ai_private_endpoint_compartment.command_name', 'change-compartment'), help=u"""Moves a resource into a different compartment. When provided, 'If-Match' is checked against 'ETag' values of the resource. \n[Command Reference](changeAiPrivateEndpointCompartment)""")
@cli_util.option('--ai-private-endpoint-id', required=True, help=u"""Unique private reverse connection identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The identifier of the compartment where the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_ai_private_endpoint_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, ai_private_endpoint_id, compartment_id, if_match):

    if isinstance(ai_private_endpoint_id, six.string_types) and len(ai_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --ai-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.change_ai_private_endpoint_compartment(
        ai_private_endpoint_id=ai_private_endpoint_id,
        change_ai_private_endpoint_compartment_details=_details,
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


@data_asset_group.command(name=cli_util.override('anomaly_detection.change_data_asset_compartment.command_name', 'change-compartment'), help=u"""Changing the compartment of a data asset. \n[Command Reference](changeDataAssetCompartment)""")
@cli_util.option('--data-asset-id', required=True, help=u"""The OCID of the Data Asset.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def change_data_asset_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, data_asset_id, compartment_id, if_match):

    if isinstance(data_asset_id, six.string_types) and len(data_asset_id.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.change_data_asset_compartment(
        data_asset_id=data_asset_id,
        change_data_asset_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_asset') and callable(getattr(client, 'get_data_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('anomaly_detection.change_model_compartment.command_name', 'change-compartment'), help=u"""Moves a Model resource from one compartment to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeModelCompartment)""")
@cli_util.option('--model-id', required=True, help=u"""The OCID of the Model.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_model_compartment(ctx, from_json, model_id, compartment_id, if_match):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.change_model_compartment(
        model_id=model_id,
        change_model_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('anomaly_detection.change_project_compartment.command_name', 'change-compartment'), help=u"""Moves a Project resource from one compartment to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeProjectCompartment)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the Project.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_project_compartment(ctx, from_json, project_id, compartment_id, if_match):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.change_project_compartment(
        project_id=project_id,
        change_project_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ai_private_endpoint_group.command(name=cli_util.override('anomaly_detection.create_ai_private_endpoint.command_name', 'create'), help=u"""Create a new private reverse connection endpoint. \n[Command Reference](createAiPrivateEndpoint)""")
@cli_util.option('--dns-zones', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of DNS zones to be used by the data assets. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--subnet-id', required=True, help=u"""The OCID of subnet to which the reverse connection is to be created.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment identifier.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Display name of the private endpoint resource being created.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'dns-zones': {'module': 'ai_anomaly_detection', 'class': 'list[string]'}, 'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dns-zones': {'module': 'ai_anomaly_detection', 'class': 'list[string]'}, 'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_ai_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dns_zones, subnet_id, compartment_id, freeform_tags, defined_tags, display_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dnsZones'] = cli_util.parse_json_parameter("dns_zones", dns_zones)
    _details['subnetId'] = subnet_id
    _details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.create_ai_private_endpoint(
        create_ai_private_endpoint_details=_details,
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


@data_asset_group.command(name=cli_util.override('anomaly_detection.create_data_asset.command_name', 'create'), help=u"""Creates a new DataAsset. \n[Command Reference](createDataAsset)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID for the data asset's compartment.""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate with the data asset.""")
@cli_util.option('--data-source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the Ai data asset""")
@cli_util.option('--private-endpoint-id', help=u"""OCID of Private Endpoint.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'data-source-details': {'module': 'ai_anomaly_detection', 'class': 'DataSourceDetails'}, 'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'data-source-details': {'module': 'ai_anomaly_detection', 'class': 'DataSourceDetails'}, 'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_anomaly_detection', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def create_data_asset(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, project_id, data_source_details, display_name, description, private_endpoint_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['projectId'] = project_id
    _details['dataSourceDetails'] = cli_util.parse_json_parameter("data_source_details", data_source_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if private_endpoint_id is not None:
        _details['privateEndpointId'] = private_endpoint_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.create_data_asset(
        create_data_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_asset') and callable(getattr(client, 'get_data_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('anomaly_detection.create_data_asset_data_source_details_object_storage.command_name', 'create-data-asset-data-source-details-object-storage'), help=u"""Creates a new DataAsset. \n[Command Reference](createDataAsset)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID for the data asset's compartment.""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate with the data asset.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the Ai data asset""")
@cli_util.option('--private-endpoint-id', help=u"""OCID of Private Endpoint.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-source-details-namespace', help=u"""Object storage namespace""")
@cli_util.option('--data-source-details-bucket-name', help=u"""Object storage bucket name""")
@cli_util.option('--data-source-details-object-name', help=u"""File name""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_anomaly_detection', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def create_data_asset_data_source_details_object_storage(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, project_id, display_name, description, private_endpoint_id, freeform_tags, defined_tags, data_source_details_namespace, data_source_details_bucket_name, data_source_details_object_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataSourceDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['projectId'] = project_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if private_endpoint_id is not None:
        _details['privateEndpointId'] = private_endpoint_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if data_source_details_namespace is not None:
        _details['dataSourceDetails']['namespace'] = data_source_details_namespace

    if data_source_details_bucket_name is not None:
        _details['dataSourceDetails']['bucketName'] = data_source_details_bucket_name

    if data_source_details_object_name is not None:
        _details['dataSourceDetails']['objectName'] = data_source_details_object_name

    _details['dataSourceDetails']['dataSourceType'] = 'ORACLE_OBJECT_STORAGE'

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.create_data_asset(
        create_data_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_asset') and callable(getattr(client, 'get_data_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('anomaly_detection.create_data_asset_data_source_details_influx.command_name', 'create-data-asset-data-source-details-influx'), help=u"""Creates a new DataAsset. \n[Command Reference](createDataAsset)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID for the data asset's compartment.""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate with the data asset.""")
@cli_util.option('--data-source-details-version-specific-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-source-details-user-name', required=True, help=u"""Username for connection to Influx""")
@cli_util.option('--data-source-details-password-secret-id', required=True, help=u"""Password Secret Id for the influx connection""")
@cli_util.option('--data-source-details-measurement-name', required=True, help=u"""Measurement name for influx""")
@cli_util.option('--data-source-details-url', required=True, help=u"""public IP address and port to influx DB""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the Ai data asset""")
@cli_util.option('--private-endpoint-id', help=u"""OCID of Private Endpoint.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}, 'data-source-details-version-specific-details': {'module': 'ai_anomaly_detection', 'class': 'InfluxDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}, 'data-source-details-version-specific-details': {'module': 'ai_anomaly_detection', 'class': 'InfluxDetails'}}, output_type={'module': 'ai_anomaly_detection', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def create_data_asset_data_source_details_influx(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, project_id, data_source_details_version_specific_details, data_source_details_user_name, data_source_details_password_secret_id, data_source_details_measurement_name, data_source_details_url, display_name, description, private_endpoint_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataSourceDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['projectId'] = project_id
    _details['dataSourceDetails']['versionSpecificDetails'] = cli_util.parse_json_parameter("data_source_details_version_specific_details", data_source_details_version_specific_details)
    _details['dataSourceDetails']['userName'] = data_source_details_user_name
    _details['dataSourceDetails']['passwordSecretId'] = data_source_details_password_secret_id
    _details['dataSourceDetails']['measurementName'] = data_source_details_measurement_name
    _details['dataSourceDetails']['url'] = data_source_details_url

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if private_endpoint_id is not None:
        _details['privateEndpointId'] = private_endpoint_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['dataSourceDetails']['dataSourceType'] = 'INFLUX'

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.create_data_asset(
        create_data_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_asset') and callable(getattr(client, 'get_data_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('anomaly_detection.create_data_asset_data_source_details_atp.command_name', 'create-data-asset-data-source-details-atp'), help=u"""Creates a new DataAsset. \n[Command Reference](createDataAsset)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID for the data asset's compartment.""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate with the data asset.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the Ai data asset""")
@cli_util.option('--private-endpoint-id', help=u"""OCID of Private Endpoint.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-source-details-wallet-password-secret-id', help=u"""wallet password Secret ID in String format""")
@cli_util.option('--data-source-details-atp-user-name', help=u"""atp db user name""")
@cli_util.option('--data-source-details-atp-password-secret-id', help=u"""atp db password Secret Id""")
@cli_util.option('--data-source-details-cwallet-file-secret-id', help=u"""OCID of the secret containing the containers certificates of ATP wallet""")
@cli_util.option('--data-source-details-ewallet-file-secret-id', help=u"""OCID of the secret containing the PDB'S certificates of ATP wallet""")
@cli_util.option('--data-source-details-key-store-file-secret-id', help=u"""OCID of the secret containing Keystore.jks file of the ATP wallet""")
@cli_util.option('--data-source-details-ojdbc-file-secret-id', help=u"""OCID of the secret that contains jdbc properties file of ATP wallet""")
@cli_util.option('--data-source-details-tnsnames-file-secret-id', help=u"""OCID of the secret that contains the tnsnames file of ATP wallet""")
@cli_util.option('--data-source-details-truststore-file-secret-id', help=u"""OCID of the secret containing truststore.jks file of the ATP wallet""")
@cli_util.option('--data-source-details-database-name', help=u"""atp database name""")
@cli_util.option('--data-source-details-table-name', help=u"""atp database table name""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_anomaly_detection', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def create_data_asset_data_source_details_atp(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, project_id, display_name, description, private_endpoint_id, freeform_tags, defined_tags, data_source_details_wallet_password_secret_id, data_source_details_atp_user_name, data_source_details_atp_password_secret_id, data_source_details_cwallet_file_secret_id, data_source_details_ewallet_file_secret_id, data_source_details_key_store_file_secret_id, data_source_details_ojdbc_file_secret_id, data_source_details_tnsnames_file_secret_id, data_source_details_truststore_file_secret_id, data_source_details_database_name, data_source_details_table_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataSourceDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['projectId'] = project_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if private_endpoint_id is not None:
        _details['privateEndpointId'] = private_endpoint_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if data_source_details_wallet_password_secret_id is not None:
        _details['dataSourceDetails']['walletPasswordSecretId'] = data_source_details_wallet_password_secret_id

    if data_source_details_atp_user_name is not None:
        _details['dataSourceDetails']['atpUserName'] = data_source_details_atp_user_name

    if data_source_details_atp_password_secret_id is not None:
        _details['dataSourceDetails']['atpPasswordSecretId'] = data_source_details_atp_password_secret_id

    if data_source_details_cwallet_file_secret_id is not None:
        _details['dataSourceDetails']['cwalletFileSecretId'] = data_source_details_cwallet_file_secret_id

    if data_source_details_ewallet_file_secret_id is not None:
        _details['dataSourceDetails']['ewalletFileSecretId'] = data_source_details_ewallet_file_secret_id

    if data_source_details_key_store_file_secret_id is not None:
        _details['dataSourceDetails']['keyStoreFileSecretId'] = data_source_details_key_store_file_secret_id

    if data_source_details_ojdbc_file_secret_id is not None:
        _details['dataSourceDetails']['ojdbcFileSecretId'] = data_source_details_ojdbc_file_secret_id

    if data_source_details_tnsnames_file_secret_id is not None:
        _details['dataSourceDetails']['tnsnamesFileSecretId'] = data_source_details_tnsnames_file_secret_id

    if data_source_details_truststore_file_secret_id is not None:
        _details['dataSourceDetails']['truststoreFileSecretId'] = data_source_details_truststore_file_secret_id

    if data_source_details_database_name is not None:
        _details['dataSourceDetails']['databaseName'] = data_source_details_database_name

    if data_source_details_table_name is not None:
        _details['dataSourceDetails']['tableName'] = data_source_details_table_name

    _details['dataSourceDetails']['dataSourceType'] = 'ORACLE_ATP'

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.create_data_asset(
        create_data_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_asset') and callable(getattr(client, 'get_data_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('anomaly_detection.create_model.command_name', 'create'), help=u"""Creates a new Model. \n[Command Reference](createModel)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID for the ai model's compartment.""")
@cli_util.option('--model-training-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate with the model.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the ai model.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'model-training-details': {'module': 'ai_anomaly_detection', 'class': 'ModelTrainingDetails'}, 'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'model-training-details': {'module': 'ai_anomaly_detection', 'class': 'ModelTrainingDetails'}, 'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_anomaly_detection', 'class': 'Model'})
@cli_util.wrap_exceptions
def create_model(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, model_training_details, project_id, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['modelTrainingDetails'] = cli_util.parse_json_parameter("model_training_details", model_training_details)
    _details['projectId'] = project_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.create_model(
        create_model_details=_details,
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


@project_group.command(name=cli_util.override('anomaly_detection.create_project.command_name', 'create'), help=u"""Creates a new Project. \n[Command Reference](createProject)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID for the project's compartment.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the project.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "FAILED", "DELETING", "DELETED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_anomaly_detection', 'class': 'Project'})
@cli_util.wrap_exceptions
def create_project(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.create_project(
        create_project_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_project') and callable(getattr(client, 'get_project')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_project(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@ai_private_endpoint_group.command(name=cli_util.override('anomaly_detection.delete_ai_private_endpoint.command_name', 'delete'), help=u"""Deletes a private reverse connection endpoint by identifier. \n[Command Reference](deleteAiPrivateEndpoint)""")
@cli_util.option('--ai-private-endpoint-id', required=True, help=u"""Unique private reverse connection identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_ai_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, ai_private_endpoint_id, if_match):

    if isinstance(ai_private_endpoint_id, six.string_types) and len(ai_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --ai-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.delete_ai_private_endpoint(
        ai_private_endpoint_id=ai_private_endpoint_id,
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


@data_asset_group.command(name=cli_util.override('anomaly_detection.delete_data_asset.command_name', 'delete'), help=u"""Deletes a DataAsset resource by identifier \n[Command Reference](deleteDataAsset)""")
@cli_util.option('--data-asset-id', required=True, help=u"""The OCID of the Data Asset.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_data_asset(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, data_asset_id, if_match):

    if isinstance(data_asset_id, six.string_types) and len(data_asset_id.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.delete_data_asset(
        data_asset_id=data_asset_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_asset') and callable(getattr(client, 'get_data_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_data_asset(data_asset_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('anomaly_detection.delete_model.command_name', 'delete'), help=u"""Deletes an ai model resource by identifier. This operation fails with a 409 error unless all associated resources are in a DELETED state. You must delete all associated resources before deleting a project. \n[Command Reference](deleteModel)""")
@cli_util.option('--model-id', required=True, help=u"""The OCID of the Model.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_model(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, model_id, if_match):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.delete_model(
        model_id=model_id,
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


@project_group.command(name=cli_util.override('anomaly_detection.delete_project.command_name', 'delete'), help=u"""Deletes a Project resource by identifier. This operation fails with a 409 error unless all associated resources (models deployments or data assets) are in a DELETED state. You must delete all associated resources before deleting a project. \n[Command Reference](deleteProject)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the Project.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_project(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, if_match):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.delete_project(
        project_id=project_id,
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


@model_group.command(name=cli_util.override('anomaly_detection.detect_anomalies.command_name', 'detect-anomalies'), help=u"""Make a detect call with an anomaly model and detection data \n[Command Reference](detectAnomalies)""")
@cli_util.option('--model-id', required=True, help=u"""The OCID of the trained model\u3002""")
@cli_util.option('--request-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["INLINE", "BASE64_ENCODED"]), help=u"""Type of request. This parameter will be filled autmatically by classes generated by the SDK. For raw curl request, user will have to provide this field.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'AnomalyDetectResult'})
@cli_util.wrap_exceptions
def detect_anomalies(ctx, from_json, model_id, request_type, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelId'] = model_id
    _details['requestType'] = request_type

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.detect_anomalies(
        detect_anomalies_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('anomaly_detection.detect_anomalies_inline_detect_anomalies_request.command_name', 'detect-anomalies-inline-detect-anomalies-request'), help=u"""Make a detect call with an anomaly model and detection data \n[Command Reference](detectAnomalies)""")
@cli_util.option('--model-id', required=True, help=u"""The OCID of the trained model\u3002""")
@cli_util.option('--signal-names', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of signal names.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array containing data.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'signal-names': {'module': 'ai_anomaly_detection', 'class': 'list[string]'}, 'data': {'module': 'ai_anomaly_detection', 'class': 'list[DataItem]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'signal-names': {'module': 'ai_anomaly_detection', 'class': 'list[string]'}, 'data': {'module': 'ai_anomaly_detection', 'class': 'list[DataItem]'}}, output_type={'module': 'ai_anomaly_detection', 'class': 'AnomalyDetectResult'})
@cli_util.wrap_exceptions
def detect_anomalies_inline_detect_anomalies_request(ctx, from_json, model_id, signal_names, data, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelId'] = model_id
    _details['signalNames'] = cli_util.parse_json_parameter("signal_names", signal_names)
    _details['data'] = cli_util.parse_json_parameter("data", data)

    _details['requestType'] = 'INLINE'

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.detect_anomalies(
        detect_anomalies_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('anomaly_detection.detect_anomalies_embedded_detect_anomalies_request.command_name', 'detect-anomalies-embedded-detect-anomalies-request'), help=u"""Make a detect call with an anomaly model and detection data \n[Command Reference](detectAnomalies)""")
@cli_util.option('--model-id', required=True, help=u"""The OCID of the trained model\u3002""")
@cli_util.option('--content', required=True, help=u"""""")
@cli_util.option('--content-type', type=custom_types.CliCaseInsensitiveChoice(["CSV", "JSON"]), help=u"""""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'AnomalyDetectResult'})
@cli_util.wrap_exceptions
def detect_anomalies_embedded_detect_anomalies_request(ctx, from_json, model_id, content, content_type, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelId'] = model_id
    _details['content'] = content

    if content_type is not None:
        _details['contentType'] = content_type

    _details['requestType'] = 'BASE64_ENCODED'

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.detect_anomalies(
        detect_anomalies_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ai_private_endpoint_group.command(name=cli_util.override('anomaly_detection.get_ai_private_endpoint.command_name', 'get'), help=u"""Gets a specific private reverse connection by identifier. \n[Command Reference](getAiPrivateEndpoint)""")
@cli_util.option('--ai-private-endpoint-id', required=True, help=u"""Unique private reverse connection identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'AiPrivateEndpoint'})
@cli_util.wrap_exceptions
def get_ai_private_endpoint(ctx, from_json, ai_private_endpoint_id):

    if isinstance(ai_private_endpoint_id, six.string_types) and len(ai_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --ai-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.get_ai_private_endpoint(
        ai_private_endpoint_id=ai_private_endpoint_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('anomaly_detection.get_data_asset.command_name', 'get'), help=u"""Gets a DataAsset by identifier \n[Command Reference](getDataAsset)""")
@cli_util.option('--data-asset-id', required=True, help=u"""The OCID of the Data Asset.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def get_data_asset(ctx, from_json, data_asset_id):

    if isinstance(data_asset_id, six.string_types) and len(data_asset_id.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.get_data_asset(
        data_asset_id=data_asset_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('anomaly_detection.get_model.command_name', 'get'), help=u"""Gets a Model by identifier \n[Command Reference](getModel)""")
@cli_util.option('--model-id', required=True, help=u"""The OCID of the Model.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'Model'})
@cli_util.wrap_exceptions
def get_model(ctx, from_json, model_id):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.get_model(
        model_id=model_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('anomaly_detection.get_project.command_name', 'get'), help=u"""Gets a Project by identifier \n[Command Reference](getProject)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the Project.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'Project'})
@cli_util.wrap_exceptions
def get_project(ctx, from_json, project_id):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.get_project(
        project_id=project_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('anomaly_detection.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ai_private_endpoint_collection_group.command(name=cli_util.override('anomaly_detection.list_ai_private_endpoints.command_name', 'list-ai-private-endpoints'), help=u"""Returns a list of all the AI private endpoints in the specified compartment. \n[Command Reference](listAiPrivateEndpoints)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""<b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--id', help=u"""unique AiPrivateEndpoint identifier""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'AiPrivateEndpointCollection'})
@cli_util.wrap_exceptions
def list_ai_private_endpoints(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_ai_private_endpoints,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_ai_private_endpoints,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_ai_private_endpoints(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@data_asset_collection_group.command(name=cli_util.override('anomaly_detection.list_data_assets.command_name', 'list-data-assets'), help=u"""Returns a list of DataAssets. \n[Command Reference](listDataAssets)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--project-id', help=u"""The ID of the project for which to list the objects.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), help=u"""<b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'DataAssetCollection'})
@cli_util.wrap_exceptions
def list_data_assets(ctx, from_json, all_pages, page_size, compartment_id, project_id, display_name, limit, page, lifecycle_state, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if project_id is not None:
        kwargs['project_id'] = project_id
    if display_name is not None:
        kwargs['display_name'] = display_name
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
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_assets,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_assets,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_data_assets(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('anomaly_detection.list_models.command_name', 'list'), help=u"""Returns a list of Models. \n[Command Reference](listModels)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--project-id', help=u"""The ID of the project for which to list the objects.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["DELETING", "DELETED", "FAILED", "CREATING", "ACTIVE", "UPDATING"]), help=u"""<b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'ModelCollection'})
@cli_util.wrap_exceptions
def list_models(ctx, from_json, all_pages, page_size, compartment_id, project_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if project_id is not None:
        kwargs['project_id'] = project_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_models,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_models,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_models(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('anomaly_detection.list_projects.command_name', 'list'), help=u"""Returns a list of  Projects. \n[Command Reference](listProjects)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "FAILED", "DELETING", "DELETED", "UPDATING"]), help=u"""<b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'ProjectCollection'})
@cli_util.wrap_exceptions
def list_projects(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_projects,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_projects,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_projects(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('anomaly_detection.list_work_request_errors.command_name', 'list'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'WorkRequestErrorCollection'})
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
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
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


@work_request_log_entry_group.command(name=cli_util.override('anomaly_detection.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'WorkRequestLogEntryCollection'})
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
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
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


@work_request_group.command(name=cli_util.override('anomaly_detection.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--work-request-id', help=u"""The ID of the asynchronous work request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_anomaly_detection', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if work_request_id is not None:
        kwargs['work_request_id'] = work_request_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
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


@ai_private_endpoint_group.command(name=cli_util.override('anomaly_detection.update_ai_private_endpoint.command_name', 'update'), help=u"""Updates the private reverse connection endpoint. \n[Command Reference](updateAiPrivateEndpoint)""")
@cli_util.option('--ai-private-endpoint-id', required=True, help=u"""Unique private reverse connection identifier.""")
@cli_util.option('--dns-zones', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of DNS zones to be used by the data assets. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Display name of the private endpoint resource.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'dns-zones': {'module': 'ai_anomaly_detection', 'class': 'list[string]'}, 'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dns-zones': {'module': 'ai_anomaly_detection', 'class': 'list[string]'}, 'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_ai_private_endpoint(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, ai_private_endpoint_id, dns_zones, freeform_tags, defined_tags, display_name, if_match):

    if isinstance(ai_private_endpoint_id, six.string_types) and len(ai_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --ai-private-endpoint-id cannot be whitespace or empty string')
    if not force:
        if dns_zones or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to dns-zones and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if dns_zones is not None:
        _details['dnsZones'] = cli_util.parse_json_parameter("dns_zones", dns_zones)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.update_ai_private_endpoint(
        ai_private_endpoint_id=ai_private_endpoint_id,
        update_ai_private_endpoint_details=_details,
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


@data_asset_group.command(name=cli_util.override('anomaly_detection.update_data_asset.command_name', 'update'), help=u"""Updates the DataAsset \n[Command Reference](updateDataAsset)""")
@cli_util.option('--data-asset-id', required=True, help=u"""The OCID of the Data Asset.""")
@cli_util.option('--display-name', help=u"""DataAsset Identifier""")
@cli_util.option('--description', help=u"""DataAsset description""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_anomaly_detection', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def update_data_asset(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, data_asset_id, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(data_asset_id, six.string_types) and len(data_asset_id.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.update_data_asset(
        data_asset_id=data_asset_id,
        update_data_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_asset') and callable(getattr(client, 'get_data_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('anomaly_detection.update_model.command_name', 'update'), help=u"""Updates the Model \n[Command Reference](updateModel)""")
@cli_util.option('--model-id', required=True, help=u"""The OCID of the Model.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the ai model.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_model(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, model_id, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.update_model(
        model_id=model_id,
        update_model_details=_details,
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


@project_group.command(name=cli_util.override('anomaly_detection.update_project.command_name', 'update'), help=u"""Updates the Project \n[Command Reference](updateProject)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the Project.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the project.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "FAILED", "DELETING", "DELETED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_anomaly_detection', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_anomaly_detection', 'class': 'Project'})
@cli_util.wrap_exceptions
def update_project(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ai_anomaly_detection', 'anomaly_detection', ctx)
    result = client.update_project(
        project_id=project_id,
        update_project_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_project') and callable(getattr(client, 'get_project')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_project(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
