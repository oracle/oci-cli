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
