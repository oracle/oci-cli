# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.functions.src.oci_cli_functions_management.generated import functionsmanagement_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Remove create-function-constant-provisioned-concurrency-config from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.create_function_constant_provisioned_concurrency_config.name)


# Remove update-function-constant-provisioned-concurrency-config from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.update_function_constant_provisioned_concurrency_config.name)


# Remove create-function-none-provisioned-concurrency-config from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.create_function_none_provisioned_concurrency_config.name)


# Remove update-function-none-provisioned-concurrency-config from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.update_function_none_provisioned_concurrency_config.name)


@cli_util.copy_params_from_generated_command(functionsmanagement_cli.create_function, params_to_exclude=['provisioned_concurrency_config'])
@functionsmanagement_cli.function_group.command(name=functionsmanagement_cli.create_function.name, help=functionsmanagement_cli.create_function.help)
@cli_util.option('--provisioned-concurrency', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'config': {'module': 'functions', 'class': 'dict(str, string)'}, 'provisioned-concurrency': {'module': 'functions', 'class': 'FunctionProvisionedConcurrencyConfig'}, 'trace-config': {'module': 'functions', 'class': 'FunctionTraceConfig'}, 'freeform-tags': {'module': 'functions', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'functions', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'functions', 'class': 'Function'})
@cli_util.wrap_exceptions
def create_function_extended(ctx, **kwargs):
    if 'provisioned_concurrency' in kwargs:
        kwargs['provisioned_concurrency_config'] = kwargs['provisioned_concurrency']
        kwargs.pop('provisioned_concurrency')

    ctx.invoke(functionsmanagement_cli.create_function, **kwargs)


@cli_util.copy_params_from_generated_command(functionsmanagement_cli.update_function, params_to_exclude=['provisioned_concurrency_config'])
@functionsmanagement_cli.function_group.command(name=functionsmanagement_cli.update_function.name, help=functionsmanagement_cli.update_function.help)
@cli_util.option('--provisioned-concurrency', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'config': {'module': 'functions', 'class': 'dict(str, string)'}, 'provisioned-concurrency': {'module': 'functions', 'class': 'FunctionProvisionedConcurrencyConfig'}, 'trace-config': {'module': 'functions', 'class': 'FunctionTraceConfig'}, 'freeform-tags': {'module': 'functions', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'functions', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'functions', 'class': 'Function'})
@cli_util.wrap_exceptions
def update_function_extended(ctx, **kwargs):
    if 'provisioned_concurrency' in kwargs:
        kwargs['provisioned_concurrency_config'] = kwargs['provisioned_concurrency']
        kwargs.pop('provisioned_concurrency')

    ctx.invoke(functionsmanagement_cli.update_function, **kwargs)
