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
from services.apm_traces.src.oci_cli_apm_traces.generated import apm_traces_service_cli


@click.command(cli_util.override('query.query_root_group.command_name', 'query'), cls=CommandGroupWithAlias, help=cli_util.override('query.query_root_group.help', """Use the Application Performance Monitoring Trace Explorer API to query traces and associated spans in Trace Explorer. For more information, see [Application Performance Monitoring]."""), short_help=cli_util.override('query.query_root_group.short_help', """Application Performance Monitoring Trace Explorer API"""))
@cli_util.help_option_group
def query_root_group():
    pass


@click.command(cli_util.override('query.query_result_response_group.command_name', 'query-result-response'), cls=CommandGroupWithAlias, help="""A response containing a collection of query rows (selected attributes and aggregations) filtered, grouped and sorted by the specified criteria from the query that is run, and the associated summary describing the corresponding query result metadata.""")
@cli_util.help_option_group
def query_result_response_group():
    pass


@click.command(cli_util.override('query.quick_pick_summary_group.command_name', 'quick-pick-summary'), cls=CommandGroupWithAlias, help="""Summary of the Quick Pick query objects.""")
@cli_util.help_option_group
def quick_pick_summary_group():
    pass


apm_traces_service_cli.apm_traces_service_group.add_command(query_root_group)
query_root_group.add_command(query_result_response_group)
query_root_group.add_command(quick_pick_summary_group)


@quick_pick_summary_group.command(name=cli_util.override('query.list_quick_picks.command_name', 'list-quick-picks'), help=u"""Returns a list of predefined Quick Pick queries intended to assist the user to choose a query to run.  There is no sorting applied on the results. \n[Command Reference](listQuickPicks)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous response.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_traces', 'class': 'list[QuickPickSummary]'})
@cli_util.wrap_exceptions
def list_quick_picks(ctx, from_json, all_pages, page_size, apm_domain_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_traces', 'query', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_quick_picks,
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_quick_picks,
            limit,
            page_size,
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    else:
        result = client.list_quick_picks(
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@query_result_response_group.command(name=cli_util.override('query.query.command_name', 'query'), help=u"""Retrieves the results (selected attributes and aggregations) of a query constructed according to the Application Performance Monitoring Defined Query Syntax. Query results are filtered by the filter criteria specified in the where clause. Further query results are grouped by the attributes specified in the group by clause.  Finally, ordering (asc/desc) is done by the specified attributes in the order by clause. \n[Command Reference](query)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--time-span-started-greater-than-or-equal-to', required=True, type=custom_types.CLI_DATETIME, help=u"""Include spans that have a `spanStartTime` equal to or greater than this value.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-span-started-less-than', required=True, type=custom_types.CLI_DATETIME, help=u"""Include spans that have a `spanStartTime`less than this value.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--query-text', help=u"""Application Performance Monitoring defined query string that filters and retrieves trace data results.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_traces', 'class': 'QueryResultResponse'})
@cli_util.wrap_exceptions
def query(ctx, from_json, apm_domain_id, time_span_started_greater_than_or_equal_to, time_span_started_less_than, query_text, limit, page):

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if query_text is not None:
        _details['queryText'] = query_text

    client = cli_util.build_client('apm_traces', 'query', ctx)
    result = client.query(
        apm_domain_id=apm_domain_id,
        time_span_started_greater_than_or_equal_to=time_span_started_greater_than_or_equal_to,
        time_span_started_less_than=time_span_started_less_than,
        query_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
