# Copyright (c) 2016, 2023, Oracle and/or its affiliates.
#
# This software is dual-licensed to you under the Universal Permissive License
# (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl and Apache License
# 2.0 as shown at https://www.apache.org/licenses/LICENSE-2.0. You may choose
# either license.
#
# If you elect to accept the software under the Apache License, Version 2.0,
# the following applies:
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'functions', 'class': 'FunctionSourceDetails'}, 'config': {'module': 'functions', 'class': 'dict(str, string)'}, 'provisioned-concurrency': {'module': 'functions', 'class': 'FunctionProvisionedConcurrencyConfig'}, 'failure-destination': {'module': 'functions', 'class': 'FailureDestinationDetails'}, 'trace-config': {'module': 'functions', 'class': 'FunctionTraceConfig'}, 'freeform-tags': {'module': 'functions', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'functions', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'functions', 'class': 'Function'})
@cli_util.wrap_exceptions
def create_function_extended(ctx, **kwargs):
    if 'provisioned_concurrency' in kwargs:
        kwargs['provisioned_concurrency_config'] = kwargs['provisioned_concurrency']
        kwargs.pop('provisioned_concurrency')

    if not (kwargs.get('source_details') or kwargs.get('image')):
        raise click.UsageError('Must specify --source-details or --image.')

    source_details = {}
    if kwargs.get('source_details') is not None:
        source_details = cli_util.parse_json_parameter("source_details", kwargs.get('source_details'))

    if source_details.get('pbfListingId') and kwargs.get('image'):
        raise click.UsageError('Cannot specify both pbfListingId (in --source-details) and --image.')

    ctx.invoke(functionsmanagement_cli.create_function, **kwargs)


@cli_util.copy_params_from_generated_command(functionsmanagement_cli.update_function, params_to_exclude=['provisioned_concurrency_config'])
@functionsmanagement_cli.function_group.command(name=functionsmanagement_cli.update_function.name, help=functionsmanagement_cli.update_function.help)
@cli_util.option('--provisioned-concurrency', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'config': {'module': 'functions', 'class': 'dict(str, string)'}, 'provisioned-concurrency': {'module': 'functions', 'class': 'FunctionProvisionedConcurrencyConfig'}, 'failure-destination': {'module': 'functions', 'class': 'FailureDestinationDetails'}, 'trace-config': {'module': 'functions', 'class': 'FunctionTraceConfig'}, 'freeform-tags': {'module': 'functions', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'functions', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'functions', 'class': 'Function'})
@cli_util.wrap_exceptions
def update_function_extended(ctx, **kwargs):
    if 'provisioned_concurrency' in kwargs:
        kwargs['provisioned_concurrency_config'] = kwargs['provisioned_concurrency']
        kwargs.pop('provisioned_concurrency')

    ctx.invoke(functionsmanagement_cli.update_function, **kwargs)


# Remove create-function-pre-built-function-source-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.create_function_pre_built_function_source_details.name)


# Remove create-function-none-failure-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.create_function_none_failure_destination_details.name)


# Remove create-function-notification-failure-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.create_function_notification_failure_destination_details.name)


# Remove create-function-queue-failure-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.create_function_queue_failure_destination_details.name)


# Remove create-function-stream-failure-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.create_function_stream_failure_destination_details.name)


# Remove update-function-none-failure-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.update_function_none_failure_destination_details.name)


# Remove update-function-notification-failure-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.update_function_notification_failure_destination_details.name)


# Remove update-function-queue-failure-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.update_function_queue_failure_destination_details.name)


# Remove update-function-stream-failure-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.update_function_stream_failure_destination_details.name)


# Remove create-function-none-success-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.create_function_none_success_destination_details.name)


# Remove create-function-notification-success-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.create_function_notification_success_destination_details.name)


# Remove create-function-queue-success-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.create_function_queue_success_destination_details.name)


# Remove create-function-stream-success-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.create_function_stream_success_destination_details.name)


# Remove update-function-none-success-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.update_function_none_success_destination_details.name)


# Remove update-function-notification-success-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.update_function_notification_success_destination_details.name)


# Remove update-function-queue-success-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.update_function_queue_success_destination_details.name)


# Remove update-function-stream-success-destination-details from oci fn function
functionsmanagement_cli.function_group.commands.pop(functionsmanagement_cli.update_function_stream_success_destination_details.name)
