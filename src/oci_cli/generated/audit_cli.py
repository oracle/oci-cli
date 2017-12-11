# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from ..cli_root import cli
from .. import cli_util
from .. import json_skeleton_utils
from .. import retry_utils  # noqa: F401
from .. import custom_types  # noqa: F401
from ..aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('audit_group.command_name', 'audit'), cls=CommandGroupWithAlias, help=cli_util.override('audit_group.help', """API for the Audit Service. You can use this API for queries, but not bulk-export operations."""))
@cli_util.help_option_group
def audit_group():
    pass


@click.command(cli_util.override('audit_event_group.command_name', 'audit-event'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def audit_event_group():
    pass


@click.command(cli_util.override('configuration_group.command_name', 'configuration'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def configuration_group():
    pass


@configuration_group.command(name=cli_util.override('get_configuration.command_name', 'get'), help="""Get the configuration""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""ID of the root compartment (tenancy) [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'audit', 'class': 'Configuration'})
@cli_util.wrap_exceptions
def get_configuration(ctx, from_json, compartment_id):
    kwargs = {}
    client = cli_util.build_client('audit', ctx)
    result = client.get_configuration(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@audit_event_group.command(name=cli_util.override('list_events.command_name', 'list-events'), help="""Returns all audit events for the specified compartment that were processed within the specified time range.""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--start-time', callback=cli_util.handle_required_param, type=custom_types.CLI_DATETIME, help="""Returns events that were processed at or after this start date and time, expressed in [RFC 3339] timestamp format. For example, a start value of `2017-01-15T11:30:00Z` will retrieve a list of all events processed since 30 minutes after the 11th hour of January 15, 2017, in Coordinated Universal Time (UTC). You can specify a value with granularity to the minute. Seconds (and milliseconds, if included) must be set to `0`. [required]""")
@click.option('--end-time', callback=cli_util.handle_required_param, type=custom_types.CLI_DATETIME, help="""Returns events that were processed before this end date and time, expressed in [RFC 3339] timestamp format. For example, a start value of `2017-01-01T00:00:00Z` and an end value of `2017-01-02T00:00:00Z` will retrieve a list of all events processed on January 1, 2017. Similarly, a start value of `2017-01-01T00:00:00Z` and an end value of `2017-02-01T00:00:00Z` will result in a list of all events processed between January 1, 2017 and January 31, 2017. You can specify a value with granularity to the minute. Seconds (and milliseconds, if included) must be set to `0`. [required]""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous list query.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'audit', 'class': 'list[AuditEvent]'})
@cli_util.wrap_exceptions
def list_events(ctx, from_json, all_pages, compartment_id, start_time, end_time, page):

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('audit', ctx)
    if all_pages:
        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_events,
            compartment_id=compartment_id,
            start_time=start_time,
            end_time=end_time,
            **kwargs
        )
    else:
        result = client.list_events(
            compartment_id=compartment_id,
            start_time=start_time,
            end_time=end_time,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@configuration_group.command(name=cli_util.override('update_configuration.command_name', 'update'), help="""Update the configuration""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""ID of the root compartment (tenancy) [required]""")
@click.option('--retention-period-days', callback=cli_util.handle_optional_param, type=click.INT, help="""The retention period days""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_configuration(ctx, from_json, compartment_id, retention_period_days):
    kwargs = {}

    details = {}

    if retention_period_days is not None:
        details['retentionPeriodDays'] = retention_period_days

    client = cli_util.build_client('audit', ctx)
    result = client.update_configuration(
        compartment_id=compartment_id,
        update_configuration_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
