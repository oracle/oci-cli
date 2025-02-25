# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.os_management_hub.src.oci_cli_managed_instance_group.generated import managedinstancegroup_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401
from services.os_management_hub.src.oci_cli_os_management_hub.generated import os_management_hub_service_cli

# oci os-management-hub managed-instance-group managed-instance-group install-module-stream-profile -> oci os-management-hub managed-instance-group managed-instance-group install-module-profile
cli_util.rename_command(managedinstancegroup_cli, managedinstancegroup_cli.managed_instance_group_group, managedinstancegroup_cli.install_module_stream_profile_on_managed_instance_group, "install-module-profile")


# oci os-management-hub managed-instance-group managed-instance-group list-managed-instance-group-available-modules -> oci os-management-hub managed-instance-group managed-instance-group list-available-modules
cli_util.rename_command(managedinstancegroup_cli, managedinstancegroup_cli.managed_instance_group_group, managedinstancegroup_cli.list_managed_instance_group_available_modules, "list-available-modules")


# oci os-management-hub managed-instance-group managed-instance-group list-managed-instance-group-available-packages -> oci os-management-hub managed-instance-group managed-instance-group list-available-packages
cli_util.rename_command(managedinstancegroup_cli, managedinstancegroup_cli.managed_instance_group_group, managedinstancegroup_cli.list_managed_instance_group_available_packages, "list-available-packages")


# oci os-management-hub managed-instance-group managed-instance-group list-managed-instance-group-available-software-sources -> oci os-management-hub managed-instance-group managed-instance-group list-available-software-sources
cli_util.rename_command(managedinstancegroup_cli, managedinstancegroup_cli.managed_instance_group_group, managedinstancegroup_cli.list_managed_instance_group_available_software_sources, "list-available-software-sources")


# oci os-management-hub managed-instance-group managed-instance-group list-managed-instance-group-installed-packages -> oci os-management-hub managed-instance-group managed-instance-group list-installed-packages
cli_util.rename_command(managedinstancegroup_cli, managedinstancegroup_cli.managed_instance_group_group, managedinstancegroup_cli.list_managed_instance_group_installed_packages, "list-installed-packages")


# oci os-management-hub managed-instance-group managed-instance-group list-managed-instance-group-modules -> oci os-management-hub managed-instance-group managed-instance-group list-modules
cli_util.rename_command(managedinstancegroup_cli, managedinstancegroup_cli.managed_instance_group_group, managedinstancegroup_cli.list_managed_instance_group_modules, "list-modules")


# oci os-management-hub managed-instance-group managed-instance-group attach -> oci os-management-hub managed-instance-group managed-instance-group attach-software-sources
cli_util.rename_command(managedinstancegroup_cli, managedinstancegroup_cli.managed_instance_group_group, managedinstancegroup_cli.attach_software_sources_to_managed_instance_group, "attach-software-sources")


# oci os-management-hub managed-instance-group managed-instance-group detach -> oci os-management-hub managed-instance-group managed-instance-group detach-software-sources
cli_util.rename_command(managedinstancegroup_cli, managedinstancegroup_cli.managed_instance_group_group, managedinstancegroup_cli.detach_software_sources_from_managed_instance_group, "detach-software-sources")


# oci os-management-hub managed-instance-group managed-instance-group remove -> oci os-management-hub managed-instance-group managed-instance-group remove-packages
cli_util.rename_command(managedinstancegroup_cli, managedinstancegroup_cli.managed_instance_group_group, managedinstancegroup_cli.remove_packages_from_managed_instance_group, "remove-packages")

# Rename remove to remove-module-profile
cli_util.rename_command(managedinstancegroup_cli, managedinstancegroup_cli.managed_instance_group_group, managedinstancegroup_cli.remove_module_stream_profile_from_managed_instance_group, "remove-module-profile")

# Rename oci os-management-hub managed-instance-group managed-instance-group attach -> oci os-management-hub managed-instance-group managed-instance-group attach-managed-instances
cli_util.rename_command(managedinstancegroup_cli, managedinstancegroup_cli.managed_instance_group_group, managedinstancegroup_cli.attach_managed_instances_to_managed_instance_group, "attach-managed-instances")

# Rename oci os-management-hub managed-instance-group managed-instance-group detach -> oci os-management-hub managed-instance-group managed-instance-group detach-managed-instances
cli_util.rename_command(managedinstancegroup_cli, managedinstancegroup_cli.managed_instance_group_group, managedinstancegroup_cli.detach_managed_instances_from_managed_instance_group, "detach-managed-instances")


# Remove manage-module-streams from oci os-management-hub managed-instance-group managed-instance-group
managedinstancegroup_cli.managed_instance_group_group.commands.pop(managedinstancegroup_cli.manage_module_streams_on_managed_instance_group.name)


# Move commands under 'oci os-management-hub managed-instance-group managed-instance-group' -> 'oci os-management-hub managed-instance-group'
managedinstancegroup_cli.managed_instance_group_root_group.commands.pop(managedinstancegroup_cli.managed_instance_group_group.name)

os_management_hub_service_cli.os_management_hub_service_group.commands.pop(managedinstancegroup_cli.managed_instance_group_root_group.name)
os_management_hub_service_cli.os_management_hub_service_group.add_command(managedinstancegroup_cli.managed_instance_group_group)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.attach_software_sources_to_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.attach_software_sources_to_managed_instance_group.name, help=managedinstancegroup_cli.attach_software_sources_to_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'software-sources': {'module': 'os_management_hub', 'class': 'list[string]'}, 'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def attach_software_sources_to_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.attach_software_sources_to_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.attach_managed_instances_to_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.attach_managed_instances_to_managed_instance_group.name, help=managedinstancegroup_cli.attach_managed_instances_to_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'managed-instances': {'module': 'os_management_hub', 'class': 'list[string]'}, 'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def attach_managed_instances_to_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.attach_managed_instances_to_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.detach_managed_instances_from_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.detach_managed_instances_from_managed_instance_group.name, help=managedinstancegroup_cli.detach_managed_instances_from_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'managed-instances': {'module': 'os_management_hub', 'class': 'list[string]'}, 'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def detach_managed_instances_from_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.detach_managed_instances_from_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.remove_module_stream_profile_from_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.remove_module_stream_profile_from_managed_instance_group.name, help=managedinstancegroup_cli.remove_module_stream_profile_from_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def remove_module_stream_profile_from_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.remove_module_stream_profile_from_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.delete_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.delete_managed_instance_group.name, help=managedinstancegroup_cli.delete_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.delete_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.detach_software_sources_from_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.detach_software_sources_from_managed_instance_group.name, help=managedinstancegroup_cli.detach_software_sources_from_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'software-sources': {'module': 'os_management_hub', 'class': 'list[string]'}, 'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def detach_software_sources_from_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.detach_software_sources_from_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.disable_module_stream_on_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.disable_module_stream_on_managed_instance_group.name, help=managedinstancegroup_cli.disable_module_stream_on_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def disable_module_stream_on_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.disable_module_stream_on_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.enable_module_stream_on_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.enable_module_stream_on_managed_instance_group.name, help=managedinstancegroup_cli.enable_module_stream_on_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def enable_module_stream_on_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.enable_module_stream_on_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.get_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.get_managed_instance_group.name, help=managedinstancegroup_cli.get_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management_hub', 'class': 'ManagedInstanceGroup'})
@cli_util.wrap_exceptions
def get_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.get_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.install_module_stream_profile_on_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.install_module_stream_profile_on_managed_instance_group.name, help=managedinstancegroup_cli.install_module_stream_profile_on_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def install_module_stream_profile_on_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.install_module_stream_profile_on_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.install_packages_on_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.install_packages_on_managed_instance_group.name, help=managedinstancegroup_cli.install_packages_on_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'package-names': {'module': 'os_management_hub', 'class': 'list[string]'}, 'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def install_packages_on_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.install_packages_on_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.list_managed_instance_groups, params_to_exclude=['managed_instance_group_id', 'location_not_equal_to', 'is_managed_by_autonomous_linux'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.list_managed_instance_groups.name, help=managedinstancegroup_cli.list_managed_instance_groups.help)
@cli_util.option('--location-ne', type=custom_types.CliCaseInsensitiveChoice(["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]), multiple=True, help="""A filter to return only resources whose location does not match the given value.""")
@cli_util.option('--is-managed-by-alx', type=click.BOOL, help="""Indicates whether to list only resources managed by the Autonomous Linux service.""")
@cli_util.option('--group-id', help=u"""The OCID of the managed instance group for which to list resources.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'display-name': {'module': 'os_management_hub', 'class': 'list[string]'}}, output_type={'module': 'os_management_hub', 'class': 'ManagedInstanceGroupCollection'})
@cli_util.wrap_exceptions
def list_managed_instance_groups_extended(ctx, **kwargs):

    if 'location_ne' in kwargs:
        kwargs['location_not_equal_to'] = kwargs['location_ne']
        kwargs.pop('location_ne')
    if 'is_managed_by_alx' in kwargs:
        kwargs['is_managed_by_autonomous_linux'] = kwargs['is_managed_by_alx']
        kwargs.pop('is_managed_by_alx')

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.list_managed_instance_groups, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.list_managed_instance_group_available_modules, params_to_exclude=['managed_instance_group_id', 'name', 'name_contains'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.list_managed_instance_group_available_modules.name, help=managedinstancegroup_cli.list_managed_instance_group_available_modules.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@cli_util.option('--module-name', help=u"""The resource name.""")
@cli_util.option('--module-name-contains', help=u"""A filter to return resources that may partially match the name given.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management_hub', 'class': 'ManagedInstanceGroupAvailableModuleCollection'})
@cli_util.wrap_exceptions
def list_managed_instance_group_available_modules_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    if 'module_name' in kwargs:
        kwargs['name'] = kwargs['module_name']
        kwargs.pop('module_name')

    if 'module_name_contains' in kwargs:
        kwargs['name_contains'] = kwargs['module_name_contains']
        kwargs.pop('module_name_contains')

    ctx.invoke(managedinstancegroup_cli.list_managed_instance_group_available_modules, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.list_managed_instance_group_available_packages, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.list_managed_instance_group_available_packages.name, help=managedinstancegroup_cli.list_managed_instance_group_available_packages.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'display-name': {'module': 'os_management_hub', 'class': 'list[string]'}}, output_type={'module': 'os_management_hub', 'class': 'ManagedInstanceGroupAvailablePackageCollection'})
@cli_util.wrap_exceptions
def list_managed_instance_group_available_packages_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.list_managed_instance_group_available_packages, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.list_managed_instance_group_available_software_sources, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.list_managed_instance_group_available_software_sources.name, help=managedinstancegroup_cli.list_managed_instance_group_available_software_sources.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'display-name': {'module': 'os_management_hub', 'class': 'list[string]'}}, output_type={'module': 'os_management_hub', 'class': 'AvailableSoftwareSourceCollection'})
@cli_util.wrap_exceptions
def list_managed_instance_group_available_software_sources_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.list_managed_instance_group_available_software_sources, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.list_managed_instance_group_installed_packages, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.list_managed_instance_group_installed_packages.name, help=managedinstancegroup_cli.list_managed_instance_group_installed_packages.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'display-name': {'module': 'os_management_hub', 'class': 'list[string]'}}, output_type={'module': 'os_management_hub', 'class': 'ManagedInstanceGroupInstalledPackageCollection'})
@cli_util.wrap_exceptions
def list_managed_instance_group_installed_packages_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.list_managed_instance_group_installed_packages, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.list_managed_instance_group_modules, params_to_exclude=['managed_instance_group_id', 'name', 'name_contains'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.list_managed_instance_group_modules.name, help=managedinstancegroup_cli.list_managed_instance_group_modules.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@cli_util.option('--module-name', help=u"""The resource name.""")
@cli_util.option('--module-name-contains', help=u"""A filter to return resources that may partially match the name given.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management_hub', 'class': 'ManagedInstanceGroupModuleCollection'})
@cli_util.wrap_exceptions
def list_managed_instance_group_modules_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    if 'module_name' in kwargs:
        kwargs['name'] = kwargs['module_name']
        kwargs.pop('module_name')

    if 'module_name_contains' in kwargs:
        kwargs['name_contains'] = kwargs['module_name_contains']
        kwargs.pop('module_name_contains')

    ctx.invoke(managedinstancegroup_cli.list_managed_instance_group_modules, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.remove_packages_from_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.remove_packages_from_managed_instance_group.name, help=managedinstancegroup_cli.remove_packages_from_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'package-names': {'module': 'os_management_hub', 'class': 'list[string]'}, 'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def remove_packages_from_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.remove_packages_from_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.update_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.update_managed_instance_group.name, help=managedinstancegroup_cli.update_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'os_management_hub', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management_hub', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'os_management_hub', 'class': 'ManagedInstanceGroup'})
@cli_util.wrap_exceptions
def update_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.update_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.update_all_packages_on_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.update_all_packages_on_managed_instance_group.name, help=managedinstancegroup_cli.update_all_packages_on_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The managed instance group OCID. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def update_all_packages_on_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.update_all_packages_on_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.change_managed_instance_group_compartment, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.change_managed_instance_group_compartment.name, help=managedinstancegroup_cli.change_managed_instance_group_compartment.help)
@cli_util.option('--group-id', required=True, help=u"""The [OCID] of the managed instance group. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_managed_instance_group_compartment_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.change_managed_instance_group_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.install_windows_updates_on_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.install_windows_updates_on_managed_instance_group.name, help=managedinstancegroup_cli.install_windows_updates_on_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The [OCID] of the managed instance group. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def install_windows_updates_on_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.install_windows_updates_on_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.switch_module_stream_on_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.switch_module_stream_on_managed_instance_group.name, help=managedinstancegroup_cli.switch_module_stream_on_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The [OCID] of the managed instance group. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def switch_module_stream_on_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.switch_module_stream_on_managed_instance_group, **kwargs)


@cli_util.copy_params_from_generated_command(managedinstancegroup_cli.reboot_managed_instance_group, params_to_exclude=['managed_instance_group_id'])
@managedinstancegroup_cli.managed_instance_group_group.command(name=managedinstancegroup_cli.reboot_managed_instance_group.name, help=managedinstancegroup_cli.reboot_managed_instance_group.help)
@cli_util.option('--group-id', required=True, help=u"""The [OCID] of the managed instance group. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@cli_util.wrap_exceptions
def reboot_managed_instance_group_extended(ctx, **kwargs):

    if 'group_id' in kwargs:
        kwargs['managed_instance_group_id'] = kwargs['group_id']
        kwargs.pop('group_id')

    ctx.invoke(managedinstancegroup_cli.reboot_managed_instance_group, **kwargs)
