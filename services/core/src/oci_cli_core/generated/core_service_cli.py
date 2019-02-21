# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('core_service_group.command_name', 'core'), cls=CommandGroupWithAlias, help=cli_util.override('core_service_group.help', """APIs for Networking Service, Compute Service, and Block Volume Service."""), short_help=cli_util.override('core_service_group.short_help', """Core Services API"""))
@cli_util.help_option_group
def core_service_group():
    pass
