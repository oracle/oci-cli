# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401

from services.os_management_hub.src.oci_cli_os_management_hub.generated import os_management_hub_service_cli
from services.os_management_hub.src.oci_cli_software_source.generated import softwaresource_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci os-management-hub software-source software-source create-software-source-create-custom-software-source-details -> oci os-management-hub software-source software-source create-custom-swsrc
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.create_software_source_create_custom_software_source_details, "create-custom-swsrc")


# oci os-management-hub software-source software-source create-software-source-create-versioned-custom-software-source-details -> oci os-management-hub software-source software-source create-versioned-custom-swsrc
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.create_software_source_create_versioned_custom_software_source_details, "create-versioned-custom-swsrc")


# oci os-management-hub software-source software-source change-availability-of -> oci os-management-hub software-source software-source change-availability
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.change_availability_of_software_sources, "change-availability")


# oci os-management-hub software-source software-source list-module-stream-profiles -> oci os-management-hub software-source software-source list-module-profiles
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.list_module_stream_profiles, "list-module-profiles")


# oci os-management-hub software-source software-source search-software-source-module-streams -> oci os-management-hub software-source software-source search-module-streams
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.search_software_source_module_streams, "search-module-streams")


# oci os-management-hub software-source software-source search-software-source-modules -> oci os-management-hub software-source software-source search-modules
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.search_software_source_modules, "search-modules")


# oci os-management-hub software-source software-source search-software-source-package-groups -> oci os-management-hub software-source software-source search-package-groups
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.search_software_source_package_groups, "search-package-groups")


# oci os-management-hub software-source software-source update-software-source-update-custom-software-source-details -> oci os-management-hub software-source software-source update-custom-swsrc
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.update_software_source_update_custom_software_source_details, "update-custom-swsrc")


# oci os-management-hub software-source erratum get -> oci os-management-hub software-source erratum get-erratum
cli_util.rename_command(softwaresource_cli, softwaresource_cli.erratum_group, softwaresource_cli.get_erratum, "get-erratum")


# oci os-management-hub software-source module-stream get -> oci os-management-hub software-source module-stream get-module-stream
cli_util.rename_command(softwaresource_cli, softwaresource_cli.module_stream_group, softwaresource_cli.get_module_stream, "get-module-stream")


# oci os-management-hub software-source module-stream-profile get -> oci os-management-hub software-source module-stream-profile get-module-profile
cli_util.rename_command(softwaresource_cli, softwaresource_cli.module_stream_profile_group, softwaresource_cli.get_module_stream_profile, "get-module-profile")


# oci os-management-hub software-source package-group get -> oci os-management-hub software-source package-group get-package-group
cli_util.rename_command(softwaresource_cli, softwaresource_cli.package_group_group, softwaresource_cli.get_package_group, "get-package-group")


# Remove create from oci os-management-hub software-source software-source
softwaresource_cli.software_source_group.commands.pop(softwaresource_cli.create_software_source.name)


# Remove update from oci os-management-hub software-source software-source
softwaresource_cli.software_source_group.commands.pop(softwaresource_cli.update_software_source.name)


# Remove update-software-source-update-vendor-software-source-details from oci os-management-hub software-source software-source
softwaresource_cli.software_source_group.commands.pop(softwaresource_cli.update_software_source_update_vendor_software_source_details.name)


# Move commands under 'oci os-management-hub software-source software-source' -> 'oci os-management-hub software-source'
softwaresource_cli.software_source_root_group.commands.pop(softwaresource_cli.software_source_group.name)
os_management_hub_service_cli.os_management_hub_service_group.commands.pop(softwaresource_cli.software_source_root_group.name)
os_management_hub_service_cli.os_management_hub_service_group.add_command(softwaresource_cli.software_source_group)


# Move commands under 'oci os-management-hub software-source erratum' -> 'oci os-management-hub software-source'
softwaresource_cli.software_source_root_group.commands.pop(softwaresource_cli.erratum_group.name)
softwaresource_cli.software_source_group.add_command(softwaresource_cli.get_erratum)
softwaresource_cli.software_source_group.add_command(softwaresource_cli.list_errata)


# Move commands under 'oci os-management-hub software-source module-stream' -> 'oci os-management-hub software-source'
softwaresource_cli.software_source_root_group.commands.pop(softwaresource_cli.module_stream_group.name)
softwaresource_cli.software_source_group.add_command(softwaresource_cli.get_module_stream)


# Move commands under 'oci os-management-hub software-source module-stream-profile' -> 'oci os-management-hub software-source'
softwaresource_cli.software_source_root_group.commands.pop(softwaresource_cli.module_stream_profile_group.name)
softwaresource_cli.software_source_group.add_command(softwaresource_cli.get_module_stream_profile)


# Move commands under 'oci os-management-hub software-source package-group' -> 'oci os-management-hub software-source'
softwaresource_cli.software_source_root_group.commands.pop(softwaresource_cli.package_group_group.name)
softwaresource_cli.software_source_group.add_command(softwaresource_cli.get_package_group)


@cli_util.copy_params_from_generated_command(softwaresource_cli.change_availability_of_software_sources, params_to_exclude=['software_source_availabilities'])
@softwaresource_cli.software_source_group.command(name=softwaresource_cli.change_availability_of_software_sources.name, help=softwaresource_cli.change_availability_of_software_sources.help)
@cli_util.option('--availabilities', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of objects containing software source ids and its availability.

This option is a JSON list with items of type SoftwareSourceAvailability.  For documentation on SoftwareSourceAvailability please see our API reference: https://docs.cloud.oracle.com/api/#/en/softwaresource/20220901/datatypes/SoftwareSourceAvailability.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'availabilities': {'module': 'os_management_hub', 'class': 'list[SoftwareSourceAvailability]'}})
@cli_util.wrap_exceptions
def change_availability_of_software_sources_extended(ctx, **kwargs):

    if 'availabilities' in kwargs:
        kwargs['software_source_availabilities'] = kwargs['availabilities']
        kwargs.pop('availabilities')

    ctx.invoke(softwaresource_cli.change_availability_of_software_sources, **kwargs)


@cli_util.copy_params_from_generated_command(softwaresource_cli.create_software_source_create_custom_software_source_details, params_to_exclude=['custom_software_source_filter', 'is_automatically_updated'])
@softwaresource_cli.software_source_group.command(name=softwaresource_cli.create_software_source_create_custom_software_source_details.name, help=softwaresource_cli.create_software_source_create_custom_software_source_details.help)
@cli_util.option('--filter', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-auto-updated', type=click.BOOL, help=u"""Indicates whether service should automatically update the custom software source for the user.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'os_management_hub', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management_hub', 'class': 'dict(str, dict(str, object))'}, 'vendor-software-sources': {'module': 'os_management_hub', 'class': 'list[Id]'}, 'filter': {'module': 'os_management_hub', 'class': 'CustomSoftwareSourceFilter'}}, output_type={'module': 'os_management_hub', 'class': 'SoftwareSource'})
@cli_util.wrap_exceptions
def create_software_source_create_custom_software_source_details_extended(ctx, **kwargs):

    if 'filter' in kwargs:
        kwargs['custom_software_source_filter'] = kwargs['filter']
        kwargs.pop('filter')

    if 'is_auto_updated' in kwargs:
        kwargs['is_automatically_updated'] = kwargs['is_auto_updated']
        kwargs.pop('is_auto_updated')

    ctx.invoke(softwaresource_cli.create_software_source_create_custom_software_source_details, **kwargs)


@cli_util.copy_params_from_generated_command(softwaresource_cli.create_software_source_create_versioned_custom_software_source_details, params_to_exclude=['custom_software_source_filter'])
@softwaresource_cli.software_source_group.command(name=softwaresource_cli.create_software_source_create_versioned_custom_software_source_details.name, help=softwaresource_cli.create_software_source_create_versioned_custom_software_source_details.help)
@cli_util.option('--filter', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'os_management_hub', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management_hub', 'class': 'dict(str, dict(str, object))'}, 'vendor-software-sources': {'module': 'os_management_hub', 'class': 'list[Id]'}, 'filter': {'module': 'os_management_hub', 'class': 'CustomSoftwareSourceFilter'}}, output_type={'module': 'os_management_hub', 'class': 'SoftwareSource'})
@cli_util.wrap_exceptions
def create_software_source_create_versioned_custom_software_source_details_extended(ctx, **kwargs):

    if 'filter' in kwargs:
        kwargs['custom_software_source_filter'] = kwargs['filter']
        kwargs.pop('filter')

    ctx.invoke(softwaresource_cli.create_software_source_create_versioned_custom_software_source_details, **kwargs)


@cli_util.copy_params_from_generated_command(softwaresource_cli.list_software_sources, params_to_exclude=['display_name_not_equal_to', 'is_mandatory_for_autonomous_linux'])
@softwaresource_cli.software_source_group.command(name=softwaresource_cli.list_software_sources.name, help=softwaresource_cli.list_software_sources.help)
@cli_util.option('--is-mandatory-for-alx', type=click.BOOL, help="""Indicates whether the software source is mandatory for the Autonomous Linux service.""")
@cli_util.option('--display-name-ne', multiple=True, help=u"""A multi filter to return resources that do not contains the given display names.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'display-name-not-equal-to': {'module': 'os_management_hub', 'class': 'list[string]'}}, output_type={'module': 'os_management_hub', 'class': 'SoftwareSourceCollection'})
@cli_util.wrap_exceptions
def list_software_sources_extended(ctx, **kwargs):

    if 'is_mandatory_for_alx' in kwargs:
        kwargs['is_mandatory_for_autonomous_linux'] = kwargs['is_mandatory_for_alx']
        kwargs.pop('is_mandatory_for_alx')

    if 'display_name_ne' in kwargs:
        kwargs['display_name_not_equal_to'] = kwargs['display_name_ne']
        kwargs.pop('display_name_ne')

    ctx.invoke(softwaresource_cli.list_software_sources, **kwargs)


@cli_util.copy_params_from_generated_command(softwaresource_cli.update_software_source_update_custom_software_source_details, params_to_exclude=['custom_software_source_filter', 'is_automatically_updated'])
@softwaresource_cli.software_source_group.command(name=softwaresource_cli.update_software_source_update_custom_software_source_details.name, help=softwaresource_cli.update_software_source_update_custom_software_source_details.help)
@cli_util.option('--filter', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-auto-updated', type=click.BOOL, help=u"""Indicates whether service should automatically update the custom software source for the user.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'os_management_hub', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management_hub', 'class': 'dict(str, dict(str, object))'}, 'vendor-software-sources': {'module': 'os_management_hub', 'class': 'list[Id]'}, 'filter': {'module': 'os_management_hub', 'class': 'CustomSoftwareSourceFilter'}}, output_type={'module': 'os_management_hub', 'class': 'SoftwareSource'})
@cli_util.wrap_exceptions
def update_software_source_update_custom_software_source_details_extended(ctx, **kwargs):

    if 'filter' in kwargs:
        kwargs['custom_software_source_filter'] = kwargs['filter']
        kwargs.pop('filter')

    if 'is_auto_updated' in kwargs:
        kwargs['is_automatically_updated'] = kwargs['is_auto_updated']
        kwargs.pop('is_auto_updated')

    ctx.invoke(softwaresource_cli.update_software_source_update_custom_software_source_details, **kwargs)


@cli_util.copy_params_from_generated_command(softwaresource_cli.list_module_stream_profiles, params_to_exclude=['name'])
@softwaresource_cli.software_source_group.command(name=softwaresource_cli.list_module_stream_profiles.name, help=softwaresource_cli.list_module_stream_profiles.help)
@cli_util.option('--profile-name', help=u"""The name of the profile.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management_hub', 'class': 'ModuleStreamProfileCollection'})
@cli_util.wrap_exceptions
def list_module_stream_profiles_extended(ctx, **kwargs):

    if 'profile_name' in kwargs:
        kwargs['name'] = kwargs['profile_name']
        kwargs.pop('profile_name')

    ctx.invoke(softwaresource_cli.list_module_stream_profiles, **kwargs)


@cli_util.copy_params_from_generated_command(softwaresource_cli.list_module_streams, params_to_exclude=['name'])
@softwaresource_cli.software_source_group.command(name=softwaresource_cli.list_module_streams.name, help=softwaresource_cli.list_module_streams.help)
@cli_util.option('--stream-name', help=u"""The name of the stream.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management_hub', 'class': 'ModuleStreamCollection'})
@cli_util.wrap_exceptions
def list_module_streams_extended(ctx, **kwargs):

    if 'stream_name' in kwargs:
        kwargs['name'] = kwargs['stream_name']
        kwargs.pop('stream_name')

    ctx.invoke(softwaresource_cli.list_module_streams, **kwargs)


@cli_util.copy_params_from_generated_command(softwaresource_cli.search_software_source_modules, params_to_exclude=['name', 'name_contains'])
@softwaresource_cli.software_source_group.command(name=softwaresource_cli.search_software_source_modules.name, help=softwaresource_cli.search_software_source_modules.help)
@cli_util.option('--module-name', help=u"""The name of a module.""")
@cli_util.option('--module-name-contains', help=u"""filters results, allowing only those with a name which contains the string.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'software-source-ids': {'module': 'os_management_hub', 'class': 'list[string]'}}, output_type={'module': 'os_management_hub', 'class': 'ModuleCollection'})
@cli_util.wrap_exceptions
def search_software_source_modules_extended(ctx, **kwargs):

    if 'module_name' in kwargs:
        kwargs['name'] = kwargs['module_name']
        kwargs.pop('module_name')

    if 'module_name_contains' in kwargs:
        kwargs['name_contains'] = kwargs['module_name_contains']
        kwargs.pop('module_name_contains')

    ctx.invoke(softwaresource_cli.search_software_source_modules, **kwargs)


# oci os-management-hub software-source add -> oci os-management-hub software-source add-packages
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.add_packages_to_software_source, "add-packages")


# oci os-management-hub software-source create-software-source-create-vendor-software-source-details -> oci os-management-hub software-source replicate-vendor-swsrc
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.create_software_source_create_vendor_software_source_details, "replicate-vendor-swsrc")


# oci os-management-hub software-source list-software-package -> oci os-management-hub software-source list-software-sources-with-package
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.list_software_package_software_sources, "list-software-sources-with-package")


# oci os-management-hub software-source update-software-source-update-versioned-custom-software-source-details -> oci os-management-hub software-source update-versioned-custom-swsrc
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.update_software_source_update_versioned_custom_software_source_details, "update-versioned-custom-swsrc")


@cli_util.copy_params_from_generated_command(softwaresource_cli.list_all_software_packages, params_to_exclude=['version_parameterconflict'])
@softwaresource_cli.software_source_group.command(name=softwaresource_cli.list_all_software_packages.name, help=softwaresource_cli.list_all_software_packages.help)
@cli_util.option('--package-version', help=u"""A filter to return software packages that match the given version.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management_hub', 'class': 'SoftwarePackageCollection'})
@cli_util.wrap_exceptions
def list_all_software_packages_extended(ctx, **kwargs):

    if 'package_version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['package_version']
        kwargs.pop('package_version')

    ctx.invoke(softwaresource_cli.list_all_software_packages, **kwargs)


# oci os-management-hub software-source create-software-source-create-private-software-source-details -> oci os-management-hub software-source create-private-swsrc
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.create_software_source_create_private_software_source_details, "create-private-swsrc")


# oci os-management-hub software-source create-software-source-create-third-party-software-source-details -> oci os-management-hub software-source create-third-party-swsrc
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.create_software_source_create_third_party_software_source_details, "create-third-party-swsrc")


# oci os-management-hub software-source remove -> oci os-management-hub software-source remove-packages
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.remove_packages_from_software_source, "remove-packages")


# oci os-management-hub software-source replace-packages-in -> oci os-management-hub software-source replace-packages
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.replace_packages_in_software_source, "replace-packages")


# oci os-management-hub software-source software-source-generate-metadata -> oci os-management-hub software-source generate-metadata
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.software_source_generate_metadata, "generate-metadata")


# oci os-management-hub software-source update-software-source-update-private-software-source-details -> oci os-management-hub software-source update-private-swsrc
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.update_software_source_update_private_software_source_details, "update-private-swsrc")


# oci os-management-hub software-source update-software-source-update-third-party-software-source-details -> oci os-management-hub software-source update-third-party-swsrc
cli_util.rename_command(softwaresource_cli, softwaresource_cli.software_source_group, softwaresource_cli.update_software_source_update_third_party_software_source_details, "update-third-party-swsrc")
