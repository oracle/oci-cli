# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import sys
import six  # noqa: F401

from services.core.src.oci_cli_virtual_network.generated import virtualnetwork_cli

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli.aliasing import CommandGroupWithAlias

cli_util.rename_command(virtualnetwork_cli, cli, virtualnetwork_cli.virtual_network_root_group, "network")

virtualnetwork_cli.virtual_network_root_group.commands.pop(virtualnetwork_cli.ip_sec_connection_device_config_group.name)
virtualnetwork_cli.virtual_network_root_group.commands.pop(virtualnetwork_cli.ip_sec_connection_device_status_group.name)
virtualnetwork_cli.virtual_network_root_group.commands.pop(virtualnetwork_cli.letter_of_authority_group.name)
virtualnetwork_cli.virtual_network_root_group.commands.pop(virtualnetwork_cli.virtual_circuit_bandwidth_shape_group.name)
virtualnetwork_cli.virtual_network_root_group.commands.pop(virtualnetwork_cli.peer_region_for_remote_peering_group.name)

virtualnetwork_cli.private_ip_group.commands.pop(virtualnetwork_cli.create_private_ip.name)
virtualnetwork_cli.private_ip_group.commands.pop(virtualnetwork_cli.update_private_ip.name)
virtualnetwork_cli.public_ip_group.commands.pop(virtualnetwork_cli.get_public_ip_by_ip_address.name)
virtualnetwork_cli.public_ip_group.commands.pop(virtualnetwork_cli.get_public_ip_by_private_ip_id.name)
virtualnetwork_cli.fast_connect_provider_service_group.commands.pop(virtualnetwork_cli.list_fast_connect_provider_virtual_circuit_bandwidth_shapes.name)

virtualnetwork_cli.get_ip_sec_connection_device_config.name = 'get-config'
virtualnetwork_cli.get_ip_sec_connection_device_status.name = 'get-status'
virtualnetwork_cli.ip_sec_connection_group.add_command(virtualnetwork_cli.get_ip_sec_connection_device_config)
virtualnetwork_cli.ip_sec_connection_group.add_command(virtualnetwork_cli.get_ip_sec_connection_device_status)
cli_util.rename_command(virtualnetwork_cli, virtualnetwork_cli.cross_connect_port_speed_shape_group, virtualnetwork_cli.list_crossconnect_port_speed_shapes, "list")

virtualnetwork_cli.virtual_network_root_group.help = "Networking Service CLI"
virtualnetwork_cli.virtual_network_root_group.short_help = "Networking Service"

cli_util.rename_command(virtualnetwork_cli, virtualnetwork_cli.virtual_network_root_group, virtualnetwork_cli.ip_sec_connection_tunnel_group, "ip-sec-tunnel")
cli_util.rename_command(virtualnetwork_cli, virtualnetwork_cli.virtual_network_root_group, virtualnetwork_cli.ip_sec_connection_tunnel_shared_secret_group, "ip-sec-psk")

cli_util.rename_command(virtualnetwork_cli, virtualnetwork_cli.virtual_network_root_group, virtualnetwork_cli.network_security_group_group, "nsg")

virtualnetwork_cli.virtual_network_root_group.commands.pop(virtualnetwork_cli.network_security_group_vnic_group.name)
virtualnetwork_cli.network_security_group_group.add_command(virtualnetwork_cli.network_security_group_vnic_group)
cli_util.rename_command(virtualnetwork_cli, virtualnetwork_cli.network_security_group_group, virtualnetwork_cli.network_security_group_vnic_group, "vnics")


virtualnetwork_cli.virtual_network_root_group.commands.pop(virtualnetwork_cli.security_rule_group.name)
virtualnetwork_cli.network_security_group_group.add_command(virtualnetwork_cli.security_rule_group)
cli_util.rename_command(virtualnetwork_cli, virtualnetwork_cli.network_security_group_group, virtualnetwork_cli.security_rule_group, "rules")

cli_util.rename_command(virtualnetwork_cli, virtualnetwork_cli.security_rule_group, virtualnetwork_cli.list_network_security_group_security_rules, "list")
cli_util.rename_command(virtualnetwork_cli, virtualnetwork_cli.security_rule_group, virtualnetwork_cli.update_network_security_group_security_rules, "update")

cli_util.rename_command(virtualnetwork_cli, virtualnetwork_cli.vcn_group, virtualnetwork_cli.add_vcn_cidr, "add-vcn-cidr")
cli_util.rename_command(virtualnetwork_cli, virtualnetwork_cli.vcn_group, virtualnetwork_cli.remove_vcn_cidr, "remove-vcn-cidr")

# help for oci network ip-sec-connection create --static-routes
network_create_ip_sec_connection_static_routes_example = """'["10.0.0.0/16"]'"""
network_create_ip_sec_connection_static_routes_help = """Static routes to the CPE. At least one route must be included. The CIDR must not be a multicast address or class E address. This must be provided in JSON format."""
cli_util.update_param_help(virtualnetwork_cli.create_ip_sec_connection, 'static_routes', network_create_ip_sec_connection_static_routes_help, append=False, example=network_create_ip_sec_connection_static_routes_example)

network_create_subnet_prohibit_public_ip_on_vnic_help = """Whether VNICs within this subnet can have public IP addresses. Defaults to false, which means VNICs created in this subnet will automatically be assigned public IP addresses unless specified otherwise during instance launch (with the `--assign-public-ip` flag). If `--prohibit-public-ip-on-vnic` is set to true, VNICs created in this subnet cannot have public IP addresses (i.e., it's a private subnet)."""
network_create_subnet_prohibit_public_ip_on_vnic_example = "`true`"
cli_util.update_param_help(virtualnetwork_cli.create_subnet, 'prohibit_public_ip_on_vnic', network_create_subnet_prohibit_public_ip_on_vnic_help, example=network_create_subnet_prohibit_public_ip_on_vnic_example)

# help for oci network subnet create --security-list-ids
security_list_example_id = 'ocid1.securitylist.oc1.phx.aaaaaaaadyndu2n3hcmdsjfiljwyq7vpxsvv7ynp4ori7aealcvhzicnzhyq'
network_create_subnet_security_list_ids_example = """'["{sl_id}"]'"""
cli_util.update_param_help(virtualnetwork_cli.create_subnet, 'security_list_ids', '', append=True, example=network_create_subnet_security_list_ids_example.format(sl_id=security_list_example_id))

# help for oci network dhcp-options create --options
network_create_dhcp_options_options_example = """'[{"type": "DomainNameServer", "customDnsServers": ["202.44.61.9"], "serverType": "CustomDnsServer"}]'"""
cli_util.update_param_help(virtualnetwork_cli.create_dhcp_options, 'options', '', append=True, example=network_create_dhcp_options_options_example)
cli_util.update_param_help(virtualnetwork_cli.update_dhcp_options, 'options', '', append=True, example=network_create_dhcp_options_options_example)

# help for oci network route-table create --route-rules
internet_gateway_example_id = 'ocid1.internetgateway.oc1.phx.aaaaaaaaxtfqb2srw7hoi5cmdum4n6ow2xm2zhrzqqypmlteiiebtmvl75ya'
network_create_route_table_route_rules_example = """'[{{"cidrBlock":"0.0.0.0/0","networkEntityId":"{ig_id}"}}]'"""
cli_util.update_param_help(virtualnetwork_cli.create_route_table, 'route_rules', '', append=True, example=network_create_route_table_route_rules_example.format(ig_id=internet_gateway_example_id))
cli_util.update_param_help(virtualnetwork_cli.update_route_table, 'route_rules', '', append=True, example=network_create_route_table_route_rules_example.format(ig_id=internet_gateway_example_id))

# help for oci network security-list create --egress-security-rules
network_create_security_list_egress_security_rules_example = """'[{"destination": "10.0.2.0/24", "protocol": "6", "isStateless": true, "tcpOptions": {"destinationPortRange": {"max": 1521, "min": 1521}, "sourcePortRange": {"max": 1521, "min": 1521}}}]'"""
cli_util.update_param_help(virtualnetwork_cli.create_security_list, 'egress_security_rules', '', append=True, example=network_create_security_list_egress_security_rules_example)
cli_util.update_param_help(virtualnetwork_cli.update_security_list, 'egress_security_rules', '', append=True, example=network_create_security_list_egress_security_rules_example)

# help for oci network security-list create --ingress-security-rules
network_create_security_list_ingress_security_rules_example = """'[{"source": "10.0.2.0/24", "protocol": "6", "isStateless": true, "tcpOptions": {"destinationPortRange": {"max": 1521, "min": 1521}, "sourcePortRange": {"max": 1521, "min": 1521}}}]'"""
cli_util.update_param_help(virtualnetwork_cli.create_security_list, 'ingress_security_rules', '', append=True, example=network_create_security_list_ingress_security_rules_example)
cli_util.update_param_help(virtualnetwork_cli.update_security_list, 'ingress_security_rules', '', append=True, example=network_create_security_list_ingress_security_rules_example)

# Formatting of the help for the bcms network private-ip list command
virtualnetwork_cli.list_private_ips.help = """Lists the [PrivateIp] objects based on one of these filters:

  \b
  - Subnet OCID.
  - VNIC OCID.
  - Both private IP address and subnet OCID: This lets you get a `privateIP` object
    based on its private IP address (for example, 10.0.3.3)  and not its OCID.
    For comparison, [GetPrivateIp] requires the OCID.

If you're listing all the private IPs associated with a given subnet or VNIC, the response includes both primary and secondary private IPs."""

# update the type of the --skip-source-dest-check switch on update_vnic to be a boolean
cli_util.get_param(virtualnetwork_cli.update_vnic, 'skip_source_dest_check').type = click.BOOL


@cli_util.copy_params_from_generated_command(virtualnetwork_cli.create_private_ip, params_to_exclude=[''])
@virtualnetwork_cli.vnic_group.command(name='assign-private-ip', help="""Assigns a secondary private IP address to the specified VNIC. The secondary private IP must be in the same subnet as the VNIC.
This command can also be used to move an existing secondary private IP to the specified VNIC.

For more information about secondary private IPs, see [IP Addresses]
""")
@cli_util.option('--unassign-if-already-assigned', is_flag=True, default=False, help="""Force reassignment of the IP address if it's already assigned to another VNIC in the subnet. This is only relevant if an IP address is associated with this command.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'PrivateIp'})
@cli_util.wrap_exceptions
def assign_private_ip(ctx, from_json, vnic_id, vlan_id, ip_address, display_name, hostname_label, unassign_if_already_assigned, defined_tags, freeform_tags):
    networking_client = cli_util.build_client('core', 'virtual_network', ctx)
    assign_private_ip_request_body = {}
    is_ip_reassignment = False

    def _pre_strip(string):
        if string is None:
            return ""
        elif isinstance(string, six.string_types):
            return string.strip()
        else:
            raise click.UsageError('Unexpected format for string  {} '.format(string))

    vlan_id = _pre_strip(vlan_id)
    vnic_id = _pre_strip(vnic_id)

    if not any((vlan_id, vnic_id)):
        raise click.UsageError(
            'Parameter --vnic-id AND --vlan-id both cannot be whitespace or empty string. '
            'You have to specify one and ONLY one of these')
    elif all((vlan_id, vnic_id)):
        raise click.UsageError(
            'Parameter --vnic-id AND --vlan-id both cannot be specified at the same time. '
            'You have to specify one and ONLY one of these')

    if vlan_id:
        if ip_address is not None:
            # Try and see whether the private IP is already in use by calling ListPrivateIps with the IP address and subnet. In this case, we don't
            # worry about pagination because we expect at most 1 entry
            list_private_ips_response = networking_client.list_private_ips(ip_address=ip_address, vlan_id=vlan_id)
            list_private_ips_response_data = list_private_ips_response.data

            if list_private_ips_response_data is not None:
                if len(list_private_ips_response_data) == 1:
                    # If the IP is already on the VNIC, make this a no-op
                    if list_private_ips_response_data[0].vlan_id == vlan_id:
                        click.echo('Taking no action as IP address {} is already assigned to VLAN {}'.format(ip_address, vlan_id), err=True)
                        return
        assign_private_ip_request_body['vlanId'] = vlan_id
    else:
        # First we get the VNIC because we need to know the subnet OCID for the ListPrivateIps call
        vnic = networking_client.get_vnic(vnic_id).data
        subnet_id = vnic.subnet_id

        if ip_address is not None:
            # Try and see whether the private IP is already in use by calling ListPrivateIps with the IP address and subnet. In this case, we don't
            # worry about pagination because we expect at most 1 entry
            list_private_ips_response = networking_client.list_private_ips(ip_address=ip_address, subnet_id=subnet_id)
            list_private_ips_response_data = list_private_ips_response.data

            if list_private_ips_response_data is not None:
                if len(list_private_ips_response_data) == 1:
                    # If the IP is already on the VNIC, make this a no-op
                    if list_private_ips_response_data[0].vnic_id == vnic_id:
                        click.echo('Taking no action as IP address {} is already assigned to VNIC {}'.format(ip_address, vnic_id), err=True)
                        return

                    # The IP address exists and it can theoretically be moved since it isn't the primary IP and it is on a separate VNIC. However,
                    # if the user did not specify the --unassign-if-already-assigned flag then we do not proceed as they haven't explicitly
                    # said they want to do the reassignment
                    if not unassign_if_already_assigned:
                        sys.exit(
                            'IP address {} is already assigned to a different VNIC: {}. To reassign it, re-run this command with the --unassign-if-already-assigned option'.format(
                                ip_address, list_private_ips_response_data[0].vnic_id
                            )
                        )

                    is_ip_reassignment = True
                elif len(list_private_ips_response_data) > 1:
                    # This would be unexpected as it means that the IP exists twice in the subnet
                    sys.exit(
                        'IP address {} appeared {} times in subnet with OCID {}. It is expected to appear at most once (Request ID: {})'.format(
                            ip_address, len(list_private_ips_response_data), subnet_id, list_private_ips_response.request_id
                        )
                    )

        assign_private_ip_request_body['vnicId'] = vnic_id
        # These are optional in the request, so check whether we should set them or not.
        if hostname_label is not None:
            assign_private_ip_request_body['hostnameLabel'] = hostname_label

    # These are optional in the request, so check whether we should set them or not.
    if display_name is not None:
        assign_private_ip_request_body['displayName'] = display_name

    if defined_tags is not None:
        assign_private_ip_request_body['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)
    if freeform_tags is not None:
        assign_private_ip_request_body['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    # If we are here then either the IP address does not exist or it is a candidate to be moved
    if not is_ip_reassignment:
        if ip_address is not None:
            assign_private_ip_request_body['ipAddress'] = ip_address

        result = networking_client.create_private_ip(assign_private_ip_request_body)
    else:
        result = networking_client.update_private_ip(list_private_ips_response_data[0].id, assign_private_ip_request_body)

    private_ip_id = result.data.id
    get_private_id_result = networking_client.get_private_ip(private_ip_id)

    cli_util.render_response(get_private_id_result, ctx)


@virtualnetwork_cli.vnic_group.command(name='unassign-private-ip', help="""Unassigns a secondary private IP address from a VNIC. After the IP address is unassigned, you
can assign to another VNIC in the subnet.

This operation cannot be used with primary private IPs, which are automatically unassigned, and then deleted when the VNIC is
terminated.

For more information about secondary private IPs, see [IP Addresses]
""")
@cli_util.option('--vnic-id', required=True, help="""The OCID of the VNIC to unassign the private IP from.""")
@cli_util.option('--ip-address', required=True, help="""The secondary private IP to unassign from the VNIC.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def unassign_private_ip(ctx, from_json, vnic_id, ip_address):
    networking_client = cli_util.build_client('core', 'virtual_network', ctx)

    list_private_ips_response = networking_client.list_private_ips(vnic_id=vnic_id)

    if list_private_ips_response.data is None:
        sys.exit('No IP addresses found for VNIC {}'.format(vnic_id))

    private_ip_addresses = list_private_ips_response.data
    next_page = list_private_ips_response.next_page
    while next_page is not None:
        list_private_ips_response = networking_client.list_private_ips(vnic_id=vnic_id, page=next_page)

        if list_private_ips_response.data is not None:
            private_ip_addresses += list_private_ips_response.data

        next_page = list_private_ips_response.next_page

    target_ip_address = None
    for private_ip in private_ip_addresses:
        if private_ip.ip_address == ip_address:
            target_ip_address = private_ip
            break

    if target_ip_address is None:
        sys.exit('IP address {} was not found on VNIC {}'.format(ip_address, vnic_id))

    if target_ip_address.is_primary:
        sys.exit('Taking no action as {} is the primary private IP on VNIC {}'.format(ip_address, vnic_id))

    networking_client.delete_private_ip(target_ip_address.id)

    # The delete result has an empty body on success so doing cli_util.render_response provides no feedback. Instead, just echo out a
    # confirmation
    click.echo('Unassigned IP address {} from VNIC {}'.format(ip_address, vnic_id), err=True)


# This method exists so that we can suppress the --vnic-id option to update_private_ip. The reason that we suppress it is because this parameter
# is used to move the private IP to another VNIC, which can be done via the assign-private-ip command with the --unassign-if-already-assigned flag
@cli_util.copy_params_from_generated_command(virtualnetwork_cli.update_private_ip, params_to_exclude=['vnic_id'])
@virtualnetwork_cli.private_ip_group.command(name='update', help="""Updates the specified private IP. You must specify the object's OCID. Use this operation if you want to:

  \b
  - Change the display name for a secondary private IP.
  - Change the hostname for a secondary private IP.

To move a secondary private IP to another VNIC, use the `bcms network vnic assign-private-ip` command with the --unassign-if-already-assigned switch.

This operation cannot be used with primary private IPs. To update the hostname for the primary IP on a VNIC, use [UpdateVnic].""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'PrivateIp'})
@cli_util.wrap_exceptions
def update_private_ip_extended(ctx, **kwargs):
    ctx.invoke(virtualnetwork_cli.update_private_ip, **kwargs)


@virtualnetwork_cli.public_ip_group.command(name='get', help="""Gets the specified public IP object.
The command needs at least one of the options to be used to be able to get the public IP object successfully.""")
@cli_util.option('--public-ip-address', help="""A public IP address. Example: 129.146.2.1""")
@cli_util.option('--public-ip-id', help="""The public IP's OCID.""")
@cli_util.option('--private-ip-id', help="""The private IP's OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PublicIp'})
@cli_util.wrap_exceptions
def get_public_ip_extended(ctx, **kwargs):
    command_args = dict([(k, v) for k, v in kwargs.items() if v is not None])
    # Remove from_json key since the parsing is done
    command_args.pop('from_json', None)
    # Check at least one of the command options is specified
    if len(command_args) == 0:
        raise click.UsageError('At least one of the options (--public-ip-id or '
                               '--public-ip-address or --private-ip-id) MUST be '
                               'specified')

    # Check ONLY one command option is specified
    if len(command_args) > 1:
        raise click.UsageError('This command accepts ONLY one option : EITHER '
                               '--public-ip-id OR --public-ip_address OR '
                               '--private-ip-id')

    func_call_dict = {
        'public_ip_id'      : virtualnetwork_cli.get_public_ip,  # noqa: E203
        'public_ip_address' : virtualnetwork_cli.get_public_ip_by_ip_address,  # noqa: E203
        'private_ip_id'     : virtualnetwork_cli.get_public_ip_by_private_ip_id  # noqa: E203
    }

    func_call_key = list(command_args.keys())[0]
    if 'public_ip_address' in command_args:
        command_args['ip_address'] = command_args.pop('public_ip_address')

    ctx.invoke(func_call_dict[func_call_key], **command_args)


@cli_util.copy_params_from_generated_command(virtualnetwork_cli.connect_remote_peering_connections, params_to_exclude=['peer_region_name'])
@virtualnetwork_cli.remote_peering_connection_group.command(name='connect', help="""Connects this RPC to another one in a different region.

This operation must be called by the VCN administrator who is designated as the *requestor* in the peering relationship. The *acceptor* must implement an Identity and Access Management (IAM) policy that gives the requestor permission to connect to RPCs in the acceptor's compartment. Without that permission, this operation will fail. For more information, see [VCN Peering].""")
# Below param is not enforced as an enum to allow backward compatibility for old CLIs to support newer regions.
@cli_util.option('--peer-region-name', required=True, help="""The name of the region that contains the RPC you want to peer with.

The region names that could be used are listed here: https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm
Example: `us-ashburn-1`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def connect_remote_peering_connections_extended(ctx, **kwargs):
    try:
        # Get the valid region list by querying IAM service
        client = cli_util.build_client('identity', 'identity', ctx)
        result = client.list_regions()
    except Exception:
        # If the IAM region list call fails, still go ahead with the remote peering connection with the user provided input
        pass
    else:
        # Check if user used the correct region name
        region_names = [elem.name for elem in result.data]
        if kwargs['peer_region_name'] not in region_names:
            click.echo('Please select one of the following Region names and reissue the command:')
            # Print region names in more legible way with each region on new line
            for elem in region_names:
                click.echo('{}'.format(elem))
            raise click.UsageError('Incorrect Peer Region Name given')
    ctx.invoke(virtualnetwork_cli.connect_remote_peering_connections, **kwargs)


# Below customization is done to add another subgroup for an API and to make the API name shorter and consistent with general
# CLI naming convention.
@virtualnetwork_cli.fast_connect_provider_service_group.command(cli_util.override('virtual_circuit_bandwidth_shape_group.command_name', 'virtual-circuit-bandwidth-shape'), cls=CommandGroupWithAlias, help="""An individual bandwidth level for virtual circuits.""")
@cli_util.help_option_group
def virtual_circuit_bandwidth_shape_group():
    pass


virtualnetwork_cli.list_fast_connect_provider_virtual_circuit_bandwidth_shapes.name = 'list'
virtual_circuit_bandwidth_shape_group.add_command(virtualnetwork_cli.list_fast_connect_provider_virtual_circuit_bandwidth_shapes)


def swap_nsg_id_value(kwargs):
    nsg_id = kwargs.pop('nsg_id')
    kwargs['network_security_group_id'] = nsg_id
    if isinstance(nsg_id, six.string_types) and len(nsg_id.strip()) == 0:
        raise click.UsageError('Parameter --nsg-id cannot be whitespace or empty string')
    return kwargs


# This command is to enable change_network_security_group_compartment command to be shortened using nsg_id
@cli_util.copy_params_from_generated_command(virtualnetwork_cli.change_network_security_group_compartment, params_to_exclude=['network_security_group_id'])
@virtualnetwork_cli.network_security_group_group.command(name=cli_util.override('change_network_security_group_compartment.command_name', 'change-compartment'), help=virtualnetwork_cli.change_network_security_group_compartment.help)
@cli_util.option('--nsg-id', required=True, help=u"""The [OCID] of the network security group.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_network_security_group_compartment_extended(ctx, **kwargs):
    if 'nsg_id' in kwargs:
        kwargs = swap_nsg_id_value(kwargs)
    ctx.invoke(virtualnetwork_cli.change_network_security_group_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(virtualnetwork_cli.delete_network_security_group, params_to_exclude=['network_security_group_id'])
@virtualnetwork_cli.network_security_group_group.command(name=cli_util.override('delete_network_security_group.command_name', 'delete'), help=virtualnetwork_cli.delete_network_security_group.help)
@cli_util.option('--nsg-id', required=True, help=u"""The [OCID] of the network security group.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_network_security_group_extended(ctx, **kwargs):
    if 'nsg_id' in kwargs:
        kwargs = swap_nsg_id_value(kwargs)
    ctx.invoke(virtualnetwork_cli.delete_network_security_group, **kwargs)


@cli_util.copy_params_from_generated_command(virtualnetwork_cli.get_network_security_group, params_to_exclude=['network_security_group_id'])
@virtualnetwork_cli.network_security_group_group.command(name=cli_util.override('get_network_security_group.command_name', 'get'), help=virtualnetwork_cli.get_network_security_group.help)
@cli_util.option('--nsg-id', required=True, help=u"""The [OCID] of the network security group.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_network_security_group_extended(ctx, **kwargs):
    if 'nsg_id' in kwargs:
        kwargs = swap_nsg_id_value(kwargs)
    ctx.invoke(virtualnetwork_cli.get_network_security_group, **kwargs)


@cli_util.copy_params_from_generated_command(virtualnetwork_cli.update_network_security_group, params_to_exclude=['network_security_group_id'])
@virtualnetwork_cli.network_security_group_group.command(name=cli_util.override('update_network_security_group.command_name', 'update'), help=virtualnetwork_cli.update_network_security_group.help)
@cli_util.option('--nsg-id', required=True, help=u"""The [OCID] of the network security group.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'NetworkSecurityGroup'})
@cli_util.wrap_exceptions
def update_network_security_group_extended(ctx, **kwargs):
    if 'nsg_id' in kwargs:
        kwargs = swap_nsg_id_value(kwargs)
    ctx.invoke(virtualnetwork_cli.update_network_security_group, **kwargs)


@cli_util.copy_params_from_generated_command(virtualnetwork_cli.list_network_security_group_vnics, params_to_exclude=['network_security_group_id'])
@virtualnetwork_cli.network_security_group_vnic_group.command(name=cli_util.override('list_network_security_group_vnics.command_name', 'list'), help=virtualnetwork_cli.list_network_security_group_vnics.help)
@cli_util.option('--nsg-id', required=True, help=u"""The [OCID] of the network security group.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def list_network_security_group_vnics_extended(ctx, **kwargs):
    if 'nsg_id' in kwargs:
        kwargs = swap_nsg_id_value(kwargs)
    ctx.invoke(virtualnetwork_cli.list_network_security_group_vnics, **kwargs)


@cli_util.copy_params_from_generated_command(virtualnetwork_cli.add_network_security_group_security_rules, params_to_exclude=['network_security_group_id'])
@virtualnetwork_cli.security_rule_group.command(name=cli_util.override('add_network_security_group_security_rules.command_name', 'add'), help=virtualnetwork_cli.add_network_security_group_security_rules.help)
@cli_util.option('--nsg-id', required=True, help=u"""The [OCID] of the network security group.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'security-rules': {'module': 'core', 'class': 'list[AddSecurityRuleDetails]'}})
@cli_util.wrap_exceptions
def add_network_security_group_security_rules_extended(ctx, **kwargs):
    if 'nsg_id' in kwargs:
        kwargs = swap_nsg_id_value(kwargs)
    ctx.invoke(virtualnetwork_cli.add_network_security_group_security_rules, **kwargs)


@cli_util.copy_params_from_generated_command(virtualnetwork_cli.list_network_security_group_security_rules, params_to_exclude=['network_security_group_id'])
@virtualnetwork_cli.security_rule_group.command(name=cli_util.override('list_network_security_group_security_rules.command_name', 'list'), help=virtualnetwork_cli.list_network_security_group_security_rules.help)
@cli_util.option('--nsg-id', required=True, help=u"""The [OCID] of the network security group.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def list_network_security_group_security_rules_extended(ctx, **kwargs):
    if 'nsg_id' in kwargs:
        kwargs = swap_nsg_id_value(kwargs)
    ctx.invoke(virtualnetwork_cli.list_network_security_group_security_rules, **kwargs)


@cli_util.copy_params_from_generated_command(virtualnetwork_cli.remove_network_security_group_security_rules, params_to_exclude=['network_security_group_id'])
@virtualnetwork_cli.security_rule_group.command(name=cli_util.override('remove_network_security_group_security_rules.command_name', 'remove'), help=virtualnetwork_cli.remove_network_security_group_security_rules.help)
@cli_util.option('--nsg-id', required=True, help=u"""The [OCID] of the network security group.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'security-rule-ids': {'module': 'core', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def remove_network_security_group_security_rules_extended(ctx, **kwargs):
    if 'nsg_id' in kwargs:
        kwargs = swap_nsg_id_value(kwargs)
    ctx.invoke(virtualnetwork_cli.remove_network_security_group_security_rules, **kwargs)


@cli_util.copy_params_from_generated_command(virtualnetwork_cli.update_network_security_group_security_rules, params_to_exclude=['network_security_group_id'])
@virtualnetwork_cli.security_rule_group.command(name=cli_util.override('update_network_security_group_security_rules.command_name', 'update'), help=virtualnetwork_cli.update_network_security_group_security_rules.help)
@cli_util.option('--nsg-id', required=True, help=u"""The [OCID] of the network security group.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'security-rules': {'module': 'core', 'class': 'list[UpdateSecurityRuleDetails]'}})
@cli_util.wrap_exceptions
def update_network_security_group_security_rules_extended(ctx, **kwargs):
    if 'nsg_id' in kwargs:
        kwargs = swap_nsg_id_value(kwargs)
    ctx.invoke(virtualnetwork_cli.update_network_security_group_security_rules, **kwargs)


@cli_util.copy_params_from_generated_command(virtualnetwork_cli.create_virtual_circuit, params_to_exclude=['region_parameterconflict'])
@virtualnetwork_cli.virtual_circuit_group.command(name=cli_util.override('create_virtual_circuit.command_name', 'create'), help=virtualnetwork_cli.create_virtual_circuit.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'cross-connect-mappings': {'module': 'core', 'class': 'list[CrossConnectMapping]'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'public-prefixes': {'module': 'core', 'class': 'list[CreateVirtualCircuitPublicPrefixDetails]'}}, output_type={'module': 'core', 'class': 'VirtualCircuit'})
@cli_util.wrap_exceptions
def create_virtual_circuit_extended(ctx, **kwargs):
    ctx.invoke(virtualnetwork_cli.create_virtual_circuit, **kwargs)
