# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
import os
import os.path
import six
import sys
from services.resource_manager.src.oci_cli_resource_manager.generated import resourcemanager_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import cli_constants
from oci_cli import custom_types  # noqa: F401
import oci  # noqa: F401
import base64
import zipfile
from oci.regions import is_region
from oci.regions import get_realm_from_region

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


@cli_util.copy_params_from_generated_command(resourcemanager_cli.create_stack, params_to_exclude=['config_source', 'wait_for_state'])
@resourcemanager_cli.stack_group.command(name=cli_util.override('create_stack.command_name', 'create'), help="""Creates a Stack""")
@cli_util.option('--config-source', required=True, help="""A Terraform configuration .zip file.""")
@cli_util.option('--working-directory', help=""" The path of the directory from which to run terraform. If not specified the root will be used.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NOT_CHECKED", "IN_SYNC", "DRIFTED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def create_stack_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, config_source, display_name, description, variables, terraform_version, freeform_tags, defined_tags, working_directory, **kwargs):

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

    config_source = {
        'configSourceType': oci.resource_manager.models.ConfigSource.CONFIG_SOURCE_TYPE_ZIP_UPLOAD,
        'zipFileBase64Encoded': send_value}

    if working_directory is not None:
        config_source['workingDirectory'] = working_directory

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['configSource'] = cli_util.parse_json_parameter("config_source", config_source)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_stack(
        create_stack_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stack') and callable(getattr(client, 'get_stack')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo(
                    'Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state),
                    file=sys.stderr)
                result = oci.wait_until(client, client.get_stack(result.data.id),
                                        'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo(
                    'Failed to wait until the work request entered the specified state. Outputting last known resource state',
                    file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo(
                    'Encountered error while waiting for work request to enter the specified state. Outputting last known resource state',
                    file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(resourcemanager_cli.update_stack, params_to_exclude=['config_source'])
@resourcemanager_cli.stack_group.command(name=cli_util.override('update_stack.command_name', 'update'), help="""Update the Stack object""")
@cli_util.option('--config-source', help="""A Terraform configuration .zip file.""")
@cli_util.option('--working-directory', help=""" The path of the directory from which to run terraform. If not specified the root will be used.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'reseouce_manager', 'class': 'Stack'})
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
@cli_util.copy_params_from_generated_command(resourcemanager_cli.create_job_create_plan_job_operation_details, params_to_exclude=['operation', 'apply_job_plan_resolution', 'job_operation_details_terraform_advanced_options'])
# Create a new command with name 'create-plan-job'
@resourcemanager_cli.job_group.command(name='create-plan-job', help=resourcemanager_cli.create_job_create_plan_job_operation_details.help)
# New/Renamed options
@cli_util.option('--terraform-advanced-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Specifies advanced options for Terraform commands. These options are not necessary for normal usage of Terraform.\n""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_plan_job(ctx, **kwargs):
    # Extract the renamed options and construct original options.
    if 'terraform_advanced_options' in kwargs:
        kwargs['job_operation_details_terraform_advanced_options'] = kwargs['terraform_advanced_options']
        del kwargs['terraform_advanced_options']
    # invoke generated command.
    ctx.invoke(resourcemanager_cli.create_job_create_plan_job_operation_details, **kwargs)


# Apply operation
# Removes create_job_create_apply_job_operation_details from CLI
resourcemanager_cli.job_group.commands.pop(resourcemanager_cli.create_job_create_apply_job_operation_details.name)


# params_to_exclude will remove unwanted params
@cli_util.copy_params_from_generated_command(resourcemanager_cli.create_job_create_apply_job_operation_details, params_to_exclude=['job_operation_details_execution_plan_strategy', 'job_operation_details_execution_plan_job_id', 'operation', 'apply_job_plan_resolution', 'job_operation_details_terraform_advanced_options'])
# Create a new command with name 'create-apply-job'
@resourcemanager_cli.job_group.command(name='create-apply-job', help=resourcemanager_cli.create_job_create_apply_job_operation_details.help)
# New/Renamed options
@cli_util.option('--execution-plan-job-id', help=u"""Specifies the source of the execution plan to apply. Use `AUTO_APPROVED` to run the job without an execution plan.""")
@cli_util.option('--execution-plan-strategy', required=True, help=u"""The OCID of a plan job, for use when specifying `FROM_PLAN_JOB_ID` as the `executionPlanStrategy`.""")
@cli_util.option('--terraform-advanced-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Specifies advanced options for Terraform commands. These options are not necessary for normal usage of Terraform.\n""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
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
    if 'terraform_advanced_options' in kwargs:
        kwargs['job_operation_details_terraform_advanced_options'] = kwargs['terraform_advanced_options']
        del kwargs['terraform_advanced_options']

    # invoke generated command.
    ctx.invoke(resourcemanager_cli.create_job_create_apply_job_operation_details, **kwargs)


# Destroy operation
# Removes create_job_create_destroy_job_operation_details from CLI
resourcemanager_cli.job_group.commands.pop(resourcemanager_cli.create_job_create_destroy_job_operation_details.name)


# params_to_exclude will remove unwanted params
@cli_util.copy_params_from_generated_command(resourcemanager_cli.create_job_create_destroy_job_operation_details, params_to_exclude=['job_operation_details_execution_plan_strategy', 'operation', 'apply_job_plan_resolution', 'job_operation_details_terraform_advanced_options'])
# Create a new command with name 'create-destroy-job'
@resourcemanager_cli.job_group.command(name='create-destroy-job', help=resourcemanager_cli.create_job_create_destroy_job_operation_details.help)
# New/Renamed options
@cli_util.option('--execution-plan-strategy', required=True, help=u"""Specifies the source of the execution plan to apply. Currently, only `AUTO_APPROVED` is allowed, which indicates that the job will be run without an execution plan.""")
@cli_util.option('--terraform-advanced-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Specifies advanced options for Terraform commands. These options are not necessary for normal usage of Terraform.\n""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_destroy_job(ctx, **kwargs):
    # Extract the renamed options and construct original options.
    if 'execution_plan_strategy' in kwargs:
        kwargs['job_operation_details_execution_plan_strategy'] = kwargs['execution_plan_strategy']
        del kwargs['execution_plan_strategy']
    if 'terraform_advanced_options' in kwargs:
        kwargs['job_operation_details_terraform_advanced_options'] = kwargs['terraform_advanced_options']
        del kwargs['terraform_advanced_options']

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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
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

# Shorten configuration-source-provider commands based on Github access token
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.configuration_source_provider_group, resourcemanager_cli.create_configuration_source_provider_create_github_access_token_configuration_source_provider_details, "create-github-access-token-provider")
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.configuration_source_provider_group, resourcemanager_cli.update_configuration_source_provider_update_github_access_token_configuration_source_provider_details, "update-github-access-token-provider")

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

# Shorten stack commands based for object storage
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.stack_group, resourcemanager_cli.create_stack_create_object_storage_config_source_details, "create-from-object-storage")
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.stack_group, resourcemanager_cli.update_stack_update_object_storage_config_source_details, "update-from-object-storage")

# oci resource-manager stack create-stack-create-stack-template-config-source-details -> oci resource-manager stack create-from-template
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.stack_group, resourcemanager_cli.create_stack_create_stack_template_config_source_details, "create-from-template")


# oci resource-manager template create-template-create-template-zip-upload-config-source-details -> oci resource-manager template create
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.template_group, resourcemanager_cli.create_template_create_template_zip_upload_config_source_details, "create")


# oci resource-manager template update-template-update-template-zip-upload-config-source-details -> oci resource-manager template update
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.template_group, resourcemanager_cli.update_template_update_template_zip_upload_config_source_details, "update")


# Remove create from oci resource-manager template
resourcemanager_cli.template_group.commands.pop(resourcemanager_cli.create_template.name)


# Remove update from oci resource-manager template
resourcemanager_cli.template_group.commands.pop(resourcemanager_cli.update_template.name)


# Move commands under 'oci resource-manager template-category-summary' -> 'oci resource-manager template'
resourcemanager_cli.resource_manager_root_group.commands.pop(resourcemanager_cli.template_category_summary_group.name)
resourcemanager_cli.template_group.add_command(resourcemanager_cli.list_template_categories)


@cli_util.copy_params_from_generated_command(resourcemanager_cli.create_stack_create_stack_template_config_source_details, params_to_exclude=['config_source_template_id', 'config_source_working_directory'])
@resourcemanager_cli.stack_group.command(name=resourcemanager_cli.create_stack_create_stack_template_config_source_details.name, help=resourcemanager_cli.create_stack_create_stack_template_config_source_details.help)
@cli_util.option('--template-id', required=True, help=u"""[required]""")
@cli_util.option('--working-directory', help=u"""File path to the directory from which Terraform runs. If not specified, the root directory is used. This parameter is ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def create_stack_create_stack_template_config_source_details_extended(ctx, **kwargs):
    if 'template_id' in kwargs:
        kwargs['config_source_template_id'] = kwargs['template_id']
        kwargs.pop('template_id')

    if 'working_directory' in kwargs:
        kwargs['config_source_working_directory'] = kwargs['working_directory']
        kwargs.pop('working_directory')

    ctx.invoke(resourcemanager_cli.create_stack_create_stack_template_config_source_details, **kwargs)


@cli_util.copy_params_from_generated_command(resourcemanager_cli.create_template_create_template_zip_upload_config_source_details, params_to_exclude=['logo_file_base64_encoded', 'template_config_source_zip_file_base64_encoded'])
@resourcemanager_cli.template_group.command(name=resourcemanager_cli.create_template_create_template_zip_upload_config_source_details.name, help=resourcemanager_cli.create_template_create_template_zip_upload_config_source_details.help)
@cli_util.option('--logo-file', help=u"""Base64-encoded logo for the template.""")
@cli_util.option('--config-source', required=True, help=u"""[required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Template'})
@cli_util.wrap_exceptions
def create_template_create_template_zip_upload_config_source_details_extended(ctx, **kwargs):
    if 'logo_file' in kwargs:
        kwargs['logo_file_base64_encoded'] = kwargs['logo_file']
        kwargs.pop('logo_file')

    if 'config_source' in kwargs:
        kwargs['template_config_source_zip_file_base64_encoded'] = kwargs['config_source']
        kwargs.pop('config_source')

    ctx.invoke(resourcemanager_cli.create_template_create_template_zip_upload_config_source_details, **kwargs)


@cli_util.copy_params_from_generated_command(resourcemanager_cli.update_template_update_template_zip_upload_config_source_details, params_to_exclude=['logo_file_base64_encoded', 'template_config_source_zip_file_base64_encoded'])
@resourcemanager_cli.template_group.command(name=resourcemanager_cli.update_template_update_template_zip_upload_config_source_details.name, help=resourcemanager_cli.update_template_update_template_zip_upload_config_source_details.help)
@cli_util.option('--logo-file', help=u"""Base64-encoded logo for the template.""")
@cli_util.option('--config-source', help=u"""""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Template'})
@cli_util.wrap_exceptions
def update_template_update_template_zip_upload_config_source_details_extended(ctx, **kwargs):
    if 'logo_file' in kwargs:
        kwargs['logo_file_base64_encoded'] = kwargs['logo_file']
        kwargs.pop('logo_file')

    if 'config_source' in kwargs:
        kwargs['template_config_source_zip_file_base64_encoded'] = kwargs['config_source']
        kwargs.pop('config_source')

    ctx.invoke(resourcemanager_cli.update_template_update_template_zip_upload_config_source_details, **kwargs)


@resourcemanager_cli.stack_group.command(name='copy', help=u"""Creates a copy of the specified stack in the specified destination (compartment and region). Note: The access token is required when copying a stack that uses a Git configuration source provider to a different region. For more information, see [To copy a stack]. \n[Command Reference](copyStack)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@cli_util.option('--destination-compartment-id', help=u"""The [OCID] of the destination compartment for the copied stack.""")
@cli_util.option('--destination-region', help=u"""The destination region for the copied stack.""")
@cli_util.option('--display-name', help=u"""The display name to use for the copied stack.""")
@cli_util.option('--description', help=u"""The description to use for the copied stack.""")
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. Maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 4096 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags associated with this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--access-token', help=u"""The personal access token for the Git repository. Required when copying a stack that uses a Git configuration source provider to a different region. Avoid entering confidential information. For more information, see [To copy a stack]. \n[Command Reference](copyStack)""")
@json_skeleton_utils.get_cli_json_input_option({'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def copy_stack(ctx, from_json, stack_id, destination_region, destination_compartment_id, display_name, description, freeform_tags, defined_tags, variables, access_token):

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')

    if destination_region is not None and not is_region(destination_region):
        raise click.UsageError("Unrecognized region: {}. Review valid regions at https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm".format(destination_region))

    inner_kwargs = {}
    inner_kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)

    # GET Stack
    source_stack_response = client.get_stack(
        stack_id=stack_id,
        **inner_kwargs
    )

    source_region = ctx.obj['config']['region']
    if destination_region is not None and get_realm_from_region(destination_region) != get_realm_from_region(source_region):
        raise click.UsageError("Invalid region. Destination region must be in the same realm {}. Review valid regions at https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm".format(destination_region))

    copy_display_name_prefix = "[copy-from-" + source_region + "]-"

    if destination_region is not None and destination_region == source_region:
        destination_region = None

    # Prepare Stack Metadata
    if source_stack_response is None or source_stack_response.data is None:
        raise Exception("Could not retrieve stack object", inner_kwargs['opc_request_id'])

    source_stack = source_stack_response.data
    _details = copy_stack_metadata(source_stack, destination_compartment_id, display_name, description, freeform_tags, defined_tags, variables, copy_display_name_prefix)

    # get config source metadata for stack
    _details['configSource'] = get_config_source_metadata_for_stack(source_stack, destination_region, access_token)

    is_zip_upload = source_stack.config_source.config_source_type == oci.resource_manager.models.ConfigSource.CONFIG_SOURCE_TYPE_ZIP_UPLOAD or source_stack.config_source.config_source_type == oci.resource_manager.models.ConfigSource.CONFIG_SOURCE_TYPE_COMPARTMENT_CONFIG_SOURCE

    is_git_config = source_stack.config_source.config_source_type == oci.resource_manager.models.ConfigSource.CONFIG_SOURCE_TYPE_GIT_CONFIG_SOURCE

    if not is_zip_upload and not is_git_config:
        raise Exception("Only zip-upload config, git-configuration-source and create-from-compartment stacks are supported for copy stack", inner_kwargs['opc_request_id'])

    # GET TF Config
    if is_zip_upload:
        stack_tf_config_response = client.get_stack_tf_config(
            stack_id=stack_id,
            **inner_kwargs
        )

        if stack_tf_config_response is None or stack_tf_config_response.data is None:
            raise Exception("Could not retrieve stack TF config", inner_kwargs['opc_request_id'])

        base64encoded_stack_tf_config = get_source_stack_tf_config_base64encoded_zip(stack_id, stack_tf_config_response)
        _details['configSource']['zipFileBase64Encoded'] = base64encoded_stack_tf_config

    # Setup Cross region
    if destination_region is not None and is_git_config:
        _get_config_details = {}

        # GET config source provider
        get_config_source_provider_response = client.get_configuration_source_provider(
            configuration_source_provider_id=source_stack.config_source.configuration_source_provider_id,
            **inner_kwargs
        )

        if get_config_source_provider_response is None or get_config_source_provider_response.data is None:
            raise Exception("Unable to get git config source provider", inner_kwargs['opc_request_id'])

        _get_config_details.update(copy_git_config_source_provider_metadata(get_config_source_provider_response.data, access_token, copy_display_name_prefix))

        # Change region
        client.base_client.set_region(destination_region)

        # CREATE config source provider in new region
        create_config_source_provider_response = client.create_configuration_source_provider(
            create_configuration_source_provider_details=_get_config_details,
            **inner_kwargs
        )

        if create_config_source_provider_response is None or create_config_source_provider_response.data is None:
            raise Exception("Unable to copy Git configuration source provider", inner_kwargs['opc_request_id'])

        cli_util.render_response(create_config_source_provider_response, ctx)
        _details['configSource']['configurationSourceProviderId'] = create_config_source_provider_response.data.id
    elif destination_region is not None:
        # Change region
        client.base_client.set_region(destination_region)

    try:
        # CREATE stack
        result = client.create_stack(
            create_stack_details=_details,
            **inner_kwargs
        )
        cli_util.render_response(result, ctx)
    except Exception as e:
        print("Failed to copy stack: ", stack_id)
        print(e)
        if destination_region is not None and is_git_config:
            print("Deleting copied configuration source provider: ", create_config_source_provider_response.data.id)

            # delete config source provider
            delete_config_source = client.delete_configuration_source_provider(
                configuration_source_provider_id=create_config_source_provider_response.data.id,
                **inner_kwargs
            )


def get_config_source_metadata_for_stack(source_stack, destination_region, access_token):
    _details = {}

    # GIT CONFIG SOURCE PROVIDER
    if source_stack.config_source.config_source_type == oci.resource_manager.models.ConfigSource.CONFIG_SOURCE_TYPE_GIT_CONFIG_SOURCE:
        if destination_region is not None and access_token is None:
            raise click.UsageError("Need access token for Git configuration source provider to copy the stack across regions")

        if destination_region is None:
            _details['configurationSourceProviderId'] = source_stack.config_source.configuration_source_provider_id

        _details['workingDirectory'] = source_stack.config_source.working_directory
        _details['repositoryUrl'] = source_stack.config_source.repository_url
        _details['branchName'] = source_stack.config_source.branch_name
        _details['configSourceType'] = oci.resource_manager.models.ConfigSource.CONFIG_SOURCE_TYPE_GIT_CONFIG_SOURCE

    # ZIP CONFIG SOURCE or RESOURCE DISCOVERY
    else:
        _details['workingDirectory'] = source_stack.config_source.working_directory
        _details['configSourceType'] = oci.resource_manager.models.ConfigSource.CONFIG_SOURCE_TYPE_ZIP_UPLOAD

    return _details


def copy_stack_metadata(source_stack_data, compartment_id, display_name, description, freeform_tags, defined_tags, variables, copy_prefix_name):
    _details = {}

    # Get non-mutable Stack Metadata
    _details['terraformVersion'] = source_stack_data.terraform_version

    # Get Optional parameters
    if display_name is not None:
        _details['displayName'] = display_name
    else:
        _details['displayName'] = copy_prefix_name + source_stack_data.display_name

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id
    else:
        _details['compartmentId'] = source_stack_data.compartment_id

    if description is not None:
        _details['description'] = description
    else:
        _details['description'] = source_stack_data.description

    # freeformTags
    merged_freeform_tags = merge_tags_variables(source_stack_data.freeform_tags, freeform_tags, "freeform_tags")
    _details['freeformTags'] = merged_freeform_tags

    # definedTags
    merged_defined_tags = merge_tags_variables(source_stack_data.defined_tags, defined_tags, "defined_tags")
    _details['definedTags'] = merged_defined_tags

    # variables
    merged_variables = merge_tags_variables(source_stack_data.variables, variables, "variables")
    _details['variables'] = merged_variables

    return _details


def merge_tags_variables(source_data, new_data, param_key):
    original_map = cli_util.parse_json_parameter(param_key, source_data)
    new_map = cli_util.parse_json_parameter(param_key, new_data)

    merged = {}

    if original_map is not None:
        merged.update(original_map)

    if new_map is not None:
        # overwrite existing key or add new key
        for key in new_map:
            merged[key] = new_map[key]

    return merged


def copy_git_config_source_provider_metadata(config_source_provider_data, access_token, copy_prefix_name):
    _config_provider_details = {}

    _config_provider_details['apiEndpoint'] = config_source_provider_data.api_endpoint
    _config_provider_details['accessToken'] = access_token
    _config_provider_details['compartmentId'] = config_source_provider_data.compartment_id
    _config_provider_details['displayName'] = copy_prefix_name + config_source_provider_data.display_name
    _config_provider_details['description'] = config_source_provider_data.description
    _config_provider_details['configSourceProviderType'] = config_source_provider_data.config_source_provider_type

    if config_source_provider_data.freeform_tags is not None:
        _config_provider_details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", config_source_provider_data.freeform_tags)

    if config_source_provider_data.defined_tags is not None:
        _config_provider_details['definedTags'] = cli_util.parse_json_parameter("defined_tags", config_source_provider_data.defined_tags)

    return _config_provider_details


def get_source_stack_tf_config_base64encoded_zip(stack_id, stack_tf_config_response):
    tf_config = b""
    try:
        for chunk in stack_tf_config_response.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            tf_config += chunk
    except Exception:
        raise Exception("Unable to complete download of the stack's Terraform configuration")

    base64encoded_tf_config = base64.b64encode(tf_config).decode('utf-8')

    if not base64encoded_tf_config:
        raise Exception('Internal error: Unable to generate encoded Terraform configuration')

    return base64encoded_tf_config


resourcemanager_cli.stack_group.add_command(copy_stack)

# oci resource-manager job get-job-detailed-log-content -> oci resource-manager job get-detailed-log-content
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.job_group, resourcemanager_cli.get_job_detailed_log_content, "get-detailed-log-content")


# oci resource-manager private-endpoint-summary list-private-endpoints -> oci resource-manager private-endpoint-summary list
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.private_endpoint_summary_group, resourcemanager_cli.list_private_endpoints, "list")


# oci resource-manager reachable-ip get -> oci resource-manager reachable-ip get-reachable-ip
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.reachable_ip_group, resourcemanager_cli.get_reachable_ip, "get-reachable-ip")


# Remove reachable-ip from oci resource-manager
resourcemanager_cli.resource_manager_root_group.commands.pop(resourcemanager_cli.reachable_ip_group.name)


# Remove private-endpoint-summary from oci resource-manager
resourcemanager_cli.resource_manager_root_group.commands.pop(resourcemanager_cli.private_endpoint_summary_group.name)


# oci resource-manager private-endpoint-summary list-private-endpoints -> oci resource-manager private-endpoint
resourcemanager_cli.private_endpoint_summary_group.commands.pop(resourcemanager_cli.list_private_endpoints.name)
resourcemanager_cli.private_endpoint_group.add_command(resourcemanager_cli.list_private_endpoints)


# oci resource-manager reachable-ip get -> oci resource-manager private-endpoint
resourcemanager_cli.reachable_ip_group.commands.pop(resourcemanager_cli.get_reachable_ip.name)
resourcemanager_cli.private_endpoint_group.add_command(resourcemanager_cli.get_reachable_ip)


# oci resource-manager job create-job-create-apply-rollback-job-operation-details -> oci resource-manager job create-apply-rollback-job
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.job_group, resourcemanager_cli.create_job_create_apply_rollback_job_operation_details, "create-apply-rollback-job")


# oci resource-manager job create-job-create-plan-rollback-job-operation-details -> oci resource-manager job create-plan-rollback-job
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.job_group, resourcemanager_cli.create_job_create_plan_rollback_job_operation_details, "create-plan-rollback-job")


@cli_util.copy_params_from_generated_command(resourcemanager_cli.create_job_create_apply_rollback_job_operation_details, params_to_exclude=['job_operation_details_execution_plan_rollback_strategy', 'job_operation_details_execution_plan_rollback_job_id', 'job_operation_details_target_rollback_job_id', 'job_operation_details_terraform_advanced_options', 'job_operation_details_is_provider_upgrade_required', 'apply_job_plan_resolution'])
@resourcemanager_cli.job_group.command(name=resourcemanager_cli.create_job_create_apply_rollback_job_operation_details.name, help=resourcemanager_cli.create_job_create_apply_rollback_job_operation_details.help)
@cli_util.option('--execution-plan-rollback-strategy', required=True, help=u"""Specifies the source of the execution plan for rollback to apply. Use `AUTO_APPROVED` to run the job without an execution plan for rollback job. [required]""")
@cli_util.option('--execution-plan-rollback-job-id', help=u"""The [OCID] of a plan rollback job, for use when specifying `"FROM_PLAN_ROLLBACK_JOB_ID"` as the `executionPlanRollbackStrategy`.""")
@cli_util.option('--target-rollback-job-id', help=u"""The [OCID] of a successful apply job, for use when specifying `"AUTO_APPROVED"` as the `executionPlanRollbackStrategy`.""")
@cli_util.option('--terraform-advanced-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}, 'terraform-advanced-options': {'module': 'resource_manager', 'class': 'TerraformAdvancedOptions'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_create_apply_rollback_job_operation_details_extended(ctx, **kwargs):

    if 'execution_plan_rollback_strategy' in kwargs:
        kwargs['job_operation_details_execution_plan_rollback_strategy'] = kwargs['execution_plan_rollback_strategy']
        kwargs.pop('execution_plan_rollback_strategy')

    if 'execution_plan_rollback_job_id' in kwargs:
        kwargs['job_operation_details_execution_plan_rollback_job_id'] = kwargs['execution_plan_rollback_job_id']
        kwargs.pop('execution_plan_rollback_job_id')

    if 'target_rollback_job_id' in kwargs:
        kwargs['job_operation_details_target_rollback_job_id'] = kwargs['target_rollback_job_id']
        kwargs.pop('target_rollback_job_id')

    if 'terraform_advanced_options' in kwargs:
        kwargs['job_operation_details_terraform_advanced_options'] = kwargs['terraform_advanced_options']
        kwargs.pop('terraform_advanced_options')

    ctx.invoke(resourcemanager_cli.create_job_create_apply_rollback_job_operation_details, **kwargs)


@cli_util.copy_params_from_generated_command(resourcemanager_cli.create_job_create_plan_rollback_job_operation_details, params_to_exclude=['job_operation_details_target_rollback_job_id', 'job_operation_details_terraform_advanced_options', 'job_operation_details_is_provider_upgrade_required', 'apply_job_plan_resolution'])
@resourcemanager_cli.job_group.command(name=resourcemanager_cli.create_job_create_plan_rollback_job_operation_details.name, help=resourcemanager_cli.create_job_create_plan_rollback_job_operation_details.help)
@cli_util.option('--target-rollback-job-id', required=True, help=u"""The [OCID] of a successful apply job to use for the plan rollback job. [required]""")
@cli_util.option('--terraform-advanced-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}, 'terraform-advanced-options': {'module': 'resource_manager', 'class': 'TerraformAdvancedOptions'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_create_plan_rollback_job_operation_details_extended(ctx, **kwargs):

    if 'target_rollback_job_id' in kwargs:
        kwargs['job_operation_details_target_rollback_job_id'] = kwargs['target_rollback_job_id']
        kwargs.pop('target_rollback_job_id')

    if 'terraform_advanced_options' in kwargs:
        kwargs['job_operation_details_terraform_advanced_options'] = kwargs['terraform_advanced_options']
        kwargs.pop('terraform_advanced_options')

    if 'branch_name' in kwargs:
        kwargs['config_source_branch_name'] = kwargs['branch_name']
        kwargs.pop('branch_name')

    if 'working_directory' in kwargs:
        kwargs['config_source_working_directory'] = kwargs['working_directory']
        kwargs.pop('working_directory')

    ctx.invoke(resourcemanager_cli.update_stack_update_dev_ops_config_source_details, **kwargs)


# oci resource-manager configuration-source-provider create-configuration-source-provider-create-bitbucket-cloud-username-app-password-configuration-source-provider-details -> oci resource-manager configuration-source-provider create-bitbucket-cloud-username-app-password-provider
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.configuration_source_provider_group, resourcemanager_cli.create_configuration_source_provider_create_bitbucket_cloud_username_app_password_configuration_source_provider_details, "create-bitbucket-cloud-username-app-password-provider")


# oci resource-manager configuration-source-provider create-configuration-source-provider-create-bitbucket-server-access-token-configuration-source-provider-details -> oci resource-manager configuration-source-provider create-bitbucket-server-access-token-provider
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.configuration_source_provider_group, resourcemanager_cli.create_configuration_source_provider_create_bitbucket_server_access_token_configuration_source_provider_details, "create-bitbucket-server-access-token-provider")


# oci resource-manager configuration-source-provider update-configuration-source-provider-update-bitbucket-cloud-username-app-password-configuration-source-provider-details -> oci resource-manager configuration-source-provider update-bitbucket-cloud-username-app-password-provider
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.configuration_source_provider_group, resourcemanager_cli.update_configuration_source_provider_update_bitbucket_cloud_username_app_password_configuration_source_provider_details, "update-bitbucket-cloud-username-app-password-provider")


# oci resource-manager configuration-source-provider update-configuration-source-provider-update-bitbucket-server-access-token-configuration-source-provider-details -> oci resource-manager configuration-source-provider update-bitbucket-server-access-token-provider
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.configuration_source_provider_group, resourcemanager_cli.update_configuration_source_provider_update_bitbucket_server_access_token_configuration_source_provider_details, "update-bitbucket-server-access-token-provider")


# oci resource-manager stack create-stack-create-bitbucket-cloud-config-source-details -> oci resource-manager stack create-from-bitbucket-cloud
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.stack_group, resourcemanager_cli.create_stack_create_bitbucket_cloud_config_source_details, "create-from-bitbucket-cloud")


# oci resource-manager stack create-stack-create-bitbucket-server-config-source-details -> oci resource-manager stack create-from-bitbucket-server
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.stack_group, resourcemanager_cli.create_stack_create_bitbucket_server_config_source_details, "create-from-bitbucket-server")


# oci resource-manager stack update-stack-update-bitbucket-cloud-config-source-details -> oci resource-manager stack update-from-bitbucket-cloud
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.stack_group, resourcemanager_cli.update_stack_update_bitbucket_cloud_config_source_details, "update-from-bitbucket-cloud")


# oci resource-manager stack update-stack-update-bitbucket-server-config-source-details -> oci resource-manager stack code
cli_util.rename_command(resourcemanager_cli, resourcemanager_cli.stack_group, resourcemanager_cli.update_stack_update_bitbucket_server_config_source_details, "code")
