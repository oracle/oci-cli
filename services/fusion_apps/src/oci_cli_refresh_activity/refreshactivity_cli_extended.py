# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.fusion_apps.src.oci_cli_refresh_activity.generated import refreshactivity_cli
from services.fusion_apps.src.oci_cli_fusion_apps.generated import fusion_apps_service_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci fusion-apps refresh-activity refresh-activity' -> 'oci fusion-apps refresh-activity'
refreshactivity_cli.refresh_activity_root_group.commands.pop(refreshactivity_cli.refresh_activity_group.name)
refreshactivity_cli.refresh_activity_root_group.add_command(refreshactivity_cli.get_refresh_activity)
refreshactivity_cli.refresh_activity_root_group.add_command(refreshactivity_cli.list_refresh_activities)

# Move commands under 'oci fusion-apps refresh-activity time-available-for-refresh -> oci fusion-apps time-available-for-refresh'
refreshactivity_cli.refresh_activity_root_group.commands.pop(refreshactivity_cli.time_available_for_refresh_group.name)
fusion_apps_service_cli.fusion_apps_service_group.add_command(refreshactivity_cli.time_available_for_refresh_group)

# Move commands under 'oci fusion-apps refresh-activity create-refresh-activity-details -> oci fusion-apps create-refresh-activity-details'
refreshactivity_cli.refresh_activity_root_group.commands.pop(refreshactivity_cli.create_refresh_activity_details_group.name)
fusion_apps_service_cli.fusion_apps_service_group.add_command(refreshactivity_cli.create_refresh_activity_details_group)
