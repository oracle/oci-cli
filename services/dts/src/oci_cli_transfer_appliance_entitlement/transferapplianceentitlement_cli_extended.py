# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


# NOTE: This file has been commented because the feature is not ready for public release
#       Once the feature is ready, this should be brought back

import click

from oci import exceptions
from oci.response import Response
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from services.dts.src.oci_cli_transfer_appliance_entitlement.generated import transferapplianceentitlement_cli
from services.dts.src.oci_cli_transfer_appliance.generated import transferappliance_cli


@cli_util.copy_params_from_generated_command(transferapplianceentitlement_cli.create_transfer_appliance_entitlement, params_to_exclude=['compartment_id', 'requestor_name', 'requestor_email'])
@transferappliance_cli.transfer_appliance_root_group.command(
    name=transferapplianceentitlement_cli.create_transfer_appliance_entitlement.name,
    help=transferapplianceentitlement_cli.create_transfer_appliance_entitlement.help)
@cli_util.option('--compartment-id', required=True, help=u"""Root compartment OCID""")
@cli_util.option('--name', required=True, help=u"""Requestor name""")
@cli_util.option('--email', required=True, help=u"""Requestor email""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dts', 'class': 'TransferJob'})
@cli_util.wrap_exceptions
def create_transfer_appliance_entitlement_extended(ctx, **kwargs):
    if 'name' in kwargs:
        kwargs['requestor_name'] = kwargs['name']
        kwargs.pop('name')
    if 'email' in kwargs:
        kwargs['requestor_email'] = kwargs['email']
        kwargs.pop('email')
    ctx.invoke(transferapplianceentitlement_cli.create_transfer_appliance_entitlement, **kwargs)


@cli_util.copy_params_from_generated_command(transferapplianceentitlement_cli.get_transfer_appliance_entitlement, params_to_exclude=['id'])
@transferappliance_cli.transfer_appliance_root_group.command(
    name=transferapplianceentitlement_cli.get_transfer_appliance_entitlement.name,
    help=transferapplianceentitlement_cli.get_transfer_appliance_entitlement.help)
@cli_util.option('--compartment-id', required=True, help=u"""Root compartment OCID""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dts', 'class': 'TransferJob'})
@cli_util.wrap_exceptions
def get_transfer_appliance_entitlement_extended(ctx, **kwargs):
    list_kwargs = {
        'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    }
    client = cli_util.build_client('dts', 'transfer_appliance_entitlement', ctx)
    compartment_id = kwargs['compartment_id']
    entitlements_list = client.list_transfer_appliance_entitlement(compartment_id=compartment_id, **list_kwargs)
    if len(entitlements_list.data) < 1:
        raise exceptions.RequestException(
            "Unable to find Transfer Appliance Entitlement in compartment {}".format(compartment_id))
    # The entitlement ID can be None when the entitlement was created in let's say PHX but accessed from IAD
    if entitlements_list.data[0].id is None:
        custom_response = Response(200, {}, entitlements_list.data[0], None)
        cli_util.render_response(custom_response, ctx)
    else:
        kwargs['id'] = entitlements_list.data[0].id
        del kwargs['compartment_id']
        ctx.invoke(transferapplianceentitlement_cli.get_transfer_appliance_entitlement, **kwargs)
