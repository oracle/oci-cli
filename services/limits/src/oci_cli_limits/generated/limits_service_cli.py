# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('quotas.limits_service_group.command_name', 'limits'), cls=CommandGroupWithAlias, help=cli_util.override('quotas.limits_service_group.help', """APIs that interact with the resource limits of a specific resource type"""), short_help=cli_util.override('quotas.limits_service_group.short_help', """Service limits APIs"""))
@cli_util.help_option_group
def limits_service_group():
    pass
