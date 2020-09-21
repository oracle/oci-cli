# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
from services.announcements_service.src.oci_cli_announcement.generated import announcement_cli
from oci_cli import cli_util
import click
from oci_cli.aliasing import CommandGroupWithAlias


'''
From:
oci announcements-service announcement get
oci announcements-service announcements-collection list-announcements
oci announcements-service announcement-user-status update
oci announcements-service announcement-user-status-details get-announcement-user-status

To:
oci announce announcements get
oci announce announcements list
oci announce user-status update
oci announce user-status get
'''
announcement_cli.announce_root_group.commands.pop(announcement_cli.announcement_group.name)
announcement_cli.announce_root_group.commands.pop(announcement_cli.announcement_user_status_group.name)
announcement_cli.announce_root_group.commands.pop(announcement_cli.announcement_user_status_details_group.name)
announcement_cli.announce_root_group.commands.pop(announcement_cli.announcements_collection_group.name)


@click.command('announcements', cls=CommandGroupWithAlias, help="""An announcement represents a message targetted to a specific tenant.""")
@cli_util.help_option_group
def announcements_group():
    pass


@click.command('user-status', cls=CommandGroupWithAlias, help="""User specific status of the announcements.""")
@cli_util.help_option_group
def user_status_group():
    pass


announcement_cli.announce_root_group.add_command(announcements_group)
announcement_cli.announce_root_group.add_command(user_status_group)
announcements_group.add_command(announcement_cli.get_announcement)
user_status_group.add_command(announcement_cli.update_announcement_user_status)
cli_util.rename_command(announcement_cli, user_status_group, announcement_cli.get_announcement_user_status, "get")


announcements_group.add_command(announcement_cli.list_announcements)
cli_util.rename_command(announcement_cli, announcements_group, announcement_cli.list_announcements, "list")
announcement_cli.list_announcements.help = "Gets a list of `Announcement` objects for the current tenancy"
