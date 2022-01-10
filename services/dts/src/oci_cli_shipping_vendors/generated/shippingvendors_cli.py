# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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
from services.dts.src.oci_cli_dts.generated import dts_service_cli


@click.command(cli_util.override('shipping_vendors.shipping_vendors_root_group.command_name', 'shipping-vendors'), cls=CommandGroupWithAlias, help=cli_util.override('shipping_vendors.shipping_vendors_root_group.help', """Data Transfer Service API Specification"""), short_help=cli_util.override('shipping_vendors.shipping_vendors_root_group.short_help', """Data Transfer Service API"""))
@cli_util.help_option_group
def shipping_vendors_root_group():
    pass


@click.command(cli_util.override('shipping_vendors.shipping_vendors_group.command_name', 'shipping-vendors'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def shipping_vendors_group():
    pass


dts_service_cli.dts_service_group.add_command(shipping_vendors_root_group)
shipping_vendors_root_group.add_command(shipping_vendors_group)


@shipping_vendors_group.command(name=cli_util.override('shipping_vendors.list_shipping_vendors.command_name', 'list'), help=u"""Lists available shipping vendors for Transfer Package delivery \n[Command Reference](listShippingVendors)""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'ShippingVendors'})
@cli_util.wrap_exceptions
def list_shipping_vendors(ctx, from_json, all_pages, ):

    kwargs = {}
    client = cli_util.build_client('dts', 'shipping_vendors', ctx)
    result = client.list_shipping_vendors(
        **kwargs
    )
    cli_util.render_response(result, ctx)
