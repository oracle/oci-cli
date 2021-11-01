# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.apm_traces.src.oci_cli_query.generated import query_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci apm-traces query query-result-response -> oci apm-traces query query-response
cli_util.rename_command(query_cli, query_cli.query_root_group, query_cli.query_result_response_group, "query-response")


# oci apm-traces query query-result-response query -> oci apm-traces query query-result-response run-query
cli_util.rename_command(query_cli, query_cli.query_result_response_group, query_cli.query, "run-query")


# oci apm-traces query quick-pick-summary -> oci apm-traces query quick-picks
cli_util.rename_command(query_cli, query_cli.query_root_group, query_cli.quick_pick_summary_group, "quick-picks")


@cli_util.copy_params_from_generated_command(query_cli.query, params_to_exclude=['time_span_started_greater_than_or_equal_to', 'time_span_started_less_than'])
@query_cli.query_result_response_group.command(name=query_cli.query.name, help=query_cli.query.help)
@cli_util.option('--start-time-gte', required=True, type=custom_types.CLI_DATETIME, help=u"""Include spans that have a `spanStartTime` equal to or greater this value.

The following datetime formats are supported:

UTC with milliseconds
***********************
Format: YYYY-MM-DDTHH:mm:ss.sssTZD
Example: 2017-09-15T20:30:00.123Z

UTC without milliseconds
**************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example: 2017-09-15T20:30:00Z

UTC with minute precision
**************************
Format: YYYY-MM-DDTHH:mmTZD
Example: 2017-09-15T20:30Z

Timezone with milliseconds
***************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00.456-08:00,
2017-09-15T12:30:00.456-0800

Timezone without milliseconds
*******************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00-08:00,
2017-09-15T12:30:00-0800

Timezone with minute precision
*******************************
Format: YYYY-MM-DDTHH:mmTZD
Example:
2017-09-15T12:30-08:00,
2017-09-15T12:30-0800

Short date and time
********************
The timezone for this date and time will be taken as UTC (Needs to be surrounded by single or double quotes)
Format: 'YYYY-MM-DD HH:mm' or "YYYY-MM-DD HH:mm"
Example: '2017-09-15 17:25'

Date Only
*********
This date will be taken as midnight UTC of that day
Format: YYYY-MM-DD
Example: 2017-09-15

Epoch seconds
**************
Example: 1412195400
    [required]""")
@cli_util.option('--start-time-lt', required=True, type=custom_types.CLI_DATETIME, help=u"""Include spans that have a `spanStartTime`less than this value.

The following datetime formats are supported:

UTC with milliseconds
***********************
Format: YYYY-MM-DDTHH:mm:ss.sssTZD
Example: 2017-09-15T20:30:00.123Z

UTC without milliseconds
**************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example: 2017-09-15T20:30:00Z

UTC with minute precision
**************************
Format: YYYY-MM-DDTHH:mmTZD
Example: 2017-09-15T20:30Z

Timezone with milliseconds
***************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00.456-08:00,
2017-09-15T12:30:00.456-0800

Timezone without milliseconds
*******************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00-08:00,
2017-09-15T12:30:00-0800

Timezone with minute precision
*******************************
Format: YYYY-MM-DDTHH:mmTZD
Example:
2017-09-15T12:30-08:00,
2017-09-15T12:30-0800

Short date and time
********************
The timezone for this date and time will be taken as UTC (Needs to be surrounded by single or double quotes)
Format: 'YYYY-MM-DD HH:mm' or "YYYY-MM-DD HH:mm"
Example: '2017-09-15 17:25'

Date Only
*********
This date will be taken as midnight UTC of that day
Format: YYYY-MM-DD
Example: 2017-09-15

Epoch seconds
**************
Example: 1412195400
    [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_traces', 'class': 'QueryResultResponse'})
@cli_util.wrap_exceptions
def query_extended(ctx, **kwargs):
    if 'start_time_gte' in kwargs:
        kwargs['time_span_started_greater_than_or_equal_to'] = kwargs['start_time_gte']
        kwargs.pop('start_time_gte')

    if 'start_time_lt' in kwargs:
        kwargs['time_span_started_less_than'] = kwargs['start_time_lt']
        kwargs.pop('start_time_lt')

    ctx.invoke(query_cli.query, **kwargs)


# oci apm-traces query quick-picks list-quick-picks -> oci apm-traces query quick-picks list
cli_util.rename_command(query_cli, query_cli.quick_pick_summary_group, query_cli.list_quick_picks, "list")
