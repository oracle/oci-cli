# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('notification_data_plane.ons_service_group.command_name', 'ons'), cls=CommandGroupWithAlias, help=cli_util.override('notification_data_plane.ons_service_group.help', """Use the Notifications API to broadcast messages to distributed components by topic, using a publish-subscribe pattern.
For information about managing topics, subscriptions, and messages, see [Notifications Overview]."""), short_help=cli_util.override('notification_data_plane.ons_service_group.short_help', """Notifications API"""))
@cli_util.help_option_group
def ons_service_group():
    pass
