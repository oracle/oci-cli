# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click

from services.core.src.oci_cli_compute.generated import compute_cli

from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli.aliasing import CommandGroupWithAlias


# We want to replace the following:
#   oci compute app-catalog-listing get
#   oci compute app-catalog-listing list
#   oci compute app-catalog-listing-resource-version get
#   oci compute app-catalog-listing-resource-version list
#   oci compute app-catalog-listing-resource-version-agreements get-app-catalog-listing-agreements
#   oci compute app-catalog-subscription create --oracle-terms-of-use-link
#   oci compute app-catalog-subscription delete
#   oci compute app-catalog-subscription list
#
# With these:
#   oci compute pic listing get
#   oci compute pic listing list
#   oci compute pic version get
#   oci compute pic version list
#   oci compute pic agreements get
#   oci compute pic subscription create --oracle-tou-link
#   oci compute pic subscription delete
#   oci compute pic subscription list

# Disabling app_catalog commands
compute_cli.compute_root_group.commands.pop(compute_cli.app_catalog_listing_group.name)
compute_cli.compute_root_group.commands.pop(compute_cli.app_catalog_listing_resource_version_agreements_group.name)
compute_cli.compute_root_group.commands.pop(compute_cli.app_catalog_listing_resource_version_group.name)
compute_cli.compute_root_group.commands.pop(compute_cli.app_catalog_subscription_group.name)


@click.command('pic', cls=CommandGroupWithAlias, help="""Partner image catalog (PIC).""")
@cli_util.help_option_group
def pic_group():
    pass


@click.command('listing', cls=CommandGroupWithAlias, help="""A PIC listing.""")
@cli_util.help_option_group
def pic_listing_group():
    pass


@click.command('version', cls=CommandGroupWithAlias, help="""A PIC listing resource version.""")
@cli_util.help_option_group
def pic_version_group():
    pass


@click.command('agreements', cls=CommandGroupWithAlias, help="""PIC listing resource version agreements.""")
@cli_util.help_option_group
def pic_agreements_group():
    pass


@click.command('subscription', cls=CommandGroupWithAlias, help="""A PIC subscription.""")
@cli_util.help_option_group
def pic_subscription_group():
    pass


compute_cli.compute_root_group.add_command(pic_group)
pic_group.add_command(pic_listing_group)
pic_group.add_command(pic_version_group)
pic_group.add_command(pic_agreements_group)
pic_group.add_command(pic_subscription_group)

pic_listing_group.add_command(compute_cli.list_app_catalog_listings)
pic_listing_group.add_command(compute_cli.get_app_catalog_listing)
pic_version_group.add_command(compute_cli.list_app_catalog_listing_resource_versions)
pic_version_group.add_command(compute_cli.get_app_catalog_listing_resource_version)
pic_subscription_group.add_command(compute_cli.list_app_catalog_subscriptions)
pic_subscription_group.add_command(compute_cli.delete_app_catalog_subscription)


@cli_util.copy_params_from_generated_command(compute_cli.get_app_catalog_listing_agreements, params_to_exclude=[])
@pic_agreements_group.command(name='get', help=compute_cli.get_app_catalog_listing_agreements.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def get_app_catalog_listing_agreements(ctx, **kwargs):
    ctx.invoke(compute_cli.get_app_catalog_listing_agreements, **kwargs)


@cli_util.copy_params_from_generated_command(compute_cli.create_app_catalog_subscription, params_to_exclude=['oracle_terms_of_use_link', 'listing_resource_version'])
@pic_subscription_group.command(name='create', help=compute_cli.create_app_catalog_subscription.help)
@cli_util.option('--resource-version', help="""Listing Resource Version.""")
@cli_util.option('--oracle-tou-link', help='''Oracle Terms of Use link''')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def create_app_catalog_subscription(ctx, **kwargs):
    if 'oracle_tou_link' in kwargs:
        kwargs['oracle_terms_of_use_link'] = kwargs['oracle_tou_link']
        kwargs.pop('oracle_tou_link')
    if 'resource_version' in kwargs:
        kwargs['listing_resource_version'] = kwargs['resource_version']
        kwargs.pop('resource_version')
    ctx.invoke(compute_cli.create_app_catalog_subscription, **kwargs)


# Remove launch-instance-amd-rome-bm-launch-instance-platform-config from oci compute instance
compute_cli.instance_group.commands.pop(compute_cli.launch_instance_amd_rome_bm_launch_instance_platform_config.name)


# Remove launch-instance-amd-vm-launch-instance-platform-config from oci compute instance
compute_cli.instance_group.commands.pop(compute_cli.launch_instance_amd_vm_launch_instance_platform_config.name)


# Remove launch-instance-intel-skylake-bm-launch-instance-platform-config from oci compute instance
compute_cli.instance_group.commands.pop(compute_cli.launch_instance_intel_skylake_bm_launch_instance_platform_config.name)


# Remove launch-instance-intel-vm-launch-instance-platform-config from oci compute instance
compute_cli.instance_group.commands.pop(compute_cli.launch_instance_intel_vm_launch_instance_platform_config.name)


# Remove launch-instance-amd-rome-bm-gpu-launch-instance-platform-config from oci compute instance
compute_cli.instance_group.commands.pop(compute_cli.launch_instance_amd_rome_bm_gpu_launch_instance_platform_config.name)


# Remove launch-instance-intel-icelake-bm-launch-instance-platform-config from oci compute instance
compute_cli.instance_group.commands.pop(compute_cli.launch_instance_intel_icelake_bm_launch_instance_platform_config.name)

# Remove instance-action-reset-action-details from oci compute instance
compute_cli.instance_group.commands.pop(compute_cli.instance_action_reset_action_details.name)


# Remove instance-action-soft-reset-action-details from oci compute instance
compute_cli.instance_group.commands.pop(compute_cli.instance_action_soft_reset_action_details.name)

# Remove instance-action-reboot-migrate-action-details from oci compute instance
compute_cli.instance_group.commands.pop(compute_cli.instance_action_reboot_migrate_action_details.name)

# Remove launch-instance-amd-milan-bm-gpu-launch-instance-platform-config from oci compute instance
compute_cli.instance_group.commands.pop(compute_cli.launch_instance_amd_milan_bm_gpu_launch_instance_platform_config.name)


# Remove launch-instance-generic-bm-launch-instance-platform-config from oci compute instance
compute_cli.instance_group.commands.pop(compute_cli.launch_instance_generic_bm_launch_instance_platform_config.name)
