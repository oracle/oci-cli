# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli.cli_util import get_param, rename_command
from services.ocvp.src.oci_cli_sddc.generated import sddc_cli
from services.ocvp.src.oci_cli_ocvp.generated import ocvs_service_cli

# Shorten parameters for create command
get_param(sddc_cli.create_sddc, 'compute_availability_domain').opts.extend(['--ad'])
get_param(sddc_cli.create_sddc, 'display_name').opts.extend(['--name'])

# Shorten parameters for update command
get_param(sddc_cli.update_sddc, 'display_name').opts.extend(['--name'])

# Shorten parameters for list command
get_param(sddc_cli.list_sddcs, 'compute_availability_domain').opts.extend(['--ad'])
get_param(sddc_cli.list_sddcs, 'display_name').opts.extend(['--name'])

# Rename commands
rename_command(sddc_cli, sddc_cli.sddc_summary_group, sddc_cli.list_sddcs, "list")
rename_command(sddc_cli, sddc_cli.supported_vmware_software_version_summary_group, sddc_cli.list_supported_vmware_software_versions, "vmware-versions")


@cli_util.copy_params_from_generated_command(sddc_cli.create_sddc, params_to_exclude=['vmware_software_version', 'esxi_hosts_count', 'provisioning_subnet_id',
                                                                                      'vsphere_vlan_id', 'vmotion_vlan_id', 'vsan_vlan_id', 'nsx_v_tep_vlan_id',
                                                                                      'nsx_edge_v_tep_vlan_id', 'nsx_edge_uplink1_vlan_id', 'nsx_edge_uplink2_vlan_id',
                                                                                      'instance_display_name_prefix', 'workload_network_cidr'])
@sddc_cli.sddc_group.command(name=cli_util.override('create_sddc.command_name', 'create'), help=sddc_cli.create_sddc.help)
@cli_util.option('--esxi-count', required=True, help=u"""The number of ESXi hosts to create in the SDDC. You can add more hosts later (see [CreateEsxiHost]).

**Note:** If you later delete EXSi hosts from the SDDC to total less than 3, you are still billed for the 3 minimum recommended EXSi hosts. Also, you cannot add more VMware workloads to the SDDC until it again has at least 3 ESXi hosts.""")
@cli_util.option('--prov-subnet-id', required=True, help=u"""The [OCID] of the management subnet to use for provisioning the SDDC.""")
@cli_util.option('--vsphere-id', required=True, help=u"""The [OCID] of the VLAN to use for the vSphere component of the VMware environment.""")
@cli_util.option('--vmotion-id', required=True, help=u"""The [OCID] of the VLAN to use for the vMotion component of the VMware environment.""")
@cli_util.option('--vsan-id', required=True, help=u"""The [OCID] of the VLAN to use for the vSAN component of the VMware environment.""")
@cli_util.option('--nsx-vtep-id', required=True, help=u"""The [OCID] of the VLAN to use for the NSX VTEP component of the VMware environment.""")
@cli_util.option('--nsx-edge-vtep-id', required=True, help=u"""The [OCID] of the VLAN to use for the NSX Edge VTEP component of the VMware environment.""")
@cli_util.option('--nsx-edge-up1-id', required=True, help=u"""The [OCID] of the VLAN to use for the NSX Edge Uplink 1 component of the VMware environment.""")
@cli_util.option('--nsx-edge-up2-id', required=True, help=u"""The [OCID] of the VLAN to use for the NSX Edge Uplink 2 component of the VMware environment.""")
@cli_util.option('--instance-prefix', required=True, help=cli_util.get_param(sddc_cli.create_sddc, 'instance_display_name_prefix').help)
@cli_util.option('--workload-cidr', help=cli_util.get_param(sddc_cli.create_sddc, 'workload_network_cidr').help)
@cli_util.option('--vmware-version', required=True, help=u"""The VMware software bundle to install on the ESXi hosts in the SDDC. To get a list of the available versions, use [ListSupportedVmwareSoftwareVersions].""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_sddc(ctx, **kwargs):
    if 'esxi_count' in kwargs:
        kwargs['esxi_hosts_count'] = kwargs['esxi_count']
        kwargs.pop('esxi_count')
    if 'prov_subnet_id' in kwargs:
        kwargs['provisioning_subnet_id'] = kwargs['prov_subnet_id']
        kwargs.pop('prov_subnet_id')
    if 'vsphere_id' in kwargs:
        kwargs['vsphere_vlan_id'] = kwargs['vsphere_id']
        kwargs.pop('vsphere_id')
    if 'vmotion_id' in kwargs:
        kwargs['vmotion_vlan_id'] = kwargs['vmotion_id']
        kwargs.pop('vmotion_id')
    if 'vsan_id' in kwargs:
        kwargs['vsan_vlan_id'] = kwargs['vsan_id']
        kwargs.pop('vsan_id')
    if 'nsx_vtep_id' in kwargs:
        kwargs['nsx_v_tep_vlan_id'] = kwargs['nsx_vtep_id']
        kwargs.pop('nsx_vtep_id')
    if 'nsx_edge_vtep_id' in kwargs:
        kwargs['nsx_edge_v_tep_vlan_id'] = kwargs['nsx_edge_vtep_id']
        kwargs.pop('nsx_edge_vtep_id')
    if 'nsx_edge_up1_id' in kwargs:
        kwargs['nsx_edge_uplink1_vlan_id'] = kwargs['nsx_edge_up1_id']
        kwargs.pop('nsx_edge_up1_id')
    if 'nsx_edge_up2_id' in kwargs:
        kwargs['nsx_edge_uplink2_vlan_id'] = kwargs['nsx_edge_up2_id']
        kwargs.pop('nsx_edge_up2_id')
    if 'instance_prefix' in kwargs:
        kwargs['instance_display_name_prefix'] = kwargs['instance_prefix']
        kwargs.pop('instance_prefix')
    if 'workload_cidr' in kwargs:
        kwargs['instance_display_name_prefix'] = kwargs['workload_cidr']
        kwargs.pop('workload_cidr')
    if 'vmware_version' in kwargs:
        kwargs['vmware_software_version'] = kwargs['vmware_version']
        kwargs.pop('vmware_version')

    ctx.invoke(sddc_cli.create_sddc, **kwargs)


@cli_util.copy_params_from_generated_command(sddc_cli.update_sddc, params_to_exclude=['vmware_software_version', 'vsphere_vlan_id', 'vmotion_vlan_id', 'vsan_vlan_id', 'nsx_v_tep_vlan_id',
                                                                                      'nsx_edge_v_tep_vlan_id', 'nsx_edge_uplink1_vlan_id', 'nsx_edge_uplink2_vlan_id',
                                                                                      'instance_display_name_prefix', 'workload_network_cidr'])
@sddc_cli.sddc_group.command(name=cli_util.override('update_sddc.command_name', 'update'), help=sddc_cli.update_sddc.help)
@cli_util.option('--vsphere-id', required=True, help=u"""The [OCID] of the VLAN to use for the vSphere component of the VMware environment.""")
@cli_util.option('--vmotion-id', required=True, help=u"""The [OCID] of the VLAN to use for the vMotion component of the VMware environment.""")
@cli_util.option('--vsan-id', required=True, help=u"""The [OCID] of the VLAN to use for the vSAN component of the VMware environment.""")
@cli_util.option('--nsx-vtep-id', required=True, help=u"""The [OCID] of the VLAN to use for the NSX VTEP component of the VMware environment.""")
@cli_util.option('--nsx-edge-vtep-id', required=True, help=u"""The [OCID] of the VLAN to use for the NSX Edge VTEP component of the VMware environment.""")
@cli_util.option('--nsx-edge-up1-id', required=True, help=u"""The [OCID] of the VLAN to use for the NSX Edge Uplink 1 component of the VMware environment.""")
@cli_util.option('--nsx-edge-up2-id', required=True, help=u"""The [OCID] of the VLAN to use for the NSX Edge Uplink 2 component of the VMware environment.""")
@cli_util.option('--vmware-version', required=True, help=u"""The VMware software bundle to install on the ESXi hosts in the SDDC. To get a list of the available versions, use [ListSupportedVmwareSoftwareVersions].""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ocvp', 'class': 'Sddc'})
@cli_util.wrap_exceptions
def update_sddc(ctx, **kwargs):
    if 'vsphere_id' in kwargs:
        kwargs['vsphere_vlan_id'] = kwargs['vsphere_id']
        kwargs.pop('vsphere_id')
    if 'vmotion_id' in kwargs:
        kwargs['vmotion_vlan_id'] = kwargs['vmotion_id']
        kwargs.pop('vmotion_id')
    if 'vsan_id' in kwargs:
        kwargs['vsan_vlan_id'] = kwargs['vsan_id']
        kwargs.pop('vsan_id')
    if 'nsx_vtep_id' in kwargs:
        kwargs['nsx_v_tep_vlan_id'] = kwargs['nsx_vtep_id']
        kwargs.pop('nsx_vtep_id')
    if 'nsx_edge_vtep_id' in kwargs:
        kwargs['nsx_edge_v_tep_vlan_id'] = kwargs['nsx_edge_vtep_id']
        kwargs.pop('nsx_edge_vtep_id')
    if 'nsx_edge_up1_id' in kwargs:
        kwargs['nsx_edge_uplink1_vlan_id'] = kwargs['nsx_edge_up1_id']
        kwargs.pop('nsx_edge_up1_id')
    if 'nsx_edge_up2_id' in kwargs:
        kwargs['nsx_edge_uplink2_vlan_id'] = kwargs['nsx_edge_up2_id']
        kwargs.pop('nsx_edge_up2_id')
    if 'vmware_version' in kwargs:
        kwargs['vmware_software_version'] = kwargs['vmware_version']
        kwargs.pop('vmware_version')

    ctx.invoke(sddc_cli.update_sddc, **kwargs)


ocvs_service_cli.ocvs_service_group.commands.pop(sddc_cli.sddc_root_group.name)
ocvs_service_cli.ocvs_service_group.add_command(sddc_cli.sddc_group)
sddc_cli.sddc_group.add_command(sddc_cli.list_supported_vmware_software_versions)
sddc_cli.sddc_group.add_command(sddc_cli.list_sddcs)
