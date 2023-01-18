# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('identity_data_plane.identity_data_plane_root_group.command_name', 'identity-data-plane'), cls=CommandGroupWithAlias, help=cli_util.override('identity_data_plane.identity_data_plane_root_group.help', """API for the Identity Dataplane"""), short_help=cli_util.override('identity_data_plane.identity_data_plane_root_group.short_help', """Identity Service"""))
@cli_util.help_option_group
def identity_data_plane_root_group():
    pass


@click.command(cli_util.override('identity_data_plane.security_token_group.command_name', 'security-token'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def security_token_group():
    pass


identity_data_plane_root_group.add_command(security_token_group)


@security_token_group.command(name=cli_util.override('identity_data_plane.generate_scoped_access_token.command_name', 'generate-scoped-access-token'), help=u"""Based on the calling principal and the input payload, derive the claims and create a security token. \n[Command Reference](generateScopedAccessToken)""")
@cli_util.option('--scope', required=True, help=u"""Scope definition for the scoped access token""")
@cli_util.option('--public-key', required=True, help=u"""A temporary public key, owned by the service. The service also owns the corresponding private key. This public key will by put inside the security token by the auth service after successful validation of the certificate.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity_data_plane', 'class': 'SecurityToken'})
@cli_util.wrap_exceptions
def generate_scoped_access_token(ctx, from_json, scope, public_key):

    kwargs = {}

    _details = {}
    _details['scope'] = scope
    _details['publicKey'] = public_key

    client = cli_util.build_client('identity_data_plane', 'dataplane', ctx)
    result = client.generate_scoped_access_token(
        generate_scoped_access_token_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
