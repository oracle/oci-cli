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
from services.dashboard_service.src.oci_cli_dashboard_service.generated import dashboard_service_service_cli


@click.command(cli_util.override('dashboard.dashboard_root_group.command_name', 'dashboard'), cls=CommandGroupWithAlias, help=cli_util.override('dashboard.dashboard_root_group.help', """Use the Oracle Cloud Infrastructure Dashboards service API to manage dashboards in the Console.
Dashboards provide an organized and customizable view of resources and their metrics in the Console.
For more information, see [Dashboards].

**Important:** Resources for the Dashboards service are created in the tenacy's home region.
Although it is possible to create dashboard and dashboard group resources in regions other than the home region,
you won't be able to view those resources in the Console.
Therefore, creating resources outside of the home region is not recommended."""), short_help=cli_util.override('dashboard.dashboard_root_group.short_help', """Dashboards API"""))
@cli_util.help_option_group
def dashboard_root_group():
    pass


@click.command(cli_util.override('dashboard.dashboard_group.command_name', 'dashboard'), cls=CommandGroupWithAlias, help="""The base schema for a dashboard. Derived schemas have configurations and widgets specific to the  `schemaVersion`.""")
@cli_util.help_option_group
def dashboard_group():
    pass


@click.command(cli_util.override('dashboard.dashboard_collection_group.command_name', 'dashboard-collection'), cls=CommandGroupWithAlias, help="""Results of a dashboard search. Contains `DashboardSummary` items.""")
@cli_util.help_option_group
def dashboard_collection_group():
    pass


dashboard_service_service_cli.dashboard_service_service_group.add_command(dashboard_root_group)
dashboard_root_group.add_command(dashboard_group)
dashboard_root_group.add_command(dashboard_collection_group)


@dashboard_group.command(name=cli_util.override('dashboard.create_dashboard.command_name', 'create'), help=u"""Creates a new dashboard in the dashboard group's compartment using the details provided in request body.

**Caution:** Resources for the Dashboard service are created in the tenacy's home region. Although it is possible to create dashboard resource in regions other than the home region, you won't be able to view those resources in the Console. Therefore, creating resources outside of the home region is not recommended. \n[Command Reference](createDashboard)""")
@cli_util.option('--dashboard-group-id', required=True, help=u"""The [OCID] of the dashboard group that the dashbaord is associated with.""")
@cli_util.option('--schema-version', required=True, help=u"""The schema describing how to interpret the dashboard configuration and widgets.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information. Leading and trailing spaces and the following special characters are not allowed: <>()=/'\"&\\""")
@cli_util.option('--description', help=u"""A short description of the dashboard. It can be changed. Avoid entering confidential information. The following special characters are not allowed: <>()=/'\"&\\""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--opc-cross-region', help=u"""To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dashboard_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dashboard_service', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dashboard_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dashboard_service', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dashboard_service', 'class': 'Dashboard'})
@cli_util.wrap_exceptions
def create_dashboard(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dashboard_group_id, schema_version, display_name, description, freeform_tags, defined_tags, opc_cross_region):

    kwargs = {}
    if opc_cross_region is not None:
        kwargs['opc_cross_region'] = opc_cross_region
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dashboardGroupId'] = dashboard_group_id
    _details['schemaVersion'] = schema_version

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('dashboard_service', 'dashboard', ctx)
    result = client.create_dashboard(
        create_dashboard_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dashboard') and callable(getattr(client, 'get_dashboard')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_dashboard(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@dashboard_group.command(name=cli_util.override('dashboard.create_dashboard_create_v1_dashboard_details.command_name', 'create-dashboard-create-v1-dashboard-details'), help=u"""Creates a new dashboard in the dashboard group's compartment using the details provided in request body.

**Caution:** Resources for the Dashboard service are created in the tenacy's home region. Although it is possible to create dashboard resource in regions other than the home region, you won't be able to view those resources in the Console. Therefore, creating resources outside of the home region is not recommended. \n[Command Reference](createDashboard)""")
@cli_util.option('--dashboard-group-id', required=True, help=u"""The [OCID] of the dashboard group that the dashbaord is associated with.""")
@cli_util.option('--widgets', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The basic visualization building blocks of a dashboard.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information. Leading and trailing spaces and the following special characters are not allowed: <>()=/'\"&\\""")
@cli_util.option('--description', help=u"""A short description of the dashboard. It can be changed. Avoid entering confidential information. The following special characters are not allowed: <>()=/'\"&\\""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The layout and widget placement for the dashboard.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--opc-cross-region', help=u"""To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dashboard_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dashboard_service', 'class': 'dict(str, dict(str, object))'}, 'config': {'module': 'dashboard_service', 'class': 'object'}, 'widgets': {'module': 'dashboard_service', 'class': 'list[object]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dashboard_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dashboard_service', 'class': 'dict(str, dict(str, object))'}, 'config': {'module': 'dashboard_service', 'class': 'object'}, 'widgets': {'module': 'dashboard_service', 'class': 'list[object]'}}, output_type={'module': 'dashboard_service', 'class': 'Dashboard'})
@cli_util.wrap_exceptions
def create_dashboard_create_v1_dashboard_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dashboard_group_id, widgets, display_name, description, freeform_tags, defined_tags, config, opc_cross_region):

    kwargs = {}
    if opc_cross_region is not None:
        kwargs['opc_cross_region'] = opc_cross_region
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dashboardGroupId'] = dashboard_group_id
    _details['widgets'] = cli_util.parse_json_parameter("widgets", widgets)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config is not None:
        _details['config'] = cli_util.parse_json_parameter("config", config)

    _details['schemaVersion'] = 'V1'

    client = cli_util.build_client('dashboard_service', 'dashboard', ctx)
    result = client.create_dashboard(
        create_dashboard_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dashboard') and callable(getattr(client, 'get_dashboard')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_dashboard(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@dashboard_group.command(name=cli_util.override('dashboard.delete_dashboard.command_name', 'delete'), help=u"""Deletes the specified dashboard. Uses the dashboard's OCID to determine which dashboard to delete. \n[Command Reference](deleteDashboard)""")
@cli_util.option('--dashboard-id', required=True, help=u"""The [OCID] of the dashboard.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--opc-cross-region', help=u"""To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_dashboard(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dashboard_id, if_match, opc_cross_region):

    if isinstance(dashboard_id, six.string_types) and len(dashboard_id.strip()) == 0:
        raise click.UsageError('Parameter --dashboard-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if opc_cross_region is not None:
        kwargs['opc_cross_region'] = opc_cross_region
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dashboard_service', 'dashboard', ctx)
    result = client.delete_dashboard(
        dashboard_id=dashboard_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dashboard') and callable(getattr(client, 'get_dashboard')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_dashboard(dashboard_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@dashboard_group.command(name=cli_util.override('dashboard.get_dashboard.command_name', 'get'), help=u"""Gets the specified dashboard's information. Uses the dashboard's OCID to determine which dashboard to retrieve. \n[Command Reference](getDashboard)""")
@cli_util.option('--dashboard-id', required=True, help=u"""The [OCID] of the dashboard.""")
@cli_util.option('--opc-cross-region', help=u"""To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dashboard_service', 'class': 'Dashboard'})
@cli_util.wrap_exceptions
def get_dashboard(ctx, from_json, dashboard_id, opc_cross_region):

    if isinstance(dashboard_id, six.string_types) and len(dashboard_id.strip()) == 0:
        raise click.UsageError('Parameter --dashboard-id cannot be whitespace or empty string')

    kwargs = {}
    if opc_cross_region is not None:
        kwargs['opc_cross_region'] = opc_cross_region
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dashboard_service', 'dashboard', ctx)
    result = client.get_dashboard(
        dashboard_id=dashboard_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dashboard_collection_group.command(name=cli_util.override('dashboard.list_dashboards.command_name', 'list-dashboards'), help=u"""Returns a list of dashboards with a specific dashboard group ID. \n[Command Reference](listDashboards)""")
@cli_util.option('--dashboard-group-id', required=True, help=u"""The [OCID] of the dashboard group that the dashboard belongs to.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter that returns dashboard resources that match the lifecycle state specified.""")
@cli_util.option('--display-name', help=u"""A case-sensitive filter that returns resources that match the entire display name specified.""")
@cli_util.option('--id', help=u"""The [OCID] of the dashboard.""")
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dashboard_service', 'class': 'DashboardCollection'})
@cli_util.wrap_exceptions
def list_dashboards(ctx, from_json, all_pages, page_size, dashboard_group_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by, opc_cross_region):

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
    client = cli_util.build_client('dashboard_service', 'dashboard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_dashboards,
            dashboard_group_id=dashboard_group_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_dashboards,
            limit,
            page_size,
            dashboard_group_id=dashboard_group_id,
            **kwargs
        )
    else:
        result = client.list_dashboards(
            dashboard_group_id=dashboard_group_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@dashboard_group.command(name=cli_util.override('dashboard.update_dashboard.command_name', 'update'), help=u"""Updates the specified dashboard. Uses the dashboard's OCID to determine which dashboard to update. \n[Command Reference](updateDashboard)""")
@cli_util.option('--dashboard-id', required=True, help=u"""The [OCID] of the dashboard.""")
@cli_util.option('--schema-version', required=True, help=u"""The schema describing how to interpret the dashboard configuration and widgets.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information. Leading and trailing spaces and the following special characters are not allowed: <>()=/'\"&\\""")
@cli_util.option('--description', help=u"""A short description of the dashboard. It can be changed. Avoid entering confidential information. The following special characters are not allowed: <>()=/'\"&\\""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--opc-cross-region', help=u"""To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dashboard_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dashboard_service', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dashboard_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dashboard_service', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dashboard_service', 'class': 'Dashboard'})
@cli_util.wrap_exceptions
def update_dashboard(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, dashboard_id, schema_version, display_name, description, freeform_tags, defined_tags, if_match, opc_cross_region):

    if isinstance(dashboard_id, six.string_types) and len(dashboard_id.strip()) == 0:
        raise click.UsageError('Parameter --dashboard-id cannot be whitespace or empty string')
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
    _details['schemaVersion'] = schema_version

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('dashboard_service', 'dashboard', ctx)
    result = client.update_dashboard(
        dashboard_id=dashboard_id,
        update_dashboard_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dashboard') and callable(getattr(client, 'get_dashboard')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_dashboard(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@dashboard_group.command(name=cli_util.override('dashboard.update_dashboard_update_v1_dashboard_details.command_name', 'update-dashboard-update-v1-dashboard-details'), help=u"""Updates the specified dashboard. Uses the dashboard's OCID to determine which dashboard to update. \n[Command Reference](updateDashboard)""")
@cli_util.option('--dashboard-id', required=True, help=u"""The [OCID] of the dashboard.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information. Leading and trailing spaces and the following special characters are not allowed: <>()=/'\"&\\""")
@cli_util.option('--description', help=u"""A short description of the dashboard. It can be changed. Avoid entering confidential information. The following special characters are not allowed: <>()=/'\"&\\""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The layout and widget placement for the dashboard.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--widgets', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The basic visualization building blocks of a dashboard.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--opc-cross-region', help=u"""To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dashboard_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dashboard_service', 'class': 'dict(str, dict(str, object))'}, 'config': {'module': 'dashboard_service', 'class': 'object'}, 'widgets': {'module': 'dashboard_service', 'class': 'list[object]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dashboard_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dashboard_service', 'class': 'dict(str, dict(str, object))'}, 'config': {'module': 'dashboard_service', 'class': 'object'}, 'widgets': {'module': 'dashboard_service', 'class': 'list[object]'}}, output_type={'module': 'dashboard_service', 'class': 'Dashboard'})
@cli_util.wrap_exceptions
def update_dashboard_update_v1_dashboard_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, dashboard_id, display_name, description, freeform_tags, defined_tags, config, widgets, if_match, opc_cross_region):

    if isinstance(dashboard_id, six.string_types) and len(dashboard_id.strip()) == 0:
        raise click.UsageError('Parameter --dashboard-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or config or widgets:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and config and widgets will replace any existing values. Are you sure you want to continue?"):
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

    if config is not None:
        _details['config'] = cli_util.parse_json_parameter("config", config)

    if widgets is not None:
        _details['widgets'] = cli_util.parse_json_parameter("widgets", widgets)

    _details['schemaVersion'] = 'V1'

    client = cli_util.build_client('dashboard_service', 'dashboard', ctx)
    result = client.update_dashboard(
        dashboard_id=dashboard_id,
        update_dashboard_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dashboard') and callable(getattr(client, 'get_dashboard')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_dashboard(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
