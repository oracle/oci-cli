# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import sys
import click
import oci  # noqa: F401
from services.functions.src.oci_cli_functions.generated import fn_service_cli
from services.functions.src.oci_cli_functions import invoke_endpoint_cache
from services.functions.src.oci_cli_functions_management.generated import functionsmanagement_cli
from services.functions.src.oci_cli_functions_invoke.generated import functionsinvoke_cli
from services.functions.src.oci_cli_work_request_management.generated import workrequestmanagement_cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils


def _add_service_requiring_endpoint(service_name):
    if service_name not in cli_util.SERVICES_REQUIRING_ENDPOINTS:
        cli_util.SERVICES_REQUIRING_ENDPOINTS.append(service_name)


def _safe_pop(command_group, command_name):
    if command_name in command_group.commands:
        command_group.commands.pop(command_name)


_add_service_requiring_endpoint("functions_invoke")
_add_service_requiring_endpoint("work_request_management")

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
# oci functions functions-management pbf-listing get
# oci functions functions-management pbf-listing list
# oci functions functions-management pbf-listing-version get
# oci functions functions-management pbf-listing-version list
# oci functions functions-management triggers-collection list-triggers

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
# oci fn pbf-listing get
# oci fn pbf-listing list
# oci fn pbf-listing-version get
# oci fn pbf-listing-version list
# oci fn triggers list

cli_util.rename_command(fn_service_cli, functionsmanagement_cli.functions_management_root_group, functionsmanagement_cli.triggers_collection_group, 'trigger')
cli_util.rename_command(fn_service_cli, functionsmanagement_cli.triggers_collection_group, functionsmanagement_cli.list_triggers, 'list')

fn_service_cli.fn_service_group.add_command(functionsmanagement_cli.application_group)
fn_service_cli.fn_service_group.add_command(functionsmanagement_cli.function_group)
fn_service_cli.fn_service_group.add_command(functionsmanagement_cli.pbf_listing_group)
fn_service_cli.fn_service_group.add_command(functionsmanagement_cli.triggers_collection_group)
fn_service_cli.fn_service_group.add_command(functionsmanagement_cli.pbf_listing_version_group)

# Expose runtime commands as `oci fn runtime` and `oci fn runtime-version`.
# Remove generated command names from all relevant groups first so interactive
# completion does not suggest the raw generated names.
_safe_pop(fn_service_cli.fn_service_group, 'functions-runtime')
_safe_pop(fn_service_cli.fn_service_group, 'functions-runtime-version')
_safe_pop(functionsmanagement_cli.functions_management_root_group, 'functions-runtime')
_safe_pop(functionsmanagement_cli.functions_management_root_group, 'functions-runtime-version')
functionsmanagement_cli.functions_runtime_group.name = 'runtime'
functionsmanagement_cli.functions_runtime_version_group.name = 'runtime-version'
fn_service_cli.fn_service_group.add_command(functionsmanagement_cli.functions_runtime_group)
fn_service_cli.fn_service_group.add_command(functionsmanagement_cli.functions_runtime_version_group)
fn_service_cli.fn_service_group.commands.pop(functionsmanagement_cli.functions_management_root_group.name)
functionsmanagement_cli.function_group.add_command(functionsinvoke_cli.functions_invoke_root_group)
fn_service_cli.fn_service_group.commands.pop(functionsinvoke_cli.functions_invoke_root_group.name)
functionsmanagement_cli.function_group.commands.pop(functionsinvoke_cli.functions_invoke_root_group.name)

# Flatten work-request commands directly under `oci fn`.
_safe_pop(fn_service_cli.fn_service_group, workrequestmanagement_cli.work_request_management_root_group.name)
fn_service_cli.fn_service_group.add_command(workrequestmanagement_cli.work_request_group)
fn_service_cli.fn_service_group.add_command(workrequestmanagement_cli.work_request_error_group)
fn_service_cli.fn_service_group.add_command(workrequestmanagement_cli.work_request_log_entry_group)
_safe_pop(workrequestmanagement_cli.work_request_group, 'cancel')
cli_util.rename_command(
    fn_service_cli,
    workrequestmanagement_cli.work_request_log_entry_group,
    workrequestmanagement_cli.list_work_request_logs,
    'list'
)


@cli_util.copy_params_from_generated_command(functionsinvoke_cli.invoke_function, params_to_exclude=['invoke_function_body'])
@functionsmanagement_cli.function_group.command(name='invoke', help=u"""Invokes a function""")
@cli_util.option('--endpoint-cache-ttl', type=click.IntRange(min=0), envvar=invoke_endpoint_cache.ENDPOINT_CACHE_TTL_ENV_VAR, help=u"""The number of seconds to cache the resolved function invoke endpoint. If not set, the endpoint is cached for 900 seconds (15 minutes). Set to 0 to disable endpoint caching.""")
@cli_util.option('--no-endpoint-cache', is_flag=True, help=u"""Disable the local function invoke endpoint cache for this invocation.""")
@cli_util.option('--body', required=True, help=u"""The body of the function invocation. Note: The maximum size of the request is limited. This limit is currently 6MB and the endpoint will not accept requests that are bigger than this limit.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def invoke_function_extended(ctx, **kwargs):
    no_endpoint_cache = kwargs.pop('no_endpoint_cache', False)
    endpoint_cache_ttl = kwargs.pop('endpoint_cache_ttl', None)
    kwargs['invoke_function_body'] = kwargs['body']
    del kwargs['body']

    # Preserve the management endpoint context before replacing ctx.obj['endpoint'] with the invoke endpoint.
    cache_context = dict(ctx.obj)
    invoke_endpoint = None
    if not no_endpoint_cache:
        invoke_endpoint = invoke_endpoint_cache.get_cached_endpoint(cache_context, kwargs['function_id'], endpoint_cache_ttl)

    if invoke_endpoint is None:
        # Make a get call so we can grab the endpoint so the user doesn't have to specify --endpoint.
        get_kwargs = {}
        get_kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
        client = cli_util.build_client('functions', 'functions_management', ctx)
        result = client.get_function(function_id=kwargs['function_id'], **get_kwargs)
        invoke_endpoint = result.data.invoke_endpoint
        if not no_endpoint_cache and endpoint_cache_ttl != 0:
            invoke_endpoint_cache.put_cached_endpoint(cache_context, kwargs['function_id'], invoke_endpoint)

    ctx.obj['endpoint'] = invoke_endpoint

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
