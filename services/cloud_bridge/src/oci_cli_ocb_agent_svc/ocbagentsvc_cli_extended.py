# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.cloud_bridge.src.oci_cli_ocb_agent_svc.generated import ocbagentsvc_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci cloud-bridge ocb-agent-svc agent-collection list-agents -> oci cloud-bridge ocb-agent-svc agent-collection list
ocbagentsvc_cli.ocb_agent_svc_root_group.commands.pop(ocbagentsvc_cli.agent_collection_group.name)
ocbagentsvc_cli.agent_group.add_command(ocbagentsvc_cli.list_agents)
cli_util.rename_command(ocbagentsvc_cli, ocbagentsvc_cli.agent_group, ocbagentsvc_cli.list_agents, "list")

# oci cloud-bridge ocb-agent-svc agent-dependency-collection list-agent-dependencies -> oci cloud-bridge ocb-agent-svc agent-dependency-collection list
ocbagentsvc_cli.ocb_agent_svc_root_group.commands.pop(ocbagentsvc_cli.agent_dependency_collection_group.name)
ocbagentsvc_cli.agent_dependency_group.add_command(ocbagentsvc_cli.list_agent_dependencies)
cli_util.rename_command(ocbagentsvc_cli, ocbagentsvc_cli.agent_dependency_group, ocbagentsvc_cli.list_agent_dependencies, "list")

# oci cloud-bridge ocb-agent-svc environment-collection list-environments -> oci cloud-bridge ocb-agent-svc environment list
ocbagentsvc_cli.ocb_agent_svc_root_group.commands.pop(ocbagentsvc_cli.environment_collection_group.name)
ocbagentsvc_cli.environment_group.add_command(ocbagentsvc_cli.list_environments)
cli_util.rename_command(ocbagentsvc_cli, ocbagentsvc_cli.environment_group, ocbagentsvc_cli.list_environments, "list")

cli_util.rename_command(ocbagentsvc_cli, ocbagentsvc_cli.ocb_agent_svc_root_group, ocbagentsvc_cli.appliance_image_collection_group, "appliance-image")
