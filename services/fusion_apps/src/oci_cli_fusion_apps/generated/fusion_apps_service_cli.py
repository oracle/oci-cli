# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('service_attachment.fusion_apps_service_group.command_name', 'fusion-apps'), cls=CommandGroupWithAlias, help=cli_util.override('service_attachment.fusion_apps_service_group.help', """Use the Fusion Applications Environment Management API to manage the environments where your Fusion Applications run. For more information, see the [Fusion Applications Environment Management documentation]."""), short_help=cli_util.override('service_attachment.fusion_apps_service_group.short_help', """Fusion Applications Environment Management API"""))
@cli_util.help_option_group
def fusion_apps_service_group():
    pass
