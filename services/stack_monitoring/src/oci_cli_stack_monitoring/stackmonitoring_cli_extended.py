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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'db-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'credentials': {'module': 'stack_monitoring', 'class': 'MonitoredResourceCredential'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}})
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'stack_monitoring', 'class': 'list[MonitoredResourceProperty]'}, 'db-connection-details': {'module': 'stack_monitoring', 'class': 'ConnectionDetails'}, 'credentials': {'module': 'stack_monitoring', 'class': 'MonitoredResourceCredential'}, 'aliases': {'module': 'stack_monitoring', 'class': 'MonitoredResourceAliasCredential'}})
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
