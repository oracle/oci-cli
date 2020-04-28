# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
import oci
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
@cli_util.copy_params_from_generated_command(datascience_cli.create_notebook_session, params_to_exclude=['notebook_session_configuration_details'])
@datascience_cli.notebook_session_group.command(name=cli_util.override('create_notebook_session.command_name', 'create'), help=datascience_cli.create_notebook_session.help)
@cli_util.option('--configuration-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'configuration-details': {'module': 'data_science', 'class': 'NotebookSessionConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'NotebookSession'})
@cli_util.wrap_exceptions
def create_notebook_session_extended(ctx, **kwargs):
    if 'configuration_details' in kwargs:
        kwargs['notebook_session_configuration_details'] = kwargs['configuration_details']
        del kwargs['configuration_details']

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

    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    # do not automatically retry operations with binary inputs
    kwargs['retry_strategy'] = oci.retry.NoneRetryStrategy()

    client = cli_util.build_client('data_science', 'data_science', ctx)
    with open(model_artifact_file, 'rb') as file:
        result = client.create_model_artifact(
            model_id=model_id,
            model_artifact=file.read(),
            **kwargs
        )
        cli_util.render_response(result, ctx)
