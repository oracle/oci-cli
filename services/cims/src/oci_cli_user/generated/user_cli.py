# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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
from services.cims.src.oci_cli_cims.generated import support_service_cli


@click.command(cli_util.override('user.user_root_group.command_name', 'user'), cls=CommandGroupWithAlias, help=cli_util.override('user.user_root_group.help', """Use the Support Management API to manage support requests. For more information, see [Getting Help and Contacting Support]. **Note**: Before you can create service requests with this API, you need to have an Oracle Single Sign On (SSO) account, and you need to register your Customer Support Identifier (CSI) with My Oracle Support."""), short_help=cli_util.override('user.user_root_group.short_help', """Support Management API"""))
@cli_util.help_option_group
def user_root_group():
    pass


@click.command(cli_util.override('user.user_group.command_name', 'user'), cls=CommandGroupWithAlias, help="""Details about the user object.""")
@cli_util.help_option_group
def user_group():
    pass


support_service_cli.support_service_group.add_command(user_root_group)
user_root_group.add_command(user_group)


@user_group.command(name=cli_util.override('user.create_user.command_name', 'create'), help=u"""Create user to request Customer Support Identifier(CSI) to Customer User Administrator(CUA). \n[Command Reference](createUser)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenancy.""")
@cli_util.option('--first-name', required=True, help=u"""First name of the user.""")
@cli_util.option('--last-name', required=True, help=u"""Last name of the user.""")
@cli_util.option('--country', required=True, help=u"""Country of the user.""")
@cli_util.option('--csi', required=True, help=u"""CSI to be associated to the user.""")
@cli_util.option('--phone', required=True, help=u"""Contact number of the user.""")
@cli_util.option('--timezone', required=True, help=u"""Timezone of the user.""")
@cli_util.option('--organization-name', required=True, help=u"""Organization of the user.""")
@cli_util.option('--ocid', required=True, help=u"""User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.""")
@cli_util.option('--homeregion', help=u"""The region of the tenancy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cims', 'class': 'User'})
@cli_util.wrap_exceptions
def create_user(ctx, from_json, compartment_id, first_name, last_name, country, csi, phone, timezone, organization_name, ocid, homeregion):

    kwargs = {}
    if homeregion is not None:
        kwargs['homeregion'] = homeregion
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['firstName'] = first_name
    _details['lastName'] = last_name
    _details['country'] = country
    _details['csi'] = csi
    _details['phone'] = phone
    _details['timezone'] = timezone
    _details['organizationName'] = organization_name

    client = cli_util.build_client('cims', 'user', ctx)
    result = client.create_user(
        ocid=ocid,
        create_user_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
