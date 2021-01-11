# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.functions.src.oci_cli_functions.generated import fn_service_cli


@click.command(cli_util.override('functions_invoke.functions_invoke_root_group.command_name', 'functions-invoke'), cls=CommandGroupWithAlias, help=cli_util.override('functions_invoke.functions_invoke_root_group.help', """API for the Functions service."""), short_help=cli_util.override('functions_invoke.functions_invoke_root_group.short_help', """Functions Service API"""))
@cli_util.help_option_group
def functions_invoke_root_group():
    pass


@click.command(cli_util.override('functions_invoke.function_group.command_name', 'function'), cls=CommandGroupWithAlias, help="""A function resource defines the code (Docker image) and configuration for a specific function. Functions are defined in applications. Avoid entering confidential information.""")
@cli_util.help_option_group
def function_group():
    pass


fn_service_cli.fn_service_group.add_command(functions_invoke_root_group)
functions_invoke_root_group.add_command(function_group)


@function_group.command(name=cli_util.override('functions_invoke.invoke_function.command_name', 'invoke'), help=u"""Invokes a function \n[Command Reference](invokeFunction)""")
@cli_util.option('--function-id', required=True, help=u"""The [OCID] of this function.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--invoke-function-body', help=u"""The body of the function invocation. Note: The maximum size of the request is limited. This limit is currently 6MB and the endpoint will not accept requests that are bigger than this limit.""")
@cli_util.option('--fn-intent', type=custom_types.CliCaseInsensitiveChoice(["httprequest", "cloudevent"]), help=u"""An optional intent header that indicates to the FDK the way the event should be interpreted. E.g. 'httprequest', 'cloudevent'.""")
@cli_util.option('--fn-invoke-type', type=custom_types.CliCaseInsensitiveChoice(["detached", "sync"]), help=u"""Indicates whether the functions platform should execute the request directly and return the result ('sync') or whether the platform should enqueue the request for later processing and acknowledge that it has been processed ('detached').""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def invoke_function(ctx, from_json, file, function_id, invoke_function_body, fn_intent, fn_invoke_type):

    if isinstance(function_id, six.string_types) and len(function_id.strip()) == 0:
        raise click.UsageError('Parameter --function-id cannot be whitespace or empty string')

    kwargs = {}
    if invoke_function_body is not None:
        kwargs['invoke_function_body'] = invoke_function_body
    if fn_intent is not None:
        kwargs['fn_intent'] = fn_intent
    if fn_invoke_type is not None:
        kwargs['fn_invoke_type'] = fn_invoke_type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    # do not automatically retry operations with binary inputs
    kwargs['retry_strategy'] = oci.retry.NoneRetryStrategy()

    client = cli_util.build_client('functions', 'functions_invoke', ctx)
    result = client.invoke_function(
        function_id=function_id,
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
