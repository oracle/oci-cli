# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click
from oci_cli import cli_util
from oci_cli import custom_types
from oci_cli import json_skeleton_utils
from services.media_services.src.oci_cli_media_stream.generated import mediastream_cli
from services.media_services.src.oci_cli_media_stream.generated.mediastream_cli import stream_distribution_channel_group

mediastream_cli.stream_distribution_channel_group.commands.pop(mediastream_cli.generate_session_token.name)


@stream_distribution_channel_group.command(name=cli_util.override('media_stream.generate_session_token.command_name', 'generate-session-token'), help=u"""Generate a new streaming session token \n[Command Reference](generateSessionToken)""")
@cli_util.option('--scopes', required=True, type=custom_types.CliCaseInsensitiveChoice(["PLAYLIST", "EDGE"]), multiple=True, help=u"""Array of scopes the token can act upon""")
@cli_util.option('--packaging-config-id', required=True, help=u"""The packaging config resource identifier used to limit the scope of the token""")
@cli_util.option('--time-expires', type=custom_types.CLI_DATETIME, help=u"""Token expiry time. An RFC3339 formatted datetime string""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--asset-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of asset resource Ids used to limit the scope of the token""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'asset-ids': {'module': 'media_services', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-ids': {'module': 'media_services', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def generate_session_token(ctx, from_json, scopes, packaging_config_id, time_expires, asset_ids):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['scopes'] = cli_util.parse_json_parameter("scopes", scopes)
    _details['packagingConfigId'] = packaging_config_id

    if time_expires is not None:
        _details['timeExpires'] = time_expires

    if asset_ids is not None:
        _details['assetIds'] = cli_util.parse_json_parameter("asset_ids", asset_ids)

    client = cli_util.build_client('media_services', 'media_stream', ctx)
    result = client.generate_session_token(
        generate_session_token_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
