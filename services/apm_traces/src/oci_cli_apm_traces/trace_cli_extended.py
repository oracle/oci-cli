# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click  # noqa: F401
import json  # noqa: F401
from services.apm_traces.src.oci_cli_trace.generated import trace_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


@cli_util.copy_params_from_generated_command(trace_cli.get_span, params_to_exclude=['time_span_started_greater_than_or_equal_to', 'time_span_started_less_than'])
@trace_cli.span_group.command(name=trace_cli.get_span.name, help=trace_cli.get_span.help)
@cli_util.option('--time-span-started-gte', type=custom_types.CLI_DATETIME, help=u"""Include spans that have a `spanStartTime` equal to or greater than this value.

The following datetime formats are supported:

UTC with microseconds
***********************
Format: YYYY-MM-DDTHH:mm:ss.ssssssTZD
Example: 2017-09-15T20:30:00.123456Z
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
Timezone with microseconds
***************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00.456789-08:00,
2017-09-15T12:30:00.456789-0800
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
    """)
@cli_util.option('--time-span-started-lt', type=custom_types.CLI_DATETIME, help=u"""Include spans that have a `spanStartTime`less than this value.

The following datetime formats are supported:

UTC with microseconds
***********************
Format: YYYY-MM-DDTHH:mm:ss.ssssssTZD
Example: 2017-09-15T20:30:00.123456Z
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
Timezone with microseconds
***************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00.456789-08:00,
2017-09-15T12:30:00.456789-0800
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
    """)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_traces', 'class': 'Span'})
@cli_util.wrap_exceptions
def get_span_extended(ctx, **kwargs):
    if 'time_span_started_gte' in kwargs:
        kwargs['time_span_started_greater_than_or_equal_to'] = kwargs['time_span_started_gte']
        kwargs.pop('time_span_started_gte')
    if 'time_span_started_lt' in kwargs:
        kwargs['time_span_started_less_than'] = kwargs['time_span_started_lt']
        kwargs.pop('time_span_started_lt')
    ctx.invoke(trace_cli.get_span, **kwargs)


@cli_util.copy_params_from_generated_command(trace_cli.get_trace, params_to_exclude=['time_trace_started_greater_than_or_equal_to', 'time_trace_started_less_than'])
@trace_cli.trace_group.command(name=trace_cli.get_trace.name, help=trace_cli.get_trace.help)
@cli_util.option('--time-trace-started-gte', type=custom_types.CLI_DATETIME, help=u"""Include traces that have a `minTraceStartTime` equal to or greater than this value.

The following datetime formats are supported:

UTC with microseconds
***********************
Format: YYYY-MM-DDTHH:mm:ss.ssssssTZD
Example: 2017-09-15T20:30:00.123456Z
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
Timezone with microseconds
***************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00.456789-08:00,
2017-09-15T12:30:00.456789-0800
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
    """)
@cli_util.option('--time-trace-started-lt', type=custom_types.CLI_DATETIME, help=u"""Include traces that have a `minTraceStartTime` less than this value.

The following datetime formats are supported:

UTC with microseconds
***********************
Format: YYYY-MM-DDTHH:mm:ss.ssssssTZD
Example: 2017-09-15T20:30:00.123456Z
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
Timezone with microseconds
***************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00.456789-08:00,
2017-09-15T12:30:00.456789-0800
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
    """)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_traces', 'class': 'Trace'})
@cli_util.wrap_exceptions
def get_trace_extended(ctx, **kwargs):
    if 'time_trace_started_gte' in kwargs:
        kwargs['time_trace_started_greater_than_or_equal_to'] = kwargs['time_trace_started_gte']
        kwargs.pop('time_trace_started_gte')
    if 'time_trace_started_lt' in kwargs:
        kwargs['time_trace_started_less_than'] = kwargs['time_trace_started_lt']
        kwargs.pop('time_trace_started_lt')
    ctx.invoke(trace_cli.get_trace, **kwargs)


@cli_util.copy_params_from_generated_command(trace_cli.get_log, params_to_exclude=['time_log_ended_less_than', 'time_log_started_greater_than_or_equal_to'])
@trace_cli.log_group.command(name=trace_cli.get_log.name, help=trace_cli.get_log.help)
@cli_util.option('--start-time-lt', required=True, type=custom_types.CLI_DATETIME, help=u"""Include logs with log time less than this value.

The following datetime formats are supported:

UTC with microseconds
***********************
Format: YYYY-MM-DDTHH:mm:ss.ssssssTZD
Example: 2017-09-15T20:30:00.123456Z
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
Timezone with microseconds
***************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00.456789-08:00,
2017-09-15T12:30:00.456789-0800
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
@cli_util.option('--start-time-gte', required=True, type=custom_types.CLI_DATETIME, help=u"""Include logs with log time greater than or equal to this value.

The following datetime formats are supported:

UTC with microseconds
***********************
Format: YYYY-MM-DDTHH:mm:ss.ssssssTZD
Example: 2017-09-15T20:30:00.123456Z
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
Timezone with microseconds
***************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00.456789-08:00,
2017-09-15T12:30:00.456789-0800
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_traces', 'class': 'Log'})
@cli_util.wrap_exceptions
def get_log_extended(ctx, **kwargs):
    if 'start_time_lt' in kwargs:
        kwargs['time_log_ended_less_than'] = kwargs['start_time_lt']
        kwargs.pop('start_time_lt')

    if 'start_time_gte' in kwargs:
        kwargs['time_log_started_greater_than_or_equal_to'] = kwargs['start_time_gte']
        kwargs.pop('start_time_gte')
    ctx.invoke(trace_cli.get_log, **kwargs)
