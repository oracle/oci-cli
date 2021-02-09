# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.compute_instance_agent.src.oci_cli_plugin.generated import plugin_cli
from services.compute_instance_agent.src.oci_cli_compute_instance_agent.generated import instance_agent_service_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401

cli_util.rename_command(plugin_cli, plugin_cli.plugin_group, plugin_cli.get_instance_agent_plugin, "get")
cli_util.rename_command(plugin_cli, plugin_cli.plugin_group, plugin_cli.list_instance_agent_plugins, "list")

# Move commands under 'oci instance-agent plugin plugin' -> 'oci instance-agent plugin'
instance_agent_service_cli.instance_agent_service_group.commands.pop(plugin_cli.plugin_root_group.name)
instance_agent_service_cli.instance_agent_service_group.add_command(plugin_cli.plugin_group)
