# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('transfer_package.dts_service_group.command_name', 'dts'), cls=CommandGroupWithAlias, help=cli_util.override('transfer_package.dts_service_group.help', """Data Transfer Service API Specification"""), short_help=cli_util.override('transfer_package.dts_service_group.short_help', """Data Transfer Service API"""))
@cli_util.help_option_group
def dts_service_group():
    pass
