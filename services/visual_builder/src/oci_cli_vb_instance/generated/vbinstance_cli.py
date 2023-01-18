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


@cli.command(cli_util.override('visual_builder.visual_builder_root_group.command_name', 'visual-builder'), cls=CommandGroupWithAlias, help=cli_util.override('visual_builder.visual_builder_root_group.help', """Oracle Visual Builder enables developers to quickly build web and mobile applications. With a visual development environment that makes it easy to connect to Oracle data and third-party REST services, developers can build modern, consumer-grade applications in a fraction of the time it would take in other tools.
The Visual Builder Instance Management API allows users to create and manage a Visual Builder instance."""), short_help=cli_util.override('visual_builder.visual_builder_root_group.short_help', """Visual Builder API"""))
@cli_util.help_option_group
def visual_builder_root_group():
    pass


@click.command(cli_util.override('visual_builder.work_request_error_collection_group.command_name', 'work-request-error-collection'), cls=CommandGroupWithAlias, help="""Result of a WorkRequest Error request. Contains list of WorkRequestError items.""")
@cli_util.help_option_group
def work_request_error_collection_group():
    pass


@click.command(cli_util.override('visual_builder.work_request_summary_collection_group.command_name', 'work-request-summary-collection'), cls=CommandGroupWithAlias, help="""Result of a WorkRequest Summary request. Contains WorkRequestSummary items.""")
@cli_util.help_option_group
def work_request_summary_collection_group():
    pass


@click.command(cli_util.override('visual_builder.vb_instance_group.command_name', 'vb-instance'), cls=CommandGroupWithAlias, help="""Description of Vb Instance.""")
@cli_util.help_option_group
def vb_instance_group():
    pass


@click.command(cli_util.override('visual_builder.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of work request status.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('visual_builder.vb_instance_summary_collection_group.command_name', 'vb-instance-summary-collection'), cls=CommandGroupWithAlias, help="""Result of a VbInstance Summary request. Contains VbInstanceSummary items.""")
@cli_util.help_option_group
def vb_instance_summary_collection_group():
    pass


@click.command(cli_util.override('visual_builder.application_summary_collection_group.command_name', 'application-summary-collection'), cls=CommandGroupWithAlias, help="""Result of listing VbInstance's applications. Contains ApplicationSummary items.""")
@cli_util.help_option_group
def application_summary_collection_group():
    pass


@click.command(cli_util.override('visual_builder.work_request_log_entry_collection_group.command_name', 'work-request-log-entry-collection'), cls=CommandGroupWithAlias, help="""Result of a WorkRequest Log request. Contains list of WorkRequestLog items.""")
@cli_util.help_option_group
def work_request_log_entry_collection_group():
    pass


visual_builder_root_group.add_command(work_request_error_collection_group)
visual_builder_root_group.add_command(work_request_summary_collection_group)
visual_builder_root_group.add_command(vb_instance_group)
visual_builder_root_group.add_command(work_request_group)
visual_builder_root_group.add_command(vb_instance_summary_collection_group)
visual_builder_root_group.add_command(application_summary_collection_group)
visual_builder_root_group.add_command(work_request_log_entry_collection_group)


@vb_instance_group.command(name=cli_util.override('visual_builder.change_vb_instance_compartment.command_name', 'change-compartment'), help=u"""Change the compartment for an vb instance \n[Command Reference](changeVbInstanceCompartment)""")
@cli_util.option('--vb-instance-id', required=True, help=u"""Unique Vb Instance identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_vb_instance_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vb_instance_id, compartment_id, if_match):

    if isinstance(vb_instance_id, six.string_types) and len(vb_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --vb-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('visual_builder', 'vb_instance', ctx)
    result = client.change_vb_instance_compartment(
        vb_instance_id=vb_instance_id,
        change_vb_instance_compartment_details=_details,
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


@vb_instance_group.command(name=cli_util.override('visual_builder.create_vb_instance.command_name', 'create'), help=u"""Creates a new Vb Instance. \n[Command Reference](createVbInstance)""")
@cli_util.option('--display-name', required=True, help=u"""Vb Instance Identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier.""")
@cli_util.option('--node-count', required=True, type=click.INT, help=u"""The number of Nodes""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--idcs-open-id', help=u"""Encrypted IDCS Open ID token. This is required for pre-UCPIS cloud accounts, but not UCPIS, hence not a required parameter""")
@cli_util.option('--is-visual-builder-enabled', type=click.BOOL, help=u"""Visual Builder is enabled or not.""")
@cli_util.option('--custom-endpoint', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--alternate-custom-endpoints', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of alternate custom endpoints to be used for the vb instance URL (contact Oracle for alternateCustomEndpoints availability for a specific instance).

This option is a JSON list with items of type CreateCustomEndpointDetails.  For documentation on CreateCustomEndpointDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/vbinstance/20210601/datatypes/CreateCustomEndpointDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--consumption-model', type=custom_types.CliCaseInsensitiveChoice(["UCM", "GOV", "VB4SAAS"]), help=u"""Optional parameter specifying which entitlement to use for billing purposes. Only required if the account possesses more than one entitlement.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'visual_builder', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'visual_builder', 'class': 'dict(str, dict(str, object))'}, 'custom-endpoint': {'module': 'visual_builder', 'class': 'CreateCustomEndpointDetails'}, 'alternate-custom-endpoints': {'module': 'visual_builder', 'class': 'list[CreateCustomEndpointDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'visual_builder', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'visual_builder', 'class': 'dict(str, dict(str, object))'}, 'custom-endpoint': {'module': 'visual_builder', 'class': 'CreateCustomEndpointDetails'}, 'alternate-custom-endpoints': {'module': 'visual_builder', 'class': 'list[CreateCustomEndpointDetails]'}})
@cli_util.wrap_exceptions
def create_vb_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, node_count, freeform_tags, defined_tags, idcs_open_id, is_visual_builder_enabled, custom_endpoint, alternate_custom_endpoints, consumption_model):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['nodeCount'] = node_count

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if idcs_open_id is not None:
        _details['idcsOpenId'] = idcs_open_id

    if is_visual_builder_enabled is not None:
        _details['isVisualBuilderEnabled'] = is_visual_builder_enabled

    if custom_endpoint is not None:
        _details['customEndpoint'] = cli_util.parse_json_parameter("custom_endpoint", custom_endpoint)

    if alternate_custom_endpoints is not None:
        _details['alternateCustomEndpoints'] = cli_util.parse_json_parameter("alternate_custom_endpoints", alternate_custom_endpoints)

    if consumption_model is not None:
        _details['consumptionModel'] = consumption_model

    client = cli_util.build_client('visual_builder', 'vb_instance', ctx)
    result = client.create_vb_instance(
        create_vb_instance_details=_details,
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


@vb_instance_group.command(name=cli_util.override('visual_builder.delete_vb_instance.command_name', 'delete'), help=u"""Deletes an Vb Instance resource by identifier. \n[Command Reference](deleteVbInstance)""")
@cli_util.option('--vb-instance-id', required=True, help=u"""Unique Vb Instance identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_vb_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vb_instance_id, if_match):

    if isinstance(vb_instance_id, six.string_types) and len(vb_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --vb-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('visual_builder', 'vb_instance', ctx)
    result = client.delete_vb_instance(
        vb_instance_id=vb_instance_id,
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


@vb_instance_group.command(name=cli_util.override('visual_builder.get_vb_instance.command_name', 'get'), help=u"""Gets a VbInstance by identifier \n[Command Reference](getVbInstance)""")
@cli_util.option('--vb-instance-id', required=True, help=u"""Unique Vb Instance identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'visual_builder', 'class': 'VbInstance'})
@cli_util.wrap_exceptions
def get_vb_instance(ctx, from_json, vb_instance_id):

    if isinstance(vb_instance_id, six.string_types) and len(vb_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --vb-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('visual_builder', 'vb_instance', ctx)
    result = client.get_vb_instance(
        vb_instance_id=vb_instance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('visual_builder.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'visual_builder', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('visual_builder', 'vb_instance', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vb_instance_summary_collection_group.command(name=cli_util.override('visual_builder.list_vb_instances.command_name', 'list-vb-instances'), help=u"""Returns a list of Vb Instances. \n[Command Reference](listVbInstances)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""Life cycle state to query on.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'visual_builder', 'class': 'VbInstanceSummaryCollection'})
@cli_util.wrap_exceptions
def list_vb_instances(ctx, from_json, all_pages, page_size, compartment_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('visual_builder', 'vb_instance', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_vb_instances,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_vb_instances,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_vb_instances(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_collection_group.command(name=cli_util.override('visual_builder.list_work_request_errors.command_name', 'list-work-request-errors'), help=u"""Get the errors of a work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'visual_builder', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('visual_builder', 'vb_instance', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            compartment_id=compartment_id,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            compartment_id=compartment_id,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            compartment_id=compartment_id,
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_collection_group.command(name=cli_util.override('visual_builder.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Get the logs of a work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'visual_builder', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('visual_builder', 'vb_instance', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            compartment_id=compartment_id,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            compartment_id=compartment_id,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            compartment_id=compartment_id,
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_summary_collection_group.command(name=cli_util.override('visual_builder.list_work_requests.command_name', 'list-work-requests'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--vb-instance-id', help=u"""The Vb Instance identifier to use to filter results""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'visual_builder', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, page, limit, vb_instance_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if vb_instance_id is not None:
        kwargs['vb_instance_id'] = vb_instance_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('visual_builder', 'vb_instance', ctx)
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


@application_summary_collection_group.command(name=cli_util.override('visual_builder.request_summarized_applications.command_name', 'request-summarized-applications'), help=u"""Summarizes the applications for a vb instance. \n[Command Reference](requestSummarizedApplications)""")
@cli_util.option('--vb-instance-id', required=True, help=u"""Unique Vb Instance identifier.""")
@cli_util.option('--idcs-open-id', help=u"""Encrypted IDCS Open ID token. This is required for pre-UCPIS cloud accounts, but not UCPIS, hence not a required parameter""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'visual_builder', 'class': 'ApplicationSummaryCollection'})
@cli_util.wrap_exceptions
def request_summarized_applications(ctx, from_json, vb_instance_id, idcs_open_id, if_match):

    if isinstance(vb_instance_id, six.string_types) and len(vb_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --vb-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if idcs_open_id is not None:
        _details['idcsOpenId'] = idcs_open_id

    client = cli_util.build_client('visual_builder', 'vb_instance', ctx)
    result = client.request_summarized_applications(
        vb_instance_id=vb_instance_id,
        request_summarized_applications_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vb_instance_group.command(name=cli_util.override('visual_builder.start_vb_instance.command_name', 'start'), help=u"""Start an vb instance that was previously in an INACTIVE state. If the previous state is not INACTIVE, then the state of the vbInstance will not be changed and a 409 response returned. \n[Command Reference](startVbInstance)""")
@cli_util.option('--vb-instance-id', required=True, help=u"""Unique Vb Instance identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def start_vb_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vb_instance_id, if_match):

    if isinstance(vb_instance_id, six.string_types) and len(vb_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --vb-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('visual_builder', 'vb_instance', ctx)
    result = client.start_vb_instance(
        vb_instance_id=vb_instance_id,
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


@vb_instance_group.command(name=cli_util.override('visual_builder.stop_vb_instance.command_name', 'stop'), help=u"""Stop an vb instance that was previously in an ACTIVE state. If the previous state is not ACTIVE, then the state of the vbInstance will not be changed and a 409 response returned. \n[Command Reference](stopVbInstance)""")
@cli_util.option('--vb-instance-id', required=True, help=u"""Unique Vb Instance identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def stop_vb_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vb_instance_id, if_match):

    if isinstance(vb_instance_id, six.string_types) and len(vb_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --vb-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('visual_builder', 'vb_instance', ctx)
    result = client.stop_vb_instance(
        vb_instance_id=vb_instance_id,
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


@vb_instance_group.command(name=cli_util.override('visual_builder.update_vb_instance.command_name', 'update'), help=u"""Updates the Vb Instance. \n[Command Reference](updateVbInstance)""")
@cli_util.option('--vb-instance-id', required=True, help=u"""Unique Vb Instance identifier.""")
@cli_util.option('--display-name', help=u"""Vb Instance Identifier.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--idcs-open-id', help=u"""Encrypted IDCS Open ID token. This is required for pre-UCPIS cloud accounts, but not UCPIS, hence not a required parameter""")
@cli_util.option('--node-count', type=click.INT, help=u"""The number of Nodes""")
@cli_util.option('--is-visual-builder-enabled', type=click.BOOL, help=u"""Enable Visual Builder. If Visual Builder is enabled alredy, then it cannot be disabled.""")
@cli_util.option('--custom-endpoint', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--alternate-custom-endpoints', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of alternate custom endpoints to be used for the vb instance URL (contact Oracle for alternateCustomEndpoints availability for a specific instance).

This option is a JSON list with items of type UpdateCustomEndpointDetails.  For documentation on UpdateCustomEndpointDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/vbinstance/20210601/datatypes/UpdateCustomEndpointDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'visual_builder', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'visual_builder', 'class': 'dict(str, dict(str, object))'}, 'custom-endpoint': {'module': 'visual_builder', 'class': 'UpdateCustomEndpointDetails'}, 'alternate-custom-endpoints': {'module': 'visual_builder', 'class': 'list[UpdateCustomEndpointDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'visual_builder', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'visual_builder', 'class': 'dict(str, dict(str, object))'}, 'custom-endpoint': {'module': 'visual_builder', 'class': 'UpdateCustomEndpointDetails'}, 'alternate-custom-endpoints': {'module': 'visual_builder', 'class': 'list[UpdateCustomEndpointDetails]'}})
@cli_util.wrap_exceptions
def update_vb_instance(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, vb_instance_id, display_name, freeform_tags, defined_tags, idcs_open_id, node_count, is_visual_builder_enabled, custom_endpoint, alternate_custom_endpoints, if_match):

    if isinstance(vb_instance_id, six.string_types) and len(vb_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --vb-instance-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or custom_endpoint or alternate_custom_endpoints:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and custom-endpoint and alternate-custom-endpoints will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if idcs_open_id is not None:
        _details['idcsOpenId'] = idcs_open_id

    if node_count is not None:
        _details['nodeCount'] = node_count

    if is_visual_builder_enabled is not None:
        _details['isVisualBuilderEnabled'] = is_visual_builder_enabled

    if custom_endpoint is not None:
        _details['customEndpoint'] = cli_util.parse_json_parameter("custom_endpoint", custom_endpoint)

    if alternate_custom_endpoints is not None:
        _details['alternateCustomEndpoints'] = cli_util.parse_json_parameter("alternate_custom_endpoints", alternate_custom_endpoints)

    client = cli_util.build_client('visual_builder', 'vb_instance', ctx)
    result = client.update_vb_instance(
        vb_instance_id=vb_instance_id,
        update_vb_instance_details=_details,
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
