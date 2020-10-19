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


@cli.command(cli_util.override('opsi.opsi_root_group.command_name', 'opsi'), cls=CommandGroupWithAlias, help=cli_util.override('opsi.opsi_root_group.help', """Use the Operations Insights API to perform data extraction operations to obtain database
resource utilization, performance statistics, and reference information. For more information,
see [About Oracle Cloud Infrastructure Operations Insights]."""), short_help=cli_util.override('opsi.opsi_root_group.short_help', """Operations Insights API"""))
@cli_util.help_option_group
def opsi_root_group():
    pass


@click.command(cli_util.override('opsi.database_insights_group.command_name', 'database-insights'), cls=CommandGroupWithAlias, help="""Logical grouping used for Operations Insights database-targeted operations.""")
@cli_util.help_option_group
def database_insights_group():
    pass


opsi_root_group.add_command(database_insights_group)


@database_insights_group.command(name=cli_util.override('opsi.ingest_sql_bucket.command_name', 'ingest-sql-bucket'), help=u"""The sqlbucket endpoint takes in a JSON payload, persists it in Operations Insights ingest pipeline. \n[Command Reference](ingestSqlBucket)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-id', required=True, help=u"""Required [OCID] of the database.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of SQL Bucket Metric Entries.

This option is a JSON list with items of type SqlBucket.  For documentation on SqlBucket please see our API reference: https://docs.cloud.oracle.com/api/#/en/operationsinsights/20200630/datatypes/SqlBucket.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'opsi', 'class': 'list[SqlBucket]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'opsi', 'class': 'list[SqlBucket]'}}, output_type={'module': 'opsi', 'class': 'IngestSqlBucketResponseDetails'})
@cli_util.wrap_exceptions
def ingest_sql_bucket(ctx, from_json, compartment_id, database_id, items, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.ingest_sql_bucket(
        compartment_id=compartment_id,
        database_id=database_id,
        ingest_sql_bucket_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.ingest_sql_plan_lines.command_name', 'ingest-sql-plan-lines'), help=u"""The SqlPlanLines endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline. \n[Command Reference](ingestSqlPlanLines)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-id', required=True, help=u"""Required [OCID] of the database.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of SQL Plan Line Entries.

This option is a JSON list with items of type SqlPlanLine.  For documentation on SqlPlanLine please see our API reference: https://docs.cloud.oracle.com/api/#/en/operationsinsights/20200630/datatypes/SqlPlanLine.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'opsi', 'class': 'list[SqlPlanLine]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'opsi', 'class': 'list[SqlPlanLine]'}}, output_type={'module': 'opsi', 'class': 'IngestSqlPlanLinesResponseDetails'})
@cli_util.wrap_exceptions
def ingest_sql_plan_lines(ctx, from_json, compartment_id, database_id, items, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.ingest_sql_plan_lines(
        compartment_id=compartment_id,
        database_id=database_id,
        ingest_sql_plan_lines_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.ingest_sql_text.command_name', 'ingest-sql-text'), help=u"""The SqlText endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline. Disclaimer: SQL text being uploaded explicitly via APIs is not masked. Any sensitive literals contained in the sqlFullText column should be masked prior to ingestion. \n[Command Reference](ingestSqlText)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-id', required=True, help=u"""Required [OCID] of the database.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of SQL Text Entries.

This option is a JSON list with items of type SqlText.  For documentation on SqlText please see our API reference: https://docs.cloud.oracle.com/api/#/en/operationsinsights/20200630/datatypes/SqlText.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'opsi', 'class': 'list[SqlText]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'opsi', 'class': 'list[SqlText]'}}, output_type={'module': 'opsi', 'class': 'IngestSqlTextResponseDetails'})
@cli_util.wrap_exceptions
def ingest_sql_text(ctx, from_json, compartment_id, database_id, items, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.ingest_sql_text(
        compartment_id=compartment_id,
        database_id=database_id,
        ingest_sql_text_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.list_database_insights.command_name', 'list'), help=u"""Lists database insight resources \n[Command Reference](listDatabaseInsights)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs].""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["compartmentId", "databaseName", "databaseDisplayName", "databaseType", "databaseVersion", "databaseHostNames", "freeformTags", "definedTags"]), multiple=True, help=u"""Specifies the fields to return in a database summary response. By default all fields are returned if omitted.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["databaseName", "databaseDisplayName", "databaseType"]), help=u"""Database insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'DatabaseInsightsCollection'})
@cli_util.wrap_exceptions
def list_database_insights(ctx, from_json, all_pages, page_size, compartment_id, database_type, database_id, fields, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_database_insights,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_database_insights,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_database_insights(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.list_sql_plans.command_name', 'list-sql-plans'), help=u"""Query SQL Warehouse to list the plan xml for a given SQL execution plan. This returns a SqlPlanCollection object, but is currently limited to a single plan. \n[Command Reference](listSqlPlans)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-id', required=True, help=u"""Required [OCID] of the database.""")
@cli_util.option('--sql-identifier', required=True, help=u"""Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--plan-hash', required=True, multiple=True, help=u"""Unique plan hash for a SQL Plan of a particular SQL Statement. Example: `9820154385`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({'plan-hash': {'module': 'opsi', 'class': 'list[integer]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'plan-hash': {'module': 'opsi', 'class': 'list[integer]'}}, output_type={'module': 'opsi', 'class': 'SqlPlanCollection'})
@cli_util.wrap_exceptions
def list_sql_plans(ctx, from_json, all_pages, compartment_id, database_id, sql_identifier, plan_hash, page):

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        result = cli_util.list_call_get_all_results(
            client.list_sql_plans,
            compartment_id=compartment_id,
            database_id=database_id,
            sql_identifier=sql_identifier,
            plan_hash=plan_hash,
            **kwargs
        )
    else:
        result = client.list_sql_plans(
            compartment_id=compartment_id,
            database_id=database_id,
            sql_identifier=sql_identifier,
            plan_hash=plan_hash,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.list_sql_searches.command_name', 'list-sql-searches'), help=u"""Search SQL by SQL Identifier across databases and get the SQL Text and the details of the databases executing the SQL for a given time period. \n[Command Reference](listSqlSearches)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--sql-identifier', required=True, help=u"""Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'SqlSearchCollection'})
@cli_util.wrap_exceptions
def list_sql_searches(ctx, from_json, all_pages, compartment_id, sql_identifier, analysis_time_interval, time_interval_start, time_interval_end, page):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        result = cli_util.list_call_get_all_results(
            client.list_sql_searches,
            compartment_id=compartment_id,
            sql_identifier=sql_identifier,
            **kwargs
        )
    else:
        result = client.list_sql_searches(
            compartment_id=compartment_id,
            sql_identifier=sql_identifier,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.list_sql_texts.command_name', 'list-sql-texts'), help=u"""Query SQL Warehouse to get the full SQL Text for a SQL. \n[Command Reference](listSqlTexts)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--sql-identifier', required=True, multiple=True, help=u"""One or more unique SQL_IDs for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({'sql-identifier': {'module': 'opsi', 'class': 'list[string]'}, 'database-id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'sql-identifier': {'module': 'opsi', 'class': 'list[string]'}, 'database-id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SqlTextCollection'})
@cli_util.wrap_exceptions
def list_sql_texts(ctx, from_json, all_pages, compartment_id, sql_identifier, database_id, page):

    kwargs = {}
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        result = cli_util.list_call_get_all_results(
            client.list_sql_texts,
            compartment_id=compartment_id,
            sql_identifier=sql_identifier,
            **kwargs
        )
    else:
        result = client.list_sql_texts(
            compartment_id=compartment_id,
            sql_identifier=sql_identifier,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_capacity_trend.command_name', 'summarize-database-insight-resource-capacity-trend'), help=u"""Returns response with time series data (endTimestamp, capacity, baseCapacity) for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. \n[Command Reference](summarizeDatabaseInsightResourceCapacityTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU and STORAGE.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs].""")
@cli_util.option('--utilization-level', type=custom_types.CliCaseInsensitiveChoice(["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]), help=u"""Filter by utilization level by the following buckets:   - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.   - LOW_UTILIZATION: DBs with utilization lower than 25.   - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.   - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["endTimestamp", "capacity", "baseCapacity"]), help=u"""Sorts using end timestamp , capacity or baseCapacity""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_capacity_trend(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, utilization_level, page, sort_order, sort_by):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if utilization_level is not None:
        kwargs['utilization_level'] = utilization_level
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_capacity_trend(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_forecast_trend.command_name', 'summarize-database-insight-resource-forecast-trend'), help=u"""Get Forecast predictions for CPU and Storage resources since a time in the past. \n[Command Reference](summarizeDatabaseInsightResourceForecastTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU and STORAGE.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs].""")
@cli_util.option('--statistic', type=custom_types.CliCaseInsensitiveChoice(["AVG", "MAX"]), help=u"""Choose the type of statistic metric data to be used for forecasting.""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--forecast-model', type=custom_types.CliCaseInsensitiveChoice(["LINEAR", "ML_AUTO", "ML_NO_AUTO"]), help=u"""Choose algorithm model for the forecasting. Possible values:   - LINEAR: Uses linear regression algorithm for forecasting.   - ML_AUTO: Automatically detects best algorithm to use for forecasting.   - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.""")
@cli_util.option('--utilization-level', type=custom_types.CliCaseInsensitiveChoice(["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]), help=u"""Filter by utilization level by the following buckets:   - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.   - LOW_UTILIZATION: DBs with utilization lower than 25.   - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.   - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.""")
@cli_util.option('--confidence', type=click.INT, help=u"""This parameter is used to change data's confidence level, this data is ingested by the forecast algorithm. Confidence is the probability of an interval to contain the expected population parameter. Manipulation of this value will lead to different results. If not set, default confidence value is 95%.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceForecastTrendAggregation'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_forecast_trend(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, statistic, forecast_days, forecast_model, utilization_level, confidence, page):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if statistic is not None:
        kwargs['statistic'] = statistic
    if forecast_days is not None:
        kwargs['forecast_days'] = forecast_days
    if forecast_model is not None:
        kwargs['forecast_model'] = forecast_model
    if utilization_level is not None:
        kwargs['utilization_level'] = utilization_level
    if confidence is not None:
        kwargs['confidence'] = confidence
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_forecast_trend(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_statistics.command_name', 'summarize-database-insight-resource-statistics'), help=u"""Lists the Resource statistics (usage,capacity, usage change percent, utilization percent, base capacity, isAutoScalingEnabled) for each database filtered by utilization level \n[Command Reference](summarizeDatabaseInsightResourceStatistics)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU and STORAGE.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs].""")
@cli_util.option('--percentile', type=click.INT, help=u"""Percentile values of daily usage to be used for computing the aggregate resource usage.""")
@cli_util.option('--insight-by', help=u"""Return data of a specific insight Possible values are High Utilization, Low Utilization, Any ,High Utilization Forecast, Low Utilization Forecast""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["utilizationPercent", "usage", "usageChangePercent", "databaseName", "databaseType"]), help=u"""The order in which resource statistics records are listed""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceStatisticsAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_statistics(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, percentile, insight_by, forecast_days, limit, page, sort_order, sort_by):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if percentile is not None:
        kwargs['percentile'] = percentile
    if insight_by is not None:
        kwargs['insight_by'] = insight_by
    if forecast_days is not None:
        kwargs['forecast_days'] = forecast_days
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_statistics(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_usage.command_name', 'summarize-database-insight-resource-usage'), help=u"""A cumulative distribution function is used to rank the usage data points per database within the specified time period. For each database, the minimum data point with a ranking > the percentile value is included in the summation. Linear regression functions are used to calculate the usage change percentage. \n[Command Reference](summarizeDatabaseInsightResourceUsage)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU and STORAGE.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--percentile', type=click.INT, help=u"""Percentile values of daily usage to be used for computing the aggregate resource usage.""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceUsageAggregation'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_usage(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, page, percentile):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if page is not None:
        kwargs['page'] = page
    if percentile is not None:
        kwargs['percentile'] = percentile
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_usage(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_usage_trend.command_name', 'summarize-database-insight-resource-usage-trend'), help=u"""Returns response with time series data (endTimestamp, usage, capacity) for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. \n[Command Reference](summarizeDatabaseInsightResourceUsageTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU and STORAGE.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["endTimestamp", "usage", "capacity"]), help=u"""Sorts using end timestamp, usage or capacity""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceUsageTrendAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_usage_trend(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, page, sort_order, sort_by):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_usage_trend(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_utilization_insight.command_name', 'summarize-database-insight-resource-utilization-insight'), help=u"""Gets resources with current utilization (high and low) and projected utilization (high and low) for a resource type over specified time period. \n[Command Reference](summarizeDatabaseInsightResourceUtilizationInsight)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU and STORAGE.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs].""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceUtilizationInsightAggregation'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_utilization_insight(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, forecast_days, page):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if forecast_days is not None:
        kwargs['forecast_days'] = forecast_days
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_utilization_insight(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_sql_insights.command_name', 'summarize-sql-insights'), help=u"""Query SQL Warehouse to get the performance insights for SQLs taking greater than X% database time for a given time period across the given databases or database types. \n[Command Reference](summarizeSqlInsights)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs].""")
@cli_util.option('--database-time-pct-greater-than', help=u"""Filter sqls by percentage of db time.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SqlInsightAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_sql_insights(ctx, from_json, compartment_id, database_type, database_id, database_time_pct_greater_than, analysis_time_interval, time_interval_start, time_interval_end, page):

    kwargs = {}
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if database_time_pct_greater_than is not None:
        kwargs['database_time_pct_greater_than'] = database_time_pct_greater_than
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_sql_insights(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_sql_plan_insights.command_name', 'summarize-sql-plan-insights'), help=u"""Query SQL Warehouse to get the performance insights on the execution plans for a given SQL for a given time period. \n[Command Reference](summarizeSqlPlanInsights)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-id', required=True, help=u"""Required [OCID] of the database.""")
@cli_util.option('--sql-identifier', required=True, help=u"""Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'SqlPlanInsightAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_sql_plan_insights(ctx, from_json, compartment_id, database_id, sql_identifier, analysis_time_interval, time_interval_start, time_interval_end, page):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_sql_plan_insights(
        compartment_id=compartment_id,
        database_id=database_id,
        sql_identifier=sql_identifier,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_sql_response_time_distributions.command_name', 'summarize-sql-response-time-distributions'), help=u"""Query SQL Warehouse to summarize the response time distribution of query executions for a given SQL for a given time period. \n[Command Reference](summarizeSqlResponseTimeDistributions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-id', required=True, help=u"""Required [OCID] of the database.""")
@cli_util.option('--sql-identifier', required=True, help=u"""Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'SqlResponseTimeDistributionAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_sql_response_time_distributions(ctx, from_json, compartment_id, database_id, sql_identifier, analysis_time_interval, time_interval_start, time_interval_end, page):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_sql_response_time_distributions(
        compartment_id=compartment_id,
        database_id=database_id,
        sql_identifier=sql_identifier,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_sql_statistics.command_name', 'summarize-sql-statistics'), help=u"""Query SQL Warehouse to get the performance statistics for SQLs taking greater than X% database time for a given time period across the given databases or database types. \n[Command Reference](summarizeSqlStatistics)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs].""")
@cli_util.option('--database-time-pct-greater-than', help=u"""Filter sqls by percentage of db time.""")
@cli_util.option('--sql-identifier', multiple=True, help=u"""One or more unique SQL_IDs for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["databaseTimeInSec", "executionsPerHour", "executionsCount", "cpuTimeInSec", "ioTimeInSec", "inefficientWaitTimeInSec", "responseTimeInSec", "planCount", "variability", "averageActiveSessions", "databaseTimePct", "inefficiencyInPct", "changeInCpuTimeInPct", "changeInIoTimeInPct", "changeInInefficientWaitTimeInPct", "changeInResponseTimeInPct", "changeInAverageActiveSessionsInPct", "changeInExecutionsPerHourInPct", "changeInInefficiencyInPct"]), help=u"""The field to use when sorting SQL statistics. Example: databaseTimeInSec""")
@cli_util.option('--category', type=custom_types.CliCaseInsensitiveChoice(["DEGRADING", "VARIANT", "INEFFICIENT", "CHANGING_PLANS", "DEGRADING_VARIANT", "DEGRADING_INEFFICIENT", "DEGRADING_CHANGING_PLANS", "DEGRADING_INCREASING_IO", "DEGRADING_INCREASING_CPU", "DEGRADING_INCREASING_INEFFICIENT_WAIT", "DEGRADING_CHANGING_PLANS_AND_INCREASING_IO", "DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU", "DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "VARIANT_INEFFICIENT", "VARIANT_CHANGING_PLANS", "VARIANT_INCREASING_IO", "VARIANT_INCREASING_CPU", "VARIANT_INCREASING_INEFFICIENT_WAIT", "VARIANT_CHANGING_PLANS_AND_INCREASING_IO", "VARIANT_CHANGING_PLANS_AND_INCREASING_CPU", "VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS", "INEFFICIENT_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT"]), multiple=True, help=u"""Filter sqls by one or more performance categories.""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'sql-identifier': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'sql-identifier': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SqlStatisticAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_sql_statistics(ctx, from_json, compartment_id, database_type, database_id, database_time_pct_greater_than, sql_identifier, analysis_time_interval, time_interval_start, time_interval_end, limit, page, sort_order, sort_by, category):

    kwargs = {}
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if database_time_pct_greater_than is not None:
        kwargs['database_time_pct_greater_than'] = database_time_pct_greater_than
    if sql_identifier is not None and len(sql_identifier) > 0:
        kwargs['sql_identifier'] = sql_identifier
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if category is not None and len(category) > 0:
        kwargs['category'] = category
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_sql_statistics(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_sql_statistics_time_series.command_name', 'summarize-sql-statistics-time-series'), help=u"""Query SQL Warehouse to get the performance statistics time series for a given SQL across given databases for a given time period. \n[Command Reference](summarizeSqlStatisticsTimeSeries)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--sql-identifier', required=True, help=u"""Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs].""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SqlStatisticsTimeSeriesAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_sql_statistics_time_series(ctx, from_json, compartment_id, sql_identifier, database_id, analysis_time_interval, time_interval_start, time_interval_end, page):

    kwargs = {}
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_sql_statistics_time_series(
        compartment_id=compartment_id,
        sql_identifier=sql_identifier,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_sql_statistics_time_series_by_plan.command_name', 'summarize-sql-statistics-time-series-by-plan'), help=u"""Query SQL Warehouse to get the performance statistics time series for a given SQL by execution plans for a given time period. \n[Command Reference](summarizeSqlStatisticsTimeSeriesByPlan)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-id', required=True, help=u"""Required [OCID] of the database.""")
@cli_util.option('--sql-identifier', required=True, help=u"""Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'SqlStatisticsTimeSeriesByPlanAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_sql_statistics_time_series_by_plan(ctx, from_json, compartment_id, database_id, sql_identifier, analysis_time_interval, time_interval_start, time_interval_end, page):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_sql_statistics_time_series_by_plan(
        compartment_id=compartment_id,
        database_id=database_id,
        sql_identifier=sql_identifier,
        **kwargs
    )
    cli_util.render_response(result, ctx)
