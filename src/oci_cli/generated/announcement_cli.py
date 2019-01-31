# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from ..cli_root import cli
from .. import cli_constants  # noqa: F401
from .. import cli_util
from .. import json_skeleton_utils
from .. import custom_types  # noqa: F401
from ..aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('announce_root_group.command_name', 'announce'), cls=CommandGroupWithAlias, help=cli_util.override('announce_root_group.help', """A description of the AnnouncementsService API"""), short_help=cli_util.override('announce_root_group.short_help', """Announcements Service API"""))
@cli_util.help_option_group
def announce_root_group():
    pass


@click.command(cli_util.override('announcements_collection_group.command_name', 'announcements-collection'), cls=CommandGroupWithAlias, help="""Results of annoucements search. Contains both announcements, and user specific status of the announcments""")
@cli_util.help_option_group
def announcements_collection_group():
    pass


@click.command(cli_util.override('announcement_user_status_details_group.command_name', 'announcement-user-status-details'), cls=CommandGroupWithAlias, help="""An announcement status""")
@cli_util.help_option_group
def announcement_user_status_details_group():
    pass


@click.command(cli_util.override('announcement_group.command_name', 'announcement'), cls=CommandGroupWithAlias, help="""An announcement object which represents a message targetted to a specific tenant""")
@cli_util.help_option_group
def announcement_group():
    pass


@click.command(cli_util.override('announcement_user_status_group.command_name', 'announcement-user-status'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def announcement_user_status_group():
    pass


announce_root_group.add_command(announcements_collection_group)
announce_root_group.add_command(announcement_user_status_details_group)
announce_root_group.add_command(announcement_group)
announce_root_group.add_command(announcement_user_status_group)


@announcement_group.command(name=cli_util.override('get_announcement.command_name', 'get'), help="""Gets details about single `Announcement` object""")
@cli_util.option('--announcement-id', required=True, help="""The OCID of the announcement""")
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
    client = cli_util.build_client('announcement', ctx)
    result = client.get_announcement(
        announcement_id=announcement_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@announcement_user_status_details_group.command(name=cli_util.override('get_announcement_user_status.command_name', 'get-announcement-user-status'), help="""Get user status of specified announcement""")
@cli_util.option('--announcement-id', required=True, help="""The OCID of the announcement""")
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
    client = cli_util.build_client('announcement', ctx)
    result = client.get_announcement_user_status(
        announcement_id=announcement_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@announcements_collection_group.command(name=cli_util.override('list_announcements.command_name', 'list-announcements'), help="""Gets a list of `Announcement` objects for the current tenancy""")
@cli_util.option('--compartment-id', required=True, help="""OCID of the compartment where search is performed. Announcements are specific to tenancy, so this should an ID of the root compartment""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--announcement-type', help="""Type of the announcements to show""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), help="""Filters returned announcements basing on whether they are active now""")
@cli_util.option('--is-banner', type=click.BOOL, help="""Filters returned announcements basing on whether they should be shown as a banner""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeOneValue", "timeTwoValue", "timeCreated", "referenceTicketNumber", "summary", "announcementType"]), help="""announcements sort order""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""sort order""")
@cli_util.option('--time-one-earliest-time', type=custom_types.CLI_DATETIME, help="""The earliest timeOneValue to include""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-one-latest-time', type=custom_types.CLI_DATETIME, help="""The latest timeOneValue to include""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'announcements_service', 'class': 'AnnouncementsCollection'})
@cli_util.wrap_exceptions
def list_announcements(ctx, from_json, all_pages, page_size, compartment_id, limit, page, announcement_type, lifecycle_state, is_banner, sort_by, sort_order, time_one_earliest_time, time_one_latest_time):

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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('announcement', ctx)
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


@announcement_user_status_group.command(name=cli_util.override('update_announcement_user_status.command_name', 'update'), help="""Update `Announcement` status with whether user has seen or supressed the announcement""")
@cli_util.option('--announcement-id', required=True, help="""The OCID of the announcement""")
@cli_util.option('--user-status-announcement-id', required=True, help="""The OCID of the announcement this status belongs to""")
@cli_util.option('--user-id', required=True, help="""The OCID of the user this status belongs to""")
@cli_util.option('--time-acknowledged', type=custom_types.CLI_DATETIME, help="""The date and time the announcement was acknowledged, in the format defined by RFC3339 Example: `2016-07-22T17:43:01.389+0000`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help="""Optimistic locking version""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_announcement_user_status(ctx, from_json, announcement_id, user_status_announcement_id, user_id, time_acknowledged, if_match):

    if isinstance(announcement_id, six.string_types) and len(announcement_id.strip()) == 0:
        raise click.UsageError('Parameter --announcement-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['userStatusAnnouncementId'] = user_status_announcement_id
    details['userId'] = user_id

    if time_acknowledged is not None:
        details['timeAcknowledged'] = time_acknowledged

    client = cli_util.build_client('announcement', ctx)
    result = client.update_announcement_user_status(
        announcement_id=announcement_id,
        status_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
