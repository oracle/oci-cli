# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli.cli_util import get_param, rename_command
from services.ocvp.src.oci_cli_sddc.generated import sddc_cli
from services.ocvp.src.oci_cli_ocvp.generated import ocvs_service_cli

# Shorten parameters for create command
# get_param(sddc_cli.create_sddc, 'compute_availability_domain').opts.extend(['--ad'])
get_param(sddc_cli.create_sddc, 'display_name').opts.extend(['--name'])

# Shorten parameters for update command
get_param(sddc_cli.update_sddc, 'display_name').opts.extend(['--name'])

# Shorten parameters for list command
# get_param(sddc_cli.list_sddcs, 'compute_availability_domain').opts.extend(['--ad'])
get_param(sddc_cli.list_sddcs, 'display_name').opts.extend(['--name'])

# Rename commands
rename_command(sddc_cli, sddc_cli.sddc_summary_group, sddc_cli.list_sddcs, "list")
rename_command(sddc_cli, sddc_cli.supported_vmware_software_version_summary_group, sddc_cli.list_supported_vmware_software_versions, "vmware-versions")


@cli_util.copy_params_from_generated_command(sddc_cli.create_sddc, params_to_exclude=['vmware_software_version'])
@sddc_cli.sddc_group.command(name=cli_util.override('create_sddc.command_name', 'create'), help=sddc_cli.create_sddc.help)
@cli_util.option('--vmware-version', required=True, help=u"""The VMware software bundle to install on the ESXi hosts in the SDDC. To get a list of the available versions, use [ListSupportedVmwareSoftwareVersions].""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_sddc(ctx, **kwargs):
    if 'vmware_version' in kwargs:
        kwargs['vmware_software_version'] = kwargs['vmware_version']
        kwargs.pop('vmware_version')

    ctx.invoke(sddc_cli.create_sddc, **kwargs)


@cli_util.copy_params_from_generated_command(sddc_cli.update_sddc, params_to_exclude=['vmware_software_version'])
@sddc_cli.sddc_group.command(name=cli_util.override('update_sddc.command_name', 'update'), help=sddc_cli.update_sddc.help)
@cli_util.option('--vmware-version', required=True, help=u"""The VMware software bundle to install on the ESXi hosts in the SDDC. To get a list of the available versions, use [ListSupportedVmwareSoftwareVersions].""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ocvp', 'class': 'Sddc'})
@cli_util.wrap_exceptions
def update_sddc(ctx, **kwargs):
    if 'vmware_version' in kwargs:
        kwargs['vmware_software_version'] = kwargs['vmware_version']
        kwargs.pop('vmware_version')

    ctx.invoke(sddc_cli.update_sddc, **kwargs)


ocvs_service_cli.ocvs_service_group.commands.pop(sddc_cli.sddc_root_group.name)
ocvs_service_cli.ocvs_service_group.add_command(sddc_cli.sddc_group)
sddc_cli.sddc_group.add_command(sddc_cli.list_supported_vmware_software_versions)
sddc_cli.sddc_group.add_command(sddc_cli.list_sddcs)


@cli_util.copy_params_from_generated_command(sddc_cli.list_supported_vmware_software_versions, params_to_exclude=['version_parameterconflict'])
@sddc_cli.sddc_group.command(name=sddc_cli.list_supported_vmware_software_versions.name, help=sddc_cli.list_supported_vmware_software_versions.help)
@cli_util.option('--version-name', help=u"""A filter to return only resources that match the given VMware software version exactly.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ocvp', 'class': 'SupportedVmwareSoftwareVersionCollection'})
@cli_util.wrap_exceptions
def list_supported_vmware_software_versions_extended(ctx, **kwargs):

    if 'version_name' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['version_name']
        kwargs.pop('version_name')

    ctx.invoke(sddc_cli.list_supported_vmware_software_versions, **kwargs)
