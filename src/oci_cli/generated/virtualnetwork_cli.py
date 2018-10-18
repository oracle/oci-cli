# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from ..cli_root import cli
from .. import cli_constants  # noqa: F401
from .. import cli_util
from .. import json_skeleton_utils
from .. import custom_types  # noqa: F401
from ..aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('virtual_network_root_group.command_name', 'virtual-network'), cls=CommandGroupWithAlias, help=cli_util.override('virtual_network_root_group.help', """APIs for Networking Service, Compute Service, and Block Volume Service."""), short_help=cli_util.override('virtual_network_root_group.short_help', """Core Services API"""))
@cli_util.help_option_group
def virtual_network_root_group():
    pass


@click.command(cli_util.override('remote_peering_connection_group.command_name', 'remote-peering-connection'), cls=CommandGroupWithAlias, help="""A remote peering connection (RPC) is an object on a DRG that lets the VCN that is attached to the DRG peer with a VCN in a different region. *Peering* means that the two VCNs can communicate using private IP addresses, but without the traffic traversing the internet or routing through your on-premises network. For more information, see [VCN Peering].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def remote_peering_connection_group():
    pass


@click.command(cli_util.override('subnet_group.command_name', 'subnet'), cls=CommandGroupWithAlias, help="""A logical subdivision of a VCN. Each subnet exists in a single availability domain and consists of a contiguous range of IP addresses that do not overlap with other subnets in the VCN. Example: 172.16.1.0/24. For more information, see [Overview of the Networking Service] and [VCNs and Subnets].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def subnet_group():
    pass


@click.command(cli_util.override('nat_gateway_group.command_name', 'nat-gateway'), cls=CommandGroupWithAlias, help="""A NAT (Network Address Translation) gateway, which represents a router that lets instances without public IPs contact the public internet without exposing the instance to inbound internet traffic. For more information, see [NAT Gateway].

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def nat_gateway_group():
    pass


@click.command(cli_util.override('drg_attachment_group.command_name', 'drg-attachment'), cls=CommandGroupWithAlias, help="""A link between a DRG and VCN. For more information, see [Overview of the Networking Service].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def drg_attachment_group():
    pass


@click.command(cli_util.override('public_ip_group.command_name', 'public-ip'), cls=CommandGroupWithAlias, help="""A *public IP* is a conceptual term that refers to a public IP address and related properties. The `publicIp` object is the API representation of a public IP.

There are two types of public IPs: 1. Ephemeral 2. Reserved

For more information and comparison of the two types, see [Public IP Addresses].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def public_ip_group():
    pass


@click.command(cli_util.override('ip_sec_connection_device_config_group.command_name', 'ip-sec-connection-device-config'), cls=CommandGroupWithAlias, help="""Information about the IPSecConnection device configuration.""")
@cli_util.help_option_group
def ip_sec_connection_device_config_group():
    pass


@click.command(cli_util.override('fast_connect_provider_service_group.command_name', 'fast-connect-provider-service'), cls=CommandGroupWithAlias, help="""A service offering from a supported provider. For more information, see [FastConnect Overview].""")
@cli_util.help_option_group
def fast_connect_provider_service_group():
    pass


@click.command(cli_util.override('cross_connect_location_group.command_name', 'cross-connect-location'), cls=CommandGroupWithAlias, help="""An individual FastConnect location.""")
@cli_util.help_option_group
def cross_connect_location_group():
    pass


@click.command(cli_util.override('virtual_circuit_public_prefix_group.command_name', 'virtual-circuit-public-prefix'), cls=CommandGroupWithAlias, help="""A public IP prefix and its details. With a public virtual circuit, the customer specifies the customer-owned public IP prefixes to advertise across the connection. For more information, see [FastConnect Overview].""")
@cli_util.help_option_group
def virtual_circuit_public_prefix_group():
    pass


@click.command(cli_util.override('private_ip_group.command_name', 'private-ip'), cls=CommandGroupWithAlias, help="""A *private IP* is a conceptual term that refers to a private IP address and related properties. The `privateIp` object is the API representation of a private IP.

Each instance has a *primary private IP* that is automatically created and assigned to the primary VNIC during instance launch. If you add a secondary VNIC to the instance, it also automatically gets a primary private IP. You can't remove a primary private IP from its VNIC. The primary private IP is automatically deleted when the VNIC is terminated.

You can add *secondary private IPs* to a VNIC after it's created. For more information, see the `privateIp` operations and also [IP Addresses].

**Note:** Only [ListPrivateIps] and [GetPrivateIp] work with *primary* private IPs. To create and update primary private IPs, you instead work with instance and VNIC operations. For example, a primary private IP's properties come from the values you specify in [CreateVnicDetails] when calling either [LaunchInstance] or [AttachVnic]. To update the hostname for a primary private IP, you use [UpdateVnic].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def private_ip_group():
    pass


@click.command(cli_util.override('virtual_circuit_group.command_name', 'virtual-circuit'), cls=CommandGroupWithAlias, help="""For use with Oracle Cloud Infrastructure FastConnect.

A virtual circuit is an isolated network path that runs over one or more physical network connections to provide a single, logical connection between the edge router on the customer's existing network and Oracle Cloud Infrastructure. *Private* virtual circuits support private peering, and *public* virtual circuits support public peering. For more information, see [FastConnect Overview].

Each virtual circuit is made up of information shared between a customer, Oracle, and a provider (if the customer is using FastConnect via a provider). Who fills in a given property of a virtual circuit depends on whether the BGP session related to that virtual circuit goes from the customer's edge router to Oracle, or from the provider's edge router to Oracle. Also, in the case where the customer is using a provider, values for some of the properties may not be present immediately, but may get filled in as the provider and Oracle each do their part to provision the virtual circuit.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def virtual_circuit_group():
    pass


@click.command(cli_util.override('local_peering_gateway_group.command_name', 'local-peering-gateway'), cls=CommandGroupWithAlias, help="""A local peering gateway (LPG) is an object on a VCN that lets that VCN peer with another VCN in the same region. *Peering* means that the two VCNs can communicate using private IP addresses, but without the traffic traversing the internet or routing through your on-premises network. For more information, see [VCN Peering].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def local_peering_gateway_group():
    pass


@click.command(cli_util.override('cross_connect_port_speed_shape_group.command_name', 'cross-connect-port-speed-shape'), cls=CommandGroupWithAlias, help="""An individual port speed level for cross-connects.""")
@cli_util.help_option_group
def cross_connect_port_speed_shape_group():
    pass


@click.command(cli_util.override('drg_group.command_name', 'drg'), cls=CommandGroupWithAlias, help="""A dynamic routing gateway (DRG), which is a virtual router that provides a path for private network traffic between your VCN and your existing network. You use it with other Networking Service components to create an IPSec VPN or a connection that uses Oracle Cloud Infrastructure FastConnect. For more information, see [Overview of the Networking Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def drg_group():
    pass


@click.command(cli_util.override('route_table_group.command_name', 'route-table'), cls=CommandGroupWithAlias, help="""A collection of `RouteRule` objects, which are used to route packets based on destination IP to a particular network entity. For more information, see [Overview of the Networking Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def route_table_group():
    pass


@click.command(cli_util.override('cpe_group.command_name', 'cpe'), cls=CommandGroupWithAlias, help="""An object you create when setting up an IPSec VPN between your on-premises network and VCN. The `Cpe` is a virtual representation of your customer-premises equipment, which is the actual router on-premises at your site at your end of the IPSec VPN connection. For more information, see [Overview of the Networking Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def cpe_group():
    pass


@click.command(cli_util.override('cross_connect_group.command_name', 'cross-connect'), cls=CommandGroupWithAlias, help="""For use with Oracle Cloud Infrastructure FastConnect. A cross-connect represents a physical connection between an existing network and Oracle. Customers who are colocated with Oracle in a FastConnect location create and use cross-connects. For more information, see [FastConnect Overview].

Oracle recommends you create each cross-connect in a [CrossConnectGroup] so you can use link aggregation with the connection.

**Note:** If you're a provider who is setting up a physical connection to Oracle so customers can use FastConnect over the connection, be aware that your connection is modeled the same way as a colocated customer's (with `CrossConnect` and `CrossConnectGroup` objects, and so on).

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def cross_connect_group():
    pass


@click.command(cli_util.override('letter_of_authority_group.command_name', 'letter-of-authority'), cls=CommandGroupWithAlias, help="""The Letter of Authority for the cross-connect. You must submit this letter when requesting cabling for the cross-connect at the FastConnect location.""")
@cli_util.help_option_group
def letter_of_authority_group():
    pass


@click.command(cli_util.override('cross_connect_status_group.command_name', 'cross-connect-status'), cls=CommandGroupWithAlias, help="""The status of the cross-connect.""")
@cli_util.help_option_group
def cross_connect_status_group():
    pass


@click.command(cli_util.override('vcn_group.command_name', 'vcn'), cls=CommandGroupWithAlias, help="""A virtual cloud network (VCN). For more information, see [Overview of the Networking Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def vcn_group():
    pass


@click.command(cli_util.override('ip_sec_connection_device_status_group.command_name', 'ip-sec-connection-device-status'), cls=CommandGroupWithAlias, help="""Status of the IPSec connection.""")
@cli_util.help_option_group
def ip_sec_connection_device_status_group():
    pass


@click.command(cli_util.override('vnic_group.command_name', 'vnic'), cls=CommandGroupWithAlias, help="""A virtual network interface card. Each VNIC resides in a subnet in a VCN. An instance attaches to a VNIC to obtain a network connection into the VCN through that subnet. Each instance has a *primary VNIC* that is automatically created and attached during launch. You can add *secondary VNICs* to an instance after it's launched. For more information, see [Virtual Network Interface Cards (VNICs)].

Each VNIC has a *primary private IP* that is automatically assigned during launch. You can add *secondary private IPs* to a VNIC after it's created. For more information, see [CreatePrivateIp] and [IP Addresses].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def vnic_group():
    pass


@click.command(cli_util.override('dhcp_options_group.command_name', 'dhcp-options'), cls=CommandGroupWithAlias, help="""A set of DHCP options. Used by the VCN to automatically provide configuration information to the instances when they boot up. There are two options you can set:

- [DhcpDnsOption]: Lets you specify how DNS (hostname resolution) is handled in the subnets in your VCN.

- [DhcpSearchDomainOption]: Lets you specify a search domain name to use for DNS queries.

For more information, see  [DNS in Your Virtual Cloud Network] and [DHCP Options].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def dhcp_options_group():
    pass


@click.command(cli_util.override('virtual_circuit_bandwidth_shape_group.command_name', 'virtual-circuit-bandwidth-shape'), cls=CommandGroupWithAlias, help="""An individual bandwidth level for virtual circuits.""")
@cli_util.help_option_group
def virtual_circuit_bandwidth_shape_group():
    pass


@click.command(cli_util.override('peer_region_for_remote_peering_group.command_name', 'peer-region-for-remote-peering'), cls=CommandGroupWithAlias, help="""Details about a region that supports remote VCN peering. For more information, see [VCN Peering].""")
@cli_util.help_option_group
def peer_region_for_remote_peering_group():
    pass


@click.command(cli_util.override('service_gateway_group.command_name', 'service-gateway'), cls=CommandGroupWithAlias, help="""Represents a router that connects the edge of a VCN with public Oracle Cloud Infrastructure services such as Object Storage. Traffic leaving the VCN and destined for a supported public service (see [ListServices]) is routed through the service gateway and does not traverse the internet. The instances in the VCN do not need to have public IP addresses nor be in a public subnet. The VCN does not need an internet gateway for this traffic. For more information, see [Access to Object Storage: Service Gateway].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def service_gateway_group():
    pass


@click.command(cli_util.override('internet_gateway_group.command_name', 'internet-gateway'), cls=CommandGroupWithAlias, help="""Represents a router that connects the edge of a VCN with the Internet. For an example scenario that uses an internet gateway, see [Typical Networking Service Scenarios].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def internet_gateway_group():
    pass


@click.command(cli_util.override('ip_sec_connection_group.command_name', 'ip-sec-connection'), cls=CommandGroupWithAlias, help="""A connection between a DRG and CPE. This connection consists of multiple IPSec tunnels. Creating this connection is one of the steps required when setting up an IPSec VPN. For more information, see [Overview of the Networking Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def ip_sec_connection_group():
    pass


@click.command(cli_util.override('service_group.command_name', 'service'), cls=CommandGroupWithAlias, help="""Information about a service that is accessible through a service gateway.""")
@cli_util.help_option_group
def service_group():
    pass


@click.command(cli_util.override('cross_connect_group_group.command_name', 'cross-connect-group'), cls=CommandGroupWithAlias, help="""For use with Oracle Cloud Infrastructure FastConnect. A cross-connect group is a link aggregation group (LAG), which can contain one or more [CrossConnects]. Customers who are colocated with Oracle in a FastConnect location create and use cross-connect groups. For more information, see [FastConnect Overview].

**Note:** If you're a provider who is setting up a physical connection to Oracle so customers can use FastConnect over the connection, be aware that your connection is modeled the same way as a colocated customer's (with `CrossConnect` and `CrossConnectGroup` objects, and so on).

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def cross_connect_group_group():
    pass


@click.command(cli_util.override('security_list_group.command_name', 'security-list'), cls=CommandGroupWithAlias, help="""A set of virtual firewall rules for your VCN. Security lists are configured at the subnet level, but the rules are applied to the ingress and egress traffic for the individual instances in the subnet. The rules can be stateful or stateless. For more information, see [Security Lists].

**Important:** Oracle Cloud Infrastructure Compute service images automatically include firewall rules (for example, Linux iptables, Windows firewall). If there are issues with some type of access to an instance, make sure both the security lists associated with the instance's subnet and the instance's firewall rules are set correctly.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def security_list_group():
    pass


virtual_network_root_group.add_command(remote_peering_connection_group)
virtual_network_root_group.add_command(subnet_group)
virtual_network_root_group.add_command(nat_gateway_group)
virtual_network_root_group.add_command(drg_attachment_group)
virtual_network_root_group.add_command(public_ip_group)
virtual_network_root_group.add_command(ip_sec_connection_device_config_group)
virtual_network_root_group.add_command(fast_connect_provider_service_group)
virtual_network_root_group.add_command(cross_connect_location_group)
virtual_network_root_group.add_command(virtual_circuit_public_prefix_group)
virtual_network_root_group.add_command(private_ip_group)
virtual_network_root_group.add_command(virtual_circuit_group)
virtual_network_root_group.add_command(local_peering_gateway_group)
virtual_network_root_group.add_command(cross_connect_port_speed_shape_group)
virtual_network_root_group.add_command(drg_group)
virtual_network_root_group.add_command(route_table_group)
virtual_network_root_group.add_command(cpe_group)
virtual_network_root_group.add_command(cross_connect_group)
virtual_network_root_group.add_command(letter_of_authority_group)
virtual_network_root_group.add_command(cross_connect_status_group)
virtual_network_root_group.add_command(vcn_group)
virtual_network_root_group.add_command(ip_sec_connection_device_status_group)
virtual_network_root_group.add_command(vnic_group)
virtual_network_root_group.add_command(dhcp_options_group)
virtual_network_root_group.add_command(virtual_circuit_bandwidth_shape_group)
virtual_network_root_group.add_command(peer_region_for_remote_peering_group)
virtual_network_root_group.add_command(service_gateway_group)
virtual_network_root_group.add_command(internet_gateway_group)
virtual_network_root_group.add_command(ip_sec_connection_group)
virtual_network_root_group.add_command(service_group)
virtual_network_root_group.add_command(cross_connect_group_group)
virtual_network_root_group.add_command(security_list_group)


@service_gateway_group.command(name=cli_util.override('attach_service_id.command_name', 'attach'), help="""Enables the specified service on the specified gateway. In other words, enables the service gateway to send traffic to the specified service. You must also set up a route rule with the service's `cidrBlock` as the rule's destination CIDR and the gateway as the rule's target. See [Route Table].

**Note:** The `AttachServiceId` operation is an easy way to enable an individual service on the service gateway. Compare it with [UpdateServiceGateway], which also lets you enable an individual service. However, with `UpdateServiceGateway`, you must specify the *entire* list of services you want enabled on the service gateway.""")
@cli_util.option('--service-gateway-id', required=True, help="""The service gateway's [OCID].""")
@cli_util.option('--service-id', required=True, help="""The [OCID] of the service.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ServiceGateway'})
@cli_util.wrap_exceptions
def attach_service_id(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, service_gateway_id, service_id, if_match):

    if isinstance(service_gateway_id, six.string_types) and len(service_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --service-gateway-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['serviceId'] = service_id

    client = cli_util.build_client('virtual_network', ctx)
    result = client.attach_service_id(
        service_gateway_id=service_gateway_id,
        attach_service_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_service_gateway') and callable(getattr(client, 'get_service_gateway')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_service_gateway(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_circuit_public_prefix_group.command(name=cli_util.override('bulk_add_virtual_circuit_public_prefixes.command_name', 'bulk-add'), help="""Adds one or more customer public IP prefixes to the specified public virtual circuit. Use this operation (and not [UpdateVirtualCircuit]) to add prefixes to the virtual circuit. Oracle must verify the customer's ownership of each prefix before traffic for that prefix will flow across the virtual circuit.""")
@cli_util.option('--virtual-circuit-id', required=True, help="""The OCID of the virtual circuit.""")
@cli_util.option('--public-prefixes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""The public IP prefixes (CIDRs) to add to the public virtual circuit.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'public-prefixes': {'module': 'core', 'class': 'list[CreateVirtualCircuitPublicPrefixDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'public-prefixes': {'module': 'core', 'class': 'list[CreateVirtualCircuitPublicPrefixDetails]'}})
@cli_util.wrap_exceptions
def bulk_add_virtual_circuit_public_prefixes(ctx, from_json, virtual_circuit_id, public_prefixes):

    if isinstance(virtual_circuit_id, six.string_types) and len(virtual_circuit_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-circuit-id cannot be whitespace or empty string')
    kwargs = {}

    details = {}
    details['publicPrefixes'] = cli_util.parse_json_parameter("public_prefixes", public_prefixes)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.bulk_add_virtual_circuit_public_prefixes(
        virtual_circuit_id=virtual_circuit_id,
        bulk_add_virtual_circuit_public_prefixes_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@virtual_circuit_public_prefix_group.command(name=cli_util.override('bulk_delete_virtual_circuit_public_prefixes.command_name', 'bulk-delete'), help="""Removes one or more customer public IP prefixes from the specified public virtual circuit. Use this operation (and not [UpdateVirtualCircuit]) to remove prefixes from the virtual circuit. When the virtual circuit's state switches back to PROVISIONED, Oracle stops advertising the specified prefixes across the connection.""")
@cli_util.option('--virtual-circuit-id', required=True, help="""The OCID of the virtual circuit.""")
@cli_util.option('--public-prefixes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""The public IP prefixes (CIDRs) to remove from the public virtual circuit.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'public-prefixes': {'module': 'core', 'class': 'list[DeleteVirtualCircuitPublicPrefixDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'public-prefixes': {'module': 'core', 'class': 'list[DeleteVirtualCircuitPublicPrefixDetails]'}})
@cli_util.wrap_exceptions
def bulk_delete_virtual_circuit_public_prefixes(ctx, from_json, virtual_circuit_id, public_prefixes):

    if isinstance(virtual_circuit_id, six.string_types) and len(virtual_circuit_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-circuit-id cannot be whitespace or empty string')
    kwargs = {}

    details = {}
    details['publicPrefixes'] = cli_util.parse_json_parameter("public_prefixes", public_prefixes)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.bulk_delete_virtual_circuit_public_prefixes(
        virtual_circuit_id=virtual_circuit_id,
        bulk_delete_virtual_circuit_public_prefixes_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@local_peering_gateway_group.command(name=cli_util.override('connect_local_peering_gateways.command_name', 'connect'), help="""Connects this local peering gateway (LPG) to another one in the same region.

This operation must be called by the VCN administrator who is designated as the *requestor* in the peering relationship. The *acceptor* must implement an Identity and Access Management (IAM) policy that gives the requestor permission to connect to LPGs in the acceptor's compartment. Without that permission, this operation will fail. For more information, see [VCN Peering].""")
@cli_util.option('--local-peering-gateway-id', required=True, help="""The OCID of the local peering gateway.""")
@cli_util.option('--peer-id', required=True, help="""The OCID of the LPG you want to peer with.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def connect_local_peering_gateways(ctx, from_json, local_peering_gateway_id, peer_id):

    if isinstance(local_peering_gateway_id, six.string_types) and len(local_peering_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --local-peering-gateway-id cannot be whitespace or empty string')
    kwargs = {}

    details = {}
    details['peerId'] = peer_id

    client = cli_util.build_client('virtual_network', ctx)
    result = client.connect_local_peering_gateways(
        local_peering_gateway_id=local_peering_gateway_id,
        connect_local_peering_gateways_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@remote_peering_connection_group.command(name=cli_util.override('connect_remote_peering_connections.command_name', 'connect'), help="""Connects this RPC to another one in a different region.

This operation must be called by the VCN administrator who is designated as the *requestor* in the peering relationship. The *acceptor* must implement an Identity and Access Management (IAM) policy that gives the requestor permission to connect to RPCs in the acceptor's compartment. Without that permission, this operation will fail. For more information, see [VCN Peering].""")
@cli_util.option('--remote-peering-connection-id', required=True, help="""The OCID of the remote peering connection (RPC).""")
@cli_util.option('--peer-id', required=True, help="""The OCID of the RPC you want to peer with.""")
@cli_util.option('--peer-region-name', required=True, help="""The name of the region that contains the RPC you want to peer with.

Example: `us-ashburn-1`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def connect_remote_peering_connections(ctx, from_json, remote_peering_connection_id, peer_id, peer_region_name):

    if isinstance(remote_peering_connection_id, six.string_types) and len(remote_peering_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --remote-peering-connection-id cannot be whitespace or empty string')
    kwargs = {}

    details = {}
    details['peerId'] = peer_id
    details['peerRegionName'] = peer_region_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.connect_remote_peering_connections(
        remote_peering_connection_id=remote_peering_connection_id,
        connect_remote_peering_connections_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cpe_group.command(name=cli_util.override('create_cpe.command_name', 'create'), help="""Creates a new virtual customer-premises equipment (CPE) object in the specified compartment. For more information, see [IPSec VPNs].

For the purposes of access control, you must provide the OCID of the compartment where you want the CPE to reside. Notice that the CPE doesn't have to be in the same compartment as the IPSec connection or other Networking Service components. If you're not sure which compartment to use, put the CPE in the same compartment as the DRG. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You must provide the public IP address of your on-premises router. See [Configuring Your On-Premises Router for an IPSec VPN].

You may optionally specify a *display name* for the CPE, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the CPE.""")
@cli_util.option('--ip-address', required=True, help="""The public IP address of the on-premises router.

Example: `143.19.23.16`""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Cpe'})
@cli_util.wrap_exceptions
def create_cpe(ctx, from_json, compartment_id, ip_address, defined_tags, display_name, freeform_tags):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['ipAddress'] = ip_address

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_cpe(
        create_cpe_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cross_connect_group.command(name=cli_util.override('create_cross_connect.command_name', 'create'), help="""Creates a new cross-connect. Oracle recommends you create each cross-connect in a [CrossConnectGroup] so you can use link aggregation with the connection.

After creating the `CrossConnect` object, you need to go the FastConnect location and request to have the physical cable installed. For more information, see [FastConnect Overview].

For the purposes of access control, you must provide the OCID of the compartment where you want the cross-connect to reside. If you're not sure which compartment to use, put the cross-connect in the same compartment with your VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the cross-connect. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the cross-connect.""")
@cli_util.option('--location-name', required=True, help="""The name of the FastConnect location where this cross-connect will be installed. To get a list of the available locations, see [ListCrossConnectLocations].

Example: `CyrusOne, Chandler, AZ`""")
@cli_util.option('--port-speed-shape-name', required=True, help="""The port speed for this cross-connect. To get a list of the available port speeds, see [ListCrossConnectPortSpeedShapes].

Example: `10 Gbps`""")
@cli_util.option('--cross-connect-group-id', help="""The OCID of the cross-connect group to put this cross-connect in.""")
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--far-cross-connect-or-cross-connect-group-id', help="""If you already have an existing cross-connect or cross-connect group at this FastConnect location, and you want this new cross-connect to be on a different router (for the purposes of redundancy), provide the OCID of that existing cross-connect or cross-connect group.""")
@cli_util.option('--near-cross-connect-or-cross-connect-group-id', help="""If you already have an existing cross-connect or cross-connect group at this FastConnect location, and you want this new cross-connect to be on the same router, provide the OCID of that existing cross-connect or cross-connect group.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'CrossConnect'})
@cli_util.wrap_exceptions
def create_cross_connect(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, location_name, port_speed_shape_name, cross_connect_group_id, display_name, far_cross_connect_or_cross_connect_group_id, near_cross_connect_or_cross_connect_group_id):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['locationName'] = location_name
    details['portSpeedShapeName'] = port_speed_shape_name

    if cross_connect_group_id is not None:
        details['crossConnectGroupId'] = cross_connect_group_id

    if display_name is not None:
        details['displayName'] = display_name

    if far_cross_connect_or_cross_connect_group_id is not None:
        details['farCrossConnectOrCrossConnectGroupId'] = far_cross_connect_or_cross_connect_group_id

    if near_cross_connect_or_cross_connect_group_id is not None:
        details['nearCrossConnectOrCrossConnectGroupId'] = near_cross_connect_or_cross_connect_group_id

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_cross_connect(
        create_cross_connect_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_cross_connect') and callable(getattr(client, 'get_cross_connect')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_cross_connect(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cross_connect_group_group.command(name=cli_util.override('create_cross_connect_group.command_name', 'create'), help="""Creates a new cross-connect group to use with Oracle Cloud Infrastructure FastConnect. For more information, see [FastConnect Overview].

For the purposes of access control, you must provide the OCID of the compartment where you want the cross-connect group to reside. If you're not sure which compartment to use, put the cross-connect group in the same compartment with your VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the cross-connect group. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the cross-connect group.""")
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'CrossConnectGroup'})
@cli_util.wrap_exceptions
def create_cross_connect_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_cross_connect_group(
        create_cross_connect_group_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_cross_connect_group') and callable(getattr(client, 'get_cross_connect_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_cross_connect_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dhcp_options_group.command(name=cli_util.override('create_dhcp_options.command_name', 'create'), help="""Creates a new set of DHCP options for the specified VCN. For more information, see [DhcpOptions].

For the purposes of access control, you must provide the OCID of the compartment where you want the set of DHCP options to reside. Notice that the set of options doesn't have to be in the same compartment as the VCN, subnets, or other Networking Service components. If you're not sure which compartment to use, put the set of DHCP options in the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the set of DHCP options, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the set of DHCP options.""")
@cli_util.option('--options', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""A set of DHCP options.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN the set of DHCP options belongs to.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'options': {'module': 'core', 'class': 'list[DhcpOption]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'options': {'module': 'core', 'class': 'list[DhcpOption]'}}, output_type={'module': 'core', 'class': 'DhcpOptions'})
@cli_util.wrap_exceptions
def create_dhcp_options(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, options, vcn_id, defined_tags, display_name, freeform_tags):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['options'] = cli_util.parse_json_parameter("options", options)
    details['vcnId'] = vcn_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_dhcp_options(
        create_dhcp_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_dhcp_options') and callable(getattr(client, 'get_dhcp_options')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_dhcp_options(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@drg_group.command(name=cli_util.override('create_drg.command_name', 'create'), help="""Creates a new dynamic routing gateway (DRG) in the specified compartment. For more information, see [Dynamic Routing Gateways (DRGs)].

For the purposes of access control, you must provide the OCID of the compartment where you want the DRG to reside. Notice that the DRG doesn't have to be in the same compartment as the VCN, the DRG attachment, or other Networking Service components. If you're not sure which compartment to use, put the DRG in the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the DRG, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the DRG.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Drg'})
@cli_util.wrap_exceptions
def create_drg(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, defined_tags, display_name, freeform_tags):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_drg(
        create_drg_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_drg') and callable(getattr(client, 'get_drg')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_drg(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@drg_attachment_group.command(name=cli_util.override('create_drg_attachment.command_name', 'create'), help="""Attaches the specified DRG to the specified VCN. A VCN can be attached to only one DRG at a time, and vice versa. The response includes a `DrgAttachment` object with its own OCID. For more information about DRGs, see [Dynamic Routing Gateways (DRGs)].

You may optionally specify a *display name* for the attachment, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

For the purposes of access control, the DRG attachment is automatically placed into the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service].""")
@cli_util.option('--drg-id', required=True, help="""The OCID of the DRG.""")
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique. Avoid entering confidential information.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'DrgAttachment'})
@cli_util.wrap_exceptions
def create_drg_attachment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_id, vcn_id, display_name):
    kwargs = {}

    details = {}
    details['drgId'] = drg_id
    details['vcnId'] = vcn_id

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_drg_attachment(
        create_drg_attachment_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_drg_attachment') and callable(getattr(client, 'get_drg_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_drg_attachment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@internet_gateway_group.command(name=cli_util.override('create_internet_gateway.command_name', 'create'), help="""Creates a new internet gateway for the specified VCN. For more information, see [Access to the Internet].

For the purposes of access control, you must provide the OCID of the compartment where you want the Internet Gateway to reside. Notice that the internet gateway doesn't have to be in the same compartment as the VCN or other Networking Service components. If you're not sure which compartment to use, put the Internet Gateway in the same compartment with the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the internet gateway, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

For traffic to flow between a subnet and an internet gateway, you must create a route rule accordingly in the subnet's route table (for example, 0.0.0.0/0 > internet gateway). See [UpdateRouteTable].

You must specify whether the internet gateway is enabled when you create it. If it's disabled, that means no traffic will flow to/from the internet even if there's a route rule that enables that traffic. You can later use [UpdateInternetGateway] to easily disable/enable the gateway without changing the route rule.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the internet gateway.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help="""Whether the gateway is enabled upon creation.""")
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN the internet gateway is attached to.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'InternetGateway'})
@cli_util.wrap_exceptions
def create_internet_gateway(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, is_enabled, vcn_id, defined_tags, display_name, freeform_tags):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['isEnabled'] = is_enabled
    details['vcnId'] = vcn_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_internet_gateway(
        create_internet_gateway_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_internet_gateway') and callable(getattr(client, 'get_internet_gateway')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_internet_gateway(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@ip_sec_connection_group.command(name=cli_util.override('create_ip_sec_connection.command_name', 'create'), help="""Creates a new IPSec connection between the specified DRG and CPE. For more information, see [IPSec VPNs].

In the request, you must include at least one static route to the CPE object (you're allowed a maximum of 10). For example: 10.0.8.0/16.

For the purposes of access control, you must provide the OCID of the compartment where you want the IPSec connection to reside. Notice that the IPSec connection doesn't have to be in the same compartment as the DRG, CPE, or other Networking Service components. If you're not sure which compartment to use, put the IPSec connection in the same compartment as the DRG. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the IPSec connection, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

After creating the IPSec connection, you need to configure your on-premises router with tunnel-specific information returned by [GetIPSecConnectionDeviceConfig]. For each tunnel, that operation gives you the IP address of Oracle's VPN headend and the shared secret (that is, the pre-shared key). For more information, see [Configuring Your On-Premises Router for an IPSec VPN].

To get the status of the tunnels (whether they're up or down), use [GetIPSecConnectionDeviceStatus].""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the IPSec connection.""")
@cli_util.option('--cpe-id', required=True, help="""The OCID of the CPE.""")
@cli_util.option('--drg-id', required=True, help="""The OCID of the DRG.""")
@cli_util.option('--static-routes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""Static routes to the CPE. At least one route must be included. The CIDR must not be a multicast address or class E address.

Example: `10.0.1.0/24`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'static-routes': {'module': 'core', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'static-routes': {'module': 'core', 'class': 'list[string]'}}, output_type={'module': 'core', 'class': 'IPSecConnection'})
@cli_util.wrap_exceptions
def create_ip_sec_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, cpe_id, drg_id, static_routes, defined_tags, display_name, freeform_tags):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['cpeId'] = cpe_id
    details['drgId'] = drg_id
    details['staticRoutes'] = cli_util.parse_json_parameter("static_routes", static_routes)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_ip_sec_connection(
        create_ip_sec_connection_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_ip_sec_connection') and callable(getattr(client, 'get_ip_sec_connection')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_ip_sec_connection(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@local_peering_gateway_group.command(name=cli_util.override('create_local_peering_gateway.command_name', 'create'), help="""Creates a new local peering gateway (LPG) for the specified VCN.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment containing the local peering gateway (LPG).""")
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN the LPG belongs to.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'LocalPeeringGateway'})
@cli_util.wrap_exceptions
def create_local_peering_gateway(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, vcn_id, defined_tags, display_name, freeform_tags):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['vcnId'] = vcn_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_local_peering_gateway(
        create_local_peering_gateway_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_local_peering_gateway') and callable(getattr(client, 'get_local_peering_gateway')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_local_peering_gateway(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@nat_gateway_group.command(name=cli_util.override('create_nat_gateway.command_name', 'create'), help="""Creates a new NAT gateway for the specified VCN. You must also set up a route rule with the NAT gateway as the rule's target. See [Route Table].""")
@cli_util.option('--compartment-id', required=True, help="""The [OCID] of the compartment to contain the NAT gateway.""")
@cli_util.option('--vcn-id', required=True, help="""The [OCID] of the VCN the gateway belongs to.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--block-traffic', type=click.BOOL, help="""Whether the NAT gateway blocks traffic through it. The default is `false`.

Example: `true`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'NatGateway'})
@cli_util.wrap_exceptions
def create_nat_gateway(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, vcn_id, defined_tags, display_name, freeform_tags, block_traffic):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['vcnId'] = vcn_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if block_traffic is not None:
        details['blockTraffic'] = block_traffic

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_nat_gateway(
        create_nat_gateway_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_nat_gateway') and callable(getattr(client, 'get_nat_gateway')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_nat_gateway(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@private_ip_group.command(name=cli_util.override('create_private_ip.command_name', 'create'), help="""Creates a secondary private IP for the specified VNIC. For more information about secondary private IPs, see [IP Addresses].""")
@cli_util.option('--vnic-id', required=True, help="""The OCID of the VNIC to assign the private IP to. The VNIC and private IP must be in the same subnet.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostname-label', help="""The hostname for the private IP. Used for DNS. The value is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952] and [RFC 1123].

For more information, see [DNS in Your Virtual Cloud Network].

Example: `bminstance-1`""")
@cli_util.option('--ip-address', help="""A private IP address of your choice. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet.

Example: `10.0.3.3`""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'PrivateIp'})
@cli_util.wrap_exceptions
def create_private_ip(ctx, from_json, vnic_id, defined_tags, display_name, freeform_tags, hostname_label, ip_address):
    kwargs = {}

    details = {}
    details['vnicId'] = vnic_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if hostname_label is not None:
        details['hostnameLabel'] = hostname_label

    if ip_address is not None:
        details['ipAddress'] = ip_address

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_private_ip(
        create_private_ip_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_group.command(name=cli_util.override('create_public_ip.command_name', 'create'), help="""Creates a public IP. Use the `lifetime` property to specify whether it's an ephemeral or reserved public IP. For information about limits on how many you can create, see [Public IP Addresses].

* **For an ephemeral public IP assigned to a private IP:** You must also specify a `privateIpId` with the OCID of the primary private IP you want to assign the public IP to. The public IP is created in the same availability domain as the private IP. An ephemeral public IP must always be assigned to a private IP, and only to the *primary* private IP on a VNIC, not a secondary private IP. Exception: If you create a [NatGateway], Oracle automatically assigns the NAT gateway a regional ephemeral public IP that you cannot remove.

* **For a reserved public IP:** You may also optionally assign the public IP to a private IP by specifying `privateIpId`. Or you can later assign the public IP with [UpdatePublicIp].

**Note:** When assigning a public IP to a private IP, the private IP must not already have a public IP with `lifecycleState` = ASSIGNING or ASSIGNED. If it does, an error is returned.

Also, for reserved public IPs, the optional assignment part of this operation is asynchronous. Poll the public IP's `lifecycleState` to determine if the assignment succeeded.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the public IP. For ephemeral public IPs, you must set this to the private IP's compartment OCID.""")
@cli_util.option('--lifetime', required=True, type=custom_types.CliCaseInsensitiveChoice(["EPHEMERAL", "RESERVED"]), help="""Defines when the public IP is deleted and released back to the Oracle Cloud Infrastructure public IP pool. For more information, see [Public IP Addresses].""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--private-ip-id', help="""The OCID of the private IP to assign the public IP to.

Required for an ephemeral public IP because it must always be assigned to a private IP (specifically a *primary* private IP).

Optional for a reserved public IP. If you don't provide it, the public IP is created but not assigned to a private IP. You can later assign the public IP with [UpdatePublicIp].""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "ASSIGNING", "ASSIGNED", "UNASSIGNING", "UNASSIGNED", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'PublicIp'})
@cli_util.wrap_exceptions
def create_public_ip(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, lifetime, defined_tags, display_name, freeform_tags, private_ip_id):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['lifetime'] = lifetime

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if private_ip_id is not None:
        details['privateIpId'] = private_ip_id

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_public_ip(
        create_public_ip_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_public_ip') and callable(getattr(client, 'get_public_ip')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_public_ip(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@remote_peering_connection_group.command(name=cli_util.override('create_remote_peering_connection.command_name', 'create'), help="""Creates a new remote peering connection (RPC) for the specified DRG.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the RPC.""")
@cli_util.option('--drg-id', required=True, help="""The OCID of the DRG the RPC belongs to.""")
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "PROVISIONING", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'RemotePeeringConnection'})
@cli_util.wrap_exceptions
def create_remote_peering_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, drg_id, display_name):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['drgId'] = drg_id

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_remote_peering_connection(
        create_remote_peering_connection_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_remote_peering_connection') and callable(getattr(client, 'get_remote_peering_connection')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_remote_peering_connection(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@route_table_group.command(name=cli_util.override('create_route_table.command_name', 'create'), help="""Creates a new route table for the specified VCN. In the request you must also include at least one route rule for the new route table. For information on the number of rules you can have in a route table, see [Service Limits]. For general information about route tables in your VCN and the types of targets you can use in route rules, see [Route Tables].

For the purposes of access control, you must provide the OCID of the compartment where you want the route table to reside. Notice that the route table doesn't have to be in the same compartment as the VCN, subnets, or other Networking Service components. If you're not sure which compartment to use, put the route table in the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the route table, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the route table.""")
@cli_util.option('--route-rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""The collection of rules used for routing destination IPs to network devices.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN the route table belongs to.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'route-rules': {'module': 'core', 'class': 'list[RouteRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'route-rules': {'module': 'core', 'class': 'list[RouteRule]'}}, output_type={'module': 'core', 'class': 'RouteTable'})
@cli_util.wrap_exceptions
def create_route_table(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, route_rules, vcn_id, defined_tags, display_name, freeform_tags):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['routeRules'] = cli_util.parse_json_parameter("route_rules", route_rules)
    details['vcnId'] = vcn_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_route_table(
        create_route_table_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_route_table') and callable(getattr(client, 'get_route_table')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_route_table(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@security_list_group.command(name=cli_util.override('create_security_list.command_name', 'create'), help="""Creates a new security list for the specified VCN. For more information about security lists, see [Security Lists]. For information on the number of rules you can have in a security list, see [Service Limits].

For the purposes of access control, you must provide the OCID of the compartment where you want the security list to reside. Notice that the security list doesn't have to be in the same compartment as the VCN, subnets, or other Networking Service components. If you're not sure which compartment to use, put the security list in the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the security list, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the security list.""")
@cli_util.option('--egress-security-rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""Rules for allowing egress IP packets.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ingress-security-rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""Rules for allowing ingress IP packets.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN the security list belongs to.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'egress-security-rules': {'module': 'core', 'class': 'list[EgressSecurityRule]'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'ingress-security-rules': {'module': 'core', 'class': 'list[IngressSecurityRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'egress-security-rules': {'module': 'core', 'class': 'list[EgressSecurityRule]'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'ingress-security-rules': {'module': 'core', 'class': 'list[IngressSecurityRule]'}}, output_type={'module': 'core', 'class': 'SecurityList'})
@cli_util.wrap_exceptions
def create_security_list(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, egress_security_rules, ingress_security_rules, vcn_id, defined_tags, display_name, freeform_tags):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['egressSecurityRules'] = cli_util.parse_json_parameter("egress_security_rules", egress_security_rules)
    details['ingressSecurityRules'] = cli_util.parse_json_parameter("ingress_security_rules", ingress_security_rules)
    details['vcnId'] = vcn_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_security_list(
        create_security_list_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_security_list') and callable(getattr(client, 'get_security_list')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_security_list(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@service_gateway_group.command(name=cli_util.override('create_service_gateway.command_name', 'create'), help="""Creates a new service gateway in the specified compartment.

For the purposes of access control, you must provide the OCID of the compartment where you want the service gateway to reside. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the service gateway, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help="""The [OCID]   of the compartment to contain the service gateway.""")
@cli_util.option('--services', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""List of the service OCIDs. These are the services that will be enabled on the service gateway. This list can be empty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vcn-id', required=True, help="""The [OCID] of the VCN.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'services': {'module': 'core', 'class': 'list[ServiceIdRequestDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'services': {'module': 'core', 'class': 'list[ServiceIdRequestDetails]'}}, output_type={'module': 'core', 'class': 'ServiceGateway'})
@cli_util.wrap_exceptions
def create_service_gateway(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, services, vcn_id, defined_tags, display_name, freeform_tags):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['services'] = cli_util.parse_json_parameter("services", services)
    details['vcnId'] = vcn_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_service_gateway(
        create_service_gateway_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_service_gateway') and callable(getattr(client, 'get_service_gateway')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_service_gateway(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@subnet_group.command(name=cli_util.override('create_subnet.command_name', 'create'), help="""Creates a new subnet in the specified VCN. You can't change the size of the subnet after creation, so it's important to think about the size of subnets you need before creating them. For more information, see [VCNs and Subnets]. For information on the number of subnets you can have in a VCN, see [Service Limits].

For the purposes of access control, you must provide the OCID of the compartment where you want the subnet to reside. Notice that the subnet doesn't have to be in the same compartment as the VCN, route tables, or other Networking Service components. If you're not sure which compartment to use, put the subnet in the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally associate a route table with the subnet. If you don't, the subnet will use the VCN's default route table. For more information about route tables, see [Route Tables].

You may optionally associate a security list with the subnet. If you don't, the subnet will use the VCN's default security list. For more information about security lists, see [Security Lists].

You may optionally associate a set of DHCP options with the subnet. If you don't, the subnet will use the VCN's default set. For more information about DHCP options, see [DHCP Options].

You may optionally specify a *display name* for the subnet, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

You can also add a DNS label for the subnet, which is required if you want the Internet and VCN Resolver to resolve hostnames for instances in the subnet. For more information, see [DNS in Your Virtual Cloud Network].""")
@cli_util.option('--availability-domain', required=True, help="""The availability domain to contain the subnet.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--cidr-block', required=True, help="""The CIDR IP address range of the subnet.

Example: `172.16.1.0/24`""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the subnet.""")
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN to contain the subnet.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dhcp-options-id', help="""The OCID of the set of DHCP options the subnet will use. If you don't provide a value, the subnet uses the VCN's default set of DHCP options.""")
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--dns-label', help="""A DNS label for the subnet, used in conjunction with the VNIC's hostname and VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be an alphanumeric string that begins with a letter and is unique within the VCN. The value cannot be changed.

This value must be set if you want to use the Internet and VCN Resolver to resolve the hostnames of instances in the subnet. It can only be set if the VCN itself was created with a DNS label.

For more information, see [DNS in Your Virtual Cloud Network].

Example: `subnet123`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--prohibit-public-ip-on-vnic', type=click.BOOL, help="""Whether VNICs within this subnet can have public IP addresses. Defaults to false, which means VNICs created in this subnet will automatically be assigned public IP addresses unless specified otherwise during instance launch or VNIC creation (with the `assignPublicIp` flag in [CreateVnicDetails]). If `prohibitPublicIpOnVnic` is set to true, VNICs created in this subnet cannot have public IP addresses (that is, it's a private subnet).

Example: `true`""")
@cli_util.option('--route-table-id', help="""The OCID of the route table the subnet will use. If you don't provide a value, the subnet uses the VCN's default route table.""")
@cli_util.option('--security-list-ids', type=custom_types.CLI_COMPLEX_TYPE, help="""The OCIDs of the security list or lists the subnet will use. If you don't provide a value, the subnet uses the VCN's default security list. Remember that security lists are associated *with the subnet*, but the rules are applied to the individual VNICs in the subnet.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'security-list-ids': {'module': 'core', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'security-list-ids': {'module': 'core', 'class': 'list[string]'}}, output_type={'module': 'core', 'class': 'Subnet'})
@cli_util.wrap_exceptions
def create_subnet(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, cidr_block, compartment_id, vcn_id, defined_tags, dhcp_options_id, display_name, dns_label, freeform_tags, prohibit_public_ip_on_vnic, route_table_id, security_list_ids):
    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['cidrBlock'] = cidr_block
    details['compartmentId'] = compartment_id
    details['vcnId'] = vcn_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if dhcp_options_id is not None:
        details['dhcpOptionsId'] = dhcp_options_id

    if display_name is not None:
        details['displayName'] = display_name

    if dns_label is not None:
        details['dnsLabel'] = dns_label

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if prohibit_public_ip_on_vnic is not None:
        details['prohibitPublicIpOnVnic'] = prohibit_public_ip_on_vnic

    if route_table_id is not None:
        details['routeTableId'] = route_table_id

    if security_list_ids is not None:
        details['securityListIds'] = cli_util.parse_json_parameter("security_list_ids", security_list_ids)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_subnet(
        create_subnet_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_subnet') and callable(getattr(client, 'get_subnet')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_subnet(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vcn_group.command(name=cli_util.override('create_vcn.command_name', 'create'), help="""Creates a new virtual cloud network (VCN). For more information, see [VCNs and Subnets].

For the VCN you must specify a single, contiguous IPv4 CIDR block. Oracle recommends using one of the private IP address ranges specified in [RFC 1918] (10.0.0.0/8, 172.16/12, and 192.168/16). Example: 172.16.0.0/16. The CIDR block can range from /16 to /30, and it must not overlap with your on-premises network. You can't change the size of the VCN after creation.

For the purposes of access control, you must provide the OCID of the compartment where you want the VCN to reside. Consult an Oracle Cloud Infrastructure administrator in your organization if you're not sure which compartment to use. Notice that the VCN doesn't have to be in the same compartment as the subnets or other Networking Service components. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the VCN, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

You can also add a DNS label for the VCN, which is required if you want the instances to use the Interent and VCN Resolver option for DNS in the VCN. For more information, see [DNS in Your Virtual Cloud Network].

The VCN automatically comes with a default route table, default security list, and default set of DHCP options. The OCID for each is returned in the response. You can't delete these default objects, but you can change their contents (that is, change the route rules, security list rules, and so on).

The VCN and subnets you create are not accessible until you attach an internet gateway or set up an IPSec VPN or FastConnect. For more information, see [Overview of the Networking Service].""")
@cli_util.option('--cidr-block', required=True, help="""The CIDR IP address block of the VCN.

Example: `172.16.0.0/16`""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the VCN.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--dns-label', help="""A DNS label for the VCN, used in conjunction with the VNIC's hostname and subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`). Not required to be unique, but it's a best practice to set unique DNS labels for VCNs in your tenancy. Must be an alphanumeric string that begins with a letter. The value cannot be changed.

You must set this value if you want instances to be able to use hostnames to resolve other instances in the VCN. Otherwise the Internet and VCN Resolver will not work.

For more information, see [DNS in Your Virtual Cloud Network].

Example: `vcn1`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Vcn'})
@cli_util.wrap_exceptions
def create_vcn(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, cidr_block, compartment_id, defined_tags, display_name, dns_label, freeform_tags):
    kwargs = {}

    details = {}
    details['cidrBlock'] = cidr_block
    details['compartmentId'] = compartment_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if dns_label is not None:
        details['dnsLabel'] = dns_label

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_vcn(
        create_vcn_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_vcn') and callable(getattr(client, 'get_vcn')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vcn(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_circuit_group.command(name=cli_util.override('create_virtual_circuit.command_name', 'create'), help="""Creates a new virtual circuit to use with Oracle Cloud Infrastructure FastConnect. For more information, see [FastConnect Overview].

For the purposes of access control, you must provide the OCID of the compartment where you want the virtual circuit to reside. If you're not sure which compartment to use, put the virtual circuit in the same compartment with the DRG it's using. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the virtual circuit. It does not have to be unique, and you can change it. Avoid entering confidential information.

**Important:** When creating a virtual circuit, you specify a DRG for the traffic to flow through. Make sure you attach the DRG to your VCN and confirm the VCN's routing sends traffic to the DRG. Otherwise traffic will not flow. For more information, see [Route Tables].""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the virtual circuit.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["PUBLIC", "PRIVATE"]), help="""The type of IP addresses used in this virtual circuit. PRIVATE means [RFC 1918] addresses (10.0.0.0/8, 172.16/12, and 192.168/16). Only PRIVATE is supported.""")
@cli_util.option('--bandwidth-shape-name', help="""The provisioned data rate of the connection.  To get a list of the available bandwidth levels (that is, shapes), see [ListFastConnectProviderServiceVirtualCircuitBandwidthShapes].

Example: `10 Gbps`""")
@cli_util.option('--cross-connect-mappings', type=custom_types.CLI_COMPLEX_TYPE, help="""Create a `CrossConnectMapping` for each cross-connect or cross-connect group this virtual circuit will run on.

This option is a JSON list with items of type CrossConnectMapping.  For documentation on CrossConnectMapping please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/CrossConnectMapping.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--customer-bgp-asn', type=click.INT, help="""Your BGP ASN (either public or private). Provide this value only if there's a BGP session that goes from your edge router to Oracle. Otherwise, leave this empty or null.""")
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--gateway-id', help="""For private virtual circuits only. The OCID of the [dynamic routing gateway (DRG)] that this virtual circuit uses.""")
@cli_util.option('--provider-name', help="""Deprecated. Instead use `providerServiceId`. To get a list of the provider names, see [ListFastConnectProviderServices].""")
@cli_util.option('--provider-service-id', help="""The OCID of the service offered by the provider (if you're connecting via a provider). To get a list of the available service offerings, see [ListFastConnectProviderServices].""")
@cli_util.option('--provider-service-name', help="""Deprecated. Instead use `providerServiceId`. To get a list of the provider names, see [ListFastConnectProviderServices].""")
@cli_util.option('--public-prefixes', type=custom_types.CLI_COMPLEX_TYPE, help="""For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to advertise across the connection.

This option is a JSON list with items of type CreateVirtualCircuitPublicPrefixDetails.  For documentation on CreateVirtualCircuitPublicPrefixDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/CreateVirtualCircuitPublicPrefixDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--region', help="""The Oracle Cloud Infrastructure region where this virtual circuit is located. Example: `phx`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_PROVIDER", "VERIFYING", "PROVISIONING", "PROVISIONED", "FAILED", "INACTIVE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'cross-connect-mappings': {'module': 'core', 'class': 'list[CrossConnectMapping]'}, 'public-prefixes': {'module': 'core', 'class': 'list[CreateVirtualCircuitPublicPrefixDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'cross-connect-mappings': {'module': 'core', 'class': 'list[CrossConnectMapping]'}, 'public-prefixes': {'module': 'core', 'class': 'list[CreateVirtualCircuitPublicPrefixDetails]'}}, output_type={'module': 'core', 'class': 'VirtualCircuit'})
@cli_util.wrap_exceptions
def create_virtual_circuit(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, type, bandwidth_shape_name, cross_connect_mappings, customer_bgp_asn, display_name, gateway_id, provider_name, provider_service_id, provider_service_name, public_prefixes, region):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['type'] = type

    if bandwidth_shape_name is not None:
        details['bandwidthShapeName'] = bandwidth_shape_name

    if cross_connect_mappings is not None:
        details['crossConnectMappings'] = cli_util.parse_json_parameter("cross_connect_mappings", cross_connect_mappings)

    if customer_bgp_asn is not None:
        details['customerBgpAsn'] = customer_bgp_asn

    if display_name is not None:
        details['displayName'] = display_name

    if gateway_id is not None:
        details['gatewayId'] = gateway_id

    if provider_name is not None:
        details['providerName'] = provider_name

    if provider_service_id is not None:
        details['providerServiceId'] = provider_service_id

    if provider_service_name is not None:
        details['providerServiceName'] = provider_service_name

    if public_prefixes is not None:
        details['publicPrefixes'] = cli_util.parse_json_parameter("public_prefixes", public_prefixes)

    if region is not None:
        details['region'] = region

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_virtual_circuit(
        create_virtual_circuit_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_virtual_circuit') and callable(getattr(client, 'get_virtual_circuit')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_virtual_circuit(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cpe_group.command(name=cli_util.override('delete_cpe.command_name', 'delete'), help="""Deletes the specified CPE object. The CPE must not be connected to a DRG. This is an asynchronous operation. The CPE's `lifecycleState` will change to TERMINATING temporarily until the CPE is completely removed.""")
@cli_util.option('--cpe-id', required=True, help="""The OCID of the CPE.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_cpe(ctx, from_json, cpe_id, if_match):

    if isinstance(cpe_id, six.string_types) and len(cpe_id.strip()) == 0:
        raise click.UsageError('Parameter --cpe-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_cpe(
        cpe_id=cpe_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cross_connect_group.command(name=cli_util.override('delete_cross_connect.command_name', 'delete'), help="""Deletes the specified cross-connect. It must not be mapped to a [VirtualCircuit].""")
@cli_util.option('--cross-connect-id', required=True, help="""The OCID of the cross-connect.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_cross_connect(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, cross_connect_id, if_match):

    if isinstance(cross_connect_id, six.string_types) and len(cross_connect_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_cross_connect(
        cross_connect_id=cross_connect_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_cross_connect') and callable(getattr(client, 'get_cross_connect')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_cross_connect(cross_connect_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cross_connect_group_group.command(name=cli_util.override('delete_cross_connect_group.command_name', 'delete'), help="""Deletes the specified cross-connect group. It must not contain any cross-connects, and it cannot be mapped to a [VirtualCircuit].""")
@cli_util.option('--cross-connect-group-id', required=True, help="""The OCID of the cross-connect group.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_cross_connect_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, cross_connect_group_id, if_match):

    if isinstance(cross_connect_group_id, six.string_types) and len(cross_connect_group_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-group-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_cross_connect_group(
        cross_connect_group_id=cross_connect_group_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_cross_connect_group') and callable(getattr(client, 'get_cross_connect_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_cross_connect_group(cross_connect_group_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dhcp_options_group.command(name=cli_util.override('delete_dhcp_options.command_name', 'delete'), help="""Deletes the specified set of DHCP options, but only if it's not associated with a subnet. You can't delete a VCN's default set of DHCP options.

This is an asynchronous operation. The state of the set of options will switch to TERMINATING temporarily until the set is completely removed.""")
@cli_util.option('--dhcp-id', required=True, help="""The OCID for the set of DHCP options.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_dhcp_options(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dhcp_id, if_match):

    if isinstance(dhcp_id, six.string_types) and len(dhcp_id.strip()) == 0:
        raise click.UsageError('Parameter --dhcp-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_dhcp_options(
        dhcp_id=dhcp_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_dhcp_options') and callable(getattr(client, 'get_dhcp_options')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_dhcp_options(dhcp_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@drg_group.command(name=cli_util.override('delete_drg.command_name', 'delete'), help="""Deletes the specified DRG. The DRG must not be attached to a VCN or be connected to your on-premise network. Also, there must not be a route table that lists the DRG as a target. This is an asynchronous operation. The DRG's `lifecycleState` will change to TERMINATING temporarily until the DRG is completely removed.""")
@cli_util.option('--drg-id', required=True, help="""The OCID of the DRG.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_drg(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_id, if_match):

    if isinstance(drg_id, six.string_types) and len(drg_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_drg(
        drg_id=drg_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_drg') and callable(getattr(client, 'get_drg')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_drg(drg_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@drg_attachment_group.command(name=cli_util.override('delete_drg_attachment.command_name', 'delete'), help="""Detaches a DRG from a VCN by deleting the corresponding `DrgAttachment`. This is an asynchronous operation. The attachment's `lifecycleState` will change to DETACHING temporarily until the attachment is completely removed.""")
@cli_util.option('--drg-attachment-id', required=True, help="""The OCID of the DRG attachment.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_drg_attachment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_attachment_id, if_match):

    if isinstance(drg_attachment_id, six.string_types) and len(drg_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-attachment-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_drg_attachment(
        drg_attachment_id=drg_attachment_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_drg_attachment') and callable(getattr(client, 'get_drg_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_drg_attachment(drg_attachment_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@internet_gateway_group.command(name=cli_util.override('delete_internet_gateway.command_name', 'delete'), help="""Deletes the specified internet gateway. The internet gateway does not have to be disabled, but there must not be a route table that lists it as a target.

This is an asynchronous operation. The gateway's `lifecycleState` will change to TERMINATING temporarily until the gateway is completely removed.""")
@cli_util.option('--ig-id', required=True, help="""The OCID of the internet gateway.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_internet_gateway(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, ig_id, if_match):

    if isinstance(ig_id, six.string_types) and len(ig_id.strip()) == 0:
        raise click.UsageError('Parameter --ig-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_internet_gateway(
        ig_id=ig_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_internet_gateway') and callable(getattr(client, 'get_internet_gateway')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_internet_gateway(ig_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@ip_sec_connection_group.command(name=cli_util.override('delete_ip_sec_connection.command_name', 'delete'), help="""Deletes the specified IPSec connection. If your goal is to disable the IPSec VPN between your VCN and on-premises network, it's easiest to simply detach the DRG but keep all the IPSec VPN components intact. If you were to delete all the components and then later need to create an IPSec VPN again, you would need to configure your on-premises router again with the new information returned from [CreateIPSecConnection].

This is an asynchronous operation. The connection's `lifecycleState` will change to TERMINATING temporarily until the connection is completely removed.""")
@cli_util.option('--ipsc-id', required=True, help="""The OCID of the IPSec connection.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_ip_sec_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, ipsc_id, if_match):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_ip_sec_connection(
        ipsc_id=ipsc_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_ip_sec_connection') and callable(getattr(client, 'get_ip_sec_connection')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_ip_sec_connection(ipsc_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@local_peering_gateway_group.command(name=cli_util.override('delete_local_peering_gateway.command_name', 'delete'), help="""Deletes the specified local peering gateway (LPG).

This is an asynchronous operation; the local peering gateway's `lifecycleState` changes to TERMINATING temporarily until the local peering gateway is completely removed.""")
@cli_util.option('--local-peering-gateway-id', required=True, help="""The OCID of the local peering gateway.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_local_peering_gateway(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, local_peering_gateway_id, if_match):

    if isinstance(local_peering_gateway_id, six.string_types) and len(local_peering_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --local-peering-gateway-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_local_peering_gateway(
        local_peering_gateway_id=local_peering_gateway_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_local_peering_gateway') and callable(getattr(client, 'get_local_peering_gateway')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_local_peering_gateway(local_peering_gateway_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@nat_gateway_group.command(name=cli_util.override('delete_nat_gateway.command_name', 'delete'), help="""Deletes the specified NAT gateway. The NAT gateway does not have to be disabled, but there must not be a route rule that lists the NAT gateway as a target.

This is an asynchronous operation. The NAT gateway's `lifecycleState` will change to TERMINATING temporarily until the NAT gateway is completely removed.""")
@cli_util.option('--nat-gateway-id', required=True, help="""The NAT gateway's [OCID].""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_nat_gateway(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, nat_gateway_id, if_match):

    if isinstance(nat_gateway_id, six.string_types) and len(nat_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --nat-gateway-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_nat_gateway(
        nat_gateway_id=nat_gateway_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_nat_gateway') and callable(getattr(client, 'get_nat_gateway')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_nat_gateway(nat_gateway_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@private_ip_group.command(name=cli_util.override('delete_private_ip.command_name', 'delete'), help="""Unassigns and deletes the specified private IP. You must specify the object's OCID. The private IP address is returned to the subnet's pool of available addresses.

This operation cannot be used with primary private IPs, which are automatically unassigned and deleted when the VNIC is terminated.

**Important:** If a secondary private IP is the [target of a route rule], unassigning it from the VNIC causes that route rule to blackhole and the traffic will be dropped.""")
@cli_util.option('--private-ip-id', required=True, help="""The OCID of the private IP.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_private_ip(ctx, from_json, private_ip_id, if_match):

    if isinstance(private_ip_id, six.string_types) and len(private_ip_id.strip()) == 0:
        raise click.UsageError('Parameter --private-ip-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_private_ip(
        private_ip_id=private_ip_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_group.command(name=cli_util.override('delete_public_ip.command_name', 'delete'), help="""Unassigns and deletes the specified public IP (either ephemeral or reserved). You must specify the object's OCID. The public IP address is returned to the Oracle Cloud Infrastructure public IP pool.

**Note:** You cannot update, unassign, or delete the public IP that Oracle automatically assigned to an entity for you (such as a load balancer or NAT gateway). The public IP is automatically deleted if the assigned entity is terminated.

For an assigned reserved public IP, the initial unassignment portion of this operation is asynchronous. Poll the public IP's `lifecycleState` to determine if the operation succeeded.

If you want to simply unassign a reserved public IP and return it to your pool of reserved public IPs, instead use [UpdatePublicIp].""")
@cli_util.option('--public-ip-id', required=True, help="""The OCID of the public IP.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "ASSIGNING", "ASSIGNED", "UNASSIGNING", "UNASSIGNED", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_public_ip(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, public_ip_id, if_match):

    if isinstance(public_ip_id, six.string_types) and len(public_ip_id.strip()) == 0:
        raise click.UsageError('Parameter --public-ip-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_public_ip(
        public_ip_id=public_ip_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_public_ip') and callable(getattr(client, 'get_public_ip')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_public_ip(public_ip_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@remote_peering_connection_group.command(name=cli_util.override('delete_remote_peering_connection.command_name', 'delete'), help="""Deletes the remote peering connection (RPC).

This is an asynchronous operation; the RPC's `lifecycleState` changes to TERMINATING temporarily until the RPC is completely removed.""")
@cli_util.option('--remote-peering-connection-id', required=True, help="""The OCID of the remote peering connection (RPC).""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "PROVISIONING", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_remote_peering_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, remote_peering_connection_id, if_match):

    if isinstance(remote_peering_connection_id, six.string_types) and len(remote_peering_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --remote-peering-connection-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_remote_peering_connection(
        remote_peering_connection_id=remote_peering_connection_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_remote_peering_connection') and callable(getattr(client, 'get_remote_peering_connection')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_remote_peering_connection(remote_peering_connection_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@route_table_group.command(name=cli_util.override('delete_route_table.command_name', 'delete'), help="""Deletes the specified route table, but only if it's not associated with a subnet. You can't delete a VCN's default route table.

This is an asynchronous operation. The route table's `lifecycleState` will change to TERMINATING temporarily until the route table is completely removed.""")
@cli_util.option('--rt-id', required=True, help="""The OCID of the route table.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_route_table(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, rt_id, if_match):

    if isinstance(rt_id, six.string_types) and len(rt_id.strip()) == 0:
        raise click.UsageError('Parameter --rt-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_route_table(
        rt_id=rt_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_route_table') and callable(getattr(client, 'get_route_table')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_route_table(rt_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@security_list_group.command(name=cli_util.override('delete_security_list.command_name', 'delete'), help="""Deletes the specified security list, but only if it's not associated with a subnet. You can't delete a VCN's default security list.

This is an asynchronous operation. The security list's `lifecycleState` will change to TERMINATING temporarily until the security list is completely removed.""")
@cli_util.option('--security-list-id', required=True, help="""The OCID of the security list.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_security_list(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, security_list_id, if_match):

    if isinstance(security_list_id, six.string_types) and len(security_list_id.strip()) == 0:
        raise click.UsageError('Parameter --security-list-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_security_list(
        security_list_id=security_list_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_security_list') and callable(getattr(client, 'get_security_list')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_security_list(security_list_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@service_gateway_group.command(name=cli_util.override('delete_service_gateway.command_name', 'delete'), help="""Deletes the specified service gateway. There must not be a route table that lists the service gateway as a target.""")
@cli_util.option('--service-gateway-id', required=True, help="""The service gateway's [OCID].""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_service_gateway(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, service_gateway_id, if_match):

    if isinstance(service_gateway_id, six.string_types) and len(service_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --service-gateway-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_service_gateway(
        service_gateway_id=service_gateway_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_service_gateway') and callable(getattr(client, 'get_service_gateway')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_service_gateway(service_gateway_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@subnet_group.command(name=cli_util.override('delete_subnet.command_name', 'delete'), help="""Deletes the specified subnet, but only if there are no instances in the subnet. This is an asynchronous operation. The subnet's `lifecycleState` will change to TERMINATING temporarily. If there are any instances in the subnet, the state will instead change back to AVAILABLE.""")
@cli_util.option('--subnet-id', required=True, help="""The OCID of the subnet.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_subnet(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, subnet_id, if_match):

    if isinstance(subnet_id, six.string_types) and len(subnet_id.strip()) == 0:
        raise click.UsageError('Parameter --subnet-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_subnet(
        subnet_id=subnet_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_subnet') and callable(getattr(client, 'get_subnet')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_subnet(subnet_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vcn_group.command(name=cli_util.override('delete_vcn.command_name', 'delete'), help="""Deletes the specified VCN. The VCN must be empty and have no attached gateways. This is an asynchronous operation. The VCN's `lifecycleState` will change to TERMINATING temporarily until the VCN is completely removed.""")
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_vcn(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vcn_id, if_match):

    if isinstance(vcn_id, six.string_types) and len(vcn_id.strip()) == 0:
        raise click.UsageError('Parameter --vcn-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_vcn(
        vcn_id=vcn_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_vcn') and callable(getattr(client, 'get_vcn')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_vcn(vcn_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_circuit_group.command(name=cli_util.override('delete_virtual_circuit.command_name', 'delete'), help="""Deletes the specified virtual circuit.

**Important:** If you're using FastConnect via a provider, make sure to also terminate the connection with the provider, or else the provider may continue to bill you.""")
@cli_util.option('--virtual-circuit-id', required=True, help="""The OCID of the virtual circuit.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_PROVIDER", "VERIFYING", "PROVISIONING", "PROVISIONED", "FAILED", "INACTIVE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_virtual_circuit(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_circuit_id, if_match):

    if isinstance(virtual_circuit_id, six.string_types) and len(virtual_circuit_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-circuit-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_virtual_circuit(
        virtual_circuit_id=virtual_circuit_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_virtual_circuit') and callable(getattr(client, 'get_virtual_circuit')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_virtual_circuit(virtual_circuit_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@service_gateway_group.command(name=cli_util.override('detach_service_id.command_name', 'detach'), help="""Disables the specified service on the specified gateway. In other words, stops the service gateway from sending traffic to the specified service. You do not need to remove any route rules that specify this service's `cidrBlock` as the destination CIDR. However, consider removing the rules if your intent is to permanently disable use of the service through this service gateway.

**Note:** The `DetachServiceId` operation is an easy way to disable an individual service on the service gateway. Compare it with [UpdateServiceGateway], which also lets you disable an individual service. However, with `UpdateServiceGateway`, you must specify the *entire* list of services you want enabled on the service gateway. `UpdateServiceGateway` also lets you block all traffic through the service gateway without having to disable each of the individual services.""")
@cli_util.option('--service-gateway-id', required=True, help="""The service gateway's [OCID].""")
@cli_util.option('--service-id', required=True, help="""The [OCID] of the service.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ServiceGateway'})
@cli_util.wrap_exceptions
def detach_service_id(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, service_gateway_id, service_id, if_match):

    if isinstance(service_gateway_id, six.string_types) and len(service_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --service-gateway-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['serviceId'] = service_id

    client = cli_util.build_client('virtual_network', ctx)
    result = client.detach_service_id(
        service_gateway_id=service_gateway_id,
        detach_service_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_service_gateway') and callable(getattr(client, 'get_service_gateway')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_service_gateway(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cpe_group.command(name=cli_util.override('get_cpe.command_name', 'get'), help="""Gets the specified CPE's information.""")
@cli_util.option('--cpe-id', required=True, help="""The OCID of the CPE.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Cpe'})
@cli_util.wrap_exceptions
def get_cpe(ctx, from_json, cpe_id):

    if isinstance(cpe_id, six.string_types) and len(cpe_id.strip()) == 0:
        raise click.UsageError('Parameter --cpe-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_cpe(
        cpe_id=cpe_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cross_connect_group.command(name=cli_util.override('get_cross_connect.command_name', 'get'), help="""Gets the specified cross-connect's information.""")
@cli_util.option('--cross-connect-id', required=True, help="""The OCID of the cross-connect.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'CrossConnect'})
@cli_util.wrap_exceptions
def get_cross_connect(ctx, from_json, cross_connect_id):

    if isinstance(cross_connect_id, six.string_types) and len(cross_connect_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_cross_connect(
        cross_connect_id=cross_connect_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cross_connect_group_group.command(name=cli_util.override('get_cross_connect_group.command_name', 'get'), help="""Gets the specified cross-connect group's information.""")
@cli_util.option('--cross-connect-group-id', required=True, help="""The OCID of the cross-connect group.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'CrossConnectGroup'})
@cli_util.wrap_exceptions
def get_cross_connect_group(ctx, from_json, cross_connect_group_id):

    if isinstance(cross_connect_group_id, six.string_types) and len(cross_connect_group_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-group-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_cross_connect_group(
        cross_connect_group_id=cross_connect_group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@letter_of_authority_group.command(name=cli_util.override('get_cross_connect_letter_of_authority.command_name', 'get-cross-connect'), help="""Gets the Letter of Authority for the specified cross-connect.""")
@cli_util.option('--cross-connect-id', required=True, help="""The OCID of the cross-connect.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'LetterOfAuthority'})
@cli_util.wrap_exceptions
def get_cross_connect_letter_of_authority(ctx, from_json, cross_connect_id):

    if isinstance(cross_connect_id, six.string_types) and len(cross_connect_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_cross_connect_letter_of_authority(
        cross_connect_id=cross_connect_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cross_connect_status_group.command(name=cli_util.override('get_cross_connect_status.command_name', 'get'), help="""Gets the status of the specified cross-connect.""")
@cli_util.option('--cross-connect-id', required=True, help="""The OCID of the cross-connect.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'CrossConnectStatus'})
@cli_util.wrap_exceptions
def get_cross_connect_status(ctx, from_json, cross_connect_id):

    if isinstance(cross_connect_id, six.string_types) and len(cross_connect_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_cross_connect_status(
        cross_connect_id=cross_connect_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dhcp_options_group.command(name=cli_util.override('get_dhcp_options.command_name', 'get'), help="""Gets the specified set of DHCP options.""")
@cli_util.option('--dhcp-id', required=True, help="""The OCID for the set of DHCP options.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'DhcpOptions'})
@cli_util.wrap_exceptions
def get_dhcp_options(ctx, from_json, dhcp_id):

    if isinstance(dhcp_id, six.string_types) and len(dhcp_id.strip()) == 0:
        raise click.UsageError('Parameter --dhcp-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_dhcp_options(
        dhcp_id=dhcp_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@drg_group.command(name=cli_util.override('get_drg.command_name', 'get'), help="""Gets the specified DRG's information.""")
@cli_util.option('--drg-id', required=True, help="""The OCID of the DRG.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Drg'})
@cli_util.wrap_exceptions
def get_drg(ctx, from_json, drg_id):

    if isinstance(drg_id, six.string_types) and len(drg_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_drg(
        drg_id=drg_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@drg_attachment_group.command(name=cli_util.override('get_drg_attachment.command_name', 'get'), help="""Gets the information for the specified `DrgAttachment`.""")
@cli_util.option('--drg-attachment-id', required=True, help="""The OCID of the DRG attachment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'DrgAttachment'})
@cli_util.wrap_exceptions
def get_drg_attachment(ctx, from_json, drg_attachment_id):

    if isinstance(drg_attachment_id, six.string_types) and len(drg_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-attachment-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_drg_attachment(
        drg_attachment_id=drg_attachment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fast_connect_provider_service_group.command(name=cli_util.override('get_fast_connect_provider_service.command_name', 'get'), help="""Gets the specified provider service. For more information, see [FastConnect Overview].""")
@cli_util.option('--provider-service-id', required=True, help="""The OCID of the provider service.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'FastConnectProviderService'})
@cli_util.wrap_exceptions
def get_fast_connect_provider_service(ctx, from_json, provider_service_id):

    if isinstance(provider_service_id, six.string_types) and len(provider_service_id.strip()) == 0:
        raise click.UsageError('Parameter --provider-service-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_fast_connect_provider_service(
        provider_service_id=provider_service_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@internet_gateway_group.command(name=cli_util.override('get_internet_gateway.command_name', 'get'), help="""Gets the specified internet gateway's information.""")
@cli_util.option('--ig-id', required=True, help="""The OCID of the internet gateway.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InternetGateway'})
@cli_util.wrap_exceptions
def get_internet_gateway(ctx, from_json, ig_id):

    if isinstance(ig_id, six.string_types) and len(ig_id.strip()) == 0:
        raise click.UsageError('Parameter --ig-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_internet_gateway(
        ig_id=ig_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ip_sec_connection_group.command(name=cli_util.override('get_ip_sec_connection.command_name', 'get'), help="""Gets the specified IPSec connection's basic information, including the static routes for the on-premises router. If you want the status of the connection (whether it's up or down), use [GetIPSecConnectionDeviceStatus].""")
@cli_util.option('--ipsc-id', required=True, help="""The OCID of the IPSec connection.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'IPSecConnection'})
@cli_util.wrap_exceptions
def get_ip_sec_connection(ctx, from_json, ipsc_id):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_ip_sec_connection(
        ipsc_id=ipsc_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ip_sec_connection_device_config_group.command(name=cli_util.override('get_ip_sec_connection_device_config.command_name', 'get'), help="""Gets the configuration information for the specified IPSec connection. For each tunnel, the response includes the IP address of Oracle's VPN headend and the shared secret.""")
@cli_util.option('--ipsc-id', required=True, help="""The OCID of the IPSec connection.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'IPSecConnectionDeviceConfig'})
@cli_util.wrap_exceptions
def get_ip_sec_connection_device_config(ctx, from_json, ipsc_id):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_ip_sec_connection_device_config(
        ipsc_id=ipsc_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ip_sec_connection_device_status_group.command(name=cli_util.override('get_ip_sec_connection_device_status.command_name', 'get'), help="""Gets the status of the specified IPSec connection (whether it's up or down).""")
@cli_util.option('--ipsc-id', required=True, help="""The OCID of the IPSec connection.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'IPSecConnectionDeviceStatus'})
@cli_util.wrap_exceptions
def get_ip_sec_connection_device_status(ctx, from_json, ipsc_id):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_ip_sec_connection_device_status(
        ipsc_id=ipsc_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@local_peering_gateway_group.command(name=cli_util.override('get_local_peering_gateway.command_name', 'get'), help="""Gets the specified local peering gateway's information.""")
@cli_util.option('--local-peering-gateway-id', required=True, help="""The OCID of the local peering gateway.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'LocalPeeringGateway'})
@cli_util.wrap_exceptions
def get_local_peering_gateway(ctx, from_json, local_peering_gateway_id):

    if isinstance(local_peering_gateway_id, six.string_types) and len(local_peering_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --local-peering-gateway-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_local_peering_gateway(
        local_peering_gateway_id=local_peering_gateway_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@nat_gateway_group.command(name=cli_util.override('get_nat_gateway.command_name', 'get'), help="""Gets the specified NAT gateway's information.""")
@cli_util.option('--nat-gateway-id', required=True, help="""The NAT gateway's [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'NatGateway'})
@cli_util.wrap_exceptions
def get_nat_gateway(ctx, from_json, nat_gateway_id):

    if isinstance(nat_gateway_id, six.string_types) and len(nat_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --nat-gateway-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_nat_gateway(
        nat_gateway_id=nat_gateway_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@private_ip_group.command(name=cli_util.override('get_private_ip.command_name', 'get'), help="""Gets the specified private IP. You must specify the object's OCID. Alternatively, you can get the object by using [ListPrivateIps] with the private IP address (for example, 10.0.3.3) and subnet OCID.""")
@cli_util.option('--private-ip-id', required=True, help="""The OCID of the private IP.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PrivateIp'})
@cli_util.wrap_exceptions
def get_private_ip(ctx, from_json, private_ip_id):

    if isinstance(private_ip_id, six.string_types) and len(private_ip_id.strip()) == 0:
        raise click.UsageError('Parameter --private-ip-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_private_ip(
        private_ip_id=private_ip_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_group.command(name=cli_util.override('get_public_ip.command_name', 'get'), help="""Gets the specified public IP. You must specify the object's OCID.

Alternatively, you can get the object by using [GetPublicIpByIpAddress] with the public IP address (for example, 129.146.2.1).

Or you can use [GetPublicIpByPrivateIpId] with the OCID of the private IP that the public IP is assigned to.

**Note:** If you're fetching a reserved public IP that is in the process of being moved to a different private IP, the service returns the public IP object with `lifecycleState` = ASSIGNING and `assignedEntityId` = OCID of the target private IP.""")
@cli_util.option('--public-ip-id', required=True, help="""The OCID of the public IP.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PublicIp'})
@cli_util.wrap_exceptions
def get_public_ip(ctx, from_json, public_ip_id):

    if isinstance(public_ip_id, six.string_types) and len(public_ip_id.strip()) == 0:
        raise click.UsageError('Parameter --public-ip-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_public_ip(
        public_ip_id=public_ip_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_group.command(name=cli_util.override('get_public_ip_by_ip_address.command_name', 'get-public-ip-by-ip-address'), help="""Gets the public IP based on the public IP address (for example, 129.146.2.1).

**Note:** If you're fetching a reserved public IP that is in the process of being moved to a different private IP, the service returns the public IP object with `lifecycleState` = ASSIGNING and `assignedEntityId` = OCID of the target private IP.""")
@cli_util.option('--ip-address', required=True, help="""The public IP address. Example: 129.146.2.1""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PublicIp'})
@cli_util.wrap_exceptions
def get_public_ip_by_ip_address(ctx, from_json, ip_address):
    kwargs = {}

    details = {}
    details['ipAddress'] = ip_address

    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_public_ip_by_ip_address(
        get_public_ip_by_ip_address_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_group.command(name=cli_util.override('get_public_ip_by_private_ip_id.command_name', 'get-public-ip-by-private-ip-id'), help="""Gets the public IP assigned to the specified private IP. You must specify the OCID of the private IP. If no public IP is assigned, a 404 is returned.

**Note:** If you're fetching a reserved public IP that is in the process of being moved to a different private IP, and you provide the OCID of the original private IP, this operation returns a 404. If you instead provide the OCID of the target private IP, or if you instead call [GetPublicIp] or [GetPublicIpByIpAddress], the service returns the public IP object with `lifecycleState` = ASSIGNING and `assignedEntityId` = OCID of the target private IP.""")
@cli_util.option('--private-ip-id', required=True, help="""OCID of the private IP.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PublicIp'})
@cli_util.wrap_exceptions
def get_public_ip_by_private_ip_id(ctx, from_json, private_ip_id):
    kwargs = {}

    details = {}
    details['privateIpId'] = private_ip_id

    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_public_ip_by_private_ip_id(
        get_public_ip_by_private_ip_id_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@remote_peering_connection_group.command(name=cli_util.override('get_remote_peering_connection.command_name', 'get'), help="""Get the specified remote peering connection's information.""")
@cli_util.option('--remote-peering-connection-id', required=True, help="""The OCID of the remote peering connection (RPC).""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'RemotePeeringConnection'})
@cli_util.wrap_exceptions
def get_remote_peering_connection(ctx, from_json, remote_peering_connection_id):

    if isinstance(remote_peering_connection_id, six.string_types) and len(remote_peering_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --remote-peering-connection-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_remote_peering_connection(
        remote_peering_connection_id=remote_peering_connection_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@route_table_group.command(name=cli_util.override('get_route_table.command_name', 'get'), help="""Gets the specified route table's information.""")
@cli_util.option('--rt-id', required=True, help="""The OCID of the route table.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'RouteTable'})
@cli_util.wrap_exceptions
def get_route_table(ctx, from_json, rt_id):

    if isinstance(rt_id, six.string_types) and len(rt_id.strip()) == 0:
        raise click.UsageError('Parameter --rt-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_route_table(
        rt_id=rt_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@security_list_group.command(name=cli_util.override('get_security_list.command_name', 'get'), help="""Gets the specified security list's information.""")
@cli_util.option('--security-list-id', required=True, help="""The OCID of the security list.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'SecurityList'})
@cli_util.wrap_exceptions
def get_security_list(ctx, from_json, security_list_id):

    if isinstance(security_list_id, six.string_types) and len(security_list_id.strip()) == 0:
        raise click.UsageError('Parameter --security-list-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_security_list(
        security_list_id=security_list_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@service_group.command(name=cli_util.override('get_service.command_name', 'get'), help="""Gets the specified service's information.""")
@cli_util.option('--service-id', required=True, help="""The service's [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Service'})
@cli_util.wrap_exceptions
def get_service(ctx, from_json, service_id):

    if isinstance(service_id, six.string_types) and len(service_id.strip()) == 0:
        raise click.UsageError('Parameter --service-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_service(
        service_id=service_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@service_gateway_group.command(name=cli_util.override('get_service_gateway.command_name', 'get'), help="""Gets the specified service gateway's information.""")
@cli_util.option('--service-gateway-id', required=True, help="""The service gateway's [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ServiceGateway'})
@cli_util.wrap_exceptions
def get_service_gateway(ctx, from_json, service_gateway_id):

    if isinstance(service_gateway_id, six.string_types) and len(service_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --service-gateway-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_service_gateway(
        service_gateway_id=service_gateway_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subnet_group.command(name=cli_util.override('get_subnet.command_name', 'get'), help="""Gets the specified subnet's information.""")
@cli_util.option('--subnet-id', required=True, help="""The OCID of the subnet.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Subnet'})
@cli_util.wrap_exceptions
def get_subnet(ctx, from_json, subnet_id):

    if isinstance(subnet_id, six.string_types) and len(subnet_id.strip()) == 0:
        raise click.UsageError('Parameter --subnet-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_subnet(
        subnet_id=subnet_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vcn_group.command(name=cli_util.override('get_vcn.command_name', 'get'), help="""Gets the specified VCN's information.""")
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Vcn'})
@cli_util.wrap_exceptions
def get_vcn(ctx, from_json, vcn_id):

    if isinstance(vcn_id, six.string_types) and len(vcn_id.strip()) == 0:
        raise click.UsageError('Parameter --vcn-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_vcn(
        vcn_id=vcn_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@virtual_circuit_group.command(name=cli_util.override('get_virtual_circuit.command_name', 'get'), help="""Gets the specified virtual circuit's information.""")
@cli_util.option('--virtual-circuit-id', required=True, help="""The OCID of the virtual circuit.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VirtualCircuit'})
@cli_util.wrap_exceptions
def get_virtual_circuit(ctx, from_json, virtual_circuit_id):

    if isinstance(virtual_circuit_id, six.string_types) and len(virtual_circuit_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-circuit-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_virtual_circuit(
        virtual_circuit_id=virtual_circuit_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vnic_group.command(name=cli_util.override('get_vnic.command_name', 'get'), help="""Gets the information for the specified virtual network interface card (VNIC). You can get the VNIC OCID from the [ListVnicAttachments] operation.""")
@cli_util.option('--vnic-id', required=True, help="""The OCID of the VNIC.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Vnic'})
@cli_util.wrap_exceptions
def get_vnic(ctx, from_json, vnic_id):

    if isinstance(vnic_id, six.string_types) and len(vnic_id.strip()) == 0:
        raise click.UsageError('Parameter --vnic-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_vnic(
        vnic_id=vnic_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@peer_region_for_remote_peering_group.command(name=cli_util.override('list_allowed_peer_regions_for_remote_peering.command_name', 'list-allowed-peer-regions-for-remote-peering'), help="""Lists the regions that support remote VCN peering (which is peering across regions). For more information, see [VCN Peering].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[PeerRegionForRemotePeering]'})
@cli_util.wrap_exceptions
def list_allowed_peer_regions_for_remote_peering(ctx, from_json, ):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_allowed_peer_regions_for_remote_peering(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cpe_group.command(name=cli_util.override('list_cpes.command_name', 'list'), help="""Lists the customer-premises equipment objects (CPEs) in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Cpe]'})
@cli_util.wrap_exceptions
def list_cpes(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_cpes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_cpes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_cpes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@cross_connect_group_group.command(name=cli_util.override('list_cross_connect_groups.command_name', 'list'), help="""Lists the cross-connect groups in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), help="""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[CrossConnectGroup]'})
@cli_util.wrap_exceptions
def list_cross_connect_groups(ctx, from_json, all_pages, page_size, compartment_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_cross_connect_groups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_cross_connect_groups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_cross_connect_groups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@cross_connect_location_group.command(name=cli_util.override('list_cross_connect_locations.command_name', 'list'), help="""Lists the available FastConnect locations for cross-connect installation. You need this information so you can specify your desired location when you create a cross-connect.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[CrossConnectLocation]'})
@cli_util.wrap_exceptions
def list_cross_connect_locations(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_cross_connect_locations,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_cross_connect_locations,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_cross_connect_locations(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@cross_connect_group.command(name=cli_util.override('list_cross_connects.command_name', 'list'), help="""Lists the cross-connects in the specified compartment. You can filter the list by specifying the OCID of a cross-connect group.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--cross-connect-group-id', help="""The OCID of the cross-connect group.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), help="""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[CrossConnect]'})
@cli_util.wrap_exceptions
def list_cross_connects(ctx, from_json, all_pages, page_size, compartment_id, cross_connect_group_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if cross_connect_group_id is not None:
        kwargs['cross_connect_group_id'] = cross_connect_group_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_cross_connects,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_cross_connects,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_cross_connects(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@cross_connect_port_speed_shape_group.command(name=cli_util.override('list_crossconnect_port_speed_shapes.command_name', 'list-crossconnect-port-speed-shapes'), help="""Lists the available port speeds for cross-connects. You need this information so you can specify your desired port speed (that is, shape) when you create a cross-connect.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[CrossConnectPortSpeedShape]'})
@cli_util.wrap_exceptions
def list_crossconnect_port_speed_shapes(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_crossconnect_port_speed_shapes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_crossconnect_port_speed_shapes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_crossconnect_port_speed_shapes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@dhcp_options_group.command(name=cli_util.override('list_dhcp_options.command_name', 'list'), help="""Lists the sets of DHCP options in the specified VCN and specified compartment. The response includes the default set of options that automatically comes with each VCN, plus any other sets you've created.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[DhcpOptions]'})
@cli_util.wrap_exceptions
def list_dhcp_options(ctx, from_json, all_pages, page_size, compartment_id, vcn_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_dhcp_options,
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_dhcp_options,
            limit,
            page_size,
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    else:
        result = client.list_dhcp_options(
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@drg_attachment_group.command(name=cli_util.override('list_drg_attachments.command_name', 'list'), help="""Lists the `DrgAttachment` objects for the specified compartment. You can filter the results by VCN or DRG.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--vcn-id', help="""The OCID of the VCN.""")
@cli_util.option('--drg-id', help="""The OCID of the DRG.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[DrgAttachment]'})
@cli_util.wrap_exceptions
def list_drg_attachments(ctx, from_json, all_pages, page_size, compartment_id, vcn_id, drg_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if vcn_id is not None:
        kwargs['vcn_id'] = vcn_id
    if drg_id is not None:
        kwargs['drg_id'] = drg_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_drg_attachments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_drg_attachments,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_drg_attachments(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@drg_group.command(name=cli_util.override('list_drgs.command_name', 'list'), help="""Lists the DRGs in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Drg]'})
@cli_util.wrap_exceptions
def list_drgs(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_drgs,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_drgs,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_drgs(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@fast_connect_provider_service_group.command(name=cli_util.override('list_fast_connect_provider_services.command_name', 'list'), help="""Lists the service offerings from supported providers. You need this information so you can specify your desired provider and service offering when you create a virtual circuit.

For the compartment ID, provide the OCID of your tenancy (the root compartment).

For more information, see [FastConnect Overview].""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[FastConnectProviderService]'})
@cli_util.wrap_exceptions
def list_fast_connect_provider_services(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_fast_connect_provider_services,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_fast_connect_provider_services,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_fast_connect_provider_services(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@fast_connect_provider_service_group.command(name=cli_util.override('list_fast_connect_provider_virtual_circuit_bandwidth_shapes.command_name', 'list-fast-connect-provider-virtual-circuit-bandwidth-shapes'), help="""Gets the list of available virtual circuit bandwidth levels for a provider. You need this information so you can specify your desired bandwidth level (shape) when you create a virtual circuit.

For more information about virtual circuits, see [FastConnect Overview].""")
@cli_util.option('--provider-service-id', required=True, help="""The OCID of the provider service.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VirtualCircuitBandwidthShape]'})
@cli_util.wrap_exceptions
def list_fast_connect_provider_virtual_circuit_bandwidth_shapes(ctx, from_json, all_pages, page_size, provider_service_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(provider_service_id, six.string_types) and len(provider_service_id.strip()) == 0:
        raise click.UsageError('Parameter --provider-service-id cannot be whitespace or empty string')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_fast_connect_provider_virtual_circuit_bandwidth_shapes,
            provider_service_id=provider_service_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_fast_connect_provider_virtual_circuit_bandwidth_shapes,
            limit,
            page_size,
            provider_service_id=provider_service_id,
            **kwargs
        )
    else:
        result = client.list_fast_connect_provider_virtual_circuit_bandwidth_shapes(
            provider_service_id=provider_service_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@internet_gateway_group.command(name=cli_util.override('list_internet_gateways.command_name', 'list'), help="""Lists the internet gateways in the specified VCN and the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[InternetGateway]'})
@cli_util.wrap_exceptions
def list_internet_gateways(ctx, from_json, all_pages, page_size, compartment_id, vcn_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_internet_gateways,
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_internet_gateways,
            limit,
            page_size,
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    else:
        result = client.list_internet_gateways(
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@ip_sec_connection_group.command(name=cli_util.override('list_ip_sec_connections.command_name', 'list'), help="""Lists the IPSec connections for the specified compartment. You can filter the results by DRG or CPE.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--drg-id', help="""The OCID of the DRG.""")
@cli_util.option('--cpe-id', help="""The OCID of the CPE.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[IPSecConnection]'})
@cli_util.wrap_exceptions
def list_ip_sec_connections(ctx, from_json, all_pages, page_size, compartment_id, drg_id, cpe_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if drg_id is not None:
        kwargs['drg_id'] = drg_id
    if cpe_id is not None:
        kwargs['cpe_id'] = cpe_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_ip_sec_connections,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_ip_sec_connections,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_ip_sec_connections(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@local_peering_gateway_group.command(name=cli_util.override('list_local_peering_gateways.command_name', 'list'), help="""Lists the local peering gateways (LPGs) for the specified VCN and compartment (the LPG's compartment).""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[LocalPeeringGateway]'})
@cli_util.wrap_exceptions
def list_local_peering_gateways(ctx, from_json, all_pages, page_size, compartment_id, vcn_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_local_peering_gateways,
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_local_peering_gateways,
            limit,
            page_size,
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    else:
        result = client.list_local_peering_gateways(
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@nat_gateway_group.command(name=cli_util.override('list_nat_gateways.command_name', 'list'), help="""Lists the NAT gateways in the specified compartment. You may optionally specify a VCN OCID to filter the results by VCN.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--vcn-id', help="""The OCID of the VCN.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[NatGateway]'})
@cli_util.wrap_exceptions
def list_nat_gateways(ctx, from_json, all_pages, page_size, compartment_id, vcn_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if vcn_id is not None:
        kwargs['vcn_id'] = vcn_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_nat_gateways,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_nat_gateways,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_nat_gateways(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@private_ip_group.command(name=cli_util.override('list_private_ips.command_name', 'list'), help="""Lists the [PrivateIp] objects based on one of these filters:

  - Subnet OCID.   - VNIC OCID.   - Both private IP address and subnet OCID: This lets   you get a `privateIP` object based on its private IP   address (for example, 10.0.3.3) and not its OCID. For comparison,   [GetPrivateIp]   requires the OCID.

If you're listing all the private IPs associated with a given subnet or VNIC, the response includes both primary and secondary private IPs.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--ip-address', help="""An IP address.

Example: `10.0.3.3`""")
@cli_util.option('--subnet-id', help="""The OCID of the subnet.""")
@cli_util.option('--vnic-id', help="""The OCID of the VNIC.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[PrivateIp]'})
@cli_util.wrap_exceptions
def list_private_ips(ctx, from_json, all_pages, page_size, limit, page, ip_address, subnet_id, vnic_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if ip_address is not None:
        kwargs['ip_address'] = ip_address
    if subnet_id is not None:
        kwargs['subnet_id'] = subnet_id
    if vnic_id is not None:
        kwargs['vnic_id'] = vnic_id
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_private_ips,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_private_ips,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_private_ips(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@public_ip_group.command(name=cli_util.override('list_public_ips.command_name', 'list'), help="""Lists the [PublicIp] objects in the specified compartment. You can filter the list by using query parameters.

To list your reserved public IPs:   * Set `scope` = `REGION`  (required)   * Leave the `availabilityDomain` parameter empty   * Set `lifetime` = `RESERVED`

To list the ephemeral public IPs assigned to a regional entity such as a NAT gateway:   * Set `scope` = `REGION`  (required)   * Leave the `availabilityDomain` parameter empty   * Set `lifetime` = `EPHEMERAL`

To list the ephemeral public IPs assigned to private IPs:   * Set `scope` = `AVAILABILITY_DOMAIN` (required)   * Set the `availabilityDomain` parameter to the desired availability domain (required)   * Set `lifetime` = `EPHEMERAL`

**Note:** An ephemeral public IP assigned to a private IP is always in the same availability domain and compartment as the private IP.""")
@cli_util.option('--scope', required=True, type=custom_types.CliCaseInsensitiveChoice(["REGION", "AVAILABILITY_DOMAIN"]), help="""Whether the public IP is regional or specific to a particular availability domain.

* `REGION`: The public IP exists within a region and is assigned to a regional entity (such as a [NatGateway]), or can be assigned to a private IP in any availability domain in the region. Reserved public IPs have `scope` = `REGION`, as do ephemeral public IPs assigned to a regional entity.

* `AVAILABILITY_DOMAIN`: The public IP exists within the availability domain of the entity it's assigned to, which is specified by the `availabilityDomain` property of the public IP object. Ephemeral public IPs that are assigned to private IPs have `scope` = `AVAILABILITY_DOMAIN`.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--availability-domain', help="""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--lifetime', type=custom_types.CliCaseInsensitiveChoice(["EPHEMERAL", "RESERVED"]), help="""A filter to return only public IPs that match given lifetime.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[PublicIp]'})
@cli_util.wrap_exceptions
def list_public_ips(ctx, from_json, all_pages, page_size, scope, compartment_id, limit, page, availability_domain, lifetime):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if lifetime is not None:
        kwargs['lifetime'] = lifetime
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_public_ips,
            scope=scope,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_public_ips,
            limit,
            page_size,
            scope=scope,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_public_ips(
            scope=scope,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@remote_peering_connection_group.command(name=cli_util.override('list_remote_peering_connections.command_name', 'list'), help="""Lists the remote peering connections (RPCs) for the specified DRG and compartment (the RPC's compartment).""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--drg-id', help="""The OCID of the DRG.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[RemotePeeringConnection]'})
@cli_util.wrap_exceptions
def list_remote_peering_connections(ctx, from_json, all_pages, page_size, compartment_id, drg_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if drg_id is not None:
        kwargs['drg_id'] = drg_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_remote_peering_connections,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_remote_peering_connections,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_remote_peering_connections(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@route_table_group.command(name=cli_util.override('list_route_tables.command_name', 'list'), help="""Lists the route tables in the specified VCN and specified compartment. The response includes the default route table that automatically comes with each VCN, plus any route tables you've created.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[RouteTable]'})
@cli_util.wrap_exceptions
def list_route_tables(ctx, from_json, all_pages, page_size, compartment_id, vcn_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_route_tables,
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_route_tables,
            limit,
            page_size,
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    else:
        result = client.list_route_tables(
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@security_list_group.command(name=cli_util.override('list_security_lists.command_name', 'list'), help="""Lists the security lists in the specified VCN and compartment.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[SecurityList]'})
@cli_util.wrap_exceptions
def list_security_lists(ctx, from_json, all_pages, page_size, compartment_id, vcn_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_security_lists,
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_security_lists,
            limit,
            page_size,
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    else:
        result = client.list_security_lists(
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@service_gateway_group.command(name=cli_util.override('list_service_gateways.command_name', 'list'), help="""Lists the service gateways in the specified compartment. You may optionally specify a VCN OCID to filter the results by VCN.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--vcn-id', help="""The OCID of the VCN.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""A filter to return only resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[ServiceGateway]'})
@cli_util.wrap_exceptions
def list_service_gateways(ctx, from_json, all_pages, page_size, compartment_id, vcn_id, limit, page, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if vcn_id is not None:
        kwargs['vcn_id'] = vcn_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_service_gateways,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_service_gateways,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_service_gateways(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@service_group.command(name=cli_util.override('list_services.command_name', 'list'), help="""Lists the available services that you can access through a service gateway in this region.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Service]'})
@cli_util.wrap_exceptions
def list_services(ctx, from_json, all_pages, page_size, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_services,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_services,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_services(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@subnet_group.command(name=cli_util.override('list_subnets.command_name', 'list'), help="""Lists the subnets in the specified VCN and the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Subnet]'})
@cli_util.wrap_exceptions
def list_subnets(ctx, from_json, all_pages, page_size, compartment_id, vcn_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_subnets,
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_subnets,
            limit,
            page_size,
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    else:
        result = client.list_subnets(
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@vcn_group.command(name=cli_util.override('list_vcns.command_name', 'list'), help="""Lists the virtual cloud networks (VCNs) in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Vcn]'})
@cli_util.wrap_exceptions
def list_vcns(ctx, from_json, all_pages, page_size, compartment_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_vcns,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_vcns,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_vcns(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@virtual_circuit_bandwidth_shape_group.command(name=cli_util.override('list_virtual_circuit_bandwidth_shapes.command_name', 'list'), help="""The deprecated operation lists available bandwidth levels for virtual circuits. For the compartment ID, provide the OCID of your tenancy (the root compartment).""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VirtualCircuitBandwidthShape]'})
@cli_util.wrap_exceptions
def list_virtual_circuit_bandwidth_shapes(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_virtual_circuit_bandwidth_shapes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_virtual_circuit_bandwidth_shapes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_virtual_circuit_bandwidth_shapes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@virtual_circuit_public_prefix_group.command(name=cli_util.override('list_virtual_circuit_public_prefixes.command_name', 'list'), help="""Lists the public IP prefixes and their details for the specified public virtual circuit.""")
@cli_util.option('--virtual-circuit-id', required=True, help="""The OCID of the virtual circuit.""")
@cli_util.option('--verification-state', type=custom_types.CliCaseInsensitiveChoice(["IN_PROGRESS", "COMPLETED", "FAILED"]), help="""A filter to only return resources that match the given verification state. The state value is case-insensitive.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VirtualCircuitPublicPrefix]'})
@cli_util.wrap_exceptions
def list_virtual_circuit_public_prefixes(ctx, from_json, virtual_circuit_id, verification_state):

    if isinstance(virtual_circuit_id, six.string_types) and len(virtual_circuit_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-circuit-id cannot be whitespace or empty string')
    kwargs = {}
    if verification_state is not None:
        kwargs['verification_state'] = verification_state
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_virtual_circuit_public_prefixes(
        virtual_circuit_id=virtual_circuit_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@virtual_circuit_group.command(name=cli_util.override('list_virtual_circuits.command_name', 'list'), help="""Lists the virtual circuits in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_PROVIDER", "VERIFYING", "PROVISIONING", "PROVISIONED", "FAILED", "INACTIVE", "TERMINATING", "TERMINATED"]), help="""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VirtualCircuit]'})
@cli_util.wrap_exceptions
def list_virtual_circuits(ctx, from_json, all_pages, page_size, compartment_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_virtual_circuits,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_virtual_circuits,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_virtual_circuits(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@cpe_group.command(name=cli_util.override('update_cpe.command_name', 'update'), help="""Updates the specified CPE's display name or tags. Avoid entering confidential information.""")
@cli_util.option('--cpe-id', required=True, help="""The OCID of the CPE.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Cpe'})
@cli_util.wrap_exceptions
def update_cpe(ctx, from_json, force, cpe_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(cpe_id, six.string_types) and len(cpe_id.strip()) == 0:
        raise click.UsageError('Parameter --cpe-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_cpe(
        cpe_id=cpe_id,
        update_cpe_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cross_connect_group.command(name=cli_util.override('update_cross_connect.command_name', 'update'), help="""Updates the specified cross-connect.""")
@cli_util.option('--cross-connect-id', required=True, help="""The OCID of the cross-connect.""")
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--is-active', type=click.BOOL, help="""Set to true to activate the cross-connect. You activate it after the physical cabling is complete, and you've confirmed the cross-connect's light levels are good and your side of the interface is up. Activation indicates to Oracle that the physical connection is ready.

Example: `true`""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'CrossConnect'})
@cli_util.wrap_exceptions
def update_cross_connect(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, cross_connect_id, display_name, is_active, if_match):

    if isinstance(cross_connect_id, six.string_types) and len(cross_connect_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if is_active is not None:
        details['isActive'] = is_active

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_cross_connect(
        cross_connect_id=cross_connect_id,
        update_cross_connect_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_cross_connect') and callable(getattr(client, 'get_cross_connect')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_cross_connect(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cross_connect_group_group.command(name=cli_util.override('update_cross_connect_group.command_name', 'update'), help="""Updates the specified cross-connect group's display name. Avoid entering confidential information.""")
@cli_util.option('--cross-connect-group-id', required=True, help="""The OCID of the cross-connect group.""")
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'CrossConnectGroup'})
@cli_util.wrap_exceptions
def update_cross_connect_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, cross_connect_group_id, display_name, if_match):

    if isinstance(cross_connect_group_id, six.string_types) and len(cross_connect_group_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-group-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_cross_connect_group(
        cross_connect_group_id=cross_connect_group_id,
        update_cross_connect_group_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_cross_connect_group') and callable(getattr(client, 'get_cross_connect_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_cross_connect_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dhcp_options_group.command(name=cli_util.override('update_dhcp_options.command_name', 'update'), help="""Updates the specified set of DHCP options. You can update the display name or the options themselves. Avoid entering confidential information.

Note that the `options` object you provide replaces the entire existing set of options.""")
@cli_util.option('--dhcp-id', required=True, help="""The OCID for the set of DHCP options.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--options', type=custom_types.CLI_COMPLEX_TYPE, help="""

This option is a JSON list with items of type DhcpOption.  For documentation on DhcpOption please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/DhcpOption.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'options': {'module': 'core', 'class': 'list[DhcpOption]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'options': {'module': 'core', 'class': 'list[DhcpOption]'}}, output_type={'module': 'core', 'class': 'DhcpOptions'})
@cli_util.wrap_exceptions
def update_dhcp_options(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, dhcp_id, defined_tags, display_name, freeform_tags, options, if_match):

    if isinstance(dhcp_id, six.string_types) and len(dhcp_id.strip()) == 0:
        raise click.UsageError('Parameter --dhcp-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or options:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and options will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if options is not None:
        details['options'] = cli_util.parse_json_parameter("options", options)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_dhcp_options(
        dhcp_id=dhcp_id,
        update_dhcp_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_dhcp_options') and callable(getattr(client, 'get_dhcp_options')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_dhcp_options(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@drg_group.command(name=cli_util.override('update_drg.command_name', 'update'), help="""Updates the specified DRG's display name or tags. Avoid entering confidential information.""")
@cli_util.option('--drg-id', required=True, help="""The OCID of the DRG.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Drg'})
@cli_util.wrap_exceptions
def update_drg(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(drg_id, six.string_types) and len(drg_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_drg(
        drg_id=drg_id,
        update_drg_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_drg') and callable(getattr(client, 'get_drg')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_drg(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@drg_attachment_group.command(name=cli_util.override('update_drg_attachment.command_name', 'update'), help="""Updates the display name for the specified `DrgAttachment`. Avoid entering confidential information.""")
@cli_util.option('--drg-attachment-id', required=True, help="""The OCID of the DRG attachment.""")
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'DrgAttachment'})
@cli_util.wrap_exceptions
def update_drg_attachment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_attachment_id, display_name, if_match):

    if isinstance(drg_attachment_id, six.string_types) and len(drg_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-attachment-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_drg_attachment(
        drg_attachment_id=drg_attachment_id,
        update_drg_attachment_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_drg_attachment') and callable(getattr(client, 'get_drg_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_drg_attachment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@internet_gateway_group.command(name=cli_util.override('update_internet_gateway.command_name', 'update'), help="""Updates the specified internet gateway. You can disable/enable it, or change its display name or tags. Avoid entering confidential information.

If the gateway is disabled, that means no traffic will flow to/from the internet even if there's a route rule that enables that traffic.""")
@cli_util.option('--ig-id', required=True, help="""The OCID of the internet gateway.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-enabled', type=click.BOOL, help="""Whether the gateway is enabled.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'InternetGateway'})
@cli_util.wrap_exceptions
def update_internet_gateway(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, ig_id, defined_tags, display_name, freeform_tags, is_enabled, if_match):

    if isinstance(ig_id, six.string_types) and len(ig_id.strip()) == 0:
        raise click.UsageError('Parameter --ig-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if is_enabled is not None:
        details['isEnabled'] = is_enabled

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_internet_gateway(
        ig_id=ig_id,
        update_internet_gateway_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_internet_gateway') and callable(getattr(client, 'get_internet_gateway')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_internet_gateway(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@ip_sec_connection_group.command(name=cli_util.override('update_ip_sec_connection.command_name', 'update'), help="""Updates the display name or tags for the specified IPSec connection. Avoid entering confidential information.""")
@cli_util.option('--ipsc-id', required=True, help="""The OCID of the IPSec connection.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'IPSecConnection'})
@cli_util.wrap_exceptions
def update_ip_sec_connection(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, ipsc_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_ip_sec_connection(
        ipsc_id=ipsc_id,
        update_ip_sec_connection_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_ip_sec_connection') and callable(getattr(client, 'get_ip_sec_connection')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_ip_sec_connection(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@local_peering_gateway_group.command(name=cli_util.override('update_local_peering_gateway.command_name', 'update'), help="""Updates the specified local peering gateway (LPG).""")
@cli_util.option('--local-peering-gateway-id', required=True, help="""The OCID of the local peering gateway.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'LocalPeeringGateway'})
@cli_util.wrap_exceptions
def update_local_peering_gateway(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, local_peering_gateway_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(local_peering_gateway_id, six.string_types) and len(local_peering_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --local-peering-gateway-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_local_peering_gateway(
        local_peering_gateway_id=local_peering_gateway_id,
        update_local_peering_gateway_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_local_peering_gateway') and callable(getattr(client, 'get_local_peering_gateway')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_local_peering_gateway(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@nat_gateway_group.command(name=cli_util.override('update_nat_gateway.command_name', 'update'), help="""Updates the specified NAT gateway.""")
@cli_util.option('--nat-gateway-id', required=True, help="""The NAT gateway's [OCID].""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--block-traffic', type=click.BOOL, help="""Whether the NAT gateway blocks traffic through it. The default is `false`.

Example: `true`""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'NatGateway'})
@cli_util.wrap_exceptions
def update_nat_gateway(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, nat_gateway_id, defined_tags, display_name, freeform_tags, block_traffic, if_match):

    if isinstance(nat_gateway_id, six.string_types) and len(nat_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --nat-gateway-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if block_traffic is not None:
        details['blockTraffic'] = block_traffic

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_nat_gateway(
        nat_gateway_id=nat_gateway_id,
        update_nat_gateway_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_nat_gateway') and callable(getattr(client, 'get_nat_gateway')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_nat_gateway(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@private_ip_group.command(name=cli_util.override('update_private_ip.command_name', 'update'), help="""Updates the specified private IP. You must specify the object's OCID. Use this operation if you want to:

  - Move a secondary private IP to a different VNIC in the same subnet.   - Change the display name for a secondary private IP.   - Change the hostname for a secondary private IP.

This operation cannot be used with primary private IPs. To update the hostname for the primary IP on a VNIC, use [UpdateVnic].""")
@cli_util.option('--private-ip-id', required=True, help="""The OCID of the private IP.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostname-label', help="""The hostname for the private IP. Used for DNS. The value is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952] and [RFC 1123].

For more information, see [DNS in Your Virtual Cloud Network].

Example: `bminstance-1`""")
@cli_util.option('--vnic-id', help="""The OCID of the VNIC to reassign the private IP to. The VNIC must be in the same subnet as the current VNIC.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'PrivateIp'})
@cli_util.wrap_exceptions
def update_private_ip(ctx, from_json, force, private_ip_id, defined_tags, display_name, freeform_tags, hostname_label, vnic_id, if_match):

    if isinstance(private_ip_id, six.string_types) and len(private_ip_id.strip()) == 0:
        raise click.UsageError('Parameter --private-ip-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if hostname_label is not None:
        details['hostnameLabel'] = hostname_label

    if vnic_id is not None:
        details['vnicId'] = vnic_id

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_private_ip(
        private_ip_id=private_ip_id,
        update_private_ip_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_group.command(name=cli_util.override('update_public_ip.command_name', 'update'), help="""Updates the specified public IP. You must specify the object's OCID. Use this operation if you want to:

* Assign a reserved public IP in your pool to a private IP. * Move a reserved public IP to a different private IP. * Unassign a reserved public IP from a private IP (which returns it to your pool of reserved public IPs). * Change the display name or tags for a public IP.

Assigning, moving, and unassigning a reserved public IP are asynchronous operations. Poll the public IP's `lifecycleState` to determine if the operation succeeded.

**Note:** When moving a reserved public IP, the target private IP must not already have a public IP with `lifecycleState` = ASSIGNING or ASSIGNED. If it does, an error is returned. Also, the initial unassignment from the original private IP always succeeds, but the assignment to the target private IP is asynchronous and could fail silently (for example, if the target private IP is deleted or has a different public IP assigned to it in the interim). If that occurs, the public IP remains unassigned and its `lifecycleState` switches to AVAILABLE (it is not reassigned to its original private IP). You must poll the public IP's `lifecycleState` to determine if the move succeeded.

Regarding ephemeral public IPs:

* If you want to assign an ephemeral public IP to a primary private IP, use [CreatePublicIp]. * You can't move an ephemeral public IP to a different private IP. * If you want to unassign an ephemeral public IP from its private IP, use [DeletePublicIp], which unassigns and deletes the ephemeral public IP.

**Note:** If a public IP (either ephemeral or reserved) is assigned to a secondary private IP (see [PrivateIp]), and you move that secondary private IP to another VNIC, the public IP moves with it.

**Note:** There's a limit to the number of [public IPs] a VNIC or instance can have. If you try to move a reserved public IP to a VNIC or instance that has already reached its public IP limit, an error is returned. For information about the public IP limits, see [Public IP Addresses].""")
@cli_util.option('--public-ip-id', required=True, help="""The OCID of the public IP.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--private-ip-id', help="""The OCID of the private IP to assign the public IP to. * If the public IP is already assigned to a different private IP, it will be unassigned and then reassigned to the specified private IP. * If you set this field to an empty string, the public IP will be unassigned from the private IP it is currently assigned to.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "ASSIGNING", "ASSIGNED", "UNASSIGNING", "UNASSIGNED", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'PublicIp'})
@cli_util.wrap_exceptions
def update_public_ip(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, public_ip_id, defined_tags, display_name, freeform_tags, private_ip_id, if_match):

    if isinstance(public_ip_id, six.string_types) and len(public_ip_id.strip()) == 0:
        raise click.UsageError('Parameter --public-ip-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if private_ip_id is not None:
        details['privateIpId'] = private_ip_id

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_public_ip(
        public_ip_id=public_ip_id,
        update_public_ip_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_public_ip') and callable(getattr(client, 'get_public_ip')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_public_ip(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@remote_peering_connection_group.command(name=cli_util.override('update_remote_peering_connection.command_name', 'update'), help="""Updates the specified remote peering connection (RPC).""")
@cli_util.option('--remote-peering-connection-id', required=True, help="""The OCID of the remote peering connection (RPC).""")
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "PROVISIONING", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'RemotePeeringConnection'})
@cli_util.wrap_exceptions
def update_remote_peering_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, remote_peering_connection_id, display_name, if_match):

    if isinstance(remote_peering_connection_id, six.string_types) and len(remote_peering_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --remote-peering-connection-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_remote_peering_connection(
        remote_peering_connection_id=remote_peering_connection_id,
        update_remote_peering_connection_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_remote_peering_connection') and callable(getattr(client, 'get_remote_peering_connection')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_remote_peering_connection(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@route_table_group.command(name=cli_util.override('update_route_table.command_name', 'update'), help="""Updates the specified route table's display name or route rules. Avoid entering confidential information.

Note that the `routeRules` object you provide replaces the entire existing set of rules.""")
@cli_util.option('--rt-id', required=True, help="""The OCID of the route table.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--route-rules', type=custom_types.CLI_COMPLEX_TYPE, help="""The collection of rules used for routing destination IPs to network devices.

This option is a JSON list with items of type RouteRule.  For documentation on RouteRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/RouteRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'route-rules': {'module': 'core', 'class': 'list[RouteRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'route-rules': {'module': 'core', 'class': 'list[RouteRule]'}}, output_type={'module': 'core', 'class': 'RouteTable'})
@cli_util.wrap_exceptions
def update_route_table(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, rt_id, defined_tags, display_name, freeform_tags, route_rules, if_match):

    if isinstance(rt_id, six.string_types) and len(rt_id.strip()) == 0:
        raise click.UsageError('Parameter --rt-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or route_rules:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and route-rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if route_rules is not None:
        details['routeRules'] = cli_util.parse_json_parameter("route_rules", route_rules)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_route_table(
        rt_id=rt_id,
        update_route_table_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_route_table') and callable(getattr(client, 'get_route_table')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_route_table(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@security_list_group.command(name=cli_util.override('update_security_list.command_name', 'update'), help="""Updates the specified security list's display name or rules. Avoid entering confidential information.

Note that the `egressSecurityRules` or `ingressSecurityRules` objects you provide replace the entire existing objects.""")
@cli_util.option('--security-list-id', required=True, help="""The OCID of the security list.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--egress-security-rules', type=custom_types.CLI_COMPLEX_TYPE, help="""Rules for allowing egress IP packets.

This option is a JSON list with items of type EgressSecurityRule.  For documentation on EgressSecurityRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/EgressSecurityRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ingress-security-rules', type=custom_types.CLI_COMPLEX_TYPE, help="""Rules for allowing ingress IP packets.

This option is a JSON list with items of type IngressSecurityRule.  For documentation on IngressSecurityRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/IngressSecurityRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'egress-security-rules': {'module': 'core', 'class': 'list[EgressSecurityRule]'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'ingress-security-rules': {'module': 'core', 'class': 'list[IngressSecurityRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'egress-security-rules': {'module': 'core', 'class': 'list[EgressSecurityRule]'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'ingress-security-rules': {'module': 'core', 'class': 'list[IngressSecurityRule]'}}, output_type={'module': 'core', 'class': 'SecurityList'})
@cli_util.wrap_exceptions
def update_security_list(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, security_list_id, defined_tags, display_name, egress_security_rules, freeform_tags, ingress_security_rules, if_match):

    if isinstance(security_list_id, six.string_types) and len(security_list_id.strip()) == 0:
        raise click.UsageError('Parameter --security-list-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or egress_security_rules or freeform_tags or ingress_security_rules:
            if not click.confirm("WARNING: Updates to defined-tags and egress-security-rules and freeform-tags and ingress-security-rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if egress_security_rules is not None:
        details['egressSecurityRules'] = cli_util.parse_json_parameter("egress_security_rules", egress_security_rules)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if ingress_security_rules is not None:
        details['ingressSecurityRules'] = cli_util.parse_json_parameter("ingress_security_rules", ingress_security_rules)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_security_list(
        security_list_id=security_list_id,
        update_security_list_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_security_list') and callable(getattr(client, 'get_security_list')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_security_list(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@service_gateway_group.command(name=cli_util.override('update_service_gateway.command_name', 'update'), help="""Updates the specified service gateway. The information you provide overwrites the existing attributes of the gateway.""")
@cli_util.option('--service-gateway-id', required=True, help="""The service gateway's [OCID].""")
@cli_util.option('--block-traffic', type=click.BOOL, help="""Whether the service gateway blocks all traffic through it. The default is `false`. When this is `true`, traffic is not routed to any services, regardless of route rules.

Example: `true`""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--services', type=custom_types.CLI_COMPLEX_TYPE, help="""List of all the services you want enabled on this service gateway. Sending an empty list means you want to disable all services. Omitting this parameter entirely keeps the existing list of services intact.

You can also enable or disable a particular service by using [AttachServiceId] and [DetachServiceId].

For each enabled service, make sure there's a route rule with the service's `cidrBlock` as the rule's destination CIDR and the service gateway as the rule's target. See [Route Table].

This option is a JSON list with items of type ServiceIdRequestDetails.  For documentation on ServiceIdRequestDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/ServiceIdRequestDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'services': {'module': 'core', 'class': 'list[ServiceIdRequestDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'services': {'module': 'core', 'class': 'list[ServiceIdRequestDetails]'}}, output_type={'module': 'core', 'class': 'ServiceGateway'})
@cli_util.wrap_exceptions
def update_service_gateway(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, service_gateway_id, block_traffic, defined_tags, display_name, freeform_tags, services, if_match):

    if isinstance(service_gateway_id, six.string_types) and len(service_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --service-gateway-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or services:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and services will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if block_traffic is not None:
        details['blockTraffic'] = block_traffic

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if services is not None:
        details['services'] = cli_util.parse_json_parameter("services", services)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_service_gateway(
        service_gateway_id=service_gateway_id,
        update_service_gateway_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_service_gateway') and callable(getattr(client, 'get_service_gateway')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_service_gateway(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@subnet_group.command(name=cli_util.override('update_subnet.command_name', 'update'), help="""Updates the specified subnet.""")
@cli_util.option('--subnet-id', required=True, help="""The OCID of the subnet.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Subnet'})
@cli_util.wrap_exceptions
def update_subnet(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, subnet_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(subnet_id, six.string_types) and len(subnet_id.strip()) == 0:
        raise click.UsageError('Parameter --subnet-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_subnet(
        subnet_id=subnet_id,
        update_subnet_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_subnet') and callable(getattr(client, 'get_subnet')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_subnet(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vcn_group.command(name=cli_util.override('update_vcn.command_name', 'update'), help="""Updates the specified VCN.""")
@cli_util.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Vcn'})
@cli_util.wrap_exceptions
def update_vcn(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, vcn_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(vcn_id, six.string_types) and len(vcn_id.strip()) == 0:
        raise click.UsageError('Parameter --vcn-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_vcn(
        vcn_id=vcn_id,
        update_vcn_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_vcn') and callable(getattr(client, 'get_vcn')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vcn(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_circuit_group.command(name=cli_util.override('update_virtual_circuit.command_name', 'update'), help="""Updates the specified virtual circuit. This can be called by either the customer who owns the virtual circuit, or the provider (when provisioning or de-provisioning the virtual circuit from their end). The documentation for [UpdateVirtualCircuitDetails] indicates who can update each property of the virtual circuit.

**Important:** If the virtual circuit is working and in the PROVISIONED state, updating any of the network-related properties (such as the DRG being used, the BGP ASN, and so on) will cause the virtual circuit's state to switch to PROVISIONING and the related BGP session to go down. After Oracle re-provisions the virtual circuit, its state will return to PROVISIONED. Make sure you confirm that the associated BGP session is back up. For more information about the various states and how to test connectivity, see [FastConnect Overview].

To change the list of public IP prefixes for a public virtual circuit, use [BulkAddVirtualCircuitPublicPrefixes] and [BulkDeleteVirtualCircuitPublicPrefixes]. Updating the list of prefixes does NOT cause the BGP session to go down. However, Oracle must verify the customer's ownership of each added prefix before traffic for that prefix will flow across the virtual circuit.""")
@cli_util.option('--virtual-circuit-id', required=True, help="""The OCID of the virtual circuit.""")
@cli_util.option('--bandwidth-shape-name', help="""The provisioned data rate of the connection. To get a list of the available bandwidth levels (that is, shapes), see [ListFastConnectProviderVirtualCircuitBandwidthShapes]. To be updated only by the customer who owns the virtual circuit.""")
@cli_util.option('--cross-connect-mappings', type=custom_types.CLI_COMPLEX_TYPE, help="""An array of mappings, each containing properties for a cross-connect or cross-connect group associated with this virtual circuit.

The customer and provider can update different properties in the mapping depending on the situation. See the description of the [CrossConnectMapping].

This option is a JSON list with items of type CrossConnectMapping.  For documentation on CrossConnectMapping please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/CrossConnectMapping.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--customer-bgp-asn', type=click.INT, help="""The BGP ASN of the network at the other end of the BGP session from Oracle.

If the BGP session is from the customer's edge router to Oracle, the required value is the customer's ASN, and it can be updated only by the customer.

If the BGP session is from the provider's edge router to Oracle, the required value is the provider's ASN, and it can be updated only by the provider.""")
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique. Avoid entering confidential information.

To be updated only by the customer who owns the virtual circuit.""")
@cli_util.option('--gateway-id', help="""The OCID of the [dynamic routing gateway (DRG)] that this private virtual circuit uses.

To be updated only by the customer who owns the virtual circuit.""")
@cli_util.option('--provider-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), help="""The provider's state in relation to this virtual circuit. Relevant only if the customer is using FastConnect via a provider.  ACTIVE means the provider has provisioned the virtual circuit from their end. INACTIVE means the provider has not yet provisioned the virtual circuit, or has de-provisioned it.

To be updated only by the provider.""")
@cli_util.option('--reference-comment', help="""Provider-supplied reference information about this virtual circuit. Relevant only if the customer is using FastConnect via a provider.

To be updated only by the provider.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_PROVIDER", "VERIFYING", "PROVISIONING", "PROVISIONED", "FAILED", "INACTIVE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'cross-connect-mappings': {'module': 'core', 'class': 'list[CrossConnectMapping]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'cross-connect-mappings': {'module': 'core', 'class': 'list[CrossConnectMapping]'}}, output_type={'module': 'core', 'class': 'VirtualCircuit'})
@cli_util.wrap_exceptions
def update_virtual_circuit(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_circuit_id, bandwidth_shape_name, cross_connect_mappings, customer_bgp_asn, display_name, gateway_id, provider_state, reference_comment, if_match):

    if isinstance(virtual_circuit_id, six.string_types) and len(virtual_circuit_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-circuit-id cannot be whitespace or empty string')
    if not force:
        if cross_connect_mappings:
            if not click.confirm("WARNING: Updates to cross-connect-mappings will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if bandwidth_shape_name is not None:
        details['bandwidthShapeName'] = bandwidth_shape_name

    if cross_connect_mappings is not None:
        details['crossConnectMappings'] = cli_util.parse_json_parameter("cross_connect_mappings", cross_connect_mappings)

    if customer_bgp_asn is not None:
        details['customerBgpAsn'] = customer_bgp_asn

    if display_name is not None:
        details['displayName'] = display_name

    if gateway_id is not None:
        details['gatewayId'] = gateway_id

    if provider_state is not None:
        details['providerState'] = provider_state

    if reference_comment is not None:
        details['referenceComment'] = reference_comment

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_virtual_circuit(
        virtual_circuit_id=virtual_circuit_id,
        update_virtual_circuit_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_virtual_circuit') and callable(getattr(client, 'get_virtual_circuit')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_virtual_circuit(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vnic_group.command(name=cli_util.override('update_vnic.command_name', 'update'), help="""Updates the specified VNIC.""")
@cli_util.option('--vnic-id', required=True, help="""The OCID of the VNIC.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostname-label', help="""The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952] and [RFC 1123]. The value appears in the [Vnic] object and also the [PrivateIp] object returned by [ListPrivateIps] and [GetPrivateIp].

For more information, see [DNS in Your Virtual Cloud Network].""")
@cli_util.option('--skip-source-dest-check', type=click.BOOL, help="""Whether the source/destination check is disabled on the VNIC. Defaults to `false`, which means the check is performed. For information about why you would skip the source/destination check, see [Using a Private IP as a Route Target].

Example: `true`""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Vnic'})
@cli_util.wrap_exceptions
def update_vnic(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, vnic_id, defined_tags, display_name, freeform_tags, hostname_label, skip_source_dest_check, if_match):

    if isinstance(vnic_id, six.string_types) and len(vnic_id.strip()) == 0:
        raise click.UsageError('Parameter --vnic-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if hostname_label is not None:
        details['hostnameLabel'] = hostname_label

    if skip_source_dest_check is not None:
        details['skipSourceDestCheck'] = skip_source_dest_check

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_vnic(
        vnic_id=vnic_id,
        update_vnic_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_vnic') and callable(getattr(client, 'get_vnic')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vnic(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
