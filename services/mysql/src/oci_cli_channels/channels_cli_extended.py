# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci_cli import cli_util, json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.cli_util import copy_help_from_generated_code
from services.mysql.src.oci_cli_channels.generated import channels_cli
from services.mysql.src.oci_cli_mysql.generated import mysql_service_cli
import click
import json

# Replace create-channel-create-channel-source-from-mysql-details with create-from-mysql
# rename  oci mysql channel create-channel-create-channel-source-from-mysql-details -> oci mysql channel create-from-mysql
cli_util.rename_command(channels_cli, channels_cli.channel_group, channels_cli.create_channel_create_channel_source_from_mysql_details, "create-from-mysql")


# flatten the single --target parameter into multiple individual --target* params
@cli_util.copy_params_from_generated_command(channels_cli.create_channel_create_channel_source_from_mysql_details, params_to_exclude=['target'])
@channels_cli.channel_group.command(name='create-from-mysql', help=channels_cli.create_channel_create_channel_source_from_mysql_details.help)
@cli_util.option('--target-db-system-id', required=True, help=copy_help_from_generated_code(channels_cli.create_channel_create_channel_target_from_db_system_details, "target_db_system_id", remove_required=False))
@cli_util.option('--target-applier-username', help=copy_help_from_generated_code(channels_cli.create_channel_create_channel_target_from_db_system_details, "target_applier_username", remove_required=False))
@cli_util.option('--target-channel-name', help=copy_help_from_generated_code(channels_cli.create_channel_create_channel_target_from_db_system_details, "target_channel_name", remove_required=False))
@cli_util.option('--target-filters', type=custom_types.CLI_COMPLEX_TYPE, help=copy_help_from_generated_code(channels_cli.create_channel_create_channel_target_from_db_system_details, "target_filters", remove_required=False))
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}, 'source-ssl-ca-certificate': {'module': 'mysql', 'class': 'CaCertificate'}, 'source-anonymous-transactions-handling': {'module': 'mysql', 'class': 'AnonymousTransactionsHandling'}, 'target-filters': {'module': 'mysql', 'class': 'list[ChannelFilter]'}})
@cli_util.wrap_exceptions
def create_channel_create_channel_source_from_mysql_details_extended(ctx, **kwargs):
    target_details = {}

    target_details['dbSystemId'] = kwargs['target_db_system_id']
    kwargs.pop('target_db_system_id')

    if 'target_applier_username' in kwargs and kwargs['target_applier_username'] is not None:
        target_details['applierUsername'] = kwargs['target_applier_username']
    kwargs.pop('target_applier_username')

    if 'target_channel_name' in kwargs and kwargs['target_channel_name'] is not None:
        target_details['channelName'] = kwargs['target_channel_name']
    kwargs.pop('target_channel_name')

    if 'target_filters' in kwargs and kwargs['target_filters'] is not None:
        target_details['filters'] = cli_util.parse_json_parameter("target_filters", kwargs['target_filters'])
    kwargs.pop('target_filters')

    target_details['targetType'] = 'DBSYSTEM'

    if len(target_details) > 0:
        kwargs['target'] = json.dumps(target_details)

    ctx.invoke(channels_cli.create_channel_create_channel_source_from_mysql_details, **kwargs)


# rename  oci mysql channel update_channel_update_channel_source_from_mysql_details -> oci mysql channel update-from-mysql
cli_util.rename_command(channels_cli, channels_cli.channel_group, channels_cli.update_channel_update_channel_source_from_mysql_details, "update-from-mysql")


# flatten the single --target parameter into multiple individual --target* params
@cli_util.copy_params_from_generated_command(channels_cli.update_channel_update_channel_source_from_mysql_details, params_to_exclude=['target'])
@channels_cli.channel_group.command(name='update-from-mysql', help=channels_cli.update_channel_update_channel_source_from_mysql_details.help)
@cli_util.option('--target-applier-username', help=copy_help_from_generated_code(channels_cli.update_channel_update_channel_target_from_db_system_details, "target_applier_username", remove_required=False))
@cli_util.option('--target-channel-name', help=copy_help_from_generated_code(channels_cli.update_channel_update_channel_target_from_db_system_details, "target_channel_name", remove_required=False))
@cli_util.option('--target-filters', type=custom_types.CLI_COMPLEX_TYPE, help=copy_help_from_generated_code(channels_cli.update_channel_update_channel_target_from_db_system_details, "target_filters", remove_required=False))
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}, 'source-ssl-ca-certificate': {'module': 'mysql', 'class': 'CaCertificate'}, 'source-anonymous-transactions-handling': {'module': 'mysql', 'class': 'AnonymousTransactionsHandling'}, 'target-filters': {'module': 'mysql', 'class': 'list[ChannelFilter]'}})
@cli_util.wrap_exceptions
def update_channel_update_channel_source_from_mysql_details_extended(ctx, **kwargs):
    target_details = {}

    if 'target_applier_username' in kwargs and kwargs['target_applier_username'] is not None:
        target_details['applierUsername'] = kwargs['target_applier_username']
    kwargs.pop('target_applier_username')

    if 'target_channel_name' in kwargs and kwargs['target_channel_name'] is not None:
        target_details['channelName'] = kwargs['target_channel_name']
    kwargs.pop('target_channel_name')

    if 'target_filters' in kwargs and kwargs['target_filters'] is not None:
        target_details['filters'] = cli_util.parse_json_parameter("target_filters", kwargs['target_filters'])
    kwargs.pop('target_filters')

    target_details['targetType'] = 'DBSYSTEM'

    if len(target_details) > 0:
        kwargs['target'] = json.dumps(target_details)

    # The current WARNING mentions --target, so we need to bypass it
    freeform_tags = False
    if 'freeform_tags' in kwargs and kwargs['freeform_tags'] is not None:
        freeform_tags = True

    defined_tags = False
    if 'defined_tags' in kwargs and kwargs['defined_tags'] is not None:
        freeform_tags = True

    if not kwargs['force'] and (freeform_tags or defined_tags):
        if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
            ctx.abort()

    kwargs['force'] = True
    ctx.invoke(channels_cli.update_channel_update_channel_source_from_mysql_details, **kwargs)


# remove create, create-channel-create-channel-target-from-db-system-details, update,
# and update-channel-update-channel-target-from-db-system-details
channels_cli.channel_group.commands.pop(channels_cli.create_channel.name)
channels_cli.channel_group.commands.pop(channels_cli.create_channel_create_channel_target_from_db_system_details.name)
channels_cli.channel_group.commands.pop(channels_cli.update_channel.name)
channels_cli.channel_group.commands.pop(channels_cli.update_channel_update_channel_target_from_db_system_details.name)

# oci mysql channels channel -> oci mysql channel
mysql_service_cli.mysql_service_group.commands.pop(channels_cli.channels_root_group.name)
mysql_service_cli.mysql_service_group.add_command(channels_cli.channel_group)
