# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

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
from services.os_management_hub.src.oci_cli_os_management_hub.generated import os_management_hub_service_cli


@click.command(cli_util.override('event.event_root_group.command_name', 'event'), cls=CommandGroupWithAlias, help=cli_util.override('event.event_root_group.help', """Use the OS Management Hub API to manage and monitor updates and patches for instances in OCI, your private data center, or 3rd-party clouds.
For more information, see [Overview of OS Management Hub]."""), short_help=cli_util.override('event.event_root_group.short_help', """OS Management Hub API"""))
@cli_util.help_option_group
def event_root_group():
    pass


@click.command(cli_util.override('event.event_collection_group.command_name', 'event-collection'), cls=CommandGroupWithAlias, help="""A set of events returned for the [ListEvents] operation. The list contains a summary of each event and other information, such as metadata.""")
@cli_util.help_option_group
def event_collection_group():
    pass


@click.command(cli_util.override('event.event_group.command_name', 'event'), cls=CommandGroupWithAlias, help="""An event is an occurrence of something of interest on a managed instance, such as a kernel crash, software package update, or software source update.""")
@cli_util.help_option_group
def event_group():
    pass


os_management_hub_service_cli.os_management_hub_service_group.add_command(event_root_group)
event_root_group.add_command(event_collection_group)
event_root_group.add_command(event_group)


@event_group.command(name=cli_util.override('event.change_event_compartment.command_name', 'change-compartment'), help=u"""Moves an event into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeEventCompartment)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the event to.""")
@cli_util.option('--event-id', required=True, help=u"""The [OCID] of the event.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_event_compartment(ctx, from_json, compartment_id, event_id, if_match):

    if isinstance(event_id, six.string_types) and len(event_id.strip()) == 0:
        raise click.UsageError('Parameter --event-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('os_management_hub', 'event', ctx)
    result = client.change_event_compartment(
        event_id=event_id,
        change_event_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@event_group.command(name=cli_util.override('event.delete_event.command_name', 'delete'), help=u"""Deletes the specified event. \n[Command Reference](deleteEvent)""")
@cli_util.option('--event-id', required=True, help=u"""The [OCID] of the event.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["WAITING", "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_event(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, event_id, if_match):

    if isinstance(event_id, six.string_types) and len(event_id.strip()) == 0:
        raise click.UsageError('Parameter --event-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management_hub', 'event', ctx)
    result = client.delete_event(
        event_id=event_id,
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
                if 'opc-work-request-id' not in result.headers:
                    click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state')
                    cli_util.render_response(result, ctx)
                    return

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


@event_group.command(name=cli_util.override('event.delete_event_content.command_name', 'delete-event-content'), help=u"""Deletes an event content ZIP archive from the service. \n[Command Reference](deleteEventContent)""")
@cli_util.option('--event-id', required=True, help=u"""The [OCID] of the event.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_event_content(ctx, from_json, event_id, if_match):

    if isinstance(event_id, six.string_types) and len(event_id.strip()) == 0:
        raise click.UsageError('Parameter --event-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management_hub', 'event', ctx)
    result = client.delete_event_content(
        event_id=event_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@event_group.command(name=cli_util.override('event.get_event.command_name', 'get'), help=u"""Returns information about the specified event. \n[Command Reference](getEvent)""")
@cli_util.option('--event-id', required=True, help=u"""The [OCID] of the event.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management_hub', 'class': 'Event'})
@cli_util.wrap_exceptions
def get_event(ctx, from_json, event_id):

    if isinstance(event_id, six.string_types) and len(event_id.strip()) == 0:
        raise click.UsageError('Parameter --event-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management_hub', 'event', ctx)
    result = client.get_event(
        event_id=event_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@event_group.command(name=cli_util.override('event.get_event_content.command_name', 'get-event-content'), help=u"""Returns a ZIP archive with additional information about an event. The archive content depends on the event type. \n[Command Reference](getEventContent)""")
@cli_util.option('--event-id', required=True, help=u"""The [OCID] of the event.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_event_content(ctx, from_json, file, event_id):

    if isinstance(event_id, six.string_types) and len(event_id.strip()) == 0:
        raise click.UsageError('Parameter --event-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management_hub', 'event', ctx)
    result = client.get_event_content(
        event_id=event_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@event_group.command(name=cli_util.override('event.import_event_content.command_name', 'import-event-content'), help=u"""Uploads an event content ZIP archive from an instance to the service. \n[Command Reference](importEventContent)""")
@cli_util.option('--event-id', required=True, help=u"""The [OCID] of the event.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["WAITING", "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def import_event_content(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, event_id, if_match):

    if isinstance(event_id, six.string_types) and len(event_id.strip()) == 0:
        raise click.UsageError('Parameter --event-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management_hub', 'event', ctx)
    result = client.import_event_content(
        event_id=event_id,
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
                if 'opc-work-request-id' not in result.headers:
                    click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state')
                    cli_util.render_response(result, ctx)
                    return

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


@event_collection_group.command(name=cli_util.override('event.list_events.command_name', 'list-events'), help=u"""Lists events that match the specified criteria, such as compartment, state, and event type. \n[Command Reference](listEvents)""")
@cli_util.option('--event-summary', help=u"""A filter to return only events whose summary matches the given value.""")
@cli_util.option('--event-summary-contains', help=u"""A filter to return only events with a summary that contains the value provided.""")
@cli_util.option('--id', help=u"""The [OCID] of the event.""")
@cli_util.option('--event-fingerprint', help=u"""The eventFingerprint of the KernelEventData.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only events that match the state provided. The state value is case-insensitive.""")
@cli_util.option('--resource-id', help=u"""The [OCID] of the resource. This filter returns resources associated with the specified resource.""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["KERNEL_OOPS", "KERNEL_CRASH", "EXPLOIT_ATTEMPT", "SOFTWARE_UPDATE", "KSPLICE_UPDATE", "SOFTWARE_SOURCE", "AGENT", "MANAGEMENT_STATION", "SYSADMIN", "REBOOT"]), multiple=True, help=u"""A filter to return only resources whose type matches the given value.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `3`""")
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that returns events that occurred on or before the date provided. Example: `2016-08-25T21:10:29.600Z`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that returns events that occurred on or after the date provided. Example: `2016-08-25T21:10:29.600Z`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeOccurredAt", "timeUpdated", "eventSummary"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated, timeOccurredAt and timeUpdated is descending. Default order for eventSummary is ascending.""")
@cli_util.option('--is-managed-by-autonomous-linux', type=click.BOOL, help=u"""Indicates whether to list only resources managed by the Autonomous Linux service.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management_hub', 'class': 'EventCollection'})
@cli_util.wrap_exceptions
def list_events(ctx, from_json, all_pages, page_size, event_summary, event_summary_contains, id, event_fingerprint, compartment_id, lifecycle_state, resource_id, type, limit, page, time_created_less_than, time_created_greater_than_or_equal_to, sort_order, sort_by, is_managed_by_autonomous_linux):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if event_summary is not None:
        kwargs['event_summary'] = event_summary
    if event_summary_contains is not None:
        kwargs['event_summary_contains'] = event_summary_contains
    if id is not None:
        kwargs['id'] = id
    if event_fingerprint is not None:
        kwargs['event_fingerprint'] = event_fingerprint
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if type is not None and len(type) > 0:
        kwargs['type'] = type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if time_created_less_than is not None:
        kwargs['time_created_less_than'] = time_created_less_than
    if time_created_greater_than_or_equal_to is not None:
        kwargs['time_created_greater_than_or_equal_to'] = time_created_greater_than_or_equal_to
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if is_managed_by_autonomous_linux is not None:
        kwargs['is_managed_by_autonomous_linux'] = is_managed_by_autonomous_linux
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management_hub', 'event', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_events,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_events,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_events(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@event_group.command(name=cli_util.override('event.update_event.command_name', 'update'), help=u"""Updates the tags for an event. \n[Command Reference](updateEvent)""")
@cli_util.option('--event-id', required=True, help=u"""The [OCID] of the event.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'os_management_hub', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management_hub', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'os_management_hub', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management_hub', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'os_management_hub', 'class': 'Event'})
@cli_util.wrap_exceptions
def update_event(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, event_id, freeform_tags, defined_tags, if_match):

    if isinstance(event_id, six.string_types) and len(event_id.strip()) == 0:
        raise click.UsageError('Parameter --event-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('os_management_hub', 'event', ctx)
    result = client.update_event(
        event_id=event_id,
        update_event_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_event') and callable(getattr(client, 'get_event')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_event(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
