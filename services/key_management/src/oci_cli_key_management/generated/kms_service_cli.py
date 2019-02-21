# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('kms_service_group.command_name', 'kms'), cls=CommandGroupWithAlias, help=cli_util.override('kms_service_group.help', """API for managing and performing operations with keys and vaults."""), short_help=cli_util.override('kms_service_group.short_help', """Key Management Service API"""))
@cli_util.help_option_group
def kms_service_group():
    pass
