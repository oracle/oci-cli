# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('operator_control_assignment.opctl_service_group.command_name', 'opctl'), cls=CommandGroupWithAlias, help=cli_util.override('operator_control_assignment.opctl_service_group.help', """Operator Access Control enables you to control the time duration and the actions an Oracle operator can perform on your Exadata Cloud@Customer infrastructure.
Using logging service, you can view a near real-time audit report of all actions performed by an Oracle operator.

Use the table of contents and search tool to explore the OperatorAccessControl API."""), short_help=cli_util.override('operator_control_assignment.opctl_service_group.short_help', """OperatorAccessControl API"""))
@cli_util.help_option_group
def opctl_service_group():
    pass
