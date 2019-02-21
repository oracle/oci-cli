# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
from oci_cli_announcement.generated import announcement_cli
from oci_cli import cli_util
import click
from oci_cli.aliasing import CommandGroupWithAlias
from oci_cli import json_skeleton_utils


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
cli_util.rename_command(user_status_group, announcement_cli.get_announcement_user_status, "get")


@cli_util.copy_params_from_generated_command(announcement_cli.list_announcements, params_to_exclude=['all_pages', 'limit', 'page_size'])
@announcements_group.command(name='list', help="""Gets a list of `Announcement` objects for the current tenancy""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'announcements_service', 'class': 'AnnouncementsCollection'})
@cli_util.wrap_exceptions
def list_announcements_extended(ctx, **kwargs):
    if kwargs.get('all_pages'):
        kwargs.pop('all_pages')
    if kwargs.get('limit'):
        kwargs.pop('limit')
    if kwargs.get('page_size'):
        kwargs.pop('page_size')
    ctx.invoke(announcement_cli.list_announcements, **kwargs)
