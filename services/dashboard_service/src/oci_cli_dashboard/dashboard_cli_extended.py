# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.dashboard_service.src.oci_cli_dashboard.generated import dashboard_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci dashboard-service dashboard dashboard update-dashboard-update-v1-dashboard-details -> oci dashboard-service dashboard dashboard update-dashboard-v1
cli_util.rename_command(dashboard_cli, dashboard_cli.dashboard_group, dashboard_cli.update_dashboard_update_v1_dashboard_details, "update-dashboard-v1")


# oci dashboard-service dashboard dashboard create-dashboard-create-v1-dashboard-details -> oci dashboard-service dashboard dashboard create-dashboard-v1
cli_util.rename_command(dashboard_cli, dashboard_cli.dashboard_group, dashboard_cli.create_dashboard_create_v1_dashboard_details, "create-dashboard-v1")


# oci dashboard-service dashboard dashboard-collection -> oci dashboard-service dashboard dashboards
cli_util.rename_command(dashboard_cli, dashboard_cli.dashboard_root_group, dashboard_cli.dashboard_collection_group, "dashboards")


# Move commands under 'oci dashboard-service dashboard dashboard' -> 'oci dashboard-service dashboard'
dashboard_cli.dashboard_root_group.commands.pop(dashboard_cli.dashboard_group.name)
dashboard_cli.dashboard_root_group.add_command(dashboard_cli.create_dashboard)
dashboard_cli.dashboard_root_group.add_command(dashboard_cli.delete_dashboard)
dashboard_cli.dashboard_root_group.add_command(dashboard_cli.get_dashboard)
dashboard_cli.dashboard_root_group.add_command(dashboard_cli.update_dashboard)
dashboard_cli.dashboard_root_group.add_command(dashboard_cli.update_dashboard_update_v1_dashboard_details)
dashboard_cli.dashboard_root_group.add_command(dashboard_cli.create_dashboard_create_v1_dashboard_details)

# Move commands under 'oci dashboard-service dashboard dashboards' -> 'oci dashboard-service dashboard'
dashboard_cli.dashboard_root_group.commands.pop(dashboard_cli.dashboard_collection_group.name)
dashboard_cli.dashboard_root_group.add_command(dashboard_cli.list_dashboards)


# Remove create from oci dashboard-service dashboard
dashboard_cli.dashboard_root_group.commands.pop(dashboard_cli.create_dashboard.name)


# Remove update from oci dashboard-service dashboard
dashboard_cli.dashboard_root_group.commands.pop(dashboard_cli.update_dashboard.name)

# Add Change_dashboard_group command in oci dashboard-service dashboard
dashboard_cli.dashboard_root_group.add_command(dashboard_cli.change_dashboard_group)
