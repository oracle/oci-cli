# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('user.support_service_group.command_name', 'support'), cls=CommandGroupWithAlias, help=cli_util.override('user.support_service_group.help', """Use the Support Management API to manage support requests. For more information, see [Getting Help and Contacting Support]. **Note**: Before you can create service requests with this API, you need to have an Oracle Single Sign On (SSO) account, and you need to register your Customer Support Identifier (CSI) with My Oracle Support."""), short_help=cli_util.override('user.support_service_group.short_help', """Support Management API"""))
@cli_util.help_option_group
def support_service_group():
    pass
