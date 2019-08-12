# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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
from services.dts.src.oci_cli_dts.generated import dts_service_cli


@click.command(cli_util.override('transfer_appliance_entitlement_root_group.command_name', 'transfer-appliance-entitlement'), cls=CommandGroupWithAlias, help=cli_util.override('transfer_appliance_entitlement_root_group.help', """A description of the DTS API"""), short_help=cli_util.override('transfer_appliance_entitlement_root_group.short_help', """DTS API"""))
@cli_util.help_option_group
def transfer_appliance_entitlement_root_group():
    pass


@click.command(cli_util.override('transfer_appliance_entitlement_group.command_name', 'transfer-appliance-entitlement'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def transfer_appliance_entitlement_group():
    pass


dts_service_cli.dts_service_group.add_command(transfer_appliance_entitlement_root_group)
transfer_appliance_entitlement_root_group.add_command(transfer_appliance_entitlement_group)


@transfer_appliance_entitlement_group.command(name=cli_util.override('create_transfer_appliance_entitlement.command_name', 'create'), help=u"""Create the Transfer Appliance Entitlement that allows customers to use Transfer Appliance""")
@cli_util.option('--compartment-id', help=u"""""")
@cli_util.option('--requestor-name', help=u"""""")
@cli_util.option('--requestor-email', help=u"""""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'TransferApplianceEntitlement'})
@cli_util.wrap_exceptions
def create_transfer_appliance_entitlement(ctx, from_json, compartment_id, requestor_name, requestor_email):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if compartment_id is not None:
        details['compartmentId'] = compartment_id

    if requestor_name is not None:
        details['requestorName'] = requestor_name

    if requestor_email is not None:
        details['requestorEmail'] = requestor_email

    client = cli_util.build_client('transfer_appliance_entitlement', ctx)
    result = client.create_transfer_appliance_entitlement(
        create_transfer_appliance_entitlement_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transfer_appliance_entitlement_group.command(name=cli_util.override('get_transfer_appliance_entitlement.command_name', 'get'), help=u"""Describes the Transfer Appliance Entitlement in detail""")
@cli_util.option('--tenant-id', required=True, help=u"""Tenant Id""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'TransferApplianceEntitlement'})
@cli_util.wrap_exceptions
def get_transfer_appliance_entitlement(ctx, from_json, tenant_id):

    if isinstance(tenant_id, six.string_types) and len(tenant_id.strip()) == 0:
        raise click.UsageError('Parameter --tenant-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('transfer_appliance_entitlement', ctx)
    result = client.get_transfer_appliance_entitlement(
        tenant_id=tenant_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)
