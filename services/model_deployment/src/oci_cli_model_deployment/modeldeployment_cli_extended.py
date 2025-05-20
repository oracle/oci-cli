# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates. All rights reserved.

import click
import six

from oci_cli import cli_util, json_skeleton_utils, cli_constants
from services.model_deployment.src.oci_cli_model_deployment.generated import modeldeployment_cli


# Updates the command to parse the request_body json string into a Python object before sending it to the SDK.
@modeldeployment_cli.inference_result_group.command(name=cli_util.override('model_deployment.predict.command_name', 'predict'), help=u"""Invoking a model deployment calls the predict endpoint of the model deployment URI. This endpoint takes sample data as input and is processed using the predict() function in score.py model artifact file \n[Command Reference](predict)""")
@cli_util.option('--model-deployment-id', required=True, help=u"""The [OCID] of the model deployment.""")
@cli_util.option('--request-body', required=True, help=u"""Input data details for making a prediction call""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def predict_extended(ctx, from_json, model_deployment_id, request_body):

    if isinstance(model_deployment_id, six.string_types) and len(model_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --model-deployment-id cannot be whitespace or empty string')

    parsed_request_body = ''
    if request_body is not None and request_body.strip() != '':
        parsed_request_body = cli_util.parse_json_parameter('request_body', request_body, 'camelize_keys', False)

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('model_deployment', 'model_deployment', ctx)
    result = client.predict(
        model_deployment_id=model_deployment_id,
        request_body=parsed_request_body,
        **kwargs
    )
    cli_util.render_response(result, ctx)


# Updates the command to parse the request_body json string into a Python object before sending it to the SDK.
@modeldeployment_cli.inference_result_group.command(name=cli_util.override('model_deployment.predict_with_response_stream.command_name', 'predict-with-response-stream'), help=u"""Invoking a model deployment calls the predictWithResponseStream endpoint of the model deployment URI to get the streaming result. This endpoint takes sample data as input and is processed using the predict() function in score.py model artifact file \n[Command Reference](predictWithResponseStream)""")
@cli_util.option('--model-deployment-id', required=True, help=u"""The [OCID] of the model deployment.""")
@cli_util.option('--request-body', required=True, help=u"""Input data details for making a prediction call""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def predict_with_response_stream_extended(ctx, from_json, file, model_deployment_id, request_body):

    if isinstance(model_deployment_id, six.string_types) and len(model_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --model-deployment-id cannot be whitespace or empty string')

    parsed_request_body = ''
    if request_body is not None and request_body.strip() != '':
        parsed_request_body = cli_util.parse_json_parameter('request_body', request_body, 'camelize_keys', False)

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('model_deployment', 'model_deployment', ctx)
    result = client.predict_with_response_stream(
        model_deployment_id=model_deployment_id,
        request_body=parsed_request_body,
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
