# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.os_management_hub.src.oci_cli_onboarding.generated import onboarding_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401
from services.os_management_hub.src.oci_cli_os_management_hub.generated import os_management_hub_service_cli

# oci os-management-hub onboarding profile create-profile-create-group-profile-details -> oci os-management-hub onboarding profile create-group-profile
cli_util.rename_command(onboarding_cli, onboarding_cli.profile_group, onboarding_cli.create_profile_create_group_profile_details, "create-group-profile")


# oci os-management-hub onboarding profile create-profile-create-lifecycle-profile-details -> oci os-management-hub onboarding profile create-lifecycle-profile
cli_util.rename_command(onboarding_cli, onboarding_cli.profile_group, onboarding_cli.create_profile_create_lifecycle_profile_details, "create-lifecycle-profile")


# oci os-management-hub onboarding profile create-profile-create-software-source-profile-details -> oci os-management-hub onboarding profile create-software-source-profile
cli_util.rename_command(onboarding_cli, onboarding_cli.profile_group, onboarding_cli.create_profile_create_software_source_profile_details, "create-software-source-profile")


# Remove create-profile-create-station-profile-details from oci os-management-hub onboarding profile
onboarding_cli.profile_group.commands.pop(onboarding_cli.create_profile_create_station_profile_details.name)


# Remove create from oci os-management-hub onboarding profile
onboarding_cli.profile_group.commands.pop(onboarding_cli.create_profile.name)


@cli_util.copy_params_from_generated_command(onboarding_cli.create_profile_create_group_profile_details, params_to_exclude=['managed_instance_group_id'])
@onboarding_cli.profile_group.command(name=onboarding_cli.create_profile_create_group_profile_details.name, help=onboarding_cli.create_profile_create_group_profile_details.help)
@cli_util.option('--group-id', required=True, help=u"""The OCID of the managed instance group from which the registration profile will inherit its software sources. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'os_management_hub', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management_hub', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'os_management_hub', 'class': 'Profile'})
@cli_util.wrap_exceptions
def create_profile_create_group_profile_details_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(onboarding_cli.create_profile_create_group_profile_details, **kwargs)


@cli_util.copy_params_from_generated_command(onboarding_cli.create_profile_create_lifecycle_profile_details, params_to_exclude=['lifecycle_stage_id'])
@onboarding_cli.profile_group.command(name=onboarding_cli.create_profile_create_lifecycle_profile_details.name, help=onboarding_cli.create_profile_create_lifecycle_profile_details.help)
@cli_util.option('--stage-id', required=True, help=u"""The OCID of the lifecycle stage from which the registration profile will inherit its software source. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'os_management_hub', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management_hub', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'os_management_hub', 'class': 'Profile'})
@cli_util.wrap_exceptions
def create_profile_create_lifecycle_profile_details_extended(ctx, **kwargs):

    if 'stage_id' in kwargs:
        kwargs['lifecycle_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    ctx.invoke(onboarding_cli.create_profile_create_lifecycle_profile_details, **kwargs)


# Remove onboarding root-group, add profile group to os-management-hub group
onboarding_cli.onboarding_root_group.commands.pop(onboarding_cli.profile_group.name)
os_management_hub_service_cli.os_management_hub_service_group.add_command(onboarding_cli.profile_group)
os_management_hub_service_cli.os_management_hub_service_group.commands.pop(onboarding_cli.onboarding_root_group.name)


# oci os-management-hub profile attach -> oci os-management-hub profile attach-software-sources
cli_util.rename_command(onboarding_cli, onboarding_cli.profile_group, onboarding_cli.attach_software_sources_to_profile, "attach-software-sources")


# oci os-management-hub profile create-profile-create-windows-stand-alone-profile-details -> oci os-management-hub profile create-windows-stand-alone-profile
cli_util.rename_command(onboarding_cli, onboarding_cli.profile_group, onboarding_cli.create_profile_create_windows_stand_alone_profile_details, "create-windows-stand-alone-profile")


# oci os-management-hub profile detach -> oci os-management-hub profile detach-software-sources
cli_util.rename_command(onboarding_cli, onboarding_cli.profile_group, onboarding_cli.detach_software_sources_from_profile, "detach-software-sources")


# oci os-management-hub profile list-profile-available-software-sources -> oci os-management-hub profile list-available-software-sources
cli_util.rename_command(onboarding_cli, onboarding_cli.profile_group, onboarding_cli.list_profile_available_software_sources, "list-available-software-sources")

# oci os-management-hub profile attach -> oci os-management-hub profile attach-lifecycle-stage
cli_util.rename_command(onboarding_cli, onboarding_cli.profile_group, onboarding_cli.attach_lifecycle_stage_to_profile, "attach-lifecycle-stage")

# oci os-management-hub profile attach -> oci os-management-hub profile attach-managed-instance-group
cli_util.rename_command(onboarding_cli, onboarding_cli.profile_group, onboarding_cli.attach_managed_instance_group_to_profile, "attach-managed-instance-group")

# oci os-management-hub profile attach -> oci os-management-hub profile attach-management-station
cli_util.rename_command(onboarding_cli, onboarding_cli.profile_group, onboarding_cli.attach_management_station_to_profile, "attach-management-station")

# oci os-management-hub profile-version get -> oci os-management-hub profile get-profile-version
cli_util.rename_command(onboarding_cli, onboarding_cli.profile_version_group, onboarding_cli.get_profile_version, "get-profile-version")
onboarding_cli.profile_version_group.commands.pop(onboarding_cli.get_profile_version.name)
onboarding_cli.profile_group.add_command(onboarding_cli.get_profile_version)


@cli_util.copy_params_from_generated_command(onboarding_cli.list_profiles, params_to_exclude=['management_station_not_equal_to'])
@onboarding_cli.profile_group.command(name=onboarding_cli.list_profiles.name, help=onboarding_cli.list_profiles.help)
@cli_util.option('--management-station-ne', multiple=True, help=u"""A filter to return resources that aren't associated with the specified management station [OCIDs].""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'display-name': {'module': 'os_management_hub', 'class': 'list[string]'}, 'management-station': {'module': 'os_management_hub', 'class': 'list[string]'}, 'management-station-not-equal-to': {'module': 'os_management_hub', 'class': 'list[string]'}}, output_type={'module': 'os_management_hub', 'class': 'ProfileCollection'})
@cli_util.wrap_exceptions
def list_profiles_extended(ctx, **kwargs):

    if 'management_station_ne' in kwargs:
        kwargs['management_station_not_equal_to'] = kwargs['management_station_ne']
        kwargs.pop('management_station_ne')

    ctx.invoke(onboarding_cli.list_profiles, **kwargs)


# Manual changes for OSMH 3.0
@cli_util.copy_params_from_generated_command(onboarding_cli.attach_managed_instance_group_to_profile, params_to_exclude=['managed_instance_group_id'])
@onboarding_cli.profile_group.command(name=onboarding_cli.attach_managed_instance_group_to_profile.name, help=onboarding_cli.attach_managed_instance_group_to_profile.help)
@cli_util.option('--group-id', required=True, help=u"""The [OCID] of the managed instance group that the profile will be associated with.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def attach_managed_instance_group_to_profile_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(onboarding_cli.attach_managed_instance_group_to_profile, **kwargs)


@cli_util.copy_params_from_generated_command(onboarding_cli.attach_lifecycle_stage_to_profile, params_to_exclude=['lifecycle_stage_id'])
@onboarding_cli.profile_group.command(name=onboarding_cli.attach_lifecycle_stage_to_profile.name, help=onboarding_cli.attach_lifecycle_stage_to_profile.help)
@cli_util.option('--stage-id', required=True, help=u"""The OCID of the lifecycle stage that the profile will be associated with. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def attach_lifecycle_stage_to_profile(ctx, **kwargs):

    if 'stage_id' in kwargs:
        kwargs['lifecycle_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    ctx.invoke(onboarding_cli.attach_lifecycle_stage_to_profile, **kwargs)
