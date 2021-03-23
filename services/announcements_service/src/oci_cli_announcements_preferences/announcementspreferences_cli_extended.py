# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.announcements_service.src.oci_cli_announcements_preferences.generated import announcementspreferences_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci announce announcements-preferences announcements-preferences' -> 'oci announce announcements-preferences'
announcementspreferences_cli.announcements_preferences_root_group.commands.pop(announcementspreferences_cli.announcements_preferences_group.name)
announcementspreferences_cli.announcements_preferences_root_group.add_command(announcementspreferences_cli.create_announcements_preference)
announcementspreferences_cli.announcements_preferences_root_group.add_command(announcementspreferences_cli.get_announcements_preference)
announcementspreferences_cli.announcements_preferences_root_group.add_command(announcementspreferences_cli.list_announcements_preferences)
announcementspreferences_cli.announcements_preferences_root_group.add_command(announcementspreferences_cli.update_announcements_preference)
