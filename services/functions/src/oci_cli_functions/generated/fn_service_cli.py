# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('functions_management.fn_service_group.command_name', 'fn'), cls=CommandGroupWithAlias, help=cli_util.override('functions_management.fn_service_group.help', """API for the Functions service."""), short_help=cli_util.override('functions_management.fn_service_group.short_help', """Functions Service API"""))
@cli_util.help_option_group
def fn_service_group():
    pass
