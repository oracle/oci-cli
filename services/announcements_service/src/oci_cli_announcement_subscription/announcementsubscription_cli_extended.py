# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.announcements_service.src.oci_cli_announcement_subscription.generated import announcementsubscription_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci announce announcement-subscription announcement-subscription-collection list-announcement-subscriptions -> oci announce announcement-subscription announcement-subscription-collection list
cli_util.rename_command(announcementsubscription_cli, announcementsubscription_cli.announcement_subscription_collection_group, announcementsubscription_cli.list_announcement_subscriptions, "list")


# Move commands under 'oci announce announcement-subscription announcement-subscription' -> 'oci announce announcement-subscription'
announcementsubscription_cli.announcement_subscription_root_group.commands.pop(announcementsubscription_cli.announcement_subscription_group.name)
announcementsubscription_cli.announcement_subscription_root_group.add_command(announcementsubscription_cli.change_announcement_subscription_compartment)
announcementsubscription_cli.announcement_subscription_root_group.add_command(announcementsubscription_cli.create_announcement_subscription)
announcementsubscription_cli.announcement_subscription_root_group.add_command(announcementsubscription_cli.create_filter_group)
announcementsubscription_cli.announcement_subscription_root_group.add_command(announcementsubscription_cli.delete_announcement_subscription)
announcementsubscription_cli.announcement_subscription_root_group.add_command(announcementsubscription_cli.delete_filter_group)
announcementsubscription_cli.announcement_subscription_root_group.add_command(announcementsubscription_cli.get_announcement_subscription)
announcementsubscription_cli.announcement_subscription_root_group.add_command(announcementsubscription_cli.update_announcement_subscription)
announcementsubscription_cli.announcement_subscription_root_group.add_command(announcementsubscription_cli.update_filter_group)


# Move commands under 'oci announce announcement-subscription announcement-subscription-collection' -> 'oci announce announcement-subscription'
announcementsubscription_cli.announcement_subscription_root_group.commands.pop(announcementsubscription_cli.announcement_subscription_collection_group.name)
announcementsubscription_cli.announcement_subscription_root_group.add_command(announcementsubscription_cli.list_announcement_subscriptions)


@cli_util.copy_params_from_generated_command(announcementsubscription_cli.change_announcement_subscription_compartment, params_to_exclude=['announcement_subscription_id'])
@announcementsubscription_cli.announcement_subscription_group.command(name=announcementsubscription_cli.change_announcement_subscription_compartment.name, help=announcementsubscription_cli.change_announcement_subscription_compartment.help)
@cli_util.option('--subscription-id', required=True, help=u"""The OCID of the announcement subscription. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_announcement_subscription_compartment_extended(ctx, **kwargs):
    if 'subscription_id' in kwargs:
        kwargs['announcement_subscription_id'] = kwargs['subscription_id']
        kwargs.pop('subscription_id')

    ctx.invoke(announcementsubscription_cli.change_announcement_subscription_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(announcementsubscription_cli.create_filter_group, params_to_exclude=['announcement_subscription_id'])
@announcementsubscription_cli.announcement_subscription_group.command(name=announcementsubscription_cli.create_filter_group.name, help=announcementsubscription_cli.create_filter_group.help)
@cli_util.option('--subscription-id', required=True, help=u"""The OCID of the announcement subscription. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'filters': {'module': 'announcements_service', 'class': 'list[Filter]'}}, output_type={'module': 'announcements_service', 'class': 'FilterGroup'})
@cli_util.wrap_exceptions
def create_filter_group_extended(ctx, **kwargs):
    if 'subscription_id' in kwargs:
        kwargs['announcement_subscription_id'] = kwargs['subscription_id']
        kwargs.pop('subscription_id')

    ctx.invoke(announcementsubscription_cli.create_filter_group, **kwargs)


@cli_util.copy_params_from_generated_command(announcementsubscription_cli.delete_announcement_subscription, params_to_exclude=['announcement_subscription_id'])
@announcementsubscription_cli.announcement_subscription_group.command(name=announcementsubscription_cli.delete_announcement_subscription.name, help=announcementsubscription_cli.delete_announcement_subscription.help)
@cli_util.option('--subscription-id', required=True, help=u"""The OCID of the announcement subscription. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_announcement_subscription_extended(ctx, **kwargs):
    if 'subscription_id' in kwargs:
        kwargs['announcement_subscription_id'] = kwargs['subscription_id']
        kwargs.pop('subscription_id')

    ctx.invoke(announcementsubscription_cli.delete_announcement_subscription, **kwargs)


@cli_util.copy_params_from_generated_command(announcementsubscription_cli.delete_filter_group, params_to_exclude=['announcement_subscription_id'])
@announcementsubscription_cli.announcement_subscription_group.command(name=announcementsubscription_cli.delete_filter_group.name, help=announcementsubscription_cli.delete_filter_group.help)
@cli_util.option('--subscription-id', required=True, help=u"""The OCID of the announcement subscription. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_filter_group_extended(ctx, **kwargs):
    if 'subscription_id' in kwargs:
        kwargs['announcement_subscription_id'] = kwargs['subscription_id']
        kwargs.pop('subscription_id')

    ctx.invoke(announcementsubscription_cli.delete_filter_group, **kwargs)


@cli_util.copy_params_from_generated_command(announcementsubscription_cli.get_announcement_subscription, params_to_exclude=['announcement_subscription_id'])
@announcementsubscription_cli.announcement_subscription_group.command(name=announcementsubscription_cli.get_announcement_subscription.name, help=announcementsubscription_cli.get_announcement_subscription.help)
@cli_util.option('--subscription-id', required=True, help=u"""The OCID of the announcement subscription. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'announcements_service', 'class': 'AnnouncementSubscription'})
@cli_util.wrap_exceptions
def get_announcement_subscription_extended(ctx, **kwargs):
    if 'subscription_id' in kwargs:
        kwargs['announcement_subscription_id'] = kwargs['subscription_id']
        kwargs.pop('subscription_id')

    ctx.invoke(announcementsubscription_cli.get_announcement_subscription, **kwargs)


@cli_util.copy_params_from_generated_command(announcementsubscription_cli.update_announcement_subscription, params_to_exclude=['announcement_subscription_id'])
@announcementsubscription_cli.announcement_subscription_group.command(name=announcementsubscription_cli.update_announcement_subscription.name, help=announcementsubscription_cli.update_announcement_subscription.help)
@cli_util.option('--subscription-id', required=True, help=u"""The OCID of the announcement subscription. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'announcements_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'announcements_service', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'announcements_service', 'class': 'AnnouncementSubscription'})
@cli_util.wrap_exceptions
def update_announcement_subscription_extended(ctx, **kwargs):
    if 'subscription_id' in kwargs:
        kwargs['announcement_subscription_id'] = kwargs['subscription_id']
        kwargs.pop('subscription_id')

    ctx.invoke(announcementsubscription_cli.update_announcement_subscription, **kwargs)


@cli_util.copy_params_from_generated_command(announcementsubscription_cli.update_filter_group, params_to_exclude=['announcement_subscription_id'])
@announcementsubscription_cli.announcement_subscription_group.command(name=announcementsubscription_cli.update_filter_group.name, help=announcementsubscription_cli.update_filter_group.help)
@cli_util.option('--subscription-id', required=True, help=u"""The OCID of the announcement subscription. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'filters': {'module': 'announcements_service', 'class': 'list[Filter]'}}, output_type={'module': 'announcements_service', 'class': 'FilterGroup'})
@cli_util.wrap_exceptions
def update_filter_group_extended(ctx, **kwargs):
    if 'subscription_id' in kwargs:
        kwargs['announcement_subscription_id'] = kwargs['subscription_id']
        kwargs.pop('subscription_id')

    ctx.invoke(announcementsubscription_cli.update_filter_group, **kwargs)
