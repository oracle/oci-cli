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
from services.dashboard_service.src.oci_cli_dashboard_service.generated import dashboard_service_service_cli


@click.command(cli_util.override('dashboard_group.dashboard_group_root_group.command_name', 'dashboard-group'), cls=CommandGroupWithAlias, help=cli_util.override('dashboard_group.dashboard_group_root_group.help', """Use the Oracle Cloud Infrastructure Dashboards service API to manage dashboards in the Console.
Dashboards provide an organized and customizable view of resources and their metrics in the Console.
For more information, see [Dashboards].

**Important:** Resources for the Dashboards service are created in the tenacy's home region.
Although it is possible to create dashboard and dashboard group resources in regions other than the home region,
you won't be able to view those resources in the Console.
Therefore, creating resources outside of the home region is not recommended."""), short_help=cli_util.override('dashboard_group.dashboard_group_root_group.short_help', """Dashboards API"""))
@cli_util.help_option_group
def dashboard_group_root_group():
    pass


@click.command(cli_util.override('dashboard_group.dashboard_group_collection_group.command_name', 'dashboard-group-collection'), cls=CommandGroupWithAlias, help="""A list of dashboard groups that match filter criteria, if any. Results contain `DashboardGroupSummary` objects.""")
@cli_util.help_option_group
def dashboard_group_collection_group():
    pass


@click.command(cli_util.override('dashboard_group.dashboard_group_group.command_name', 'dashboard-group'), cls=CommandGroupWithAlias, help="""The base schema for a dashboard group.""")
@cli_util.help_option_group
def dashboard_group_group():
    pass


dashboard_service_service_cli.dashboard_service_service_group.add_command(dashboard_group_root_group)
dashboard_group_root_group.add_command(dashboard_group_collection_group)
dashboard_group_root_group.add_command(dashboard_group_group)


@dashboard_group_group.command(name=cli_util.override('dashboard_group.change_dashboard_group_compartment.command_name', 'change-compartment'), help=u"""Moves a DashboardGroup resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeDashboardGroupCompartment)""")
@cli_util.option('--dashboard-group-id', required=True, help=u"""The [OCID] of the dashboard group.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_dashboard_group_compartment(ctx, from_json, dashboard_group_id, compartment_id, if_match):

    if isinstance(dashboard_group_id, six.string_types) and len(dashboard_group_id.strip()) == 0:
        raise click.UsageError('Parameter --dashboard-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('dashboard_service', 'dashboard_group', ctx)
    result = client.change_dashboard_group_compartment(
        dashboard_group_id=dashboard_group_id,
        change_dashboard_group_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dashboard_group_group.command(name=cli_util.override('dashboard_group.create_dashboard_group.command_name', 'create'), help=u"""Creates a new dashboard group using the details provided in request body.

**Caution:** Resources for the Dashboard service are created in the tenacy's home region. Although it is possible to create dashboard group resource in regions other than the home region, you won't be able to view those resources in the Console. Therefore, creating resources outside of the home region is not recommended. \n[Command Reference](createDashboardGroup)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the dashboard group.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information. Leading and trailing spaces and the following special characters are not allowed: <>()=/'\"&\\""")
@cli_util.option('--description', help=u"""A short description of the dashboard group. It can be changed. Avoid entering confidential information. The following special characters are not allowed: <>()=/'\"&\\""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--opc-cross-region', help=u"""To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dashboard_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dashboard_service', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dashboard_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dashboard_service', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dashboard_service', 'class': 'DashboardGroup'})
@cli_util.wrap_exceptions
def create_dashboard_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, description, freeform_tags, defined_tags, opc_cross_region):

    kwargs = {}
    if opc_cross_region is not None:
        kwargs['opc_cross_region'] = opc_cross_region
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

    client = cli_util.build_client('dashboard_service', 'dashboard_group', ctx)
    result = client.create_dashboard_group(
        create_dashboard_group_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dashboard_group') and callable(getattr(client, 'get_dashboard_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_dashboard_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@dashboard_group_group.command(name=cli_util.override('dashboard_group.delete_dashboard_group.command_name', 'delete'), help=u"""Deletes the specified dashboard group. Uses the dashboard group's OCID to determine which dashboard group to delete. \n[Command Reference](deleteDashboardGroup)""")
@cli_util.option('--dashboard-group-id', required=True, help=u"""The [OCID] of the dashboard group.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--opc-cross-region', help=u"""To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_dashboard_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dashboard_group_id, if_match, opc_cross_region):

    if isinstance(dashboard_group_id, six.string_types) and len(dashboard_group_id.strip()) == 0:
        raise click.UsageError('Parameter --dashboard-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if opc_cross_region is not None:
        kwargs['opc_cross_region'] = opc_cross_region
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dashboard_service', 'dashboard_group', ctx)
    result = client.delete_dashboard_group(
        dashboard_group_id=dashboard_group_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dashboard_group') and callable(getattr(client, 'get_dashboard_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_dashboard_group(dashboard_group_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@dashboard_group_group.command(name=cli_util.override('dashboard_group.get_dashboard_group.command_name', 'get'), help=u"""Gets the specified dashboard group's information. Uses the dashboard group's OCID to determine which dashboard to retrieve. \n[Command Reference](getDashboardGroup)""")
@cli_util.option('--dashboard-group-id', required=True, help=u"""The [OCID] of the dashboard group.""")
@cli_util.option('--opc-cross-region', help=u"""To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dashboard_service', 'class': 'DashboardGroup'})
@cli_util.wrap_exceptions
def get_dashboard_group(ctx, from_json, dashboard_group_id, opc_cross_region):

    if isinstance(dashboard_group_id, six.string_types) and len(dashboard_group_id.strip()) == 0:
        raise click.UsageError('Parameter --dashboard-group-id cannot be whitespace or empty string')

    kwargs = {}
    if opc_cross_region is not None:
        kwargs['opc_cross_region'] = opc_cross_region
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dashboard_service', 'dashboard_group', ctx)
    result = client.get_dashboard_group(
        dashboard_group_id=dashboard_group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dashboard_group_collection_group.command(name=cli_util.override('dashboard_group.list_dashboard_groups.command_name', 'list-dashboard-groups'), help=u"""Returns a list of dashboard groups with a specific compartment ID. \n[Command Reference](listDashboardGroups)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter that returns dashboard groups that match the lifecycle state specified.""")
@cli_util.option('--display-name', help=u"""A case-sensitive filter that returns resources that match the entire display name specified.""")
@cli_util.option('--id', help=u"""The [OCID] of the dashboard group.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This value is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--opc-cross-region', help=u"""To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dashboard_service', 'class': 'DashboardGroupCollection'})
@cli_util.wrap_exceptions
def list_dashboard_groups(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by, opc_cross_region):

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
    if opc_cross_region is not None:
        kwargs['opc_cross_region'] = opc_cross_region
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dashboard_service', 'dashboard_group', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_dashboard_groups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_dashboard_groups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_dashboard_groups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@dashboard_group_group.command(name=cli_util.override('dashboard_group.update_dashboard_group.command_name', 'update'), help=u"""Updates the specified dashboard group. Uses the dashboard group's OCID to determine which dashboard group to update. \n[Command Reference](updateDashboardGroup)""")
@cli_util.option('--dashboard-group-id', required=True, help=u"""The [OCID] of the dashboard group.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information. Leading and trailing spaces and the following special characters are not allowed: <>()=/'\"&\\""")
@cli_util.option('--description', help=u"""A short description of the dashboard group. It can be changed. Avoid entering confidential information. The following special characters are not allowed: <>()=/'\"&\\""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--opc-cross-region', help=u"""To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dashboard_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dashboard_service', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dashboard_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dashboard_service', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dashboard_service', 'class': 'DashboardGroup'})
@cli_util.wrap_exceptions
def update_dashboard_group(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, dashboard_group_id, display_name, description, freeform_tags, defined_tags, if_match, opc_cross_region):

    if isinstance(dashboard_group_id, six.string_types) and len(dashboard_group_id.strip()) == 0:
        raise click.UsageError('Parameter --dashboard-group-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if opc_cross_region is not None:
        kwargs['opc_cross_region'] = opc_cross_region
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

    client = cli_util.build_client('dashboard_service', 'dashboard_group', ctx)
    result = client.update_dashboard_group(
        dashboard_group_id=dashboard_group_id,
        update_dashboard_group_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dashboard_group') and callable(getattr(client, 'get_dashboard_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_dashboard_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
