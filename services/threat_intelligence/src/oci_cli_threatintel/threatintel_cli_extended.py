# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.threat_intelligence.src.oci_cli_threatintel.generated import threatintel_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci threat-intelligence indicator-summary-collection -> oci threat-intelligence indicator-summaries
cli_util.rename_command(threatintel_cli, threatintel_cli.threat_intelligence_root_group, threatintel_cli.indicator_summary_collection_group, "indicator-summaries")


@cli_util.copy_params_from_generated_command(threatintel_cli.list_indicators, params_to_exclude=['confidence_greater_than_or_equal_to', 'time_updated_greater_than_or_equal_to'])
@threatintel_cli.indicator_summary_collection_group.command(name=threatintel_cli.list_indicators.name, help=threatintel_cli.list_indicators.help)
@cli_util.option('--confidence-above', type=click.INT, help=u"""The minimum confidence score of entities to be returned.""")
@cli_util.option('--time-updated-after', type=custom_types.CLI_DATETIME, help=u"""The oldest update time of entities to be returned.
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'threat-type-name': {'module': 'threat_intelligence', 'class': 'list[string]'}}, output_type={'module': 'threat_intelligence', 'class': 'IndicatorSummaryCollection'})
@cli_util.wrap_exceptions
def list_indicators_extended(ctx, **kwargs):
    if 'confidence_above' in kwargs:
        kwargs['confidence_greater_than_or_equal_to'] = kwargs['confidence_above']
        kwargs.pop('confidence_above')

    if 'time_updated_after' in kwargs:
        kwargs['time_updated_greater_than_or_equal_to'] = kwargs['time_updated_after']
        kwargs.pop('time_updated_after')

    ctx.invoke(threatintel_cli.list_indicators, **kwargs)


# oci threat-intelligence indicator-count-collection -> oci threat-intelligence indicator-counts
cli_util.rename_command(threatintel_cli, threatintel_cli.threat_intelligence_root_group, threatintel_cli.indicator_count_collection_group, "indicator-counts")
