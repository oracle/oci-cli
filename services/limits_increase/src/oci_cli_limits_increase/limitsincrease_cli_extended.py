# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.limits_increase.src.oci_cli_limits_increase.generated import limitsincrease_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci limits-increase limits-increase-question-collection list-limits-increase-questions -> oci limits-increase limits-increase-question-collection list
cli_util.rename_command(limitsincrease_cli, limitsincrease_cli.limits_increase_question_collection_group, limitsincrease_cli.list_limits_increase_questions, "list")


# oci limits-increase limits-increase-item-request-collection list-limits-increase-item-requests -> oci limits-increase limits-increase-item-request-collection list
cli_util.rename_command(limitsincrease_cli, limitsincrease_cli.limits_increase_item_request_collection_group, limitsincrease_cli.list_limits_increase_item_requests, "list")


# oci limits-increase limits-increase-question-collection -> oci limits-increase question
cli_util.rename_command(limitsincrease_cli, limitsincrease_cli.limits_increase_root_group, limitsincrease_cli.limits_increase_question_collection_group, "question")


# oci limits-increase limits-increase-item-request -> oci limits-increase item
cli_util.rename_command(limitsincrease_cli, limitsincrease_cli.limits_increase_root_group, limitsincrease_cli.limits_increase_item_request_group, "item")


# Move commands under 'oci limits-increase limits-increase-item-request-collection' -> 'oci limits-increase limits-increase-item-request'
limitsincrease_cli.limits_increase_root_group.commands.pop(limitsincrease_cli.limits_increase_item_request_collection_group.name)
limitsincrease_cli.limits_increase_item_request_group.add_command(limitsincrease_cli.list_limits_increase_item_requests)


@cli_util.copy_params_from_generated_command(limitsincrease_cli.update_limits_increase_request, params_to_exclude=['limits_increase_request_id'])
@limitsincrease_cli.limits_increase_request_group.command(name=limitsincrease_cli.update_limits_increase_request.name, help=limitsincrease_cli.update_limits_increase_request.help)
@cli_util.option('--id', required=True, help=u"""The [OCID] of the limit increase request. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'limits_increase', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'limits_increase', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'limits_increase', 'class': 'LimitsIncreaseRequest'})
@cli_util.wrap_exceptions
def update_limits_increase_request_extended(ctx, **kwargs):

    if 'id' in kwargs:
        kwargs['limits_increase_request_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(limitsincrease_cli.update_limits_increase_request, **kwargs)


@cli_util.copy_params_from_generated_command(limitsincrease_cli.patch_limits_increase_request, params_to_exclude=['limits_increase_request_id'])
@limitsincrease_cli.limits_increase_request_group.command(name=limitsincrease_cli.patch_limits_increase_request.name, help=limitsincrease_cli.patch_limits_increase_request.help)
@cli_util.option('--id', required=True, help=u"""The [OCID] of the limit increase request. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'limits_increase', 'class': 'list[PatchInstruction]'}}, output_type={'module': 'limits_increase', 'class': 'LimitsIncreaseRequest'})
@cli_util.wrap_exceptions
def patch_limits_increase_request_extended(ctx, **kwargs):

    if 'id' in kwargs:
        kwargs['limits_increase_request_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(limitsincrease_cli.patch_limits_increase_request, **kwargs)


@cli_util.copy_params_from_generated_command(limitsincrease_cli.get_limits_increase_request, params_to_exclude=['limits_increase_request_id'])
@limitsincrease_cli.limits_increase_request_group.command(name=limitsincrease_cli.get_limits_increase_request.name, help=limitsincrease_cli.get_limits_increase_request.help)
@cli_util.option('--id', required=True, help=u"""The [OCID] of the limit increase request. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'limits_increase', 'class': 'LimitsIncreaseRequest'})
@cli_util.wrap_exceptions
def get_limits_increase_request_extended(ctx, **kwargs):

    if 'id' in kwargs:
        kwargs['limits_increase_request_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(limitsincrease_cli.get_limits_increase_request, **kwargs)


@cli_util.copy_params_from_generated_command(limitsincrease_cli.delete_limits_increase_request, params_to_exclude=['limits_increase_request_id'])
@limitsincrease_cli.limits_increase_request_group.command(name=limitsincrease_cli.delete_limits_increase_request.name, help=limitsincrease_cli.delete_limits_increase_request.help)
@cli_util.option('--id', required=True, help=u"""The [OCID] of the limit increase request. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_limits_increase_request_extended(ctx, **kwargs):

    if 'id' in kwargs:
        kwargs['limits_increase_request_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(limitsincrease_cli.delete_limits_increase_request, **kwargs)


@cli_util.copy_params_from_generated_command(limitsincrease_cli.create_limits_increase_request, params_to_exclude=['limits_increase_item_requests'])
@limitsincrease_cli.limits_increase_request_group.command(name=limitsincrease_cli.create_limits_increase_request.name, help=limitsincrease_cli.create_limits_increase_request.help)
@cli_util.option('--items', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of items in the limit increase request.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'limits-increase-item-requests': {'module': 'limits_increase', 'class': 'list[CreateLimitsIncreaseItemRequestDetails]'}, 'freeform-tags': {'module': 'limits_increase', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'limits_increase', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'limits_increase', 'class': 'LimitsIncreaseRequest'})
@cli_util.wrap_exceptions
def create_limits_increase_request_extended(ctx, **kwargs):

    if 'items' in kwargs:
        kwargs['limits_increase_item_requests'] = kwargs['items']
        kwargs.pop('items')

    ctx.invoke(limitsincrease_cli.create_limits_increase_request, **kwargs)


@cli_util.copy_params_from_generated_command(limitsincrease_cli.cancel_limits_increase_request, params_to_exclude=['limits_increase_request_id'])
@limitsincrease_cli.limits_increase_request_group.command(name=limitsincrease_cli.cancel_limits_increase_request.name, help=limitsincrease_cli.cancel_limits_increase_request.help)
@cli_util.option('--id', required=True, help=u"""The [OCID] of the limit increase request. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'limits_increase', 'class': 'LimitsIncreaseRequest'})
@cli_util.wrap_exceptions
def cancel_limits_increase_request_extended(ctx, **kwargs):

    if 'id' in kwargs:
        kwargs['limits_increase_request_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(limitsincrease_cli.cancel_limits_increase_request, **kwargs)


@cli_util.copy_params_from_generated_command(limitsincrease_cli.get_limits_increase_item_request, params_to_exclude=['limits_increase_item_request_id'])
@limitsincrease_cli.limits_increase_item_request_group.command(name=limitsincrease_cli.get_limits_increase_item_request.name, help=limitsincrease_cli.get_limits_increase_item_request.help)
@cli_util.option('--id', required=True, help=u"""The [OCID] of the limit increase request. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'limits_increase', 'class': 'LimitsIncreaseItemRequest'})
@cli_util.wrap_exceptions
def get_limits_increase_item_request_extended(ctx, **kwargs):

    if 'id' in kwargs:
        kwargs['limits_increase_item_request_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(limitsincrease_cli.get_limits_increase_item_request, **kwargs)


@cli_util.copy_params_from_generated_command(limitsincrease_cli.cancel_limits_increase_item_request, params_to_exclude=['limits_increase_item_request_id'])
@limitsincrease_cli.limits_increase_item_request_group.command(name=limitsincrease_cli.cancel_limits_increase_item_request.name, help=limitsincrease_cli.cancel_limits_increase_item_request.help)
@cli_util.option('--id', required=True, help=u"""The [OCID] of the limit increase request. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'limits_increase', 'class': 'LimitsIncreaseItemRequest'})
@cli_util.wrap_exceptions
def cancel_limits_increase_item_request_extended(ctx, **kwargs):

    if 'id' in kwargs:
        kwargs['limits_increase_item_request_id'] = kwargs['id']
        kwargs.pop('id')

    ctx.invoke(limitsincrease_cli.cancel_limits_increase_item_request, **kwargs)
