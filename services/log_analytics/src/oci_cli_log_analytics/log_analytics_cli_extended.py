# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
import json

from oci_cli.cli_util import get_param
from services.log_analytics.src.oci_cli_log_analytics.generated import loganalytics_cli
from oci_cli import cli_util
from oci_cli import custom_types
from oci_cli import json_skeleton_utils

# Query CLI ovverrides
get_param(loganalytics_cli.query, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.export_query_result, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.filter, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.parse_query, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.suggest, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.get_query_result, 'namespace_name').opts.extend(['--namespace', '-ns'])

cli_util.rename_command(loganalytics_cli, loganalytics_cli.query_group, loganalytics_cli.query, "search")


@cli_util.copy_params_from_generated_command(loganalytics_cli.query, params_to_exclude=['time_filter', 'saved_search_id'])
@loganalytics_cli.query_group.command(name='search', help=loganalytics_cli.query.help)
@cli_util.option('--time-start', type=custom_types.CLI_DATETIME, help="""Date-time for query to start matching results from. Start time must be less than end time otherwise it will result in error.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', type=custom_types.CLI_DATETIME, help="""Date-time for query to stop matching results to. End Time must be greater than or equal to start time otherwise it will result in error.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--timezone', help="""Time zone for query. Should use long time zone name e.g America/New_York to handle daylight savings properly.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'scope-filters': {'module': 'log_analytics', 'class': 'list[ScopeFilter]'}}, output_type={'module': 'log_analytics', 'class': 'QueryAggregation'})
@cli_util.wrap_exceptions
def query_extended(ctx, **kwargs):
    time_filter = {}
    if kwargs['time_start']:
        time_filter['timeStart'] = kwargs['time_start']
    kwargs.pop('time_start')

    if kwargs['time_end']:
        time_filter['timeEnd'] = kwargs['time_end']
    kwargs.pop('time_end')

    if kwargs['timezone']:
        time_filter['timeZone'] = kwargs['timezone']
    kwargs.pop('timezone')

    if len(time_filter) > 0:
        kwargs['time_filter'] = json.dumps(time_filter)

    ctx.invoke(loganalytics_cli.query, **kwargs)


cli_util.rename_command(loganalytics_cli, loganalytics_cli.query_group, loganalytics_cli.export_query_result, "export")


@cli_util.copy_params_from_generated_command(loganalytics_cli.export_query_result, params_to_exclude=['time_filter'])
@loganalytics_cli.query_group.command(name='export', help=loganalytics_cli.export_query_result.help)
@cli_util.option('--time-start', type=custom_types.CLI_DATETIME, help="""Date-time for query to start matching results from. Start time must be less than end time otherwise it will result in error.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', type=custom_types.CLI_DATETIME, help="""Date-time for query to stop matching results to. End Time must be greater than or equal to start time otherwise it will result in error.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--timezone', help="""Time zone for query. Should use long time zone name e.g America/New_York to handle daylight savings properly.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'scope-filters': {'module': 'log_analytics', 'class': 'list[ScopeFilter]'}})
@cli_util.wrap_exceptions
def export_query_result_extended(ctx, **kwargs):
    time_filter = {}
    if kwargs['time_start']:
        time_filter['timeStart'] = kwargs['time_start']
    kwargs.pop('time_start')

    if kwargs['time_end']:
        time_filter['timeEnd'] = kwargs['time_end']
    kwargs.pop('time_end')

    if kwargs['timezone']:
        time_filter['timeZone'] = kwargs['timezone']
    kwargs.pop('timezone')

    if len(time_filter) > 0:
        kwargs['time_filter'] = json.dumps(time_filter)

    ctx.invoke(loganalytics_cli.export_query_result, **kwargs)


# query-work-request overrides
cli_util.rename_command(loganalytics_cli, loganalytics_cli.query_work_request_group,
                        loganalytics_cli.put_query_work_request_background, "background")
get_param(loganalytics_cli.list_query_work_requests, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.get_query_work_request, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.cancel_query_work_request, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.put_query_work_request_background, 'namespace_name').opts.extend(['--namespace', '-ns'])


# ScheduledTask overrides
loganalytics_cli.scheduled_task_group.commands.pop(loganalytics_cli.create_scheduled_task.name)
cli_util.rename_command(loganalytics_cli, loganalytics_cli.scheduled_task_group,
                        loganalytics_cli.create_scheduled_task_create_acceleration_task_details, "create-acceleration-task")
cli_util.rename_command(loganalytics_cli, loganalytics_cli.scheduled_task_group,
                        loganalytics_cli.create_scheduled_task_create_standard_task_details, "create-standard-task")

get_param(loganalytics_cli.create_scheduled_task_create_standard_task_details, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.create_scheduled_task_create_acceleration_task_details, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.update_scheduled_task, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.clean, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.run, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.delete_scheduled_task, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.list_scheduled_tasks, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.change_scheduled_task_compartment, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.get_scheduled_task, 'namespace_name').opts.extend(['--namespace', '-ns'])


# logan-uploads-api overrides
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_object_collection_rule_group, "object-collection-rule")


# object-collection-rule get
@cli_util.copy_params_from_generated_command(loganalytics_cli.get_log_analytics_object_collection_rule, params_to_exclude=['log_analytics_object_collection_rule_id'])
@loganalytics_cli.log_analytics_object_collection_rule_group.command(name='get', help=loganalytics_cli.get_log_analytics_object_collection_rule.help)
@cli_util.option('--object-collection-rule-id', required=True, help="""The Logging Analytics Object Collection Rule [OCID]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsObjectCollectionRule'})
@cli_util.wrap_exceptions
def get_log_analytics_object_collection_rule_extended(ctx, **kwargs):
    if 'object_collection_rule_id' in kwargs:
        kwargs['log_analytics_object_collection_rule_id'] = kwargs['object_collection_rule_id']
        kwargs.pop('object_collection_rule_id')
    ctx.invoke(loganalytics_cli.get_log_analytics_object_collection_rule, **kwargs)


# object-collection-rule update
@cli_util.copy_params_from_generated_command(loganalytics_cli.update_log_analytics_object_collection_rule, params_to_exclude=['log_analytics_object_collection_rule_id'])
@loganalytics_cli.log_analytics_object_collection_rule_group.command(name='update', help=loganalytics_cli.update_log_analytics_object_collection_rule.help)
@cli_util.option('--object-collection-rule-id', required=True, help="""The Logging Analytics Object Collection Rule [OCID]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'overrides': {'module': 'log_analytics', 'class': 'dict(str, list[PropertyOverride])'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsObjectCollectionRule'})
@cli_util.wrap_exceptions
def update_log_analytics_object_collection_rule_extended(ctx, **kwargs):
    if 'object_collection_rule_id' in kwargs:
        kwargs['log_analytics_object_collection_rule_id'] = kwargs['object_collection_rule_id']
        kwargs.pop('object_collection_rule_id')
    ctx.invoke(loganalytics_cli.update_log_analytics_object_collection_rule, **kwargs)


# object-collection-rule delete
@cli_util.copy_params_from_generated_command(loganalytics_cli.delete_log_analytics_object_collection_rule, params_to_exclude=['log_analytics_object_collection_rule_id'])
@loganalytics_cli.log_analytics_object_collection_rule_group.command(name='delete', help=loganalytics_cli.delete_log_analytics_object_collection_rule.help)
@cli_util.option('--object-collection-rule-id', required=True, help="""The Logging Analytics Object Collection Rule [OCID]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_log_analytics_object_collection_rule_extended(ctx, **kwargs):
    if 'object_collection_rule_id' in kwargs:
        kwargs['log_analytics_object_collection_rule_id'] = kwargs['object_collection_rule_id']
        kwargs.pop('object_collection_rule_id')
    ctx.invoke(loganalytics_cli.delete_log_analytics_object_collection_rule, **kwargs)


# object-collection-rule change-compartment
@cli_util.copy_params_from_generated_command(loganalytics_cli.change_log_analytics_object_collection_rule_compartment, params_to_exclude=['log_analytics_object_collection_rule_id'])
@loganalytics_cli.log_analytics_object_collection_rule_group.command(name='change-compartment', help=loganalytics_cli.change_log_analytics_object_collection_rule_compartment.help)
@cli_util.option('--object-collection-rule-id', required=True, help="""The Logging Analytics Object Collection Rule [OCID]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_log_analytics_object_collection_rule_compartment_extended(ctx, **kwargs):
    if 'object_collection_rule_id' in kwargs:
        kwargs['log_analytics_object_collection_rule_id'] = kwargs['object_collection_rule_id']
        kwargs.pop('object_collection_rule_id')
    ctx.invoke(loganalytics_cli.change_log_analytics_object_collection_rule_compartment, **kwargs)


# list-supported-char-encodings
cli_util.rename_command(loganalytics_cli, loganalytics_cli.char_encoding_collection_group,
                        loganalytics_cli.list_supported_char_encodings, "list-supported-encodings")


# upload-log-file
@cli_util.copy_params_from_generated_command(loganalytics_cli.upload_log_file, params_to_exclude=['upload_log_file_body'])
@loganalytics_cli.upload_group.command(name='upload-log-file', help=loganalytics_cli.upload_log_file.help)
@cli_util.option('--file', type=click.File(mode='rb'), required=True, help=u"""Log data file. Example: --file /Users/me/myfile.txt""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'Upload'})
@cli_util.wrap_exceptions
def upload_log_file_extended(ctx, **kwargs):
    # Set "--upload-log-file-body" to the content of file "--file"
    if 'file' in kwargs and kwargs['file']:
        content = kwargs['file'].read()
        kwargs['upload_log_file_body'] = content
    del kwargs['file']
    ctx.invoke(loganalytics_cli.upload_log_file, **kwargs)


# namespace aliases for uplaods
get_param(loganalytics_cli.upload_log_file, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.list_uploads, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.get_upload, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.delete_upload, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.list_upload_files, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.delete_upload_file, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.list_upload_warnings, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.delete_upload_warning, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.validate_source_mapping, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.validate_file, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.list_supported_char_encodings, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.list_supported_timezones, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.create_log_analytics_object_collection_rule, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.list_log_analytics_object_collection_rules, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.get_log_analytics_object_collection_rule, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.update_log_analytics_object_collection_rule, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.delete_log_analytics_object_collection_rule, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.change_log_analytics_object_collection_rule_compartment, 'namespace_name').opts.extend(['--namespace', '-ns'])


# Entity type command and param changes


cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_entity_type_group, "entity-type")


# Change entity_type_name to name in delete entity type
@cli_util.copy_params_from_generated_command(loganalytics_cli.delete_log_analytics_entity_type, params_to_exclude=['entity_type_name'])
@loganalytics_cli.log_analytics_entity_type_group.command(name='delete', help=loganalytics_cli.delete_log_analytics_entity_type.help)
@cli_util.option('--name', required=True, help="""Log analytics entity type name""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_log_analytics_entity_type_extended(ctx, **kwargs):
    if 'name' in kwargs:
        kwargs['entity_type_name'] = kwargs['name']
        kwargs.pop('name')
    ctx.invoke(loganalytics_cli.delete_log_analytics_entity_type, **kwargs)


# Change entity_type_name to name in get entity type
@cli_util.copy_params_from_generated_command(loganalytics_cli.get_log_analytics_entity_type, params_to_exclude=['entity_type_name'])
@loganalytics_cli.log_analytics_entity_type_group.command(name='get', help=loganalytics_cli.get_log_analytics_entity_type.help)
@cli_util.option('--name', required=True, help="""Log analytics entity type name""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsEntityType'})
@cli_util.wrap_exceptions
def get_log_analytics_entity_type_extended(ctx, **kwargs):
    if 'name' in kwargs:
        kwargs['entity_type_name'] = kwargs['name']
        kwargs.pop('name')
    ctx.invoke(loganalytics_cli.get_log_analytics_entity_type, **kwargs)


# Change entity_type_name to name in update entity type
@cli_util.copy_params_from_generated_command(loganalytics_cli.update_log_analytics_entity_type, params_to_exclude=['entity_type_name'])
@loganalytics_cli.log_analytics_entity_type_group.command(name='update', help=loganalytics_cli.update_log_analytics_entity_type.help)
@cli_util.option('--name', required=True, help="""Log analytics entity type name""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'log_analytics', 'class': 'list[EntityTypeProperty]'}})
@cli_util.wrap_exceptions
def update_log_analytics_entity_type_extended(ctx, **kwargs):
    if 'name' in kwargs:
        kwargs['entity_type_name'] = kwargs['name']
        kwargs.pop('name')
    ctx.invoke(loganalytics_cli.update_log_analytics_entity_type, **kwargs)


get_param(loganalytics_cli.create_log_analytics_entity_type, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.delete_log_analytics_entity_type, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.get_log_analytics_entity_type, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.list_log_analytics_entity_types, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.list_log_analytics_entity_types, 'lifecycle_state').opts.extend(['-lc'])
get_param(loganalytics_cli.update_log_analytics_entity_type, 'namespace_name').opts.extend(['--namespace', '-ns'])


# Entity resource command and param changes
# Rename command and sub-commands
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_entity_group, "entity")
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_entity_group, loganalytics_cli.add_entity_association, "add-associations")
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_entity_group, loganalytics_cli.list_entity_associations, "list-associations")
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_entity_group, loganalytics_cli.remove_entity_associations, "remove-associations")
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_entity_group, loganalytics_cli.get_log_analytics_entities_summary, "summary")


# Rename log_analytics_entity_id to entity_id in change compartment
@cli_util.copy_params_from_generated_command(loganalytics_cli.change_log_analytics_entity_compartment, params_to_exclude=['log_analytics_entity_id'])
@loganalytics_cli.log_analytics_entity_group.command(name='change-compartment', help=loganalytics_cli.change_log_analytics_entity_compartment.help)
@cli_util.option('--entity-id', required=True, help="""The log analytics entity OCID""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_log_analytics_entity_compartment_extended(ctx, **kwargs):
    if 'entity_id' in kwargs:
        kwargs['log_analytics_entity_id'] = kwargs['entity_id']
        kwargs.pop('entity_id')
    ctx.invoke(loganalytics_cli.change_log_analytics_entity_compartment, **kwargs)


# Rename log_analytics_entity_id to entity_id in create entity
@cli_util.copy_params_from_generated_command(loganalytics_cli.create_log_analytics_entity, params_to_exclude=['management_agent_id'])
@loganalytics_cli.log_analytics_entity_group.command(name='create', help=loganalytics_cli.create_log_analytics_entity.help)
@cli_util.option('--agent-id', required=False, help="""The OCID of the Management Agent""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsEntity'})
@cli_util.wrap_exceptions
def create_log_analytics_entity_extended(ctx, **kwargs):
    if 'agent_id' in kwargs:
        kwargs['management_agent_id'] = kwargs['agent_id']
        kwargs.pop('agent_id')
    ctx.invoke(loganalytics_cli.create_log_analytics_entity, **kwargs)


# Rename log_analytics_entity_id to entity_id in delete entity
@cli_util.copy_params_from_generated_command(loganalytics_cli.delete_log_analytics_entity, params_to_exclude=['log_analytics_entity_id'])
@loganalytics_cli.log_analytics_entity_group.command(name='delete', help=loganalytics_cli.delete_log_analytics_entity.help)
@cli_util.option('--entity-id', required=True, help="""The log analytics entity OCID""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_log_analytics_entity_extended(ctx, **kwargs):
    if 'entity_id' in kwargs:
        kwargs['log_analytics_entity_id'] = kwargs['entity_id']
        kwargs.pop('entity_id')
    ctx.invoke(loganalytics_cli.delete_log_analytics_entity, **kwargs)


# Rename log_analytics_entity_id to entity_id in get entity
@cli_util.copy_params_from_generated_command(loganalytics_cli.get_log_analytics_entity, params_to_exclude=['log_analytics_entity_id'])
@loganalytics_cli.log_analytics_entity_group.command(name='get', help=loganalytics_cli.get_log_analytics_entity.help)
@cli_util.option('--entity-id', required=True, help="""The log analytics entity OCID""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsEntity'})
@cli_util.wrap_exceptions
def get_log_analytics_entity_extended(ctx, **kwargs):
    if 'entity_id' in kwargs:
        kwargs['log_analytics_entity_id'] = kwargs['entity_id']
        kwargs.pop('entity_id')
    ctx.invoke(loganalytics_cli.get_log_analytics_entity, **kwargs)


# Shorten is_management_agent_id_null to is_agent_id_null in list entities
@cli_util.copy_params_from_generated_command(loganalytics_cli.list_log_analytics_entities, params_to_exclude=['is_management_agent_id_null'])
@loganalytics_cli.log_analytics_entity_group.command(name='list', help=loganalytics_cli.list_log_analytics_entities.help)
@cli_util.option('--is-agent-id-null', type=custom_types.CliCaseInsensitiveChoice(["true", "false"]), required=False, help="""A filter to return only those log analytics entities whose managementAgentId is null or is not null""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'entity-type-name': {'module': 'log_analytics', 'class': 'list[string]'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsEntityCollection'})
@cli_util.wrap_exceptions
def list_log_analytics_entities_extended(ctx, **kwargs):
    if 'is_agent_id_null' in kwargs:
        kwargs['is_management_agent_id_null'] = kwargs['is_agent_id_null']
        kwargs.pop('is_agent_id_null')
    ctx.invoke(loganalytics_cli.list_log_analytics_entities, **kwargs)


# Rename log_analytics_entity_id to entity_id in update entity and shorten management_agent_id to agent_id
@cli_util.copy_params_from_generated_command(loganalytics_cli.update_log_analytics_entity, params_to_exclude=['management_agent_id', 'log_analytics_entity_id'])
@loganalytics_cli.log_analytics_entity_group.command(name='update', help=loganalytics_cli.update_log_analytics_entity.help)
@cli_util.option('--entity-id', required=True, help="""The log analytics entity OCID""")
@cli_util.option('--agent-id', required=False, help="""The OCID of the Management Agent.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsEntity'})
@cli_util.wrap_exceptions
def update_log_analytics_entity_extended(ctx, **kwargs):
    if 'entity_id' in kwargs:
        kwargs['log_analytics_entity_id'] = kwargs['entity_id']
        kwargs.pop('entity_id')
    if 'agent_id' in kwargs:
        kwargs['management_agent_id'] = kwargs['agent_id']
        kwargs.pop('agent_id')

    ctx.invoke(loganalytics_cli.update_log_analytics_entity, **kwargs)


# Rename log_analytics_entity_id to entity_id in add entity associations
@cli_util.copy_params_from_generated_command(loganalytics_cli.add_entity_association, params_to_exclude=['log_analytics_entity_id'])
@loganalytics_cli.log_analytics_entity_group.command(name='add-associations', help=loganalytics_cli.add_entity_association.help)
@cli_util.option('--entity-id', required=True, help="""The log analytics entity OCID""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'association-entities': {'module': 'log_analytics', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def add_entity_association_extended(ctx, **kwargs):
    if 'entity_id' in kwargs:
        kwargs['log_analytics_entity_id'] = kwargs['entity_id']
        kwargs.pop('entity_id')
    ctx.invoke(loganalytics_cli.add_entity_association, **kwargs)


# Rename log_analytics_entity_id to entity_id in update entity and shorten direct_or_all_associations to direct_or_all
@cli_util.copy_params_from_generated_command(loganalytics_cli.list_entity_associations, params_to_exclude=['direct_or_all_associations', 'log_analytics_entity_id'])
@loganalytics_cli.log_analytics_entity_group.command(name='list-associations', help=loganalytics_cli.list_entity_associations.help)
@cli_util.option('--entity-id', required=True, help="""The log analytics entity OCID""")
@cli_util.option('--direct-or-all', type=custom_types.CliCaseInsensitiveChoice(["DIRECT", "ALL"]), required=False, help="""Indicates whether to return direct associated entities or direct and inferred associated entities.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsEntityCollection'})
@cli_util.wrap_exceptions
def list_entity_associations_extended(ctx, **kwargs):
    if 'entity_id' in kwargs:
        kwargs['log_analytics_entity_id'] = kwargs['entity_id']
        kwargs.pop('entity_id')
    if 'direct_or_all' in kwargs:
        kwargs['direct_or_all_associations'] = kwargs['direct_or_all']
        kwargs.pop('direct_or_all')

    ctx.invoke(loganalytics_cli.list_entity_associations, **kwargs)


# Rename log_analytics_entity_id to entity_id in remove entity associations
@cli_util.copy_params_from_generated_command(loganalytics_cli.remove_entity_associations, params_to_exclude=['log_analytics_entity_id'])
@loganalytics_cli.log_analytics_entity_group.command(name='remove-associations', help=loganalytics_cli.remove_entity_associations.help)
@cli_util.option('--entity-id', required=True, help="""The log analytics entity OCID""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'association-entities': {'module': 'log_analytics', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def remove_entity_associations_extended(ctx, **kwargs):
    if 'entity_id' in kwargs:
        kwargs['log_analytics_entity_id'] = kwargs['entity_id']
        kwargs.pop('entity_id')
    ctx.invoke(loganalytics_cli.remove_entity_associations, **kwargs)


get_param(loganalytics_cli.add_entity_association, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.list_entity_associations, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.remove_entity_associations, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.change_log_analytics_entity_compartment, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.create_log_analytics_entity, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.delete_log_analytics_entity, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.get_log_analytics_entity, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.get_log_analytics_entities_summary, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.list_log_analytics_entities, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(loganalytics_cli.update_log_analytics_entity, 'namespace_name').opts.extend(['--namespace', '-ns'])

# Config CLI overrides

# ###########################
# Top Level Commands - Start
# ###########################

# log-group commands
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_log_group_group, "log-group")

# label commands
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_label_group, "label")

# field commands
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_field_group, "field")

# parser commands
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_parser_group, "parser")

# source commands
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_source_group, "source")
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.extended_fields_validation_result_group, "extfields-validation")

# Association commands
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.association_summary_report_group, "assoc-summary")
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.error_details_group, "assoc-delete")
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_associated_entity_collection_group, "assoc-entities")
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_association_collection_group, "assoc-collection")
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_association_group, "assoc")
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_association_parameter_collection_group, "assoc-params")

# lookup commands
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_lookup_group, "lookup")

# content commands
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.binary_group, "content-export")
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_import_custom_content_group, "content-import")

# config-work-request commands
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_config_work_request_group, "config-work-request")
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_root_group, loganalytics_cli.log_analytics_config_work_request_collection_group, "config-work-request-collection")

# #########################
# Top Level Commands - End
# #########################

# ###########################
# Sub Level Commands - Start
# ###########################

# get-association-summary -> get-assoc-summary
cli_util.rename_command(loganalytics_cli, loganalytics_cli.association_summary_report_group, loganalytics_cli.get_association_summary, "get-assoc-summary")
# delete-associations -> delete-assocs
cli_util.rename_command(loganalytics_cli, loganalytics_cli.error_details_group, loganalytics_cli.delete_associations, "delete-assocs")
# upsert-associations -> upsert-assocs
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_association_group, loganalytics_cli.upsert_associations, "upsert-assocs")
# validate_source_extended_field_details -> validate-extfield-details
cli_util.rename_command(loganalytics_cli, loganalytics_cli.extended_fields_validation_result_group, loganalytics_cli.validate_source_extended_field_details, "validate-source-extfield-details")
# list-entity-source-associations -> list-entity-source-assocs
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_association_collection_group, loganalytics_cli.list_entity_source_associations, "list-entity-source-assocs")
# list-source-associations -> list-source-assocs
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_association_collection_group, loganalytics_cli.list_source_associations, "list-source-assocs")
# validate-association-parameters -> validate-association-params
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_association_parameter_collection_group, loganalytics_cli.validate_association_parameters, "validate-assoc-params")

# #########################
# Sub Level Commands - End
# #########################

# ######################
# Param Changes - Start
# ######################


# log-group get param changes


@cli_util.copy_params_from_generated_command(loganalytics_cli.get_log_analytics_log_group, params_to_exclude=['log_analytics_log_group_id'])
@loganalytics_cli.log_analytics_log_group_group.command(name='get', help=loganalytics_cli.get_log_analytics_log_group.help)
@cli_util.option("--log-group-id", help='''The log group OCID''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsLogGroup'})
@cli_util.wrap_exceptions
def get_log_analytics_log_group_extended(ctx, **kwargs):
    if 'log_group_id' in kwargs:
        kwargs['log_analytics_log_group_id'] = kwargs['log_group_id']
        kwargs.pop('log_group_id')
    ctx.invoke(loganalytics_cli.get_log_analytics_log_group, **kwargs)


# log-group update param changes
@cli_util.copy_params_from_generated_command(loganalytics_cli.update_log_analytics_log_group, params_to_exclude=['log_analytics_log_group_id'])
@loganalytics_cli.log_analytics_log_group_group.command(name='update', help=loganalytics_cli.update_log_analytics_log_group.help)
@cli_util.option("--log-group-id", help='''The log group OCID''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsLogGroup'})
@cli_util.wrap_exceptions
def update_log_analytics_log_group_extended(ctx, **kwargs):
    if 'log_group_id' in kwargs:
        kwargs['log_analytics_log_group_id'] = kwargs['log_group_id']
        kwargs.pop('log_group_id')
    ctx.invoke(loganalytics_cli.update_log_analytics_log_group, **kwargs)


# log-group change-compartment param changes
@cli_util.copy_params_from_generated_command(loganalytics_cli.change_log_analytics_log_group_compartment, params_to_exclude=['log_analytics_log_group_id'])
@loganalytics_cli.log_analytics_log_group_group.command(name='change-compartment', help=loganalytics_cli.change_log_analytics_log_group_compartment.help)
@cli_util.option("--log-group-id", help='''The log group OCID''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_log_analytics_log_group_compartment_extended(ctx, **kwargs):
    if 'log_group_id' in kwargs:
        kwargs['log_analytics_log_group_id'] = kwargs['log_group_id']
        kwargs.pop('log_group_id')
    ctx.invoke(loganalytics_cli.change_log_analytics_log_group_compartment, **kwargs)


# log-group delete param changes
@cli_util.copy_params_from_generated_command(loganalytics_cli.delete_log_analytics_log_group, params_to_exclude=['log_analytics_log_group_id'])
@loganalytics_cli.log_analytics_log_group_group.command(name='delete', help=loganalytics_cli.delete_log_analytics_log_group.help)
@cli_util.option("--log-group-id", help='''The log group OCID''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_log_analytics_log_group_extended(ctx, **kwargs):
    if 'log_group_id' in kwargs:
        kwargs['log_analytics_log_group_id'] = kwargs['log_group_id']
        kwargs.pop('log_group_id')
    ctx.invoke(loganalytics_cli.delete_log_analytics_log_group, **kwargs)


# list_associated_entities param changes
@cli_util.copy_params_from_generated_command(loganalytics_cli.list_associated_entities, params_to_exclude=['entity_type_display_name'])
@loganalytics_cli.log_analytics_associated_entity_collection_group.command(name='list-associated-entities', help=loganalytics_cli.list_associated_entities.help)
@cli_util.option("--entity-type-name", help='''Entity Type Display Name''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsAssociatedEntityCollection'})
@cli_util.wrap_exceptions
def list_associated_entities_extended(ctx, **kwargs):
    if 'entity_type_name' in kwargs:
        kwargs['entity_type_display_name'] = kwargs['entity_type_name']
        kwargs.pop('entity_type_name')
    ctx.invoke(loganalytics_cli.list_associated_entities, **kwargs)


# list-entity-source-associations param changes
@cli_util.copy_params_from_generated_command(loganalytics_cli.list_entity_source_associations, params_to_exclude=['entity_type_display_name'])
@loganalytics_cli.log_analytics_association_collection_group.command(name='list-entity-source-assocs', help=loganalytics_cli.list_entity_source_associations.help)
@cli_util.option("--entity-type-name", help='''Entity Type Display Name''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsAssociationCollection'})
@cli_util.wrap_exceptions
def list_entity_source_associations_extended(ctx, **kwargs):
    if 'entity_type_name' in kwargs:
        kwargs['entity_type_display_name'] = kwargs['entity_type_name']
        kwargs.pop('entity_type_name')
    ctx.invoke(loganalytics_cli.list_entity_source_associations, **kwargs)


# import-custom-content read from file
@cli_util.copy_params_from_generated_command(loganalytics_cli.import_custom_content, params_to_exclude=['import_custom_content_file_body'])
@loganalytics_cli.log_analytics_import_custom_content_group.command(name='import-custom-content', help=loganalytics_cli.import_custom_content.help)
@cli_util.option('--file', type=click.File(mode='rb'), required=True, help='''Path to the custom content file''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsImportCustomContent'})
@cli_util.wrap_exceptions
def import_custom_content_extended(ctx, **kwargs):
    # Set "--import-custom-content-file-body" to the content of file "--file"
    if 'file' in kwargs and kwargs['file']:
        content = kwargs['file'].read()
        kwargs['import_custom_content_file_body'] = content
    del kwargs['file']
    ctx.invoke(loganalytics_cli.import_custom_content, **kwargs)


# register-lookup read from file
@cli_util.copy_params_from_generated_command(loganalytics_cli.register_lookup, params_to_exclude=['register_lookup_content_file_body'])
@loganalytics_cli.log_analytics_lookup_group.command(name='register-lookup', help=loganalytics_cli.register_lookup.help)
@cli_util.option('--file', type=click.File(mode='rb'), required=True, help='''Path to the lookup content file''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsLookup'})
@cli_util.wrap_exceptions
def register_lookup_extended(ctx, **kwargs):
    # Set "--register-lookup-content-file-body" to the content of file "--file"
    if 'file' in kwargs and kwargs['file']:
        content = kwargs['file'].read()
        kwargs['register_lookup_content_file_body'] = content
    del kwargs['file']
    ctx.invoke(loganalytics_cli.register_lookup, **kwargs)


# extract-structured-log-field-paths param changes
@cli_util.copy_params_from_generated_command(loganalytics_cli.extract_structured_log_field_paths, params_to_exclude=['parser_ignoreline_characters', 'should_tokenize_original_text'])
@loganalytics_cli.log_analytics_parser_group.command(name='extract-structured-log-field-paths', help=loganalytics_cli.extract_structured_log_field_paths.help)
@cli_util.option("--parser-ignoreline-chars", help='''Ignore line characters''')
@cli_util.option("--tokenize-original-text", help='''Tokenize original text: true/false''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'field-maps': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserField]'}, 'mapped-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'parser-filter': {'module': 'log_analytics', 'class': 'LogAnalyticsParserFilter'}, 'parser-functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserFunction]'}, 'sources': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSource]'}}, output_type={'module': 'log_analytics', 'class': 'ExtractLogFieldResults'})
@cli_util.wrap_exceptions
def extract_structured_log_field_paths_extended(ctx, **kwargs):
    if 'parser_ignoreline_chars' in kwargs:
        kwargs['parser_ignoreline_characters'] = kwargs['parser_ignoreline_chars']
        kwargs.pop('parser_ignoreline_chars')

    if 'tokenize_original_text' in kwargs:
        kwargs['should_tokenize_original_text'] = kwargs['tokenize_original_text']
        kwargs.pop('tokenize_original_text')

    ctx.invoke(loganalytics_cli.extract_structured_log_field_paths, **kwargs)


# extract-structured-log-header-paths param changes
@cli_util.copy_params_from_generated_command(loganalytics_cli.extract_structured_log_header_paths, params_to_exclude=['parser_ignoreline_characters', 'should_tokenize_original_text'])
@loganalytics_cli.log_analytics_parser_group.command(name='extract-structured-log-header-paths', help=loganalytics_cli.extract_structured_log_header_paths.help)
@cli_util.option("--parser-ignoreline-chars", help='''Ignore line characters''')
@cli_util.option("--tokenize-original-text", help='''Tokenize original text: true/false''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'field-maps': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserField]'}, 'mapped-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'parser-filter': {'module': 'log_analytics', 'class': 'LogAnalyticsParserFilter'}, 'parser-functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserFunction]'}, 'sources': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSource]'}}, output_type={'module': 'log_analytics', 'class': 'ExtractLogHeaderResults'})
@cli_util.wrap_exceptions
def extract_structured_log_header_paths_extended(ctx, **kwargs):
    if 'parser_ignoreline_chars' in kwargs:
        kwargs['parser_ignoreline_characters'] = kwargs['parser_ignoreline_chars']
        kwargs.pop('parser_ignoreline_chars')

    if 'tokenize_original_text' in kwargs:
        kwargs['should_tokenize_original_text'] = kwargs['tokenize_original_text']
        kwargs.pop('tokenize_original_text')

    ctx.invoke(loganalytics_cli.extract_structured_log_header_paths, **kwargs)


# test-parser param changes
@cli_util.copy_params_from_generated_command(loganalytics_cli.test_parser, params_to_exclude=['parser_ignoreline_characters', 'should_tokenize_original_text'])
@loganalytics_cli.log_analytics_parser_group.command(name='test-parser', help=loganalytics_cli.test_parser.help)
@cli_util.option("--parser-ignoreline-chars", help='''Ignore line characters''')
@cli_util.option("--tokenize-original-text", help='''Tokenize original text: true/false''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'field-maps': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserField]'}, 'metadata': {'module': 'log_analytics', 'class': 'UiParserTestMetadata'}, 'parser-functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserFunction]'}}, output_type={'module': 'log_analytics', 'class': 'ParserTestResult'})
@cli_util.wrap_exceptions
def test_parser_extended(ctx, **kwargs):
    if 'parser_ignoreline_chars' in kwargs:
        kwargs['parser_ignoreline_characters'] = kwargs['parser_ignoreline_chars']
        kwargs.pop('parser_ignoreline_chars')

    if 'tokenize_original_text' in kwargs:
        kwargs['should_tokenize_original_text'] = kwargs['tokenize_original_text']
        kwargs.pop('tokenize_original_text')

    ctx.invoke(loganalytics_cli.test_parser, **kwargs)


# upsert-parser param changes
@cli_util.copy_params_from_generated_command(loganalytics_cli.upsert_parser, params_to_exclude=['parser_ignoreline_characters', 'should_tokenize_original_text'])
@loganalytics_cli.log_analytics_parser_group.command(name='upsert-parser', help=loganalytics_cli.upsert_parser.help)
@cli_util.option("--parser-ignoreline-chars", help='''Ignore line characters''')
@cli_util.option("--tokenize-original-text", help='''Tokenize original text: true/false''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'field-maps': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserField]'}, 'parser-functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserFunction]'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsParser'})
@cli_util.wrap_exceptions
def upsert_parser_extended(ctx, **kwargs):
    if 'parser_ignoreline_chars' in kwargs:
        kwargs['parser_ignoreline_characters'] = kwargs['parser_ignoreline_chars']
        kwargs.pop('parser_ignoreline_chars')

    if 'tokenize_original_text' in kwargs:
        kwargs['should_tokenize_original_text'] = kwargs['tokenize_original_text']
        kwargs.pop('tokenize_original_text')

    ctx.invoke(loganalytics_cli.upsert_parser, **kwargs)


# list-source-extended-field-definitions command changes
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_source_group, loganalytics_cli.list_source_extended_field_definitions, "list-source-extfield-defs")


# list-source-meta-functions command changes
cli_util.rename_command(loganalytics_cli, loganalytics_cli.log_analytics_source_group, loganalytics_cli.list_source_meta_functions, "list-source-functions")


# upsert-source param changes
@cli_util.copy_params_from_generated_command(loganalytics_cli.upsert_source, params_to_exclude=['extended_field_definitions'])
@loganalytics_cli.log_analytics_source_group.command(name='upsert-source', help=loganalytics_cli.upsert_source.help)
@cli_util.option("--extfield-defs", help='''Extended field definitions''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'label-conditions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceLabelCondition]'}, 'data-filter-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceDataFilter]'}, 'extfield_defs': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceExtendedFieldDefinition]'}, 'labels': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelView]'}, 'metric-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsMetric]'}, 'metrics': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetric]'}, 'oob-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'parameters': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParameter]'}, 'patterns': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourcePattern]'}, 'functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceFunction]'}, 'parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'metadata-fields': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetadataField]'}, 'label-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelDefinition]'}, 'entity-types': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceEntityType]'}, 'user-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsSource'})
@cli_util.wrap_exceptions
def upsert_source_extended(ctx, **kwargs):
    if 'extfield_defs' in kwargs:
        kwargs['extended_field_definitions'] = kwargs['extfield_defs']
        kwargs.pop('extfield_defs')
    ctx.invoke(loganalytics_cli.upsert_source, **kwargs)


# validate-source param changes
@cli_util.copy_params_from_generated_command(loganalytics_cli.validate_source, params_to_exclude=['extended_field_definitions'])
@loganalytics_cli.log_analytics_source_group.command(name='validate-source', help=loganalytics_cli.validate_source.help)
@cli_util.option("--extfield-defs", help='''Extended field definitions''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'label-conditions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceLabelCondition]'}, 'data-filter-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceDataFilter]'}, 'extfield_defs': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceExtendedFieldDefinition]'}, 'labels': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelView]'}, 'metric-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsMetric]'}, 'metrics': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetric]'}, 'oob-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'parameters': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParameter]'}, 'patterns': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourcePattern]'}, 'functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceFunction]'}, 'parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'metadata-fields': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetadataField]'}, 'label-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelDefinition]'}, 'entity-types': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceEntityType]'}, 'user-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}}, output_type={'module': 'log_analytics', 'class': 'SourceValidateResults'})
@cli_util.wrap_exceptions
def validate_source_extended(ctx, **kwargs):
    if 'extfield_defs' in kwargs:
        kwargs['extended_field_definitions'] = kwargs['extfield_defs']
        kwargs.pop('extfield_defs')
    ctx.invoke(loganalytics_cli.validate_source, **kwargs)


# validate_source_extended_field_details param changes
@cli_util.copy_params_from_generated_command(loganalytics_cli.validate_source_extended_field_details, params_to_exclude=['association_count', 'association_entity', 'extended_field_definitions', 'is_auto_association_enabled', 'is_auto_association_override'])
@loganalytics_cli.extended_fields_validation_result_group.command(name='validate-source-extfield-details', help=loganalytics_cli.validate_source_extended_field_details.help)
@cli_util.option("--assoc-count", help='''Association count''')
@cli_util.option("--assoc-entity", help='''Association entity''')
@cli_util.option("--extfield-defs", help='''Extended Field Definitions''')
@cli_util.option("--is-auto-assoc-enabled", help='''Auto associaton enabled flag''')
@cli_util.option("--is-auto-assoc-override", help='''Auto associaton override flag''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'label-conditions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceLabelCondition]'}, 'assoc-entity': {'module': 'log_analytics', 'class': 'list[LogAnalyticsAssociation]'}, 'data-filter-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceDataFilter]'}, 'extfield_defs': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceExtendedFieldDefinition]'}, 'labels': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelView]'}, 'metric-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsMetric]'}, 'metrics': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetric]'}, 'oob-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'parameters': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParameter]'}, 'patterns': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourcePattern]'}, 'functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceFunction]'}, 'parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'metadata-fields': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetadataField]'}, 'label-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelDefinition]'}, 'entity-types': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceEntityType]'}, 'user-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}}, output_type={'module': 'log_analytics', 'class': 'ExtendedFieldsValidationResult'})
@cli_util.wrap_exceptions
def validate_source_extended_field_details_extended(ctx, **kwargs):
    if 'assoc_count' in kwargs:
        kwargs['association_count'] = kwargs['assoc_count']
        kwargs.pop('assoc_count')

    if 'assoc_entity' in kwargs:
        kwargs['association_entity'] = kwargs['assoc_entity']
        kwargs.pop('assoc_entity')

    if 'extfield_defs' in kwargs:
        kwargs['extended_field_definitions'] = kwargs['extfield_defs']
        kwargs.pop('extfield_defs')

    if 'is_auto_assoc_enabled' in kwargs:
        kwargs['is_auto_association_enabled'] = kwargs['is_auto_assoc_enabled']
        kwargs.pop('is_auto_assoc_enabled')

    if 'is_auto_assoc_override' in kwargs:
        kwargs['is_auto_association_override'] = kwargs['is_auto_assoc_override']
        kwargs.pop('is_auto_assoc_override')

    ctx.invoke(loganalytics_cli.validate_source_extended_field_details, **kwargs)

# ######################
# Param Changes - End
# ######################
