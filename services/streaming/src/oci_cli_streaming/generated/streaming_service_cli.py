# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('streaming_service_group.command_name', 'streaming'), cls=CommandGroupWithAlias, help=cli_util.override('streaming_service_group.help', """The API for the Streaming Service."""), short_help=cli_util.override('streaming_service_group.short_help', """Streaming Service API"""))
@cli_util.help_option_group
def streaming_service_group():
    pass
