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
@cli_util.copy_params_from_generated_command(datascience_cli.update_notebook_session, params_to_exclude=['notebook_session_configuration_details', 'notebook_session_runtime_config_details'])
@datascience_cli.notebook_session_group.command(name=cli_util.override('update_notebook_session.command_name', 'update'), help=datascience_cli.update_notebook_session.help)
@cli_util.option('--runtime-config-details', type=custom_types.CLI_COMPLEX_TYPE, help="""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--configuration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'configuration-details': {'module': 'data_science', 'class': 'NotebookSessionConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'NotebookSession'})
@cli_util.wrap_exceptions
def update_notebook_session_extended(ctx, **kwargs):

    if 'runtime_config_details' in kwargs:
        kwargs['notebook_session_runtime_config_details'] = kwargs['runtime_config_details']
        kwargs.pop('runtime_config_details')
    if 'configuration_details' in kwargs:
        kwargs['notebook_session_configuration_details'] = kwargs['configuration_details']
        del kwargs['configuration_details']

    ctx.invoke(datascience_cli.update_notebook_session, **kwargs)


# Rename oci data-science notebook-session create --notebook-session-configuration-details to
# oci data-science notebook-session create --configuration-details
# Rename oci data-science notebook-session create --notebook-session-config-details to
# oci data-science notebook-session create --config-details
@cli_util.copy_params_from_generated_command(datascience_cli.create_notebook_session, params_to_exclude=['notebook_session_configuration_details', 'notebook_session_config_details', 'notebook_session_runtime_config_details'])
@datascience_cli.notebook_session_group.command(name=cli_util.override('create_notebook_session.command_name', 'create'), help=datascience_cli.create_notebook_session.help)
@cli_util.option('--runtime-config-details', type=custom_types.CLI_COMPLEX_TYPE, help="""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--configuration-details', required=False, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Deprecated. Use --config-details. If you specify values for both, then the values must match.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-details', required=False, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Used to configure the infrastructure details of a Data Science notebook. To use the default network configuration, omit the subnet value.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'configuration-details': {'module': 'data_science', 'class': 'NotebookSessionConfigurationDetails'}, 'config-details': {'module': 'data_science', 'class': 'NotebookSessionConfigDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'NotebookSession'})
@cli_util.wrap_exceptions
def create_notebook_session_extended(ctx, **kwargs):

    if 'runtime_config_details' in kwargs:
        kwargs['notebook_session_runtime_config_details'] = kwargs['runtime_config_details']
        kwargs.pop('runtime_config_details')
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
@cli_util.option('--configuration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--infrastructure-configuration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
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


# Overrides the rendering behavior to include all heads in the head step artifact response
@cli_util.copy_params_from_generated_command(datascience_cli.head_step_artifact, params_to_exclude=[])
@datascience_cli.pipeline_group.command(name=cli_util.override('head_step_artifact.command_name', 'head-step-artifact'), help=datascience_cli.head_step_artifact.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def head_step_artifact(ctx, from_json, pipeline_id, step_name):

    if isinstance(pipeline_id, six.string_types) and len(pipeline_id.strip()) == 0:
        raise click.UsageError('Parameter --pipeline-id cannot be whitespace or empty string')

    if isinstance(step_name, six.string_types) and len(step_name.strip()) == 0:
        raise click.UsageError('Parameter --step-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.head_step_artifact(
        pipeline_id=pipeline_id,
        step_name=step_name,
        **kwargs
    )
    cli_util.render(result.data, result.headers, ctx, display_all_headers=True)


# updates the command to use the new option and open the resource prior to sending to the sdk
@cli_util.copy_params_from_generated_command(datascience_cli.create_step_artifact, params_to_exclude=['step_artifact', 'content_disposition'])
@datascience_cli.pipeline_group.command(name=cli_util.override('create_step_artifact.command_name', 'create-step-artifact'), help=datascience_cli.create_step_artifact.help)
@cli_util.option('--step-artifact', required=True, help=u"""The step artifact to upload.""")
@cli_util.option('--content-disposition', help=u"""This header is for specifying a filename during upload. It is used to identify the file type and validate if the file type is supported. Example: `--content-disposition "attachment; filename=hello-world.py"`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_step_artifact_extended(ctx, pipeline_id, step_name, from_json, **kwargs):

    step_artifact = kwargs['step_artifact']
    del kwargs['step_artifact']

    if isinstance(pipeline_id, six.string_types) and len(pipeline_id.strip()) == 0:
        raise click.UsageError('Parameter --pipeline-id cannot be whitespace or empty string')

    if isinstance(step_name, six.string_types) and len(step_name.strip()) == 0:
        raise click.UsageError('Parameter --step-name cannot be whitespace or empty string')

    with open(step_artifact, 'rb') as file:
        kwargs['pipeline_id'] = pipeline_id
        kwargs['step_artifact'] = file
        kwargs['step_name'] = step_name
        ctx.invoke(datascience_cli.create_step_artifact, **kwargs)


# Overrides list pipelines to set compartment id as optional when resource id is provided
@datascience_cli.pipeline_group.command(name=cli_util.override('data_science.list_pipelines.command_name', 'list'), help=u"""Returns a list of Pipelines. \n[Command Reference](listPipelines)""")
@cli_util.option('--compartment-id', help=u"""<b>Filter</b> results by the [OCID] of the compartment.""")
@cli_util.option('--project-id', help=u"""<b>Filter</b> results by the [OCID] of the project.""")
@cli_util.option('--id', help=u"""<b>Filter</b> results by [OCID]. Must be an OCID of the correct type for the resource type.""")
@cli_util.option('--display-name', help=u"""<b>Filter</b> results by its user-friendly name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "FAILED", "DELETED"]), help=u"""The current state of the Pipeline.""")
@cli_util.option('--created-by', help=u"""<b>Filter</b> results by the [OCID] of the user who created the resource.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. See [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

See [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[PipelineSummary]'})
@cli_util.wrap_exceptions
def list_pipelines(ctx, from_json, all_pages, page_size, compartment_id, project_id, id, display_name, lifecycle_state, created_by, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if project_id is not None:
        kwargs['project_id'] = project_id
    if id is not None:
        kwargs['id'] = id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if created_by is not None:
        kwargs['created_by'] = created_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_pipelines,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_pipelines,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_pipelines(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


# Overrides list pipeline runs to set compartment id as optional when resource id is provided
@datascience_cli.pipeline_run_group.command(name=cli_util.override('data_science.list_pipeline_runs.command_name', 'list'), help=u"""Returns a list of PipelineRuns. \n[Command Reference](listPipelineRuns)""")
@cli_util.option('--compartment-id', help=u"""<b>Filter</b> results by the [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""<b>Filter</b> results by [OCID]. Must be an OCID of the correct type for the resource type.""")
@cli_util.option('--pipeline-id', help=u"""The [OCID] of the pipeline.""")
@cli_util.option('--display-name', help=u"""<b>Filter</b> results by its user-friendly name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETING", "DELETED"]), help=u"""The current state of the PipelineRun.""")
@cli_util.option('--created-by', help=u"""<b>Filter</b> results by the [OCID] of the user who created the resource.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. See [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

See [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeAccepted`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[PipelineRunSummary]'})
@cli_util.wrap_exceptions
def list_pipeline_runs(ctx, from_json, all_pages, page_size, compartment_id, id, pipeline_id, display_name, lifecycle_state, created_by, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if pipeline_id is not None:
        kwargs['pipeline_id'] = pipeline_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if created_by is not None:
        kwargs['created_by'] = created_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_pipeline_runs,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_pipeline_runs,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_pipeline_runs(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


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

# Remove create-job-multi-node-job-infrastructure-configuration-details
datascience_cli.job_group.commands.pop(datascience_cli.create_job_multi_node_job_infrastructure_configuration_details.name)

# Remove create-job-multi-node-job-node-configuration-details
datascience_cli.job_group.commands.pop(datascience_cli.create_job_multi_node_job_node_configuration_details.name)

# Remove create-job-ocir-container-job-environment-configuration-details
datascience_cli.job_group.commands.pop(datascience_cli.create_job_ocir_container_job_environment_configuration_details.name)

# Remove create-job-oke-job-infrastructure-configuration-details
# datascience_cli.job_group.commands.pop(datascience_cli.create_job_oke_job_infrastructure_configuration_details.name)

# Remove update-job-empty-job-infrastructure-configuration-details
datascience_cli.job_group.commands.pop(datascience_cli.update_job_empty_job_infrastructure_configuration_details.name)

# Remove update-job-multi-node-job-infrastructure-configuration-details
datascience_cli.job_group.commands.pop(datascience_cli.update_job_multi_node_job_infrastructure_configuration_details.name)

# Remove update-job-oke-job-infrastructure-configuration-details
# datascience_cli.job_group.commands.pop(datascience_cli.update_job_oke_job_infrastructure_configuration_details.name)

# Remove create-job-empty-job-infrastructure-configuration-details from oci data-science job
datascience_cli.job_group.commands.pop(datascience_cli.create_job_empty_job_infrastructure_configuration_details.name)

# Remove create-job-run-default-job-configuration-details from oci data-science job-run
datascience_cli.job_run_group.commands.pop(datascience_cli.create_job_run_default_job_configuration_details.name)

# Remove create-job-run-ocir-container-job-environment-configuration-details from oci data-science job-run
datascience_cli.job_run_group.commands.pop(datascience_cli.create_job_run_ocir_container_job_environment_configuration_details.name)

# Remove create-job-run-empty-job-configuration-details
datascience_cli.job_run_group.commands.pop(datascience_cli.create_job_run_empty_job_configuration_details.name)

# Remove create-job-empty-job-configuration-details from oci data-science job
datascience_cli.job_group.commands.pop(datascience_cli.create_job_empty_job_configuration_details.name)

# Remove create-job-run-empty-job-infrastructure-configuration-details
datascience_cli.job_run_group.commands.pop(datascience_cli.create_job_run_empty_job_infrastructure_configuration_details.name)

# Remove create-job-run-managed-egress-standalone-job-infrastructure-configuration-details
datascience_cli.job_run_group.commands.pop(datascience_cli.create_job_run_managed_egress_standalone_job_infrastructure_configuration_details.name)

# Remove create-job-run-multi-node-job-infrastructure-configuration-details
datascience_cli.job_run_group.commands.pop(datascience_cli.create_job_run_multi_node_job_infrastructure_configuration_details.name)

# Remove create-job-run-multi-node-job-node-configuration-details
datascience_cli.job_run_group.commands.pop(datascience_cli.create_job_run_multi_node_job_node_configuration_details.name)

# Remove create-job-run-oke-job-infrastructure-configuration-details
# datascience_cli.job_run_group.commands.pop(datascience_cli.create_job_run_oke_job_infrastructure_configuration_details.name)

# Remove create-job-run-standalone-job-infrastructure-configuration-details
datascience_cli.job_run_group.commands.pop(datascience_cli.create_job_run_standalone_job_infrastructure_configuration_details.name)

# oci data-science job get-job-artifact-content -> oci data-science job get-artifact-content
cli_util.rename_command(datascience_cli, datascience_cli.job_group, datascience_cli.get_job_artifact_content, "get-artifact-content")


# Remove create-pipeline-pipeline-default-configuration-details from oci data-science pipeline
datascience_cli.pipeline_group.commands.pop(datascience_cli.create_pipeline_pipeline_default_configuration_details.name)


# Remove update-pipeline-pipeline-default-configuration-details from oci data-science pipeline
datascience_cli.pipeline_group.commands.pop(datascience_cli.update_pipeline_pipeline_default_configuration_details.name)


# Remove create-pipeline-run-pipeline-default-configuration-details from oci data-science pipeline-run
datascience_cli.pipeline_run_group.commands.pop(datascience_cli.create_pipeline_run_pipeline_default_configuration_details.name)


# oci data-science data-science-private-endpoint -> oci data-science ds-private-endpoint
cli_util.rename_command(datascience_cli, datascience_cli.data_science_root_group, datascience_cli.data_science_private_endpoint_group, "ds-private-endpoint")


@cli_util.copy_params_from_generated_command(datascience_cli.change_data_science_private_endpoint_compartment, params_to_exclude=['data_science_private_endpoint_id'])
@datascience_cli.data_science_private_endpoint_group.command(name=datascience_cli.change_data_science_private_endpoint_compartment.name, help=datascience_cli.change_data_science_private_endpoint_compartment.help)
@cli_util.option('--ds-private-endpoint-id', required=True, help=u"""The unique ID for a Data Science private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_data_science_private_endpoint_compartment_extended(ctx, **kwargs):

    if 'ds_private_endpoint_id' in kwargs:
        kwargs['data_science_private_endpoint_id'] = kwargs['ds_private_endpoint_id']
        kwargs.pop('ds_private_endpoint_id')

    ctx.invoke(datascience_cli.change_data_science_private_endpoint_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(datascience_cli.create_data_science_private_endpoint, params_to_exclude=['data_science_resource_type'])
@datascience_cli.data_science_private_endpoint_group.command(name=datascience_cli.create_data_science_private_endpoint.name, help=datascience_cli.create_data_science_private_endpoint.help)
@cli_util.option('--ds-resource-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["NOTEBOOK_SESSION"]), help=u"""Data Science resource type. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'data_science', 'class': 'list[string]'}}, output_type={'module': 'data_science', 'class': 'DataSciencePrivateEndpoint'})
@cli_util.wrap_exceptions
def create_data_science_private_endpoint_extended(ctx, **kwargs):

    if 'ds_resource_type' in kwargs:
        kwargs['data_science_resource_type'] = kwargs['ds_resource_type']
        kwargs.pop('ds_resource_type')

    ctx.invoke(datascience_cli.create_data_science_private_endpoint, **kwargs)


@cli_util.copy_params_from_generated_command(datascience_cli.delete_data_science_private_endpoint, params_to_exclude=['data_science_private_endpoint_id'])
@datascience_cli.data_science_private_endpoint_group.command(name=datascience_cli.delete_data_science_private_endpoint.name, help=datascience_cli.delete_data_science_private_endpoint.help)
@cli_util.option('--ds-private-endpoint-id', required=True, help=u"""The unique ID for a Data Science private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_data_science_private_endpoint_extended(ctx, **kwargs):

    if 'ds_private_endpoint_id' in kwargs:
        kwargs['data_science_private_endpoint_id'] = kwargs['ds_private_endpoint_id']
        kwargs.pop('ds_private_endpoint_id')

    ctx.invoke(datascience_cli.delete_data_science_private_endpoint, **kwargs)


@cli_util.copy_params_from_generated_command(datascience_cli.get_data_science_private_endpoint, params_to_exclude=['data_science_private_endpoint_id'])
@datascience_cli.data_science_private_endpoint_group.command(name=datascience_cli.get_data_science_private_endpoint.name, help=datascience_cli.get_data_science_private_endpoint.help)
@cli_util.option('--ds-private-endpoint-id', required=True, help=u"""The unique ID for a Data Science private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'DataSciencePrivateEndpoint'})
@cli_util.wrap_exceptions
def get_data_science_private_endpoint_extended(ctx, **kwargs):

    if 'ds_private_endpoint_id' in kwargs:
        kwargs['data_science_private_endpoint_id'] = kwargs['ds_private_endpoint_id']
        kwargs.pop('ds_private_endpoint_id')

    ctx.invoke(datascience_cli.get_data_science_private_endpoint, **kwargs)


@cli_util.copy_params_from_generated_command(datascience_cli.list_data_science_private_endpoints, params_to_exclude=['data_science_resource_type'])
@datascience_cli.data_science_private_endpoint_group.command(name=datascience_cli.list_data_science_private_endpoints.name, help=datascience_cli.list_data_science_private_endpoints.help)
@cli_util.option('--ds-resource-type', type=custom_types.CliCaseInsensitiveChoice(["NOTEBOOK_SESSION"]), help=u"""Resource types in the Data Science service such as notebooks.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[DataSciencePrivateEndpointSummary]'})
@cli_util.wrap_exceptions
def list_data_science_private_endpoints_extended(ctx, **kwargs):

    if 'ds_resource_type' in kwargs:
        kwargs['data_science_resource_type'] = kwargs['ds_resource_type']
        kwargs.pop('ds_resource_type')

    ctx.invoke(datascience_cli.list_data_science_private_endpoints, **kwargs)


@cli_util.copy_params_from_generated_command(datascience_cli.update_data_science_private_endpoint, params_to_exclude=['data_science_private_endpoint_id'])
@datascience_cli.data_science_private_endpoint_group.command(name=datascience_cli.update_data_science_private_endpoint.name, help=datascience_cli.update_data_science_private_endpoint.help)
@cli_util.option('--ds-private-endpoint-id', required=True, help=u"""The unique ID for a Data Science private endpoint. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'data_science', 'class': 'list[string]'}}, output_type={'module': 'data_science', 'class': 'DataSciencePrivateEndpoint'})
@cli_util.wrap_exceptions
def update_data_science_private_endpoint_extended(ctx, **kwargs):

    if 'ds_private_endpoint_id' in kwargs:
        kwargs['data_science_private_endpoint_id'] = kwargs['ds_private_endpoint_id']
        kwargs.pop('ds_private_endpoint_id')

    ctx.invoke(datascience_cli.update_data_science_private_endpoint, **kwargs)


# Remove create-schedule-schedule-cron-trigger from oci data-science schedule
datascience_cli.schedule_group.commands.pop(datascience_cli.create_schedule_schedule_cron_trigger.name)


# Remove create-schedule-schedule-http-action from oci data-science schedule
datascience_cli.schedule_group.commands.pop(datascience_cli.create_schedule_schedule_http_action.name)


# Remove create-schedule-schedule-i-cal-trigger from oci data-science schedule
datascience_cli.schedule_group.commands.pop(datascience_cli.create_schedule_schedule_i_cal_trigger.name)


# Remove create-schedule-schedule-interval-trigger from oci data-science schedule
datascience_cli.schedule_group.commands.pop(datascience_cli.create_schedule_schedule_interval_trigger.name)


# Remove update-schedule-schedule-cron-trigger from oci data-science schedule
datascience_cli.schedule_group.commands.pop(datascience_cli.update_schedule_schedule_cron_trigger.name)


# Remove update-schedule-schedule-http-action from oci data-science schedule
datascience_cli.schedule_group.commands.pop(datascience_cli.update_schedule_schedule_http_action.name)


# Remove update-schedule-schedule-i-cal-trigger from oci data-science schedule
datascience_cli.schedule_group.commands.pop(datascience_cli.update_schedule_schedule_i_cal_trigger.name)


# Remove update-schedule-schedule-interval-trigger from oci data-science schedule
datascience_cli.schedule_group.commands.pop(datascience_cli.update_schedule_schedule_interval_trigger.name)


# oci data-science ml-application -> oci data-science ml-app
cli_util.rename_command(datascience_cli, datascience_cli.data_science_root_group, datascience_cli.ml_application_group, "ml-app")


# oci data-science ml-application-instance -> oci data-science ml-app-instance
cli_util.rename_command(datascience_cli, datascience_cli.data_science_root_group, datascience_cli.ml_application_instance_group, "ml-app-instance")


# oci data-science ml-app-instance trigger-ml-application-instance-flow -> oci data-science ml-app-instance trigger
cli_util.rename_command(datascience_cli, datascience_cli.ml_application_instance_group, datascience_cli.trigger_ml_application_instance_flow, "trigger")


# oci data-science ml-app-instance create-ml-application-instance-create-idcs-auth-configuration-details -> oci data-science ml-app-instance create-with-idcs-auth
cli_util.rename_command(datascience_cli, datascience_cli.ml_application_instance_group, datascience_cli.create_ml_application_instance_create_idcs_auth_configuration_details, "create-with-idcs-auth")


# oci data-science ml-app-instance create-ml-application-instance-create-iam-auth-configuration-create-details -> oci data-science ml-app-instance create-with-iam-auth
cli_util.rename_command(datascience_cli, datascience_cli.ml_application_instance_group, datascience_cli.create_ml_application_instance_create_iam_auth_configuration_create_details, "create-with-iam-auth")


# oci data-science ml-app-instance create-ml-application-instance-create-idcs-custom-service-auth-configuration-details -> oci data-science ml-app-instance create-with-custom-service-idcs-auth
cli_util.rename_command(datascience_cli, datascience_cli.ml_application_instance_group, datascience_cli.create_ml_application_instance_create_idcs_custom_service_auth_configuration_details, "create-with-custom-service-idcs-auth")


# oci data-science ml-application-implementation -> oci data-science ml-app-implementation
cli_util.rename_command(datascience_cli, datascience_cli.data_science_root_group, datascience_cli.ml_application_implementation_group, "ml-app-implementation")


# oci data-science ml-app-implementation get-ml-application-package-content -> oci data-science ml-app-implementation download-package
cli_util.rename_command(datascience_cli, datascience_cli.ml_application_implementation_group, datascience_cli.get_ml_application_package_content, "download-package")


# oci data-science ml-application-instance-view -> oci data-science ml-app-instance-view
cli_util.rename_command(datascience_cli, datascience_cli.data_science_root_group, datascience_cli.ml_application_instance_view_group, "ml-app-instance-view")


# oci data-science ml-app-instance-view trigger-ml-application-instance-flow -> oci data-science ml-app-instance-view trigger
cli_util.rename_command(datascience_cli, datascience_cli.ml_application_instance_view_group, datascience_cli.trigger_ml_application_instance_view_flow, "trigger")


# oci data-science ml-app-instance-view disable-ml-application-instance-view-trigger -> oci data-science ml-app-instance-view disable-trigger
cli_util.rename_command(datascience_cli, datascience_cli.ml_application_instance_view_group, datascience_cli.disable_ml_application_instance_view_trigger, "disable-trigger")

# oci data-science ml-app-instance-view enable-ml-application-instance-view-trigger -> oci data-science ml-app-instance-view enable-trigger
cli_util.rename_command(datascience_cli, datascience_cli.ml_application_instance_view_group, datascience_cli.enable_ml_application_instance_view_trigger, "enable-trigger")


# oci data-science ml-application-implementation-version -> oci data-science ml-app-implementation-version
cli_util.rename_command(datascience_cli, datascience_cli.data_science_root_group, datascience_cli.ml_application_implementation_version_group, "ml-app-implementation-version")


# oci data-science ml-app-instance-view get-ml-application-historical-package-content -> oci data-science ml-app-instance-view download-package
cli_util.rename_command(datascience_cli, datascience_cli.ml_application_implementation_version_group, datascience_cli.get_ml_application_historical_package_content, "download-package")


# Overriding put-ml-application-package to accept file for package on the ml-app-implementation resource
@cli_util.copy_params_from_generated_command(datascience_cli.put_ml_application_package, params_to_exclude=['put_ml_application_package', 'ml_application_implementation_id'])
@datascience_cli.ml_application_implementation_group.command(name=cli_util.override('data_science.put_ml_application_package.command_name', 'upload-package'), help=datascience_cli.put_ml_application_package.help)
@cli_util.option('--ml-app-package-file', type=click.File(mode='rb'), required=True, help=u"""The package artifact to upload.""")
@cli_util.option('--ml-app-implementation-id', required=True, help=u"""unique MlApplicationImplementation identifier""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def put_ml_application_package_extended(ctx, ml_app_implementation_id, from_json, **kwargs):

    template_file = kwargs['ml_app_package_file']
    del kwargs['ml_app_package_file']

    if isinstance(ml_app_implementation_id, six.string_types) and len(
            ml_app_implementation_id.strip()) == 0:
        raise click.UsageError('Parameter --ml_app_implementation_id cannot be whitespace or empty string')

    kwargs['ml_application_implementation_id'] = ml_app_implementation_id
    kwargs['put_ml_application_package'] = template_file
    ctx.invoke(datascience_cli.put_ml_application_package, **kwargs)


# Remove put-ml-application-package from oci data-science model-deployment
datascience_cli.ml_application_implementation_group.commands.pop(datascience_cli.put_ml_application_package.name)


# Rename oci data-science ml-app change_ml_application_compartment --ml-application-id
#   to oci data-science ml-app change_ml_application_compartment --ml-app-id
@cli_util.copy_params_from_generated_command(datascience_cli.change_ml_application_compartment, params_to_exclude=['ml_application_id'])
@datascience_cli.ml_application_group.command(name=datascience_cli.change_ml_application_compartment.name, help=datascience_cli.change_ml_application_compartment.help)
@cli_util.option('--ml-app-id', required=True, help=u"""unique MlApplication identifier""")
@click.pass_context
def change_ml_application_compartment(ctx, **kwargs):

    if isinstance(kwargs['ml_app_id'], six.string_types) and len(kwargs['ml_app_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-id cannot be whitespace or empty string')

    if 'ml_app_id' in kwargs:
        kwargs['ml_application_id'] = kwargs['ml_app_id']
        del kwargs['ml_app_id']

    ctx.invoke(datascience_cli.change_ml_application_compartment, **kwargs)


# Rename oci data-science ml-app-implementation change_ml_application_implementation_compartment --ml-application-implementation-id
#   to oci data-science ml-app-implementation change_ml_application_implementation_compartment --ml-app-implementation-id
@cli_util.copy_params_from_generated_command(datascience_cli.change_ml_application_implementation_compartment, params_to_exclude=['ml_application_implementation_id'])
@datascience_cli.ml_application_implementation_group.command(name=datascience_cli.change_ml_application_implementation_compartment.name, help=datascience_cli.change_ml_application_implementation_compartment.help)
@cli_util.option('--ml-app-implementation-id', required=True, help=u"""unique MlApplicationImplementation identifier""")
@click.pass_context
def change_ml_application_implementation_compartment(ctx, **kwargs):

    if isinstance(kwargs['ml_app_implementation_id'], six.string_types) and len(kwargs['ml_app_implementation_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-implementation-id cannot be whitespace or empty string')

    if 'ml_app_implementation_id' in kwargs:
        kwargs['ml_application_implementation_id'] = kwargs['ml_app_implementation_id']
        del kwargs['ml_app_implementation_id']

    ctx.invoke(datascience_cli.change_ml_application_implementation_compartment, **kwargs)


# Rename oci data-science ml-app-instance change_ml_application_instance_compartment --ml-application-instance-id
#   to oci data-science ml-app-instance change_ml_application_instance_compartment --ml-app-instance-id
@cli_util.copy_params_from_generated_command(datascience_cli.change_ml_application_instance_compartment, params_to_exclude=['ml_application_instance_id'])
@datascience_cli.ml_application_instance_group.command(name=datascience_cli.change_ml_application_instance_compartment.name, help=datascience_cli.change_ml_application_instance_compartment.help)
@cli_util.option('--ml-app-instance-id', required=True, help=u"""unique MlApplicationInstance identifier""")
@click.pass_context
def change_ml_application_instance_compartment(ctx, **kwargs):

    if isinstance(kwargs['ml_app_instance_id'], six.string_types) and len(kwargs['ml_app_instance_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-instance-id cannot be whitespace or empty string')

    if 'ml_app_instance_id' in kwargs:
        kwargs['ml_application_instance_id'] = kwargs['ml_app_instance_id']
        del kwargs['ml_app_instance_id']

    ctx.invoke(datascience_cli.change_ml_application_instance_compartment, **kwargs)


# Rename oci data-science ml-app-instance-view change_ml_application_instance_view_compartment --ml-application-instance-view-id
#   to oci data-science ml-app-instance-view change_ml_application_instance_view_compartment --ml-app-instance-view-id
@cli_util.copy_params_from_generated_command(datascience_cli.change_ml_application_instance_view_compartment, params_to_exclude=['ml_application_instance_view_id'])
@datascience_cli.ml_application_instance_view_group.command(name=datascience_cli.change_ml_application_instance_view_compartment.name, help=datascience_cli.change_ml_application_instance_view_compartment.help)
@cli_util.option('--ml-app-instance-view-id', required=True, help=u"""unique MlApplicationInstanceView identifier""")
@click.pass_context
def change_ml_application_instance_view_compartment(ctx, **kwargs):

    if isinstance(kwargs['ml_app_instance_view_id'], six.string_types) and len(kwargs['ml_app_instance_view_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-instance-view-id cannot be whitespace or empty string')

    if 'ml_app_instance_view_id' in kwargs:
        kwargs['ml_application_instance_view_id'] = kwargs['ml_app_instance_view_id']
        del kwargs['ml_app_instance_view_id']

    ctx.invoke(datascience_cli.change_ml_application_instance_view_compartment, **kwargs)


# Rename oci data-science ml-app-implementation create_ml_application_implementation --ml-application-id
#   to oci data-science ml-app-implementation create_ml_application_implementation --ml-app-id
@cli_util.copy_params_from_generated_command(datascience_cli.create_ml_application_implementation, params_to_exclude=['ml_application_id'])
@datascience_cli.ml_application_implementation_group.command(name=datascience_cli.create_ml_application_implementation.name, help=datascience_cli.create_ml_application_implementation.help)
@cli_util.option('--ml-app-id', required=True, help=u"""The OCID of the ML Application implemented by this ML Application Implementation""")
@click.pass_context
def create_ml_application_implementation(ctx, **kwargs):

    if isinstance(kwargs['ml_app_id'], six.string_types) and len(kwargs['ml_app_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-id cannot be whitespace or empty string')

    if 'ml_app_id' in kwargs:
        kwargs['ml_application_id'] = kwargs['ml_app_id']
        del kwargs['ml_app_id']

    ctx.invoke(datascience_cli.create_ml_application_implementation, **kwargs)


# Rename oci data-science ml-app-instance create_ml_application_instance --ml-application-id --ml-application-implementation-id
#   to oci data-science ml-app-instance create_ml_application_instance --ml-app-id --ml-app-implementation-id
@cli_util.copy_params_from_generated_command(datascience_cli.create_ml_application_instance, params_to_exclude=['ml_application_id', 'ml_application_implementation_id'])
@datascience_cli.ml_application_instance_group.command(name=datascience_cli.create_ml_application_instance.name, help=datascience_cli.create_ml_application_instance.help)
@cli_util.option('--ml-app-id', required=True, help=u"""The OCID of ML Application. This resource is an instance of ML Application referenced by this OCID.""")
@cli_util.option('--ml-app-implementation-id', help=u"""The OCID of ML Application Implementation selected as a certain solution for a given ML problem (ML Application)""")
@click.pass_context
def create_ml_application_instance(ctx, **kwargs):

    if isinstance(kwargs['ml_app_id'], six.string_types) and len(kwargs['ml_app_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-id cannot be whitespace or empty string')

    if 'ml_app_id' in kwargs:
        kwargs['ml_application_id'] = kwargs['ml_app_id']
        del kwargs['ml_app_id']
    if 'ml_app_implementation_id' in kwargs:
        kwargs['ml_application_implementation_id'] = kwargs['ml_app_implementation_id']
        del kwargs['ml_app_implementation_id']

    ctx.invoke(datascience_cli.create_ml_application_instance, **kwargs)


# Rename oci data-science ml-app-instance create_ml_application_instance_create_idcs_auth_configuration_details --ml-application-id --ml-application-implementation-id
#   to oci data-science ml-app-instance create_ml_application_instance_create_idcs_auth_configuration_details --ml-app-id --ml-app-implementation-id
@cli_util.copy_params_from_generated_command(datascience_cli.create_ml_application_instance_create_idcs_auth_configuration_details, params_to_exclude=['ml_application_id', 'ml_application_implementation_id'])
@datascience_cli.ml_application_instance_group.command(name=datascience_cli.create_ml_application_instance_create_idcs_auth_configuration_details.name, help=datascience_cli.create_ml_application_instance_create_idcs_auth_configuration_details.help)
@cli_util.option('--ml-app-id', required=True, help=u"""The OCID of ML Application. This resource is an instance of ML Application referenced by this OCID.""")
@cli_util.option('--ml-app-implementation-id', help=u"""The OCID of ML Application Implementation selected as a certain solution for a given ML problem (ML Application)""")
@click.pass_context
def create_ml_application_instance_create_idcs_auth_configuration_details(ctx, **kwargs):

    if isinstance(kwargs['ml_app_id'], six.string_types) and len(kwargs['ml_app_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-id cannot be whitespace or empty string')

    if 'ml_app_id' in kwargs:
        kwargs['ml_application_id'] = kwargs['ml_app_id']
        del kwargs['ml_app_id']
    if 'ml_app_implementation_id' in kwargs:
        kwargs['ml_application_implementation_id'] = kwargs['ml_app_implementation_id']
        del kwargs['ml_app_implementation_id']

    ctx.invoke(datascience_cli.create_ml_application_instance_create_idcs_auth_configuration_details, **kwargs)


# Rename oci data-science ml-app-instance create_ml_application_instance_create_idcs_custom_service_auth_configuration_details --ml-application-id --ml-application-implementation-id
#   to oci data-science ml-app-instance create_ml_application_instance_create_idcs_custom_service_auth_configuration_details --ml-app-id --ml-app-implementation-id
@cli_util.copy_params_from_generated_command(datascience_cli.create_ml_application_instance_create_idcs_custom_service_auth_configuration_details, params_to_exclude=['ml_application_id', 'ml_application_implementation_id'])
@datascience_cli.ml_application_instance_group.command(name=datascience_cli.create_ml_application_instance_create_idcs_custom_service_auth_configuration_details.name, help=datascience_cli.create_ml_application_instance_create_idcs_custom_service_auth_configuration_details.help)
@cli_util.option('--ml-app-id', required=True, help=u"""The OCID of ML Application. This resource is an instance of ML Application referenced by this OCID.""")
@cli_util.option('--ml-app-implementation-id', help=u"""The OCID of ML Application Implementation selected as a certain solution for a given ML problem (ML Application)""")
@click.pass_context
def create_ml_application_instance_create_idcs_custom_service_auth_configuration_details(ctx, **kwargs):

    if isinstance(kwargs['ml_app_id'], six.string_types) and len(kwargs['ml_app_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-id cannot be whitespace or empty string')

    if 'ml_app_id' in kwargs:
        kwargs['ml_application_id'] = kwargs['ml_app_id']
        del kwargs['ml_app_id']
    if 'ml_app_implementation_id' in kwargs:
        kwargs['ml_application_implementation_id'] = kwargs['ml_app_implementation_id']
        del kwargs['ml_app_implementation_id']

    ctx.invoke(datascience_cli.create_ml_application_instance_create_idcs_custom_service_auth_configuration_details, **kwargs)


# Rename oci data-science ml-app-instance create_ml_application_instance_create_iam_auth_configuration_create_details --ml-application-id --ml-application-implementation-id
#   to oci data-science ml-app-instance create_ml_application_instance_create_iam_auth_configuration_create_details --ml-app-id --ml-app-implementation-id
@cli_util.copy_params_from_generated_command(datascience_cli.create_ml_application_instance_create_iam_auth_configuration_create_details, params_to_exclude=['ml_application_id', 'ml_application_implementation_id'])
@datascience_cli.ml_application_instance_group.command(name=datascience_cli.create_ml_application_instance_create_iam_auth_configuration_create_details.name, help=datascience_cli.create_ml_application_instance_create_iam_auth_configuration_create_details.help)
@cli_util.option('--ml-app-id', required=True, help=u"""The OCID of ML Application. This resource is an instance of ML Application referenced by this OCID.""")
@cli_util.option('--ml-app-implementation-id', help=u"""The OCID of ML Application Implementation selected as a certain solution for a given ML problem (ML Application)""")
@click.pass_context
def create_ml_application_instance_create_iam_auth_configuration_create_details(ctx, **kwargs):

    if isinstance(kwargs['ml_app_id'], six.string_types) and len(kwargs['ml_app_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-id cannot be whitespace or empty string')

    if 'ml_app_id' in kwargs:
        kwargs['ml_application_id'] = kwargs['ml_app_id']
        del kwargs['ml_app_id']
    if 'ml_app_implementation_id' in kwargs:
        kwargs['ml_application_implementation_id'] = kwargs['ml_app_implementation_id']
        del kwargs['ml_app_implementation_id']

    ctx.invoke(datascience_cli.create_ml_application_instance_create_iam_auth_configuration_create_details, **kwargs)


# Rename oci data-science ml-app delete_ml_application --ml-application-id
#   to oci data-science ml-app delete_ml_application --ml-app-id
@cli_util.copy_params_from_generated_command(datascience_cli.delete_ml_application, params_to_exclude=['ml_application_id'])
@datascience_cli.ml_application_group.command(name=datascience_cli.delete_ml_application.name, help=datascience_cli.delete_ml_application.help)
@cli_util.option('--ml-app-id', required=True, help=u"""unique MlApplication identifier""")
@click.pass_context
def delete_ml_application(ctx, **kwargs):

    if isinstance(kwargs['ml_app_id'], six.string_types) and len(kwargs['ml_app_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-id cannot be whitespace or empty string')

    if 'ml_app_id' in kwargs:
        kwargs['ml_application_id'] = kwargs['ml_app_id']
        del kwargs['ml_app_id']

    ctx.invoke(datascience_cli.delete_ml_application, **kwargs)


# Rename oci data-science ml-app-implementation delete_ml_application_implementation --ml-application-implementation-id
#   to oci data-science ml-app-implementation delete_ml_application_implementation --ml-app-implementation-id
@cli_util.copy_params_from_generated_command(datascience_cli.delete_ml_application_implementation, params_to_exclude=['ml_application_implementation_id'])
@datascience_cli.ml_application_implementation_group.command(name=datascience_cli.delete_ml_application_implementation.name, help=datascience_cli.delete_ml_application_implementation.help)
@cli_util.option('--ml-app-implementation-id', required=True, help=u"""unique MlApplicationImplementation identifier""")
@click.pass_context
def delete_ml_application_implementation(ctx, **kwargs):

    if isinstance(kwargs['ml_app_implementation_id'], six.string_types) and len(kwargs['ml_app_implementation_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-implementation-id cannot be whitespace or empty string')

    if 'ml_app_implementation_id' in kwargs:
        kwargs['ml_application_implementation_id'] = kwargs['ml_app_implementation_id']
        del kwargs['ml_app_implementation_id']

    ctx.invoke(datascience_cli.delete_ml_application_implementation, **kwargs)


# Rename oci data-science ml-app-instance delete_ml_application_instance --ml-application-instance-id
#   to oci data-science ml-app-instance delete_ml_application_instance --ml-app-instance-id
@cli_util.copy_params_from_generated_command(datascience_cli.delete_ml_application_instance, params_to_exclude=['ml_application_instance_id'])
@datascience_cli.ml_application_instance_group.command(name=datascience_cli.delete_ml_application_instance.name, help=datascience_cli.delete_ml_application_instance.help)
@cli_util.option('--ml-app-instance-id', required=True, help=u"""unique MlApplicationInstance identifier""")
@click.pass_context
def delete_ml_application_instance(ctx, **kwargs):

    if isinstance(kwargs['ml_app_instance_id'], six.string_types) and len(kwargs['ml_app_instance_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-instance-id cannot be whitespace or empty string')

    if 'ml_app_instance_id' in kwargs:
        kwargs['ml_application_instance_id'] = kwargs['ml_app_instance_id']
        del kwargs['ml_app_instance_id']

    ctx.invoke(datascience_cli.delete_ml_application_instance, **kwargs)


# Rename oci data-science ml-app-instance-view disable_ml_application_instance_view_trigger --ml-application-instance-view-id
#   to oci data-science ml-app-instance-view disable_ml_application_instance_view_trigger --ml-app-instance-view-id
@cli_util.copy_params_from_generated_command(datascience_cli.disable_ml_application_instance_view_trigger, params_to_exclude=['ml_application_instance_view_id'])
@datascience_cli.ml_application_instance_view_group.command(name=datascience_cli.disable_ml_application_instance_view_trigger.name, help=datascience_cli.disable_ml_application_instance_view_trigger.help)
@cli_util.option('--ml-app-instance-view-id', required=True, help=u"""unique MlApplicationInstanceView identifier""")
@click.pass_context
def disable_ml_application_instance_view_trigger(ctx, **kwargs):

    if isinstance(kwargs['ml_app_instance_view_id'], six.string_types) and len(kwargs['ml_app_instance_view_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-instance-view-id cannot be whitespace or empty string')

    if 'ml_app_instance_view_id' in kwargs:
        kwargs['ml_application_instance_view_id'] = kwargs['ml_app_instance_view_id']
        del kwargs['ml_app_instance_view_id']

    ctx.invoke(datascience_cli.disable_ml_application_instance_view_trigger, **kwargs)


# Rename oci data-science ml-app-instance-view enable_ml_application_instance_view_trigger --ml-application-instance-view-id
#   to oci data-science ml-app-instance-view enable_ml_application_instance_view_trigger --ml-app-instance-view-id
@cli_util.copy_params_from_generated_command(datascience_cli.enable_ml_application_instance_view_trigger, params_to_exclude=['ml_application_instance_view_id'])
@datascience_cli.ml_application_instance_view_group.command(name=datascience_cli.enable_ml_application_instance_view_trigger.name, help=datascience_cli.enable_ml_application_instance_view_trigger.help)
@cli_util.option('--ml-app-instance-view-id', required=True, help=u"""unique MlApplicationInstanceView identifier""")
@click.pass_context
def enable_ml_application_instance_view_trigger(ctx, **kwargs):

    if isinstance(kwargs['ml_app_instance_view_id'], six.string_types) and len(kwargs['ml_app_instance_view_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-instance-view-id cannot be whitespace or empty string')

    if 'ml_app_instance_view_id' in kwargs:
        kwargs['ml_application_instance_view_id'] = kwargs['ml_app_instance_view_id']
        del kwargs['ml_app_instance_view_id']

    ctx.invoke(datascience_cli.enable_ml_application_instance_view_trigger, **kwargs)


# Rename oci data-science ml-app get_ml_application --ml-application-id
#   to oci data-science ml-app get_ml_application --ml-app-id
@cli_util.copy_params_from_generated_command(datascience_cli.get_ml_application, params_to_exclude=['ml_application_id'])
@datascience_cli.ml_application_group.command(name=datascience_cli.get_ml_application.name, help=datascience_cli.get_ml_application.help)
@cli_util.option('--ml-app-id', required=True, help=u"""unique MlApplication identifier""")
@click.pass_context
def get_ml_application(ctx, **kwargs):

    if isinstance(kwargs['ml_app_id'], six.string_types) and len(kwargs['ml_app_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-id cannot be whitespace or empty string')

    if 'ml_app_id' in kwargs:
        kwargs['ml_application_id'] = kwargs['ml_app_id']
        del kwargs['ml_app_id']

    ctx.invoke(datascience_cli.get_ml_application, **kwargs)


# Rename oci data-science ml-app-implementation-version get_ml_application_historical_package_content --ml-application-implementation-version-id
#   to oci data-science ml-app-implementation-version get_ml_application_historical_package_content --ml-app-implementation-version-id
@cli_util.copy_params_from_generated_command(datascience_cli.get_ml_application_historical_package_content, params_to_exclude=['ml_application_implementation_version_id'])
@datascience_cli.ml_application_implementation_version_group.command(name=datascience_cli.get_ml_application_historical_package_content.name, help=datascience_cli.get_ml_application_historical_package_content.help)
@cli_util.option('--ml-app-implementation-version-id', required=True, help=u"""unique MlApplicationImplementationVersion identifier""")
@click.pass_context
def get_ml_application_historical_package_content(ctx, **kwargs):

    if isinstance(kwargs['ml_app_implementation_version_id'], six.string_types) and len(kwargs['ml_app_implementation_version_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-implementation-version-id cannot be whitespace or empty string')

    if 'ml_app_implementation_version_id' in kwargs:
        kwargs['ml_application_implementation_version_id'] = kwargs['ml_app_implementation_version_id']
        del kwargs['ml_app_implementation_version_id']

    ctx.invoke(datascience_cli.get_ml_application_historical_package_content, **kwargs)


# Rename oci data-science ml-app-implementation get_ml_application_implementation --ml-application-implementation-id
#   to oci data-science ml-app-implementation get_ml_application_implementation --ml-app-implementation-id
@cli_util.copy_params_from_generated_command(datascience_cli.get_ml_application_implementation, params_to_exclude=['ml_application_implementation_id'])
@datascience_cli.ml_application_implementation_group.command(name=datascience_cli.get_ml_application_implementation.name, help=datascience_cli.get_ml_application_implementation.help)
@cli_util.option('--ml-app-implementation-id', required=True, help=u"""unique MlApplicationImplementation identifier""")
@click.pass_context
def get_ml_application_implementation(ctx, **kwargs):

    if isinstance(kwargs['ml_app_implementation_id'], six.string_types) and len(kwargs['ml_app_implementation_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-implementation-id cannot be whitespace or empty string')

    if 'ml_app_implementation_id' in kwargs:
        kwargs['ml_application_implementation_id'] = kwargs['ml_app_implementation_id']
        del kwargs['ml_app_implementation_id']

    ctx.invoke(datascience_cli.get_ml_application_implementation, **kwargs)


# Rename oci data-science ml-app-implementation-version get_ml_application_implementation_version --ml-application-implementation-version-id
#   to oci data-science ml-app-implementation-version get_ml_application_implementation_version --ml-app-implementation-version-id
@cli_util.copy_params_from_generated_command(datascience_cli.get_ml_application_implementation_version, params_to_exclude=['ml_application_implementation_version_id'])
@datascience_cli.ml_application_implementation_version_group.command(name=datascience_cli.get_ml_application_implementation_version.name, help=datascience_cli.get_ml_application_implementation_version.help)
@cli_util.option('--ml-app-implementation-version-id', required=True, help=u"""unique MlApplicationImplementationVersion identifier""")
@click.pass_context
def get_ml_application_implementation_version(ctx, **kwargs):

    if isinstance(kwargs['ml_app_implementation_version_id'], six.string_types) and len(kwargs['ml_app_implementation_version_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-implementation-version-id cannot be whitespace or empty string')

    if 'ml_app_implementation_version_id' in kwargs:
        kwargs['ml_application_implementation_version_id'] = kwargs['ml_app_implementation_version_id']
        del kwargs['ml_app_implementation_version_id']

    ctx.invoke(datascience_cli.get_ml_application_implementation_version, **kwargs)


# Rename oci data-science ml-app-instance get_ml_application_instance --ml-application-instance-id
#   to oci data-science ml-app-instance get_ml_application_instance --ml-app-instance-id
@cli_util.copy_params_from_generated_command(datascience_cli.get_ml_application_instance, params_to_exclude=['ml_application_instance_id'])
@datascience_cli.ml_application_instance_group.command(name=datascience_cli.get_ml_application_instance.name, help=datascience_cli.get_ml_application_instance.help)
@cli_util.option('--ml-app-instance-id', required=True, help=u"""unique MlApplicationInstance identifier""")
@click.pass_context
def get_ml_application_instance(ctx, **kwargs):

    if isinstance(kwargs['ml_app_instance_id'], six.string_types) and len(kwargs['ml_app_instance_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-instance-id cannot be whitespace or empty string')

    if 'ml_app_instance_id' in kwargs:
        kwargs['ml_application_instance_id'] = kwargs['ml_app_instance_id']
        del kwargs['ml_app_instance_id']

    ctx.invoke(datascience_cli.get_ml_application_instance, **kwargs)


# Rename oci data-science ml-app-instance-view get_ml_application_instance_view --ml-application-instance-view-id
#   to oci data-science ml-app-instance-view get_ml_application_instance_view --ml-app-instance-view-id
@cli_util.copy_params_from_generated_command(datascience_cli.get_ml_application_instance_view, params_to_exclude=['ml_application_instance_view_id'])
@datascience_cli.ml_application_instance_view_group.command(name=datascience_cli.get_ml_application_instance_view.name, help=datascience_cli.get_ml_application_instance_view.help)
@cli_util.option('--ml-app-instance-view-id', required=True, help=u"""unique MlApplicationInstanceView identifier""")
@click.pass_context
def get_ml_application_instance_view(ctx, **kwargs):

    if isinstance(kwargs['ml_app_instance_view_id'], six.string_types) and len(kwargs['ml_app_instance_view_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-instance-view-id cannot be whitespace or empty string')

    if 'ml_app_instance_view_id' in kwargs:
        kwargs['ml_application_instance_view_id'] = kwargs['ml_app_instance_view_id']
        del kwargs['ml_app_instance_view_id']

    ctx.invoke(datascience_cli.get_ml_application_instance_view, **kwargs)


# Rename oci data-science ml-app-implementation get_ml_application_package_content --ml-application-implementation-id
#   to oci data-science ml-app-implementation get_ml_application_package_content --ml-app-implementation-id
@cli_util.copy_params_from_generated_command(datascience_cli.get_ml_application_package_content, params_to_exclude=['ml_application_implementation_id'])
@datascience_cli.ml_application_implementation_group.command(name=datascience_cli.get_ml_application_package_content.name, help=datascience_cli.get_ml_application_package_content.help)
@cli_util.option('--ml-app-implementation-id', required=True, help=u"""unique MlApplicationImplementation identifier""")
@click.pass_context
def get_ml_application_package_content(ctx, **kwargs):

    if isinstance(kwargs['ml_app_implementation_id'], six.string_types) and len(kwargs['ml_app_implementation_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-implementation-id cannot be whitespace or empty string')

    if 'ml_app_implementation_id' in kwargs:
        kwargs['ml_application_implementation_id'] = kwargs['ml_app_implementation_id']
        del kwargs['ml_app_implementation_id']

    ctx.invoke(datascience_cli.get_ml_application_package_content, **kwargs)


# Rename oci data-science ml-app-implementation-version list_ml_application_implementation_versions --ml-application-implementation-id
#   to oci data-science ml-app-implementation-version list_ml_application_implementation_versions --ml-app-implementation-id
@cli_util.copy_params_from_generated_command(datascience_cli.list_ml_application_implementation_versions, params_to_exclude=['ml_application_implementation_id'])
@datascience_cli.ml_application_implementation_version_group.command(name=datascience_cli.list_ml_application_implementation_versions.name, help=datascience_cli.list_ml_application_implementation_versions.help)
@cli_util.option('--ml-app-implementation-id', help=u"""unique MlApplicationImplementation identifier""")
@click.pass_context
def list_ml_application_implementation_versions(ctx, **kwargs):

    if 'ml_app_implementation_id' in kwargs:
        kwargs['ml_application_implementation_id'] = kwargs['ml_app_implementation_id']
        del kwargs['ml_app_implementation_id']

    ctx.invoke(datascience_cli.list_ml_application_implementation_versions, **kwargs)


# Rename oci data-science ml-app-implementation list_ml_application_implementations --ml-application-implementation-id --ml-application-id
#   to oci data-science ml-app-implementation list_ml_application_implementations --ml-app-implementation-id --ml-app-id
@cli_util.copy_params_from_generated_command(datascience_cli.list_ml_application_implementations, params_to_exclude=['ml_application_implementation_id', 'ml_application_id'])
@datascience_cli.ml_application_implementation_group.command(name=datascience_cli.list_ml_application_implementations.name, help=datascience_cli.list_ml_application_implementations.help)
@cli_util.option('--ml-app-implementation-id', help=u"""unique MlApplicationImplementation identifier""")
@cli_util.option('--ml-app-id', help=u"""unique MlApplication identifier""")
@click.pass_context
def list_ml_application_implementations(ctx, **kwargs):

    if 'ml_app_implementation_id' in kwargs:
        kwargs['ml_application_implementation_id'] = kwargs['ml_app_implementation_id']
        del kwargs['ml_app_implementation_id']
    if 'ml_app_id' in kwargs:
        kwargs['ml_application_id'] = kwargs['ml_app_id']
        del kwargs['ml_app_id']

    ctx.invoke(datascience_cli.list_ml_application_implementations, **kwargs)


# Rename oci data-science ml-app-instance-view list_ml_application_instance_views --ml-application-id --ml-application-implementation-id
#   to oci data-science ml-app-instance-view list_ml_application_instance_views --ml-app-id --ml-app-implementation-id
@cli_util.copy_params_from_generated_command(datascience_cli.list_ml_application_instance_views, params_to_exclude=['ml_application_id', 'ml_application_implementation_id'])
@datascience_cli.ml_application_instance_view_group.command(name=datascience_cli.list_ml_application_instance_views.name, help=datascience_cli.list_ml_application_instance_views.help)
@cli_util.option('--ml-app-id', help=u"""unique MlApplication identifier""")
@cli_util.option('--ml-app-implementation-id', help=u"""unique MlApplicationImplementation identifier""")
@click.pass_context
def list_ml_application_instance_views(ctx, **kwargs):

    if 'ml_app_id' in kwargs:
        kwargs['ml_application_id'] = kwargs['ml_app_id']
        del kwargs['ml_app_id']
    if 'ml_app_implementation_id' in kwargs:
        kwargs['ml_application_implementation_id'] = kwargs['ml_app_implementation_id']
        del kwargs['ml_app_implementation_id']

    ctx.invoke(datascience_cli.list_ml_application_instance_views, **kwargs)


# Rename oci data-science ml-app-instance list_ml_application_instances --ml-application-id
#   to oci data-science ml-app-instance list_ml_application_instances --ml-app-id
@cli_util.copy_params_from_generated_command(datascience_cli.list_ml_application_instances, params_to_exclude=['ml_application_id'])
@datascience_cli.ml_application_instance_group.command(name=datascience_cli.list_ml_application_instances.name, help=datascience_cli.list_ml_application_instances.help)
@cli_util.option('--ml-app-id', help=u"""unique MlApplication identifier""")
@click.pass_context
def list_ml_application_instances(ctx, **kwargs):

    if 'ml_app_id' in kwargs:
        kwargs['ml_application_id'] = kwargs['ml_app_id']
        del kwargs['ml_app_id']

    ctx.invoke(datascience_cli.list_ml_application_instances, **kwargs)


# Rename oci data-science ml-app list_ml_applications --ml-application-id
#   to oci data-science ml-app list_ml_applications --ml-app-id
@cli_util.copy_params_from_generated_command(datascience_cli.list_ml_applications, params_to_exclude=['ml_application_id'])
@datascience_cli.ml_application_group.command(name=datascience_cli.list_ml_applications.name, help=datascience_cli.list_ml_applications.help)
@cli_util.option('--ml-app-id', help=u"""unique MlApplication identifier""")
@click.pass_context
def list_ml_applications(ctx, **kwargs):

    if 'ml_app_id' in kwargs:
        kwargs['ml_application_id'] = kwargs['ml_app_id']
        del kwargs['ml_app_id']

    ctx.invoke(datascience_cli.list_ml_applications, **kwargs)


# Rename oci data-science ml-app-instance-view recover_ml_application_instance_view --ml-application-instance-view-id
#   to oci data-science ml-app-instance-view recover_ml_application_instance_view --ml-app-instance-view-id
@cli_util.copy_params_from_generated_command(datascience_cli.recover_ml_application_instance_view, params_to_exclude=['ml_application_instance_view_id'])
@datascience_cli.ml_application_instance_view_group.command(name=datascience_cli.recover_ml_application_instance_view.name, help=datascience_cli.recover_ml_application_instance_view.help)
@cli_util.option('--ml-app-instance-view-id', required=True, help=u"""unique MlApplicationInstanceView identifier""")
@click.pass_context
def recover_ml_application_instance_view(ctx, **kwargs):

    if isinstance(kwargs['ml_app_instance_view_id'], six.string_types) and len(kwargs['ml_app_instance_view_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-instance-view-id cannot be whitespace or empty string')

    if 'ml_app_instance_view_id' in kwargs:
        kwargs['ml_application_instance_view_id'] = kwargs['ml_app_instance_view_id']
        del kwargs['ml_app_instance_view_id']

    ctx.invoke(datascience_cli.recover_ml_application_instance_view, **kwargs)


# Rename oci data-science ml-app-instance trigger_ml_application_instance_flow --ml-application-instance-id
#   to oci data-science ml-app-instance trigger_ml_application_instance_flow --ml-app-instance-id
@cli_util.copy_params_from_generated_command(datascience_cli.trigger_ml_application_instance_flow, params_to_exclude=['ml_application_instance_id'])
@datascience_cli.ml_application_instance_group.command(name=datascience_cli.trigger_ml_application_instance_flow.name, help=datascience_cli.trigger_ml_application_instance_flow.help)
@cli_util.option('--ml-app-instance-id', required=True, help=u"""unique MlApplicationInstance identifier""")
@click.pass_context
def trigger_ml_application_instance_flow(ctx, **kwargs):

    if isinstance(kwargs['ml_app_instance_id'], six.string_types) and len(kwargs['ml_app_instance_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-instance-id cannot be whitespace or empty string')

    if 'ml_app_instance_id' in kwargs:
        kwargs['ml_application_instance_id'] = kwargs['ml_app_instance_id']
        del kwargs['ml_app_instance_id']

    ctx.invoke(datascience_cli.trigger_ml_application_instance_flow, **kwargs)


# Rename oci data-science ml-app-instance-view trigger_ml_application_instance_view_flow --ml-application-instance-view-id
#   to oci data-science ml-app-instance-view trigger_ml_application_instance_view_flow --ml-app-instance-view-id
@cli_util.copy_params_from_generated_command(datascience_cli.trigger_ml_application_instance_view_flow, params_to_exclude=['ml_application_instance_view_id'])
@datascience_cli.ml_application_instance_view_group.command(name=datascience_cli.trigger_ml_application_instance_view_flow.name, help=datascience_cli.trigger_ml_application_instance_view_flow.help)
@cli_util.option('--ml-app-instance-view-id', required=True, help=u"""unique MlApplicationInstanceView identifier""")
@click.pass_context
def trigger_ml_application_instance_view_flow(ctx, **kwargs):

    if isinstance(kwargs['ml_app_instance_view_id'], six.string_types) and len(kwargs['ml_app_instance_view_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-instance-view-id cannot be whitespace or empty string')

    if 'ml_app_instance_view_id' in kwargs:
        kwargs['ml_application_instance_view_id'] = kwargs['ml_app_instance_view_id']
        del kwargs['ml_app_instance_view_id']

    ctx.invoke(datascience_cli.trigger_ml_application_instance_view_flow, **kwargs)


# Rename oci data-science ml-app update_ml_application --ml-application-id
#   to oci data-science ml-app update_ml_application --ml-app-id
@cli_util.copy_params_from_generated_command(datascience_cli.update_ml_application, params_to_exclude=['ml_application_id'])
@datascience_cli.ml_application_group.command(name=datascience_cli.update_ml_application.name, help=datascience_cli.update_ml_application.help)
@cli_util.option('--ml-app-id', required=True, help=u"""unique MlApplication identifier""")
@click.pass_context
def update_ml_application(ctx, **kwargs):

    if isinstance(kwargs['ml_app_id'], six.string_types) and len(kwargs['ml_app_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-id cannot be whitespace or empty string')

    if 'ml_app_id' in kwargs:
        kwargs['ml_application_id'] = kwargs['ml_app_id']
        del kwargs['ml_app_id']

    ctx.invoke(datascience_cli.update_ml_application, **kwargs)


# Rename oci data-science ml-app-implementation update_ml_application_implementation --ml-application-implementation-id
#   to oci data-science ml-app-implementation update_ml_application_implementation --ml-app-implementation-id
@cli_util.copy_params_from_generated_command(datascience_cli.update_ml_application_implementation, params_to_exclude=['ml_application_implementation_id'])
@datascience_cli.ml_application_implementation_group.command(name=datascience_cli.update_ml_application_implementation.name, help=datascience_cli.update_ml_application_implementation.help)
@cli_util.option('--ml-app-implementation-id', required=True, help=u"""unique MlApplicationImplementation identifier""")
@click.pass_context
def update_ml_application_implementation(ctx, **kwargs):

    if isinstance(kwargs['ml_app_implementation_id'], six.string_types) and len(kwargs['ml_app_implementation_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-implementation-id cannot be whitespace or empty string')

    if 'ml_app_implementation_id' in kwargs:
        kwargs['ml_application_implementation_id'] = kwargs['ml_app_implementation_id']
        del kwargs['ml_app_implementation_id']

    ctx.invoke(datascience_cli.update_ml_application_implementation, **kwargs)


# Rename oci data-science ml-app-implementation-version update_ml_application_implementation_version --ml-application-implementation-version-id
#   to oci data-science ml-app-implementation-version update_ml_application_implementation_version --ml-app-implementation-version-id
@cli_util.copy_params_from_generated_command(datascience_cli.update_ml_application_implementation_version, params_to_exclude=['ml_application_implementation_version_id'])
@datascience_cli.ml_application_implementation_version_group.command(name=datascience_cli.update_ml_application_implementation_version.name, help=datascience_cli.update_ml_application_implementation_version.help)
@cli_util.option('--ml-app-implementation-version-id', required=True, help=u"""unique MlApplicationImplementationVersion identifier""")
@click.pass_context
def update_ml_application_implementation_version(ctx, **kwargs):

    if isinstance(kwargs['ml_app_implementation_version_id'], six.string_types) and len(kwargs['ml_app_implementation_version_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-implementation-version-id cannot be whitespace or empty string')

    if 'ml_app_implementation_version_id' in kwargs:
        kwargs['ml_application_implementation_version_id'] = kwargs['ml_app_implementation_version_id']
        del kwargs['ml_app_implementation_version_id']

    ctx.invoke(datascience_cli.update_ml_application_implementation_version, **kwargs)


# Rename oci data-science ml-app-instance update_ml_application_instance --ml-application-instance-id --ml-application-implementation-id
#   to oci data-science ml-app-instance update_ml_application_instance --ml-app-instance-id --ml-app-implementation-id
@cli_util.copy_params_from_generated_command(datascience_cli.update_ml_application_instance, params_to_exclude=['ml_application_instance_id', 'ml_application_implementation_id'])
@datascience_cli.ml_application_instance_group.command(name=datascience_cli.update_ml_application_instance.name, help=datascience_cli.update_ml_application_instance.help)
@cli_util.option('--ml-app-instance-id', required=True, help=u"""unique MlApplicationInstance identifier""")
@cli_util.option('--ml-app-implementation-id', help=u"""The OCID of ML Application Implementation selected as a certain solution for a given ML problem (ML Application) used for the given instance.""")
@click.pass_context
def update_ml_application_instance(ctx, **kwargs):

    if isinstance(kwargs['ml_app_instance_id'], six.string_types) and len(kwargs['ml_app_instance_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-instance-id cannot be whitespace or empty string')

    if 'ml_app_instance_id' in kwargs:
        kwargs['ml_application_instance_id'] = kwargs['ml_app_instance_id']
        del kwargs['ml_app_instance_id']
    if 'ml_app_implementation_id' in kwargs:
        kwargs['ml_application_implementation_id'] = kwargs['ml_app_implementation_id']
        del kwargs['ml_app_implementation_id']

    ctx.invoke(datascience_cli.update_ml_application_instance, **kwargs)


# Rename oci data-science ml-app-instance-view update_ml_application_instance_view --ml-application-instance-view-id
#   to oci data-science ml-app-instance-view update_ml_application_instance_view --ml-app-instance-view-id
@cli_util.copy_params_from_generated_command(datascience_cli.update_ml_application_instance_view, params_to_exclude=['ml_application_instance_view_id'])
@datascience_cli.ml_application_instance_view_group.command(name=datascience_cli.update_ml_application_instance_view.name, help=datascience_cli.update_ml_application_instance_view.help)
@cli_util.option('--ml-app-instance-view-id', required=True, help=u"""unique MlApplicationInstanceView identifier""")
@click.pass_context
def update_ml_application_instance_view(ctx, **kwargs):

    if isinstance(kwargs['ml_app_instance_view_id'], six.string_types) and len(kwargs['ml_app_instance_view_id'].strip()) == 0:
        raise click.UsageError('Parameter --ml-app-instance-view-id cannot be whitespace or empty string')

    if 'ml_app_instance_view_id' in kwargs:
        kwargs['ml_application_instance_view_id'] = kwargs['ml_app_instance_view_id']
        del kwargs['ml_app_instance_view_id']

    ctx.invoke(datascience_cli.update_ml_application_instance_view, **kwargs)
