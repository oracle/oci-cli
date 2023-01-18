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
from services.announcements_service.src.oci_cli_announcements_service.generated import announce_service_cli


@click.command(cli_util.override('announcement_subscription.announcement_subscription_root_group.command_name', 'announcement-subscription'), cls=CommandGroupWithAlias, help=cli_util.override('announcement_subscription.announcement_subscription_root_group.help', """Manage Oracle Cloud Infrastructure console announcements."""), short_help=cli_util.override('announcement_subscription.announcement_subscription_root_group.short_help', """Announcements Service API"""))
@cli_util.help_option_group
def announcement_subscription_root_group():
    pass


@click.command(cli_util.override('announcement_subscription.announcement_subscription_group.command_name', 'announcement-subscription'), cls=CommandGroupWithAlias, help="""A subscription with the Announcements service to receive selected announcements in the format and delivery mechanisms supported by a corresponding topic endpoint configured in the Oracle Cloud Infrastructure Notifications service.""")
@cli_util.help_option_group
def announcement_subscription_group():
    pass


@click.command(cli_util.override('announcement_subscription.announcement_subscription_collection_group.command_name', 'announcement-subscription-collection'), cls=CommandGroupWithAlias, help="""The results of a search for announcement subscriptions. This object contains both announcement subscription summary objects and other information, such as metadata.""")
@cli_util.help_option_group
def announcement_subscription_collection_group():
    pass


announce_service_cli.announce_service_group.add_command(announcement_subscription_root_group)
announcement_subscription_root_group.add_command(announcement_subscription_group)
announcement_subscription_root_group.add_command(announcement_subscription_collection_group)


@announcement_subscription_group.command(name=cli_util.override('announcement_subscription.change_announcement_subscription_compartment.command_name', 'change-compartment'), help=u"""Moves the specified announcement subscription from one compartment to another compartment. When provided, If-Match is checked against ETag values of the resource.

This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy. \n[Command Reference](changeAnnouncementSubscriptionCompartment)""")
@cli_util.option('--announcement-subscription-id', required=True, help=u"""The OCID of the announcement subscription.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which you want to move the announcement subscription.""")
@cli_util.option('--if-match', help=u"""The locking version, used for optimistic concurrency control.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_announcement_subscription_compartment(ctx, from_json, announcement_subscription_id, compartment_id, if_match):

    if isinstance(announcement_subscription_id, six.string_types) and len(announcement_subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --announcement-subscription-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('announcements_service', 'announcement_subscription', ctx)
    result = client.change_announcement_subscription_compartment(
        announcement_subscription_id=announcement_subscription_id,
        change_announcement_subscription_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@announcement_subscription_group.command(name=cli_util.override('announcement_subscription.create_announcement_subscription.command_name', 'create'), help=u"""Creates a new announcement subscription.

This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy. \n[Command Reference](createAnnouncementSubscription)""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name for the announcement subscription. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the announcement subscription.""")
@cli_util.option('--ons-topic-id', required=True, help=u"""The OCID of the Notifications service topic that is the target for publishing announcements that match the configured announcement subscription. The caller of the operation needs the ONS_TOPIC_PUBLISH permission for the targeted Notifications service topic. For more information about Notifications permissions, see [Details for Notifications].""")
@cli_util.option('--description', help=u"""A description of the announcement subscription. Avoid entering confidential information.""")
@cli_util.option('--filter-groups', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of filter groups for the announcement subscription. A filter group combines one or more filters that the Announcements service applies to announcements for matching purposes.

This option is a JSON dictionary of type dict(str, FilterGroupDetails).  For documentation on FilterGroupDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/announcementsubscription/0.0.1/datatypes/FilterGroupDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--preferred-language', help=u"""(For announcement subscriptions with Oracle Fusion Applications configured as the service only) The language in which the user prefers to receive emailed announcements. Specify the preference with a value that uses the language tag format (x-obmcs-human-language). For example fr-FR.""")
@cli_util.option('--preferred-time-zone', help=u"""The time zone that the user prefers for announcement time stamps. Specify the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example America/Los_Angeles.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'filter-groups': {'module': 'announcements_service', 'class': 'dict(str, FilterGroupDetails)'}, 'freeform-tags': {'module': 'announcements_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'announcements_service', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'filter-groups': {'module': 'announcements_service', 'class': 'dict(str, FilterGroupDetails)'}, 'freeform-tags': {'module': 'announcements_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'announcements_service', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'announcements_service', 'class': 'AnnouncementSubscription'})
@cli_util.wrap_exceptions
def create_announcement_subscription(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, ons_topic_id, description, filter_groups, preferred_language, preferred_time_zone, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['onsTopicId'] = ons_topic_id

    if description is not None:
        _details['description'] = description

    if filter_groups is not None:
        _details['filterGroups'] = cli_util.parse_json_parameter("filter_groups", filter_groups)

    if preferred_language is not None:
        _details['preferredLanguage'] = preferred_language

    if preferred_time_zone is not None:
        _details['preferredTimeZone'] = preferred_time_zone

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('announcements_service', 'announcement_subscription', ctx)
    result = client.create_announcement_subscription(
        create_announcement_subscription_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_announcement_subscription') and callable(getattr(client, 'get_announcement_subscription')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_announcement_subscription(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@announcement_subscription_group.command(name=cli_util.override('announcement_subscription.create_filter_group.command_name', 'create-filter-group'), help=u"""Creates a new filter group in the specified announcement subscription.

This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy. \n[Command Reference](createFilterGroup)""")
@cli_util.option('--announcement-subscription-id', required=True, help=u"""The OCID of the announcement subscription.""")
@cli_util.option('--name', required=True, help=u"""The name of the filter group. The name must be unique and it cannot be changed. Avoid entering confidential information.""")
@cli_util.option('--filters', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of filters against which the Announcements service will match announcements. You cannot have more than one of any given filter type within a filter group.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The locking version, used for optimistic concurrency control.""")
@json_skeleton_utils.get_cli_json_input_option({'filters': {'module': 'announcements_service', 'class': 'list[Filter]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'filters': {'module': 'announcements_service', 'class': 'list[Filter]'}}, output_type={'module': 'announcements_service', 'class': 'FilterGroup'})
@cli_util.wrap_exceptions
def create_filter_group(ctx, from_json, announcement_subscription_id, name, filters, if_match):

    if isinstance(announcement_subscription_id, six.string_types) and len(announcement_subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --announcement-subscription-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['filters'] = cli_util.parse_json_parameter("filters", filters)

    client = cli_util.build_client('announcements_service', 'announcement_subscription', ctx)
    result = client.create_filter_group(
        announcement_subscription_id=announcement_subscription_id,
        create_filter_group_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@announcement_subscription_group.command(name=cli_util.override('announcement_subscription.delete_announcement_subscription.command_name', 'delete'), help=u"""Deletes the specified announcement subscription.

This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy. \n[Command Reference](deleteAnnouncementSubscription)""")
@cli_util.option('--announcement-subscription-id', required=True, help=u"""The OCID of the announcement subscription.""")
@cli_util.option('--if-match', help=u"""The locking version, used for optimistic concurrency control.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_announcement_subscription(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, announcement_subscription_id, if_match):

    if isinstance(announcement_subscription_id, six.string_types) and len(announcement_subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --announcement-subscription-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('announcements_service', 'announcement_subscription', ctx)
    result = client.delete_announcement_subscription(
        announcement_subscription_id=announcement_subscription_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_announcement_subscription') and callable(getattr(client, 'get_announcement_subscription')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_announcement_subscription(announcement_subscription_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@announcement_subscription_group.command(name=cli_util.override('announcement_subscription.delete_filter_group.command_name', 'delete-filter-group'), help=u"""Deletes a filter group in the specified announcement subscription.

This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy. \n[Command Reference](deleteFilterGroup)""")
@cli_util.option('--announcement-subscription-id', required=True, help=u"""The OCID of the announcement subscription.""")
@cli_util.option('--filter-group-name', required=True, help=u"""The name of the filter group.""")
@cli_util.option('--if-match', help=u"""The locking version, used for optimistic concurrency control.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_filter_group(ctx, from_json, announcement_subscription_id, filter_group_name, if_match):

    if isinstance(announcement_subscription_id, six.string_types) and len(announcement_subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --announcement-subscription-id cannot be whitespace or empty string')

    if isinstance(filter_group_name, six.string_types) and len(filter_group_name.strip()) == 0:
        raise click.UsageError('Parameter --filter-group-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('announcements_service', 'announcement_subscription', ctx)
    result = client.delete_filter_group(
        announcement_subscription_id=announcement_subscription_id,
        filter_group_name=filter_group_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@announcement_subscription_group.command(name=cli_util.override('announcement_subscription.get_announcement_subscription.command_name', 'get'), help=u"""Gets the specified announcement subscription.

This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy. \n[Command Reference](getAnnouncementSubscription)""")
@cli_util.option('--announcement-subscription-id', required=True, help=u"""The OCID of the announcement subscription.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'announcements_service', 'class': 'AnnouncementSubscription'})
@cli_util.wrap_exceptions
def get_announcement_subscription(ctx, from_json, announcement_subscription_id):

    if isinstance(announcement_subscription_id, six.string_types) and len(announcement_subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --announcement-subscription-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('announcements_service', 'announcement_subscription', ctx)
    result = client.get_announcement_subscription(
        announcement_subscription_id=announcement_subscription_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@announcement_subscription_collection_group.command(name=cli_util.override('announcement_subscription.list_announcement_subscriptions.command_name', 'list-announcement-subscriptions'), help=u"""Gets a list of all announcement subscriptions in the specified compartment.

This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy. \n[Command Reference](listAnnouncementSubscriptions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "FAILED"]), help=u"""A filter to return only announcement subscriptions that match the given lifecycle state.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--id', help=u"""The OCID of the announcement subscription.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether ascending ('ASC') or descending ('DESC').""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The criteria to sort by. You can specify only one sort order. The default sort order for the creation date of resources is descending. The default sort order for display names is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'announcements_service', 'class': 'AnnouncementSubscriptionCollection'})
@cli_util.wrap_exceptions
def list_announcement_subscriptions(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by):

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
    client = cli_util.build_client('announcements_service', 'announcement_subscription', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_announcement_subscriptions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_announcement_subscriptions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_announcement_subscriptions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@announcement_subscription_group.command(name=cli_util.override('announcement_subscription.update_announcement_subscription.command_name', 'update'), help=u"""Updates the specified announcement subscription.

This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy. \n[Command Reference](updateAnnouncementSubscription)""")
@cli_util.option('--announcement-subscription-id', required=True, help=u"""The OCID of the announcement subscription.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the announcement subscription. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A description of the announcement subscription. Avoid entering confidential information.""")
@cli_util.option('--ons-topic-id', help=u"""The [OCID] of the Notifications service topic that is the target for publishing announcements that match the configured announcement subscription. The caller of the operation needs the ONS_TOPIC_PUBLISH permission for the targeted Notifications service topic. For more information about Notifications permissions, see [Details for Notifications].""")
@cli_util.option('--preferred-language', help=u"""(For announcement subscriptions with Oracle Fusion Applications configured as the service only) The language in which the user prefers to receive emailed announcements. Specify the preference with a value that uses the language tag format (x-obmcs-human-language). For example fr-FR.""")
@cli_util.option('--preferred-time-zone', help=u"""The time zone that the user prefers for announcement time stamps. Specify the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example America/Los_Angeles.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The locking version, used for optimistic concurrency control.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'announcements_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'announcements_service', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'announcements_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'announcements_service', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'announcements_service', 'class': 'AnnouncementSubscription'})
@cli_util.wrap_exceptions
def update_announcement_subscription(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, announcement_subscription_id, display_name, description, ons_topic_id, preferred_language, preferred_time_zone, freeform_tags, defined_tags, if_match):

    if isinstance(announcement_subscription_id, six.string_types) and len(announcement_subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --announcement-subscription-id cannot be whitespace or empty string')
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

    if ons_topic_id is not None:
        _details['onsTopicId'] = ons_topic_id

    if preferred_language is not None:
        _details['preferredLanguage'] = preferred_language

    if preferred_time_zone is not None:
        _details['preferredTimeZone'] = preferred_time_zone

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('announcements_service', 'announcement_subscription', ctx)
    result = client.update_announcement_subscription(
        announcement_subscription_id=announcement_subscription_id,
        update_announcement_subscription_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_announcement_subscription') and callable(getattr(client, 'get_announcement_subscription')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_announcement_subscription(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@announcement_subscription_group.command(name=cli_util.override('announcement_subscription.update_filter_group.command_name', 'update-filter-group'), help=u"""Updates a filter group in the specified announcement subscription.

This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy. \n[Command Reference](updateFilterGroup)""")
@cli_util.option('--announcement-subscription-id', required=True, help=u"""The OCID of the announcement subscription.""")
@cli_util.option('--filter-group-name', required=True, help=u"""The name of the filter group.""")
@cli_util.option('--filters', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of filters against which the Announcements service will match announcements. You cannot have more than one of any given filter type within a filter group.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The locking version, used for optimistic concurrency control.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'filters': {'module': 'announcements_service', 'class': 'list[Filter]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'filters': {'module': 'announcements_service', 'class': 'list[Filter]'}}, output_type={'module': 'announcements_service', 'class': 'FilterGroup'})
@cli_util.wrap_exceptions
def update_filter_group(ctx, from_json, force, announcement_subscription_id, filter_group_name, filters, if_match):

    if isinstance(announcement_subscription_id, six.string_types) and len(announcement_subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --announcement-subscription-id cannot be whitespace or empty string')

    if isinstance(filter_group_name, six.string_types) and len(filter_group_name.strip()) == 0:
        raise click.UsageError('Parameter --filter-group-name cannot be whitespace or empty string')
    if not force:
        if filters:
            if not click.confirm("WARNING: Updates to filters will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['filters'] = cli_util.parse_json_parameter("filters", filters)

    client = cli_util.build_client('announcements_service', 'announcement_subscription', ctx)
    result = client.update_filter_group(
        announcement_subscription_id=announcement_subscription_id,
        filter_group_name=filter_group_name,
        update_filter_group_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
