# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.os_management_hub.src.oci_cli_lifecycle_environment.generated import lifecycleenvironment_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401
from services.os_management_hub.src.oci_cli_os_management_hub.generated import os_management_hub_service_cli


# oci os-management-hub lifecycle-environment lifecycle-stage list-lifecycle-stage-installed-packages -> oci os-management-hub lifecycle-environment lifecycle-stage list-installed-packages
cli_util.rename_command(lifecycleenvironment_cli, lifecycleenvironment_cli.lifecycle_stage_group, lifecycleenvironment_cli.list_lifecycle_stage_installed_packages, "list-installed-packages")


# oci os-management-hub lifecycle-environment lifecycle-stage attach -> oci os-management-hub lifecycle-environment lifecycle-stage attach-managed-instance
cli_util.rename_command(lifecycleenvironment_cli, lifecycleenvironment_cli.lifecycle_stage_group, lifecycleenvironment_cli.attach_managed_instances_to_lifecycle_stage, "attach-managed-instance")


# oci os-management-hub lifecycle-environment lifecycle-stage detach -> oci os-management-hub lifecycle-environment lifecycle-stage detach-managed-instance
cli_util.rename_command(lifecycleenvironment_cli, lifecycleenvironment_cli.lifecycle_stage_group, lifecycleenvironment_cli.detach_managed_instances_from_lifecycle_stage, "detach-managed-instance")


# Move commands under 'oci os-management-hub lifecycle-environment lifecycle-environment' -> 'oci os-management-hub lifecycle-environment'
lifecycleenvironment_cli.lifecycle_environment_root_group.commands.pop(lifecycleenvironment_cli.lifecycle_environment_group.name)
lifecycleenvironment_cli.lifecycle_environment_root_group.commands.pop(lifecycleenvironment_cli.lifecycle_stage_group.name)

os_management_hub_service_cli.os_management_hub_service_group.add_command(lifecycleenvironment_cli.lifecycle_stage_group)
os_management_hub_service_cli.os_management_hub_service_group.add_command(lifecycleenvironment_cli.lifecycle_environment_group)


@cli_util.copy_params_from_generated_command(lifecycleenvironment_cli.delete_lifecycle_environment, params_to_exclude=['lifecycle_environment_id'])
@lifecycleenvironment_cli.lifecycle_environment_group.command(name=lifecycleenvironment_cli.delete_lifecycle_environment.name, help=lifecycleenvironment_cli.delete_lifecycle_environment.help)
@cli_util.option('--lifecycle-env-id', required=True, help=u"""The OCID of the lifecycle environment. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_lifecycle_environment_extended(ctx, **kwargs):

    if 'lifecycle_env_id' in kwargs:
        kwargs['lifecycle_environment_id'] = kwargs['lifecycle_env_id']
        kwargs.pop('lifecycle_env_id')

    ctx.invoke(lifecycleenvironment_cli.delete_lifecycle_environment, **kwargs)


@cli_util.copy_params_from_generated_command(lifecycleenvironment_cli.get_lifecycle_environment, params_to_exclude=['lifecycle_environment_id'])
@lifecycleenvironment_cli.lifecycle_environment_group.command(name=lifecycleenvironment_cli.get_lifecycle_environment.name, help=lifecycleenvironment_cli.get_lifecycle_environment.help)
@cli_util.option('--lifecycle-env-id', required=True, help=u"""The OCID of the lifecycle environment. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management_hub', 'class': 'LifecycleEnvironment'})
@cli_util.wrap_exceptions
def get_lifecycle_environment_extended(ctx, **kwargs):

    if 'lifecycle_env_id' in kwargs:
        kwargs['lifecycle_environment_id'] = kwargs['lifecycle_env_id']
        kwargs.pop('lifecycle_env_id')

    ctx.invoke(lifecycleenvironment_cli.get_lifecycle_environment, **kwargs)


@cli_util.copy_params_from_generated_command(lifecycleenvironment_cli.list_lifecycle_environments, params_to_exclude=['lifecycle_environment_id', 'location_not_equal_to'])
@lifecycleenvironment_cli.lifecycle_environment_group.command(name=lifecycleenvironment_cli.list_lifecycle_environments.name, help=lifecycleenvironment_cli.list_lifecycle_environments.help)
@cli_util.option('--location-ne', type=custom_types.CliCaseInsensitiveChoice(["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]), multiple=True, help="""A filter to return only resources whose location does not match the given value.""")
@cli_util.option('--lifecycle-env-id', help=u"""The OCID of the lifecycle environment.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'display-name': {'module': 'os_management_hub', 'class': 'list[string]'}}, output_type={'module': 'os_management_hub', 'class': 'LifecycleEnvironmentCollection'})
@cli_util.wrap_exceptions
def list_lifecycle_environments_extended(ctx, **kwargs):

    if 'location_ne' in kwargs:
        kwargs['location_not_equal_to'] = kwargs['location_ne']
        kwargs.pop('location_ne')

    if 'lifecycle_env_id' in kwargs:
        kwargs['lifecycle_environment_id'] = kwargs['lifecycle_env_id']
        kwargs.pop('lifecycle_env_id')

    ctx.invoke(lifecycleenvironment_cli.list_lifecycle_environments, **kwargs)


@cli_util.copy_params_from_generated_command(lifecycleenvironment_cli.update_lifecycle_environment, params_to_exclude=['lifecycle_environment_id'])
@lifecycleenvironment_cli.lifecycle_environment_group.command(name=lifecycleenvironment_cli.update_lifecycle_environment.name, help=lifecycleenvironment_cli.update_lifecycle_environment.help)
@cli_util.option('--lifecycle-env-id', required=True, help=u"""The OCID of the lifecycle environment. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'stages': {'module': 'os_management_hub', 'class': 'list[UpdateLifecycleStageDetails]'}, 'freeform-tags': {'module': 'os_management_hub', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management_hub', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'os_management_hub', 'class': 'LifecycleEnvironment'})
@cli_util.wrap_exceptions
def update_lifecycle_environment_extended(ctx, **kwargs):

    if 'lifecycle_env_id' in kwargs:
        kwargs['lifecycle_environment_id'] = kwargs['lifecycle_env_id']
        kwargs.pop('lifecycle_env_id')

    ctx.invoke(lifecycleenvironment_cli.update_lifecycle_environment, **kwargs)


@cli_util.copy_params_from_generated_command(lifecycleenvironment_cli.attach_managed_instances_to_lifecycle_stage, params_to_exclude=['lifecycle_stage_id'])
@lifecycleenvironment_cli.lifecycle_stage_group.command(name=lifecycleenvironment_cli.attach_managed_instances_to_lifecycle_stage.name, help=lifecycleenvironment_cli.attach_managed_instances_to_lifecycle_stage.help)
@cli_util.option('--stage-id', required=True, help=u"""The OCID of the lifecycle stage. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'managed-instance-details': {'module': 'os_management_hub', 'class': 'ManagedInstancesDetails'}})
@cli_util.wrap_exceptions
def attach_managed_instances_to_lifecycle_stage_extended(ctx, **kwargs):

    if 'stage_id' in kwargs:
        kwargs['lifecycle_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    ctx.invoke(lifecycleenvironment_cli.attach_managed_instances_to_lifecycle_stage, **kwargs)


@cli_util.copy_params_from_generated_command(lifecycleenvironment_cli.detach_managed_instances_from_lifecycle_stage, params_to_exclude=['lifecycle_stage_id'])
@lifecycleenvironment_cli.lifecycle_stage_group.command(name=lifecycleenvironment_cli.detach_managed_instances_from_lifecycle_stage.name, help=lifecycleenvironment_cli.detach_managed_instances_from_lifecycle_stage.help)
@cli_util.option('--stage-id', required=True, help=u"""The OCID of the lifecycle stage. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'managed-instance-details': {'module': 'os_management_hub', 'class': 'ManagedInstancesDetails'}})
@cli_util.wrap_exceptions
def detach_managed_instances_from_lifecycle_stage_extended(ctx, **kwargs):

    if 'stage_id' in kwargs:
        kwargs['lifecycle_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    ctx.invoke(lifecycleenvironment_cli.detach_managed_instances_from_lifecycle_stage, **kwargs)


@cli_util.copy_params_from_generated_command(lifecycleenvironment_cli.get_lifecycle_stage, params_to_exclude=['lifecycle_stage_id'])
@lifecycleenvironment_cli.lifecycle_stage_group.command(name=lifecycleenvironment_cli.get_lifecycle_stage.name, help=lifecycleenvironment_cli.get_lifecycle_stage.help)
@cli_util.option('--stage-id', required=True, help=u"""The OCID of the lifecycle stage. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management_hub', 'class': 'LifecycleStage'})
@cli_util.wrap_exceptions
def get_lifecycle_stage_extended(ctx, **kwargs):

    if 'stage_id' in kwargs:
        kwargs['lifecycle_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    ctx.invoke(lifecycleenvironment_cli.get_lifecycle_stage, **kwargs)


@cli_util.copy_params_from_generated_command(lifecycleenvironment_cli.list_lifecycle_stages, params_to_exclude=['lifecycle_stage_id', 'location_not_equal_to'])
@lifecycleenvironment_cli.lifecycle_stage_group.command(name=lifecycleenvironment_cli.list_lifecycle_stages.name, help=lifecycleenvironment_cli.list_lifecycle_stages.help)
@cli_util.option('--location-ne', type=custom_types.CliCaseInsensitiveChoice(["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]), multiple=True, help="""A filter to return only resources whose location does not match the given value.""")
@cli_util.option('--stage-id', help=u"""The OCID of the lifecycle stage.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'display-name': {'module': 'os_management_hub', 'class': 'list[string]'}}, output_type={'module': 'os_management_hub', 'class': 'LifecycleStageCollection'})
@cli_util.wrap_exceptions
def list_lifecycle_stages_extended(ctx, **kwargs):

    if 'location_ne' in kwargs:
        kwargs['location_not_equal_to'] = kwargs['location_ne']
        kwargs.pop('location_ne')

    if 'stage_id' in kwargs:
        kwargs['lifecycle_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    ctx.invoke(lifecycleenvironment_cli.list_lifecycle_stages, **kwargs)


@cli_util.copy_params_from_generated_command(lifecycleenvironment_cli.list_lifecycle_stage_installed_packages, params_to_exclude=['lifecycle_stage_id'])
@lifecycleenvironment_cli.lifecycle_stage_group.command(name=lifecycleenvironment_cli.list_lifecycle_stage_installed_packages.name, help=lifecycleenvironment_cli.list_lifecycle_stage_installed_packages.help)
@cli_util.option('--stage-id', required=True, help=u"""The OCID of the lifecycle stage. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'display-name': {'module': 'os_management_hub', 'class': 'list[string]'}}, output_type={'module': 'os_management_hub', 'class': 'InstalledPackageCollection'})
@cli_util.wrap_exceptions
def list_lifecycle_stage_installed_packages_extended(ctx, **kwargs):

    if 'stage_id' in kwargs:
        kwargs['lifecycle_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    ctx.invoke(lifecycleenvironment_cli.list_lifecycle_stage_installed_packages, **kwargs)


@cli_util.copy_params_from_generated_command(lifecycleenvironment_cli.promote_software_source_to_lifecycle_stage, params_to_exclude=['lifecycle_stage_id'])
@lifecycleenvironment_cli.lifecycle_stage_group.command(name=lifecycleenvironment_cli.promote_software_source_to_lifecycle_stage.name, help=lifecycleenvironment_cli.promote_software_source_to_lifecycle_stage.help)
@cli_util.option('--stage-id', required=True, help=u"""The OCID of the lifecycle stage. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def promote_software_source_to_lifecycle_stage_extended(ctx, **kwargs):

    if 'stage_id' in kwargs:
        kwargs['lifecycle_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    ctx.invoke(lifecycleenvironment_cli.promote_software_source_to_lifecycle_stage, **kwargs)


@cli_util.copy_params_from_generated_command(lifecycleenvironment_cli.change_lifecycle_environment_compartment, params_to_exclude=['lifecycle_environment_id'])
@lifecycleenvironment_cli.lifecycle_environment_group.command(name=lifecycleenvironment_cli.change_lifecycle_environment_compartment.name, help=lifecycleenvironment_cli.change_lifecycle_environment_compartment.help)
@cli_util.option('--lifecycle-env-id', required=True, help=u"""The [OCID] of the lifecycle environment. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_lifecycle_environment_compartment_extended(ctx, **kwargs):

    if 'lifecycle_env_id' in kwargs:
        kwargs['lifecycle_environment_id'] = kwargs['lifecycle_env_id']
        kwargs.pop('lifecycle_env_id')

    ctx.invoke(lifecycleenvironment_cli.change_lifecycle_environment_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(lifecycleenvironment_cli.reboot_lifecycle_stage, params_to_exclude=['lifecycle_stage_id'])
@lifecycleenvironment_cli.lifecycle_stage_group.command(name=lifecycleenvironment_cli.reboot_lifecycle_stage.name, help=lifecycleenvironment_cli.reboot_lifecycle_stage.help)
@cli_util.option('--stage-id', required=True, help=u"""The [OCID] of the lifecycle stage. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def reboot_lifecycle_stage_extended(ctx, **kwargs):

    if 'stage_id' in kwargs:
        kwargs['lifecycle_stage_id'] = kwargs['stage_id']
        kwargs.pop('stage_id')

    ctx.invoke(lifecycleenvironment_cli.reboot_lifecycle_stage, **kwargs)
