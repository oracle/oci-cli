# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import sys
import click
import oci  # noqa: F401
from services.functions.src.oci_cli_functions.generated import fn_service_cli
from services.functions.src.oci_cli_functions_management.generated import functionsmanagement_cli
from services.functions.src.oci_cli_functions_invoke.generated import functionsinvoke_cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils

cli_util.SERVICES_REQUIRING_ENDPOINTS.append("functions_invoke")

# Change from:
# oci functions functions-management application change-compartment
# oci functions functions-management application create
# oci functions functions-management application delete
# oci functions functions-management application update
# oci functions functions-management application get
# oci functions functions-management application list
# oci functions functions-management function create --display-name, --application-id, --image, --memory-in-m-bs
# oci functions functions-management function delete
# oci functions functions-management function update
# oci functions functions-management function get
# oci functions functions-management function list
# oci functions functions-invoke function --function-id --invoke-function-body --file --endpoint --fn-intent --fn-invoke-type

# To:
# oci fn application change-compartment
# oci fn application create
# oci fn application delete
# oci fn application update
# oci fn application get
# oci fn application list
# oci fn function create --display-name, --application-id, --image, --memory-in-mbs
# oci fn function delete
# oci fn function update
# oci fn function get
# oci fn function list
# oci fn function invoke --function-id --body --file --fn-intent --fn-invoke-type

fn_service_cli.fn_service_group.add_command(functionsmanagement_cli.application_group)
fn_service_cli.fn_service_group.add_command(functionsmanagement_cli.function_group)
fn_service_cli.fn_service_group.commands.pop(functionsmanagement_cli.functions_management_root_group.name)
functionsmanagement_cli.function_group.add_command(functionsinvoke_cli.functions_invoke_root_group)
fn_service_cli.fn_service_group.commands.pop(functionsinvoke_cli.functions_invoke_root_group.name)
functionsmanagement_cli.function_group.commands.pop(functionsinvoke_cli.functions_invoke_root_group.name)


@cli_util.copy_params_from_generated_command(functionsinvoke_cli.invoke_function, params_to_exclude=['invoke_function_body'])
@functionsmanagement_cli.function_group.command(name='invoke', help=u"""Invokes a function""")
@cli_util.option('--body', required=True, help=u"""The body of the function invocation. Note: The maximum size of the request is limited. This limit is currently 6MB and the endpoint will not accept requests that are bigger than this limit.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.wrap_exceptions
def invoke_function_extended(ctx, **kwargs):
    kwargs['invoke_function_body'] = kwargs['body']
    del kwargs['body']

    # Make a get call so we can grab the endpoint so the user doesn't have to specify --endpoint.
    get_kwargs = {}
    get_kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('functions', 'functions_management', ctx)
    result = client.get_function(function_id=kwargs['function_id'], **get_kwargs)
    ctx.obj['endpoint'] = result.data.invoke_endpoint

    # Theoretically, this should be good enough, but there is a bug in python sdk when
    # oci.retry.NoneRetryStrategy() is used.  The retry strategy is set in the generated code, functionsinvoke_cli.py.
    # Until the retry bug is fixed in python sdk, we'll just call the client directly.
    # ctx.invoke(functionsinvoke_cli.invoke_function, **kwargs)

    output_file = kwargs['file']
    del kwargs['file']
    if 'from_json' in kwargs:
        del kwargs['from_json']
    client = cli_util.build_client('functions', 'functions_invoke', ctx)
    result = client.invoke_function(**kwargs)

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(output_file, 'name') and output_file.name != '<stdout>' and result and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')
    try:
        if bar:
            bar.__enter__()
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        if result and result.data:
            for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
                if bar:
                    bar.update(len(chunk))
                output_file.write(chunk)
        else:
            sys.exit(1)
    finally:
        if bar:
            bar.render_finish()
        output_file.close()
