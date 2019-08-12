# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# NOTE: This file has been commented because the feature is not ready for public release
#       Once the feature is ready, this should be brought back

# import click
#
# from oci_cli import cli_util
# from services.dts.src.oci_cli_transfer_appliance_entitlement.generated import transferapplianceentitlement_cli
#
#
# @cli_util.copy_params_from_generated_command(transferapplianceentitlement_cli.create_transfer_appliance_entitlement, params_to_exclude=['tenent_id', 'requestor_name', 'requestor_email'])
# @transferapplianceentitlement_cli.transfer_appliance_entitlement_root_group.command(
#     name=transferapplianceentitlement_cli.create_transfer_appliance_entitlement.name,
#     help=transferapplianceentitlement_cli.create_transfer_appliance_entitlement.help)
# @cli_util.option('--tenant-id', required=True, help=u"""Tenant ID""")
# @cli_util.option('--name', required=True, help=u"""Requestor name""")
# @cli_util.option('--email', required=True, help=u"""Requestor email""")
# @click.pass_context
# @cli_util.wrap_exceptions
# def create_entitlement_extended(ctx, **kwargs):
#     if 'name' in kwargs:
#         kwargs['requestor_name'] = kwargs['name']
#         kwargs.pop('name')
#     if 'email' in kwargs:
#         kwargs['requestor_email'] = kwargs['email']
#         kwargs.pop('email')
#     ctx.invoke(transferapplianceentitlement_cli.create_transfer_appliance_entitlement, **kwargs)
