# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
from services.integration.src.oci_cli_integration_instance.generated import integrationinstance_cli
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils
from oci_cli import cli_util


# Rename integration-instance-id -> id for all parameters
# Rename integration-instance-type -> type for all parameters
@cli_util.copy_params_from_generated_command(integrationinstance_cli.change_integration_instance_compartment, params_to_exclude=['integration_instance_id'])
@integrationinstance_cli.integration_instance_group.command(name=cli_util.override('integration.change_integration_instance_compartment.command_name', 'change-compartment'), help=integrationinstance_cli.change_integration_instance_compartment.help)
@cli_util.option('--id', required=True, help=u"""Unique Integration Instance identifier.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_integration_instance_compartment_extended(ctx, **kwargs):
    if 'id' in kwargs:
        kwargs['integration_instance_id'] = kwargs['id']
        kwargs.pop('id')
    ctx.invoke(integrationinstance_cli.change_integration_instance_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(integrationinstance_cli.start_integration_instance, params_to_exclude=['integration_instance_id'])
@integrationinstance_cli.integration_instance_group.command(name=cli_util.override('integration.start_integration_instance.command_name', 'start'), help=integrationinstance_cli.start_integration_instance.help)
@cli_util.option('--id', required=True, help=u"""Unique Integration Instance identifier.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def start_integration_instance_extended(ctx, **kwargs):
    if 'id' in kwargs:
        kwargs['integration_instance_id'] = kwargs['id']
        kwargs.pop('id')
    ctx.invoke(integrationinstance_cli.start_integration_instance, **kwargs)


@cli_util.copy_params_from_generated_command(integrationinstance_cli.stop_integration_instance, params_to_exclude=['integration_instance_id'])
@integrationinstance_cli.integration_instance_group.command(name=cli_util.override('integration.stop_integration_instance.command_name', 'stop'), help=integrationinstance_cli.stop_integration_instance.help)
@cli_util.option('--id', required=True, help=u"""Unique Integration Instance identifier.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def stop_integration_instance_extended(ctx, **kwargs):
    if 'id' in kwargs:
        kwargs['integration_instance_id'] = kwargs['id']
        kwargs.pop('id')
    ctx.invoke(integrationinstance_cli.stop_integration_instance, **kwargs)


@cli_util.copy_params_from_generated_command(integrationinstance_cli.delete_integration_instance, params_to_exclude=['integration_instance_id'])
@integrationinstance_cli.integration_instance_group.command(name=cli_util.override('integration.delete_integration_instance.command_name', 'delete'), help=integrationinstance_cli.delete_integration_instance.help)
@cli_util.option('--id', required=True, help=u"""Unique Integration Instance identifier.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_integration_instance_extended(ctx, **kwargs):
    if 'id' in kwargs:
        kwargs['integration_instance_id'] = kwargs['id']
        kwargs.pop('id')
    ctx.invoke(integrationinstance_cli.delete_integration_instance, **kwargs)


@cli_util.copy_params_from_generated_command(integrationinstance_cli.get_integration_instance, params_to_exclude=['integration_instance_id'])
@integrationinstance_cli.integration_instance_group.command(name=cli_util.override('integration.get_integration_instance.command_name', 'get'), help=integrationinstance_cli.get_integration_instance.help)
@cli_util.option('--id', required=True, help=u"""Unique Integration Instance identifier.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'integration', 'class': 'IntegrationInstance'})
@cli_util.wrap_exceptions
def get_integration_instance_extended(ctx, **kwargs):
    if 'id' in kwargs:
        kwargs['integration_instance_id'] = kwargs['id']
        kwargs.pop('id')
    ctx.invoke(integrationinstance_cli.get_integration_instance, **kwargs)


@cli_util.copy_params_from_generated_command(integrationinstance_cli.list_work_requests, params_to_exclude=['integration_instance_id'])
@integrationinstance_cli.work_request_group.command(name=cli_util.override('integration.list_work_requests.command_name', 'list'), help=integrationinstance_cli.list_work_requests.help)
@cli_util.option('--id', required=True, help=u"""Unique Integration Instance identifier.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'integration', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests_extended(ctx, **kwargs):
    if 'id' in kwargs:
        kwargs['integration_instance_id'] = kwargs['id']
        kwargs.pop('id')
    ctx.invoke(integrationinstance_cli.list_work_requests, **kwargs)


@cli_util.copy_params_from_generated_command(integrationinstance_cli.update_integration_instance, params_to_exclude=['integration_instance_id', 'integration_instance_type'])
@integrationinstance_cli.integration_instance_group.command(name=cli_util.override('integration.update_integration_instance.command_name', 'update'), help=integrationinstance_cli.update_integration_instance.help)
@cli_util.option('--id', required=True, help=u"""Unique Integration Instance identifier.""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["STANDARD", "ENTERPRISE"]), help=u"""Standard or Enterprise type""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'integration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'integration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_integration_instance_extended(ctx, **kwargs):
    if 'id' in kwargs:
        kwargs['integration_instance_id'] = kwargs['id']
        kwargs.pop('id')

    if 'type' in kwargs:
        kwargs['integration_instance_type'] = kwargs['type']
        kwargs.pop('type')
    ctx.invoke(integrationinstance_cli.update_integration_instance, **kwargs)


@cli_util.copy_params_from_generated_command(integrationinstance_cli.create_integration_instance, params_to_exclude=['integration_instance_type'])
@integrationinstance_cli.integration_instance_group.command(name=cli_util.override('integration.create_integration_instance.command_name', 'create'), help=integrationinstance_cli.create_integration_instance.help)
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["STANDARD", "ENTERPRISE"]), help=u"""Standard or Enterprise type""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'integration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'integration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_integration_instance_extended(ctx, **kwargs):
    if 'type' in kwargs:
        kwargs['integration_instance_type'] = kwargs['type']
        kwargs.pop('type')
    ctx.invoke(integrationinstance_cli.create_integration_instance, **kwargs)
