# Copyright (c) 2016, 2023, Oracle and/or its affiliates.
#
# This software is dual-licensed to you under the Universal Permissive License
# (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl and Apache License
# 2.0 as shown at https://www.apache.org/licenses/LICENSE-2.0. You may choose
# either license.
#
# If you elect to accept the software under the Apache License, Version 2.0,
# the following applies:
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click
from services.sch.src.oci_cli_connector_plugins.generated import connectorplugins_cli
from services.sch.src.oci_cli_sch.generated import sch_service_cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias

# Rename list command
cli_util.rename_command(connectorplugins_cli, connectorplugins_cli.connector_plugin_summary_group, connectorplugins_cli.list_connector_plugins, "list")

# Move connector plugins method under root group
connectorplugins_cli.connector_plugins_root_group.commands.pop(connectorplugins_cli.connector_plugin_summary_group.name)
connectorplugins_cli.connector_plugins_root_group.commands.pop(connectorplugins_cli.connector_plugin_group.name)


# Redefine the group to have better help text
@click.command(cli_util.override('connector_plugins.connector_plugins_root_group.command_name', 'connector-plugins'), cls=CommandGroupWithAlias, help=cli_util.override('connector_plugins.connector_plugins_root_group.help', """Example connector plugins include the Queue source and the Notifications target.
For more information about flows defined by connectors, see [Overview of Connector Hub].
For configuration instructions, see [Creating a Connector]."""), short_help=cli_util.override('connector_plugins.connector_plugins_root_group.short_help', """Connector plugins information"""))
@cli_util.help_option_group
def connector_plugins_root_group():
    pass


connector_plugins_root_group.add_command(connectorplugins_cli.list_connector_plugins)
connector_plugins_root_group.add_command(connectorplugins_cli.get_connector_plugin)


# need to remove and add back the group into sch_service_cli to get the previous change
sch_service_cli.sch_service_group.commands.pop(connector_plugins_root_group.name)
sch_service_cli.sch_service_group.add_command(connector_plugins_root_group)
