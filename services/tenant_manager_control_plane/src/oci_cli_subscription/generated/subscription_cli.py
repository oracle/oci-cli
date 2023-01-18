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
from services.tenant_manager_control_plane.src.oci_cli_tenant_manager_control_plane.generated import organizations_service_cli


@click.command(cli_util.override('subscription.subscription_root_group.command_name', 'subscription'), cls=CommandGroupWithAlias, help=cli_util.override('subscription.subscription_root_group.help', """The Organizations API allows you to consolidate multiple OCI tenancies into an organization, and centrally manage your tenancies and its resources."""), short_help=cli_util.override('subscription.subscription_root_group.short_help', """Organizations API"""))
@cli_util.help_option_group
def subscription_root_group():
    pass


@click.command(cli_util.override('subscription.subscription_mapping_group.command_name', 'subscription-mapping'), cls=CommandGroupWithAlias, help="""Subscription mapping information.""")
@cli_util.help_option_group
def subscription_mapping_group():
    pass


@click.command(cli_util.override('subscription.assigned_subscription_group.command_name', 'assigned-subscription'), cls=CommandGroupWithAlias, help="""Assigned subscription information.""")
@cli_util.help_option_group
def assigned_subscription_group():
    pass


@click.command(cli_util.override('subscription.subscription_group.command_name', 'subscription'), cls=CommandGroupWithAlias, help="""Subscription information for compartmentId. Only root compartments are allowed.""")
@cli_util.help_option_group
def subscription_group():
    pass


organizations_service_cli.organizations_service_group.add_command(subscription_root_group)
subscription_root_group.add_command(subscription_mapping_group)
subscription_root_group.add_command(assigned_subscription_group)
subscription_root_group.add_command(subscription_group)


@subscription_mapping_group.command(name=cli_util.override('subscription.create_subscription_mapping.command_name', 'create'), help=u"""Assign the tenancy record identified by the compartment ID to the given subscription ID. \n[Command Reference](createSubscriptionMapping)""")
@cli_util.option('--compartment-id', required=True, help=u"""OCID of the compartment. Always a tenancy OCID.""")
@cli_util.option('--subscription-id', required=True, help=u"""OCID of subscription.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'SubscriptionMapping'})
@cli_util.wrap_exceptions
def create_subscription_mapping(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, subscription_id, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['subscriptionId'] = subscription_id

    client = cli_util.build_client('tenant_manager_control_plane', 'subscription', ctx)
    result = client.create_subscription_mapping(
        create_subscription_mapping_details=_details,
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


@subscription_mapping_group.command(name=cli_util.override('subscription.delete_subscription_mapping.command_name', 'delete'), help=u"""Delete the subscription mapping details by subscription mapping ID. \n[Command Reference](deleteSubscriptionMapping)""")
@cli_util.option('--subscription-mapping-id', required=True, help=u"""OCID of the subscription mapping ID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_subscription_mapping(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, subscription_mapping_id, if_match):

    if isinstance(subscription_mapping_id, six.string_types) and len(subscription_mapping_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-mapping-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'subscription', ctx)
    result = client.delete_subscription_mapping(
        subscription_mapping_id=subscription_mapping_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_subscription_mapping') and callable(getattr(client, 'get_subscription_mapping')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_subscription_mapping(subscription_mapping_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@assigned_subscription_group.command(name=cli_util.override('subscription.get_assigned_subscription.command_name', 'get'), help=u"""Get the assigned subscription details by assigned subscription ID. \n[Command Reference](getAssignedSubscription)""")
@cli_util.option('--assigned-subscription-id', required=True, help=u"""OCID of the assigned subscription.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'AssignedSubscription'})
@cli_util.wrap_exceptions
def get_assigned_subscription(ctx, from_json, assigned_subscription_id):

    if isinstance(assigned_subscription_id, six.string_types) and len(assigned_subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --assigned-subscription-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'subscription', ctx)
    result = client.get_assigned_subscription(
        assigned_subscription_id=assigned_subscription_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subscription_group.command(name=cli_util.override('subscription.get_subscription.command_name', 'get'), help=u"""Gets the subscription details by subscriptionId. \n[Command Reference](getSubscription)""")
@cli_util.option('--subscription-id', required=True, help=u"""OCID of the subscription.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'Subscription'})
@cli_util.wrap_exceptions
def get_subscription(ctx, from_json, subscription_id):

    if isinstance(subscription_id, six.string_types) and len(subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'subscription', ctx)
    result = client.get_subscription(
        subscription_id=subscription_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subscription_mapping_group.command(name=cli_util.override('subscription.get_subscription_mapping.command_name', 'get'), help=u"""Get the subscription mapping details by subscription mapping ID. \n[Command Reference](getSubscriptionMapping)""")
@cli_util.option('--subscription-mapping-id', required=True, help=u"""OCID of the subscriptionMappingId.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'SubscriptionMapping'})
@cli_util.wrap_exceptions
def get_subscription_mapping(ctx, from_json, subscription_mapping_id):

    if isinstance(subscription_mapping_id, six.string_types) and len(subscription_mapping_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-mapping-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'subscription', ctx)
    result = client.get_subscription_mapping(
        subscription_mapping_id=subscription_mapping_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@assigned_subscription_group.command(name=cli_util.override('subscription.list_assigned_subscriptions.command_name', 'list'), help=u"""Lists subscriptions that are consumed by the compartment. Only the root compartment is allowed. \n[Command Reference](listAssignedSubscriptions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--subscription-id', help=u"""The ID of the subscription to which the tenancy is associated.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. * The default order for timeCreated is descending. * The default order for displayName is ascending. * If no value is specified, timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'AssignedSubscriptionCollection'})
@cli_util.wrap_exceptions
def list_assigned_subscriptions(ctx, from_json, all_pages, page_size, compartment_id, subscription_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if subscription_id is not None:
        kwargs['subscription_id'] = subscription_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'subscription', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_assigned_subscriptions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_assigned_subscriptions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_assigned_subscriptions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@subscription_group.command(name=cli_util.override('subscription.list_available_regions.command_name', 'list-available-regions'), help=u"""List the available regions based on subscription ID. \n[Command Reference](listAvailableRegions)""")
@cli_util.option('--subscription-id', required=True, help=u"""The ID of the subscription to which the tenancy is associated.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'AvailableRegionCollection'})
@cli_util.wrap_exceptions
def list_available_regions(ctx, from_json, all_pages, subscription_id, page):

    if isinstance(subscription_id, six.string_types) and len(subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'subscription', ctx)
    if all_pages:
        result = cli_util.list_call_get_all_results(
            client.list_available_regions,
            subscription_id=subscription_id,
            **kwargs
        )
    else:
        result = client.list_available_regions(
            subscription_id=subscription_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@subscription_mapping_group.command(name=cli_util.override('subscription.list_subscription_mappings.command_name', 'list'), help=u"""Lists the subscription mappings for all the subscriptions owned by a given compartmentId. Only the root compartment is allowed. \n[Command Reference](listSubscriptionMappings)""")
@cli_util.option('--subscription-id', required=True, help=u"""The ID of the subscription to which the tenancy is associated.""")
@cli_util.option('--subscription-mapping-id', help=u"""SubscriptionMappingId is a unique ID for subscription and tenancy mapping.""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), help=u"""The lifecycle state of the resource.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. * The default order for timeCreated is descending. * The default order for displayName is ascending. * If no value is specified, timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'SubscriptionMappingCollection'})
@cli_util.wrap_exceptions
def list_subscription_mappings(ctx, from_json, all_pages, page_size, subscription_id, subscription_mapping_id, compartment_id, lifecycle_state, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if subscription_mapping_id is not None:
        kwargs['subscription_mapping_id'] = subscription_mapping_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'subscription', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_subscription_mappings,
            subscription_id=subscription_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_subscription_mappings,
            limit,
            page_size,
            subscription_id=subscription_id,
            **kwargs
        )
    else:
        result = client.list_subscription_mappings(
            subscription_id=subscription_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@subscription_group.command(name=cli_util.override('subscription.list_subscriptions.command_name', 'list'), help=u"""List the subscriptions that a compartment owns. Only the root compartment is allowed. \n[Command Reference](listSubscriptions)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--subscription-id', help=u"""The ID of the subscription to which the tenancy is associated.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. * The default order for timeCreated is descending. * The default order for displayName is ascending. * If no value is specified, timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'SubscriptionCollection'})
@cli_util.wrap_exceptions
def list_subscriptions(ctx, from_json, all_pages, page_size, compartment_id, subscription_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if subscription_id is not None:
        kwargs['subscription_id'] = subscription_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'subscription', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_subscriptions,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_subscriptions,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_subscriptions(
            **kwargs
        )
    cli_util.render_response(result, ctx)
