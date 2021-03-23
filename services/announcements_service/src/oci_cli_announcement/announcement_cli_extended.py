# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
from services.announcements_service.src.oci_cli_announcement.generated import announcement_cli
from services.announcements_service.src.oci_cli_announcements_service.generated import announce_service_cli
from oci_cli import cli_util
import click
from oci_cli.aliasing import CommandGroupWithAlias


@click.command('announcements', cls=CommandGroupWithAlias, help="""An announcement represents a message targetted to a specific tenant.""")
@cli_util.help_option_group
def announcements_group():
    pass


announce_service_cli.announce_service_group.add_command(announcements_group)


# oci announce announcement announcement-user-status-details -> oci announce announcement user-status
cli_util.rename_command(announcement_cli, announcement_cli.announcement_root_group, announcement_cli.announcement_user_status_details_group, "user-status")


# oci announce announcement announcement-user-status-details get-announcement-user-status -> oci announce announcement announcement-user-status-details get
cli_util.rename_command(announcement_cli, announcement_cli.announcement_user_status_details_group, announcement_cli.get_announcement_user_status, "get")


# oci announce announcement announcement-user-status-details update-announcement-user-status -> oci announce announcement announcement-user-status-details update
cli_util.rename_command(announcement_cli, announcement_cli.announcement_user_status_details_group, announcement_cli.update_announcement_user_status, "update")


# oci announce announcement user-status -> oci announce user-status
announce_service_cli.announce_service_group.commands.pop(announcement_cli.announcement_root_group.name)
announce_service_cli.announce_service_group.add_command(announcement_cli.announcement_user_status_details_group)


# oci announce announcement announcements-collection list-announcements -> oci announce announcement announcements-collection list
cli_util.rename_command(announcement_cli, announcement_cli.announcements_collection_group, announcement_cli.list_announcements, "list")
announcements_group.add_command(announcement_cli.list_announcements)
announcement_cli.announcements_collection_group.commands.pop(announcement_cli.list_announcements.name)


# oci announce announcement announcement get -> oci announce announcements get
announcements_group.add_command(announcement_cli.get_announcement)
announcement_cli.announcement_group.commands.pop(announcement_cli.get_announcement.name)
