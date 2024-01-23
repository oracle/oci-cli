# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.stack_monitoring.src.oci_cli_stack_monitoring.generated import stackmonitoring_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci stack-monitoring work-request-error-collection list-work-request-errors -> oci stack-monitoring work-request-error-collection list-errors
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.work_request_error_collection_group, stackmonitoring_cli.list_work_request_errors, "list-errors")


# oci stack-monitoring work-request-log-entry-collection list-work-request-logs -> oci stack-monitoring work-request-log-entry-collection list-logs
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.work_request_log_entry_collection_group, stackmonitoring_cli.list_work_request_logs, "list-logs")


# oci stack-monitoring work-request-summary-collection list-work-requests -> oci stack-monitoring work-request-summary-collection list
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.work_request_summary_collection_group, stackmonitoring_cli.list_work_requests, "list")


# oci stack-monitoring discovery-job-collection list-discovery-jobs -> oci stack-monitoring discovery-job-collection list
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.discovery_job_collection_group, stackmonitoring_cli.list_discovery_jobs, "list")


# oci stack-monitoring discovery-job-log-collection list-discovery-job-logs -> oci stack-monitoring discovery-job-log-collection list-logs
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.discovery_job_log_collection_group, stackmonitoring_cli.list_discovery_job_logs, "list-logs")


# oci stack-monitoring monitored-resource search-monitored-resource-associations -> oci stack-monitoring monitored-resource search-associations
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.monitored_resource_group, stackmonitoring_cli.search_monitored_resource_associations, "search-associations")


# oci stack-monitoring monitored-resource search-monitored-resource-members -> oci stack-monitoring monitored-resource search-members
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.monitored_resource_group, stackmonitoring_cli.search_monitored_resource_members, "search-members")


# oci stack-monitoring monitored-resource -> oci stack-monitoring resource
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.stack_monitoring_root_group, stackmonitoring_cli.monitored_resource_group, "resource")


# Remove create-monitored-resource-encrypted-credentials from oci stack-monitoring monitored-resource
stackmonitoring_cli.monitored_resource_group.commands.pop(stackmonitoring_cli.create_monitored_resource_encrypted_credentials.name)


# Remove create-monitored-resource-plain-text-credentials from oci stack-monitoring monitored-resource
stackmonitoring_cli.monitored_resource_group.commands.pop(stackmonitoring_cli.create_monitored_resource_plain_text_credentials.name)


# Remove create-monitored-resource-pre-existing-credentials from oci stack-monitoring monitored-resource
stackmonitoring_cli.monitored_resource_group.commands.pop(stackmonitoring_cli.create_monitored_resource_pre_existing_credentials.name)


# Remove update-monitored-resource-encrypted-credentials from oci stack-monitoring monitored-resource
stackmonitoring_cli.monitored_resource_group.commands.pop(stackmonitoring_cli.update_monitored_resource_encrypted_credentials.name)


# Remove update-monitored-resource-plain-text-credentials from oci stack-monitoring monitored-resource
stackmonitoring_cli.monitored_resource_group.commands.pop(stackmonitoring_cli.update_monitored_resource_plain_text_credentials.name)


# Remove update-monitored-resource-pre-existing-credentials from oci stack-monitoring monitored-resource
stackmonitoring_cli.monitored_resource_group.commands.pop(stackmonitoring_cli.update_monitored_resource_pre_existing_credentials.name)


# Remove work-request-error-collection from oci stack-monitoring
stackmonitoring_cli.stack_monitoring_root_group.commands.pop(stackmonitoring_cli.work_request_error_collection_group.name)


# Remove work-request-log-entry-collection from oci stack-monitoring
stackmonitoring_cli.stack_monitoring_root_group.commands.pop(stackmonitoring_cli.work_request_log_entry_collection_group.name)


# Remove work-request-summary-collection from oci stack-monitoring
stackmonitoring_cli.stack_monitoring_root_group.commands.pop(stackmonitoring_cli.work_request_summary_collection_group.name)


# Remove discovery-job-collection from oci stack-monitoring
stackmonitoring_cli.stack_monitoring_root_group.commands.pop(stackmonitoring_cli.discovery_job_collection_group.name)


# Remove discovery-job-log-collection from oci stack-monitoring
stackmonitoring_cli.stack_monitoring_root_group.commands.pop(stackmonitoring_cli.discovery_job_log_collection_group.name)


# oci stack-monitoring work-request-error-collection list-work-request-errors -> oci stack-monitoring work-request
stackmonitoring_cli.work_request_error_collection_group.commands.pop(stackmonitoring_cli.list_work_request_errors.name)
stackmonitoring_cli.work_request_group.add_command(stackmonitoring_cli.list_work_request_errors)


# oci stack-monitoring work-request-log-entry-collection list-work-request-logs -> oci stack-monitoring work-request
stackmonitoring_cli.work_request_log_entry_collection_group.commands.pop(stackmonitoring_cli.list_work_request_logs.name)
stackmonitoring_cli.work_request_group.add_command(stackmonitoring_cli.list_work_request_logs)


# oci stack-monitoring work-request-summary-collection list-work-requests -> oci stack-monitoring work-request
stackmonitoring_cli.work_request_summary_collection_group.commands.pop(stackmonitoring_cli.list_work_requests.name)
stackmonitoring_cli.work_request_group.add_command(stackmonitoring_cli.list_work_requests)


# oci stack-monitoring discovery-job-collection list-discovery-jobs -> oci stack-monitoring discovery-job
stackmonitoring_cli.discovery_job_collection_group.commands.pop(stackmonitoring_cli.list_discovery_jobs.name)
stackmonitoring_cli.discovery_job_group.add_command(stackmonitoring_cli.list_discovery_jobs)


# oci stack-monitoring discovery-job-log-collection list-discovery-job-logs -> oci stack-monitoring discovery-job
stackmonitoring_cli.discovery_job_log_collection_group.commands.pop(stackmonitoring_cli.list_discovery_job_logs.name)
stackmonitoring_cli.discovery_job_group.add_command(stackmonitoring_cli.list_discovery_job_logs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.create_monitored_resource, params_to_exclude=['database_connection_details'])
@stackmonitoring_cli.monitored_resource_group.command(name=stackmonitoring_cli.create_monitored_resource.name, help=stackmonitoring_cli.create_monitored_resource.help)
@cli_util.option('--db-connection-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'db-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'credentials': {'module': 'stack_monitoring', 'class': 'MonitoredResourceCredential'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}, 'additional-credentials': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceCredential]'}, 'additional-aliases': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceAliasCredential]'}, 'freeform-tags': {'module': 'stack_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'stack_monitoring', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_monitored_resource_extended(ctx, **kwargs):
    if 'db_connection_details' in kwargs:
        kwargs['database_connection_details'] = kwargs['db_connection_details']
        kwargs.pop('db_connection_details')

    ctx.invoke(stackmonitoring_cli.create_monitored_resource, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.update_monitored_resource, params_to_exclude=['monitored_resource_id', 'database_connection_details'])
@stackmonitoring_cli.monitored_resource_group.command(name=stackmonitoring_cli.update_monitored_resource.name, help=stackmonitoring_cli.update_monitored_resource.help)
@cli_util.option('--resource-id', required=True, help=u"""The [OCID] of monitored resource. [required]""")
@cli_util.option('--db-connection-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'db-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'credentials': {'module': 'stack_monitoring', 'class': 'MonitoredResourceCredential'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}, 'additional-credentials': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceCredential]'}, 'additional-aliases': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceAliasCredential]'}, 'freeform-tags': {'module': 'stack_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'stack_monitoring', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_monitored_resource_extended(ctx, **kwargs):
    if 'resource_id' in kwargs:
        kwargs['monitored_resource_id'] = kwargs['resource_id']
        kwargs.pop('resource_id')

    if 'db_connection_details' in kwargs:
        kwargs['database_connection_details'] = kwargs['db_connection_details']
        kwargs.pop('db_connection_details')

    ctx.invoke(stackmonitoring_cli.update_monitored_resource, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.delete_monitored_resource, params_to_exclude=['monitored_resource_id'])
@stackmonitoring_cli.monitored_resource_group.command(name=stackmonitoring_cli.delete_monitored_resource.name, help=stackmonitoring_cli.delete_monitored_resource.help)
@cli_util.option('--resource-id', required=True, help=u"""The [OCID] of monitored resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_monitored_resource_extended(ctx, **kwargs):
    if 'resource_id' in kwargs:
        kwargs['monitored_resource_id'] = kwargs['resource_id']
        kwargs.pop('resource_id')

    ctx.invoke(stackmonitoring_cli.delete_monitored_resource, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.get_monitored_resource, params_to_exclude=['monitored_resource_id'])
@stackmonitoring_cli.monitored_resource_group.command(name=stackmonitoring_cli.get_monitored_resource.name, help=stackmonitoring_cli.get_monitored_resource.help)
@cli_util.option('--resource-id', required=True, help=u"""The [OCID] of monitored resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResource'})
@cli_util.wrap_exceptions
def get_monitored_resource_extended(ctx, **kwargs):
    if 'resource_id' in kwargs:
        kwargs['monitored_resource_id'] = kwargs['resource_id']
        kwargs.pop('resource_id')

    ctx.invoke(stackmonitoring_cli.get_monitored_resource, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.change_monitored_resource_compartment, params_to_exclude=['monitored_resource_id'])
@stackmonitoring_cli.monitored_resource_group.command(name=stackmonitoring_cli.change_monitored_resource_compartment.name, help=stackmonitoring_cli.change_monitored_resource_compartment.help)
@cli_util.option('--resource-id', required=True, help=u"""The [OCID] of monitored resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_monitored_resource_compartment_extended(ctx, **kwargs):
    if 'resource_id' in kwargs:
        kwargs['monitored_resource_id'] = kwargs['resource_id']
        kwargs.pop('resource_id')

    ctx.invoke(stackmonitoring_cli.change_monitored_resource_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.disable_external_database, params_to_exclude=['monitored_resource_id'])
@stackmonitoring_cli.monitored_resource_group.command(name=stackmonitoring_cli.disable_external_database.name, help=stackmonitoring_cli.disable_external_database.help)
@cli_util.option('--resource-id', required=True, help=u"""The [OCID] of monitored resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def disable_external_database_extended(ctx, **kwargs):
    if 'resource_id' in kwargs:
        kwargs['monitored_resource_id'] = kwargs['resource_id']
        kwargs.pop('resource_id')

    ctx.invoke(stackmonitoring_cli.disable_external_database, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.search_monitored_resource_members, params_to_exclude=['monitored_resource_id'])
@stackmonitoring_cli.monitored_resource_group.command(name=stackmonitoring_cli.search_monitored_resource_members.name, help=stackmonitoring_cli.search_monitored_resource_members.help)
@cli_util.option('--resource-id', required=True, help=u"""The [OCID] of monitored resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResourceMembersCollection'})
@cli_util.wrap_exceptions
def search_monitored_resource_members_extended(ctx, **kwargs):
    if 'resource_id' in kwargs:
        kwargs['monitored_resource_id'] = kwargs['resource_id']
        kwargs.pop('resource_id')

    ctx.invoke(stackmonitoring_cli.search_monitored_resource_members, **kwargs)


# oci stack-monitoring config create-config-create-auto-promote-config-details -> oci stack-monitoring config create-auto-promote-config
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.config_group, stackmonitoring_cli.create_config_create_auto_promote_config_details, "create-auto-promote-config")


# oci stack-monitoring config update-config-update-auto-promote-config-details -> oci stack-monitoring config update-auto-promote-config
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.config_group, stackmonitoring_cli.update_config_update_auto_promote_config_details, "update-auto-promote-config")


# oci stack-monitoring config-collection list-configs -> oci stack-monitoring config-collection list
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.config_collection_group, stackmonitoring_cli.list_configs, "list")


# Remove config-collection from oci stack-monitoring
stackmonitoring_cli.stack_monitoring_root_group.commands.pop(stackmonitoring_cli.config_collection_group.name)


# oci stack-monitoring config-collection list-configs -> oci stack-monitoring config
stackmonitoring_cli.config_collection_group.commands.pop(stackmonitoring_cli.list_configs.name)
stackmonitoring_cli.config_group.add_command(stackmonitoring_cli.list_configs)


# oci stack-monitoring config create-config-create-license-auto-assign-config-details -> oci stack-monitoring config create-license-auto-assign-config
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.config_group, stackmonitoring_cli.create_config_create_license_auto_assign_config_details, "create-license-auto-assign-config")


# oci stack-monitoring config create-config-create-license-enterprise-extensibility-config-details -> oci stack-monitoring config create-license-enterprise-extensibility-config
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.config_group, stackmonitoring_cli.create_config_create_license_enterprise_extensibility_config_details, "create-license-enterprise-extensibility-config")


# oci stack-monitoring config update-config-update-license-auto-assign-config-details -> oci stack-monitoring config update-license-auto-assign-config
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.config_group, stackmonitoring_cli.update_config_update_license_auto_assign_config_details, "update-license-auto-assign-config")


# oci stack-monitoring config update-config-update-license-enterprise-extensibility-config-details -> oci stack-monitoring config update-license-enterprise-extensibility-config
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.config_group, stackmonitoring_cli.update_config_update_license_enterprise_extensibility_config_details, "update-license-enterprise-extensibility-config")


# oci stack-monitoring resource request-monitored-resources-summarized-count -> oci stack-monitoring resource summarize-count
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.monitored_resource_group, stackmonitoring_cli.request_monitored_resources_summarized_count, "summarize-count")


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.manage_license, params_to_exclude=['monitored_resource_id'])
@stackmonitoring_cli.monitored_resource_group.command(name=stackmonitoring_cli.manage_license.name, help=stackmonitoring_cli.manage_license.help)
@cli_util.option('--resource-id', required=True, help=u"""The [OCID] of monitored resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def manage_license_extended(ctx, **kwargs):

    if 'resource_id' in kwargs:
        kwargs['monitored_resource_id'] = kwargs['resource_id']
        kwargs.pop('resource_id')

    ctx.invoke(stackmonitoring_cli.manage_license, **kwargs)


# oci stack-monitoring create-baselineable-metric-details create-baselineable-metric -> oci stack-monitoring baselineable-metric
stackmonitoring_cli.create_baselineable_metric_details_group.commands.pop(stackmonitoring_cli.create_baselineable_metric.name)
stackmonitoring_cli.baselineable_metric_group.add_command(stackmonitoring_cli.create_baselineable_metric)


# oci stack-monitoring update-baselineable-metric-details update-baselineable-metric -> oci stack-monitoring baselineable-metric
stackmonitoring_cli.update_baselineable_metric_details_group.commands.pop(stackmonitoring_cli.update_baselineable_metric.name)
stackmonitoring_cli.baselineable_metric_group.add_command(stackmonitoring_cli.update_baselineable_metric)


# oci stack-monitoring evaluate-baselineable-metric-result evaluate-baselineable-metric -> oci stack-monitoring baselineable-metric
stackmonitoring_cli.evaluate_baselineable_metric_result_group.commands.pop(stackmonitoring_cli.evaluate_baselineable_metric.name)
stackmonitoring_cli.baselineable_metric_group.add_command(stackmonitoring_cli.evaluate_baselineable_metric)


# oci stack-monitoring baselineable-metric-summary list-baselineable-metrics -> oci stack-monitoring baselineable-metric
stackmonitoring_cli.baselineable_metric_summary_group.commands.pop(stackmonitoring_cli.list_baselineable_metrics.name)
stackmonitoring_cli.baselineable_metric_group.add_command(stackmonitoring_cli.list_baselineable_metrics)


# oci stack-monitoring baselineable-metric create-baselineable-metric -> oci stack-monitoring baselineable-metric create
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.baselineable_metric_group, stackmonitoring_cli.create_baselineable_metric, "create")


# oci stack-monitoring baselineable update-baselineable-metric -> oci stack-monitoring baselineable-metr update
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.baselineable_metric_group, stackmonitoring_cli.update_baselineable_metric, "update")


# oci stack-monitoring baselineable-metric evaluate-baselineable-metric -> oci stack-monitoring baselineable-metr evaluate
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.baselineable_metric_group, stackmonitoring_cli.evaluate_baselineable_metric, "evaluate")


# oci stack-monitoring baselineable-metric list-baselineable-metrics -> oci stack-monitoring baselineable-metr list
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.baselineable_metric_group, stackmonitoring_cli.list_baselineable_metrics, "list")


# Remove create-baselineable-metric-details from oci stack-monitoring
stackmonitoring_cli.stack_monitoring_root_group.commands.pop(stackmonitoring_cli.create_baselineable_metric_details_group.name)


# Remove update-baselineable-metric-details from oci stack-monitoring
stackmonitoring_cli.stack_monitoring_root_group.commands.pop(stackmonitoring_cli.update_baselineable_metric_details_group.name)


# Remove evaluate-baselineable-metric-result from oci stack-monitoring
stackmonitoring_cli.stack_monitoring_root_group.commands.pop(stackmonitoring_cli.evaluate_baselineable_metric_result_group.name)


# Remove baselineable-metric-summary from oci stack-monitoring
stackmonitoring_cli.stack_monitoring_root_group.commands.pop(stackmonitoring_cli.baselineable_metric_summary_group.name)


# oci stack-monitoring update-baselineable-metric-details update-baselineable-metric --baselineable-metric-id -> oci stack-monitoring baselineable-metric update --metric-id
# oci stack-monitoring update-baselineable-metric-details update-baselineable-metric --namespace -> oci stack-monitoring baselineable-metric update --metric-namespace
@cli_util.copy_params_from_generated_command(stackmonitoring_cli.update_baselineable_metric, params_to_exclude=['baselineable_metric_id', 'namespace'])
@stackmonitoring_cli.baselineable_metric_group.command(name=stackmonitoring_cli.update_baselineable_metric.name, help=stackmonitoring_cli.update_baselineable_metric.help)
@cli_util.option('--metric-id', required=True, help=u"""Identifier for the metric [required]""")
@cli_util.option('--metric-namespace', required=True, help=u"""namespace of the metric [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'stack_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'stack_monitoring', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'stack_monitoring', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'stack_monitoring', 'class': 'BaselineableMetric'})
@cli_util.wrap_exceptions
def update_baselineable_metric_extended(ctx, **kwargs):

    if 'metric_id' in kwargs:
        kwargs['baselineable_metric_id'] = kwargs['metric_id']
        kwargs.pop('metric_id')

    if 'metric_namespace' in kwargs:
        kwargs['namespace'] = kwargs['metric_namespace']
        kwargs.pop('metric_namespace')

    ctx.invoke(stackmonitoring_cli.update_baselineable_metric, **kwargs)


# oci stack-monitoring evaluate-baselineable-metric-result evaluate-baselineable-metric --baselineable-metric-id -> oci stack-monitoring baselineable-metric evaluate --metric-id
@cli_util.copy_params_from_generated_command(stackmonitoring_cli.evaluate_baselineable_metric, params_to_exclude=['baselineable_metric_id'])
@stackmonitoring_cli.baselineable_metric_group.command(name=stackmonitoring_cli.evaluate_baselineable_metric.name, help=stackmonitoring_cli.evaluate_baselineable_metric.help)
@cli_util.option('--metric-id', required=True, help=u"""Identifier for the metric [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'stack_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'stack_monitoring', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'stack_monitoring', 'class': 'dict(str, dict(str, object))'}, 'items': {'module': 'stack_monitoring', 'class': 'list[MetricData]'}}, output_type={'module': 'stack_monitoring', 'class': 'BaselineableMetric'})
@cli_util.wrap_exceptions
def evaluate_baselineable_metric_extended(ctx, **kwargs):

    if 'metric_id' in kwargs:
        kwargs['baselineable_metric_id'] = kwargs['metric_id']
        kwargs.pop('metric_id')

    ctx.invoke(stackmonitoring_cli.evaluate_baselineable_metric, **kwargs)


# oci stack-monitoring baselineable-metric get --baselineable-metric-id -> oci stack-monitoring baselineable-metric get --metric-id
@cli_util.copy_params_from_generated_command(stackmonitoring_cli.delete_baselineable_metric, params_to_exclude=['baselineable_metric_id'])
@stackmonitoring_cli.baselineable_metric_group.command(name=stackmonitoring_cli.delete_baselineable_metric.name, help=stackmonitoring_cli.delete_baselineable_metric.help)
@cli_util.option('--metric-id', required=True, help=u"""Identifier for the metric [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_baselineable_metric_extended(ctx, **kwargs):

    if 'metric_id' in kwargs:
        kwargs['baselineable_metric_id'] = kwargs['metric_id']
        kwargs.pop('metric_id')

    ctx.invoke(stackmonitoring_cli.delete_baselineable_metric, **kwargs)


# oci stack-monitoring baselineable-metric delete --baselineable-metric-id -> oci stack-monitoring baselineable-metric delete --metric-id
@cli_util.copy_params_from_generated_command(stackmonitoring_cli.get_baselineable_metric, params_to_exclude=['baselineable_metric_id'])
@stackmonitoring_cli.baselineable_metric_group.command(name=stackmonitoring_cli.get_baselineable_metric.name, help=stackmonitoring_cli.get_baselineable_metric.help)
@cli_util.option('--metric-id', required=True, help=u"""Identifier for the metric [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'BaselineableMetric'})
@cli_util.wrap_exceptions
def get_baselineable_metric_extended(ctx, **kwargs):

    if 'metric_id' in kwargs:
        kwargs['baselineable_metric_id'] = kwargs['metric_id']
        kwargs.pop('metric_id')

    ctx.invoke(stackmonitoring_cli.get_baselineable_metric, **kwargs)


# oci stack-monitoring create-baselineable-metric-details create-baselineable-metric --namespace -> oci stack-monitoring baselineable-metric create --metric-namespace
@cli_util.copy_params_from_generated_command(stackmonitoring_cli.create_baselineable_metric, params_to_exclude=['namespace'])
@stackmonitoring_cli.baselineable_metric_group.command(name=stackmonitoring_cli.create_baselineable_metric.name, help=stackmonitoring_cli.create_baselineable_metric.help)
@cli_util.option('--metric-namespace', required=True, help=u"""namespace of the metric [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'BaselineableMetric'})
@cli_util.wrap_exceptions
def create_baselineable_metric_extended(ctx, **kwargs):

    if 'metric_namespace' in kwargs:
        kwargs['namespace'] = kwargs['metric_namespace']
        kwargs.pop('metric_namespace')

    ctx.invoke(stackmonitoring_cli.create_baselineable_metric, **kwargs)


# oci stack-monitoring baselineable-metric list-baselineable-metrics --baselineable-metric-id -> oci stack-monitoring baselineable-metric list --metric-id
@cli_util.copy_params_from_generated_command(stackmonitoring_cli.list_baselineable_metrics, params_to_exclude=['baselineable_metric_id'])
@stackmonitoring_cli.baselineable_metric_group.command(name=stackmonitoring_cli.list_baselineable_metrics.name, help=stackmonitoring_cli.list_baselineable_metrics.help)
@cli_util.option('--metric-id', help=u"""Identifier for the metric""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'stack_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'stack_monitoring', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'stack_monitoring', 'class': 'dict(str, dict(str, object))'}, 'items': {'module': 'stack_monitoring', 'class': 'list[MetricData]'}}, output_type={'module': 'stack_monitoring', 'class': 'BaselineableMetric'})
@cli_util.wrap_exceptions
def list_baselineable_metrics_extended(ctx, **kwargs):

    if 'metric_id' in kwargs:
        kwargs['baselineable_metric_id'] = kwargs['metric_id']
        kwargs.pop('metric_id')

    ctx.invoke(stackmonitoring_cli.list_baselineable_metrics, **kwargs)


# oci stack-monitoring monitored-resource-task create-monitored-resource-task-import-oci-telemetry-resources-task-details -> oci stack-monitoring monitored- import-telemetry-resources
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.monitored_resource_task_group, stackmonitoring_cli.create_monitored_resource_task_import_oci_telemetry_resources_task_details, "import-telemetry-resources")


# oci stack-monitoring monitored-resource-task -> oci stack-monitoring resource-task
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.stack_monitoring_root_group, stackmonitoring_cli.monitored_resource_task_group, "resource-task")


# oci stack-monitoring monitored-resource-type create-monitored-resource-type-system-format-resource-type-metadata-details -> oci stack-monitoring monitored-resource-type create-system-format-resource-type
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.monitored_resource_type_group, stackmonitoring_cli.create_monitored_resource_type_system_format_resource_type_metadata_details, "create-system-format-resource-type")


# oci stack-monitoring monitored-resource-type update-monitored-resource-type-system-format-resource-type-metadata-details -> oci stack-monitoring monitored-resource-type update-system-format-resource-type
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.monitored_resource_type_group, stackmonitoring_cli.update_monitored_resource_type_system_format_resource_type_metadata_details, "update-system-format-resource-type")


# oci stack-monitoring monitored-resource-type -> oci stack-monitoring resource-type
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.stack_monitoring_root_group, stackmonitoring_cli.monitored_resource_type_group, "resource-type")


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.change_monitored_resource_task_compartment, params_to_exclude=['monitored_resource_task_id'])
@stackmonitoring_cli.monitored_resource_task_group.command(name=stackmonitoring_cli.change_monitored_resource_task_compartment.name, help=stackmonitoring_cli.change_monitored_resource_task_compartment.help)
@cli_util.option('--resource-task-id', required=True, help=u"""The [OCID] of stack monitoring resource task. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_monitored_resource_task_compartment_extended(ctx, **kwargs):

    if 'resource_task_id' in kwargs:
        kwargs['monitored_resource_task_id'] = kwargs['resource_task_id']
        kwargs.pop('resource_task_id')

    ctx.invoke(stackmonitoring_cli.change_monitored_resource_task_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.get_monitored_resource_task, params_to_exclude=['monitored_resource_task_id'])
@stackmonitoring_cli.monitored_resource_task_group.command(name=stackmonitoring_cli.get_monitored_resource_task.name, help=stackmonitoring_cli.get_monitored_resource_task.help)
@cli_util.option('--resource-task-id', required=True, help=u"""The [OCID] of stack monitoring resource task. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResourceTask'})
@cli_util.wrap_exceptions
def get_monitored_resource_task_extended(ctx, **kwargs):

    if 'resource_task_id' in kwargs:
        kwargs['monitored_resource_task_id'] = kwargs['resource_task_id']
        kwargs.pop('resource_task_id')

    ctx.invoke(stackmonitoring_cli.get_monitored_resource_task, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.update_monitored_resource_task, params_to_exclude=['monitored_resource_task_id'])
@stackmonitoring_cli.monitored_resource_task_group.command(name=stackmonitoring_cli.update_monitored_resource_task.name, help=stackmonitoring_cli.update_monitored_resource_task.help)
@cli_util.option('--resource-task-id', required=True, help=u"""The [OCID] of stack monitoring resource task. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'stack_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'stack_monitoring', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResourceTask'})
@cli_util.wrap_exceptions
def update_monitored_resource_task_extended(ctx, **kwargs):

    if 'resource_task_id' in kwargs:
        kwargs['monitored_resource_task_id'] = kwargs['resource_task_id']
        kwargs.pop('resource_task_id')

    ctx.invoke(stackmonitoring_cli.update_monitored_resource_task, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.create_monitored_resource_task_import_oci_telemetry_resources_task_details, params_to_exclude=['task_details_namespace', 'task_details_source', 'task_details_availability_proxy_metric_collection_interval', 'task_details_availability_proxy_metrics', 'task_details_resource_group'])
@stackmonitoring_cli.monitored_resource_task_group.command(name=stackmonitoring_cli.create_monitored_resource_task_import_oci_telemetry_resources_task_details.name, help=stackmonitoring_cli.create_monitored_resource_task_import_oci_telemetry_resources_task_details.help)
@cli_util.option('--namespace', required=True, help=u"""Name space to be used for OCI Native service resources discovery. [required]""")
@cli_util.option('--source', required=True, type=custom_types.CliCaseInsensitiveChoice(["OCI_TELEMETRY_NATIVE", "OCI_TELEMETRY_PROMETHEUS"]), help=u"""Source from where the metrics pushed to telemetry. Possible values:   * OCI_TELEMETRY_NATIVE      - The metrics are pushed to telemetry from OCI Native Services.   * OCI_TELEMETRY_PROMETHEUS  - The metrics are pushed to telemetry from Prometheus. [required]""")
@cli_util.option('--availability-proxy-metric-collection-interval', type=click.INT, help=u"""Metrics collection interval in seconds used when calculating the availability of the resource based on metrics specified using the property 'availabilityProxyMetrics'.""")
@cli_util.option('--availability-proxy-metrics', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of metrics to be used to calculate the availability of the resource. Resource is considered to be up if at least one of the specified metrics is available for the resource during the specified interval using the property 'availabilityProxyMetricCollectionIntervalInSeconds'. If no metrics are specified, availability will not be calculated for the resource.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--resource-group', help=u"""The resource group to use while fetching metrics from telemetry. If not specified, resource group will be skipped in the list metrics request.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'stack_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'stack_monitoring', 'class': 'dict(str, dict(str, object))'}, 'availability-proxy-metrics': {'module': 'stack_monitoring', 'class': 'list[string]'}}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResourceTask'})
@cli_util.wrap_exceptions
def create_monitored_resource_task_import_oci_telemetry_resources_task_details_extended(ctx, **kwargs):

    if 'namespace' in kwargs:
        kwargs['task_details_namespace'] = kwargs['namespace']
        kwargs.pop('namespace')

    if 'source' in kwargs:
        kwargs['task_details_source'] = kwargs['source']
        kwargs.pop('source')

    if 'availability_proxy_metric_collection_interval' in kwargs:
        kwargs['task_details_availability_proxy_metric_collection_interval'] = kwargs['availability_proxy_metric_collection_interval']
        kwargs.pop('availability_proxy_metric_collection_interval')

    if 'availability_proxy_metrics' in kwargs:
        kwargs['task_details_availability_proxy_metrics'] = kwargs['availability_proxy_metrics']
        kwargs.pop('availability_proxy_metrics')

    if 'resource_group' in kwargs:
        kwargs['task_details_resource_group'] = kwargs['resource_group']
        kwargs.pop('resource_group')

    ctx.invoke(stackmonitoring_cli.create_monitored_resource_task_import_oci_telemetry_resources_task_details, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.delete_monitored_resource_type, params_to_exclude=['monitored_resource_type_id'])
@stackmonitoring_cli.monitored_resource_type_group.command(name=stackmonitoring_cli.delete_monitored_resource_type.name, help=stackmonitoring_cli.delete_monitored_resource_type.help)
@cli_util.option('--resource-type-id', required=True, help=u"""The [OCID] of monitored resource type. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_monitored_resource_type_extended(ctx, **kwargs):

    if 'resource_type_id' in kwargs:
        kwargs['monitored_resource_type_id'] = kwargs['resource_type_id']
        kwargs.pop('resource_type_id')

    ctx.invoke(stackmonitoring_cli.delete_monitored_resource_type, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.get_monitored_resource_type, params_to_exclude=['monitored_resource_type_id'])
@stackmonitoring_cli.monitored_resource_type_group.command(name=stackmonitoring_cli.get_monitored_resource_type.name, help=stackmonitoring_cli.get_monitored_resource_type.help)
@cli_util.option('--resource-type-id', required=True, help=u"""The [OCID] of monitored resource type. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResourceType'})
@cli_util.wrap_exceptions
def get_monitored_resource_type_extended(ctx, **kwargs):

    if 'resource_type_id' in kwargs:
        kwargs['monitored_resource_type_id'] = kwargs['resource_type_id']
        kwargs.pop('resource_type_id')

    ctx.invoke(stackmonitoring_cli.get_monitored_resource_type, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.update_monitored_resource_type, params_to_exclude=['monitored_resource_type_id'])
@stackmonitoring_cli.monitored_resource_type_group.command(name=stackmonitoring_cli.update_monitored_resource_type.name, help=stackmonitoring_cli.update_monitored_resource_type.help)
@cli_util.option('--resource-type-id', required=True, help=u"""The [OCID] of monitored resource type. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'stack_monitoring', 'class': 'ResourceTypeMetadataDetails'}, 'freeform-tags': {'module': 'stack_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'stack_monitoring', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResourceType'})
@cli_util.wrap_exceptions
def update_monitored_resource_type_extended(ctx, **kwargs):

    if 'resource_type_id' in kwargs:
        kwargs['monitored_resource_type_id'] = kwargs['resource_type_id']
        kwargs.pop('resource_type_id')

    ctx.invoke(stackmonitoring_cli.update_monitored_resource_type, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.create_monitored_resource_type_system_format_resource_type_metadata_details, params_to_exclude=['metadata_agent_properties', 'metadata_required_properties', 'metadata_unique_property_sets', 'metadata_valid_properties_for_create', 'metadata_valid_properties_for_update', 'metadata_valid_property_values'])
@stackmonitoring_cli.monitored_resource_type_group.command(name=stackmonitoring_cli.create_monitored_resource_type_system_format_resource_type_metadata_details.name, help=stackmonitoring_cli.create_monitored_resource_type_system_format_resource_type_metadata_details.help)
@cli_util.option('--agent-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of properties needed by the agent for monitoring the resource. Valid only if resource type is OCI management agent based. When specified, these properties are passed to the management agent during resource create or update.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--required-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of required properties for resource type.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--unique-property-sets', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of property sets used to uniquely identify the resources. This check is made during create or update of stack monitoring resource. The resource has to pass unique check for each set in the list. For example, database can have user, password and SID as one unique set. Another unique set would be user, password and service name.

This option is a JSON list with items of type UniquePropertySet.  For documentation on UniquePropertySet please see our API reference: https://docs.cloud.oracle.com/api/#/en/stackmonitoring/20210330/datatypes/UniquePropertySet.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--valid-properties-for-create', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of valid properties for resource type while creating the monitored resource. If resources of this type specifies any other properties during create operation, the operation will fail.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--valid-properties-for-update', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of valid properties for resource type while updating the monitored resource. If resources of this type specifies any other properties during update operation, the operation will fail.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--valid-property-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of valid values for the properties. This is useful when resource type wants to restrict only certain values for some properties. For instance for 'osType' property, supported values can be restricted to be either Linux or Windows. Example: `{ "osType": ["Linux","Windows","Solaris"]}`
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'stack_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'stack_monitoring', 'class': 'dict(str, dict(str, object))'}, 'required-properties': {'module': 'stack_monitoring', 'class': 'list[string]'}, 'agent-properties': {'module': 'stack_monitoring', 'class': 'list[string]'}, 'valid-properties-for-create': {'module': 'stack_monitoring', 'class': 'list[string]'}, 'valid-properties-for-update': {'module': 'stack_monitoring', 'class': 'list[string]'}, 'unique-property-sets': {'module': 'stack_monitoring', 'class': 'list[UniquePropertySet]'}, 'valid-property-values': {'module': 'stack_monitoring', 'class': 'dict(str, list[string])'}}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResourceType'})
@cli_util.wrap_exceptions
def create_monitored_resource_type_system_format_resource_type_metadata_details_extended(ctx, **kwargs):

    if 'agent_properties' in kwargs:
        kwargs['metadata_agent_properties'] = kwargs['agent_properties']
        kwargs.pop('agent_properties')

    if 'required_properties' in kwargs:
        kwargs['metadata_required_properties'] = kwargs['required_properties']
        kwargs.pop('required_properties')

    if 'unique_property_sets' in kwargs:
        kwargs['metadata_unique_property_sets'] = kwargs['unique_property_sets']
        kwargs.pop('unique_property_sets')

    if 'valid_properties_for_create' in kwargs:
        kwargs['metadata_valid_properties_for_create'] = kwargs['valid_properties_for_create']
        kwargs.pop('valid_properties_for_create')

    if 'valid_properties_for_update' in kwargs:
        kwargs['metadata_valid_properties_for_update'] = kwargs['valid_properties_for_update']
        kwargs.pop('valid_properties_for_update')

    if 'valid_property_values' in kwargs:
        kwargs['metadata_valid_property_values'] = kwargs['valid_property_values']
        kwargs.pop('valid_property_values')

    ctx.invoke(stackmonitoring_cli.create_monitored_resource_type_system_format_resource_type_metadata_details, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.update_monitored_resource_type_system_format_resource_type_metadata_details, params_to_exclude=['monitored_resource_type_id', 'metadata_agent_properties', 'metadata_required_properties', 'metadata_unique_property_sets', 'metadata_valid_properties_for_create', 'metadata_valid_properties_for_update', 'metadata_valid_property_values'])
@stackmonitoring_cli.monitored_resource_type_group.command(name=stackmonitoring_cli.update_monitored_resource_type_system_format_resource_type_metadata_details.name, help=stackmonitoring_cli.update_monitored_resource_type_system_format_resource_type_metadata_details.help)
@cli_util.option('--resource-type-id', required=True, help=u"""The [OCID] of monitored resource type. [required]""")
@cli_util.option('--agent-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of properties needed by the agent for monitoring the resource. Valid only if resource type is OCI management agent based. When specified, these properties are passed to the management agent during resource create or update.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--required-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of required properties for resource type.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--unique-property-sets', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of property sets used to uniquely identify the resources. This check is made during create or update of stack monitoring resource. The resource has to pass unique check for each set in the list. For example, database can have user, password and SID as one unique set. Another unique set would be user, password and service name.

This option is a JSON list with items of type UniquePropertySet.  For documentation on UniquePropertySet please see our API reference: https://docs.cloud.oracle.com/api/#/en/stackmonitoring/20210330/datatypes/UniquePropertySet.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--valid-properties-for-create', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of valid properties for resource type while creating the monitored resource. If resources of this type specifies any other properties during create operation, the operation will fail.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--valid-properties-for-update', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of valid properties for resource type while updating the monitored resource. If resources of this type specifies any other properties during update operation, the operation will fail.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--valid-property-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of valid values for the properties. This is useful when resource type wants to restrict only certain values for some properties. For instance for 'osType' property, supported values can be restricted to be either Linux or Windows. Example: `{ "osType": ["Linux","Windows","Solaris"]}`
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'stack_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'stack_monitoring', 'class': 'dict(str, dict(str, object))'}, 'required-properties': {'module': 'stack_monitoring', 'class': 'list[string]'}, 'agent-properties': {'module': 'stack_monitoring', 'class': 'list[string]'}, 'valid-properties-for-create': {'module': 'stack_monitoring', 'class': 'list[string]'}, 'valid-properties-for-update': {'module': 'stack_monitoring', 'class': 'list[string]'}, 'unique-property-sets': {'module': 'stack_monitoring', 'class': 'list[UniquePropertySet]'}, 'valid-property-values': {'module': 'stack_monitoring', 'class': 'dict(str, list[string])'}}, output_type={'module': 'stack_monitoring', 'class': 'MonitoredResourceType'})
@cli_util.wrap_exceptions
def update_monitored_resource_type_system_format_resource_type_metadata_details_extended(ctx, **kwargs):

    if 'resource_type_id' in kwargs:
        kwargs['monitored_resource_type_id'] = kwargs['resource_type_id']
        kwargs.pop('resource_type_id')

    if 'agent_properties' in kwargs:
        kwargs['metadata_agent_properties'] = kwargs['agent_properties']
        kwargs.pop('agent_properties')

    if 'required_properties' in kwargs:
        kwargs['metadata_required_properties'] = kwargs['required_properties']
        kwargs.pop('required_properties')

    if 'unique_property_sets' in kwargs:
        kwargs['metadata_unique_property_sets'] = kwargs['unique_property_sets']
        kwargs.pop('unique_property_sets')

    if 'valid_properties_for_create' in kwargs:
        kwargs['metadata_valid_properties_for_create'] = kwargs['valid_properties_for_create']
        kwargs.pop('valid_properties_for_create')

    if 'valid_properties_for_update' in kwargs:
        kwargs['metadata_valid_properties_for_update'] = kwargs['valid_properties_for_update']
        kwargs.pop('valid_properties_for_update')

    if 'valid_property_values' in kwargs:
        kwargs['metadata_valid_property_values'] = kwargs['valid_property_values']
        kwargs.pop('valid_property_values')

    ctx.invoke(stackmonitoring_cli.update_monitored_resource_type_system_format_resource_type_metadata_details, **kwargs)


# oci stack-monitoring metric-extension create-metric-extension-jmx-query-properties -> oci stack-monitoring metric-extension create-jmx-metric-ext
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.metric_extension_group, stackmonitoring_cli.create_metric_extension_jmx_query_properties, "create-jmx-metric-ext")


# oci stack-monitoring metric-extension create-metric-extension-os-command-query-properties -> oci stack-monitoring metric-extension create-os-cmd-metric-ext
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.metric_extension_group, stackmonitoring_cli.create_metric_extension_os_command_query_properties, "create-os-cmd-metric-ext")


# oci stack-monitoring metric-extension create-metric-extension-sql-query-properties -> oci stack-monitoring metric-extension create-sql-metric-ext
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.metric_extension_group, stackmonitoring_cli.create_metric_extension_sql_query_properties, "create-sql-metric-ext")


# oci stack-monitoring metric-extension update-metric-extension-jmx-update-query-properties -> oci stack-monitoring metric-extension update-jmx-metric-ext
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.metric_extension_group, stackmonitoring_cli.update_metric_extension_jmx_update_query_properties, "update-jmx-metric-ext")


# oci stack-monitoring metric-extension update-metric-extension-os-command-update-query-properties -> oci stack-monitoring metric-extension update-os-cmd-metric-ext
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.metric_extension_group, stackmonitoring_cli.update_metric_extension_os_command_update_query_properties, "update-os-cmd-metric-ext")


# oci stack-monitoring metric-extension update-metric-extension-sql-update-query-properties -> oci stack-monitoring metric-extension update-sql-metric-ext
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.metric_extension_group, stackmonitoring_cli.update_metric_extension_sql_update_query_properties, "update-sql-metric-ext")


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.change_metric_extension_compartment, params_to_exclude=['metric_extension_id'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.change_metric_extension_compartment.name, help=stackmonitoring_cli.change_metric_extension_compartment.help)
@cli_util.option('--metric-ext-id', required=True, help=u"""The [OCID] of the metric extension resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_metric_extension_compartment_extended(ctx, **kwargs):

    if 'metric_ext_id' in kwargs:
        kwargs['metric_extension_id'] = kwargs['metric_ext_id']
        kwargs.pop('metric_ext_id')

    ctx.invoke(stackmonitoring_cli.change_metric_extension_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.create_metric_extension, params_to_exclude=['collection_recurrences'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.create_metric_extension.name, help=stackmonitoring_cli.create_metric_extension.help)
@cli_util.option('--collection-schedule', required=True, help=u"""Schedule of metric extension should use RFC 5545 format i.e. recur-rule-part = "FREQ";INTERVAL where FREQ rule part identifies the type of recurrence rule. Valid values are "MINUTELY","HOURLY","DAILY" to specify repeating events based on an interval of a minute, an hour and a day or more. Example- FREQ=DAILY;INTERVAL=1 [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metric-list': {'module': 'stack_monitoring', 'class': 'list[Metric]'}, 'query-properties': {'module': 'stack_monitoring', 'class': 'MetricExtensionQueryProperties'}}, output_type={'module': 'stack_monitoring', 'class': 'MetricExtension'})
@cli_util.wrap_exceptions
def create_metric_extension_extended(ctx, **kwargs):

    if 'collection_schedule' in kwargs:
        kwargs['collection_recurrences'] = kwargs['collection_schedule']
        kwargs.pop('collection_schedule')

    ctx.invoke(stackmonitoring_cli.create_metric_extension, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.create_metric_extension_jmx_query_properties, params_to_exclude=['collection_recurrences', 'query_properties_jmx_attributes', 'query_properties_managed_bean_query', 'query_properties_auto_row_prefix', 'query_properties_identity_metric', 'query_properties_is_metric_service_enabled'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.create_metric_extension_jmx_query_properties.name, help=stackmonitoring_cli.create_metric_extension_jmx_query_properties.help)
@cli_util.option('--collection-schedule', required=True, help=u"""Schedule of metric extension should use RFC 5545 format i.e. recur-rule-part = "FREQ";INTERVAL where FREQ rule part identifies the type of recurrence rule. Valid values are "MINUTELY","HOURLY","DAILY" to specify repeating events based on an interval of a minute, an hour and a day or more. Example- FREQ=DAILY;INTERVAL=1 [required]""")
@cli_util.option('--jmx-attributes', required=True, help=u"""List of JMX attributes or Metric Service Table columns separated by semi-colon [required]""")
@cli_util.option('--managed-bean-query', required=True, help=u"""JMX Managed Bean Query or Metric Service Table name [required]""")
@cli_util.option('--auto-row-prefix', help=u"""Prefix for an auto generated metric, in case multiple rows with non unique key values are returned""")
@cli_util.option('--identity-metric', help=u"""Semi-colon separated list of key properties from Managed Bean ObjectName to be used as key metrics""")
@cli_util.option('--is-metric-service-enabled', type=click.BOOL, help=u"""Indicates if Metric Service is enabled on server domain""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metric-list': {'module': 'stack_monitoring', 'class': 'list[Metric]'}}, output_type={'module': 'stack_monitoring', 'class': 'MetricExtension'})
@cli_util.wrap_exceptions
def create_metric_extension_jmx_query_properties_extended(ctx, **kwargs):

    if 'collection_schedule' in kwargs:
        kwargs['collection_recurrences'] = kwargs['collection_schedule']
        kwargs.pop('collection_schedule')

    if 'jmx_attributes' in kwargs:
        kwargs['query_properties_jmx_attributes'] = kwargs['jmx_attributes']
        kwargs.pop('jmx_attributes')

    if 'managed_bean_query' in kwargs:
        kwargs['query_properties_managed_bean_query'] = kwargs['managed_bean_query']
        kwargs.pop('managed_bean_query')

    if 'auto_row_prefix' in kwargs:
        kwargs['query_properties_auto_row_prefix'] = kwargs['auto_row_prefix']
        kwargs.pop('auto_row_prefix')

    if 'identity_metric' in kwargs:
        kwargs['query_properties_identity_metric'] = kwargs['identity_metric']
        kwargs.pop('identity_metric')

    if 'is_metric_service_enabled' in kwargs:
        kwargs['query_properties_is_metric_service_enabled'] = kwargs['is_metric_service_enabled']
        kwargs.pop('is_metric_service_enabled')

    ctx.invoke(stackmonitoring_cli.create_metric_extension_jmx_query_properties, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.create_metric_extension_os_command_query_properties, params_to_exclude=['collection_recurrences', 'query_properties_command', 'query_properties_delimiter', 'query_properties_arguments', 'query_properties_script_details', 'query_properties_starts_with'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.create_metric_extension_os_command_query_properties.name, help=stackmonitoring_cli.create_metric_extension_os_command_query_properties.help)
@cli_util.option('--collection-schedule', required=True, help=u"""Schedule of metric extension should use RFC 5545 format i.e. recur-rule-part = "FREQ";INTERVAL where FREQ rule part identifies the type of recurrence rule. Valid values are "MINUTELY","HOURLY","DAILY" to specify repeating events based on an interval of a minute, an hour and a day or more. Example- FREQ=DAILY;INTERVAL=1 [required]""")
@cli_util.option('--command', required=True, help=u"""OS command to execute without arguments [required]""")
@cli_util.option('--delimiter', required=True, help=u"""Character used to delimit multiple metric values in single line of output [required]""")
@cli_util.option('--arguments', help=u"""Arguments required by either command or script""")
@cli_util.option('--script-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--starts-with', help=u"""String prefix used to identify metric output of the OS Command""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metric-list': {'module': 'stack_monitoring', 'class': 'list[Metric]'}, 'script-details': {'module': 'stack_monitoring', 'class': 'ScriptFileDetails'}}, output_type={'module': 'stack_monitoring', 'class': 'MetricExtension'})
@cli_util.wrap_exceptions
def create_metric_extension_os_command_query_properties_extended(ctx, **kwargs):

    if 'collection_schedule' in kwargs:
        kwargs['collection_recurrences'] = kwargs['collection_schedule']
        kwargs.pop('collection_schedule')

    if 'command' in kwargs:
        kwargs['query_properties_command'] = kwargs['command']
        kwargs.pop('command')

    if 'delimiter' in kwargs:
        kwargs['query_properties_delimiter'] = kwargs['delimiter']
        kwargs.pop('delimiter')

    if 'arguments' in kwargs:
        kwargs['query_properties_arguments'] = kwargs['arguments']
        kwargs.pop('arguments')

    if 'script_details' in kwargs:
        kwargs['query_properties_script_details'] = kwargs['script_details']
        kwargs.pop('script_details')

    if 'starts_with' in kwargs:
        kwargs['query_properties_starts_with'] = kwargs['starts_with']
        kwargs.pop('starts_with')

    ctx.invoke(stackmonitoring_cli.create_metric_extension_os_command_query_properties, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.create_metric_extension_sql_query_properties, params_to_exclude=['collection_recurrences', 'query_properties_sql_details', 'query_properties_sql_type', 'query_properties_in_param_details', 'query_properties_out_param_details'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.create_metric_extension_sql_query_properties.name, help=stackmonitoring_cli.create_metric_extension_sql_query_properties.help)
@cli_util.option('--collection-schedule', required=True, help=u"""Schedule of metric extension should use RFC 5545 format i.e. recur-rule-part = "FREQ";INTERVAL where FREQ rule part identifies the type of recurrence rule. Valid values are "MINUTELY","HOURLY","DAILY" to specify repeating events based on an interval of a minute, an hour and a day or more. Example- FREQ=DAILY;INTERVAL=1 [required]""")
@cli_util.option('--sql-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--sql-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["STATEMENT", "SQL_SCRIPT"]), help=u"""Type of SQL data collection method i.e. either a Statement or SQL Script File [required]""")
@cli_util.option('--in-param-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of values and position of PL/SQL procedure IN parameters

This option is a JSON list with items of type SqlInParamDetails.  For documentation on SqlInParamDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/stackmonitoring/20210330/datatypes/SqlInParamDetails.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--out-param-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metric-list': {'module': 'stack_monitoring', 'class': 'list[Metric]'}, 'sql-details': {'module': 'stack_monitoring', 'class': 'SqlDetails'}, 'in-param-details': {'module': 'stack_monitoring', 'class': 'list[SqlInParamDetails]'}, 'out-param-details': {'module': 'stack_monitoring', 'class': 'SqlOutParamDetails'}}, output_type={'module': 'stack_monitoring', 'class': 'MetricExtension'})
@cli_util.wrap_exceptions
def create_metric_extension_sql_query_properties_extended(ctx, **kwargs):

    if 'collection_schedule' in kwargs:
        kwargs['collection_recurrences'] = kwargs['collection_schedule']
        kwargs.pop('collection_schedule')

    if 'sql_details' in kwargs:
        kwargs['query_properties_sql_details'] = kwargs['sql_details']
        kwargs.pop('sql_details')

    if 'sql_type' in kwargs:
        kwargs['query_properties_sql_type'] = kwargs['sql_type']
        kwargs.pop('sql_type')

    if 'in_param_details' in kwargs:
        kwargs['query_properties_in_param_details'] = kwargs['in_param_details']
        kwargs.pop('in_param_details')

    if 'out_param_details' in kwargs:
        kwargs['query_properties_out_param_details'] = kwargs['out_param_details']
        kwargs.pop('out_param_details')

    ctx.invoke(stackmonitoring_cli.create_metric_extension_sql_query_properties, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.delete_metric_extension, params_to_exclude=['metric_extension_id'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.delete_metric_extension.name, help=stackmonitoring_cli.delete_metric_extension.help)
@cli_util.option('--metric-ext-id', required=True, help=u"""The [OCID] of the metric extension resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_metric_extension_extended(ctx, **kwargs):

    if 'metric_ext_id' in kwargs:
        kwargs['metric_extension_id'] = kwargs['metric_ext_id']
        kwargs.pop('metric_ext_id')

    ctx.invoke(stackmonitoring_cli.delete_metric_extension, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.disable_metric_extension, params_to_exclude=['metric_extension_id'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.disable_metric_extension.name, help=stackmonitoring_cli.disable_metric_extension.help)
@cli_util.option('--metric-ext-id', required=True, help=u"""The [OCID] of the metric extension resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'resource-ids': {'module': 'stack_monitoring', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def disable_metric_extension_extended(ctx, **kwargs):

    if 'metric_ext_id' in kwargs:
        kwargs['metric_extension_id'] = kwargs['metric_ext_id']
        kwargs.pop('metric_ext_id')

    ctx.invoke(stackmonitoring_cli.disable_metric_extension, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.enable_metric_extension, params_to_exclude=['metric_extension_id'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.enable_metric_extension.name, help=stackmonitoring_cli.enable_metric_extension.help)
@cli_util.option('--metric-ext-id', required=True, help=u"""The [OCID] of the metric extension resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'resource-ids': {'module': 'stack_monitoring', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def enable_metric_extension_extended(ctx, **kwargs):

    if 'metric_ext_id' in kwargs:
        kwargs['metric_extension_id'] = kwargs['metric_ext_id']
        kwargs.pop('metric_ext_id')

    ctx.invoke(stackmonitoring_cli.enable_metric_extension, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.export_metric_extension, params_to_exclude=['metric_extension_id'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.export_metric_extension.name, help=stackmonitoring_cli.export_metric_extension.help)
@cli_util.option('--metric-ext-id', required=True, help=u"""The [OCID] of the metric extension resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def export_metric_extension_extended(ctx, **kwargs):

    if 'metric_ext_id' in kwargs:
        kwargs['metric_extension_id'] = kwargs['metric_ext_id']
        kwargs.pop('metric_ext_id')

    ctx.invoke(stackmonitoring_cli.export_metric_extension, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.get_metric_extension, params_to_exclude=['metric_extension_id'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.get_metric_extension.name, help=stackmonitoring_cli.get_metric_extension.help)
@cli_util.option('--metric-ext-id', required=True, help=u"""The [OCID] of the metric extension resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'MetricExtension'})
@cli_util.wrap_exceptions
def get_metric_extension_extended(ctx, **kwargs):

    if 'metric_ext_id' in kwargs:
        kwargs['metric_extension_id'] = kwargs['metric_ext_id']
        kwargs.pop('metric_ext_id')

    ctx.invoke(stackmonitoring_cli.get_metric_extension, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.publish_metric_extension, params_to_exclude=['metric_extension_id'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.publish_metric_extension.name, help=stackmonitoring_cli.publish_metric_extension.help)
@cli_util.option('--metric-ext-id', required=True, help=u"""The [OCID] of the metric extension resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'stack_monitoring', 'class': 'MetricExtension'})
@cli_util.wrap_exceptions
def publish_metric_extension_extended(ctx, **kwargs):

    if 'metric_ext_id' in kwargs:
        kwargs['metric_extension_id'] = kwargs['metric_ext_id']
        kwargs.pop('metric_ext_id')

    ctx.invoke(stackmonitoring_cli.publish_metric_extension, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.test_metric_extension, params_to_exclude=['metric_extension_id'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.test_metric_extension.name, help=stackmonitoring_cli.test_metric_extension.help)
@cli_util.option('--metric-ext-id', required=True, help=u"""The [OCID] of the metric extension resource. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'resource-ids': {'module': 'stack_monitoring', 'class': 'list[string]'}}, output_type={'module': 'stack_monitoring', 'class': 'TestMetricExtensionData'})
@cli_util.wrap_exceptions
def test_metric_extension_extended(ctx, **kwargs):

    if 'metric_ext_id' in kwargs:
        kwargs['metric_extension_id'] = kwargs['metric_ext_id']
        kwargs.pop('metric_ext_id')

    ctx.invoke(stackmonitoring_cli.test_metric_extension, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.update_metric_extension, params_to_exclude=['metric_extension_id', 'collection_recurrences'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.update_metric_extension.name, help=stackmonitoring_cli.update_metric_extension.help)
@cli_util.option('--metric-ext-id', required=True, help=u"""The [OCID] of the metric extension resource. [required]""")
@cli_util.option('--collection-schedule', help=u"""Schedule of metric extension should use RFC 5545 format -> recur-rule-part = "FREQ";"INTERVAL" where FREQ rule part identifies the type of recurrence rule. Valid values are "MINUTELY","HOURLY","DAILY" to specify repeating events based on an interval of a minute, an hour and a day or more. Example- FREQ=DAILY;INTERVAL=1""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metric-list': {'module': 'stack_monitoring', 'class': 'list[Metric]'}, 'query-properties': {'module': 'stack_monitoring', 'class': 'MetricExtensionUpdateQueryProperties'}}, output_type={'module': 'stack_monitoring', 'class': 'MetricExtension'})
@cli_util.wrap_exceptions
def update_metric_extension_extended(ctx, **kwargs):

    if 'metric_ext_id' in kwargs:
        kwargs['metric_extension_id'] = kwargs['metric_ext_id']
        kwargs.pop('metric_ext_id')

    if 'collection_schedule' in kwargs:
        kwargs['collection_recurrences'] = kwargs['collection_schedule']
        kwargs.pop('collection_schedule')

    ctx.invoke(stackmonitoring_cli.update_metric_extension, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.update_metric_extension_jmx_update_query_properties, params_to_exclude=['metric_extension_id', 'query_properties_jmx_attributes', 'query_properties_managed_bean_query', 'collection_recurrences', 'query_properties_auto_row_prefix', 'query_properties_identity_metric', 'query_properties_is_metric_service_enabled'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.update_metric_extension_jmx_update_query_properties.name, help=stackmonitoring_cli.update_metric_extension_jmx_update_query_properties.help)
@cli_util.option('--metric-ext-id', required=True, help=u"""The [OCID] of the metric extension resource. [required]""")
@cli_util.option('--jmx-attributes', help=u"""List of JMX attributes or Metric Service Table columns separated by semi-colon""")
@cli_util.option('--managed-bean-query', help=u"""JMX Managed Bean Query or Metric Service Table name""")
@cli_util.option('--collection-schedule', help=u"""Schedule of metric extension should use RFC 5545 format -> recur-rule-part = "FREQ";"INTERVAL" where FREQ rule part identifies the type of recurrence rule. Valid values are "MINUTELY","HOURLY","DAILY" to specify repeating events based on an interval of a minute, an hour and a day or more. Example- FREQ=DAILY;INTERVAL=1""")
@cli_util.option('--auto-row-prefix', help=u"""Prefix for an auto generated metric, in case multiple rows with non unique key values are returned""")
@cli_util.option('--identity-metric', help=u"""Semi-colon separated list of key properties from Managed Bean ObjectName to be used as key metrics""")
@cli_util.option('--is-metric-service-enabled', type=click.BOOL, help=u"""Indicates if Metric Service is enabled on server domain""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metric-list': {'module': 'stack_monitoring', 'class': 'list[Metric]'}}, output_type={'module': 'stack_monitoring', 'class': 'MetricExtension'})
@cli_util.wrap_exceptions
def update_metric_extension_jmx_update_query_properties_extended(ctx, **kwargs):

    if 'metric_ext_id' in kwargs:
        kwargs['metric_extension_id'] = kwargs['metric_ext_id']
        kwargs.pop('metric_ext_id')

    if 'jmx_attributes' in kwargs:
        kwargs['query_properties_jmx_attributes'] = kwargs['jmx_attributes']
        kwargs.pop('jmx_attributes')

    if 'managed_bean_query' in kwargs:
        kwargs['query_properties_managed_bean_query'] = kwargs['managed_bean_query']
        kwargs.pop('managed_bean_query')

    if 'collection_schedule' in kwargs:
        kwargs['collection_recurrences'] = kwargs['collection_schedule']
        kwargs.pop('collection_schedule')

    if 'auto_row_prefix' in kwargs:
        kwargs['query_properties_auto_row_prefix'] = kwargs['auto_row_prefix']
        kwargs.pop('auto_row_prefix')

    if 'identity_metric' in kwargs:
        kwargs['query_properties_identity_metric'] = kwargs['identity_metric']
        kwargs.pop('identity_metric')

    if 'is_metric_service_enabled' in kwargs:
        kwargs['query_properties_is_metric_service_enabled'] = kwargs['is_metric_service_enabled']
        kwargs.pop('is_metric_service_enabled')

    ctx.invoke(stackmonitoring_cli.update_metric_extension_jmx_update_query_properties, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.update_metric_extension_os_command_update_query_properties, params_to_exclude=['metric_extension_id', 'query_properties_command', 'query_properties_delimiter', 'collection_recurrences', 'query_properties_arguments', 'query_properties_script_details', 'query_properties_starts_with'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.update_metric_extension_os_command_update_query_properties.name, help=stackmonitoring_cli.update_metric_extension_os_command_update_query_properties.help)
@cli_util.option('--metric-ext-id', required=True, help=u"""The [OCID] of the metric extension resource. [required]""")
@cli_util.option('--command', help=u"""OS command to execute without arguments""")
@cli_util.option('--delimiter', help=u"""Character used to delimit multiple metric values in single line of output""")
@cli_util.option('--collection-schedule', help=u"""Schedule of metric extension should use RFC 5545 format -> recur-rule-part = "FREQ";"INTERVAL" where FREQ rule part identifies the type of recurrence rule. Valid values are "MINUTELY","HOURLY","DAILY" to specify repeating events based on an interval of a minute, an hour and a day or more. Example- FREQ=DAILY;INTERVAL=1""")
@cli_util.option('--arguments', help=u"""Arguments required by either command or script""")
@cli_util.option('--script-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--starts-with', help=u"""String prefix used to identify metric output of the OS Command""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metric-list': {'module': 'stack_monitoring', 'class': 'list[Metric]'}, 'script-details': {'module': 'stack_monitoring', 'class': 'ScriptFileDetails'}}, output_type={'module': 'stack_monitoring', 'class': 'MetricExtension'})
@cli_util.wrap_exceptions
def update_metric_extension_os_command_update_query_properties_extended(ctx, **kwargs):

    if 'metric_ext_id' in kwargs:
        kwargs['metric_extension_id'] = kwargs['metric_ext_id']
        kwargs.pop('metric_ext_id')

    if 'command' in kwargs:
        kwargs['query_properties_command'] = kwargs['command']
        kwargs.pop('command')

    if 'delimiter' in kwargs:
        kwargs['query_properties_delimiter'] = kwargs['delimiter']
        kwargs.pop('delimiter')

    if 'collection_schedule' in kwargs:
        kwargs['collection_recurrences'] = kwargs['collection_schedule']
        kwargs.pop('collection_schedule')

    if 'arguments' in kwargs:
        kwargs['query_properties_arguments'] = kwargs['arguments']
        kwargs.pop('arguments')

    if 'script_details' in kwargs:
        kwargs['query_properties_script_details'] = kwargs['script_details']
        kwargs.pop('script_details')

    if 'starts_with' in kwargs:
        kwargs['query_properties_starts_with'] = kwargs['starts_with']
        kwargs.pop('starts_with')

    ctx.invoke(stackmonitoring_cli.update_metric_extension_os_command_update_query_properties, **kwargs)


@cli_util.copy_params_from_generated_command(stackmonitoring_cli.update_metric_extension_sql_update_query_properties, params_to_exclude=['metric_extension_id', 'query_properties_sql_details', 'query_properties_sql_type', 'collection_recurrences', 'query_properties_in_param_details', 'query_properties_out_param_details'])
@stackmonitoring_cli.metric_extension_group.command(name=stackmonitoring_cli.update_metric_extension_sql_update_query_properties.name, help=stackmonitoring_cli.update_metric_extension_sql_update_query_properties.help)
@cli_util.option('--metric-ext-id', required=True, help=u"""The [OCID] of the metric extension resource. [required]""")
@cli_util.option('--sql-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--sql-type', type=custom_types.CliCaseInsensitiveChoice(["STATEMENT", "SQL_SCRIPT"]), help=u"""Type of SQL data collection method i.e. either a Statement or SQL Script File""")
@cli_util.option('--collection-schedule', help=u"""Schedule of metric extension should use RFC 5545 format -> recur-rule-part = "FREQ";"INTERVAL" where FREQ rule part identifies the type of recurrence rule. Valid values are "MINUTELY","HOURLY","DAILY" to specify repeating events based on an interval of a minute, an hour and a day or more. Example- FREQ=DAILY;INTERVAL=1""")
@cli_util.option('--in-param-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of values and position of PL/SQL procedure IN parameters

This option is a JSON list with items of type SqlInParamDetails.  For documentation on SqlInParamDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/stackmonitoring/20210330/datatypes/SqlInParamDetails.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--out-param-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metric-list': {'module': 'stack_monitoring', 'class': 'list[Metric]'}, 'sql-details': {'module': 'stack_monitoring', 'class': 'SqlDetails'}, 'in-param-details': {'module': 'stack_monitoring', 'class': 'list[SqlInParamDetails]'}, 'out-param-details': {'module': 'stack_monitoring', 'class': 'SqlOutParamDetails'}}, output_type={'module': 'stack_monitoring', 'class': 'MetricExtension'})
@cli_util.wrap_exceptions
def update_metric_extension_sql_update_query_properties_extended(ctx, **kwargs):

    if 'metric_ext_id' in kwargs:
        kwargs['metric_extension_id'] = kwargs['metric_ext_id']
        kwargs.pop('metric_ext_id')

    if 'sql_details' in kwargs:
        kwargs['query_properties_sql_details'] = kwargs['sql_details']
        kwargs.pop('sql_details')

    if 'sql_type' in kwargs:
        kwargs['query_properties_sql_type'] = kwargs['sql_type']
        kwargs.pop('sql_type')

    if 'collection_schedule' in kwargs:
        kwargs['collection_recurrences'] = kwargs['collection_schedule']
        kwargs.pop('collection_schedule')

    if 'in_param_details' in kwargs:
        kwargs['query_properties_in_param_details'] = kwargs['in_param_details']
        kwargs.pop('in_param_details')

    if 'out_param_details' in kwargs:
        kwargs['query_properties_out_param_details'] = kwargs['out_param_details']
        kwargs.pop('out_param_details')

    ctx.invoke(stackmonitoring_cli.update_metric_extension_sql_update_query_properties, **kwargs)


# oci stack-monitoring process-set-collection list-process-sets -> oci stack-monitoring process-set-collection list
cli_util.rename_command(stackmonitoring_cli, stackmonitoring_cli.process_set_collection_group, stackmonitoring_cli.list_process_sets, "list")


# Remove process-set-collection from oci stack-monitoring
stackmonitoring_cli.stack_monitoring_root_group.commands.pop(stackmonitoring_cli.process_set_collection_group.name)


# oci stack-monitoring process-set-collection list-process-sets -> oci stack-monitoring process-set
stackmonitoring_cli.process_set_collection_group.commands.pop(stackmonitoring_cli.list_process_sets.name)
stackmonitoring_cli.process_set_group.add_command(stackmonitoring_cli.list_process_sets)
