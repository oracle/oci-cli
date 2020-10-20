# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.ocvp.src.oci_cli_ocvp.generated import ocvs_service_cli


@click.command(cli_util.override('sddc.sddc_root_group.command_name', 'sddc'), cls=CommandGroupWithAlias, help=cli_util.override('sddc.sddc_root_group.help', """Use this API to manage the Oracle Cloud VMware Solution."""), short_help=cli_util.override('sddc.sddc_root_group.short_help', """Oracle Cloud VMware Solution API"""))
@cli_util.help_option_group
def sddc_root_group():
    pass


@click.command(cli_util.override('sddc.sddc_group.command_name', 'sddc'), cls=CommandGroupWithAlias, help="""A software-defined data center (SDDC) contains the resources required for a functional VMware environment. Instances in an SDDC (see [EsxiHost]) run in a virtual cloud network (VCN) and are preconfigured with VMware and storage. Use the vCenter utility to manage and deploy VMware virtual machines (VMs) in the SDDC.

The SDDC uses a single management subnet for provisioning the SDDC. It also uses a set of VLANs for various components of the VMware environment (vSphere, vMotion, vSAN, and so on). See the Core Services API for information about VCN subnets and VLANs.""")
@cli_util.help_option_group
def sddc_group():
    pass


@click.command(cli_util.override('sddc.supported_vmware_software_version_summary_group.command_name', 'supported-vmware-software-version-summary'), cls=CommandGroupWithAlias, help="""A specific version of bundled VMware software supported by the Oracle Cloud VMware Solution.""")
@cli_util.help_option_group
def supported_vmware_software_version_summary_group():
    pass


@click.command(cli_util.override('sddc.sddc_summary_group.command_name', 'sddc-summary'), cls=CommandGroupWithAlias, help="""A summary of the SDDC.""")
@cli_util.help_option_group
def sddc_summary_group():
    pass


ocvs_service_cli.ocvs_service_group.add_command(sddc_root_group)
sddc_root_group.add_command(sddc_group)
sddc_root_group.add_command(supported_vmware_software_version_summary_group)
sddc_root_group.add_command(sddc_summary_group)


@sddc_group.command(name=cli_util.override('sddc.change_sddc_compartment.command_name', 'change-compartment'), help=u"""Moves an SDDC into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeSddcCompartment)""")
@cli_util.option('--sddc-id', required=True, help=u"""The [OCID] of the SDDC.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the SDDC to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_sddc_compartment(ctx, from_json, sddc_id, compartment_id, if_match):

    if isinstance(sddc_id, six.string_types) and len(sddc_id.strip()) == 0:
        raise click.UsageError('Parameter --sddc-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('ocvp', 'sddc', ctx)
    result = client.change_sddc_compartment(
        sddc_id=sddc_id,
        change_sddc_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@sddc_group.command(name=cli_util.override('sddc.create_sddc.command_name', 'create'), help=u"""Creates a software-defined data center (SDDC).

Use the [WorkRequest] operations to track the creation of the SDDC. \n[Command Reference](createSddc)""")
@cli_util.option('--compute-availability-domain', required=True, help=u"""The availability domain to create the SDDC's ESXi hosts in.""")
@cli_util.option('--vmware-software-version', required=True, help=u"""The VMware software bundle to install on the ESXi hosts in the SDDC. To get a list of the available versions, use [ListSupportedVmwareSoftwareVersions].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to contain the SDDC.""")
@cli_util.option('--esxi-hosts-count', required=True, type=click.INT, help=u"""The number of ESXi hosts to create in the SDDC. You can add more hosts later (see [CreateEsxiHost]).

**Note:** If you later delete EXSi hosts from the SDDC to total less than 3, you are still billed for the 3 minimum recommended EXSi hosts. Also, you cannot add more VMware workloads to the SDDC until it again has at least 3 ESXi hosts.""")
@cli_util.option('--ssh-authorized-keys', required=True, help=u"""One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for the default user on each ESXi host. Use a newline character to separate multiple keys. The SSH keys must be in the format required for the `authorized_keys` file""")
@cli_util.option('--provisioning-subnet-id', required=True, help=u"""The [OCID] of the management subnet to use for provisioning the SDDC.""")
@cli_util.option('--vsphere-vlan-id', required=True, help=u"""The [OCID] of the VLAN to use for the vSphere component of the VMware environment.""")
@cli_util.option('--vmotion-vlan-id', required=True, help=u"""The [OCID] of the VLAN to use for the vMotion component of the VMware environment.""")
@cli_util.option('--vsan-vlan-id', required=True, help=u"""The [OCID] of the VLAN to use for the vSAN component of the VMware environment.""")
@cli_util.option('--nsx-v-tep-vlan-id', required=True, help=u"""The [OCID] of the VLAN to use for the NSX VTEP component of the VMware environment.""")
@cli_util.option('--nsx-edge-v-tep-vlan-id', required=True, help=u"""The [OCID] of the VLAN to use for the NSX Edge VTEP component of the VMware environment.""")
@cli_util.option('--nsx-edge-uplink1-vlan-id', required=True, help=u"""The [OCID] of the VLAN to use for the NSX Edge Uplink 1 component of the VMware environment.""")
@cli_util.option('--nsx-edge-uplink2-vlan-id', required=True, help=u"""The [OCID] of the VLAN to use for the NSX Edge Uplink 2 component of the VMware environment.""")
@cli_util.option('--display-name', help=u"""A descriptive name for the SDDC. SDDC name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the region. Avoid entering confidential information.""")
@cli_util.option('--instance-display-name-prefix', help=u"""A prefix used in the name of each ESXi host and Compute instance in the SDDC. If this isn't set, the SDDC's `displayName` is used as the prefix.

For example, if the value is `mySDDC`, the ESXi hosts are named `mySDDC-1`, `mySDDC-2`, and so on.""")
@cli_util.option('--is-hcx-enabled', type=click.BOOL, help=u"""This flag tells us if HCX is enabled or not.""")
@cli_util.option('--hcx-vlan-id', help=u"""This id is required only when hcxEnabled is true""")
@cli_util.option('--workload-network-cidr', help=u"""The CIDR block for the IP addresses that VMware VMs in the SDDC use to run application workloads.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_sddc(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compute_availability_domain, vmware_software_version, compartment_id, esxi_hosts_count, ssh_authorized_keys, provisioning_subnet_id, vsphere_vlan_id, vmotion_vlan_id, vsan_vlan_id, nsx_v_tep_vlan_id, nsx_edge_v_tep_vlan_id, nsx_edge_uplink1_vlan_id, nsx_edge_uplink2_vlan_id, display_name, instance_display_name_prefix, is_hcx_enabled, hcx_vlan_id, workload_network_cidr, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['computeAvailabilityDomain'] = compute_availability_domain
    _details['vmwareSoftwareVersion'] = vmware_software_version
    _details['compartmentId'] = compartment_id
    _details['esxiHostsCount'] = esxi_hosts_count
    _details['sshAuthorizedKeys'] = ssh_authorized_keys
    _details['provisioningSubnetId'] = provisioning_subnet_id
    _details['vsphereVlanId'] = vsphere_vlan_id
    _details['vmotionVlanId'] = vmotion_vlan_id
    _details['vsanVlanId'] = vsan_vlan_id
    _details['nsxVTepVlanId'] = nsx_v_tep_vlan_id
    _details['nsxEdgeVTepVlanId'] = nsx_edge_v_tep_vlan_id
    _details['nsxEdgeUplink1VlanId'] = nsx_edge_uplink1_vlan_id
    _details['nsxEdgeUplink2VlanId'] = nsx_edge_uplink2_vlan_id

    if display_name is not None:
        _details['displayName'] = display_name

    if instance_display_name_prefix is not None:
        _details['instanceDisplayNamePrefix'] = instance_display_name_prefix

    if is_hcx_enabled is not None:
        _details['isHcxEnabled'] = is_hcx_enabled

    if hcx_vlan_id is not None:
        _details['hcxVlanId'] = hcx_vlan_id

    if workload_network_cidr is not None:
        _details['workloadNetworkCidr'] = workload_network_cidr

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ocvp', 'sddc', ctx)
    result = client.create_sddc(
        create_sddc_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@sddc_group.command(name=cli_util.override('sddc.delete_sddc.command_name', 'delete'), help=u"""Deletes the specified SDDC, along with the other resources that were created with the SDDC. For example: the Compute instances, DNS records, and so on.

Use the [WorkRequest] operations to track the deletion of the SDDC. \n[Command Reference](deleteSddc)""")
@cli_util.option('--sddc-id', required=True, help=u"""The [OCID] of the SDDC.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_sddc(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, sddc_id, if_match):

    if isinstance(sddc_id, six.string_types) and len(sddc_id.strip()) == 0:
        raise click.UsageError('Parameter --sddc-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ocvp', 'sddc', ctx)
    result = client.delete_sddc(
        sddc_id=sddc_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@sddc_group.command(name=cli_util.override('sddc.get_sddc.command_name', 'get'), help=u"""Gets the specified SDDC's information. \n[Command Reference](getSddc)""")
@cli_util.option('--sddc-id', required=True, help=u"""The [OCID] of the SDDC.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ocvp', 'class': 'Sddc'})
@cli_util.wrap_exceptions
def get_sddc(ctx, from_json, sddc_id):

    if isinstance(sddc_id, six.string_types) and len(sddc_id.strip()) == 0:
        raise click.UsageError('Parameter --sddc-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ocvp', 'sddc', ctx)
    result = client.get_sddc(
        sddc_id=sddc_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@sddc_summary_group.command(name=cli_util.override('sddc.list_sddcs.command_name', 'list-sddcs'), help=u"""Lists the SDDCs in the specified compartment. The list can be filtered by display name or availability domain. \n[Command Reference](listSddcs)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--compute-availability-domain', help=u"""The name of the availability domain that the Compute instances are running in.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The lifecycle state of the resource.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ocvp', 'class': 'SddcCollection'})
@cli_util.wrap_exceptions
def list_sddcs(ctx, from_json, all_pages, page_size, compartment_id, compute_availability_domain, display_name, limit, page, sort_order, sort_by, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compute_availability_domain is not None:
        kwargs['compute_availability_domain'] = compute_availability_domain
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ocvp', 'sddc', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_sddcs,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_sddcs,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_sddcs(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@supported_vmware_software_version_summary_group.command(name=cli_util.override('sddc.list_supported_vmware_software_versions.command_name', 'list-supported-vmware-software-versions'), help=u"""Lists the versions of bundled VMware software supported by the Oracle Cloud VMware Solution. \n[Command Reference](listSupportedVmwareSoftwareVersions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ocvp', 'class': 'SupportedVmwareSoftwareVersionCollection'})
@cli_util.wrap_exceptions
def list_supported_vmware_software_versions(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ocvp', 'sddc', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_supported_vmware_software_versions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_supported_vmware_software_versions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_supported_vmware_software_versions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@sddc_group.command(name=cli_util.override('sddc.update_sddc.command_name', 'update'), help=u"""Updates the specified SDDC.

**Important:** Updating an SDDC affects only certain attributes in the `Sddc` object and does not affect the VMware environment currently running in the SDDC. For more information, see [UpdateSddcDetails]. \n[Command Reference](updateSddc)""")
@cli_util.option('--sddc-id', required=True, help=u"""The [OCID] of the SDDC.""")
@cli_util.option('--display-name', help=u"""The [OCID] of the SDDC. SDDC name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the region.""")
@cli_util.option('--vmware-software-version', help=u"""The version of bundled VMware software that the Oracle Cloud VMware Solution will install on any new ESXi hosts that you add to this SDDC in the future.

For the list of versions supported by the Oracle Cloud VMware Solution, see [ListSupportedVmwareSoftwareVersions]).""")
@cli_util.option('--ssh-authorized-keys', help=u"""One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for the default user on each ESXi host, only when adding new ESXi hosts to this SDDC. Use a newline character to separate multiple keys. The SSH keys must be in the format required for the `authorized_keys` file.""")
@cli_util.option('--vsphere-vlan-id', help=u"""The [OCID] of the VLAN to use for the vSphere component of the VMware environment when adding new ESXi hosts to the SDDC.""")
@cli_util.option('--vmotion-vlan-id', help=u"""The [OCID] of the VLAN to use for the vMotion component of the VMware environment when adding new ESXi hosts to the SDDC.""")
@cli_util.option('--vsan-vlan-id', help=u"""The [OCID] of the VLAN to use for the vSAN component of the VMware environment when adding new ESXi hosts to the SDDC.""")
@cli_util.option('--nsx-v-tep-vlan-id', help=u"""The [OCID] of the VLAN to use for the NSX VTEP component of the VMware environment when adding new ESXi hosts to the SDDC.""")
@cli_util.option('--nsx-edge-v-tep-vlan-id', help=u"""The [OCID] of the VLAN to use for the NSX Edge VTEP component of the VMware environment when adding new ESXi hosts to the SDDC.""")
@cli_util.option('--nsx-edge-uplink1-vlan-id', help=u"""The [OCID] of the VLAN to use for the NSX Edge Uplink 1 component of the VMware environment when adding new ESXi hosts to the SDDC.""")
@cli_util.option('--nsx-edge-uplink2-vlan-id', help=u"""The [OCID] of the VLAN to use for the NSX Edge Uplink 2 component of the VMware environment when adding new ESXi hosts to the SDDC.""")
@cli_util.option('--hcx-vlan-id', help=u"""This id is editable only when hcxEnabled is true""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ocvp', 'class': 'Sddc'})
@cli_util.wrap_exceptions
def update_sddc(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, sddc_id, display_name, vmware_software_version, ssh_authorized_keys, vsphere_vlan_id, vmotion_vlan_id, vsan_vlan_id, nsx_v_tep_vlan_id, nsx_edge_v_tep_vlan_id, nsx_edge_uplink1_vlan_id, nsx_edge_uplink2_vlan_id, hcx_vlan_id, freeform_tags, defined_tags, if_match):

    if isinstance(sddc_id, six.string_types) and len(sddc_id.strip()) == 0:
        raise click.UsageError('Parameter --sddc-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if vmware_software_version is not None:
        _details['vmwareSoftwareVersion'] = vmware_software_version

    if ssh_authorized_keys is not None:
        _details['sshAuthorizedKeys'] = ssh_authorized_keys

    if vsphere_vlan_id is not None:
        _details['vsphereVlanId'] = vsphere_vlan_id

    if vmotion_vlan_id is not None:
        _details['vmotionVlanId'] = vmotion_vlan_id

    if vsan_vlan_id is not None:
        _details['vsanVlanId'] = vsan_vlan_id

    if nsx_v_tep_vlan_id is not None:
        _details['nsxVTepVlanId'] = nsx_v_tep_vlan_id

    if nsx_edge_v_tep_vlan_id is not None:
        _details['nsxEdgeVTepVlanId'] = nsx_edge_v_tep_vlan_id

    if nsx_edge_uplink1_vlan_id is not None:
        _details['nsxEdgeUplink1VlanId'] = nsx_edge_uplink1_vlan_id

    if nsx_edge_uplink2_vlan_id is not None:
        _details['nsxEdgeUplink2VlanId'] = nsx_edge_uplink2_vlan_id

    if hcx_vlan_id is not None:
        _details['hcxVlanId'] = hcx_vlan_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ocvp', 'sddc', ctx)
    result = client.update_sddc(
        sddc_id=sddc_id,
        update_sddc_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_sddc') and callable(getattr(client, 'get_sddc')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_sddc(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
