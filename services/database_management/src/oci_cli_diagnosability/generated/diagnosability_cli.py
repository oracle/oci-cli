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
from services.database_management.src.oci_cli_database_management.generated import database_management_service_cli


@click.command(cli_util.override('diagnosability.diagnosability_root_group.command_name', 'diagnosability'), cls=CommandGroupWithAlias, help=cli_util.override('diagnosability.diagnosability_root_group.help', """Use the Database Management API to perform tasks such as obtaining performance and resource usage metrics
for a fleet of Managed Databases or a specific Managed Database, creating Managed Database Groups, and
running a SQL job on a Managed Database or Managed Database Group."""), short_help=cli_util.override('diagnosability.diagnosability_root_group.short_help', """Database Management API"""))
@cli_util.help_option_group
def diagnosability_root_group():
    pass


@click.command(cli_util.override('diagnosability.managed_database_group.command_name', 'managed-database'), cls=CommandGroupWithAlias, help="""The details of a Managed Database.""")
@cli_util.help_option_group
def managed_database_group():
    pass


database_management_service_cli.database_management_service_group.add_command(diagnosability_root_group)
diagnosability_root_group.add_command(managed_database_group)


@managed_database_group.command(name=cli_util.override('diagnosability.list_alert_logs.command_name', 'list-alert-logs'), help=u"""Lists the alert logs for the specified Managed Database. \n[Command Reference](listAlertLogs)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to timestamp to filter the logs.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to timestamp to filter the logs.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--level-filter', type=custom_types.CliCaseInsensitiveChoice(["CRITICAL", "SEVERE", "IMPORTANT", "NORMAL", "ALL"]), help=u"""The optional parameter to filter the alert logs by log level.""")
@cli_util.option('--type-filter', type=custom_types.CliCaseInsensitiveChoice(["UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", "ALL"]), help=u"""The optional parameter to filter the attention or alert logs by type.""")
@cli_util.option('--log-search-text', help=u"""The optional query parameter to filter the attention or alert logs by search text.""")
@cli_util.option('--is-regular-expression', type=click.BOOL, help=u"""The flag to indicate whether the search text is regular expression or not.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["LEVEL", "TYPE", "MESSAGE", "TIMESTAMP"]), help=u"""The possible sortBy values of attention logs.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AlertLogCollection'})
@cli_util.wrap_exceptions
def list_alert_logs(ctx, from_json, all_pages, page_size, managed_database_id, time_greater_than_or_equal_to, time_less_than_or_equal_to, level_filter, type_filter, log_search_text, is_regular_expression, sort_by, sort_order, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if level_filter is not None:
        kwargs['level_filter'] = level_filter
    if type_filter is not None:
        kwargs['type_filter'] = type_filter
    if log_search_text is not None:
        kwargs['log_search_text'] = log_search_text
    if is_regular_expression is not None:
        kwargs['is_regular_expression'] = is_regular_expression
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'diagnosability', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_alert_logs,
            managed_database_id=managed_database_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_alert_logs,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            **kwargs
        )
    else:
        result = client.list_alert_logs(
            managed_database_id=managed_database_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('diagnosability.list_attention_logs.command_name', 'list-attention-logs'), help=u"""Lists the attention logs for the specified Managed Database. \n[Command Reference](listAttentionLogs)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to timestamp to filter the logs.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to timestamp to filter the logs.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--urgency-filter', type=custom_types.CliCaseInsensitiveChoice(["IMMEDIATE", "SOON", "DEFERRABLE", "INFO", "ALL"]), help=u"""The optional parameter to filter the attention logs by urgency.""")
@cli_util.option('--type-filter', type=custom_types.CliCaseInsensitiveChoice(["UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", "ALL"]), help=u"""The optional parameter to filter the attention or alert logs by type.""")
@cli_util.option('--log-search-text', help=u"""The optional query parameter to filter the attention or alert logs by search text.""")
@cli_util.option('--is-regular-expression', type=click.BOOL, help=u"""The flag to indicate whether the search text is regular expression or not.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["URGENCY", "TYPE", "MESSAGE", "TIMESTAMP", "SCOPE", "TARGET_USER"]), help=u"""The possible sortBy values of attention logs.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AttentionLogCollection'})
@cli_util.wrap_exceptions
def list_attention_logs(ctx, from_json, all_pages, page_size, managed_database_id, time_greater_than_or_equal_to, time_less_than_or_equal_to, urgency_filter, type_filter, log_search_text, is_regular_expression, sort_by, sort_order, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if urgency_filter is not None:
        kwargs['urgency_filter'] = urgency_filter
    if type_filter is not None:
        kwargs['type_filter'] = type_filter
    if log_search_text is not None:
        kwargs['log_search_text'] = log_search_text
    if is_regular_expression is not None:
        kwargs['is_regular_expression'] = is_regular_expression
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'diagnosability', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_attention_logs,
            managed_database_id=managed_database_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_attention_logs,
            limit,
            page_size,
            managed_database_id=managed_database_id,
            **kwargs
        )
    else:
        result = client.list_attention_logs(
            managed_database_id=managed_database_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('diagnosability.summarize_alert_log_counts.command_name', 'summarize-alert-log-counts'), help=u"""Get the counts of alert logs for the specified Managed Database. \n[Command Reference](summarizeAlertLogCounts)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to timestamp to filter the logs.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to timestamp to filter the logs.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--level-filter', type=custom_types.CliCaseInsensitiveChoice(["CRITICAL", "SEVERE", "IMPORTANT", "NORMAL", "ALL"]), help=u"""The optional parameter to filter the alert logs by log level.""")
@cli_util.option('--group-by', type=custom_types.CliCaseInsensitiveChoice(["LEVEL", "TYPE"]), help=u"""The optional parameter used to group different alert logs.""")
@cli_util.option('--type-filter', type=custom_types.CliCaseInsensitiveChoice(["UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", "ALL"]), help=u"""The optional parameter to filter the attention or alert logs by type.""")
@cli_util.option('--log-search-text', help=u"""The optional query parameter to filter the attention or alert logs by search text.""")
@cli_util.option('--is-regular-expression', type=click.BOOL, help=u"""The flag to indicate whether the search text is regular expression or not.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AlertLogCountsCollection'})
@cli_util.wrap_exceptions
def summarize_alert_log_counts(ctx, from_json, managed_database_id, time_greater_than_or_equal_to, time_less_than_or_equal_to, level_filter, group_by, type_filter, log_search_text, is_regular_expression, page, limit):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if level_filter is not None:
        kwargs['level_filter'] = level_filter
    if group_by is not None:
        kwargs['group_by'] = group_by
    if type_filter is not None:
        kwargs['type_filter'] = type_filter
    if log_search_text is not None:
        kwargs['log_search_text'] = log_search_text
    if is_regular_expression is not None:
        kwargs['is_regular_expression'] = is_regular_expression
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'diagnosability', ctx)
    result = client.summarize_alert_log_counts(
        managed_database_id=managed_database_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_database_group.command(name=cli_util.override('diagnosability.summarize_attention_log_counts.command_name', 'summarize-attention-log-counts'), help=u"""Get the counts of attention logs for the specified Managed Database. \n[Command Reference](summarizeAttentionLogCounts)""")
@cli_util.option('--managed-database-id', required=True, help=u"""The [OCID] of the Managed Database.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to timestamp to filter the logs.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to timestamp to filter the logs.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--urgency-filter', type=custom_types.CliCaseInsensitiveChoice(["IMMEDIATE", "SOON", "DEFERRABLE", "INFO", "ALL"]), help=u"""The optional parameter to filter the attention logs by urgency.""")
@cli_util.option('--group-by', type=custom_types.CliCaseInsensitiveChoice(["URGENCY", "TYPE"]), help=u"""The optional parameter used to group different attention logs.""")
@cli_util.option('--type-filter', type=custom_types.CliCaseInsensitiveChoice(["UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", "ALL"]), help=u"""The optional parameter to filter the attention or alert logs by type.""")
@cli_util.option('--log-search-text', help=u"""The optional query parameter to filter the attention or alert logs by search text.""")
@cli_util.option('--is-regular-expression', type=click.BOOL, help=u"""The flag to indicate whether the search text is regular expression or not.""")
@cli_util.option('--page', help=u"""The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of records returned in the paginated response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_management', 'class': 'AttentionLogCountsCollection'})
@cli_util.wrap_exceptions
def summarize_attention_log_counts(ctx, from_json, managed_database_id, time_greater_than_or_equal_to, time_less_than_or_equal_to, urgency_filter, group_by, type_filter, log_search_text, is_regular_expression, page, limit):

    if isinstance(managed_database_id, six.string_types) and len(managed_database_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-database-id cannot be whitespace or empty string')

    kwargs = {}
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if urgency_filter is not None:
        kwargs['urgency_filter'] = urgency_filter
    if group_by is not None:
        kwargs['group_by'] = group_by
    if type_filter is not None:
        kwargs['type_filter'] = type_filter
    if log_search_text is not None:
        kwargs['log_search_text'] = log_search_text
    if is_regular_expression is not None:
        kwargs['is_regular_expression'] = is_regular_expression
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_management', 'diagnosability', ctx)
    result = client.summarize_attention_log_counts(
        managed_database_id=managed_database_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)
