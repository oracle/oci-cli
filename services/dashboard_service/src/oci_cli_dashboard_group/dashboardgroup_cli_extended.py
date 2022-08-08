# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.dashboard_service.src.oci_cli_dashboard_group.generated import dashboardgroup_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci dashboard-service dashboard-group dashboard-group-collection -> oci dashboard-service dashboard-group dashboard-groups
cli_util.rename_command(dashboardgroup_cli, dashboardgroup_cli.dashboard_group_root_group, dashboardgroup_cli.dashboard_group_collection_group, "dashboard-groups")


# Move commands under 'oci dashboard-service dashboard-group dashboard-group' -> 'oci dashboard-service dashboard-group'
dashboardgroup_cli.dashboard_group_root_group.commands.pop(dashboardgroup_cli.dashboard_group_group.name)
dashboardgroup_cli.dashboard_group_root_group.add_command(dashboardgroup_cli.create_dashboard_group)
dashboardgroup_cli.dashboard_group_root_group.add_command(dashboardgroup_cli.delete_dashboard_group)
dashboardgroup_cli.dashboard_group_root_group.add_command(dashboardgroup_cli.get_dashboard_group)
dashboardgroup_cli.dashboard_group_root_group.add_command(dashboardgroup_cli.update_dashboard_group)


# Move commands under 'oci dashboard-service dashboard-group dashboard-groups' -> 'oci dashboard-service dashboard-group'
dashboardgroup_cli.dashboard_group_root_group.commands.pop(dashboardgroup_cli.dashboard_group_collection_group.name)
dashboardgroup_cli.dashboard_group_root_group.add_command(dashboardgroup_cli.list_dashboard_groups)

# Add Change_dashboard_group command in oci dashboard-service dashboard
dashboardgroup_cli.dashboard_group_root_group.add_command(dashboardgroup_cli.change_dashboard_group_compartment)
