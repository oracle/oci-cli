# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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
from services.tenant_manager_control_plane.src.oci_cli_tenant_manager_control_plane.generated import organizations_service_cli


@click.command(cli_util.override('link.link_root_group.command_name', 'link'), cls=CommandGroupWithAlias, help=cli_util.override('link.link_root_group.help', """A description of the TenantManager API"""), short_help=cli_util.override('link.link_root_group.short_help', """TenantManager API"""))
@cli_util.help_option_group
def link_root_group():
    pass


@click.command(cli_util.override('link.link_group.command_name', 'link'), cls=CommandGroupWithAlias, help="""A link between a parent tenancy and a child tenancy.""")
@cli_util.help_option_group
def link_group():
    pass


organizations_service_cli.organizations_service_group.add_command(link_root_group)
link_root_group.add_command(link_group)


@link_group.command(name=cli_util.override('link.delete_link.command_name', 'delete'), help=u"""Terminate the link. \n[Command Reference](deleteLink)""")
@cli_util.option('--link-id', required=True, help=u"""OCID of the link to terminate.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_link(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, link_id, if_match):

    if isinstance(link_id, six.string_types) and len(link_id.strip()) == 0:
        raise click.UsageError('Parameter --link-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'link', ctx)
    result = client.delete_link(
        link_id=link_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_link') and callable(getattr(client, 'get_link')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_link(link_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@link_group.command(name=cli_util.override('link.get_link.command_name', 'get'), help=u"""Gets information about the link. \n[Command Reference](getLink)""")
@cli_util.option('--link-id', required=True, help=u"""OCID of the link to retrieve.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'Link'})
@cli_util.wrap_exceptions
def get_link(ctx, from_json, link_id):

    if isinstance(link_id, six.string_types) and len(link_id.strip()) == 0:
        raise click.UsageError('Parameter --link-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'link', ctx)
    result = client.get_link(
        link_id=link_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@link_group.command(name=cli_util.override('link.list_links.command_name', 'list'), help=u"""Return a (paginated) list of links. \n[Command Reference](listLinks)""")
@cli_util.option('--parent-tenancy-id', help=u"""The ID of the parent tenancy this link is associated with.""")
@cli_util.option('--child-tenancy-id', help=u"""The ID of the child tenancy this link is associated with.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "TERMINATED"]), help=u"""The lifecycle state of the resource.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'LinkCollection'})
@cli_util.wrap_exceptions
def list_links(ctx, from_json, all_pages, page_size, parent_tenancy_id, child_tenancy_id, lifecycle_state, page, limit, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if parent_tenancy_id is not None:
        kwargs['parent_tenancy_id'] = parent_tenancy_id
    if child_tenancy_id is not None:
        kwargs['child_tenancy_id'] = child_tenancy_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'link', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_links,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_links,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_links(
            **kwargs
        )
    cli_util.render_response(result, ctx)
