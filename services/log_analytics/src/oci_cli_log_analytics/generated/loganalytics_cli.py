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


@cli.command(cli_util.override('log_analytics.log_analytics_root_group.command_name', 'log-analytics'), cls=CommandGroupWithAlias, help=cli_util.override('log_analytics.log_analytics_root_group.help', """The LogAnalytics API for the LogAnalytics service."""), short_help=cli_util.override('log_analytics.log_analytics_root_group.short_help', """LogAnalytics API"""))
@cli_util.help_option_group
def log_analytics_root_group():
    pass


@click.command(cli_util.override('log_analytics.log_analytics_config_work_request_group.command_name', 'log-analytics-config-work-request'), cls=CommandGroupWithAlias, help="""LogAnalyticsConfigWorkRequest""")
@cli_util.help_option_group
def log_analytics_config_work_request_group():
    pass


@click.command(cli_util.override('log_analytics.scheduled_task_group.command_name', 'scheduled-task'), cls=CommandGroupWithAlias, help="""Log analytics scheduled task resource.""")
@cli_util.help_option_group
def scheduled_task_group():
    pass


@click.command(cli_util.override('log_analytics.upload_group.command_name', 'upload'), cls=CommandGroupWithAlias, help="""Upload is a container that can be used to optionally put all the relevant and related on-demand upload based log files.""")
@cli_util.help_option_group
def upload_group():
    pass


@click.command(cli_util.override('log_analytics.log_analytics_import_custom_content_group.command_name', 'log-analytics-import-custom-content'), cls=CommandGroupWithAlias, help="""LogAnalyticsImportCustomContent""")
@cli_util.help_option_group
def log_analytics_import_custom_content_group():
    pass


@click.command(cli_util.override('log_analytics.log_analytics_field_group.command_name', 'log-analytics-field'), cls=CommandGroupWithAlias, help="""Field Details""")
@cli_util.help_option_group
def log_analytics_field_group():
    pass


@click.command(cli_util.override('log_analytics.storage_group.command_name', 'storage'), cls=CommandGroupWithAlias, help="""This is the storage configuration and status of a tenancy in Logan Analytics application""")
@cli_util.help_option_group
def storage_group():
    pass


@click.command(cli_util.override('log_analytics.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('log_analytics.log_analytics_entity_type_group.command_name', 'log-analytics-entity-type'), cls=CommandGroupWithAlias, help="""Description of log analytics entity type.""")
@cli_util.help_option_group
def log_analytics_entity_type_group():
    pass


@click.command(cli_util.override('log_analytics.log_analytics_object_collection_rule_group.command_name', 'log-analytics-object-collection-rule'), cls=CommandGroupWithAlias, help="""The configuration details of an Object Storage based collection rule.""")
@cli_util.help_option_group
def log_analytics_object_collection_rule_group():
    pass


@click.command(cli_util.override('log_analytics.log_analytics_lookup_group.command_name', 'log-analytics-lookup'), cls=CommandGroupWithAlias, help="""LogAnalyticsLookup""")
@cli_util.help_option_group
def log_analytics_lookup_group():
    pass


@click.command(cli_util.override('log_analytics.work_request_log_group.command_name', 'work-request-log'), cls=CommandGroupWithAlias, help="""This is a log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_group():
    pass


@click.command(cli_util.override('log_analytics.log_analytics_label_group.command_name', 'log-analytics-label'), cls=CommandGroupWithAlias, help="""LogAnalytics label""")
@cli_util.help_option_group
def log_analytics_label_group():
    pass


@click.command(cli_util.override('log_analytics.log_analytics_entity_group.command_name', 'log-analytics-entity'), cls=CommandGroupWithAlias, help="""Description of a log analytics entity.""")
@cli_util.help_option_group
def log_analytics_entity_group():
    pass


@click.command(cli_util.override('log_analytics.char_encoding_collection_group.command_name', 'char-encoding-collection'), cls=CommandGroupWithAlias, help="""List of supported character encodings""")
@cli_util.help_option_group
def char_encoding_collection_group():
    pass


@click.command(cli_util.override('log_analytics.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('log_analytics.namespace_group.command_name', 'namespace'), cls=CommandGroupWithAlias, help="""This is the namespace details of a tenancy in Logan Analytics application""")
@cli_util.help_option_group
def namespace_group():
    pass


@click.command(cli_util.override('log_analytics.timezone_collection_group.command_name', 'timezone-collection'), cls=CommandGroupWithAlias, help="""List of supported timezones.""")
@cli_util.help_option_group
def timezone_collection_group():
    pass


@click.command(cli_util.override('log_analytics.log_analytics_log_group_group.command_name', 'log-analytics-log-group'), cls=CommandGroupWithAlias, help="""Summary of an Log-Analytics log group.""")
@cli_util.help_option_group
def log_analytics_log_group_group():
    pass


@click.command(cli_util.override('log_analytics.log_analytics_source_group.command_name', 'log-analytics-source'), cls=CommandGroupWithAlias, help="""LogAnalyticsSource""")
@cli_util.help_option_group
def log_analytics_source_group():
    pass


@click.command(cli_util.override('log_analytics.log_analytics_parser_group.command_name', 'log-analytics-parser'), cls=CommandGroupWithAlias, help="""LoganParserDetails""")
@cli_util.help_option_group
def log_analytics_parser_group():
    pass


@click.command(cli_util.override('log_analytics.query_details_group.command_name', 'query-details'), cls=CommandGroupWithAlias, help="""Input arguments for running a log anlaytics query. If the request is set to run in asynchronous mode then shouldIncludeColumns and shouldIncludeFields can be overwritten when retrieving the results.""")
@cli_util.help_option_group
def query_details_group():
    pass


@click.command(cli_util.override('log_analytics.log_analytics_association_group.command_name', 'log-analytics-association'), cls=CommandGroupWithAlias, help="""LogAnalyticsAssociation""")
@cli_util.help_option_group
def log_analytics_association_group():
    pass


@click.command(cli_util.override('log_analytics.query_work_request_group.command_name', 'query-work-request'), cls=CommandGroupWithAlias, help="""Job details outlining parameters specified when job was submitted.""")
@cli_util.help_option_group
def query_work_request_group():
    pass


@click.command(cli_util.override('log_analytics.binary_group.command_name', 'binary'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def binary_group():
    pass


log_analytics_root_group.add_command(log_analytics_config_work_request_group)
log_analytics_root_group.add_command(scheduled_task_group)
log_analytics_root_group.add_command(upload_group)
log_analytics_root_group.add_command(log_analytics_import_custom_content_group)
log_analytics_root_group.add_command(log_analytics_field_group)
log_analytics_root_group.add_command(storage_group)
log_analytics_root_group.add_command(work_request_group)
log_analytics_root_group.add_command(log_analytics_entity_type_group)
log_analytics_root_group.add_command(log_analytics_object_collection_rule_group)
log_analytics_root_group.add_command(log_analytics_lookup_group)
log_analytics_root_group.add_command(work_request_log_group)
log_analytics_root_group.add_command(log_analytics_label_group)
log_analytics_root_group.add_command(log_analytics_entity_group)
log_analytics_root_group.add_command(char_encoding_collection_group)
log_analytics_root_group.add_command(work_request_error_group)
log_analytics_root_group.add_command(namespace_group)
log_analytics_root_group.add_command(timezone_collection_group)
log_analytics_root_group.add_command(log_analytics_log_group_group)
log_analytics_root_group.add_command(log_analytics_source_group)
log_analytics_root_group.add_command(log_analytics_parser_group)
log_analytics_root_group.add_command(query_details_group)
log_analytics_root_group.add_command(log_analytics_association_group)
log_analytics_root_group.add_command(query_work_request_group)
log_analytics_root_group.add_command(binary_group)


@log_analytics_entity_group.command(name=cli_util.override('log_analytics.add_entity_association.command_name', 'add'), help=u"""Adds association between input source log analytics entity and destination entities. \n[Command Reference](addEntityAssociation)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--log-analytics-entity-id', required=True, help=u"""The log analytics entity OCID.""")
@cli_util.option('--association-entities', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Destination entities OCIDs with which associations are to be added.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'association-entities': {'module': 'log_analytics', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'association-entities': {'module': 'log_analytics', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def add_entity_association(ctx, from_json, namespace_name, log_analytics_entity_id, association_entities, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(log_analytics_entity_id, six.string_types) and len(log_analytics_entity_id.strip()) == 0:
        raise click.UsageError('Parameter --log-analytics-entity-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['associationEntities'] = cli_util.parse_json_parameter("association_entities", association_entities)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.add_entity_association(
        namespace_name=namespace_name,
        log_analytics_entity_id=log_analytics_entity_id,
        add_entity_association_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_label_group.command(name=cli_util.override('log_analytics.batch_get_basic_info.command_name', 'batch-get-basic-info'), help=u"""get basic information about a specified set of labels \n[Command Reference](batchGetBasicInfo)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--is-include-deleted', required=True, type=click.BOOL, help=u"""flag for whether or not to include information on deleted labels""")
@cli_util.option('--label-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""string list""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--basic-label-sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "priority"]), help=u"""sort by label""")
@json_skeleton_utils.get_cli_json_input_option({'label-names': {'module': 'log_analytics', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'label-names': {'module': 'log_analytics', 'class': 'list[string]'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsLabelCollection'})
@cli_util.wrap_exceptions
def batch_get_basic_info(ctx, from_json, namespace_name, is_include_deleted, label_names, limit, page, sort_order, basic_label_sort_by):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if basic_label_sort_by is not None:
        kwargs['basic_label_sort_by'] = basic_label_sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if label_names is not None:
        _details['labelNames'] = cli_util.parse_json_parameter("label_names", label_names)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.batch_get_basic_info(
        namespace_name=namespace_name,
        is_include_deleted=is_include_deleted,
        basic_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@query_work_request_group.command(name=cli_util.override('log_analytics.cancel_query_work_request.command_name', 'cancel'), help=u"""Cancel/Remove query job work request. \n[Command Reference](cancelQueryWorkRequest)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--work-request-id', required=True, help=u"""Work Request Identifier [OCID]  for the asynchronous request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_query_work_request(ctx, from_json, namespace_name, work_request_id, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.cancel_query_work_request(
        namespace_name=namespace_name,
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_entity_group.command(name=cli_util.override('log_analytics.change_log_analytics_entity_compartment.command_name', 'change-compartment'), help=u"""Update the compartment of the log analytics entity with the given id. \n[Command Reference](changeLogAnalyticsEntityCompartment)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--log-analytics-entity-id', required=True, help=u"""The log analytics entity OCID.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where the log analytics entity should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_log_analytics_entity_compartment(ctx, from_json, namespace_name, log_analytics_entity_id, compartment_id, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(log_analytics_entity_id, six.string_types) and len(log_analytics_entity_id.strip()) == 0:
        raise click.UsageError('Parameter --log-analytics-entity-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.change_log_analytics_entity_compartment(
        namespace_name=namespace_name,
        log_analytics_entity_id=log_analytics_entity_id,
        change_log_analytics_entity_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_log_group_group.command(name=cli_util.override('log_analytics.change_log_analytics_log_group_compartment.command_name', 'change-compartment'), help=u"""Updates the compartment of the Log-Analytics group with the given id. \n[Command Reference](changeLogAnalyticsLogGroupCompartment)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--log-analytics-log-group-id', required=True, help=u"""unique logAnalytics log group identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where the log analytics entity should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_log_analytics_log_group_compartment(ctx, from_json, namespace_name, log_analytics_log_group_id, compartment_id, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(log_analytics_log_group_id, six.string_types) and len(log_analytics_log_group_id.strip()) == 0:
        raise click.UsageError('Parameter --log-analytics-log-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.change_log_analytics_log_group_compartment(
        namespace_name=namespace_name,
        log_analytics_log_group_id=log_analytics_log_group_id,
        change_log_analytics_log_group_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_object_collection_rule_group.command(name=cli_util.override('log_analytics.change_log_analytics_object_collection_rule_compartment.command_name', 'change-compartment'), help=u"""Move the rule from it's current compartment to given compartment. \n[Command Reference](changeLogAnalyticsObjectCollectionRuleCompartment)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--log-analytics-object-collection-rule-id', required=True, help=u"""The Logging Analytics Object Collection Rule [OCID]""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the rule should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_log_analytics_object_collection_rule_compartment(ctx, from_json, namespace_name, log_analytics_object_collection_rule_id, compartment_id, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(log_analytics_object_collection_rule_id, six.string_types) and len(log_analytics_object_collection_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --log-analytics-object-collection-rule-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.change_log_analytics_object_collection_rule_compartment(
        namespace_name=namespace_name,
        log_analytics_object_collection_rule_id=log_analytics_object_collection_rule_id,
        change_log_analytics_object_collection_rule_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@scheduled_task_group.command(name=cli_util.override('log_analytics.change_scheduled_task_compartment.command_name', 'change-compartment'), help=u"""Move the scheduled task into a different compartment within the same tenancy. \n[Command Reference](changeScheduledTaskCompartment)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--scheduled-task-id', required=True, help=u"""Unique scheduledTask id returned from task create. If invalid will lead to a 404 not found.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID] .""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_scheduled_task_compartment(ctx, from_json, namespace_name, scheduled_task_id, compartment_id, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(scheduled_task_id, six.string_types) and len(scheduled_task_id.strip()) == 0:
        raise click.UsageError('Parameter --scheduled-task-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.change_scheduled_task_compartment(
        namespace_name=namespace_name,
        scheduled_task_id=scheduled_task_id,
        change_scheduled_task_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@scheduled_task_group.command(name=cli_util.override('log_analytics.clean.command_name', 'clean'), help=u"""Clean accumulated acceleration data stored for the accelerated saved search. The ScheduledTask taskType must be ACCELERATION. \n[Command Reference](clean)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--scheduled-task-id', required=True, help=u"""Unique scheduledTask id returned from task create. If invalid will lead to a 404 not found.""")
@cli_util.option('--time-start', type=custom_types.CLI_DATETIME, help=u"""Optional parameter to specify start of time range, in the format defined by RFC3339. Default value is beginning of time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', type=custom_types.CLI_DATETIME, help=u"""Optional parameter to specify end of time range, in the format defined by RFC3339. Default value is end of time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def clean(ctx, from_json, namespace_name, scheduled_task_id, time_start, time_end):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(scheduled_task_id, six.string_types) and len(scheduled_task_id.strip()) == 0:
        raise click.UsageError('Parameter --scheduled-task-id cannot be whitespace or empty string')

    kwargs = {}
    if time_start is not None:
        kwargs['time_start'] = time_start
    if time_end is not None:
        kwargs['time_end'] = time_end
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.clean(
        namespace_name=namespace_name,
        scheduled_task_id=scheduled_task_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_entity_group.command(name=cli_util.override('log_analytics.create_log_analytics_entity.command_name', 'create'), help=u"""Create a new log analytics entity. \n[Command Reference](createLogAnalyticsEntity)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--name', required=True, help=u"""Log analytics entity name. The name must be unique, within the tenancy, and cannot be changed.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID] .""")
@cli_util.option('--entity-type-name', required=True, help=u"""Log analytics entity type name.""")
@cli_util.option('--management-agent-id', help=u"""The OCID of the Management Agent.""")
@cli_util.option('--cloud-resource-id', help=u"""The OCID of the Cloud resource which this entity is a representation of. This may be blank when the entity represents a non-cloud resource that the customer may have on their premises.""")
@cli_util.option('--timezone-region', help=u"""The timezone region of the log analytics entity.""")
@cli_util.option('--hostname', help=u"""The hostname where the entity represented here is actually present. This would be the output one would get if they run `echo $HOSTNAME` on Linux or an equivalent OS command. This may be different from management agents host since logs may be collected remotely.""")
@cli_util.option('--source-id', help=u"""This indicates the type of source. It is primarily for Enterprise Manager Repository ID.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The name/value pairs for parameter values to be used in file patterns specified in log sources.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsEntity'})
@cli_util.wrap_exceptions
def create_log_analytics_entity(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, name, compartment_id, entity_type_name, management_agent_id, cloud_resource_id, timezone_region, hostname, source_id, properties, freeform_tags, defined_tags):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['entityTypeName'] = entity_type_name

    if management_agent_id is not None:
        _details['managementAgentId'] = management_agent_id

    if cloud_resource_id is not None:
        _details['cloudResourceId'] = cloud_resource_id

    if timezone_region is not None:
        _details['timezoneRegion'] = timezone_region

    if hostname is not None:
        _details['hostname'] = hostname

    if source_id is not None:
        _details['sourceId'] = source_id

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.create_log_analytics_entity(
        namespace_name=namespace_name,
        create_log_analytics_entity_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_log_analytics_entity') and callable(getattr(client, 'get_log_analytics_entity')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_log_analytics_entity(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@log_analytics_entity_type_group.command(name=cli_util.override('log_analytics.create_log_analytics_entity_type.command_name', 'create'), help=u"""Add custom log analytics entity type. \n[Command Reference](createLogAnalyticsEntityType)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--name', required=True, help=u"""Log analytics entity type name.""")
@cli_util.option('--category', help=u"""Log analytics entity type category. Category will be used for grouping and filtering.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Log analytics entity type property definition.

This option is a JSON list with items of type EntityTypeProperty.  For documentation on EntityTypeProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/EntityTypeProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'log_analytics', 'class': 'list[EntityTypeProperty]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'log_analytics', 'class': 'list[EntityTypeProperty]'}})
@cli_util.wrap_exceptions
def create_log_analytics_entity_type(ctx, from_json, namespace_name, name, category, properties):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name

    if category is not None:
        _details['category'] = category

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.create_log_analytics_entity_type(
        namespace_name=namespace_name,
        create_log_analytics_entity_type_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_log_group_group.command(name=cli_util.override('log_analytics.create_log_analytics_log_group.command_name', 'create'), help=u"""Creates a new Log-Analytics group. \n[Command Reference](createLogAnalyticsLogGroup)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name that is changeable and that does not have to be unique. Format: a leading alphanumeric, followed by zero or more alphanumerics, underscores, spaces, backslashes, or hyphens in any order). No trailing spaces allowed.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID] .""")
@cli_util.option('--description', help=u"""Description for this resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsLogGroup'})
@cli_util.wrap_exceptions
def create_log_analytics_log_group(ctx, from_json, namespace_name, display_name, compartment_id, description, freeform_tags, defined_tags):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.create_log_analytics_log_group(
        namespace_name=namespace_name,
        create_log_analytics_log_group_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_object_collection_rule_group.command(name=cli_util.override('log_analytics.create_log_analytics_object_collection_rule.command_name', 'create'), help=u"""Create a configuration to collect logs from object storage bucket. \n[Command Reference](createLogAnalyticsObjectCollectionRule)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--name', required=True, help=u"""A unique name given to the rule. The name must be unique within the tenancy, and cannot be modified.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to which this rule belongs.""")
@cli_util.option('--os-namespace', required=True, help=u"""Object Storage namespace.""")
@cli_util.option('--os-bucket-name', required=True, help=u"""Name of the Object Storage bucket.""")
@cli_util.option('--log-group-id', required=True, help=u"""Logging Analytics Log group OCID to associate the processed logs with.""")
@cli_util.option('--log-source-name', required=True, help=u"""Name of the Logging Analytics Source to use for the processing.""")
@cli_util.option('--description', help=u"""A string that describes the details of the rule. It does not have to be unique, and can be changed. Avoid entering confidential information.""")
@cli_util.option('--collection-type', type=custom_types.CliCaseInsensitiveChoice(["LIVE", "HISTORIC", "HISTORIC_LIVE"]), help=u"""The type of collection. Supported collection types: LIVE, HISTORIC, HISTORIC_LIVE""")
@cli_util.option('--poll-since', help=u"""The oldest time of the file in the bucket to consider for collection. Accepted values are: BEGINNING or CURRENT_TIME or RFC3339 formatted datetime string. When collectionType is LIVE, specifying pollSince value other than CURRENT_TIME will result in error.""")
@cli_util.option('--poll-till', help=u"""The oldest time of the file in the bucket to consider for collection. Accepted values are: CURRENT_TIME or RFC3339 formatted datetime string. When collectionType is LIVE, specifying pollTill will result in error.""")
@cli_util.option('--entity-id', help=u"""Logging Analytics entity OCID. Associates the processed logs with the given entity (optional).""")
@cli_util.option('--char-encoding', help=u"""An optional character encoding to aid in detecting the character encoding of the contents of the objects while processing. It is recommended to set this value as ISO_8589_1 when configuring content of the objects having more numeric characters, and very few alphabets. For e.g. this applies when configuring VCN Flow Logs.""")
@cli_util.option('--overrides', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The override is used to modify some important configuration properties for objects matching a specific pattern inside the bucket. Supported propeties for override are - logSourceName, charEncoding. Supported matchType for override are \"contains\".""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'overrides': {'module': 'log_analytics', 'class': 'dict(str, list[PropertyOverride])'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'overrides': {'module': 'log_analytics', 'class': 'dict(str, list[PropertyOverride])'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsObjectCollectionRule'})
@cli_util.wrap_exceptions
def create_log_analytics_object_collection_rule(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, name, compartment_id, os_namespace, os_bucket_name, log_group_id, log_source_name, description, collection_type, poll_since, poll_till, entity_id, char_encoding, overrides, defined_tags, freeform_tags):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['osNamespace'] = os_namespace
    _details['osBucketName'] = os_bucket_name
    _details['logGroupId'] = log_group_id
    _details['logSourceName'] = log_source_name

    if description is not None:
        _details['description'] = description

    if collection_type is not None:
        _details['collectionType'] = collection_type

    if poll_since is not None:
        _details['pollSince'] = poll_since

    if poll_till is not None:
        _details['pollTill'] = poll_till

    if entity_id is not None:
        _details['entityId'] = entity_id

    if char_encoding is not None:
        _details['charEncoding'] = char_encoding

    if overrides is not None:
        _details['overrides'] = cli_util.parse_json_parameter("overrides", overrides)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.create_log_analytics_object_collection_rule(
        namespace_name=namespace_name,
        create_log_analytics_object_collection_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_log_analytics_object_collection_rule') and callable(getattr(client, 'get_log_analytics_object_collection_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_log_analytics_object_collection_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@scheduled_task_group.command(name=cli_util.override('log_analytics.create_scheduled_task.command_name', 'create'), help=u"""Schedule a task as specified and return task info. \n[Command Reference](createScheduledTask)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--kind', required=True, type=custom_types.CliCaseInsensitiveChoice(["ACCELERATION", "STANDARD"]), help=u"""Discriminator.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID] .""")
@cli_util.option('--display-name', help=u"""A user-friendly name that is changeable and that does not have to be unique. Format: a leading alphanumeric, followed by zero or more alphanumerics, underscores, spaces, backslashes, or hyphens in any order). No trailing spaces allowed.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'log_analytics', 'class': 'ScheduledTask'})
@cli_util.wrap_exceptions
def create_scheduled_task(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, kind, compartment_id, display_name, freeform_tags, defined_tags):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['kind'] = kind
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.create_scheduled_task(
        namespace_name=namespace_name,
        create_scheduled_task_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_scheduled_task') and callable(getattr(client, 'get_scheduled_task')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_scheduled_task(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@scheduled_task_group.command(name=cli_util.override('log_analytics.create_scheduled_task_create_standard_task_details.command_name', 'create-scheduled-task-create-standard-task-details'), help=u"""Schedule a task as specified and return task info. \n[Command Reference](createScheduledTask)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID] .""")
@cli_util.option('--task-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SAVED_SEARCH", "ACCELERATION", "PURGE", "ACCELERATION_MAINTENANCE"]), help=u"""Task type.""")
@cli_util.option('--schedules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Schedules, typically a single schedule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--action', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name that is changeable and that does not have to be unique. Format: a leading alphanumeric, followed by zero or more alphanumerics, underscores, spaces, backslashes, or hyphens in any order). No trailing spaces allowed.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}, 'schedules': {'module': 'log_analytics', 'class': 'list[Schedule]'}, 'action': {'module': 'log_analytics', 'class': 'Action'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}, 'schedules': {'module': 'log_analytics', 'class': 'list[Schedule]'}, 'action': {'module': 'log_analytics', 'class': 'Action'}}, output_type={'module': 'log_analytics', 'class': 'ScheduledTask'})
@cli_util.wrap_exceptions
def create_scheduled_task_create_standard_task_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, compartment_id, task_type, schedules, action, display_name, freeform_tags, defined_tags):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['taskType'] = task_type
    _details['schedules'] = cli_util.parse_json_parameter("schedules", schedules)
    _details['action'] = cli_util.parse_json_parameter("action", action)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['kind'] = 'STANDARD'

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.create_scheduled_task(
        namespace_name=namespace_name,
        create_scheduled_task_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_scheduled_task') and callable(getattr(client, 'get_scheduled_task')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_scheduled_task(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@scheduled_task_group.command(name=cli_util.override('log_analytics.create_scheduled_task_create_acceleration_task_details.command_name', 'create-scheduled-task-create-acceleration-task-details'), help=u"""Schedule a task as specified and return task info. \n[Command Reference](createScheduledTask)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID] .""")
@cli_util.option('--saved-search-id', required=True, help=u"""The ManagementSavedSearch id [OCID] to be accelerated.""")
@cli_util.option('--display-name', help=u"""A user-friendly name that is changeable and that does not have to be unique. Format: a leading alphanumeric, followed by zero or more alphanumerics, underscores, spaces, backslashes, or hyphens in any order). No trailing spaces allowed.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'log_analytics', 'class': 'ScheduledTask'})
@cli_util.wrap_exceptions
def create_scheduled_task_create_acceleration_task_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, compartment_id, saved_search_id, display_name, freeform_tags, defined_tags):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['savedSearchId'] = saved_search_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['kind'] = 'ACCELERATION'

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.create_scheduled_task(
        namespace_name=namespace_name,
        create_scheduled_task_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_scheduled_task') and callable(getattr(client, 'get_scheduled_task')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_scheduled_task(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@log_analytics_association_group.command(name=cli_util.override('log_analytics.delete_associations.command_name', 'delete-associations'), help=u"""delete associations \n[Command Reference](deleteAssociations)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', help=u"""compartmentId""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""list of rule entity association details

This option is a JSON list with items of type DeleteLogAnalyticsAssociation.  For documentation on DeleteLogAnalyticsAssociation please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/DeleteLogAnalyticsAssociation.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'log_analytics', 'class': 'list[DeleteLogAnalyticsAssociation]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'log_analytics', 'class': 'list[DeleteLogAnalyticsAssociation]'}})
@cli_util.wrap_exceptions
def delete_associations(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, compartment_id, items):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.delete_associations(
        namespace_name=namespace_name,
        delete_log_analytics_association_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_config_work_request') and callable(getattr(client, 'get_config_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_config_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@log_analytics_field_group.command(name=cli_util.override('log_analytics.delete_field.command_name', 'delete-field'), help=u"""delete field with specified name \n[Command Reference](deleteField)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--field-name', required=True, help=u"""name of the field to get""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_field(ctx, from_json, namespace_name, field_name, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(field_name, six.string_types) and len(field_name.strip()) == 0:
        raise click.UsageError('Parameter --field-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.delete_field(
        namespace_name=namespace_name,
        field_name=field_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_label_group.command(name=cli_util.override('log_analytics.delete_label.command_name', 'delete-label'), help=u"""delete a label \n[Command Reference](deleteLabel)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--label-name', required=True, help=u"""name of the label to get""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_label(ctx, from_json, namespace_name, label_name, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(label_name, six.string_types) and len(label_name.strip()) == 0:
        raise click.UsageError('Parameter --label-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.delete_label(
        namespace_name=namespace_name,
        label_name=label_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_entity_group.command(name=cli_util.override('log_analytics.delete_log_analytics_entity.command_name', 'delete'), help=u"""Delete log analytics entity with the given id. \n[Command Reference](deleteLogAnalyticsEntity)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--log-analytics-entity-id', required=True, help=u"""The log analytics entity OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_log_analytics_entity(ctx, from_json, namespace_name, log_analytics_entity_id, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(log_analytics_entity_id, six.string_types) and len(log_analytics_entity_id.strip()) == 0:
        raise click.UsageError('Parameter --log-analytics-entity-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.delete_log_analytics_entity(
        namespace_name=namespace_name,
        log_analytics_entity_id=log_analytics_entity_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_entity_type_group.command(name=cli_util.override('log_analytics.delete_log_analytics_entity_type.command_name', 'delete'), help=u"""Delete the log analytics entity type with the given name. \n[Command Reference](deleteLogAnalyticsEntityType)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--entity-type-name', required=True, help=u"""Log analytics entity type name.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_log_analytics_entity_type(ctx, from_json, namespace_name, entity_type_name, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(entity_type_name, six.string_types) and len(entity_type_name.strip()) == 0:
        raise click.UsageError('Parameter --entity-type-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.delete_log_analytics_entity_type(
        namespace_name=namespace_name,
        entity_type_name=entity_type_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_log_group_group.command(name=cli_util.override('log_analytics.delete_log_analytics_log_group.command_name', 'delete'), help=u"""Deletes the Log-Analytics group with the given id. \n[Command Reference](deleteLogAnalyticsLogGroup)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--log-analytics-log-group-id', required=True, help=u"""unique logAnalytics log group identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_log_analytics_log_group(ctx, from_json, namespace_name, log_analytics_log_group_id, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(log_analytics_log_group_id, six.string_types) and len(log_analytics_log_group_id.strip()) == 0:
        raise click.UsageError('Parameter --log-analytics-log-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.delete_log_analytics_log_group(
        namespace_name=namespace_name,
        log_analytics_log_group_id=log_analytics_log_group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_object_collection_rule_group.command(name=cli_util.override('log_analytics.delete_log_analytics_object_collection_rule.command_name', 'delete'), help=u"""Deletes a configured object storage bucket based collection rule to stop the log collection of the configured bucket . It will not delete the already collected log data from the configured bucket. \n[Command Reference](deleteLogAnalyticsObjectCollectionRule)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--log-analytics-object-collection-rule-id', required=True, help=u"""The Logging Analytics Object Collection Rule [OCID]""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_log_analytics_object_collection_rule(ctx, from_json, namespace_name, log_analytics_object_collection_rule_id, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(log_analytics_object_collection_rule_id, six.string_types) and len(log_analytics_object_collection_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --log-analytics-object-collection-rule-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.delete_log_analytics_object_collection_rule(
        namespace_name=namespace_name,
        log_analytics_object_collection_rule_id=log_analytics_object_collection_rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_parser_group.command(name=cli_util.override('log_analytics.delete_parser.command_name', 'delete-parser'), help=u"""delete parser with specified name \n[Command Reference](deleteParser)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--parser-name', required=True, help=u"""parserName""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_parser(ctx, from_json, namespace_name, parser_name, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(parser_name, six.string_types) and len(parser_name.strip()) == 0:
        raise click.UsageError('Parameter --parser-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.delete_parser(
        namespace_name=namespace_name,
        parser_name=parser_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@scheduled_task_group.command(name=cli_util.override('log_analytics.delete_scheduled_task.command_name', 'delete'), help=u"""Delete the scheduled task. \n[Command Reference](deleteScheduledTask)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--scheduled-task-id', required=True, help=u"""Unique scheduledTask id returned from task create. If invalid will lead to a 404 not found.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_scheduled_task(ctx, from_json, namespace_name, scheduled_task_id, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(scheduled_task_id, six.string_types) and len(scheduled_task_id.strip()) == 0:
        raise click.UsageError('Parameter --scheduled-task-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.delete_scheduled_task(
        namespace_name=namespace_name,
        scheduled_task_id=scheduled_task_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_source_group.command(name=cli_util.override('log_analytics.delete_source.command_name', 'delete-source'), help=u"""delete source with specified ID \n[Command Reference](deleteSource)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--source-name', required=True, help=u"""source name""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_source(ctx, from_json, namespace_name, source_name, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(source_name, six.string_types) and len(source_name.strip()) == 0:
        raise click.UsageError('Parameter --source-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.delete_source(
        namespace_name=namespace_name,
        source_name=source_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@upload_group.command(name=cli_util.override('log_analytics.delete_upload.command_name', 'delete'), help=u"""Deletes an Upload by its reference. It deletes all the logs in storage asscoiated with the upload and the corresponding upload metadata. \n[Command Reference](deleteUpload)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--upload-reference', required=True, help=u"""Unique internal identifier to refer to upload container""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_upload(ctx, from_json, namespace_name, upload_reference, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(upload_reference, six.string_types) and len(upload_reference.strip()) == 0:
        raise click.UsageError('Parameter --upload-reference cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.delete_upload(
        namespace_name=namespace_name,
        upload_reference=upload_reference,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@upload_group.command(name=cli_util.override('log_analytics.delete_upload_file.command_name', 'delete-upload-file'), help=u"""Deletes a specific log file inside an upload by providing upload file reference. It deletes all the logs in storage asscoiated with the upload file and the corresponding upload metadata. \n[Command Reference](deleteUploadFile)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--upload-reference', required=True, help=u"""Unique internal identifier to refer to upload container""")
@cli_util.option('--file-reference', required=True, help=u"""Unique internal identifier to refer to upload file""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_upload_file(ctx, from_json, namespace_name, upload_reference, file_reference):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(upload_reference, six.string_types) and len(upload_reference.strip()) == 0:
        raise click.UsageError('Parameter --upload-reference cannot be whitespace or empty string')

    if isinstance(file_reference, six.string_types) and len(file_reference.strip()) == 0:
        raise click.UsageError('Parameter --file-reference cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.delete_upload_file(
        namespace_name=namespace_name,
        upload_reference=upload_reference,
        file_reference=file_reference,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@upload_group.command(name=cli_util.override('log_analytics.delete_upload_warning.command_name', 'delete-upload-warning'), help=u"""Suppresses a specific warning inside an upload. \n[Command Reference](deleteUploadWarning)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--upload-reference', required=True, help=u"""Unique internal identifier to refer to upload container""")
@cli_util.option('--warning-reference', required=True, help=u"""Unique internal identifier to refer to upload warning""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_upload_warning(ctx, from_json, namespace_name, upload_reference, warning_reference):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(upload_reference, six.string_types) and len(upload_reference.strip()) == 0:
        raise click.UsageError('Parameter --upload-reference cannot be whitespace or empty string')

    if isinstance(warning_reference, six.string_types) and len(warning_reference.strip()) == 0:
        raise click.UsageError('Parameter --warning-reference cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.delete_upload_warning(
        namespace_name=namespace_name,
        upload_reference=upload_reference,
        warning_reference=warning_reference,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@storage_group.command(name=cli_util.override('log_analytics.disable_archiving.command_name', 'disable-archiving'), help=u"""This API disables archiving. \n[Command Reference](disableArchiving)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'Success'})
@cli_util.wrap_exceptions
def disable_archiving(ctx, from_json, namespace_name, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.disable_archiving(
        namespace_name=namespace_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@storage_group.command(name=cli_util.override('log_analytics.enable_archiving.command_name', 'enable-archiving'), help=u"""THis API enables archiving. \n[Command Reference](enableArchiving)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'Success'})
@cli_util.wrap_exceptions
def enable_archiving(ctx, from_json, namespace_name, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.enable_archiving(
        namespace_name=namespace_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@storage_group.command(name=cli_util.override('log_analytics.estimate_purge_data_size.command_name', 'estimate-purge-data-size'), help=u"""This API estimates the size of data to be purged based based on time interval, purge query etc. \n[Command Reference](estimatePurgeDataSize)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""This is the compartment OCID under which the data will be purged""")
@cli_util.option('--time-data-ended', required=True, type=custom_types.CLI_DATETIME, help=u"""This is the time before which data will be purged""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""If true, purge child compartments data""")
@cli_util.option('--purge-query-string', help=u"""This is the solr data filter query, '*' means all""")
@cli_util.option('--data-type', type=custom_types.CliCaseInsensitiveChoice(["LOG", "LOOKUP"]), help=u"""This is the type of the log data to be purged""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'EstimatePurgeDataSizeResult'})
@cli_util.wrap_exceptions
def estimate_purge_data_size(ctx, from_json, namespace_name, compartment_id, time_data_ended, compartment_id_in_subtree, purge_query_string, data_type, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['timeDataEnded'] = time_data_ended

    if compartment_id_in_subtree is not None:
        _details['compartmentIdInSubtree'] = compartment_id_in_subtree

    if purge_query_string is not None:
        _details['purgeQueryString'] = purge_query_string

    if data_type is not None:
        _details['dataType'] = data_type

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.estimate_purge_data_size(
        namespace_name=namespace_name,
        estimate_purge_data_size_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@binary_group.command(name=cli_util.override('log_analytics.export_custom_content.command_name', 'export-custom-content'), help=u"""export \n[Command Reference](exportCustomContent)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--field-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""fieldNames""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parser-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""parserNames""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--source-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""sourceNames""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'field-names': {'module': 'log_analytics', 'class': 'list[string]'}, 'parser-names': {'module': 'log_analytics', 'class': 'list[string]'}, 'source-names': {'module': 'log_analytics', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'field-names': {'module': 'log_analytics', 'class': 'list[string]'}, 'parser-names': {'module': 'log_analytics', 'class': 'list[string]'}, 'source-names': {'module': 'log_analytics', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def export_custom_content(ctx, from_json, file, namespace_name, field_names, parser_names, source_names):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if field_names is not None:
        _details['fieldNames'] = cli_util.parse_json_parameter("field_names", field_names)

    if parser_names is not None:
        _details['parserNames'] = cli_util.parse_json_parameter("parser_names", parser_names)

    if source_names is not None:
        _details['sourceNames'] = cli_util.parse_json_parameter("source_names", source_names)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.export_custom_content(
        namespace_name=namespace_name,
        export_custom_content_details=_details,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@query_details_group.command(name=cli_util.override('log_analytics.export_query_result.command_name', 'export-query-result'), help=u"""Export data based on query. Endpoint returns a stream of data. Endpoint is synchronous. Queries must deliver first result within 60 seconds or calls are subject to timeout. \n[Command Reference](exportQueryResult)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID] .""")
@cli_util.option('--query-string', required=True, help=u"""Query to perform.""")
@cli_util.option('--sub-system', required=True, type=custom_types.CliCaseInsensitiveChoice(["LOG"]), help=u"""Default subsystem to qualify fields with in the queryString if not specified.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Flag to search all child compartments of the compartment Id specified in the compartmentId query parameter.""")
@cli_util.option('--scope-filters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of filters to be applied when the query executes. More than one filter per field is not permitted.

This option is a JSON list with items of type ScopeFilter.  For documentation on ScopeFilter please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/ScopeFilter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--max-total-count', type=click.INT, help=u"""Maximum number of results retrieved from data source.  Note a maximum value will be enforced; if the export results can be streamed, the maximum will be 50000000, otherwise 10000; that is, if not streamed, actualMaxTotalCountUsed = Math.min(maxTotalCount, 10000).

 Export will incrementally stream results depending on the queryString.

Some commands including head/tail are not compatible with streaming result delivery and therefore enforce a reduced limit on overall maxtotalcount.  no sort command or sort by id, e.g. ' | sort id ' - is streaming compatible  sort by time and id, e.g. ' | sort -time, id ' - is streaming compatible all other cases, e.g. ' | sort -time, id, mtgtguid ' - is not streaming compatible due to the additional sort field""")
@cli_util.option('--time-filter', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--query-timeout-in-seconds', type=click.INT, help=u"""Amount of time, in seconds, allowed for a query to execute. If this time expires before the query is complete, any partial results will be returned.""")
@cli_util.option('--should-include-columns', type=click.BOOL, help=u"""Include columns in response""")
@cli_util.option('--output-format', type=custom_types.CliCaseInsensitiveChoice(["CSV", "JSON"]), help=u"""Specifies the format for the returned results.""")
@cli_util.option('--should-localize', type=click.BOOL, help=u"""Localize results, including header columns, List-Of-Values and timestamp values.""")
@cli_util.option('--should-use-acceleration', type=click.BOOL, help=u"""Controls if query should ignore pre-calculated results if available and only use raw data.""")
@json_skeleton_utils.get_cli_json_input_option({'scope-filters': {'module': 'log_analytics', 'class': 'list[ScopeFilter]'}, 'time-filter': {'module': 'log_analytics', 'class': 'TimeRange'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'scope-filters': {'module': 'log_analytics', 'class': 'list[ScopeFilter]'}, 'time-filter': {'module': 'log_analytics', 'class': 'TimeRange'}})
@cli_util.wrap_exceptions
def export_query_result(ctx, from_json, file, namespace_name, compartment_id, query_string, sub_system, compartment_id_in_subtree, scope_filters, max_total_count, time_filter, query_timeout_in_seconds, should_include_columns, output_format, should_localize, should_use_acceleration):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['queryString'] = query_string
    _details['subSystem'] = sub_system

    if compartment_id_in_subtree is not None:
        _details['compartmentIdInSubtree'] = compartment_id_in_subtree

    if scope_filters is not None:
        _details['scopeFilters'] = cli_util.parse_json_parameter("scope_filters", scope_filters)

    if max_total_count is not None:
        _details['maxTotalCount'] = max_total_count

    if time_filter is not None:
        _details['timeFilter'] = cli_util.parse_json_parameter("time_filter", time_filter)

    if query_timeout_in_seconds is not None:
        _details['queryTimeoutInSeconds'] = query_timeout_in_seconds

    if should_include_columns is not None:
        _details['shouldIncludeColumns'] = should_include_columns

    if output_format is not None:
        _details['outputFormat'] = output_format

    if should_localize is not None:
        _details['shouldLocalize'] = should_localize

    if should_use_acceleration is not None:
        _details['shouldUseAcceleration'] = should_use_acceleration

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.export_query_result(
        namespace_name=namespace_name,
        export_details=_details,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@log_analytics_parser_group.command(name=cli_util.override('log_analytics.extract_structured_log_field_paths.command_name', 'extract-structured-log-field-paths'), help=u"""structured log fieldpaths \n[Command Reference](extractStructuredLogFieldPaths)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--content', help=u"""content""")
@cli_util.option('--description', help=u"""description""")
@cli_util.option('--display-name', help=u"""display name""")
@cli_util.option('--edit-version', type=click.INT, help=u"""edit version""")
@cli_util.option('--encoding', help=u"""encoding""")
@cli_util.option('--example-content', help=u"""example content""")
@cli_util.option('--field-maps', type=custom_types.CLI_COMPLEX_TYPE, help=u"""fields Maps

This option is a JSON list with items of type LogAnalyticsParserField.  For documentation on LogAnalyticsParserField please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParserField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--footer-content', help=u"""footer regular expression""")
@cli_util.option('--header-content', help=u"""header content""")
@cli_util.option('--name', help=u"""Name""")
@cli_util.option('--is-default', type=click.BOOL, help=u"""is default flag""")
@cli_util.option('--is-single-line-content', type=click.BOOL, help=u"""is single line content""")
@cli_util.option('--is-system', type=click.BOOL, help=u"""is system flag""")
@cli_util.option('--language', help=u"""language""")
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""last updated date""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--log-type-test-request-version', type=click.INT, help=u"""log type test request version""")
@cli_util.option('--mapped-parsers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""mapped parser list

This option is a JSON list with items of type LogAnalyticsParser.  For documentation on LogAnalyticsParser please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParser.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parser-ignoreline-characters', help=u"""parser ignore line characters""")
@cli_util.option('--is-hidden', type=click.BOOL, help=u"""is hidden flag""")
@cli_util.option('--parser-sequence', type=click.INT, help=u"""sequence""")
@cli_util.option('--parser-timezone', help=u"""time zone""")
@cli_util.option('--parser-filter', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-parser-written-once', type=click.BOOL, help=u"""write once""")
@cli_util.option('--parser-functions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""plugin instance list

This option is a JSON list with items of type LogAnalyticsParserFunction.  For documentation on LogAnalyticsParserFunction please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParserFunction.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--sources-count', type=click.INT, help=u"""sources using this parser""")
@cli_util.option('--sources', type=custom_types.CLI_COMPLEX_TYPE, help=u"""sources using list

This option is a JSON list with items of type LogAnalyticsSource.  For documentation on LogAnalyticsSource please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSource.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--should-tokenize-original-text', type=click.BOOL, help=u"""tokenize original text""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["XML", "JSON", "REGEX", "ODL"]), help=u"""type""")
@cli_util.option('--is-user-deleted', type=click.BOOL, help=u"""user deleted flag""")
@cli_util.option('--parser-type', type=custom_types.CliCaseInsensitiveChoice(["XML", "JSON"]), help=u"""type - possible values are xml or json""")
@json_skeleton_utils.get_cli_json_input_option({'field-maps': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserField]'}, 'mapped-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'parser-filter': {'module': 'log_analytics', 'class': 'LogAnalyticsParserFilter'}, 'parser-functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserFunction]'}, 'sources': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSource]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'field-maps': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserField]'}, 'mapped-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'parser-filter': {'module': 'log_analytics', 'class': 'LogAnalyticsParserFilter'}, 'parser-functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserFunction]'}, 'sources': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSource]'}}, output_type={'module': 'log_analytics', 'class': 'ExtractLogFieldResults'})
@cli_util.wrap_exceptions
def extract_structured_log_field_paths(ctx, from_json, namespace_name, content, description, display_name, edit_version, encoding, example_content, field_maps, footer_content, header_content, name, is_default, is_single_line_content, is_system, language, time_updated, log_type_test_request_version, mapped_parsers, parser_ignoreline_characters, is_hidden, parser_sequence, parser_timezone, parser_filter, is_parser_written_once, parser_functions, sources_count, sources, should_tokenize_original_text, type, is_user_deleted, parser_type):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if parser_type is not None:
        kwargs['parser_type'] = parser_type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if content is not None:
        _details['content'] = content

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if edit_version is not None:
        _details['editVersion'] = edit_version

    if encoding is not None:
        _details['encoding'] = encoding

    if example_content is not None:
        _details['exampleContent'] = example_content

    if field_maps is not None:
        _details['fieldMaps'] = cli_util.parse_json_parameter("field_maps", field_maps)

    if footer_content is not None:
        _details['footerContent'] = footer_content

    if header_content is not None:
        _details['headerContent'] = header_content

    if name is not None:
        _details['name'] = name

    if is_default is not None:
        _details['isDefault'] = is_default

    if is_single_line_content is not None:
        _details['isSingleLineContent'] = is_single_line_content

    if is_system is not None:
        _details['isSystem'] = is_system

    if language is not None:
        _details['language'] = language

    if time_updated is not None:
        _details['timeUpdated'] = time_updated

    if log_type_test_request_version is not None:
        _details['logTypeTestRequestVersion'] = log_type_test_request_version

    if mapped_parsers is not None:
        _details['mappedParsers'] = cli_util.parse_json_parameter("mapped_parsers", mapped_parsers)

    if parser_ignoreline_characters is not None:
        _details['parserIgnorelineCharacters'] = parser_ignoreline_characters

    if is_hidden is not None:
        _details['isHidden'] = is_hidden

    if parser_sequence is not None:
        _details['parserSequence'] = parser_sequence

    if parser_timezone is not None:
        _details['parserTimezone'] = parser_timezone

    if parser_filter is not None:
        _details['parserFilter'] = cli_util.parse_json_parameter("parser_filter", parser_filter)

    if is_parser_written_once is not None:
        _details['isParserWrittenOnce'] = is_parser_written_once

    if parser_functions is not None:
        _details['parserFunctions'] = cli_util.parse_json_parameter("parser_functions", parser_functions)

    if sources_count is not None:
        _details['sourcesCount'] = sources_count

    if sources is not None:
        _details['sources'] = cli_util.parse_json_parameter("sources", sources)

    if should_tokenize_original_text is not None:
        _details['shouldTokenizeOriginalText'] = should_tokenize_original_text

    if type is not None:
        _details['type'] = type

    if is_user_deleted is not None:
        _details['isUserDeleted'] = is_user_deleted

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.extract_structured_log_field_paths(
        namespace_name=namespace_name,
        logan_parser_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_parser_group.command(name=cli_util.override('log_analytics.extract_structured_log_header_paths.command_name', 'extract-structured-log-header-paths'), help=u"""structured log header paths \n[Command Reference](extractStructuredLogHeaderPaths)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--content', help=u"""content""")
@cli_util.option('--description', help=u"""description""")
@cli_util.option('--display-name', help=u"""display name""")
@cli_util.option('--edit-version', type=click.INT, help=u"""edit version""")
@cli_util.option('--encoding', help=u"""encoding""")
@cli_util.option('--example-content', help=u"""example content""")
@cli_util.option('--field-maps', type=custom_types.CLI_COMPLEX_TYPE, help=u"""fields Maps

This option is a JSON list with items of type LogAnalyticsParserField.  For documentation on LogAnalyticsParserField please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParserField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--footer-content', help=u"""footer regular expression""")
@cli_util.option('--header-content', help=u"""header content""")
@cli_util.option('--name', help=u"""Name""")
@cli_util.option('--is-default', type=click.BOOL, help=u"""is default flag""")
@cli_util.option('--is-single-line-content', type=click.BOOL, help=u"""is single line content""")
@cli_util.option('--is-system', type=click.BOOL, help=u"""is system flag""")
@cli_util.option('--language', help=u"""language""")
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""last updated date""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--log-type-test-request-version', type=click.INT, help=u"""log type test request version""")
@cli_util.option('--mapped-parsers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""mapped parser list

This option is a JSON list with items of type LogAnalyticsParser.  For documentation on LogAnalyticsParser please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParser.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parser-ignoreline-characters', help=u"""parser ignore line characters""")
@cli_util.option('--is-hidden', type=click.BOOL, help=u"""is hidden flag""")
@cli_util.option('--parser-sequence', type=click.INT, help=u"""sequence""")
@cli_util.option('--parser-timezone', help=u"""time zone""")
@cli_util.option('--parser-filter', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-parser-written-once', type=click.BOOL, help=u"""write once""")
@cli_util.option('--parser-functions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""plugin instance list

This option is a JSON list with items of type LogAnalyticsParserFunction.  For documentation on LogAnalyticsParserFunction please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParserFunction.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--sources-count', type=click.INT, help=u"""sources using this parser""")
@cli_util.option('--sources', type=custom_types.CLI_COMPLEX_TYPE, help=u"""sources using list

This option is a JSON list with items of type LogAnalyticsSource.  For documentation on LogAnalyticsSource please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSource.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--should-tokenize-original-text', type=click.BOOL, help=u"""tokenize original text""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["XML", "JSON", "REGEX", "ODL"]), help=u"""type""")
@cli_util.option('--is-user-deleted', type=click.BOOL, help=u"""user deleted flag""")
@cli_util.option('--parser-type', type=custom_types.CliCaseInsensitiveChoice(["XML", "JSON"]), help=u"""type - possible values are xml or json""")
@json_skeleton_utils.get_cli_json_input_option({'field-maps': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserField]'}, 'mapped-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'parser-filter': {'module': 'log_analytics', 'class': 'LogAnalyticsParserFilter'}, 'parser-functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserFunction]'}, 'sources': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSource]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'field-maps': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserField]'}, 'mapped-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'parser-filter': {'module': 'log_analytics', 'class': 'LogAnalyticsParserFilter'}, 'parser-functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserFunction]'}, 'sources': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSource]'}}, output_type={'module': 'log_analytics', 'class': 'ExtractLogHeaderResults'})
@cli_util.wrap_exceptions
def extract_structured_log_header_paths(ctx, from_json, namespace_name, content, description, display_name, edit_version, encoding, example_content, field_maps, footer_content, header_content, name, is_default, is_single_line_content, is_system, language, time_updated, log_type_test_request_version, mapped_parsers, parser_ignoreline_characters, is_hidden, parser_sequence, parser_timezone, parser_filter, is_parser_written_once, parser_functions, sources_count, sources, should_tokenize_original_text, type, is_user_deleted, parser_type):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if parser_type is not None:
        kwargs['parser_type'] = parser_type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if content is not None:
        _details['content'] = content

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if edit_version is not None:
        _details['editVersion'] = edit_version

    if encoding is not None:
        _details['encoding'] = encoding

    if example_content is not None:
        _details['exampleContent'] = example_content

    if field_maps is not None:
        _details['fieldMaps'] = cli_util.parse_json_parameter("field_maps", field_maps)

    if footer_content is not None:
        _details['footerContent'] = footer_content

    if header_content is not None:
        _details['headerContent'] = header_content

    if name is not None:
        _details['name'] = name

    if is_default is not None:
        _details['isDefault'] = is_default

    if is_single_line_content is not None:
        _details['isSingleLineContent'] = is_single_line_content

    if is_system is not None:
        _details['isSystem'] = is_system

    if language is not None:
        _details['language'] = language

    if time_updated is not None:
        _details['timeUpdated'] = time_updated

    if log_type_test_request_version is not None:
        _details['logTypeTestRequestVersion'] = log_type_test_request_version

    if mapped_parsers is not None:
        _details['mappedParsers'] = cli_util.parse_json_parameter("mapped_parsers", mapped_parsers)

    if parser_ignoreline_characters is not None:
        _details['parserIgnorelineCharacters'] = parser_ignoreline_characters

    if is_hidden is not None:
        _details['isHidden'] = is_hidden

    if parser_sequence is not None:
        _details['parserSequence'] = parser_sequence

    if parser_timezone is not None:
        _details['parserTimezone'] = parser_timezone

    if parser_filter is not None:
        _details['parserFilter'] = cli_util.parse_json_parameter("parser_filter", parser_filter)

    if is_parser_written_once is not None:
        _details['isParserWrittenOnce'] = is_parser_written_once

    if parser_functions is not None:
        _details['parserFunctions'] = cli_util.parse_json_parameter("parser_functions", parser_functions)

    if sources_count is not None:
        _details['sourcesCount'] = sources_count

    if sources is not None:
        _details['sources'] = cli_util.parse_json_parameter("sources", sources)

    if should_tokenize_original_text is not None:
        _details['shouldTokenizeOriginalText'] = should_tokenize_original_text

    if type is not None:
        _details['type'] = type

    if is_user_deleted is not None:
        _details['isUserDeleted'] = is_user_deleted

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.extract_structured_log_header_paths(
        namespace_name=namespace_name,
        logan_parser_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@query_details_group.command(name=cli_util.override('log_analytics.filter.command_name', 'filter'), help=u"""Each filter specifies an operator, a field and one or more values to be inserted into the provided query as criteria. \n[Command Reference](filter)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--query-string', required=True, help=u"""Query to apply edits to.""")
@cli_util.option('--sub-system', required=True, type=custom_types.CliCaseInsensitiveChoice(["LOG"]), help=u"""Default subsystem to qualify fields with in the queryString if not specified.""")
@cli_util.option('--filters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of edit operations to be applied in the specified order to the specified queryString.

This option is a JSON list with items of type Filter.  For documentation on Filter please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/Filter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'filters': {'module': 'log_analytics', 'class': 'list[Filter]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'filters': {'module': 'log_analytics', 'class': 'list[Filter]'}}, output_type={'module': 'log_analytics', 'class': 'FilterOutput'})
@cli_util.wrap_exceptions
def filter(ctx, from_json, namespace_name, query_string, sub_system, filters):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['queryString'] = query_string
    _details['subSystem'] = sub_system

    if filters is not None:
        _details['filters'] = cli_util.parse_json_parameter("filters", filters)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.filter(
        namespace_name=namespace_name,
        filter_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_association_group.command(name=cli_util.override('log_analytics.get_association_summary.command_name', 'get-association-summary'), help=u"""association summary \n[Command Reference](getAssociationSummary)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'AssociationSummaryReport'})
@cli_util.wrap_exceptions
def get_association_summary(ctx, from_json, namespace_name, compartment_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_association_summary(
        namespace_name=namespace_name,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_source_group.command(name=cli_util.override('log_analytics.get_column_names.command_name', 'get-column-names'), help=u"""extract column names from SQL query \n[Command Reference](getColumnNames)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--sql-query', required=True, help=u"""sql query to get the columns""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'ColumnNameCollection'})
@cli_util.wrap_exceptions
def get_column_names(ctx, from_json, namespace_name, sql_query):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_column_names(
        namespace_name=namespace_name,
        sql_query=sql_query,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_config_work_request_group.command(name=cli_util.override('log_analytics.get_config_work_request.command_name', 'get-config-work-request'), help=u"""association summary by source \n[Command Reference](getConfigWorkRequest)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--work-request-id', required=True, help=u"""Work Request Identifier [OCID]  for the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsConfigWorkRequest'})
@cli_util.wrap_exceptions
def get_config_work_request(ctx, from_json, namespace_name, work_request_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_config_work_request(
        namespace_name=namespace_name,
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_field_group.command(name=cli_util.override('log_analytics.get_field.command_name', 'get-field'), help=u"""get common field with specified name \n[Command Reference](getField)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--field-name', required=True, help=u"""name of the field to get""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsField'})
@cli_util.wrap_exceptions
def get_field(ctx, from_json, namespace_name, field_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(field_name, six.string_types) and len(field_name.strip()) == 0:
        raise click.UsageError('Parameter --field-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_field(
        namespace_name=namespace_name,
        field_name=field_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_field_group.command(name=cli_util.override('log_analytics.get_fields_summary.command_name', 'get-fields-summary'), help=u"""get field summary \n[Command Reference](getFieldsSummary)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--is-show-detail', type=click.BOOL, help=u"""show detail flag""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'FieldSummaryReport'})
@cli_util.wrap_exceptions
def get_fields_summary(ctx, from_json, namespace_name, is_show_detail):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if is_show_detail is not None:
        kwargs['is_show_detail'] = is_show_detail
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_fields_summary(
        namespace_name=namespace_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_label_group.command(name=cli_util.override('log_analytics.get_label.command_name', 'get-label'), help=u"""get label with specified name \n[Command Reference](getLabel)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--label-name', required=True, help=u"""name of the label to get""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsLabel'})
@cli_util.wrap_exceptions
def get_label(ctx, from_json, namespace_name, label_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(label_name, six.string_types) and len(label_name.strip()) == 0:
        raise click.UsageError('Parameter --label-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_label(
        namespace_name=namespace_name,
        label_name=label_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_label_group.command(name=cli_util.override('log_analytics.get_label_summary.command_name', 'get-label-summary'), help=u"""get total count \n[Command Reference](getLabelSummary)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LabelSummaryReport'})
@cli_util.wrap_exceptions
def get_label_summary(ctx, from_json, namespace_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_label_summary(
        namespace_name=namespace_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_entity_group.command(name=cli_util.override('log_analytics.get_log_analytics_entities_summary.command_name', 'get-log-analytics-entities-summary'), help=u"""Returns log analytics entities count summary. \n[Command Reference](getLogAnalyticsEntitiesSummary)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsEntitySummaryReport'})
@cli_util.wrap_exceptions
def get_log_analytics_entities_summary(ctx, from_json, namespace_name, compartment_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_log_analytics_entities_summary(
        namespace_name=namespace_name,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_entity_group.command(name=cli_util.override('log_analytics.get_log_analytics_entity.command_name', 'get'), help=u"""Retrieve the log analytics entity with the given id. \n[Command Reference](getLogAnalyticsEntity)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--log-analytics-entity-id', required=True, help=u"""The log analytics entity OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsEntity'})
@cli_util.wrap_exceptions
def get_log_analytics_entity(ctx, from_json, namespace_name, log_analytics_entity_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(log_analytics_entity_id, six.string_types) and len(log_analytics_entity_id.strip()) == 0:
        raise click.UsageError('Parameter --log-analytics-entity-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_log_analytics_entity(
        namespace_name=namespace_name,
        log_analytics_entity_id=log_analytics_entity_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_entity_type_group.command(name=cli_util.override('log_analytics.get_log_analytics_entity_type.command_name', 'get'), help=u"""Retrieve the log analytics entity type with the given name. \n[Command Reference](getLogAnalyticsEntityType)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--entity-type-name', required=True, help=u"""Log analytics entity type name.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsEntityType'})
@cli_util.wrap_exceptions
def get_log_analytics_entity_type(ctx, from_json, namespace_name, entity_type_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(entity_type_name, six.string_types) and len(entity_type_name.strip()) == 0:
        raise click.UsageError('Parameter --entity-type-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_log_analytics_entity_type(
        namespace_name=namespace_name,
        entity_type_name=entity_type_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_log_group_group.command(name=cli_util.override('log_analytics.get_log_analytics_log_group.command_name', 'get'), help=u"""Retrieves the Log-Analytics group with the given id. \n[Command Reference](getLogAnalyticsLogGroup)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--log-analytics-log-group-id', required=True, help=u"""unique logAnalytics log group identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsLogGroup'})
@cli_util.wrap_exceptions
def get_log_analytics_log_group(ctx, from_json, namespace_name, log_analytics_log_group_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(log_analytics_log_group_id, six.string_types) and len(log_analytics_log_group_id.strip()) == 0:
        raise click.UsageError('Parameter --log-analytics-log-group-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_log_analytics_log_group(
        namespace_name=namespace_name,
        log_analytics_log_group_id=log_analytics_log_group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_log_group_group.command(name=cli_util.override('log_analytics.get_log_analytics_log_groups_summary.command_name', 'get-log-analytics-log-groups-summary'), help=u"""Returns a count of Log-Analytics groups. \n[Command Reference](getLogAnalyticsLogGroupsSummary)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogGroupSummaryReport'})
@cli_util.wrap_exceptions
def get_log_analytics_log_groups_summary(ctx, from_json, namespace_name, compartment_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_log_analytics_log_groups_summary(
        namespace_name=namespace_name,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_object_collection_rule_group.command(name=cli_util.override('log_analytics.get_log_analytics_object_collection_rule.command_name', 'get'), help=u"""Gets a configured object storage based collection rule by given id \n[Command Reference](getLogAnalyticsObjectCollectionRule)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--log-analytics-object-collection-rule-id', required=True, help=u"""The Logging Analytics Object Collection Rule [OCID]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsObjectCollectionRule'})
@cli_util.wrap_exceptions
def get_log_analytics_object_collection_rule(ctx, from_json, namespace_name, log_analytics_object_collection_rule_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(log_analytics_object_collection_rule_id, six.string_types) and len(log_analytics_object_collection_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --log-analytics-object-collection-rule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_log_analytics_object_collection_rule(
        namespace_name=namespace_name,
        log_analytics_object_collection_rule_id=log_analytics_object_collection_rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@namespace_group.command(name=cli_util.override('log_analytics.get_namespace.command_name', 'get'), help=u"""This API gets the namespace details of a tenancy already onboarded in Logging Analytics Application \n[Command Reference](getNamespace)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'Namespace'})
@cli_util.wrap_exceptions
def get_namespace(ctx, from_json, namespace_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_namespace(
        namespace_name=namespace_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_parser_group.command(name=cli_util.override('log_analytics.get_parser.command_name', 'get-parser'), help=u"""get parser with fields by Name \n[Command Reference](getParser)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--parser-name', required=True, help=u"""parserName""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsParser'})
@cli_util.wrap_exceptions
def get_parser(ctx, from_json, namespace_name, parser_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(parser_name, six.string_types) and len(parser_name.strip()) == 0:
        raise click.UsageError('Parameter --parser-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_parser(
        namespace_name=namespace_name,
        parser_name=parser_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_parser_group.command(name=cli_util.override('log_analytics.get_parser_summary.command_name', 'get-parser-summary'), help=u"""parser summary \n[Command Reference](getParserSummary)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'ParserSummaryReport'})
@cli_util.wrap_exceptions
def get_parser_summary(ctx, from_json, namespace_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_parser_summary(
        namespace_name=namespace_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@query_details_group.command(name=cli_util.override('log_analytics.get_query_result.command_name', 'get-query-result'), help=u"""Returns the intermediate results for a query that was specified to run asynchronously if the query has not completed, otherwise the final query results identified by a queryWorkRequestId returned when submitting the query execute asynchronously. \n[Command Reference](getQueryResult)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--work-request-id', required=True, help=u"""Work Request Identifier [OCID]  for the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""Maximum number of results to return in this request.  Note a limit=-1 returns all results from pageId onwards up to maxtotalCount.""")
@cli_util.option('--should-include-columns', type=click.BOOL, help=u"""Include columns in response""")
@cli_util.option('--should-include-fields', type=click.BOOL, help=u"""Include fields in response""")
@cli_util.option('--output-mode', type=custom_types.CliCaseInsensitiveChoice(["JSON_ROWS"]), help=u"""Specifies the format for the returned results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'QueryAggregation'})
@cli_util.wrap_exceptions
def get_query_result(ctx, from_json, namespace_name, work_request_id, page, limit, should_include_columns, should_include_fields, output_mode):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if should_include_columns is not None:
        kwargs['should_include_columns'] = should_include_columns
    if should_include_fields is not None:
        kwargs['should_include_fields'] = should_include_fields
    if output_mode is not None:
        kwargs['output_mode'] = output_mode
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_query_result(
        namespace_name=namespace_name,
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@query_work_request_group.command(name=cli_util.override('log_analytics.get_query_work_request.command_name', 'get'), help=u"""Retrieve work request details by workRequestId. This endpoint can be polled for status tracking of work request. Clients should poll using the interval returned in the retry-after header. \n[Command Reference](getQueryWorkRequest)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--work-request-id', required=True, help=u"""Work Request Identifier [OCID]  for the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'QueryWorkRequest'})
@cli_util.wrap_exceptions
def get_query_work_request(ctx, from_json, namespace_name, work_request_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_query_work_request(
        namespace_name=namespace_name,
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@scheduled_task_group.command(name=cli_util.override('log_analytics.get_scheduled_task.command_name', 'get'), help=u"""Get the scheduled task for the specified task identifier. \n[Command Reference](getScheduledTask)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--scheduled-task-id', required=True, help=u"""Unique scheduledTask id returned from task create. If invalid will lead to a 404 not found.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'ScheduledTask'})
@cli_util.wrap_exceptions
def get_scheduled_task(ctx, from_json, namespace_name, scheduled_task_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(scheduled_task_id, six.string_types) and len(scheduled_task_id.strip()) == 0:
        raise click.UsageError('Parameter --scheduled-task-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_scheduled_task(
        namespace_name=namespace_name,
        scheduled_task_id=scheduled_task_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_source_group.command(name=cli_util.override('log_analytics.get_source.command_name', 'get-source'), help=u"""get source with specified name \n[Command Reference](getSource)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--source-name', required=True, help=u"""source name""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsSource'})
@cli_util.wrap_exceptions
def get_source(ctx, from_json, namespace_name, source_name, compartment_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(source_name, six.string_types) and len(source_name.strip()) == 0:
        raise click.UsageError('Parameter --source-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_source(
        namespace_name=namespace_name,
        source_name=source_name,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_source_group.command(name=cli_util.override('log_analytics.get_source_summary.command_name', 'get-source-summary'), help=u"""source summary \n[Command Reference](getSourceSummary)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'SourceSummaryReport'})
@cli_util.wrap_exceptions
def get_source_summary(ctx, from_json, namespace_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_source_summary(
        namespace_name=namespace_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@storage_group.command(name=cli_util.override('log_analytics.get_storage.command_name', 'get'), help=u"""This API gets the storage configuration of a tenancy \n[Command Reference](getStorage)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'Storage'})
@cli_util.wrap_exceptions
def get_storage(ctx, from_json, namespace_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_storage(
        namespace_name=namespace_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@storage_group.command(name=cli_util.override('log_analytics.get_storage_usage.command_name', 'get-storage-usage'), help=u"""This API gets storage usage information of a tenancy.  Storage usage information includes active, archived or recalled data.  The unit of return data is in bytes. \n[Command Reference](getStorageUsage)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'StorageUsage'})
@cli_util.wrap_exceptions
def get_storage_usage(ctx, from_json, namespace_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_storage_usage(
        namespace_name=namespace_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@storage_group.command(name=cli_util.override('log_analytics.get_storage_work_request.command_name', 'get-storage-work-request'), help=u"""This API returns work request details specified by {workRequestId}. This API can be polled for status tracking of work request.  Clients should poll using the interval returned in retry-after header. \n[Command Reference](getStorageWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""Work Request Identifier [OCID]  for the asynchronous request.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'StorageWorkRequest'})
@cli_util.wrap_exceptions
def get_storage_work_request(ctx, from_json, work_request_id, namespace_name):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_storage_work_request(
        work_request_id=work_request_id,
        namespace_name=namespace_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@upload_group.command(name=cli_util.override('log_analytics.get_upload.command_name', 'get'), help=u"""Gets an On-Demand Upload info by reference \n[Command Reference](getUpload)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--upload-reference', required=True, help=u"""Unique internal identifier to refer to upload container""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'Upload'})
@cli_util.wrap_exceptions
def get_upload(ctx, from_json, namespace_name, upload_reference):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(upload_reference, six.string_types) and len(upload_reference.strip()) == 0:
        raise click.UsageError('Parameter --upload-reference cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_upload(
        namespace_name=namespace_name,
        upload_reference=upload_reference,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('log_analytics.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--work-request-id', required=True, help=u"""Work Request Identifier [OCID]  for the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, namespace_name, work_request_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.get_work_request(
        namespace_name=namespace_name,
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_import_custom_content_group.command(name=cli_util.override('log_analytics.import_custom_content.command_name', 'import-custom-content'), help=u"""register custom content \n[Command Reference](importCustomContent)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--import-custom-content-file-body', required=True, help=u"""The file to upload which contains the custom content.""")
@cli_util.option('--is-overwrite', type=click.BOOL, help=u"""is overwrite""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsImportCustomContent'})
@cli_util.wrap_exceptions
def import_custom_content(ctx, from_json, namespace_name, import_custom_content_file_body, is_overwrite):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if is_overwrite is not None:
        kwargs['is_overwrite'] = is_overwrite
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    # do not automatically retry operations with binary inputs
    kwargs['retry_strategy'] = oci.retry.NoneRetryStrategy()

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.import_custom_content(
        namespace_name=namespace_name,
        import_custom_content_file_body=import_custom_content_file_body,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_association_group.command(name=cli_util.override('log_analytics.list_associated_entities.command_name', 'list-associated-entities'), help=u"""list of entities that have been associated to at least one source \n[Command Reference](listAssociatedEntities)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--entity-id', help=u"""The entity OCID.""")
@cli_util.option('--entity-type', help=u"""entity type name""")
@cli_util.option('--entity-type-display-name', help=u"""entity type display name""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["entityName", "entityTypeDisplayName", "associationCount"]), help=u"""sort by field""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsAssociatedEntityCollection'})
@cli_util.wrap_exceptions
def list_associated_entities(ctx, from_json, all_pages, page_size, namespace_name, compartment_id, entity_id, entity_type, entity_type_display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if entity_id is not None:
        kwargs['entity_id'] = entity_id
    if entity_type is not None:
        kwargs['entity_type'] = entity_type
    if entity_type_display_name is not None:
        kwargs['entity_type_display_name'] = entity_type_display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_associated_entities,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_associated_entities,
            limit,
            page_size,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_associated_entities(
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_config_work_request_group.command(name=cli_util.override('log_analytics.list_config_work_requests.command_name', 'list-config-work-requests'), help=u"""association summary by source \n[Command Reference](listConfigWorkRequests)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""work requests sort by""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsConfigWorkRequestCollection'})
@cli_util.wrap_exceptions
def list_config_work_requests(ctx, from_json, all_pages, page_size, namespace_name, compartment_id, sort_order, sort_by, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_config_work_requests,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_config_work_requests,
            limit,
            page_size,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_config_work_requests(
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_entity_group.command(name=cli_util.override('log_analytics.list_entity_associations.command_name', 'list-entity-associations'), help=u"""Return a list of log analytics entities associated with input source log analytics entity. \n[Command Reference](listEntityAssociations)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--log-analytics-entity-id', required=True, help=u"""The log analytics entity OCID.""")
@cli_util.option('--direct-or-all-associations', type=custom_types.CliCaseInsensitiveChoice(["DIRECT", "ALL"]), help=u"""Indicates whether to return direct associated entities or direct and inferred associated entities.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "name"]), help=u"""The field to sort entities by. Only one sort order may be provided. Default order for timeCreated and timeUpdated is descending. Default order for entity name is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsEntityCollection'})
@cli_util.wrap_exceptions
def list_entity_associations(ctx, from_json, all_pages, page_size, namespace_name, log_analytics_entity_id, direct_or_all_associations, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(log_analytics_entity_id, six.string_types) and len(log_analytics_entity_id.strip()) == 0:
        raise click.UsageError('Parameter --log-analytics-entity-id cannot be whitespace or empty string')

    kwargs = {}
    if direct_or_all_associations is not None:
        kwargs['direct_or_all_associations'] = direct_or_all_associations
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_entity_associations,
            namespace_name=namespace_name,
            log_analytics_entity_id=log_analytics_entity_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_entity_associations,
            limit,
            page_size,
            namespace_name=namespace_name,
            log_analytics_entity_id=log_analytics_entity_id,
            **kwargs
        )
    else:
        result = client.list_entity_associations(
            namespace_name=namespace_name,
            log_analytics_entity_id=log_analytics_entity_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_association_group.command(name=cli_util.override('log_analytics.list_entity_source_associations.command_name', 'list-entity-source-associations'), help=u"""entity associations summary \n[Command Reference](listEntitySourceAssociations)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--entity-id', help=u"""The entity OCID.""")
@cli_util.option('--entity-type', help=u"""entity type name""")
@cli_util.option('--entity-type-display-name', help=u"""entity type display name""")
@cli_util.option('--life-cycle-state', type=custom_types.CliCaseInsensitiveChoice(["ALL", "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED"]), help=u"""Status""")
@cli_util.option('--is-show-total', type=click.BOOL, help=u"""is Show Total""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["sourceDisplayName", "timeLastAttempted", "status"]), help=u"""sort by field""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsAssociationCollection'})
@cli_util.wrap_exceptions
def list_entity_source_associations(ctx, from_json, all_pages, page_size, namespace_name, compartment_id, entity_id, entity_type, entity_type_display_name, life_cycle_state, is_show_total, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if entity_id is not None:
        kwargs['entity_id'] = entity_id
    if entity_type is not None:
        kwargs['entity_type'] = entity_type
    if entity_type_display_name is not None:
        kwargs['entity_type_display_name'] = entity_type_display_name
    if life_cycle_state is not None:
        kwargs['life_cycle_state'] = life_cycle_state
    if is_show_total is not None:
        kwargs['is_show_total'] = is_show_total
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_entity_source_associations,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_entity_source_associations,
            limit,
            page_size,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_entity_source_associations(
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_field_group.command(name=cli_util.override('log_analytics.list_fields.command_name', 'list-fields'), help=u"""get all common field with specified display name and description \n[Command Reference](listFields)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--is-match-all', type=click.BOOL, help=u"""isMatchAll""")
@cli_util.option('--source-ids', help=u"""comma delimited list of source ids""")
@cli_util.option('--source-names', help=u"""comma delimited list of source Names""")
@cli_util.option('--parser-type', type=custom_types.CliCaseInsensitiveChoice(["ALL", "REGEX", "XML", "JSON"]), help=u"""parserType""")
@cli_util.option('--parser-ids', help=u"""comma delimited list of parser ids""")
@cli_util.option('--parser-names', help=u"""comma delimited list of parser names""")
@cli_util.option('--is-include-parser', type=click.BOOL, help=u"""isIncludeParser""")
@cli_util.option('--filter', help=u"""filter""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "dataType"]), help=u"""sort by field""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsFieldCollection'})
@cli_util.wrap_exceptions
def list_fields(ctx, from_json, all_pages, page_size, namespace_name, is_match_all, source_ids, source_names, parser_type, parser_ids, parser_names, is_include_parser, filter, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if is_match_all is not None:
        kwargs['is_match_all'] = is_match_all
    if source_ids is not None:
        kwargs['source_ids'] = source_ids
    if source_names is not None:
        kwargs['source_names'] = source_names
    if parser_type is not None:
        kwargs['parser_type'] = parser_type
    if parser_ids is not None:
        kwargs['parser_ids'] = parser_ids
    if parser_names is not None:
        kwargs['parser_names'] = parser_names
    if is_include_parser is not None:
        kwargs['is_include_parser'] = is_include_parser
    if filter is not None:
        kwargs['filter'] = filter
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_fields,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_fields,
            limit,
            page_size,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_fields(
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_label_group.command(name=cli_util.override('log_analytics.list_label_priorities.command_name', 'list-label-priorities'), help=u"""get list of priorities \n[Command Reference](listLabelPriorities)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LabelPriorityCollection'})
@cli_util.wrap_exceptions
def list_label_priorities(ctx, from_json, all_pages, page_size, namespace_name, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_label_priorities,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_label_priorities,
            limit,
            page_size,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_label_priorities(
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_label_group.command(name=cli_util.override('log_analytics.list_label_source_details.command_name', 'list-label-source-details'), help=u"""get details of sources using the label \n[Command Reference](listLabelSourceDetails)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--label-name', help=u"""label name""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--label-source-sort-by', type=custom_types.CliCaseInsensitiveChoice(["sourceDisplayName", "labelFieldDisplayName"]), help=u"""sort by source displayname""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LabelSourceCollection'})
@cli_util.wrap_exceptions
def list_label_source_details(ctx, from_json, all_pages, page_size, namespace_name, label_name, limit, page, sort_order, label_source_sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if label_name is not None:
        kwargs['label_name'] = label_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if label_source_sort_by is not None:
        kwargs['label_source_sort_by'] = label_source_sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_label_source_details,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_label_source_details,
            limit,
            page_size,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_label_source_details(
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_label_group.command(name=cli_util.override('log_analytics.list_labels.command_name', 'list-labels'), help=u"""get labels passing specified filter \n[Command Reference](listLabels)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--label-name', help=u"""label name""")
@cli_util.option('--label-display-text', help=u"""search by label display name or description""")
@cli_util.option('--is-system', type=custom_types.CliCaseInsensitiveChoice(["ALL", "CUSTOM", "BUILT_IN"]), help=u"""Is system param of value (all, custom, sourceUsing)""")
@cli_util.option('--label-priority', type=custom_types.CliCaseInsensitiveChoice(["NONE", "LOW", "MEDIUM", "HIGH"]), help=u"""label priority""")
@cli_util.option('--is-count-pop', type=click.BOOL, help=u"""isCountPop""")
@cli_util.option('--is-alias-pop', type=click.BOOL, help=u"""isAliasPop""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--label-sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "priority", "sourceUsing"]), help=u"""sort by label""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsLabelCollection'})
@cli_util.wrap_exceptions
def list_labels(ctx, from_json, all_pages, page_size, namespace_name, label_name, label_display_text, is_system, label_priority, is_count_pop, is_alias_pop, limit, page, sort_order, label_sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if label_name is not None:
        kwargs['label_name'] = label_name
    if label_display_text is not None:
        kwargs['label_display_text'] = label_display_text
    if is_system is not None:
        kwargs['is_system'] = is_system
    if label_priority is not None:
        kwargs['label_priority'] = label_priority
    if is_count_pop is not None:
        kwargs['is_count_pop'] = is_count_pop
    if is_alias_pop is not None:
        kwargs['is_alias_pop'] = is_alias_pop
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if label_sort_by is not None:
        kwargs['label_sort_by'] = label_sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_labels,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_labels,
            limit,
            page_size,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_labels(
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_entity_group.command(name=cli_util.override('log_analytics.list_log_analytics_entities.command_name', 'list'), help=u"""Return a list of log analytics entities. \n[Command Reference](listLogAnalyticsEntities)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--name', help=u"""A filter to return only log analytics entities whose name matches the entire name given. The match is case-insensitive.""")
@cli_util.option('--name-contains', help=u"""A filter to return only log analytics entities whose name contains the name given. The match is case-insensitive.""")
@cli_util.option('--entity-type-name', multiple=True, help=u"""A filter to return only log analytics entities whose entityTypeName matches the entire log analytics entity type name of one of the entityTypeNames given in the list. The match is case-insensitive.""")
@cli_util.option('--cloud-resource-id', help=u"""A filter to return only log analytics entities whose cloudResourceId matches the cloudResourceId given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), help=u"""A filter to return only those log analytics entities with the specified lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--lifecycle-details-contains', help=u"""A filter to return only log analytics entities whose lifecycleDetails contains the specified string.""")
@cli_util.option('--is-management-agent-id-null', type=custom_types.CliCaseInsensitiveChoice(["true", "false"]), help=u"""A filter to return only those log analytics entities whose managementAgentId is null or is not null.""")
@cli_util.option('--hostname', help=u"""A filter to return only log analytics entities whose hostname matches the entire hostname given.""")
@cli_util.option('--hostname-contains', help=u"""A filter to return only log analytics entities whose hostname contains the substring given. The match is case-insensitive.""")
@cli_util.option('--source-id', help=u"""A filter to return only log analytics entities whose sourceId matches the sourceId given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "name"]), help=u"""The field to sort entities by. Only one sort order may be provided. Default order for timeCreated and timeUpdated is descending. Default order for entity name is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'entity-type-name': {'module': 'log_analytics', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'entity-type-name': {'module': 'log_analytics', 'class': 'list[string]'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsEntityCollection'})
@cli_util.wrap_exceptions
def list_log_analytics_entities(ctx, from_json, all_pages, page_size, namespace_name, compartment_id, name, name_contains, entity_type_name, cloud_resource_id, lifecycle_state, lifecycle_details_contains, is_management_agent_id_null, hostname, hostname_contains, source_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if name_contains is not None:
        kwargs['name_contains'] = name_contains
    if entity_type_name is not None and len(entity_type_name) > 0:
        kwargs['entity_type_name'] = entity_type_name
    if cloud_resource_id is not None:
        kwargs['cloud_resource_id'] = cloud_resource_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if lifecycle_details_contains is not None:
        kwargs['lifecycle_details_contains'] = lifecycle_details_contains
    if is_management_agent_id_null is not None:
        kwargs['is_management_agent_id_null'] = is_management_agent_id_null
    if hostname is not None:
        kwargs['hostname'] = hostname
    if hostname_contains is not None:
        kwargs['hostname_contains'] = hostname_contains
    if source_id is not None:
        kwargs['source_id'] = source_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_log_analytics_entities,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_log_analytics_entities,
            limit,
            page_size,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_log_analytics_entities(
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_entity_type_group.command(name=cli_util.override('log_analytics.list_log_analytics_entity_types.command_name', 'list'), help=u"""Return a list of log analytics entity types. \n[Command Reference](listLogAnalyticsEntityTypes)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--name', help=u"""A filter to return only log analytics entity types whose name matches the entire name given. The match is case-insensitive.""")
@cli_util.option('--name-contains', help=u"""A filter to return only log analytics entity types whose name or internalName contains name given. The match is case-insensitive.""")
@cli_util.option('--cloud-type', type=custom_types.CliCaseInsensitiveChoice(["CLOUD", "NON_CLOUD"]), help=u"""A filter to return CLOUD or NON_CLOUD entity types.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), help=u"""A filter to return only those log analytics entities with the specified lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "name"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated and timeUpdated is descending. Default order for name is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsEntityTypeCollection'})
@cli_util.wrap_exceptions
def list_log_analytics_entity_types(ctx, from_json, all_pages, page_size, namespace_name, name, name_contains, cloud_type, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if name_contains is not None:
        kwargs['name_contains'] = name_contains
    if cloud_type is not None:
        kwargs['cloud_type'] = cloud_type
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_log_analytics_entity_types,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_log_analytics_entity_types,
            limit,
            page_size,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_log_analytics_entity_types(
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_log_group_group.command(name=cli_util.override('log_analytics.list_log_analytics_log_groups.command_name', 'list'), help=u"""Returns a list of Log-Analytics groups. \n[Command Reference](listLogAnalyticsLogGroups)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only log analytics log groups whose displayName matches the entire display name given. The match is case-insensitive.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsLogGroupSummaryCollection'})
@cli_util.wrap_exceptions
def list_log_analytics_log_groups(ctx, from_json, all_pages, page_size, namespace_name, compartment_id, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_log_analytics_log_groups,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_log_analytics_log_groups,
            limit,
            page_size,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_log_analytics_log_groups(
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_object_collection_rule_group.command(name=cli_util.override('log_analytics.list_log_analytics_object_collection_rules.command_name', 'list'), help=u"""Gets list of configuration details of Object Storage based collection rules. \n[Command Reference](listLogAnalyticsObjectCollectionRules)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--name', help=u"""A filter to return rules only matching with this name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), help=u"""Lifecycle state filter.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeUpdated", "timeCreated", "name"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeUpdated is descending. Default order for name is ascending. If no value is specified timeUpdated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsObjectCollectionRuleCollection'})
@cli_util.wrap_exceptions
def list_log_analytics_object_collection_rules(ctx, from_json, all_pages, page_size, namespace_name, compartment_id, name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_log_analytics_object_collection_rules,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_log_analytics_object_collection_rules,
            limit,
            page_size,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_log_analytics_object_collection_rules(
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_source_group.command(name=cli_util.override('log_analytics.list_meta_source_types.command_name', 'list-meta-source-types'), help=u"""get all meta source types \n[Command Reference](listMetaSourceTypes)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', help=u"""sort by field""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsMetaSourceTypeCollection'})
@cli_util.wrap_exceptions
def list_meta_source_types(ctx, from_json, all_pages, page_size, namespace_name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

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
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_meta_source_types,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_meta_source_types,
            limit,
            page_size,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_meta_source_types(
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@namespace_group.command(name=cli_util.override('log_analytics.list_namespaces.command_name', 'list'), help=u"""Given a tenancy OCID, this API returns the namespace of the tenancy if it is valid and subscribed to the region.  The result also indicates if the tenancy is onboarded with Logging Analytics. \n[Command Reference](listNamespaces)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'NamespaceCollection'})
@cli_util.wrap_exceptions
def list_namespaces(ctx, from_json, all_pages, compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.list_namespaces(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_parser_group.command(name=cli_util.override('log_analytics.list_parser_functions.command_name', 'list-parser-functions'), help=u"""get pre-process plugin instance \n[Command Reference](listParserFunctions)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--parser-name', help=u"""parserName""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', help=u"""sort by field""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsParserFunctionCollection'})
@cli_util.wrap_exceptions
def list_parser_functions(ctx, from_json, all_pages, page_size, namespace_name, parser_name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if parser_name is not None:
        kwargs['parser_name'] = parser_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_parser_functions,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_parser_functions,
            limit,
            page_size,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_parser_functions(
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_parser_group.command(name=cli_util.override('log_analytics.list_parser_meta_plugins.command_name', 'list-parser-meta-plugins'), help=u"""get pre-process Meta plugins \n[Command Reference](listParserMetaPlugins)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', help=u"""sort by field""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsParserMetaPluginCollection'})
@cli_util.wrap_exceptions
def list_parser_meta_plugins(ctx, from_json, all_pages, page_size, namespace_name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

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
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_parser_meta_plugins,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_parser_meta_plugins,
            limit,
            page_size,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_parser_meta_plugins(
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_parser_group.command(name=cli_util.override('log_analytics.list_parsers.command_name', 'list-parsers'), help=u"""List parsers passing specified filter \n[Command Reference](listParsers)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--is-match-all', type=click.BOOL, help=u"""isMatchAll""")
@cli_util.option('--source-type', type=custom_types.CliCaseInsensitiveChoice(["OS_FILE", "SYSLOG", "ODL", "OS_WINDOWS_SYS"]), help=u"""source type""")
@cli_util.option('--parser-name', help=u"""parserName""")
@cli_util.option('--parser-display-text', help=u"""search by parser display name or description""")
@cli_util.option('--parser-type', type=custom_types.CliCaseInsensitiveChoice(["ALL", "REGEX", "XML", "JSON"]), help=u"""parserType""")
@cli_util.option('--is-system', type=custom_types.CliCaseInsensitiveChoice(["ALL", "CUSTOM", "BUILT_IN"]), help=u"""Is system param of value (all, custom, sourceUsing)""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "type", "sourcesCount", "timeUpdated"]), help=u"""sort by parser""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsParserCollection'})
@cli_util.wrap_exceptions
def list_parsers(ctx, from_json, all_pages, page_size, namespace_name, is_match_all, source_type, parser_name, parser_display_text, parser_type, is_system, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if is_match_all is not None:
        kwargs['is_match_all'] = is_match_all
    if source_type is not None:
        kwargs['source_type'] = source_type
    if parser_name is not None:
        kwargs['parser_name'] = parser_name
    if parser_display_text is not None:
        kwargs['parser_display_text'] = parser_display_text
    if parser_type is not None:
        kwargs['parser_type'] = parser_type
    if is_system is not None:
        kwargs['is_system'] = is_system
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_parsers,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_parsers,
            limit,
            page_size,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_parsers(
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@query_work_request_group.command(name=cli_util.override('log_analytics.list_query_work_requests.command_name', 'list'), help=u"""List active asynchronous queries. \n[Command Reference](listQueryWorkRequests)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--mode', type=custom_types.CliCaseInsensitiveChoice(["ALL", "FOREGROUND", "BACKGROUND"]), help=u"""Filter based on job execution mode""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeStarted", "timeExpires"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeStarted is descending. If no value is specified timeStarted is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'QueryWorkRequestCollection'})
@cli_util.wrap_exceptions
def list_query_work_requests(ctx, from_json, all_pages, page_size, namespace_name, compartment_id, mode, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if mode is not None:
        kwargs['mode'] = mode
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_query_work_requests,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_query_work_requests,
            limit,
            page_size,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_query_work_requests(
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@scheduled_task_group.command(name=cli_util.override('log_analytics.list_scheduled_tasks.command_name', 'list'), help=u"""Lists scheduled tasks. \n[Command Reference](listScheduledTasks)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--task-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SAVED_SEARCH", "ACCELERATION", "PURGE", "ACCELERATION_MAINTENANCE"]), help=u"""Required parameter to specify schedule task type.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'ScheduledTaskCollection'})
@cli_util.wrap_exceptions
def list_scheduled_tasks(ctx, from_json, all_pages, page_size, namespace_name, task_type, compartment_id, limit, page, display_name, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_scheduled_tasks,
            namespace_name=namespace_name,
            task_type=task_type,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_scheduled_tasks,
            limit,
            page_size,
            namespace_name=namespace_name,
            task_type=task_type,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_scheduled_tasks(
            namespace_name=namespace_name,
            task_type=task_type,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_association_group.command(name=cli_util.override('log_analytics.list_source_associations.command_name', 'list-source-associations'), help=u"""association summary by source \n[Command Reference](listSourceAssociations)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--source-name', required=True, help=u"""sourceName""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--entity-id', help=u"""The entity OCID.""")
@cli_util.option('--life-cycle-state', type=custom_types.CliCaseInsensitiveChoice(["ALL", "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED"]), help=u"""Status""")
@cli_util.option('--is-show-total', type=click.BOOL, help=u"""is Show Total""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["entityName", "timeLastAttempted", "status"]), help=u"""sort by field""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsAssociationCollection'})
@cli_util.wrap_exceptions
def list_source_associations(ctx, from_json, all_pages, page_size, namespace_name, source_name, compartment_id, entity_id, life_cycle_state, is_show_total, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if entity_id is not None:
        kwargs['entity_id'] = entity_id
    if life_cycle_state is not None:
        kwargs['life_cycle_state'] = life_cycle_state
    if is_show_total is not None:
        kwargs['is_show_total'] = is_show_total
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_source_associations,
            namespace_name=namespace_name,
            source_name=source_name,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_source_associations,
            limit,
            page_size,
            namespace_name=namespace_name,
            source_name=source_name,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_source_associations(
            namespace_name=namespace_name,
            source_name=source_name,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_source_group.command(name=cli_util.override('log_analytics.list_source_extended_field_definitions.command_name', 'list-source-extended-field-definitions'), help=u"""get source extended fields for source with specified Id \n[Command Reference](listSourceExtendedFieldDefinitions)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--source-name', required=True, help=u"""source name""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["baseFieldName", "regularExpression"]), help=u"""sort by source extended field definition""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsSourceExtendedFieldDefinitionCollection'})
@cli_util.wrap_exceptions
def list_source_extended_field_definitions(ctx, from_json, all_pages, page_size, namespace_name, source_name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(source_name, six.string_types) and len(source_name.strip()) == 0:
        raise click.UsageError('Parameter --source-name cannot be whitespace or empty string')

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
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_source_extended_field_definitions,
            namespace_name=namespace_name,
            source_name=source_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_source_extended_field_definitions,
            limit,
            page_size,
            namespace_name=namespace_name,
            source_name=source_name,
            **kwargs
        )
    else:
        result = client.list_source_extended_field_definitions(
            namespace_name=namespace_name,
            source_name=source_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_source_group.command(name=cli_util.override('log_analytics.list_source_label_operators.command_name', 'list-source-label-operators'), help=u"""list source label operators \n[Command Reference](listSourceLabelOperators)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', help=u"""sort by field""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsLabelOperatorCollection'})
@cli_util.wrap_exceptions
def list_source_label_operators(ctx, from_json, all_pages, page_size, namespace_name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

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
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_source_label_operators,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_source_label_operators,
            limit,
            page_size,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_source_label_operators(
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_source_group.command(name=cli_util.override('log_analytics.list_source_meta_functions.command_name', 'list-source-meta-functions'), help=u"""get source meta functions \n[Command Reference](listSourceMetaFunctions)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', help=u"""sort by field""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsMetaFunctionCollection'})
@cli_util.wrap_exceptions
def list_source_meta_functions(ctx, from_json, all_pages, page_size, namespace_name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

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
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_source_meta_functions,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_source_meta_functions,
            limit,
            page_size,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_source_meta_functions(
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_source_group.command(name=cli_util.override('log_analytics.list_source_patterns.command_name', 'list-source-patterns'), help=u"""get source patterns for source with specified Id \n[Command Reference](listSourcePatterns)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--source-name', required=True, help=u"""source name""")
@cli_util.option('--is-include', type=click.BOOL, help=u"""is included source patterns""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["patternText"]), help=u"""sort by source pattern text""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsSourcePatternCollection'})
@cli_util.wrap_exceptions
def list_source_patterns(ctx, from_json, all_pages, page_size, namespace_name, source_name, is_include, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(source_name, six.string_types) and len(source_name.strip()) == 0:
        raise click.UsageError('Parameter --source-name cannot be whitespace or empty string')

    kwargs = {}
    if is_include is not None:
        kwargs['is_include'] = is_include
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_source_patterns,
            namespace_name=namespace_name,
            source_name=source_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_source_patterns,
            limit,
            page_size,
            namespace_name=namespace_name,
            source_name=source_name,
            **kwargs
        )
    else:
        result = client.list_source_patterns(
            namespace_name=namespace_name,
            source_name=source_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_analytics_source_group.command(name=cli_util.override('log_analytics.list_sources.command_name', 'list-sources'), help=u"""source list \n[Command Reference](listSources)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--entity-type', help=u"""entityType""")
@cli_util.option('--source-display-text', help=u"""search by source display name or description""")
@cli_util.option('--is-system', type=custom_types.CliCaseInsensitiveChoice(["ALL", "CUSTOM", "BUILT_IN"]), help=u"""Is system param of value (all, custom, sourceUsing)""")
@cli_util.option('--is-auto-associated', type=click.BOOL, help=u"""auto association flag""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "timeUpdated", "associationCount", "sourceType"]), help=u"""sort by source""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--name', help=u"""A filter to return only log analytics entities whose name matches the entire name given. The match is case-insensitive.""")
@cli_util.option('--is-simplified', type=click.BOOL, help=u"""is simplified""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsSourceCollection'})
@cli_util.wrap_exceptions
def list_sources(ctx, from_json, all_pages, page_size, namespace_name, compartment_id, entity_type, source_display_text, is_system, is_auto_associated, sort_order, sort_by, limit, page, name, is_simplified):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if entity_type is not None:
        kwargs['entity_type'] = entity_type
    if source_display_text is not None:
        kwargs['source_display_text'] = source_display_text
    if is_system is not None:
        kwargs['is_system'] = is_system
    if is_auto_associated is not None:
        kwargs['is_auto_associated'] = is_auto_associated
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if name is not None:
        kwargs['name'] = name
    if is_simplified is not None:
        kwargs['is_simplified'] = is_simplified
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_sources,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_sources,
            limit,
            page_size,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_sources(
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@storage_group.command(name=cli_util.override('log_analytics.list_storage_work_request_errors.command_name', 'list-storage-work-request-errors'), help=u"""This API returns the list of work request errors if any. \n[Command Reference](listStorageWorkRequestErrors)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--work-request-id', required=True, help=u"""Work Request Identifier [OCID]  for the asynchronous request.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_storage_work_request_errors(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, namespace_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_storage_work_request_errors,
            compartment_id=compartment_id,
            work_request_id=work_request_id,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_storage_work_request_errors,
            limit,
            page_size,
            compartment_id=compartment_id,
            work_request_id=work_request_id,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_storage_work_request_errors(
            compartment_id=compartment_id,
            work_request_id=work_request_id,
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@storage_group.command(name=cli_util.override('log_analytics.list_storage_work_requests.command_name', 'list-storage-work-requests'), help=u"""This API lists storage work requests.  Use query parameters to narrow down or sort the result list. \n[Command Reference](listStorageWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted", "timeExpires", "timeFinished"]), help=u"""This is the query parameter of which field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending. If no value is specified timeAccepted is default.""")
@cli_util.option('--operation-type', type=custom_types.CliCaseInsensitiveChoice(["OFFBOARD_TENANCY", "PURGE_STORAGE_DATA", "RECALL_ARCHIVED_STORAGE_DATA", "RELEASE_RECALLED_STORAGE_DATA", "ARCHIVE_STORAGE_DATA", "CLEANUP_ARCHIVAL_STORAGE_DATA"]), help=u"""The is the work request type query parameter""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "CANCELED", "FAILED", "IN_PROGRESS", "SUCCEEDED"]), help=u"""The is the work request status query parameter""")
@cli_util.option('--time-started', type=custom_types.CLI_DATETIME, help=u"""The is the query parameter of when the processing of work request was started""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-finished', type=custom_types.CLI_DATETIME, help=u"""The is the query parameter of when the processing of work request was finished""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--policy-name', help=u"""This is the query parameter of purge policy name""")
@cli_util.option('--policy-id', help=u"""This is the query parameter of purge policy ID""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'StorageWorkRequestCollection'})
@cli_util.wrap_exceptions
def list_storage_work_requests(ctx, from_json, all_pages, page_size, compartment_id, namespace_name, limit, page, sort_order, sort_by, operation_type, status, time_started, time_finished, policy_name, policy_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if operation_type is not None:
        kwargs['operation_type'] = operation_type
    if status is not None:
        kwargs['status'] = status
    if time_started is not None:
        kwargs['time_started'] = time_started
    if time_finished is not None:
        kwargs['time_finished'] = time_finished
    if policy_name is not None:
        kwargs['policy_name'] = policy_name
    if policy_id is not None:
        kwargs['policy_id'] = policy_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_storage_work_requests,
            compartment_id=compartment_id,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_storage_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_storage_work_requests(
            compartment_id=compartment_id,
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@char_encoding_collection_group.command(name=cli_util.override('log_analytics.list_supported_char_encodings.command_name', 'list-supported-char-encodings'), help=u"""Gets the list of character encodings supported for log files. \n[Command Reference](listSupportedCharEncodings)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'CharEncodingCollection'})
@cli_util.wrap_exceptions
def list_supported_char_encodings(ctx, from_json, all_pages, page_size, namespace_name, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_supported_char_encodings,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_supported_char_encodings,
            limit,
            page_size,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_supported_char_encodings(
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@timezone_collection_group.command(name=cli_util.override('log_analytics.list_supported_timezones.command_name', 'list-supported-timezones'), help=u"""Gets timezones that are supported when performing uploads. \n[Command Reference](listSupportedTimezones)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'TimezoneCollection'})
@cli_util.wrap_exceptions
def list_supported_timezones(ctx, from_json, all_pages, page_size, namespace_name, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_supported_timezones,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_supported_timezones,
            limit,
            page_size,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_supported_timezones(
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@upload_group.command(name=cli_util.override('log_analytics.list_upload_files.command_name', 'list-upload-files'), help=u"""Gets list of files in an upload. \n[Command Reference](listUploadFiles)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--upload-reference', required=True, help=u"""Unique internal identifier to refer to upload container""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "fileName", "logGroup", "sourceName", "status"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.""")
@cli_util.option('--search-str', help=u"""Search string used to filtering uploads based on file name, log group name and log source name.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["IN_PROGRESS", "SUCCESSFUL", "FAILED"]), multiple=True, help=u"""Upload Status.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'UploadFileCollection'})
@cli_util.wrap_exceptions
def list_upload_files(ctx, from_json, all_pages, page_size, namespace_name, upload_reference, limit, page, sort_order, sort_by, search_str, status):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(upload_reference, six.string_types) and len(upload_reference.strip()) == 0:
        raise click.UsageError('Parameter --upload-reference cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if search_str is not None:
        kwargs['search_str'] = search_str
    if status is not None and len(status) > 0:
        kwargs['status'] = status
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_upload_files,
            namespace_name=namespace_name,
            upload_reference=upload_reference,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_upload_files,
            limit,
            page_size,
            namespace_name=namespace_name,
            upload_reference=upload_reference,
            **kwargs
        )
    else:
        result = client.list_upload_files(
            namespace_name=namespace_name,
            upload_reference=upload_reference,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@upload_group.command(name=cli_util.override('log_analytics.list_upload_warnings.command_name', 'list-upload-warnings'), help=u"""Gets list of warnings in an upload explaining the failures due to incorrect configuration. \n[Command Reference](listUploadWarnings)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--upload-reference', required=True, help=u"""Unique internal identifier to refer to upload container""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'UploadWarningCollection'})
@cli_util.wrap_exceptions
def list_upload_warnings(ctx, from_json, all_pages, page_size, namespace_name, upload_reference, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(upload_reference, six.string_types) and len(upload_reference.strip()) == 0:
        raise click.UsageError('Parameter --upload-reference cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_upload_warnings,
            namespace_name=namespace_name,
            upload_reference=upload_reference,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_upload_warnings,
            limit,
            page_size,
            namespace_name=namespace_name,
            upload_reference=upload_reference,
            **kwargs
        )
    else:
        result = client.list_upload_warnings(
            namespace_name=namespace_name,
            upload_reference=upload_reference,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@upload_group.command(name=cli_util.override('log_analytics.list_uploads.command_name', 'list'), help=u"""Gets a list of all On-demand uploads. To use this and other API operations, you must be authorized in an IAM policy. \n[Command Reference](listUploads)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--name', help=u"""Name of the upload container.""")
@cli_util.option('--name-contains', help=u"""A filter to return only uploads whose name contains the given name.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeUpdated", "timeCreated", "name"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeUpdated is descending. Default order for name is ascending. If no value is specified timeUpdated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'UploadCollection'})
@cli_util.wrap_exceptions
def list_uploads(ctx, from_json, all_pages, page_size, namespace_name, name, name_contains, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if name_contains is not None:
        kwargs['name_contains'] = name_contains
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_uploads,
            namespace_name=namespace_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_uploads,
            limit,
            page_size,
            namespace_name=namespace_name,
            **kwargs
        )
    else:
        result = client.list_uploads(
            namespace_name=namespace_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('log_analytics.list_work_request_errors.command_name', 'list'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--work-request-id', required=True, help=u"""Work Request Identifier [OCID]  for the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, namespace_name, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            namespace_name=namespace_name,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            namespace_name=namespace_name,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            namespace_name=namespace_name,
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_group.command(name=cli_util.override('log_analytics.list_work_request_logs.command_name', 'list'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--work-request-id', required=True, help=u"""Work Request Identifier [OCID]  for the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'WorkRequestLogCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, namespace_name, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            namespace_name=namespace_name,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            namespace_name=namespace_name,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            namespace_name=namespace_name,
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('log_analytics.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'WorkRequestCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, namespace_name, compartment_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@namespace_group.command(name=cli_util.override('log_analytics.offboard_namespace.command_name', 'offboard'), help=u"""Off-boards a tenant from Logging Analytics \n[Command Reference](offboardNamespace)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def offboard_namespace(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.offboard_namespace(
        namespace_name=namespace_name,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@namespace_group.command(name=cli_util.override('log_analytics.onboard_namespace.command_name', 'onboard'), help=u"""On-boards a tenant to Logging Analytics. \n[Command Reference](onboardNamespace)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def onboard_namespace(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.onboard_namespace(
        namespace_name=namespace_name,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@query_details_group.command(name=cli_util.override('log_analytics.parse_query.command_name', 'parse-query'), help=u"""Describe query \n[Command Reference](parseQuery)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--query-string', required=True, help=u"""Query to parse.""")
@cli_util.option('--sub-system', required=True, type=custom_types.CliCaseInsensitiveChoice(["LOG"]), help=u"""Default subsystem to qualify fields with in the queryString if not specified.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'ParseQueryOutput'})
@cli_util.wrap_exceptions
def parse_query(ctx, from_json, namespace_name, query_string, sub_system):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['queryString'] = query_string
    _details['subSystem'] = sub_system

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.parse_query(
        namespace_name=namespace_name,
        parse_query_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@storage_group.command(name=cli_util.override('log_analytics.purge_storage_data.command_name', 'purge-storage-data'), help=u"""This API submits a work request to purge data. Only data from log groups that the user has permission to delete will be purged.  To purge all data, the user must have permission to all log groups. \n[Command Reference](purgeStorageData)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""This is the compartment OCID under which the data will be purged and required permission will be checked""")
@cli_util.option('--time-data-ended', required=True, type=custom_types.CLI_DATETIME, help=u"""This is the end of the purge time interval""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""If true, purge child compartments data""")
@cli_util.option('--purge-query-string', help=u"""This is the solr query used to filter data, '*' means all""")
@cli_util.option('--data-type', type=custom_types.CliCaseInsensitiveChoice(["LOG", "LOOKUP"]), help=u"""This is the type of the log data to be purged""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def purge_storage_data(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, compartment_id, time_data_ended, compartment_id_in_subtree, purge_query_string, data_type, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['timeDataEnded'] = time_data_ended

    if compartment_id_in_subtree is not None:
        _details['compartmentIdInSubtree'] = compartment_id_in_subtree

    if purge_query_string is not None:
        _details['purgeQueryString'] = purge_query_string

    if data_type is not None:
        _details['dataType'] = data_type

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.purge_storage_data(
        namespace_name=namespace_name,
        purge_storage_data_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_storage_work_request') and callable(getattr(client, 'get_storage_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_storage_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@query_work_request_group.command(name=cli_util.override('log_analytics.put_query_work_request_background.command_name', 'put-query-work-request-background'), help=u"""Put the work request specified by {workRequestId} into the background. Backgrounded queries will preserve query results on query completion for up to 7 days for recall. After 7 days the results and query expire. \n[Command Reference](putQueryWorkRequestBackground)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--work-request-id', required=True, help=u"""Work Request Identifier [OCID]  for the asynchronous request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'QueryWorkRequest'})
@cli_util.wrap_exceptions
def put_query_work_request_background(ctx, from_json, namespace_name, work_request_id, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.put_query_work_request_background(
        namespace_name=namespace_name,
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@query_details_group.command(name=cli_util.override('log_analytics.query.command_name', 'query'), help=u"""Performs a log analytics search, if shouldRunAsync is false returns the query results once they become available subject to 60 second timeout. If a query is subject to exceed that time then it should be run asynchronously. Asynchronous query submissions return the queryWorkRequestId to use for execution tracking, query submission lifecycle actions and to poll for query results. \n[Command Reference](query)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID] .""")
@cli_util.option('--query-string', required=True, help=u"""Query to perform. Must conform to logging analytic querylanguage syntax. Syntax errors will be returned if present.""")
@cli_util.option('--sub-system', required=True, type=custom_types.CliCaseInsensitiveChoice(["LOG"]), help=u"""Default subsystem to qualify fields with in the queryString if not specified.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Flag to search all child compartments of the compartment Id specified in the compartmentId query parameter.""")
@cli_util.option('--saved-search-id', help=u"""Saved search OCID for this query if known.""")
@cli_util.option('--max-total-count', type=click.INT, help=u"""Maximum number of results to count.  Note a maximum of 2001 will be enforced; that is, actualMaxTotalCountUsed = Math.min(maxTotalCount, 2001).""")
@cli_util.option('--time-filter', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--scope-filters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of filters to be applied when the query executes. More than one filter per field is not permitted.

This option is a JSON list with items of type ScopeFilter.  For documentation on ScopeFilter please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/ScopeFilter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--query-timeout-in-seconds', type=click.INT, help=u"""Amount of time, in seconds, allowed for a query to execute. If this time expires before the query is complete, any partial results will be returned.""")
@cli_util.option('--should-run-async', type=click.BOOL, help=u"""Option to run the query asynchronously. This will lead to a LogAnalyticsQueryJobWorkRequest being submitted and the {workRequestId} will be returned to use for fetching the results.""")
@cli_util.option('--async-mode', type=custom_types.CliCaseInsensitiveChoice(["FOREGROUND", "BACKGROUND"]), help=u"""Execution mode for the query if running asynchronously i.e (shouldRunAsync is set to true).""")
@cli_util.option('--should-include-total-count', type=click.BOOL, help=u"""Include the total number of results from the query. Note, this value will always be equal to or less than maxTotalCount.""")
@cli_util.option('--should-include-columns', type=click.BOOL, help=u"""Include columns in response""")
@cli_util.option('--should-include-fields', type=click.BOOL, help=u"""Include fields in response""")
@cli_util.option('--should-use-acceleration', type=click.BOOL, help=u"""Controls if query should ignore pre-calculated results if available and only use raw data. If set and no acceleration data is found it will fallback to raw data.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""Maximum number of results to return in this request.  Note a limit=-1 returns all results from pageId onwards up to maxtotalCount.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'time-filter': {'module': 'log_analytics', 'class': 'TimeRange'}, 'scope-filters': {'module': 'log_analytics', 'class': 'list[ScopeFilter]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'time-filter': {'module': 'log_analytics', 'class': 'TimeRange'}, 'scope-filters': {'module': 'log_analytics', 'class': 'list[ScopeFilter]'}}, output_type={'module': 'log_analytics', 'class': 'QueryAggregation'})
@cli_util.wrap_exceptions
def query(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, compartment_id, query_string, sub_system, compartment_id_in_subtree, saved_search_id, max_total_count, time_filter, scope_filters, query_timeout_in_seconds, should_run_async, async_mode, should_include_total_count, should_include_columns, should_include_fields, should_use_acceleration, page, limit):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['queryString'] = query_string
    _details['subSystem'] = sub_system

    if compartment_id_in_subtree is not None:
        _details['compartmentIdInSubtree'] = compartment_id_in_subtree

    if saved_search_id is not None:
        _details['savedSearchId'] = saved_search_id

    if max_total_count is not None:
        _details['maxTotalCount'] = max_total_count

    if time_filter is not None:
        _details['timeFilter'] = cli_util.parse_json_parameter("time_filter", time_filter)

    if scope_filters is not None:
        _details['scopeFilters'] = cli_util.parse_json_parameter("scope_filters", scope_filters)

    if query_timeout_in_seconds is not None:
        _details['queryTimeoutInSeconds'] = query_timeout_in_seconds

    if should_run_async is not None:
        _details['shouldRunAsync'] = should_run_async

    if async_mode is not None:
        _details['asyncMode'] = async_mode

    if should_include_total_count is not None:
        _details['shouldIncludeTotalCount'] = should_include_total_count

    if should_include_columns is not None:
        _details['shouldIncludeColumns'] = should_include_columns

    if should_include_fields is not None:
        _details['shouldIncludeFields'] = should_include_fields

    if should_use_acceleration is not None:
        _details['shouldUseAcceleration'] = should_use_acceleration

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.query(
        namespace_name=namespace_name,
        query_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_query_work_request') and callable(getattr(client, 'get_query_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_query_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@storage_group.command(name=cli_util.override('log_analytics.recall_archived_data.command_name', 'recall-archived-data'), help=u"""This API submits a work request to recall archived data based on time interval and data type. \n[Command Reference](recallArchivedData)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""This is the compartment OCID for permission checking""")
@cli_util.option('--time-data-ended', required=True, type=custom_types.CLI_DATETIME, help=u"""This is the end of the time interval""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-data-started', required=True, type=custom_types.CLI_DATETIME, help=u"""This is the start of the time interval""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--data-type', type=custom_types.CliCaseInsensitiveChoice(["LOG", "LOOKUP"]), help=u"""This is the type of the log data to be recalled""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def recall_archived_data(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, compartment_id, time_data_ended, time_data_started, data_type, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['timeDataEnded'] = time_data_ended
    _details['timeDataStarted'] = time_data_started

    if data_type is not None:
        _details['dataType'] = data_type

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.recall_archived_data(
        namespace_name=namespace_name,
        recall_archived_data_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_storage_work_request') and callable(getattr(client, 'get_storage_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_storage_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@log_analytics_lookup_group.command(name=cli_util.override('log_analytics.register_lookup.command_name', 'register-lookup'), help=u"""register lookup \n[Command Reference](registerLookup)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["Lookup", "Dictionary"]), help=u"""type - possible values are Lookup or Dictionary""")
@cli_util.option('--register-lookup-content-file-body', required=True, help=u"""file containing data for lookup creation""")
@cli_util.option('--name', help=u"""A filter to return only log analytics entities whose name matches the entire name given. The match is case-insensitive.""")
@cli_util.option('--description', help=u"""Description of the fields to get""")
@cli_util.option('--char-encoding', help=u"""Character Encoding""")
@cli_util.option('--is-hidden', type=click.BOOL, help=u"""is hidden""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsLookup'})
@cli_util.wrap_exceptions
def register_lookup(ctx, from_json, namespace_name, type, register_lookup_content_file_body, name, description, char_encoding, is_hidden):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if description is not None:
        kwargs['description'] = description
    if char_encoding is not None:
        kwargs['char_encoding'] = char_encoding
    if is_hidden is not None:
        kwargs['is_hidden'] = is_hidden
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    # do not automatically retry operations with binary inputs
    kwargs['retry_strategy'] = oci.retry.NoneRetryStrategy()

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.register_lookup(
        namespace_name=namespace_name,
        type=type,
        register_lookup_content_file_body=register_lookup_content_file_body,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@storage_group.command(name=cli_util.override('log_analytics.release_recalled_data.command_name', 'release-recalled-data'), help=u"""This API submits a work request to release recalled data based on time interval and data type. \n[Command Reference](releaseRecalledData)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""This is the compartment OCID for permission checking""")
@cli_util.option('--time-data-ended', required=True, type=custom_types.CLI_DATETIME, help=u"""This is the end of the time interval""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-data-started', required=True, type=custom_types.CLI_DATETIME, help=u"""This is the start of the time interval""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--data-type', type=custom_types.CliCaseInsensitiveChoice(["LOG", "LOOKUP"]), help=u"""This is the type of the recalled data to be released""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def release_recalled_data(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, compartment_id, time_data_ended, time_data_started, data_type, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['timeDataEnded'] = time_data_ended
    _details['timeDataStarted'] = time_data_started

    if data_type is not None:
        _details['dataType'] = data_type

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.release_recalled_data(
        namespace_name=namespace_name,
        release_recalled_data_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_storage_work_request') and callable(getattr(client, 'get_storage_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_storage_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@log_analytics_entity_group.command(name=cli_util.override('log_analytics.remove_entity_associations.command_name', 'remove'), help=u"""Delete association between input source log analytics entity and destination entities. \n[Command Reference](removeEntityAssociations)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--log-analytics-entity-id', required=True, help=u"""The log analytics entity OCID.""")
@cli_util.option('--association-entities', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Destination entities OCIDs with which associations are to be deleted""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'association-entities': {'module': 'log_analytics', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'association-entities': {'module': 'log_analytics', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def remove_entity_associations(ctx, from_json, namespace_name, log_analytics_entity_id, association_entities, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(log_analytics_entity_id, six.string_types) and len(log_analytics_entity_id.strip()) == 0:
        raise click.UsageError('Parameter --log-analytics-entity-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['associationEntities'] = cli_util.parse_json_parameter("association_entities", association_entities)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.remove_entity_associations(
        namespace_name=namespace_name,
        log_analytics_entity_id=log_analytics_entity_id,
        remove_entity_associations_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@scheduled_task_group.command(name=cli_util.override('log_analytics.run.command_name', 'run'), help=u"""Execute the saved search acceleration task in the foreground. The ScheduledTask taskType must be ACCELERATION. Optionally specify time range (timeStart and timeEnd). The default is all time. \n[Command Reference](run)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--scheduled-task-id', required=True, help=u"""Unique scheduledTask id returned from task create. If invalid will lead to a 404 not found.""")
@cli_util.option('--time-start', type=custom_types.CLI_DATETIME, help=u"""Optional parameter to specify start of time range, in the format defined by RFC3339. Default value is beginning of time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', type=custom_types.CLI_DATETIME, help=u"""Optional parameter to specify end of time range, in the format defined by RFC3339. Default value is end of time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def run(ctx, from_json, namespace_name, scheduled_task_id, time_start, time_end):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(scheduled_task_id, six.string_types) and len(scheduled_task_id.strip()) == 0:
        raise click.UsageError('Parameter --scheduled-task-id cannot be whitespace or empty string')

    kwargs = {}
    if time_start is not None:
        kwargs['time_start'] = time_start
    if time_end is not None:
        kwargs['time_end'] = time_end
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.run(
        namespace_name=namespace_name,
        scheduled_task_id=scheduled_task_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@query_details_group.command(name=cli_util.override('log_analytics.suggest.command_name', 'suggest'), help=u"""Returns a context specific list of either commands, fields, or values to append to the end of the specified query string if applicable. \n[Command Reference](suggest)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier [OCID] .""")
@cli_util.option('--query-string', required=True, help=u"""Query seeking suggestions for.""")
@cli_util.option('--sub-system', required=True, type=custom_types.CliCaseInsensitiveChoice(["LOG"]), help=u"""Default subsystem to qualify fields with in the queryString if not specified.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Flag to search all child compartments of the compartment Id specified in the compartmentId query parameter.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'SuggestOutput'})
@cli_util.wrap_exceptions
def suggest(ctx, from_json, namespace_name, compartment_id, query_string, sub_system, compartment_id_in_subtree):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['queryString'] = query_string
    _details['subSystem'] = sub_system

    if compartment_id_in_subtree is not None:
        _details['compartmentIdInSubtree'] = compartment_id_in_subtree

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.suggest(
        namespace_name=namespace_name,
        suggest_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_parser_group.command(name=cli_util.override('log_analytics.test_parser.command_name', 'test-parser'), help=u"""test parser \n[Command Reference](testParser)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--content', help=u"""content""")
@cli_util.option('--description', help=u"""description""")
@cli_util.option('--display-name', help=u"""Display name""")
@cli_util.option('--encoding', help=u"""encoding""")
@cli_util.option('--example-content', help=u"""exampleContent""")
@cli_util.option('--field-maps', type=custom_types.CLI_COMPLEX_TYPE, help=u"""fieldMaps

This option is a JSON list with items of type LogAnalyticsParserField.  For documentation on LogAnalyticsParserField please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParserField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--footer-content', help=u"""footerRegex""")
@cli_util.option('--header-content', help=u"""headerContent""")
@cli_util.option('--name', help=u"""name""")
@cli_util.option('--is-default', type=click.BOOL, help=u"""isDefault""")
@cli_util.option('--is-single-line-content', type=click.BOOL, help=u"""isSingleLineContent""")
@cli_util.option('--is-system', type=click.BOOL, help=u"""isSystem""")
@cli_util.option('--language', help=u"""language""")
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""lastUpdatedDate""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--log-type-test-request-version', type=click.INT, help=u"""logTypeTestRequestVersion""")
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parser-ignoreline-characters', help=u"""parser ignore linechars""")
@cli_util.option('--is-hidden', type=click.INT, help=u"""parser is hidden""")
@cli_util.option('--parser-sequence', type=click.INT, help=u"""parser seq""")
@cli_util.option('--parser-timezone', help=u"""parser timezone""")
@cli_util.option('--is-parser-written-once', type=click.BOOL, help=u"""isParserWrittenOnce""")
@cli_util.option('--parser-functions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""plugin instance list

This option is a JSON list with items of type LogAnalyticsParserFunction.  For documentation on LogAnalyticsParserFunction please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParserFunction.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--should-tokenize-original-text', type=click.BOOL, help=u"""tokenize original text""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["XML", "JSON", "REGEX", "ODL"]), help=u"""type""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["LOG_LINES", "LOG_ENTRIES", "LOG_LINES_LOG_ENTRIES"]), help=u"""scope""")
@cli_util.option('--req-origin-module', help=u"""module""")
@json_skeleton_utils.get_cli_json_input_option({'field-maps': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserField]'}, 'metadata': {'module': 'log_analytics', 'class': 'UiParserTestMetadata'}, 'parser-functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserFunction]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'field-maps': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserField]'}, 'metadata': {'module': 'log_analytics', 'class': 'UiParserTestMetadata'}, 'parser-functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserFunction]'}}, output_type={'module': 'log_analytics', 'class': 'ParserTestResult'})
@cli_util.wrap_exceptions
def test_parser(ctx, from_json, namespace_name, content, description, display_name, encoding, example_content, field_maps, footer_content, header_content, name, is_default, is_single_line_content, is_system, language, time_updated, log_type_test_request_version, metadata, parser_ignoreline_characters, is_hidden, parser_sequence, parser_timezone, is_parser_written_once, parser_functions, should_tokenize_original_text, type, scope, req_origin_module):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if scope is not None:
        kwargs['scope'] = scope
    if req_origin_module is not None:
        kwargs['req_origin_module'] = req_origin_module
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if content is not None:
        _details['content'] = content

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if encoding is not None:
        _details['encoding'] = encoding

    if example_content is not None:
        _details['exampleContent'] = example_content

    if field_maps is not None:
        _details['fieldMaps'] = cli_util.parse_json_parameter("field_maps", field_maps)

    if footer_content is not None:
        _details['footerContent'] = footer_content

    if header_content is not None:
        _details['headerContent'] = header_content

    if name is not None:
        _details['name'] = name

    if is_default is not None:
        _details['isDefault'] = is_default

    if is_single_line_content is not None:
        _details['isSingleLineContent'] = is_single_line_content

    if is_system is not None:
        _details['isSystem'] = is_system

    if language is not None:
        _details['language'] = language

    if time_updated is not None:
        _details['timeUpdated'] = time_updated

    if log_type_test_request_version is not None:
        _details['logTypeTestRequestVersion'] = log_type_test_request_version

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if parser_ignoreline_characters is not None:
        _details['parserIgnorelineCharacters'] = parser_ignoreline_characters

    if is_hidden is not None:
        _details['isHidden'] = is_hidden

    if parser_sequence is not None:
        _details['parserSequence'] = parser_sequence

    if parser_timezone is not None:
        _details['parserTimezone'] = parser_timezone

    if is_parser_written_once is not None:
        _details['isParserWrittenOnce'] = is_parser_written_once

    if parser_functions is not None:
        _details['parserFunctions'] = cli_util.parse_json_parameter("parser_functions", parser_functions)

    if should_tokenize_original_text is not None:
        _details['shouldTokenizeOriginalText'] = should_tokenize_original_text

    if type is not None:
        _details['type'] = type

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.test_parser(
        namespace_name=namespace_name,
        test_parser_payload_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_entity_group.command(name=cli_util.override('log_analytics.update_log_analytics_entity.command_name', 'update'), help=u"""Update the log analytics entity with the given id. \n[Command Reference](updateLogAnalyticsEntity)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--log-analytics-entity-id', required=True, help=u"""The log analytics entity OCID.""")
@cli_util.option('--name', help=u"""Log analytics entity name. The name must be unique, within the tenancy, and cannot be changed.""")
@cli_util.option('--management-agent-id', help=u"""The OCID of the Management Agent.""")
@cli_util.option('--timezone-region', help=u"""The timezone region of the log analytics entity.""")
@cli_util.option('--hostname', help=u"""The hostname where the entity represented here is actually present. This would be the output one would get if they run `echo $HOSTNAME` on Linux or an equivalent OS command. This may be different from management agents host since logs may be collected remotely.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The name/value pairs for parameter values to be used in file patterns specified in log sources.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsEntity'})
@cli_util.wrap_exceptions
def update_log_analytics_entity(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, log_analytics_entity_id, name, management_agent_id, timezone_region, hostname, properties, freeform_tags, defined_tags, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(log_analytics_entity_id, six.string_types) and len(log_analytics_entity_id.strip()) == 0:
        raise click.UsageError('Parameter --log-analytics-entity-id cannot be whitespace or empty string')
    if not force:
        if properties or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to properties and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if name is not None:
        _details['name'] = name

    if management_agent_id is not None:
        _details['managementAgentId'] = management_agent_id

    if timezone_region is not None:
        _details['timezoneRegion'] = timezone_region

    if hostname is not None:
        _details['hostname'] = hostname

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.update_log_analytics_entity(
        namespace_name=namespace_name,
        log_analytics_entity_id=log_analytics_entity_id,
        update_log_analytics_entity_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_log_analytics_entity') and callable(getattr(client, 'get_log_analytics_entity')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_log_analytics_entity(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@log_analytics_entity_type_group.command(name=cli_util.override('log_analytics.update_log_analytics_entity_type.command_name', 'update'), help=u"""Update custom log analytics entity type. Out of box entity types cannot be udpated. \n[Command Reference](updateLogAnalyticsEntityType)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--entity-type-name', required=True, help=u"""Log analytics entity type name.""")
@cli_util.option('--category', help=u"""Log analytics entity type category. Category will be used for grouping and filtering.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A single log analytics entity type property definition.

This option is a JSON list with items of type EntityTypeProperty.  For documentation on EntityTypeProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/EntityTypeProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'log_analytics', 'class': 'list[EntityTypeProperty]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'log_analytics', 'class': 'list[EntityTypeProperty]'}})
@cli_util.wrap_exceptions
def update_log_analytics_entity_type(ctx, from_json, force, namespace_name, entity_type_name, category, properties, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(entity_type_name, six.string_types) and len(entity_type_name.strip()) == 0:
        raise click.UsageError('Parameter --entity-type-name cannot be whitespace or empty string')
    if not force:
        if properties:
            if not click.confirm("WARNING: Updates to properties will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if category is not None:
        _details['category'] = category

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.update_log_analytics_entity_type(
        namespace_name=namespace_name,
        entity_type_name=entity_type_name,
        update_log_analytics_entity_type_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_log_group_group.command(name=cli_util.override('log_analytics.update_log_analytics_log_group.command_name', 'update'), help=u"""Updates the Log-Analytics group with the given id. \n[Command Reference](updateLogAnalyticsLogGroup)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--log-analytics-log-group-id', required=True, help=u"""unique logAnalytics log group identifier""")
@cli_util.option('--display-name', help=u"""A user-friendly name that is changeable and that does not have to be unique. Format: a leading alphanumeric, followed by zero or more alphanumerics, underscores, spaces, backslashes, or hyphens in any order). No trailing spaces allowed.""")
@cli_util.option('--description', help=u"""Description for this resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsLogGroup'})
@cli_util.wrap_exceptions
def update_log_analytics_log_group(ctx, from_json, force, namespace_name, log_analytics_log_group_id, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(log_analytics_log_group_id, six.string_types) and len(log_analytics_log_group_id.strip()) == 0:
        raise click.UsageError('Parameter --log-analytics-log-group-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.update_log_analytics_log_group(
        namespace_name=namespace_name,
        log_analytics_log_group_id=log_analytics_log_group_id,
        update_log_analytics_log_group_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_object_collection_rule_group.command(name=cli_util.override('log_analytics.update_log_analytics_object_collection_rule.command_name', 'update'), help=u"""Update the rule with the given id. \n[Command Reference](updateLogAnalyticsObjectCollectionRule)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--log-analytics-object-collection-rule-id', required=True, help=u"""The Logging Analytics Object Collection Rule [OCID]""")
@cli_util.option('--description', help=u"""A string that describes the details of the rule. Avoid entering confidential information.""")
@cli_util.option('--log-group-id', help=u"""Logging Analytics Log group OCID to associate the processed logs with.""")
@cli_util.option('--log-source-name', help=u"""Name of the Logging Analytics Source to use for the processing.""")
@cli_util.option('--entity-id', help=u"""Logging Analytics entity OCID. Associates the processed logs with the given entity (optional).""")
@cli_util.option('--char-encoding', help=u"""An optional character encoding to aid in detecting the character encoding of the contents of the objects while processing. It is recommended to set this value as ISO_8589_1 when configuring content of the objects having more numeric characters, and very few alphabets. For e.g. this applies when configuring VCN Flow Logs.""")
@cli_util.option('--overrides', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Use this to override some property values which are defined at bucket level to the scope of object. Supported propeties for override are, logSourceName, charEncoding. Supported matchType for override are \"contains\".""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'overrides': {'module': 'log_analytics', 'class': 'dict(str, list[PropertyOverride])'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'overrides': {'module': 'log_analytics', 'class': 'dict(str, list[PropertyOverride])'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsObjectCollectionRule'})
@cli_util.wrap_exceptions
def update_log_analytics_object_collection_rule(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, log_analytics_object_collection_rule_id, description, log_group_id, log_source_name, entity_id, char_encoding, overrides, defined_tags, freeform_tags, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(log_analytics_object_collection_rule_id, six.string_types) and len(log_analytics_object_collection_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --log-analytics-object-collection-rule-id cannot be whitespace or empty string')
    if not force:
        if overrides or defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to overrides and defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if log_group_id is not None:
        _details['logGroupId'] = log_group_id

    if log_source_name is not None:
        _details['logSourceName'] = log_source_name

    if entity_id is not None:
        _details['entityId'] = entity_id

    if char_encoding is not None:
        _details['charEncoding'] = char_encoding

    if overrides is not None:
        _details['overrides'] = cli_util.parse_json_parameter("overrides", overrides)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.update_log_analytics_object_collection_rule(
        namespace_name=namespace_name,
        log_analytics_object_collection_rule_id=log_analytics_object_collection_rule_id,
        update_log_analytics_object_collection_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_log_analytics_object_collection_rule') and callable(getattr(client, 'get_log_analytics_object_collection_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_log_analytics_object_collection_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@scheduled_task_group.command(name=cli_util.override('log_analytics.update_scheduled_task.command_name', 'update'), help=u"""Update the scheduled task. Schedules may be updated only for taskType SAVED_SEARCH and PURGE. \n[Command Reference](updateScheduledTask)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--scheduled-task-id', required=True, help=u"""Unique scheduledTask id returned from task create. If invalid will lead to a 404 not found.""")
@cli_util.option('--display-name', help=u"""A user-friendly name that is changeable and that does not have to be unique. Format: a leading alphanumeric, followed by zero or more alphanumerics, underscores, spaces, backslashes, or hyphens in any order). No trailing spaces allowed.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schedules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Schedules may be updated for task types SAVED_SEARCH and PURGE

This option is a JSON list with items of type Schedule.  For documentation on Schedule please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/Schedule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}, 'schedules': {'module': 'log_analytics', 'class': 'list[Schedule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'log_analytics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'log_analytics', 'class': 'dict(str, dict(str, object))'}, 'schedules': {'module': 'log_analytics', 'class': 'list[Schedule]'}}, output_type={'module': 'log_analytics', 'class': 'ScheduledTask'})
@cli_util.wrap_exceptions
def update_scheduled_task(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, scheduled_task_id, display_name, freeform_tags, defined_tags, schedules, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(scheduled_task_id, six.string_types) and len(scheduled_task_id.strip()) == 0:
        raise click.UsageError('Parameter --scheduled-task-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or schedules:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and schedules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if schedules is not None:
        _details['schedules'] = cli_util.parse_json_parameter("schedules", schedules)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.update_scheduled_task(
        namespace_name=namespace_name,
        scheduled_task_id=scheduled_task_id,
        update_scheduled_task_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_scheduled_task') and callable(getattr(client, 'get_scheduled_task')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_scheduled_task(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@storage_group.command(name=cli_util.override('log_analytics.update_storage.command_name', 'update'), help=u"""This API updates the archiving configuration \n[Command Reference](updateStorage)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--archiving-configuration', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'archiving-configuration': {'module': 'log_analytics', 'class': 'ArchivingConfiguration'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'archiving-configuration': {'module': 'log_analytics', 'class': 'ArchivingConfiguration'}}, output_type={'module': 'log_analytics', 'class': 'Storage'})
@cli_util.wrap_exceptions
def update_storage(ctx, from_json, force, namespace_name, archiving_configuration, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')
    if not force:
        if archiving_configuration:
            if not click.confirm("WARNING: Updates to archiving-configuration will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['archivingConfiguration'] = cli_util.parse_json_parameter("archiving_configuration", archiving_configuration)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.update_storage(
        namespace_name=namespace_name,
        update_storage_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@upload_group.command(name=cli_util.override('log_analytics.upload_log_file.command_name', 'upload-log-file'), help=u"""Accepts log data for processing by Logging Analytics. \n[Command Reference](uploadLogFile)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--upload-name', required=True, help=u"""The name of the upload. This can be considered as a container name where different kind of logs will be collected and searched together. This upload name/id can further be used for retrieving the details of the upload, including its status or deleting the upload.""")
@cli_util.option('--log-source-name', required=True, help=u"""Name of the log source that will be used to process the files being uploaded.""")
@cli_util.option('--filename', required=True, help=u"""The name of the file being uploaded. The extension of the filename part will be used to detect the type of file (like zip, tar).""")
@cli_util.option('--opc-meta-loggrpid', required=True, help=u"""The log group OCID to which the log data in this upload will be mapped to.""")
@cli_util.option('--upload-log-file-body', required=True, help=u"""Log data""")
@cli_util.option('--entity-id', help=u"""The entity OCID.""")
@cli_util.option('--timezone', help=u"""Timezone to be used when processing log entries whose timestamps do not include an explicit timezone. When this property is not specified, the timezone of the entity specified is used. If the entity is also not specified or do not have a valid timezone then UTC is used""")
@cli_util.option('--char-encoding', help=u"""Character Encoding""")
@cli_util.option('--date-format', help=u"""This property is used to specify the format of the date. This is to be used for ambiguous dates like 12/11/10. This property can take any of the following values -  MONTH_DAY_YEAR, DAY_MONTH_YEAR, YEAR_MONTH_DAY, MONTH_DAY, DAY_MONTH.""")
@cli_util.option('--date-year', help=u"""Used to indicate the year where the log entries timestamp do not mention year (Ex: Nov  8 20:45:56).""")
@cli_util.option('--invalidate-cache', type=click.BOOL, help=u"""This property can be used to reset configuration cache in case of an issue with the upload.""")
@cli_util.option('--content-md5', help=u"""The base-64 encoded MD5 hash of the body. If the Content-MD5 header is present, Logging Analytics performs an integrity check on the body of the HTTP request by computing the MD5 hash for the body and comparing it to the MD5 hash supplied in the header. If the two hashes do not match, the log data is rejected and an HTTP-400 Unmatched Content MD5 error is returned with the message:

\"The computed MD5 of the request body (ACTUAL_MD5) does not match the Content-MD5 header (HEADER_MD5)\"""")
@cli_util.option('--content-type', help=u"""The content type of the log data.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'Upload'})
@cli_util.wrap_exceptions
def upload_log_file(ctx, from_json, namespace_name, upload_name, log_source_name, filename, opc_meta_loggrpid, upload_log_file_body, entity_id, timezone, char_encoding, date_format, date_year, invalidate_cache, content_md5, content_type):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if entity_id is not None:
        kwargs['entity_id'] = entity_id
    if timezone is not None:
        kwargs['timezone'] = timezone
    if char_encoding is not None:
        kwargs['char_encoding'] = char_encoding
    if date_format is not None:
        kwargs['date_format'] = date_format
    if date_year is not None:
        kwargs['date_year'] = date_year
    if invalidate_cache is not None:
        kwargs['invalidate_cache'] = invalidate_cache
    if content_md5 is not None:
        kwargs['content_md5'] = content_md5
    if content_type is not None:
        kwargs['content_type'] = content_type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    # do not automatically retry operations with binary inputs
    kwargs['retry_strategy'] = oci.retry.NoneRetryStrategy()

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.upload_log_file(
        namespace_name=namespace_name,
        upload_name=upload_name,
        log_source_name=log_source_name,
        filename=filename,
        opc_meta_loggrpid=opc_meta_loggrpid,
        upload_log_file_body=upload_log_file_body,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_association_group.command(name=cli_util.override('log_analytics.upsert_associations.command_name', 'upsert-associations'), help=u"""create or update associations for a source \n[Command Reference](upsertAssociations)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', help=u"""compartmentId""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""list of rule entity association details

This option is a JSON list with items of type UpsertLogAnalyticsAssociation.  For documentation on UpsertLogAnalyticsAssociation please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/UpsertLogAnalyticsAssociation.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-from-republish', type=click.BOOL, help=u"""isFromRepublish""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'log_analytics', 'class': 'list[UpsertLogAnalyticsAssociation]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'log_analytics', 'class': 'list[UpsertLogAnalyticsAssociation]'}})
@cli_util.wrap_exceptions
def upsert_associations(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, compartment_id, items, is_from_republish):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if is_from_republish is not None:
        kwargs['is_from_republish'] = is_from_republish
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.upsert_associations(
        namespace_name=namespace_name,
        upsert_log_analytics_association_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_config_work_request') and callable(getattr(client, 'get_config_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_config_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@log_analytics_field_group.command(name=cli_util.override('log_analytics.upsert_field.command_name', 'upsert-field'), help=u"""Defines or update a field. \n[Command Reference](upsertField)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--data-type', help=u"""data type""")
@cli_util.option('--is-multi-valued', type=click.BOOL, help=u"""is multi-valued flag""")
@cli_util.option('--description', help=u"""description""")
@cli_util.option('--display-name', help=u"""display name""")
@cli_util.option('--name', help=u"""internal name""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsField'})
@cli_util.wrap_exceptions
def upsert_field(ctx, from_json, namespace_name, data_type, is_multi_valued, description, display_name, name, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if data_type is not None:
        _details['dataType'] = data_type

    if is_multi_valued is not None:
        _details['isMultiValued'] = is_multi_valued

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if name is not None:
        _details['name'] = name

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.upsert_field(
        namespace_name=namespace_name,
        upsert_log_analytics_field_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_label_group.command(name=cli_util.override('log_analytics.upsert_label.command_name', 'upsert-label'), help=u"""Define or update a label. \n[Command Reference](upsertLabel)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--aliases', type=custom_types.CLI_COMPLEX_TYPE, help=u"""alias list

This option is a JSON list with items of type LogAnalyticsLabelAlias.  For documentation on LogAnalyticsLabelAlias please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsLabelAlias.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--suggest-type', type=click.INT, help=u"""suggest type""")
@cli_util.option('--description', help=u"""description""")
@cli_util.option('--display-name', help=u"""display name""")
@cli_util.option('--edit-version', type=click.INT, help=u"""edit version""")
@cli_util.option('--impact', help=u"""impact""")
@cli_util.option('--is-system', type=click.BOOL, help=u"""is system flag""")
@cli_util.option('--name', help=u"""label identifier""")
@cli_util.option('--priority', type=custom_types.CliCaseInsensitiveChoice(["NONE", "LOW", "MEDIUM", "HIGH"]), help=u"""Valid values are (NONE, LOW, HIGH). NONE is default.""")
@cli_util.option('--recommendation', help=u"""tag recommendation""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["INFO", "PROBLEM"]), help=u"""Valid values are (INFO, PROBLEM). INFO is default.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'aliases': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelAlias]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'aliases': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelAlias]'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsLabel'})
@cli_util.wrap_exceptions
def upsert_label(ctx, from_json, namespace_name, aliases, suggest_type, description, display_name, edit_version, impact, is_system, name, priority, recommendation, type, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if aliases is not None:
        _details['aliases'] = cli_util.parse_json_parameter("aliases", aliases)

    if suggest_type is not None:
        _details['suggestType'] = suggest_type

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if edit_version is not None:
        _details['editVersion'] = edit_version

    if impact is not None:
        _details['impact'] = impact

    if is_system is not None:
        _details['isSystem'] = is_system

    if name is not None:
        _details['name'] = name

    if priority is not None:
        _details['priority'] = priority

    if recommendation is not None:
        _details['recommendation'] = recommendation

    if type is not None:
        _details['type'] = type

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.upsert_label(
        namespace_name=namespace_name,
        upsert_log_analytics_label_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_parser_group.command(name=cli_util.override('log_analytics.upsert_parser.command_name', 'upsert-parser'), help=u"""Define or update parser \n[Command Reference](upsertParser)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--content', help=u"""content""")
@cli_util.option('--description', help=u"""description""")
@cli_util.option('--display-name', help=u"""display name""")
@cli_util.option('--edit-version', type=click.INT, help=u"""edit version""")
@cli_util.option('--encoding', help=u"""encoding""")
@cli_util.option('--example-content', help=u"""example content""")
@cli_util.option('--field-maps', type=custom_types.CLI_COMPLEX_TYPE, help=u"""fields Maps

This option is a JSON list with items of type LogAnalyticsParserField.  For documentation on LogAnalyticsParserField please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParserField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--footer-content', help=u"""footer regular expression""")
@cli_util.option('--header-content', help=u"""header content""")
@cli_util.option('--name', help=u"""Name""")
@cli_util.option('--is-default', type=click.BOOL, help=u"""is default flag""")
@cli_util.option('--is-single-line-content', type=click.BOOL, help=u"""is single line content""")
@cli_util.option('--is-system', type=click.BOOL, help=u"""is system flag""")
@cli_util.option('--language', help=u"""language""")
@cli_util.option('--log-type-test-request-version', type=click.INT, help=u"""log type test request version""")
@cli_util.option('--parser-ignoreline-characters', help=u"""parser ignore line characters""")
@cli_util.option('--parser-sequence', type=click.INT, help=u"""sequence""")
@cli_util.option('--parser-timezone', help=u"""time zone""")
@cli_util.option('--is-parser-written-once', type=click.BOOL, help=u"""write once""")
@cli_util.option('--parser-functions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""plugin instance list

This option is a JSON list with items of type LogAnalyticsParserFunction.  For documentation on LogAnalyticsParserFunction please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParserFunction.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--should-tokenize-original-text', type=click.BOOL, help=u"""tokenize original text""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["XML", "JSON", "REGEX", "ODL"]), help=u"""type""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'field-maps': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserField]'}, 'parser-functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserFunction]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'field-maps': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserField]'}, 'parser-functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParserFunction]'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsParser'})
@cli_util.wrap_exceptions
def upsert_parser(ctx, from_json, namespace_name, content, description, display_name, edit_version, encoding, example_content, field_maps, footer_content, header_content, name, is_default, is_single_line_content, is_system, language, log_type_test_request_version, parser_ignoreline_characters, parser_sequence, parser_timezone, is_parser_written_once, parser_functions, should_tokenize_original_text, type, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if content is not None:
        _details['content'] = content

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if edit_version is not None:
        _details['editVersion'] = edit_version

    if encoding is not None:
        _details['encoding'] = encoding

    if example_content is not None:
        _details['exampleContent'] = example_content

    if field_maps is not None:
        _details['fieldMaps'] = cli_util.parse_json_parameter("field_maps", field_maps)

    if footer_content is not None:
        _details['footerContent'] = footer_content

    if header_content is not None:
        _details['headerContent'] = header_content

    if name is not None:
        _details['name'] = name

    if is_default is not None:
        _details['isDefault'] = is_default

    if is_single_line_content is not None:
        _details['isSingleLineContent'] = is_single_line_content

    if is_system is not None:
        _details['isSystem'] = is_system

    if language is not None:
        _details['language'] = language

    if log_type_test_request_version is not None:
        _details['logTypeTestRequestVersion'] = log_type_test_request_version

    if parser_ignoreline_characters is not None:
        _details['parserIgnorelineCharacters'] = parser_ignoreline_characters

    if parser_sequence is not None:
        _details['parserSequence'] = parser_sequence

    if parser_timezone is not None:
        _details['parserTimezone'] = parser_timezone

    if is_parser_written_once is not None:
        _details['isParserWrittenOnce'] = is_parser_written_once

    if parser_functions is not None:
        _details['parserFunctions'] = cli_util.parse_json_parameter("parser_functions", parser_functions)

    if should_tokenize_original_text is not None:
        _details['shouldTokenizeOriginalText'] = should_tokenize_original_text

    if type is not None:
        _details['type'] = type

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.upsert_parser(
        namespace_name=namespace_name,
        upsert_log_analytics_parser_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_source_group.command(name=cli_util.override('log_analytics.upsert_source.command_name', 'upsert-source'), help=u"""Define or update a source \n[Command Reference](upsertSource)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--label-conditions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""source label conditions

This option is a JSON list with items of type LogAnalyticsSourceLabelCondition.  For documentation on LogAnalyticsSourceLabelCondition please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceLabelCondition.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-filter-definitions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""data filter definitions

This option is a JSON list with items of type LogAnalyticsSourceDataFilter.  For documentation on LogAnalyticsSourceDataFilter please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceDataFilter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-credential', help=u"""DB credential name""")
@cli_util.option('--extended-field-definitions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""extended field definition

This option is a JSON list with items of type LogAnalyticsSourceExtendedFieldDefinition.  For documentation on LogAnalyticsSourceExtendedFieldDefinition please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceExtendedFieldDefinition.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-for-cloud', type=click.BOOL, help=u"""is for cloud flag""")
@cli_util.option('--labels', type=custom_types.CLI_COMPLEX_TYPE, help=u"""labels

This option is a JSON list with items of type LogAnalyticsLabelView.  For documentation on LogAnalyticsLabelView please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsLabelView.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metric-definitions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""metric definitions

This option is a JSON list with items of type LogAnalyticsMetric.  For documentation on LogAnalyticsMetric please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsMetric.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metrics', type=custom_types.CLI_COMPLEX_TYPE, help=u"""metric source map

This option is a JSON list with items of type LogAnalyticsSourceMetric.  For documentation on LogAnalyticsSourceMetric please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceMetric.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oob-parsers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""out-of-the-box source parser list

This option is a JSON list with items of type LogAnalyticsParser.  For documentation on LogAnalyticsParser please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParser.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""parameters

This option is a JSON list with items of type LogAnalyticsParameter.  For documentation on LogAnalyticsParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--patterns', type=custom_types.CLI_COMPLEX_TYPE, help=u"""patterns

This option is a JSON list with items of type LogAnalyticsSourcePattern.  For documentation on LogAnalyticsSourcePattern please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourcePattern.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""description""")
@cli_util.option('--display-name', help=u"""display name""")
@cli_util.option('--edit-version', type=click.INT, help=u"""source edit version""")
@cli_util.option('--functions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""source functions

This option is a JSON list with items of type LogAnalyticsSourceFunction.  For documentation on LogAnalyticsSourceFunction please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceFunction.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--source-id', type=click.INT, help=u"""source Id""")
@cli_util.option('--name', help=u"""source internal name""")
@cli_util.option('--is-secure-content', type=click.BOOL, help=u"""is secure content flag""")
@cli_util.option('--is-system', type=click.BOOL, help=u"""is system flag""")
@cli_util.option('--parsers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""parser list

This option is a JSON list with items of type LogAnalyticsParser.  For documentation on LogAnalyticsParser please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParser.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rule-id', type=click.INT, help=u"""rule Id""")
@cli_util.option('--type-name', help=u"""source type internal name""")
@cli_util.option('--warning-config', type=click.INT, help=u"""source warning configuration""")
@cli_util.option('--metadata-fields', type=custom_types.CLI_COMPLEX_TYPE, help=u"""source metadata fields

This option is a JSON list with items of type LogAnalyticsSourceMetadataField.  For documentation on LogAnalyticsSourceMetadataField please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceMetadataField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--label-definitions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""tags

This option is a JSON list with items of type LogAnalyticsLabelDefinition.  For documentation on LogAnalyticsLabelDefinition please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsLabelDefinition.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--entity-types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""entity types

This option is a JSON list with items of type LogAnalyticsSourceEntityType.  For documentation on LogAnalyticsSourceEntityType please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceEntityType.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-timezone-override', type=click.BOOL, help=u"""time zone override""")
@cli_util.option('--user-parsers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""source parser list

This option is a JSON list with items of type LogAnalyticsParser.  For documentation on LogAnalyticsParser please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParser.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--create-like-source-id', type=click.INT, help=u"""create like sourceId""")
@cli_util.option('--is-incremental', type=click.BOOL, help=u"""is incremental""")
@cli_util.option('--is-ignore-warning', type=click.BOOL, help=u"""is ignore warning""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'label-conditions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceLabelCondition]'}, 'data-filter-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceDataFilter]'}, 'extended-field-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceExtendedFieldDefinition]'}, 'labels': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelView]'}, 'metric-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsMetric]'}, 'metrics': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetric]'}, 'oob-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'parameters': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParameter]'}, 'patterns': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourcePattern]'}, 'functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceFunction]'}, 'parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'metadata-fields': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetadataField]'}, 'label-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelDefinition]'}, 'entity-types': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceEntityType]'}, 'user-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'label-conditions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceLabelCondition]'}, 'data-filter-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceDataFilter]'}, 'extended-field-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceExtendedFieldDefinition]'}, 'labels': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelView]'}, 'metric-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsMetric]'}, 'metrics': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetric]'}, 'oob-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'parameters': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParameter]'}, 'patterns': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourcePattern]'}, 'functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceFunction]'}, 'parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'metadata-fields': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetadataField]'}, 'label-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelDefinition]'}, 'entity-types': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceEntityType]'}, 'user-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsSource'})
@cli_util.wrap_exceptions
def upsert_source(ctx, from_json, namespace_name, label_conditions, data_filter_definitions, database_credential, extended_field_definitions, is_for_cloud, labels, metric_definitions, metrics, oob_parsers, parameters, patterns, description, display_name, edit_version, functions, source_id, name, is_secure_content, is_system, parsers, rule_id, type_name, warning_config, metadata_fields, label_definitions, entity_types, is_timezone_override, user_parsers, create_like_source_id, is_incremental, is_ignore_warning, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if create_like_source_id is not None:
        kwargs['create_like_source_id'] = create_like_source_id
    if is_incremental is not None:
        kwargs['is_incremental'] = is_incremental
    if is_ignore_warning is not None:
        kwargs['is_ignore_warning'] = is_ignore_warning
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if label_conditions is not None:
        _details['labelConditions'] = cli_util.parse_json_parameter("label_conditions", label_conditions)

    if data_filter_definitions is not None:
        _details['dataFilterDefinitions'] = cli_util.parse_json_parameter("data_filter_definitions", data_filter_definitions)

    if database_credential is not None:
        _details['databaseCredential'] = database_credential

    if extended_field_definitions is not None:
        _details['extendedFieldDefinitions'] = cli_util.parse_json_parameter("extended_field_definitions", extended_field_definitions)

    if is_for_cloud is not None:
        _details['isForCloud'] = is_for_cloud

    if labels is not None:
        _details['labels'] = cli_util.parse_json_parameter("labels", labels)

    if metric_definitions is not None:
        _details['metricDefinitions'] = cli_util.parse_json_parameter("metric_definitions", metric_definitions)

    if metrics is not None:
        _details['metrics'] = cli_util.parse_json_parameter("metrics", metrics)

    if oob_parsers is not None:
        _details['oobParsers'] = cli_util.parse_json_parameter("oob_parsers", oob_parsers)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if patterns is not None:
        _details['patterns'] = cli_util.parse_json_parameter("patterns", patterns)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if edit_version is not None:
        _details['editVersion'] = edit_version

    if functions is not None:
        _details['functions'] = cli_util.parse_json_parameter("functions", functions)

    if source_id is not None:
        _details['sourceId'] = source_id

    if name is not None:
        _details['name'] = name

    if is_secure_content is not None:
        _details['isSecureContent'] = is_secure_content

    if is_system is not None:
        _details['isSystem'] = is_system

    if parsers is not None:
        _details['parsers'] = cli_util.parse_json_parameter("parsers", parsers)

    if rule_id is not None:
        _details['ruleId'] = rule_id

    if type_name is not None:
        _details['typeName'] = type_name

    if warning_config is not None:
        _details['warningConfig'] = warning_config

    if metadata_fields is not None:
        _details['metadataFields'] = cli_util.parse_json_parameter("metadata_fields", metadata_fields)

    if label_definitions is not None:
        _details['labelDefinitions'] = cli_util.parse_json_parameter("label_definitions", label_definitions)

    if entity_types is not None:
        _details['entityTypes'] = cli_util.parse_json_parameter("entity_types", entity_types)

    if is_timezone_override is not None:
        _details['isTimezoneOverride'] = is_timezone_override

    if user_parsers is not None:
        _details['userParsers'] = cli_util.parse_json_parameter("user_parsers", user_parsers)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.upsert_source(
        namespace_name=namespace_name,
        upsert_log_analytics_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_association_group.command(name=cli_util.override('log_analytics.validate_association_parameters.command_name', 'validate-association-parameters'), help=u"""association parameter validation \n[Command Reference](validateAssociationParameters)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--compartment-id', help=u"""compartmentId""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""list of rule entity association details

This option is a JSON list with items of type UpsertLogAnalyticsAssociation.  For documentation on UpsertLogAnalyticsAssociation please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/UpsertLogAnalyticsAssociation.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["sourceDisplayName", "status"]), help=u"""sort by field""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'log_analytics', 'class': 'list[UpsertLogAnalyticsAssociation]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'log_analytics', 'class': 'list[UpsertLogAnalyticsAssociation]'}}, output_type={'module': 'log_analytics', 'class': 'LogAnalyticsAssociationParameterCollection'})
@cli_util.wrap_exceptions
def validate_association_parameters(ctx, from_json, namespace_name, compartment_id, items, limit, page, sort_order, sort_by):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.validate_association_parameters(
        namespace_name=namespace_name,
        upsert_log_analytics_association_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@upload_group.command(name=cli_util.override('log_analytics.validate_file.command_name', 'validate-file'), help=u"""Validates a log file to check whether it is eligible to upload or not. \n[Command Reference](validateFile)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--object-location', required=True, help=u"""Location of the log file""")
@cli_util.option('--filename', required=True, help=u"""The name of the file being uploaded. The extension of the filename part will be used to detect the type of file (like zip, tar).""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'FileValidationResponse'})
@cli_util.wrap_exceptions
def validate_file(ctx, from_json, namespace_name, object_location, filename):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.validate_file(
        namespace_name=namespace_name,
        object_location=object_location,
        filename=filename,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_source_group.command(name=cli_util.override('log_analytics.validate_source.command_name', 'validate-source'), help=u"""Pre-define or update a source \n[Command Reference](validateSource)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--label-conditions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""source label conditions

This option is a JSON list with items of type LogAnalyticsSourceLabelCondition.  For documentation on LogAnalyticsSourceLabelCondition please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceLabelCondition.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-filter-definitions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""data filter definitions

This option is a JSON list with items of type LogAnalyticsSourceDataFilter.  For documentation on LogAnalyticsSourceDataFilter please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceDataFilter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-credential', help=u"""DB credential name""")
@cli_util.option('--extended-field-definitions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""extended field definition

This option is a JSON list with items of type LogAnalyticsSourceExtendedFieldDefinition.  For documentation on LogAnalyticsSourceExtendedFieldDefinition please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceExtendedFieldDefinition.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-for-cloud', type=click.BOOL, help=u"""is for cloud flag""")
@cli_util.option('--labels', type=custom_types.CLI_COMPLEX_TYPE, help=u"""labels

This option is a JSON list with items of type LogAnalyticsLabelView.  For documentation on LogAnalyticsLabelView please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsLabelView.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metric-definitions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""metric definitions

This option is a JSON list with items of type LogAnalyticsMetric.  For documentation on LogAnalyticsMetric please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsMetric.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metrics', type=custom_types.CLI_COMPLEX_TYPE, help=u"""metric source map

This option is a JSON list with items of type LogAnalyticsSourceMetric.  For documentation on LogAnalyticsSourceMetric please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceMetric.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oob-parsers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""out-of-the-box source parser list

This option is a JSON list with items of type LogAnalyticsParser.  For documentation on LogAnalyticsParser please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParser.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""parameters

This option is a JSON list with items of type LogAnalyticsParameter.  For documentation on LogAnalyticsParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--patterns', type=custom_types.CLI_COMPLEX_TYPE, help=u"""patterns

This option is a JSON list with items of type LogAnalyticsSourcePattern.  For documentation on LogAnalyticsSourcePattern please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourcePattern.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""description""")
@cli_util.option('--display-name', help=u"""display name""")
@cli_util.option('--edit-version', type=click.INT, help=u"""source edit version""")
@cli_util.option('--functions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""source functions

This option is a JSON list with items of type LogAnalyticsSourceFunction.  For documentation on LogAnalyticsSourceFunction please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceFunction.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--source-id', type=click.INT, help=u"""source Id""")
@cli_util.option('--name', help=u"""source internal name""")
@cli_util.option('--is-secure-content', type=click.BOOL, help=u"""is secure content flag""")
@cli_util.option('--is-system', type=click.BOOL, help=u"""is system flag""")
@cli_util.option('--parsers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""parser list

This option is a JSON list with items of type LogAnalyticsParser.  For documentation on LogAnalyticsParser please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParser.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rule-id', type=click.INT, help=u"""rule Id""")
@cli_util.option('--type-name', help=u"""source type internal name""")
@cli_util.option('--warning-config', type=click.INT, help=u"""source warning configuration""")
@cli_util.option('--metadata-fields', type=custom_types.CLI_COMPLEX_TYPE, help=u"""source metadata fields

This option is a JSON list with items of type LogAnalyticsSourceMetadataField.  For documentation on LogAnalyticsSourceMetadataField please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceMetadataField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--label-definitions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""tags

This option is a JSON list with items of type LogAnalyticsLabelDefinition.  For documentation on LogAnalyticsLabelDefinition please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsLabelDefinition.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--entity-types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""entity types

This option is a JSON list with items of type LogAnalyticsSourceEntityType.  For documentation on LogAnalyticsSourceEntityType please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceEntityType.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-timezone-override', type=click.BOOL, help=u"""time zone override""")
@cli_util.option('--user-parsers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""source parser list

This option is a JSON list with items of type LogAnalyticsParser.  For documentation on LogAnalyticsParser please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParser.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--create-like-source-id', type=click.INT, help=u"""create like sourceId""")
@cli_util.option('--is-incremental', type=click.BOOL, help=u"""is incremental""")
@cli_util.option('--is-ignore-warning', type=click.BOOL, help=u"""is ignore warning""")
@json_skeleton_utils.get_cli_json_input_option({'label-conditions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceLabelCondition]'}, 'data-filter-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceDataFilter]'}, 'extended-field-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceExtendedFieldDefinition]'}, 'labels': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelView]'}, 'metric-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsMetric]'}, 'metrics': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetric]'}, 'oob-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'parameters': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParameter]'}, 'patterns': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourcePattern]'}, 'functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceFunction]'}, 'parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'metadata-fields': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetadataField]'}, 'label-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelDefinition]'}, 'entity-types': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceEntityType]'}, 'user-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'label-conditions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceLabelCondition]'}, 'data-filter-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceDataFilter]'}, 'extended-field-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceExtendedFieldDefinition]'}, 'labels': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelView]'}, 'metric-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsMetric]'}, 'metrics': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetric]'}, 'oob-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'parameters': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParameter]'}, 'patterns': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourcePattern]'}, 'functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceFunction]'}, 'parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'metadata-fields': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetadataField]'}, 'label-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelDefinition]'}, 'entity-types': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceEntityType]'}, 'user-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}}, output_type={'module': 'log_analytics', 'class': 'SourceValidateResults'})
@cli_util.wrap_exceptions
def validate_source(ctx, from_json, namespace_name, label_conditions, data_filter_definitions, database_credential, extended_field_definitions, is_for_cloud, labels, metric_definitions, metrics, oob_parsers, parameters, patterns, description, display_name, edit_version, functions, source_id, name, is_secure_content, is_system, parsers, rule_id, type_name, warning_config, metadata_fields, label_definitions, entity_types, is_timezone_override, user_parsers, create_like_source_id, is_incremental, is_ignore_warning):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if create_like_source_id is not None:
        kwargs['create_like_source_id'] = create_like_source_id
    if is_incremental is not None:
        kwargs['is_incremental'] = is_incremental
    if is_ignore_warning is not None:
        kwargs['is_ignore_warning'] = is_ignore_warning
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if label_conditions is not None:
        _details['labelConditions'] = cli_util.parse_json_parameter("label_conditions", label_conditions)

    if data_filter_definitions is not None:
        _details['dataFilterDefinitions'] = cli_util.parse_json_parameter("data_filter_definitions", data_filter_definitions)

    if database_credential is not None:
        _details['databaseCredential'] = database_credential

    if extended_field_definitions is not None:
        _details['extendedFieldDefinitions'] = cli_util.parse_json_parameter("extended_field_definitions", extended_field_definitions)

    if is_for_cloud is not None:
        _details['isForCloud'] = is_for_cloud

    if labels is not None:
        _details['labels'] = cli_util.parse_json_parameter("labels", labels)

    if metric_definitions is not None:
        _details['metricDefinitions'] = cli_util.parse_json_parameter("metric_definitions", metric_definitions)

    if metrics is not None:
        _details['metrics'] = cli_util.parse_json_parameter("metrics", metrics)

    if oob_parsers is not None:
        _details['oobParsers'] = cli_util.parse_json_parameter("oob_parsers", oob_parsers)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if patterns is not None:
        _details['patterns'] = cli_util.parse_json_parameter("patterns", patterns)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if edit_version is not None:
        _details['editVersion'] = edit_version

    if functions is not None:
        _details['functions'] = cli_util.parse_json_parameter("functions", functions)

    if source_id is not None:
        _details['sourceId'] = source_id

    if name is not None:
        _details['name'] = name

    if is_secure_content is not None:
        _details['isSecureContent'] = is_secure_content

    if is_system is not None:
        _details['isSystem'] = is_system

    if parsers is not None:
        _details['parsers'] = cli_util.parse_json_parameter("parsers", parsers)

    if rule_id is not None:
        _details['ruleId'] = rule_id

    if type_name is not None:
        _details['typeName'] = type_name

    if warning_config is not None:
        _details['warningConfig'] = warning_config

    if metadata_fields is not None:
        _details['metadataFields'] = cli_util.parse_json_parameter("metadata_fields", metadata_fields)

    if label_definitions is not None:
        _details['labelDefinitions'] = cli_util.parse_json_parameter("label_definitions", label_definitions)

    if entity_types is not None:
        _details['entityTypes'] = cli_util.parse_json_parameter("entity_types", entity_types)

    if is_timezone_override is not None:
        _details['isTimezoneOverride'] = is_timezone_override

    if user_parsers is not None:
        _details['userParsers'] = cli_util.parse_json_parameter("user_parsers", user_parsers)

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.validate_source(
        namespace_name=namespace_name,
        upsert_log_analytics_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_analytics_source_group.command(name=cli_util.override('log_analytics.validate_source_extended_field_details.command_name', 'validate-source-extended-field-details'), help=u"""test extended fields \n[Command Reference](validateSourceExtendedFieldDetails)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--label-conditions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""alert conditions

This option is a JSON list with items of type LogAnalyticsSourceLabelCondition.  For documentation on LogAnalyticsSourceLabelCondition please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceLabelCondition.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--association-count', type=click.INT, help=u"""association count""")
@cli_util.option('--association-entity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""association entity

This option is a JSON list with items of type LogAnalyticsAssociation.  For documentation on LogAnalyticsAssociation please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsAssociation.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-filter-definitions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""data filter definitions

This option is a JSON list with items of type LogAnalyticsSourceDataFilter.  For documentation on LogAnalyticsSourceDataFilter please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceDataFilter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-credential', help=u"""DB credential""")
@cli_util.option('--extended-field-definitions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""extended field definition

This option is a JSON list with items of type LogAnalyticsSourceExtendedFieldDefinition.  For documentation on LogAnalyticsSourceExtendedFieldDefinition please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceExtendedFieldDefinition.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-for-cloud', type=click.BOOL, help=u"""is for cloud flag""")
@cli_util.option('--labels', type=custom_types.CLI_COMPLEX_TYPE, help=u"""labels

This option is a JSON list with items of type LogAnalyticsLabelView.  For documentation on LogAnalyticsLabelView please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsLabelView.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metric-definitions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""metric definitions

This option is a JSON list with items of type LogAnalyticsMetric.  For documentation on LogAnalyticsMetric please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsMetric.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metrics', type=custom_types.CLI_COMPLEX_TYPE, help=u"""metric source map

This option is a JSON list with items of type LogAnalyticsSourceMetric.  For documentation on LogAnalyticsSourceMetric please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceMetric.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oob-parsers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""out-of-the-box source parser list

This option is a JSON list with items of type LogAnalyticsParser.  For documentation on LogAnalyticsParser please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParser.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""parameters

This option is a JSON list with items of type LogAnalyticsParameter.  For documentation on LogAnalyticsParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--pattern-count', type=click.INT, help=u"""pattern count""")
@cli_util.option('--patterns', type=custom_types.CLI_COMPLEX_TYPE, help=u"""patterns

This option is a JSON list with items of type LogAnalyticsSourcePattern.  For documentation on LogAnalyticsSourcePattern please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourcePattern.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""description""")
@cli_util.option('--display-name', help=u"""display name""")
@cli_util.option('--edit-version', type=click.INT, help=u"""source edit version""")
@cli_util.option('--functions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""source functions

This option is a JSON list with items of type LogAnalyticsSourceFunction.  For documentation on LogAnalyticsSourceFunction please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceFunction.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--source-id', type=click.INT, help=u"""source Id""")
@cli_util.option('--name', help=u"""source internal name""")
@cli_util.option('--is-secure-content', type=click.BOOL, help=u"""is secure content flag""")
@cli_util.option('--is-system', type=click.BOOL, help=u"""is system flag""")
@cli_util.option('--parsers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""parser list

This option is a JSON list with items of type LogAnalyticsParser.  For documentation on LogAnalyticsParser please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParser.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-auto-association-enabled', type=click.BOOL, help=u"""rule auto association enabled flag""")
@cli_util.option('--is-auto-association-override', type=click.BOOL, help=u"""rule auto association override""")
@cli_util.option('--rule-id', type=click.INT, help=u"""rule Id""")
@cli_util.option('--type-name', help=u"""source type internal name""")
@cli_util.option('--type-display-name', help=u"""source type name""")
@cli_util.option('--warning-config', type=click.INT, help=u"""source warning configuration""")
@cli_util.option('--metadata-fields', type=custom_types.CLI_COMPLEX_TYPE, help=u"""source metadata fields

This option is a JSON list with items of type LogAnalyticsSourceMetadataField.  For documentation on LogAnalyticsSourceMetadataField please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceMetadataField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--label-definitions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""tags

This option is a JSON list with items of type LogAnalyticsLabelDefinition.  For documentation on LogAnalyticsLabelDefinition please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsLabelDefinition.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--entity-types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Entity types

This option is a JSON list with items of type LogAnalyticsSourceEntityType.  For documentation on LogAnalyticsSourceEntityType please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsSourceEntityType.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-timezone-override', type=click.BOOL, help=u"""time zone override""")
@cli_util.option('--user-parsers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""source parser list

This option is a JSON list with items of type LogAnalyticsParser.  For documentation on LogAnalyticsParser please see our API reference: https://docs.cloud.oracle.com/api/#/en/loganalytics/20200601/datatypes/LogAnalyticsParser.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""timeUpdated""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@json_skeleton_utils.get_cli_json_input_option({'label-conditions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceLabelCondition]'}, 'association-entity': {'module': 'log_analytics', 'class': 'list[LogAnalyticsAssociation]'}, 'data-filter-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceDataFilter]'}, 'extended-field-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceExtendedFieldDefinition]'}, 'labels': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelView]'}, 'metric-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsMetric]'}, 'metrics': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetric]'}, 'oob-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'parameters': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParameter]'}, 'patterns': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourcePattern]'}, 'functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceFunction]'}, 'parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'metadata-fields': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetadataField]'}, 'label-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelDefinition]'}, 'entity-types': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceEntityType]'}, 'user-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'label-conditions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceLabelCondition]'}, 'association-entity': {'module': 'log_analytics', 'class': 'list[LogAnalyticsAssociation]'}, 'data-filter-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceDataFilter]'}, 'extended-field-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceExtendedFieldDefinition]'}, 'labels': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelView]'}, 'metric-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsMetric]'}, 'metrics': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetric]'}, 'oob-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'parameters': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParameter]'}, 'patterns': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourcePattern]'}, 'functions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceFunction]'}, 'parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}, 'metadata-fields': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceMetadataField]'}, 'label-definitions': {'module': 'log_analytics', 'class': 'list[LogAnalyticsLabelDefinition]'}, 'entity-types': {'module': 'log_analytics', 'class': 'list[LogAnalyticsSourceEntityType]'}, 'user-parsers': {'module': 'log_analytics', 'class': 'list[LogAnalyticsParser]'}}, output_type={'module': 'log_analytics', 'class': 'ExtendedFieldsValidationResult'})
@cli_util.wrap_exceptions
def validate_source_extended_field_details(ctx, from_json, namespace_name, label_conditions, association_count, association_entity, data_filter_definitions, database_credential, extended_field_definitions, is_for_cloud, labels, metric_definitions, metrics, oob_parsers, parameters, pattern_count, patterns, description, display_name, edit_version, functions, source_id, name, is_secure_content, is_system, parsers, is_auto_association_enabled, is_auto_association_override, rule_id, type_name, type_display_name, warning_config, metadata_fields, label_definitions, entity_types, is_timezone_override, user_parsers, time_updated):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if label_conditions is not None:
        _details['labelConditions'] = cli_util.parse_json_parameter("label_conditions", label_conditions)

    if association_count is not None:
        _details['associationCount'] = association_count

    if association_entity is not None:
        _details['associationEntity'] = cli_util.parse_json_parameter("association_entity", association_entity)

    if data_filter_definitions is not None:
        _details['dataFilterDefinitions'] = cli_util.parse_json_parameter("data_filter_definitions", data_filter_definitions)

    if database_credential is not None:
        _details['databaseCredential'] = database_credential

    if extended_field_definitions is not None:
        _details['extendedFieldDefinitions'] = cli_util.parse_json_parameter("extended_field_definitions", extended_field_definitions)

    if is_for_cloud is not None:
        _details['isForCloud'] = is_for_cloud

    if labels is not None:
        _details['labels'] = cli_util.parse_json_parameter("labels", labels)

    if metric_definitions is not None:
        _details['metricDefinitions'] = cli_util.parse_json_parameter("metric_definitions", metric_definitions)

    if metrics is not None:
        _details['metrics'] = cli_util.parse_json_parameter("metrics", metrics)

    if oob_parsers is not None:
        _details['oobParsers'] = cli_util.parse_json_parameter("oob_parsers", oob_parsers)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if pattern_count is not None:
        _details['patternCount'] = pattern_count

    if patterns is not None:
        _details['patterns'] = cli_util.parse_json_parameter("patterns", patterns)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if edit_version is not None:
        _details['editVersion'] = edit_version

    if functions is not None:
        _details['functions'] = cli_util.parse_json_parameter("functions", functions)

    if source_id is not None:
        _details['sourceId'] = source_id

    if name is not None:
        _details['name'] = name

    if is_secure_content is not None:
        _details['isSecureContent'] = is_secure_content

    if is_system is not None:
        _details['isSystem'] = is_system

    if parsers is not None:
        _details['parsers'] = cli_util.parse_json_parameter("parsers", parsers)

    if is_auto_association_enabled is not None:
        _details['isAutoAssociationEnabled'] = is_auto_association_enabled

    if is_auto_association_override is not None:
        _details['isAutoAssociationOverride'] = is_auto_association_override

    if rule_id is not None:
        _details['ruleId'] = rule_id

    if type_name is not None:
        _details['typeName'] = type_name

    if type_display_name is not None:
        _details['typeDisplayName'] = type_display_name

    if warning_config is not None:
        _details['warningConfig'] = warning_config

    if metadata_fields is not None:
        _details['metadataFields'] = cli_util.parse_json_parameter("metadata_fields", metadata_fields)

    if label_definitions is not None:
        _details['labelDefinitions'] = cli_util.parse_json_parameter("label_definitions", label_definitions)

    if entity_types is not None:
        _details['entityTypes'] = cli_util.parse_json_parameter("entity_types", entity_types)

    if is_timezone_override is not None:
        _details['isTimezoneOverride'] = is_timezone_override

    if user_parsers is not None:
        _details['userParsers'] = cli_util.parse_json_parameter("user_parsers", user_parsers)

    if time_updated is not None:
        _details['timeUpdated'] = time_updated

    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.validate_source_extended_field_details(
        namespace_name=namespace_name,
        log_analytics_source=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@upload_group.command(name=cli_util.override('log_analytics.validate_source_mapping.command_name', 'validate-source-mapping'), help=u"""Validates the source mapping for given file and provides match status and parsed representation of log data. \n[Command Reference](validateSourceMapping)""")
@cli_util.option('--namespace-name', required=True, help=u"""The Logging Analytics namespace used for the request.""")
@cli_util.option('--object-location', required=True, help=u"""Location of the log file""")
@cli_util.option('--filename', required=True, help=u"""The name of the file being uploaded. The extension of the filename part will be used to detect the type of file (like zip, tar).""")
@cli_util.option('--log-source-name', required=True, help=u"""Name of the log source that will be used to process the files being uploaded.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'log_analytics', 'class': 'SourceMappingResponse'})
@cli_util.wrap_exceptions
def validate_source_mapping(ctx, from_json, namespace_name, object_location, filename, log_source_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('log_analytics', 'log_analytics', ctx)
    result = client.validate_source_mapping(
        namespace_name=namespace_name,
        object_location=object_location,
        filename=filename,
        log_source_name=log_source_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)
