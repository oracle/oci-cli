# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.apm_traces.src.oci_cli_scheduled_query.generated import scheduledquery_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401

# oci apm-traces scheduled-query scheduled-query-collection list-scheduled-queries -> oci apm-traces scheduled-query scheduled-query-collection list
cli_util.rename_command(scheduledquery_cli, scheduledquery_cli.scheduled_query_collection_group, scheduledquery_cli.list_scheduled_queries, "list")

# Move commands under 'oci apm-traces scheduled-query scheduled-query' -> 'oci apm-traces scheduled-query'
scheduledquery_cli.scheduled_query_root_group.commands.pop(scheduledquery_cli.scheduled_query_group.name)
scheduledquery_cli.scheduled_query_root_group.add_command(scheduledquery_cli.create_scheduled_query)
scheduledquery_cli.scheduled_query_root_group.add_command(scheduledquery_cli.delete_scheduled_query)
scheduledquery_cli.scheduled_query_root_group.add_command(scheduledquery_cli.get_scheduled_query)
scheduledquery_cli.scheduled_query_root_group.add_command(scheduledquery_cli.update_scheduled_query)

# Move commands under 'oci apm-traces scheduled-query scheduled-query-collection' -> 'oci apm-traces scheduled-query'
scheduledquery_cli.scheduled_query_root_group.commands.pop(scheduledquery_cli.scheduled_query_collection_group.name)
scheduledquery_cli.scheduled_query_root_group.add_command(scheduledquery_cli.list_scheduled_queries)


# Rename parameter for 'oci apm-traces scheduled-query scheduled-query delete --scheduled-query-id' -> '--id'
@cli_util.copy_params_from_generated_command(scheduledquery_cli.delete_scheduled_query, params_to_exclude=['scheduled_query_id'])
@scheduledquery_cli.scheduled_query_root_group.command(name=scheduledquery_cli.delete_scheduled_query.name, help=scheduledquery_cli.delete_scheduled_query.help)
@cli_util.option('--id', required=True, help=u"""Id of the scheduled query. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_scheduled_query_extended(ctx, **kwargs):

    if 'id' in kwargs:
        kwargs['scheduled_query_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(scheduledquery_cli.delete_scheduled_query, **kwargs)


# Rename parameter for 'oci apm-traces scheduled-query scheduled-query get --scheduled-query-id' -> '--id'
@cli_util.copy_params_from_generated_command(scheduledquery_cli.get_scheduled_query, params_to_exclude=['scheduled_query_id'])
@scheduledquery_cli.scheduled_query_root_group.command(name=scheduledquery_cli.get_scheduled_query.name, help=scheduledquery_cli.get_scheduled_query.help)
@cli_util.option('--id', required=True, help=u"""Id of the scheduled query. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_traces', 'class': 'ScheduledQuery'})
@cli_util.wrap_exceptions
def get_scheduled_query_extended(ctx, **kwargs):

    if 'id' in kwargs:
        kwargs['scheduled_query_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(scheduledquery_cli.get_scheduled_query, **kwargs)


# Rename parameter oci apm-traces scheduled-query scheduled-query update --scheduled-query-description -> --description
# Rename parameter oci apm-traces scheduled-query scheduled-query update --scheduled-query-maximum-runtime-in-seconds -> --maximum-runtime-in-seconds
# Rename parameter oci apm-traces scheduled-query scheduled-query update --scheduled-query-name -> --name
# Rename parameter oci apm-traces scheduled-query scheduled-query update --scheduled-query-processing-configuration -> --processing-configuration
# Rename parameter oci apm-traces scheduled-query scheduled-query update --scheduled-query-processing-sub-type -> --processing-sub-type
# Rename parameter oci apm-traces scheduled-query scheduled-query update --scheduled-query-processing-type -> --processing-type
# Rename parameter oci apm-traces scheduled-query scheduled-query update --scheduled_query_id -> --id
@cli_util.copy_params_from_generated_command(scheduledquery_cli.update_scheduled_query, params_to_exclude=['scheduled_query_id', 'scheduled_query_description', 'scheduled_query_maximum_runtime_in_seconds', 'scheduled_query_name', 'scheduled_query_processing_configuration', 'scheduled_query_processing_sub_type', 'scheduled_query_processing_type', 'scheduled_query_retention_criteria', 'scheduled_query_retention_period_in_ms', 'scheduled_query_schedule', 'scheduled_query_text'])
@scheduledquery_cli.scheduled_query_root_group.command(name=scheduledquery_cli.update_scheduled_query.name, help=scheduledquery_cli.update_scheduled_query.help)
@cli_util.option('--processing-type', type=custom_types.CliCaseInsensitiveChoice(["EXPORT", "QUERY", "ALERT"]), help="""Type of the scheduled query.""")
@cli_util.option('--processing-sub-type', type=custom_types.CliCaseInsensitiveChoice(["OBJECT_STORAGE", "STREAMING", "CUSTOM_METRIC", "NONE"]), help="""Processing sub type of the scheduled query.""")
@cli_util.option('--processing-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--name', help="""Name of the scheduled query.""")
@cli_util.option('--maximum-runtime-in-seconds', type=click.INT, help="""Maximum runtime for the scheduled query in seconds.""")
@cli_util.option('--description', help="""Description for the scheduled query.""")
@cli_util.option('--id', required=True, help=u"""Id of the scheduled query. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'processing-configuration': {'module': 'apm_traces', 'class': 'ScheduledQueryProcessingConfig'}, 'freeform-tags': {'module': 'apm_traces', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_traces', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_traces', 'class': 'ScheduledQuery'})
@cli_util.wrap_exceptions
def update_scheduled_query_extended(ctx, **kwargs):

    if 'processing_type' in kwargs:
        kwargs['scheduled_query_processing_type'] = kwargs['processing_type']
        kwargs.pop('processing_type')

    if 'processing_sub_type' in kwargs:
        kwargs['scheduled_query_processing_sub_type'] = kwargs['processing_sub_type']
        kwargs.pop('processing_sub_type')

    if 'processing_configuration' in kwargs:
        kwargs['scheduled_query_processing_configuration'] = kwargs['processing_configuration']
        kwargs.pop('processing_configuration')

    if 'name' in kwargs:
        kwargs['scheduled_query_name'] = kwargs['name']
        kwargs.pop('name')

    if 'maximum_runtime_in_seconds' in kwargs:
        kwargs['scheduled_query_maximum_runtime_in_seconds'] = kwargs['maximum_runtime_in_seconds']
        kwargs.pop('maximum_runtime_in_seconds')

    if 'description' in kwargs:
        kwargs['scheduled_query_description'] = kwargs['description']
        kwargs.pop('description')

    if 'id' in kwargs:
        kwargs['scheduled_query_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(scheduledquery_cli.update_scheduled_query, **kwargs)


# Rename parameter oci apm-traces scheduled-query scheduled-query create --scheduled-query-description -> --description
# Rename parameter oci apm-traces scheduled-query scheduled-query create --scheduled-query-maximum-runtime-in-seconds -> --maximum-runtime-in-seconds
# Rename parameter oci apm-traces scheduled-query scheduled-query create --scheduled-query-name -> --name
# Rename parameter oci apm-traces scheduled-query scheduled-query create --scheduled-query-processing-configuration -> --processing-configuration
# Rename parameter oci apm-traces scheduled-query scheduled-query create --scheduled-query-processing-sub-type -> --processing-sub-type
# Rename parameter oci apm-traces scheduled-query scheduled-query create --scheduled-query-processing-type -> --processing-type
# Rename parameter oci apm-traces scheduled-query scheduled-query create --scheduled-query-retention-criteria -> --retention-criteria
# Rename parameter oci apm-traces scheduled-query scheduled-query create --scheduled-query-retention-period-in-ms -> --retention-period-in-ms
# Rename parameter oci apm-traces scheduled-query scheduled-query create --scheduled-query-schedule -> --schedule
# Rename parameter oci apm-traces scheduled-query scheduled-query create --scheduled-query-text -> --text
@cli_util.copy_params_from_generated_command(scheduledquery_cli.create_scheduled_query, params_to_exclude=['scheduled_query_id', 'scheduled_query_description', 'scheduled_query_maximum_runtime_in_seconds', 'scheduled_query_name', 'scheduled_query_processing_configuration', 'scheduled_query_processing_sub_type', 'scheduled_query_processing_type', 'scheduled_query_retention_criteria', 'scheduled_query_retention_period_in_ms', 'scheduled_query_schedule', 'scheduled_query_text'])
@scheduledquery_cli.scheduled_query_root_group.command(name=scheduledquery_cli.create_scheduled_query.name, help=scheduledquery_cli.create_scheduled_query.help)
@cli_util.option('--text', help="""Scheduled query to be run.""")
@cli_util.option('--schedule', help="""Schedule for the scheduled query.""")
@cli_util.option('--retention-period-in-ms', type=click.INT, help="""Retention period for the scheduled query in milliseconds.""")
@cli_util.option('--retention-criteria', type=custom_types.CliCaseInsensitiveChoice(["KEEP_DATA_UNTIL_RETENTION_PERIOD", "UPDATE"]), help="""Retention criteria for the scheduled query.""")
@cli_util.option('--processing-type', type=custom_types.CliCaseInsensitiveChoice(["EXPORT", "QUERY", "ALERT"]), help="""Type of the scheduled query.""")
@cli_util.option('--processing-sub-type', type=custom_types.CliCaseInsensitiveChoice(["OBJECT_STORAGE", "STREAMING", "CUSTOM_METRIC", "NONE"]), help="""Processing sub type of the scheduled query.""")
@cli_util.option('--processing-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--name', help="""Name of the scheduled query.""")
@cli_util.option('--maximum-runtime-in-seconds', type=click.INT, help="""Maximum runtime for the scheduled query in seconds.""")
@cli_util.option('--description', help="""Description for the scheduled query.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'processing-configuration': {'module': 'apm_traces', 'class': 'ScheduledQueryProcessingConfig'}, 'freeform-tags': {'module': 'apm_traces', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_traces', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_traces', 'class': 'ScheduledQuery'})
@cli_util.wrap_exceptions
def create_scheduled_query_extended(ctx, **kwargs):

    if 'text' in kwargs:
        kwargs['scheduled_query_text'] = kwargs['text']
        kwargs.pop('text')

    if 'schedule' in kwargs:
        kwargs['scheduled_query_schedule'] = kwargs['schedule']
        kwargs.pop('schedule')

    if 'retention_period_in_ms' in kwargs:
        kwargs['scheduled_query_retention_period_in_ms'] = kwargs['retention_period_in_ms']
        kwargs.pop('retention_period_in_ms')

    if 'retention_criteria' in kwargs:
        kwargs['scheduled_query_retention_criteria'] = kwargs['retention_criteria']
        kwargs.pop('retention_criteria')

    if 'processing_type' in kwargs:
        kwargs['scheduled_query_processing_type'] = kwargs['processing_type']
        kwargs.pop('processing_type')

    if 'processing_sub_type' in kwargs:
        kwargs['scheduled_query_processing_sub_type'] = kwargs['processing_sub_type']
        kwargs.pop('processing_sub_type')

    if 'processing_configuration' in kwargs:
        kwargs['scheduled_query_processing_configuration'] = kwargs['processing_configuration']
        kwargs.pop('processing_configuration')

    if 'name' in kwargs:
        kwargs['scheduled_query_name'] = kwargs['name']
        kwargs.pop('name')

    if 'maximum_runtime_in_seconds' in kwargs:
        kwargs['scheduled_query_maximum_runtime_in_seconds'] = kwargs['maximum_runtime_in_seconds']
        kwargs.pop('maximum_runtime_in_seconds')

    if 'description' in kwargs:
        kwargs['scheduled_query_description'] = kwargs['description']
        kwargs.pop('description')

    ctx.invoke(scheduledquery_cli.create_scheduled_query, **kwargs)


# Rename parameter oci apm-traces scheduled-query list --display-name -> --name
@cli_util.copy_params_from_generated_command(scheduledquery_cli.list_scheduled_queries, params_to_exclude=['display_name'])
@scheduledquery_cli.scheduled_query_root_group.command(name=scheduledquery_cli.list_scheduled_queries.name, help=scheduledquery_cli.list_scheduled_queries.help)
@cli_util.option('--name', help=u"""A filter to return resources that match the
                                  given display name.  This will return
                                  resources that have name starting with this
                                  filter.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def list_scheduled_queries_extended(ctx, **kwargs):

    if 'name' in kwargs:
        kwargs['display_name'] = kwargs['name']
        kwargs.pop('name')

    ctx.invoke(scheduledquery_cli.list_scheduled_queries, **kwargs)
