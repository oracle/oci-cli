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


@click.command(cli_util.override('announcement.announcement_root_group.command_name', 'announcement'), cls=CommandGroupWithAlias, help=cli_util.override('announcement.announcement_root_group.help', """Manage Oracle Cloud Infrastructure console announcements."""), short_help=cli_util.override('announcement.announcement_root_group.short_help', """Announcements Service API"""))
@cli_util.help_option_group
def announcement_root_group():
    pass


@click.command(cli_util.override('announcement.announcements_collection_group.command_name', 'announcements-collection'), cls=CommandGroupWithAlias, help="""A list of announcements that match filter criteria, if any. Results contain both the announcements and the user-specific status of the announcements.""")
@cli_util.help_option_group
def announcements_collection_group():
    pass


@click.command(cli_util.override('announcement.announcement_user_status_details_group.command_name', 'announcement-user-status-details'), cls=CommandGroupWithAlias, help="""An announcement's status regarding whether it has been acknowledged by a user.""")
@cli_util.help_option_group
def announcement_user_status_details_group():
    pass


@click.command(cli_util.override('announcement.announcement_group.command_name', 'announcement'), cls=CommandGroupWithAlias, help="""A message about an impactful operational event.""")
@cli_util.help_option_group
def announcement_group():
    pass


announce_service_cli.announce_service_group.add_command(announcement_root_group)
announcement_root_group.add_command(announcements_collection_group)
announcement_root_group.add_command(announcement_user_status_details_group)
announcement_root_group.add_command(announcement_group)


@announcement_group.command(name=cli_util.override('announcement.get_announcement.command_name', 'get'), help=u"""Gets the details of a specific announcement.

This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy. \n[Command Reference](getAnnouncement)""")
@cli_util.option('--announcement-id', required=True, help=u"""The OCID of the announcement.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'announcements_service', 'class': 'Announcement'})
@cli_util.wrap_exceptions
def get_announcement(ctx, from_json, announcement_id):

    if isinstance(announcement_id, six.string_types) and len(announcement_id.strip()) == 0:
        raise click.UsageError('Parameter --announcement-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('announcements_service', 'announcement', ctx)
    result = client.get_announcement(
        announcement_id=announcement_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@announcement_user_status_details_group.command(name=cli_util.override('announcement.get_announcement_user_status.command_name', 'get-announcement-user-status'), help=u"""Gets information about whether a specific announcement was acknowledged by a user.

This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy. \n[Command Reference](getAnnouncementUserStatus)""")
@cli_util.option('--announcement-id', required=True, help=u"""The OCID of the announcement.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'announcements_service', 'class': 'AnnouncementUserStatusDetails'})
@cli_util.wrap_exceptions
def get_announcement_user_status(ctx, from_json, announcement_id):

    if isinstance(announcement_id, six.string_types) and len(announcement_id.strip()) == 0:
        raise click.UsageError('Parameter --announcement-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('announcements_service', 'announcement', ctx)
    result = client.get_announcement_user_status(
        announcement_id=announcement_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@announcements_collection_group.command(name=cli_util.override('announcement.list_announcements.command_name', 'list-announcements'), help=u"""Gets a list of announcements for the current tenancy.

This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy. \n[Command Reference](listAnnouncements)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--announcement-type', help=u"""The type of announcement.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), help=u"""The announcement's current lifecycle state.""")
@cli_util.option('--is-banner', type=click.BOOL, help=u"""Whether the announcement is displayed as a console banner.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeOneValue", "timeTwoValue", "timeCreated", "referenceTicketNumber", "summary", "announcementType"]), help=u"""The criteria to sort by. You can specify only one sort order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. (Sorting by `announcementType` orders the announcements list according to importance.)""")
@cli_util.option('--time-one-earliest-time', type=custom_types.CLI_DATETIME, help=u"""The boundary for the earliest `timeOneValue` date on announcements that you want to see.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-one-latest-time', type=custom_types.CLI_DATETIME, help=u"""The boundary for the latest `timeOneValue` date on announcements that you want to see.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--environment-name', help=u"""A filter to return only announcements that match a specific environment name.""")
@cli_util.option('--service', help=u"""A filter to return only announcements affecting a specific service.""")
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["IAAS", "SAAS"]), help=u"""A filter to return only announcements affecting a specific platform.""")
@cli_util.option('--exclude-announcement-types', multiple=True, help=u"""Exclude The type of announcement.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'exclude-announcement-types': {'module': 'announcements_service', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'exclude-announcement-types': {'module': 'announcements_service', 'class': 'list[string]'}}, output_type={'module': 'announcements_service', 'class': 'AnnouncementsCollection'})
@cli_util.wrap_exceptions
def list_announcements(ctx, from_json, all_pages, page_size, compartment_id, limit, page, announcement_type, lifecycle_state, is_banner, sort_by, sort_order, time_one_earliest_time, time_one_latest_time, environment_name, service, platform_type, exclude_announcement_types):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if announcement_type is not None:
        kwargs['announcement_type'] = announcement_type
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if is_banner is not None:
        kwargs['is_banner'] = is_banner
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if time_one_earliest_time is not None:
        kwargs['time_one_earliest_time'] = time_one_earliest_time
    if time_one_latest_time is not None:
        kwargs['time_one_latest_time'] = time_one_latest_time
    if environment_name is not None:
        kwargs['environment_name'] = environment_name
    if service is not None:
        kwargs['service'] = service
    if platform_type is not None:
        kwargs['platform_type'] = platform_type
    if exclude_announcement_types is not None and len(exclude_announcement_types) > 0:
        kwargs['exclude_announcement_types'] = exclude_announcement_types
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('announcements_service', 'announcement', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_announcements,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_announcements,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_announcements(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@announcement_user_status_details_group.command(name=cli_util.override('announcement.update_announcement_user_status.command_name', 'update-announcement-user-status'), help=u"""Updates the status of the specified announcement with regard to whether it has been marked as read.

This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy. \n[Command Reference](updateAnnouncementUserStatus)""")
@cli_util.option('--announcement-id', required=True, help=u"""The OCID of the announcement.""")
@cli_util.option('--user-status-announcement-id', required=True, help=u"""The OCID of the announcement that this status is associated with.""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user that this status is associated with.""")
@cli_util.option('--time-acknowledged', type=custom_types.CLI_DATETIME, help=u"""The date and time the announcement was acknowledged, expressed in [RFC 3339] timestamp format. Example: `2019-01-01T17:43:01.389+0000`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help=u"""The locking version, used for optimistic concurrency control.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'announcements_service', 'class': 'AnnouncementUserStatusDetails'})
@cli_util.wrap_exceptions
def update_announcement_user_status(ctx, from_json, announcement_id, user_status_announcement_id, user_id, time_acknowledged, if_match):

    if isinstance(announcement_id, six.string_types) and len(announcement_id.strip()) == 0:
        raise click.UsageError('Parameter --announcement-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['userStatusAnnouncementId'] = user_status_announcement_id
    _details['userId'] = user_id

    if time_acknowledged is not None:
        _details['timeAcknowledged'] = time_acknowledged

    client = cli_util.build_client('announcements_service', 'announcement', ctx)
    result = client.update_announcement_user_status(
        announcement_id=announcement_id,
        status_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
