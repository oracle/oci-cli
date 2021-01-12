# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.monitoring.src.oci_cli_monitoring.generated import monitoring_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
import click


@cli_util.copy_params_from_generated_command(monitoring_cli.create_alarm, params_to_exclude=['query_parameterconflict'])
@monitoring_cli.alarm_group.command(name=cli_util.override('create_alarm.command_name', 'create'), help="""Creates a new alarm in the specified compartment.""")
@cli_util.option('--query-text', required=True, help="""The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of the Monitoring service interprets results for each returned time series as Boolean values, where zero represents false and a non-zero value represents true. A true value means that the trigger rule condition has been met. The query must specify a metric, statistic, interval, and trigger rule (threshold or absence). Supported values for interval: `1m`-`60m` (also `1h`). You can optionally specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`. For details about Monitoring Query Language (MQL), see [Monitoring Query Language (MQL) Reference]. For available dimensions, review the metric definition for the supported service. See [Supported Services].

Example of threshold alarm:

  -----

    CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.groupBy(availabilityDomain).percentile(0.9) > 85

  -----

Example of absence alarm:

  -----

    CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent()

  -----""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'destinations': {'module': 'monitoring', 'class': 'list[string]'}, 'suppression': {'module': 'monitoring', 'class': 'Suppression'}, 'freeform-tags': {'module': 'monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'monitoring', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'monitoring', 'class': 'Alarm'})
@cli_util.wrap_exceptions
def create_alarm(ctx, query_text, **kwargs):
    kwargs['query_parameterconflict'] = query_text
    ctx.invoke(monitoring_cli.create_alarm, **kwargs)


@cli_util.copy_params_from_generated_command(monitoring_cli.summarize_metrics_data, params_to_exclude=['query_parameterconflict'])
@monitoring_cli.metric_data_group.command(name=cli_util.override('summarize_metrics_data.command_name', 'summarize-metrics-data'), help="""Returns aggregated data that match the criteria specified in the request. Compartment OCID required. For information on metric queries, see [Building Metric Queries].""")
@cli_util.option('--query-text', required=True, help="""The Monitoring Query Language (MQL) expression to use when searching for metric data points to aggregate. The query must specify a metric, statistic, and interval. Supported values for interval: `1m`-`60m` (also `1h`). You can optionally specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`. For details about Monitoring Query Language (MQL), see [Monitoring Query Language (MQL) Reference]. For available dimensions, review the metric definition for the supported service. See [Supported Services].

Example: `CpuUtilization[1m].sum()`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'monitoring', 'class': 'list[MetricData]'})
@cli_util.wrap_exceptions
def summarize_metrics_data(ctx, query_text, **kwargs):
    kwargs['query_parameterconflict'] = query_text
    ctx.invoke(monitoring_cli.summarize_metrics_data, **kwargs)


@cli_util.copy_params_from_generated_command(monitoring_cli.update_alarm, params_to_exclude=['query_parameterconflict'])
@monitoring_cli.alarm_group.command(name=cli_util.override('update_alarm.command_name', 'update'), help="""Updates the specified alarm.""")
@cli_util.option('--query-text', help="""The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of the Monitoring service interprets results for each returned time series as Boolean values, where zero represents false and a non-zero value represents true. A true value means that the trigger rule condition has been met. The query must specify a metric, statistic, interval, and trigger rule (threshold or absence). Supported values for interval: `1m`-`60m` (also `1h`). You can optionally specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`. For details about Monitoring Query Language (MQL), see [Monitoring Query Language (MQL) Reference]. For available dimensions, review the metric definition for the supported service. See [Supported Services].

Example of threshold alarm:

  -----

    CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.groupBy(availabilityDomain).percentile(0.9) > 85

  -----

Example of absence alarm:

  -----

    CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent()

  -----""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'destinations': {'module': 'monitoring', 'class': 'list[string]'}, 'suppression': {'module': 'monitoring', 'class': 'Suppression'}, 'freeform-tags': {'module': 'monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'monitoring', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'monitoring', 'class': 'Alarm'})
@cli_util.wrap_exceptions
def update_alarm(ctx, query_text, **kwargs):
    kwargs['query_parameterconflict'] = query_text
    ctx.invoke(monitoring_cli.update_alarm, **kwargs)
