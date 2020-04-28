# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function

from services.audit.src.oci_cli_audit.generated import audit_cli
from oci_cli import cli_util
from oci_cli import custom_types
from oci_cli import json_skeleton_utils
from timeit import default_timer as timer
import click
import sys

cli_util.rename_command(audit_cli, audit_cli.audit_root_group, audit_cli.audit_event_group, "event")
cli_util.rename_command(audit_cli, audit_cli.audit_root_group, audit_cli.configuration_group, "config")
audit_cli.configuration_group.commands.pop(audit_cli.update_configuration.name)
audit_cli.audit_event_group.commands.pop(audit_cli.list_events.name)

cli_util.get_param(audit_cli.list_events, 'start_time').type = custom_types.CLI_DATETIME_ROUNDED_MINUTE
cli_util.get_param(audit_cli.list_events, 'end_time').type = custom_types.CLI_DATETIME_ROUNDED_MINUTE

audit_start_time_help = """Returns events that were processed at or after this start date and time. For example, a start value of `2017-01-15T11:30:00Z` will retrieve a list of all events processed since 30 minutes after the 11th hour of January 15, 2017, in Coordinated Universal Time (UTC).
You can specify a value with granularity to the minute. If seconds are provided then this will be rounded to the nearest minute, with greater than or equal to 30 seconds rounding up and less than 30 seconds rounding down.
""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE
cli_util.update_param_help(audit_cli.list_events, 'start_time', audit_start_time_help, append=False)
audit_end_time_help = """Returns events that were processed before this end date and time. For example, a start value of `2017-01-01T00:00:00Z` and an end value of `2017-01-02T00:00:00Z` will retrieve a list of all events processed on January 1, 2017. Similarly, a start value of `2017-01-01T00:00:00Z` and an end value of `2017-02-01T00:00:00Z` will result in a list of all events processed between January 1, 2017 and January 31, 2017.
You can specify a value with granularity to the minute. If seconds are provided then this will be rounded to the nearest minute, with greater than or equal to 30 seconds rounding up and less than 30 seconds rounding down.
""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE
cli_util.update_param_help(audit_cli.list_events, 'end_time', audit_end_time_help, append=False)


@cli_util.copy_params_from_generated_command(audit_cli.update_configuration, params_to_exclude=['wait_for_state', 'max_wait_seconds', 'wait_interval_seconds'])
@audit_cli.configuration_group.command(name=cli_util.override('update_configuration.command_name', 'update'), help="""Update the configuration""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PrivateIp'})
@cli_util.wrap_exceptions
def update_configuration(ctx, **kwargs):
    ctx.invoke(audit_cli.update_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(audit_cli.list_events, params_to_exclude=['start_time', 'end_time'])
@audit_cli.audit_event_group.command(name='list', help=audit_cli.list_events.help)
@cli_util.option('--skip-deserialization', 'skip_deserialization', is_flag=True, help="""Skips deserializing service response into python sdk response models and returns as plain JSON object.""")
@cli_util.option('--stream-output', 'stream_output', is_flag=True, help="""Print output to stdout as it is fetched so the full response is not stored in memory. This only works with --all.""")
@cli_util.option('--start-time', required=True, type=custom_types.CLI_DATETIME, help=u"""Returns events that were processed at or after this start date and time, expressed in [RFC 3339] timestamp format. For example, a start value of `2017-01-15T11:30:00Z` will retrieve a list of all events processed since 30 minutes after the 11th hour of January 15, 2017, in Coordinated Universal Time (UTC). You can specify a value with granularity to the minute. Seconds (and milliseconds, if included) must be set to `0`.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--end-time', required=True, type=custom_types.CLI_DATETIME, help=u"""Returns events that were processed before this end date and time, expressed in [RFC 3339] timestamp format. For example, a start value of `2017-01-01T00:00:00Z` and an end value of `2017-01-02T00:00:00Z` will retrieve a list of all events processed on January 1, 2017. Similarly, a start value of `2017-01-01T00:00:00Z` and an end value of `2017-02-01T00:00:00Z` will result in a list of all events processed between January 1, 2017 and January 31, 2017. You can specify a value with granularity to the minute. Seconds (and milliseconds, if included) must be set to `0`.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def list_events(ctx, from_json, all_pages, compartment_id, start_time, end_time, page, skip_deserialization, stream_output):
    if ctx.obj['debug']:
        start_command = timer()
        cli_util.output_memory('total memory usage before command execution: ')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    if skip_deserialization:
        ctx.obj['skip_deserialization'] = True

    client = cli_util.build_client('audit', 'audit', ctx)
    if all_pages:
        result = cli_util.list_call_get_all_results(
            client.list_events,
            stream_output=stream_output,
            ctx=ctx,
            is_json=True,
            compartment_id=compartment_id,
            start_time=start_time,
            end_time=end_time,
            **kwargs
        )
    else:
        # TODO: figure out streaming output for single page
        if stream_output:
            print("--stream-output requires --all.", file=sys.stderr)
            return

        result = client.list_events(
            compartment_id=compartment_id,
            start_time=start_time,
            end_time=end_time,
            **kwargs
        )
    if stream_output:
        # we've already printed everything
        if ctx.obj['debug']:
            print("", file=sys.stderr)
    else:
        start_render = timer()
        cli_util.render_response(result, ctx)
        if ctx.obj['debug']:
            print("", file=sys.stderr)
            end_render = timer()
            print("Time elapsed for total rendering response: {}".format(end_render - start_render), file=sys.stderr)
    if ctx.obj['debug']:
        end_command = timer()
        print("Time elapsed for total command execution: {}".format(end_command - start_command), file=sys.stderr)
        cli_util.output_memory('total memory usage after command execution: ')
