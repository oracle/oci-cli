# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.fusion_apps.src.oci_cli_scheduled_activity.generated import scheduledactivity_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci fusion-apps scheduled-activity scheduled-activity' -> 'oci fusion-apps scheduled-activity'
scheduledactivity_cli.scheduled_activity_root_group.commands.pop(scheduledactivity_cli.scheduled_activity_group.name)
scheduledactivity_cli.scheduled_activity_root_group.add_command(scheduledactivity_cli.get_scheduled_activity)
scheduledactivity_cli.scheduled_activity_root_group.add_command(scheduledactivity_cli.list_scheduled_activities)