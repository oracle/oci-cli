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
from services.fusion_apps.src.oci_cli_fusion_apps.generated import fusion_apps_service_cli


@click.command(cli_util.override('scheduled_activity.scheduled_activity_root_group.command_name', 'scheduled-activity'), cls=CommandGroupWithAlias, help=cli_util.override('scheduled_activity.scheduled_activity_root_group.help', """Use the Fusion Applications Environment Management API to manage the environments where your Fusion Applications run. For more information, see the [Fusion Applications Environment Management documentation]."""), short_help=cli_util.override('scheduled_activity.scheduled_activity_root_group.short_help', """Fusion Applications Environment Management API"""))
@cli_util.help_option_group
def scheduled_activity_root_group():
    pass


@click.command(cli_util.override('scheduled_activity.scheduled_activity_group.command_name', 'scheduled-activity'), cls=CommandGroupWithAlias, help="""Details of scheduled activity.""")
@cli_util.help_option_group
def scheduled_activity_group():
    pass


fusion_apps_service_cli.fusion_apps_service_group.add_command(scheduled_activity_root_group)
scheduled_activity_root_group.add_command(scheduled_activity_group)


@scheduled_activity_group.command(name=cli_util.override('scheduled_activity.get_scheduled_activity.command_name', 'get'), help=u"""Gets a ScheduledActivity by identifier \n[Command Reference](getScheduledActivity)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--scheduled-activity-id', required=True, help=u"""Unique ScheduledActivity identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'ScheduledActivity'})
@cli_util.wrap_exceptions
def get_scheduled_activity(ctx, from_json, fusion_environment_id, scheduled_activity_id):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    if isinstance(scheduled_activity_id, six.string_types) and len(scheduled_activity_id.strip()) == 0:
        raise click.UsageError('Parameter --scheduled-activity-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'scheduled_activity', ctx)
    result = client.get_scheduled_activity(
        fusion_environment_id=fusion_environment_id,
        scheduled_activity_id=scheduled_activity_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@scheduled_activity_group.command(name=cli_util.override('scheduled_activity.list_scheduled_activities.command_name', 'list'), help=u"""Returns a list of ScheduledActivities. \n[Command Reference](listScheduledActivities)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--time-scheduled-start-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that returns all resources that are scheduled after this date""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-expected-finish-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that returns all resources that end before this date""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--run-cycle', type=custom_types.CliCaseInsensitiveChoice(["QUARTERLY", "MONTHLY", "ONEOFF", "VERTEX"]), help=u"""A filter that returns all resources that match the specified run cycle.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), help=u"""A filter that returns all resources that match the specified status""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'ScheduledActivityCollection'})
@cli_util.wrap_exceptions
def list_scheduled_activities(ctx, from_json, all_pages, page_size, fusion_environment_id, display_name, time_scheduled_start_greater_than_or_equal_to, time_expected_finish_less_than_or_equal_to, run_cycle, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if time_scheduled_start_greater_than_or_equal_to is not None:
        kwargs['time_scheduled_start_greater_than_or_equal_to'] = time_scheduled_start_greater_than_or_equal_to
    if time_expected_finish_less_than_or_equal_to is not None:
        kwargs['time_expected_finish_less_than_or_equal_to'] = time_expected_finish_less_than_or_equal_to
    if run_cycle is not None:
        kwargs['run_cycle'] = run_cycle
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
    client = cli_util.build_client('fusion_apps', 'scheduled_activity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_scheduled_activities,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_scheduled_activities,
            limit,
            page_size,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    else:
        result = client.list_scheduled_activities(
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
