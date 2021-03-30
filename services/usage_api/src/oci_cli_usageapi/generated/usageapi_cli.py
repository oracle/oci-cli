# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('usage_api.usage_api_root_group.command_name', 'usage-api'), cls=CommandGroupWithAlias, help=cli_util.override('usage_api.usage_api_root_group.help', """Use the Usage API to view your Oracle Cloud usage and costs. The API allows you to request data that meets the specified filter criteria, and to group that data by the dimension of your choosing. The Usage API is used by the Cost Analysis tool in the Console. Also see [Using the Usage API] for more information."""), short_help=cli_util.override('usage_api.usage_api_root_group.short_help', """Usage API"""))
@cli_util.help_option_group
def usage_api_root_group():
    pass


@click.command(cli_util.override('usage_api.usage_summary_group.command_name', 'usage-summary'), cls=CommandGroupWithAlias, help="""The usage store result.""")
@cli_util.help_option_group
def usage_summary_group():
    pass


@click.command(cli_util.override('usage_api.configuration_group.command_name', 'configuration'), cls=CommandGroupWithAlias, help="""A configuration.""")
@cli_util.help_option_group
def configuration_group():
    pass


@click.command(cli_util.override('usage_api.query_group.command_name', 'query'), cls=CommandGroupWithAlias, help="""The query to filter and aggregate.""")
@cli_util.help_option_group
def query_group():
    pass


usage_api_root_group.add_command(usage_summary_group)
usage_api_root_group.add_command(configuration_group)
usage_api_root_group.add_command(query_group)


@query_group.command(name=cli_util.override('usage_api.create_query.command_name', 'create'), help=u"""Returns the created query. \n[Command Reference](createQuery)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment OCID.""")
@cli_util.option('--query-definition', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'query-definition': {'module': 'usage_api', 'class': 'QueryDefinition'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'query-definition': {'module': 'usage_api', 'class': 'QueryDefinition'}}, output_type={'module': 'usage_api', 'class': 'Query'})
@cli_util.wrap_exceptions
def create_query(ctx, from_json, compartment_id, query_definition):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['queryDefinition'] = cli_util.parse_json_parameter("query_definition", query_definition)

    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.create_query(
        create_query_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@query_group.command(name=cli_util.override('usage_api.delete_query.command_name', 'delete'), help=u"""Delete a saved query by the OCID. \n[Command Reference](deleteQuery)""")
@cli_util.option('--query-id', required=True, help=u"""The query unique OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_query(ctx, from_json, query_id, if_match):

    if isinstance(query_id, six.string_types) and len(query_id.strip()) == 0:
        raise click.UsageError('Parameter --query-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.delete_query(
        query_id=query_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@query_group.command(name=cli_util.override('usage_api.get_query.command_name', 'get'), help=u"""Returns the saved query. \n[Command Reference](getQuery)""")
@cli_util.option('--query-id', required=True, help=u"""The query unique OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage_api', 'class': 'Query'})
@cli_util.wrap_exceptions
def get_query(ctx, from_json, query_id):

    if isinstance(query_id, six.string_types) and len(query_id.strip()) == 0:
        raise click.UsageError('Parameter --query-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.get_query(
        query_id=query_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@query_group.command(name=cli_util.override('usage_api.list_queries.command_name', 'list'), help=u"""Returns the saved query list. \n[Command Reference](listQueries)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment ID in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximumimum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName"]), help=u"""The field to sort by. If not specified, the default is displayName.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage_api', 'class': 'QueryCollection'})
@cli_util.wrap_exceptions
def list_queries(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_queries,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_queries,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_queries(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@configuration_group.command(name=cli_util.override('usage_api.request_summarized_configurations.command_name', 'request-summarized'), help=u"""Returns the configurations list for the UI drop-down list. \n[Command Reference](requestSummarizedConfigurations)""")
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


@usage_summary_group.command(name=cli_util.override('usage_api.request_summarized_usages.command_name', 'request-summarized-usages'), help=u"""Returns usage for the given account. \n[Command Reference](requestSummarizedUsages)""")
@cli_util.option('--tenant-id', required=True, help=u"""Tenant ID.""")
@cli_util.option('--time-usage-started', required=True, type=custom_types.CLI_DATETIME, help=u"""The usage start time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-usage-ended', required=True, type=custom_types.CLI_DATETIME, help=u"""The usage end time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--granularity', required=True, type=custom_types.CliCaseInsensitiveChoice(["HOURLY", "DAILY", "MONTHLY", "TOTAL"]), help=u"""The usage granularity. HOURLY - Hourly data aggregation. DAILY - Daily data aggregation. MONTHLY - Monthly data aggregation. TOTAL - Not yet supported.""")
@cli_util.option('--is-aggregate-by-time', type=click.BOOL, help=u"""is aggregated by time. true isAggregateByTime will add up all usage/cost over query time period""")
@cli_util.option('--forecast', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--query-type', type=custom_types.CliCaseInsensitiveChoice(["USAGE", "COST"]), help=u"""The query usage type. COST by default if it is missing Usage - Query the usage data. Cost - Query the cost/billing data.""")
@cli_util.option('--group-by', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Aggregate the result by. example:   `[\"tagNamespace\", \"tagKey\", \"tagValue\", \"service\", \"skuName\", \"skuPartNumber\", \"unit\",     \"compartmentName\", \"compartmentPath\", \"compartmentId\", \"platform\", \"region\", \"logicalAd\",     \"resourceId\", \"tenantId\", \"tenantName\"]`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--group-by-tag', type=custom_types.CLI_COMPLEX_TYPE, help=u"""GroupBy a specific tagKey. Provide tagNamespace and tagKey in tag object. Only support one tag in the list example:   `[{\"namespace\":\"oracle\", \"key\":\"createdBy\"]`

This option is a JSON list with items of type Tag.  For documentation on Tag please see our API reference: https://docs.cloud.oracle.com/api/#/en/usageapi/20200107/datatypes/Tag.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-depth', type=click.FLOAT, help=u"""The compartment depth level.""")
@cli_util.option('--filter', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximumimum number of items to return.""")
@json_skeleton_utils.get_cli_json_input_option({'forecast': {'module': 'usage_api', 'class': 'Forecast'}, 'group-by': {'module': 'usage_api', 'class': 'list[string]'}, 'group-by-tag': {'module': 'usage_api', 'class': 'list[Tag]'}, 'filter': {'module': 'usage_api', 'class': 'Filter'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'forecast': {'module': 'usage_api', 'class': 'Forecast'}, 'group-by': {'module': 'usage_api', 'class': 'list[string]'}, 'group-by-tag': {'module': 'usage_api', 'class': 'list[Tag]'}, 'filter': {'module': 'usage_api', 'class': 'Filter'}}, output_type={'module': 'usage_api', 'class': 'UsageAggregation'})
@cli_util.wrap_exceptions
def request_summarized_usages(ctx, from_json, tenant_id, time_usage_started, time_usage_ended, granularity, is_aggregate_by_time, forecast, query_type, group_by, group_by_tag, compartment_depth, filter, page, limit):

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

    if is_aggregate_by_time is not None:
        _details['isAggregateByTime'] = is_aggregate_by_time

    if forecast is not None:
        _details['forecast'] = cli_util.parse_json_parameter("forecast", forecast)

    if query_type is not None:
        _details['queryType'] = query_type

    if group_by is not None:
        _details['groupBy'] = cli_util.parse_json_parameter("group_by", group_by)

    if group_by_tag is not None:
        _details['groupByTag'] = cli_util.parse_json_parameter("group_by_tag", group_by_tag)

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


@query_group.command(name=cli_util.override('usage_api.update_query.command_name', 'update'), help=u"""Update a saved query by the OCID. \n[Command Reference](updateQuery)""")
@cli_util.option('--query-definition', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--query-id', required=True, help=u"""The query unique OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'query-definition': {'module': 'usage_api', 'class': 'QueryDefinition'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'query-definition': {'module': 'usage_api', 'class': 'QueryDefinition'}}, output_type={'module': 'usage_api', 'class': 'Query'})
@cli_util.wrap_exceptions
def update_query(ctx, from_json, force, query_definition, query_id, if_match):

    if isinstance(query_id, six.string_types) and len(query_id.strip()) == 0:
        raise click.UsageError('Parameter --query-id cannot be whitespace or empty string')
    if not force:
        if query_definition:
            if not click.confirm("WARNING: Updates to query-definition will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['queryDefinition'] = cli_util.parse_json_parameter("query_definition", query_definition)

    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.update_query(
        query_id=query_id,
        update_query_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
