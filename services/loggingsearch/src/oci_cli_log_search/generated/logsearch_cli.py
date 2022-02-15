# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('logging_search.logging_search_root_group.command_name', 'logging-search'), cls=CommandGroupWithAlias, help=cli_util.override('logging_search.logging_search_root_group.help', """Search for logs in your compartments, log groups, and log objects."""), short_help=cli_util.override('logging_search.logging_search_root_group.short_help', """Logging Search API"""))
@cli_util.help_option_group
def logging_search_root_group():
    pass


@click.command(cli_util.override('logging_search.search_result_group.command_name', 'search-result'), cls=CommandGroupWithAlias, help="""A log search result entry.""")
@cli_util.help_option_group
def search_result_group():
    pass


logging_search_root_group.add_command(search_result_group)


@search_result_group.command(name=cli_util.override('logging_search.search_logs.command_name', 'search-logs'), help=u"""Submit a query to search logs.

See [Using the API] for SDK examples. \n[Command Reference](searchLogs)""")
@cli_util.option('--time-start', required=True, type=custom_types.CLI_DATETIME, help=u"""Start filter log's date and time, in the format defined by RFC3339.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', required=True, type=custom_types.CLI_DATETIME, help=u"""End filter log's date and time, in the format defined by RFC3339.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--search-query', required=True, help=u"""Query corresponding to the search operation. This query is parsed and validated before execution and should follow the specification. For more information on the query language specification, see [Logging Query Language Specification].""")
@cli_util.option('--is-return-field-info', type=click.BOOL, help=u"""Whether to return field schema information for the log stream specified in searchQuery.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a response. Pagination is not supported in this API.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the opc-next-page response header from the previous \"Search\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'loggingsearch', 'class': 'SearchResponse'})
@cli_util.wrap_exceptions
def search_logs(ctx, from_json, time_start, time_end, search_query, is_return_field_info, limit, page):

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['timeStart'] = time_start
    _details['timeEnd'] = time_end
    _details['searchQuery'] = search_query

    if is_return_field_info is not None:
        _details['isReturnFieldInfo'] = is_return_field_info

    client = cli_util.build_client('loggingsearch', 'log_search', ctx)
    result = client.search_logs(
        search_logs_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
