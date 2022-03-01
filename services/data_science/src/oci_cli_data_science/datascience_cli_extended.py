# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types
from services.data_science.src.oci_cli_data_science.generated import datascience_cli
import six


@cli_util.copy_params_from_generated_command(datascience_cli.list_work_request_logs, params_to_exclude=[])
@datascience_cli.work_request_group.command(name=cli_util.override('datascience_list_work_request_logs.command_name', 'list-work-request-logs'), help=datascience_cli.list_work_request_logs.help)
@click.pass_context
def list_work_request_logs_extended(ctx, **kwargs):
    ctx.invoke(datascience_cli.list_work_request_logs, **kwargs)


# Rename oci data-science notebook-session update --notebook-session-configuration-details to
# oci data-science notebook-session update --configuration-details
@cli_util.copy_params_from_generated_command(datascience_cli.update_notebook_session, params_to_exclude=['notebook_session_configuration_details'])
@datascience_cli.notebook_session_group.command(name=cli_util.override('update_notebook_session.command_name', 'update'), help=datascience_cli.update_notebook_session.help)
@cli_util.option('--configuration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'configuration-details': {'module': 'data_science', 'class': 'NotebookSessionConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'NotebookSession'})
@cli_util.wrap_exceptions
def update_notebook_session_extended(ctx, **kwargs):
    if 'configuration_details' in kwargs:
        kwargs['notebook_session_configuration_details'] = kwargs['configuration_details']
        del kwargs['configuration_details']

    ctx.invoke(datascience_cli.update_notebook_session, **kwargs)


# Rename oci data-science notebook-session create --notebook-session-configuration-details to
# oci data-science notebook-session create --configuration-details
# Rename oci data-science notebook-session create --notebook-session-config-details to
# oci data-science notebook-session create --config-details
@cli_util.copy_params_from_generated_command(datascience_cli.create_notebook_session, params_to_exclude=['notebook_session_configuration_details', 'notebook_session_config_details'])
@datascience_cli.notebook_session_group.command(name=cli_util.override('create_notebook_session.command_name', 'create'), help=datascience_cli.create_notebook_session.help)
@cli_util.option('--configuration-details', required=False, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Deprecated. Use --config-details. If you specify values for both, then the values must match.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-details', required=False, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Used to configure the infrastructure details of a Data Science notebook. To use the default network configuration, omit the subnet value.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'configuration-details': {'module': 'data_science', 'class': 'NotebookSessionConfigurationDetails'}, 'config-details': {'module': 'data_science', 'class': 'NotebookSessionConfigDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'NotebookSession'})
@cli_util.wrap_exceptions
def create_notebook_session_extended(ctx, **kwargs):
    if 'configuration_details' in kwargs:
        kwargs['notebook_session_configuration_details'] = kwargs['configuration_details']
        del kwargs['configuration_details']
    if 'config_details' in kwargs:
        kwargs['notebook_session_config_details'] = kwargs['config_details']
        del kwargs['config_details']

    ctx.invoke(datascience_cli.create_notebook_session, **kwargs)


cli_util.rename_command(datascience_cli, datascience_cli.model_group,
                        datascience_cli.get_model_artifact_content, "get-artifact-content")


# Overrides the rendering behavior to include all heads in the response
@cli_util.copy_params_from_generated_command(datascience_cli.head_model_artifact, params_to_exclude=[])
@datascience_cli.model_group.command(name=cli_util.override('head_model_artifact.command_name', 'head-model-artifact'), help=datascience_cli.head_model_artifact.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def head_model_artifact(ctx, from_json, model_id):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.head_model_artifact(
        model_id=model_id,
        **kwargs
    )
    cli_util.render(result.data, result.headers, ctx, display_all_headers=True)


# updates the command to use the new option and open the resource prior to sending to the sdk
@cli_util.copy_params_from_generated_command(datascience_cli.create_model_artifact, params_to_exclude=['model_artifact'])
@datascience_cli.model_group.command(name=cli_util.override('create_model_artifact.command_name', 'create-model-artifact'), help=datascience_cli.create_model_artifact.help)
@cli_util.option('--model-artifact-file', required=True, help=u"""The model artifact to upload.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_model_artifact_extended(ctx, model_id, from_json, **kwargs):

    model_artifact_file = kwargs['model_artifact_file']
    del kwargs['model_artifact_file']

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    with open(model_artifact_file, 'rb') as file:
        kwargs['model_id'] = model_id
        kwargs['model_artifact'] = file
        ctx.invoke(datascience_cli.create_model_artifact, **kwargs)


# Overrides the rendering behavior to include all heads in the response
@cli_util.copy_params_from_generated_command(datascience_cli.head_job_artifact, params_to_exclude=[])
@datascience_cli.job_group.command(name=cli_util.override('head_job_artifact.command_name', 'head-job-artifact'), help=datascience_cli.head_job_artifact.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def head_job_artifact(ctx, from_json, job_id):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.head_job_artifact(
        job_id=job_id,
        **kwargs
    )
    cli_util.render(result.data, result.headers, ctx, display_all_headers=True)


# updates the command to use the new option and open the resource prior to sending to the sdk
@cli_util.copy_params_from_generated_command(datascience_cli.create_job_artifact, params_to_exclude=['job_artifact', 'content_disposition'])
@datascience_cli.job_group.command(name=cli_util.override('create_job_artifact.command_name', 'create-job-artifact'), help=datascience_cli.create_job_artifact.help)
@cli_util.option('--job-artifact-file', required=True, help=u"""The job artifact to upload.""")
@cli_util.option('--content-disposition', help=u"""This header is for specifying a filename during upload. It is used to identify the file type and validate if the file type is supported. Example: `--content-disposition "attachment; filename=hello-world.py"`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_job_artifact_extended(ctx, job_id, from_json, **kwargs):

    job_artifact_file = kwargs['job_artifact_file']
    del kwargs['job_artifact_file']

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    with open(job_artifact_file, 'rb') as file:
        kwargs['job_id'] = job_id
        kwargs['job_artifact'] = file
        ctx.invoke(datascience_cli.create_job_artifact, **kwargs)


# Rename oci data-science job create --job-configuration-details --job-infrastructure-configuration-details --job-log-configuration-details to
# oci data-science job create --configuration-details --infrastructure-configuration-details --log-configuration-details
@cli_util.copy_params_from_generated_command(datascience_cli.create_job, params_to_exclude=['job_configuration_details', 'job_infrastructure_configuration_details', 'job_log_configuration_details'])
@datascience_cli.job_group.command(name=cli_util.override('create_job.command_name', 'create'), help=datascience_cli.create_job.help)
@cli_util.option('--configuration-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--infrastructure-configuration-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--log-configuration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'configuration-details': {'module': 'data_science', 'class': 'JobConfigurationDetails'}, 'infrastructure-configuration-details': {'module': 'data_science', 'class': 'JobInfrastructureConfigurationDetails'}, 'log-configuration-details': {'module': 'data_science', 'class': 'JobLogConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_extended(ctx, **kwargs):
    if 'configuration_details' in kwargs:
        kwargs['job_configuration_details'] = kwargs['configuration_details']
        del kwargs['configuration_details']

    if 'infrastructure_configuration_details' in kwargs:
        kwargs['job_infrastructure_configuration_details'] = kwargs['infrastructure_configuration_details']
        del kwargs['infrastructure_configuration_details']

    if 'log_configuration_details' in kwargs:
        kwargs['job_log_configuration_details'] = kwargs['log_configuration_details']
        del kwargs['log_configuration_details']

    ctx.invoke(datascience_cli.create_job, **kwargs)


# Rename oci data-science job-run create --job-configuration-override-details --job-log-configuration-override-details to
# oci data-science job-run create --configuration-override-details --log-configuration-override-details
@cli_util.copy_params_from_generated_command(datascience_cli.create_job_run, params_to_exclude=['job_configuration_override_details', 'job_log_configuration_override_details'])
@datascience_cli.job_run_group.command(name=cli_util.override('create_job_run.command_name', 'create'), help=datascience_cli.create_job_run.help)
@cli_util.option('--configuration-override-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--log-configuration-override-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'configuration-override-details': {'module': 'data_science', 'class': 'JobConfigurationDetails'}, 'log-configuration-override-details': {'module': 'data_science', 'class': 'JobLogConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'JobRun'})
@cli_util.wrap_exceptions
def create_job_run_extended(ctx, **kwargs):
    if 'configuration_override_details' in kwargs:
        kwargs['job_configuration_override_details'] = kwargs['configuration_override_details']
        del kwargs['configuration_override_details']

    if 'log_configuration_override_details' in kwargs:
        kwargs['job_log_configuration_override_details'] = kwargs['log_configuration_override_details']
        del kwargs['log_configuration_override_details']

    ctx.invoke(datascience_cli.create_job_run, **kwargs)


# Rename oci data-science job update --job-infrastructure-configuration-details to
# oci data-science job update --infrastructure-configuration-details
@cli_util.copy_params_from_generated_command(datascience_cli.update_job, params_to_exclude=['job_infrastructure_configuration_details'])
@datascience_cli.job_group.command(name=cli_util.override('update_job.command_name', 'update'), help=datascience_cli.update_job.help)
@cli_util.option('--infrastructure-configuration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'infrastructure-configuration-details': {'module': 'data_science', 'class': 'JobInfrastructureConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'Job'})
@cli_util.wrap_exceptions
def update_job_extended(ctx, **kwargs):

    if 'infrastructure_configuration_details' in kwargs:
        kwargs['job_infrastructure_configuration_details'] = kwargs['infrastructure_configuration_details']
        del kwargs['infrastructure_configuration_details']

    ctx.invoke(datascience_cli.update_job, **kwargs)


# Remove create-model-deployment-single-model-deployment-configuration-details from oci data-science model-deployment
datascience_cli.model_deployment_group.commands.pop(datascience_cli.create_model_deployment_single_model_deployment_configuration_details.name)


# Remove update-model-deployment-update-single-model-deployment-configuration-details from oci data-science model-deployment
datascience_cli.model_deployment_group.commands.pop(datascience_cli.update_model_deployment_update_single_model_deployment_configuration_details.name)


# Remove create-job-standalone-job-infrastructure-configuration-details from oci data-science job
datascience_cli.job_group.commands.pop(datascience_cli.create_job_standalone_job_infrastructure_configuration_details.name)


# Remove update-job-standalone-job-infrastructure-configuration-details from oci data-science job
datascience_cli.job_group.commands.pop(datascience_cli.update_job_standalone_job_infrastructure_configuration_details.name)


# Remove create-job-managed-egress-standalone-job-infrastructure-configuration-details from oci data-science job
datascience_cli.job_group.commands.pop(datascience_cli.create_job_managed_egress_standalone_job_infrastructure_configuration_details.name)


# Remove update-job-managed-egress-standalone-job-infrastructure-configuration-details from oci data-science job
datascience_cli.job_group.commands.pop(datascience_cli.update_job_managed_egress_standalone_job_infrastructure_configuration_details.name)


# Remove create-job-default-job-configuration-details from oci data-science job
datascience_cli.job_group.commands.pop(datascience_cli.create_job_default_job_configuration_details.name)


# Remove create-job-run-default-job-configuration-details from oci data-science job-run
datascience_cli.job_run_group.commands.pop(datascience_cli.create_job_run_default_job_configuration_details.name)


# oci data-science job get-job-artifact-content -> oci data-science job get-artifact-content
cli_util.rename_command(datascience_cli, datascience_cli.job_group, datascience_cli.get_job_artifact_content, "get-artifact-content")
