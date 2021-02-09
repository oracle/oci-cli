# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.compute_instance_agent.src.oci_cli_pluginconfig.generated import pluginconfig_cli
from services.compute_instance_agent.src.oci_cli_compute_instance_agent.generated import instance_agent_service_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci instance-agent pluginconfig plugin list-instanceagent-available -> oci instance-agent pluginconfig plugin get
cli_util.rename_command(pluginconfig_cli, pluginconfig_cli.plugin_group, pluginconfig_cli.list_instanceagent_available_plugins, "get")

cli_util.rename_command(instance_agent_service_cli, instance_agent_service_cli.instance_agent_service_group, pluginconfig_cli.pluginconfig_root_group, "available-plugins")

# Move commands under 'oci instance-agent pluginconfig plugin' -> 'oci instance-agent pluginconfig'
pluginconfig_cli.pluginconfig_root_group.commands.pop(pluginconfig_cli.plugin_group.name)
pluginconfig_cli.pluginconfig_root_group.add_command(pluginconfig_cli.list_instanceagent_available_plugins)
