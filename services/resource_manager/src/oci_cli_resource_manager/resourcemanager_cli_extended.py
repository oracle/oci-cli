# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
import os
import os.path
import six
import sys
from services.resource_manager.src.oci_cli_resource_manager.generated import resourcemanager_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
import oci  # noqa: F401
import base64
import zipfile

resourcemanager_cli.stack_group.commands.pop(resourcemanager_cli.create_stack.name)
resourcemanager_cli.stack_group.commands.pop(resourcemanager_cli.update_stack.name)

# Disabling nested polymorphic commands:
resourcemanager_cli.stack_group.commands.pop(resourcemanager_cli.create_stack_create_zip_upload_config_source_details.name)
resourcemanager_cli.stack_group.commands.pop(resourcemanager_cli.update_stack_update_zip_upload_config_source_details.name)


def create_base64encoded_zip(config_source):
    if config_source.endswith(".zip") and os.path.isfile(config_source) and zipfile.is_zipfile(config_source):
        with open(config_source, mode='rb') as zip_file:
            return base64.b64encode(zip_file.read()).decode('utf-8')


def create_base64encoded_tf_state(tf_state):
    if os.path.isfile(tf_state):
        with open(tf_state, mode='rb') as tf_state_file:
            return base64.b64encode(tf_state_file.read()).decode('utf-8')


@cli_util.copy_params_from_generated_command(resourcemanager_cli.create_stack, params_to_exclude=['config_source'])
@resourcemanager_cli.stack_group.command(name=cli_util.override('create_stack.command_name', 'create'), help="""Creates a Stack""")
@cli_util.option('--config-source', required=True, help="""A Terraform configuration .zip file.""")
@cli_util.option('--working-directory', help=""" The path of the directory from which to run terraform. If not specified the root will be used.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def create_stack_extended(ctx, config_source, working_directory, **kwargs):

    config_source = os.path.expandvars(os.path.expanduser(config_source))
    if not os.path.exists(config_source):
        click.echo('Config source does not exist', file=sys.stderr)
        ctx.abort()

    if not (config_source.endswith(".zip") and os.path.isfile(config_source) and zipfile.is_zipfile(config_source)):
        click.echo('Config source must be a .zip file.', file=sys.stderr)
        ctx.abort()

    send_value = create_base64encoded_zip(config_source)
    if not send_value:
        click.echo('Internal error: Unable to generate encoded zip', file=sys.stderr)
        ctx.abort()

    kwargs['config_source'] = {
        'configSourceType': oci.resource_manager.models.ConfigSource.CONFIG_SOURCE_TYPE_ZIP_UPLOAD,
        'zipFileBase64Encoded': send_value}

    if working_directory is not None:
        kwargs['config_source']['workingDirectory'] = working_directory

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)
    ctx.invoke(resourcemanager_cli.create_stack, **kwargs)


@cli_util.copy_params_from_generated_command(resourcemanager_cli.update_stack, params_to_exclude=['config_source'])
@resourcemanager_cli.stack_group.command(name=cli_util.override('update_stack.command_name', 'update'), help="""Update the Stack object""")
@cli_util.option('--config-source', help="""A Terraform configuration .zip file.""")
@cli_util.option('--working-directory', help=""" The path of the directory from which to run terraform. If not specified the root will be used.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'reseouce_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def update_stack_extended(ctx, config_source, working_directory, **kwargs):

    if working_directory is not None or config_source is not None:
        kwargs['config_source'] = {'configSourceType': oci.resource_manager.models.ConfigSource.CONFIG_SOURCE_TYPE_ZIP_UPLOAD}

        if working_directory is not None:
            kwargs['config_source']['workingDirectory'] = working_directory

        if config_source is not None:
            config_source = os.path.expandvars(os.path.expanduser(config_source))
            if not os.path.exists(config_source):
                click.echo('Config source does not exist', file=sys.stderr)
                ctx.abort()

            if not (config_source.endswith(".zip") and os.path.isfile(config_source) and zipfile.is_zipfile(config_source)):
                click.echo('Config source must be a .zip file.', file=sys.stderr)
                ctx.abort()

            send_value = create_base64encoded_zip(config_source)
            if not send_value:
                click.echo('Internal error: Unable to generate encoded zip', file=sys.stderr)
                ctx.abort()

            kwargs['config_source']['zipFileBase64Encoded'] = send_value

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)
    ctx.invoke(resourcemanager_cli.update_stack, **kwargs)


# Overriding polymorphic sub commands of create job to shorten the names of the commands and remove redundant parameters
# For final design adn full review see:
# https://jira.oci.oraclecorp.com/browse/DEX-6309?focusedCommentId=1406256&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#comment-1406256

# Plan operation
# Removes create_job_create_plan_job_operation_details from CLI
resourcemanager_cli.job_group.commands.pop(resourcemanager_cli.create_job_create_plan_job_operation_details.name)


# params_to_exclude will remove unwanted params
@cli_util.copy_params_from_generated_command(resourcemanager_cli.create_job_create_plan_job_operation_details, params_to_exclude=['operation', 'apply_job_plan_resolution'])
# Create a new command with name 'create-plan-job'
@resourcemanager_cli.job_group.command(name='create-plan-job', help=resourcemanager_cli.create_job_create_plan_job_operation_details.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_plan_job(ctx, **kwargs):
    # invoke generated command.
    ctx.invoke(resourcemanager_cli.create_job_create_plan_job_operation_details, **kwargs)


# Apply operation
# Removes create_job_create_apply_job_operation_details from CLI
resourcemanager_cli.job_group.commands.pop(resourcemanager_cli.create_job_create_apply_job_operation_details.name)


# params_to_exclude will remove unwanted params
@cli_util.copy_params_from_generated_command(resourcemanager_cli.create_job_create_apply_job_operation_details, params_to_exclude=['job_operation_details_execution_plan_strategy', 'job_operation_details_execution_plan_job_id', 'operation', 'apply_job_plan_resolution'])
# Create a new command with name 'create-apply-job'
@resourcemanager_cli.job_group.command(name='create-apply-job', help=resourcemanager_cli.create_job_create_apply_job_operation_details.help)
# New/Renamed options
@cli_util.option('--execution-plan-job-id', help=u"""Specifies the source of the execution plan to apply. Use `AUTO_APPROVED` to run the job without an execution plan.""")
@cli_util.option('--execution-plan-strategy', required=True, help=u"""The OCID of a plan job, for use when specifying `FROM_PLAN_JOB_ID` as the `executionPlanStrategy`.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_apply_job(ctx, **kwargs):
    # Extract the renamed options and construct original options.
    if 'execution_plan_strategy' in kwargs:
        kwargs['job_operation_details_execution_plan_strategy'] = kwargs['execution_plan_strategy']
        del kwargs['execution_plan_strategy']
    if 'execution_plan_job_id' in kwargs:
        kwargs['job_operation_details_execution_plan_job_id'] = kwargs['execution_plan_job_id']
        del kwargs['execution_plan_job_id']

    # invoke generated command.
    ctx.invoke(resourcemanager_cli.create_job_create_apply_job_operation_details, **kwargs)


# Destroy operation
# Removes create_job_create_destroy_job_operation_details from CLI
resourcemanager_cli.job_group.commands.pop(resourcemanager_cli.create_job_create_destroy_job_operation_details.name)


# params_to_exclude will remove unwanted params
@cli_util.copy_params_from_generated_command(resourcemanager_cli.create_job_create_destroy_job_operation_details, params_to_exclude=['job_operation_details_execution_plan_strategy', 'operation', 'apply_job_plan_resolution'])
# Create a new command with name 'create-destroy-job'
@resourcemanager_cli.job_group.command(name='create-destroy-job', help=resourcemanager_cli.create_job_create_destroy_job_operation_details.help)
# New/Renamed options
@cli_util.option('--execution-plan-strategy', required=True, help=u"""Specifies the source of the execution plan to apply. Currently, only `AUTO_APPROVED` is allowed, which indicates that the job will be run without an execution plan.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_destroy_job(ctx, **kwargs):
    # Extract the renamed options and construct original options.
    if 'execution_plan_strategy' in kwargs:
        kwargs['job_operation_details_execution_plan_strategy'] = kwargs['execution_plan_strategy']
        del kwargs['execution_plan_strategy']

    # invoke generated command.
    ctx.invoke(resourcemanager_cli.create_job_create_destroy_job_operation_details, **kwargs)


# Import TF State operation
# Removes create_job_create_import_tf_state_job_operation_details from CLI
resourcemanager_cli.job_group.commands.pop(resourcemanager_cli.create_job_create_import_tf_state_job_operation_details.name)


# params_to_exclude will remove unwanted params
@cli_util.copy_params_from_generated_command(resourcemanager_cli.create_job_create_import_tf_state_job_operation_details, params_to_exclude=['job_operation_details_tf_state_base64_encoded', 'operation', 'apply_job_plan_resolution'])
# Create a new command with name 'create-import-tf-state-job'
@resourcemanager_cli.job_group.command(name='create-import-tf-state-job', help=resourcemanager_cli.create_job_create_import_tf_state_job_operation_details.help)
# New/Renamed options
@cli_util.option('--tf-state-file', required=True, help=u"""Job details that are specific to import Terraform state operations.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_import_tf_state_job(ctx, **kwargs):
    # Extract the renamed options and construct original options.
    if 'tf_state_file' in kwargs:
        state_to_import = os.path.expandvars(os.path.expanduser(kwargs['tf_state_file']))
        if not os.path.exists(state_to_import):
            click.echo('tf state file does not exist', file=sys.stderr)
            ctx.abort()

        if not (os.path.isfile(state_to_import)):
            click.echo('tf state must be a file.', file=sys.stderr)
            ctx.abort()

        send_value = create_base64encoded_tf_state(state_to_import)
        if not send_value:
            click.echo('Internal error: Unable to generate encoded tf state', file=sys.stderr)
            ctx.abort()

        kwargs['job_operation_details_tf_state_base64_encoded'] = send_value
        del kwargs['tf_state_file']

    # invoke generated command.
    ctx.invoke(resourcemanager_cli.create_job_create_import_tf_state_job_operation_details, **kwargs)


# Add all pagination support for oci resource-manager job get-job-logs
@cli_util.copy_params_from_generated_command(resourcemanager_cli.get_job_logs, params_to_exclude=[])
@resourcemanager_cli.job_group.command(name='get-job-logs', help=resourcemanager_cli.get_job_logs.help)
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'list[LogEntry]'})
@cli_util.wrap_exceptions
def get_job_logs_extended(ctx, job_id, type, level_greater_than_or_equal_to, sort_order, limit, page, timestamp_greater_than_or_equal_to, timestamp_less_than_or_equal_to, all_pages, **kwargs):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if type is not None and len(type) > 0:
        kwargs['type'] = type
    if level_greater_than_or_equal_to is not None:
        kwargs['level_greater_than_or_equal_to'] = level_greater_than_or_equal_to
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if timestamp_greater_than_or_equal_to is not None:
        kwargs['timestamp_greater_than_or_equal_to'] = timestamp_greater_than_or_equal_to
    if timestamp_less_than_or_equal_to is not None:
        kwargs['timestamp_less_than_or_equal_to'] = timestamp_less_than_or_equal_to
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)

    if all_pages:
        result = cli_util.list_call_get_all_results(
            client.get_job_logs,
            job_id=job_id,
            **kwargs
        )
    # GetJobLogs operation already has built in support for limit
    else:
        result = client.get_job_logs(
            job_id=job_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


# Shorten stack commands based on compartment resource discovery
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.stack_group, resourcemanager_cli.create_stack_create_compartment_config_source_details, "create-from-compartment")

# Shorten stack commands based on Git provider
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.stack_group, resourcemanager_cli.create_stack_create_git_config_source_details, "create-from-git-provider")
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.stack_group, resourcemanager_cli.update_stack_update_git_config_source_details, "update-from-git-provider")

# Shorten configuration-source-provider commands based on Gitlab access token
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.configuration_source_provider_group, resourcemanager_cli.create_configuration_source_provider_create_gitlab_access_token_configuration_source_provider_details, "create-gitlab-access-token-provider")
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.configuration_source_provider_group, resourcemanager_cli.update_configuration_source_provider_update_gitlab_access_token_configuration_source_provider_details, "update-gitlab-access-token-provider")

# Move `configuration-source-provider-summary list-configuration-source-providers` to `configuration-source-provider list`
resourcemanager_cli.configuration_source_provider_summary_group.commands.pop(resourcemanager_cli.list_configuration_source_providers.name)
resourcemanager_cli.configuration_source_provider_group.add_command(resourcemanager_cli.list_configuration_source_providers)
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.configuration_source_provider_group, resourcemanager_cli.list_configuration_source_providers, "list")
resourcemanager_cli.resource_manager_root_group.commands.pop(resourcemanager_cli.configuration_source_provider_summary_group.name)

# Rename detect-stack-drift to detect-drift
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.stack_group, resourcemanager_cli.detect_stack_drift, "detect-drift")

# Move list-stack-resource-drift-details from stack-resource-drift-summary-group to stack-group
resourcemanager_cli.stack_resource_drift_summary_group.commands.pop(resourcemanager_cli.list_stack_resource_drift_details.name)
resourcemanager_cli.stack_group.add_command(resourcemanager_cli.list_stack_resource_drift_details)

# Rename list-stack-resource-drift-details to list-resource-drift-details
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.stack_group, resourcemanager_cli.list_stack_resource_drift_details, "list-resource-drift-details")

# Pop the stack_resource_drift_summary group
resourcemanager_cli.resource_manager_root_group.commands.pop(resourcemanager_cli.stack_resource_drift_summary_group.name)
