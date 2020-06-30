# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('usage_api.usage_api_root_group.command_name', 'usage-api'), cls=CommandGroupWithAlias, help=cli_util.override('usage_api.usage_api_root_group.help', """A description of the UsageApi API."""), short_help=cli_util.override('usage_api.usage_api_root_group.short_help', """Usage API"""))
@cli_util.help_option_group
def usage_api_root_group():
    pass


@click.command(cli_util.override('usage_api.usage_summary_group.command_name', 'usage-summary'), cls=CommandGroupWithAlias, help="""The result from usage store.""")
@cli_util.help_option_group
def usage_summary_group():
    pass


@click.command(cli_util.override('usage_api.configuration_group.command_name', 'configuration'), cls=CommandGroupWithAlias, help="""A configuration""")
@cli_util.help_option_group
def configuration_group():
    pass


usage_api_root_group.add_command(usage_summary_group)
usage_api_root_group.add_command(configuration_group)


@configuration_group.command(name=cli_util.override('usage_api.request_summarized_configurations.command_name', 'request-summarized'), help=u"""Returns the list of config for UI dropdown list""")
@cli_util.option('--tenant-id', required=True, help=u"""tenant id""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage_api', 'class': 'ConfigurationAggregation'})
@cli_util.wrap_exceptions
def request_summarized_configurations(ctx, from_json, tenant_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.request_summarized_configurations(
        tenant_id=tenant_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@usage_summary_group.command(name=cli_util.override('usage_api.request_summarized_usages.command_name', 'request-summarized-usages'), help=u"""Returns the usage for the given account""")
@cli_util.option('--tenant-id', required=True, help=u"""tenant id""")
@cli_util.option('--time-usage-started', required=True, type=custom_types.CLI_DATETIME, help=u"""The start time of the usage.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-usage-ended', required=True, type=custom_types.CLI_DATETIME, help=u"""The end time of the usage.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--granularity', required=True, type=custom_types.CliCaseInsensitiveChoice(["HOURLY", "DAILY", "MONTHLY", "TOTAL"]), help=u"""The granularity of the usage. HOURLY - Hourly aggregation of data DAILY - Daily aggregation of data MONTHLY - Monthly aggregation of data TOTAL - Not Supported Yet""")
@cli_util.option('--query-type', type=custom_types.CliCaseInsensitiveChoice(["USAGE", "COST"]), help=u"""The type of query of the usage. Usage - Query the usage data. Cost - Query the cost / billing data.""")
@cli_util.option('--group-by', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Aggregate the result by. example:   `[\"service\"]`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-depth', type=click.FLOAT, help=u"""The depth level of the compartment.""")
@cli_util.option('--filter', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@json_skeleton_utils.get_cli_json_input_option({'group-by': {'module': 'usage_api', 'class': 'list[string]'}, 'filter': {'module': 'usage_api', 'class': 'Filter'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'group-by': {'module': 'usage_api', 'class': 'list[string]'}, 'filter': {'module': 'usage_api', 'class': 'Filter'}}, output_type={'module': 'usage_api', 'class': 'UsageAggregation'})
@cli_util.wrap_exceptions
def request_summarized_usages(ctx, from_json, tenant_id, time_usage_started, time_usage_ended, granularity, query_type, group_by, compartment_depth, filter, page, limit):

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['tenantId'] = tenant_id
    _details['timeUsageStarted'] = time_usage_started
    _details['timeUsageEnded'] = time_usage_ended
    _details['granularity'] = granularity

    if query_type is not None:
        _details['queryType'] = query_type

    if group_by is not None:
        _details['groupBy'] = cli_util.parse_json_parameter("group_by", group_by)

    if compartment_depth is not None:
        _details['compartmentDepth'] = compartment_depth

    if filter is not None:
        _details['filter'] = cli_util.parse_json_parameter("filter", filter)

    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.request_summarized_usages(
        request_summarized_usages_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
