# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
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
from services.rover.src.oci_cli_rover.generated import rover_service_cli


@click.command(cli_util.override('rover_entitlement.rover_entitlement_root_group.command_name', 'rover-entitlement'), cls=CommandGroupWithAlias, help=cli_util.override('rover_entitlement.rover_entitlement_root_group.help', """A description of the RoverCloudService API."""), short_help=cli_util.override('rover_entitlement.rover_entitlement_root_group.short_help', """RoverCloudService API"""))
@cli_util.help_option_group
def rover_entitlement_root_group():
    pass


@click.command(cli_util.override('rover_entitlement.rover_entitlement_group.command_name', 'rover-entitlement'), cls=CommandGroupWithAlias, help="""Information about a RoverEntitlement.""")
@cli_util.help_option_group
def rover_entitlement_group():
    pass


rover_service_cli.rover_service_group.add_command(rover_entitlement_root_group)
rover_entitlement_root_group.add_command(rover_entitlement_group)


@rover_entitlement_group.command(name=cli_util.override('rover_entitlement.change_rover_entitlement_compartment.command_name', 'change-compartment'), help=u"""Moves an entitlement into a different compartment. \n[Command Reference](changeRoverEntitlementCompartment)""")
@cli_util.option('--rover-entitlement-id', required=True, help=u"""ID of the rover node or cluster entitlement""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID]  of the compartment into which the resources should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_rover_entitlement_compartment(ctx, from_json, rover_entitlement_id, compartment_id, if_match):

    if isinstance(rover_entitlement_id, six.string_types) and len(rover_entitlement_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-entitlement-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('rover', 'rover_entitlement', ctx)
    result = client.change_rover_entitlement_compartment(
        rover_entitlement_id=rover_entitlement_id,
        change_rover_entitlement_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rover_entitlement_group.command(name=cli_util.override('rover_entitlement.create_rover_entitlement.command_name', 'create'), help=u"""Create the Entitlement to use a Rover Device. It requires some offline process of review and signatures before request is granted. \n[Command Reference](createRoverEntitlement)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment containing the RoverEntitlement.""")
@cli_util.option('--requestor-name', required=True, help=u"""Requestor name for the entitlement.""")
@cli_util.option('--requestor-email', required=True, help=u"""Requestor email for the entitlement.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--entitlement-details', help=u"""Details about the entitlement.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The current state of the RoverNode.""")
@cli_util.option('--lifecycle-state-details', help=u"""A property that can contain details on the lifecycle.""")
@cli_util.option('--tenant-id', help=u"""tenant Id.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{orcl-cloud: {free-tier-retain: true}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'rover', 'class': 'RoverEntitlement'})
@cli_util.wrap_exceptions
def create_rover_entitlement(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, requestor_name, requestor_email, display_name, entitlement_details, lifecycle_state, lifecycle_state_details, tenant_id, freeform_tags, defined_tags, system_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['requestorName'] = requestor_name
    _details['requestorEmail'] = requestor_email

    if display_name is not None:
        _details['displayName'] = display_name

    if entitlement_details is not None:
        _details['entitlementDetails'] = entitlement_details

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if lifecycle_state_details is not None:
        _details['lifecycleStateDetails'] = lifecycle_state_details

    if tenant_id is not None:
        _details['tenantId'] = tenant_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('rover', 'rover_entitlement', ctx)
    result = client.create_rover_entitlement(
        create_rover_entitlement_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_rover_entitlement') and callable(getattr(client, 'get_rover_entitlement')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_rover_entitlement(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@rover_entitlement_group.command(name=cli_util.override('rover_entitlement.delete_rover_entitlement.command_name', 'delete'), help=u"""Deletes a rover entitlement \n[Command Reference](deleteRoverEntitlement)""")
@cli_util.option('--rover-entitlement-id', required=True, help=u"""ID of the rover node or cluster entitlement""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_rover_entitlement(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, rover_entitlement_id, if_match):

    if isinstance(rover_entitlement_id, six.string_types) and len(rover_entitlement_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-entitlement-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'rover_entitlement', ctx)
    result = client.delete_rover_entitlement(
        rover_entitlement_id=rover_entitlement_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_rover_entitlement') and callable(getattr(client, 'get_rover_entitlement')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_rover_entitlement(rover_entitlement_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@rover_entitlement_group.command(name=cli_util.override('rover_entitlement.get_rover_entitlement.command_name', 'get'), help=u"""Describes the Rover Device Entitlement in detail \n[Command Reference](getRoverEntitlement)""")
@cli_util.option('--rover-entitlement-id', required=True, help=u"""ID of the rover node or cluster entitlement""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to list resources.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverEntitlement'})
@cli_util.wrap_exceptions
def get_rover_entitlement(ctx, from_json, rover_entitlement_id, compartment_id):

    if isinstance(rover_entitlement_id, six.string_types) and len(rover_entitlement_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-entitlement-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'rover_entitlement', ctx)
    result = client.get_rover_entitlement(
        rover_entitlement_id=rover_entitlement_id,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rover_entitlement_group.command(name=cli_util.override('rover_entitlement.list_rover_entitlements.command_name', 'list'), help=u"""Returns a list of RoverEntitlements. \n[Command Reference](listRoverEntitlements)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--id', help=u"""filtering by Rover Device Entitlement id""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'RoverEntitlementCollection'})
@cli_util.wrap_exceptions
def list_rover_entitlements(ctx, from_json, all_pages, page_size, compartment_id, id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
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
    client = cli_util.build_client('rover', 'rover_entitlement', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_rover_entitlements,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_rover_entitlements,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_rover_entitlements(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@rover_entitlement_group.command(name=cli_util.override('rover_entitlement.update_rover_entitlement.command_name', 'update'), help=u"""Updates the RoverEntitlement \n[Command Reference](updateRoverEntitlement)""")
@cli_util.option('--rover-entitlement-id', required=True, help=u"""ID of the rover node or cluster entitlement""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--tenant-id', help=u"""tenant Id.""")
@cli_util.option('--requestor-name', help=u"""Requestor name for the entitlement.""")
@cli_util.option('--requestor-email', help=u"""Requestor email for the entitlement.""")
@cli_util.option('--entitlement-details', help=u"""Details about the entitlement.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The current state of the RoverNode.""")
@cli_util.option('--lifecycle-state-details', help=u"""A property that can contain details on the lifecycle.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{orcl-cloud: {free-tier-retain: true}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'rover', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'rover', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'rover', 'class': 'RoverEntitlement'})
@cli_util.wrap_exceptions
def update_rover_entitlement(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, rover_entitlement_id, display_name, tenant_id, requestor_name, requestor_email, entitlement_details, lifecycle_state, lifecycle_state_details, freeform_tags, defined_tags, system_tags, if_match):

    if isinstance(rover_entitlement_id, six.string_types) and len(rover_entitlement_id.strip()) == 0:
        raise click.UsageError('Parameter --rover-entitlement-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or system_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and system-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if tenant_id is not None:
        _details['tenantId'] = tenant_id

    if requestor_name is not None:
        _details['requestorName'] = requestor_name

    if requestor_email is not None:
        _details['requestorEmail'] = requestor_email

    if entitlement_details is not None:
        _details['entitlementDetails'] = entitlement_details

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if lifecycle_state_details is not None:
        _details['lifecycleStateDetails'] = lifecycle_state_details

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('rover', 'rover_entitlement', ctx)
    result = client.update_rover_entitlement(
        rover_entitlement_id=rover_entitlement_id,
        update_rover_entitlement_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_rover_entitlement') and callable(getattr(client, 'get_rover_entitlement')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_rover_entitlement(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
