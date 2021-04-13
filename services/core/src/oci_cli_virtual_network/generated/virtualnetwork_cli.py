# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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
from services.core.src.oci_cli_core.generated import core_service_cli


@click.command(cli_util.override('virtual_network.virtual_network_root_group.command_name', 'virtual-network'), cls=CommandGroupWithAlias, help=cli_util.override('virtual_network.virtual_network_root_group.help', """API covering the [Networking],
[Compute], and
[Block Volume] services. Use this API
to manage resources such as virtual cloud networks (VCNs), compute instances, and
block storage volumes."""), short_help=cli_util.override('virtual_network.virtual_network_root_group.short_help', """Core Services API"""))
@cli_util.help_option_group
def virtual_network_root_group():
    pass


@click.command(cli_util.override('virtual_network.subnet_group.command_name', 'subnet'), cls=CommandGroupWithAlias, help="""A logical subdivision of a VCN. Each subnet consists of a contiguous range of IP addresses that do not overlap with other subnets in the VCN. Example: 172.16.1.0/24. For more information, see [Overview of the Networking Service] and [VCNs and Subnets].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def subnet_group():
    pass


@click.command(cli_util.override('virtual_network.public_ip_group.command_name', 'public-ip'), cls=CommandGroupWithAlias, help="""A *public IP* is a conceptual term that refers to a public IP address and related properties. The `publicIp` object is the API representation of a public IP.

There are two types of public IPs: 1. Ephemeral 2. Reserved

For more information and comparison of the two types, see [Public IP Addresses].""")
@cli_util.help_option_group
def public_ip_group():
    pass


@click.command(cli_util.override('virtual_network.ip_sec_connection_device_config_group.command_name', 'ip-sec-connection-device-config'), cls=CommandGroupWithAlias, help="""Deprecated. For tunnel information, instead see:

  * [IPSecConnectionTunnel]   * [IPSecConnectionTunnelSharedSecret]""")
@cli_util.help_option_group
def ip_sec_connection_device_config_group():
    pass


@click.command(cli_util.override('virtual_network.byoip_range_group.command_name', 'byoip-range'), cls=CommandGroupWithAlias, help="""Oracle offers the ability to Bring Your Own IP (BYOIP), importing public IP addresses that you currently own to Oracle Cloud Infrastructure. A `ByoipRange` resource is a record of the imported address block (a BYOIP CIDR block) and also some associated metadata. The process used to [Bring Your Own IP] is explained in the documentation.""")
@cli_util.help_option_group
def byoip_range_group():
    pass


@click.command(cli_util.override('virtual_network.fast_connect_provider_service_group.command_name', 'fast-connect-provider-service'), cls=CommandGroupWithAlias, help="""A service offering from a supported provider. For more information, see [FastConnect Overview].""")
@cli_util.help_option_group
def fast_connect_provider_service_group():
    pass


@click.command(cli_util.override('virtual_network.virtual_circuit_public_prefix_group.command_name', 'virtual-circuit-public-prefix'), cls=CommandGroupWithAlias, help="""A public IP prefix and its details. With a public virtual circuit, the customer specifies the customer-owned public IP prefixes to advertise across the connection. For more information, see [FastConnect Overview].""")
@cli_util.help_option_group
def virtual_circuit_public_prefix_group():
    pass


@click.command(cli_util.override('virtual_network.ip_sec_connection_tunnel_shared_secret_group.command_name', 'ip-sec-connection-tunnel-shared-secret'), cls=CommandGroupWithAlias, help="""The tunnel's shared secret (pre-shared key).""")
@cli_util.help_option_group
def ip_sec_connection_tunnel_shared_secret_group():
    pass


@click.command(cli_util.override('virtual_network.drg_group.command_name', 'drg'), cls=CommandGroupWithAlias, help="""A dynamic routing gateway (DRG) is a virtual router that provides a path for private network traffic between networks. You use it with other Networking Service components to create a connection to your on-premises network using [VPN Connect] or a connection that uses [FastConnect]. For more information, see [Overview of the Networking Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def drg_group():
    pass


@click.command(cli_util.override('virtual_network.cpe_group.command_name', 'cpe'), cls=CommandGroupWithAlias, help="""An object you create when setting up an IPSec VPN between your on-premises network and VCN. The `Cpe` is a virtual representation of your customer-premises equipment, which is the actual router on-premises at your site at your end of the IPSec VPN connection. For more information, see [Overview of the Networking Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def cpe_group():
    pass


@click.command(cli_util.override('virtual_network.cross_connect_group.command_name', 'cross-connect'), cls=CommandGroupWithAlias, help="""For use with Oracle Cloud Infrastructure FastConnect. A cross-connect represents a physical connection between an existing network and Oracle. Customers who are colocated with Oracle in a FastConnect location create and use cross-connects. For more information, see [FastConnect Overview].

Oracle recommends you create each cross-connect in a [CrossConnectGroup] so you can use link aggregation with the connection.

**Note:** If you're a provider who is setting up a physical connection to Oracle so customers can use FastConnect over the connection, be aware that your connection is modeled the same way as a colocated customer's (with `CrossConnect` and `CrossConnectGroup` objects, and so on).

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def cross_connect_group():
    pass


@click.command(cli_util.override('virtual_network.letter_of_authority_group.command_name', 'letter-of-authority'), cls=CommandGroupWithAlias, help="""The Letter of Authority for the cross-connect. You must submit this letter when requesting cabling for the cross-connect at the FastConnect location.""")
@cli_util.help_option_group
def letter_of_authority_group():
    pass


@click.command(cli_util.override('virtual_network.cross_connect_status_group.command_name', 'cross-connect-status'), cls=CommandGroupWithAlias, help="""The status of the cross-connect.""")
@cli_util.help_option_group
def cross_connect_status_group():
    pass


@click.command(cli_util.override('virtual_network.security_rule_group.command_name', 'security-rule'), cls=CommandGroupWithAlias, help="""A security rule is one of the items in a [NetworkSecurityGroup]. It is a virtual firewall rule for the VNICs in the network security group. A rule can be for either inbound (`direction`= INGRESS) or outbound (`direction`= EGRESS) IP packets.""")
@cli_util.help_option_group
def security_rule_group():
    pass


@click.command(cli_util.override('virtual_network.vcn_topology_group.command_name', 'vcn-topology'), cls=CommandGroupWithAlias, help="""Defines the representation of a virtual network topology for a VCN.""")
@cli_util.help_option_group
def vcn_topology_group():
    pass


@click.command(cli_util.override('virtual_network.cpe_device_shape_group.command_name', 'cpe-device-shape'), cls=CommandGroupWithAlias, help="""A summary of information about a particular CPE device type. Compare with [CpeDeviceShapeDetail].""")
@cli_util.help_option_group
def cpe_device_shape_group():
    pass


@click.command(cli_util.override('virtual_network.drg_route_rule_group.command_name', 'drg-route-rule'), cls=CommandGroupWithAlias, help="""A DRG route rule is a mapping between a destination IP address range and a DRG attachment. The map is used to route matching packets. Traffic will be routed across the attachments using Equal-cost multi-path routing (ECMP) if there are multiple rules with identical destinations and none of the rules conflict.""")
@cli_util.help_option_group
def drg_route_rule_group():
    pass


@click.command(cli_util.override('virtual_network.ip_sec_connection_device_status_group.command_name', 'ip-sec-connection-device-status'), cls=CommandGroupWithAlias, help="""Deprecated. For tunnel information, instead see [IPSecConnectionTunnel].""")
@cli_util.help_option_group
def ip_sec_connection_device_status_group():
    pass


@click.command(cli_util.override('virtual_network.cpe_device_shape_detail_group.command_name', 'cpe-device-shape-detail'), cls=CommandGroupWithAlias, help="""The detailed information about a particular CPE device type. Compare with [CpeDeviceShapeSummary].""")
@cli_util.help_option_group
def cpe_device_shape_detail_group():
    pass


@click.command(cli_util.override('virtual_network.fast_connect_provider_service_key_group.command_name', 'fast-connect-provider-service-key'), cls=CommandGroupWithAlias, help="""A provider service key and its details. A provider service key is an identifier for a provider's virtual circuit.""")
@cli_util.help_option_group
def fast_connect_provider_service_key_group():
    pass


@click.command(cli_util.override('virtual_network.drg_route_distribution_statement_group.command_name', 'drg-route-distribution-statement'), cls=CommandGroupWithAlias, help="""A single statement within a route distribution. All match criteria in a statement must be met for the action to take place.""")
@cli_util.help_option_group
def drg_route_distribution_statement_group():
    pass


@click.command(cli_util.override('virtual_network.drg_route_table_group.command_name', 'drg-route-table'), cls=CommandGroupWithAlias, help="""All routing inside the DRG is driven by the contents of DRG route tables. DRG route tables contain rules which route packets to a particular network destination, represented as a DRG attachment. The routing decision for a packet entering a DRG is determined by the rules in the DRG route table assigned to the attachment-of-entry.

Each DRG attachment can inject routes in any DRG route table, provided there is a statement corresponding to the attachment in the route table's `importDrgRouteDistribution`. You can also insert static routes into the DRG route tables.

The DRG route table is always in the same compartment as the DRG. There must always be a default DRG route table for each attachment type.""")
@cli_util.help_option_group
def drg_route_table_group():
    pass


@click.command(cli_util.override('virtual_network.internet_gateway_group.command_name', 'internet-gateway'), cls=CommandGroupWithAlias, help="""Represents a router that connects the edge of a VCN with the Internet. For an example scenario that uses an internet gateway, see [Typical Networking Service Scenarios].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def internet_gateway_group():
    pass


@click.command(cli_util.override('virtual_network.ip_sec_connection_group.command_name', 'ip-sec-connection'), cls=CommandGroupWithAlias, help="""A connection between a DRG and CPE. This connection consists of multiple IPSec tunnels. Creating this connection is one of the steps required when setting up an IPSec VPN.

**Important:**  Each tunnel in an IPSec connection can use either static routing or BGP dynamic routing (see the [IPSecConnectionTunnel] object's `routing` attribute). Originally only static routing was supported and every IPSec connection was required to have at least one static route configured. To maintain backward compatibility in the API when support for BPG dynamic routing was introduced, the API accepts an empty list of static routes if you configure both of the IPSec tunnels to use BGP dynamic routing. If you switch a tunnel's routing from `BGP` to `STATIC`, you must first ensure that the IPSec connection is configured with at least one valid CIDR block static route. Oracle uses the IPSec connection's static routes when routing a tunnel's traffic *only* if that tunnel's `routing` attribute = `STATIC`. Otherwise the static routes are ignored.

For more information about the workflow for setting up an IPSec connection, see [IPSec VPN].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def ip_sec_connection_group():
    pass


@click.command(cli_util.override('virtual_network.network_security_group_group.command_name', 'network-security-group'), cls=CommandGroupWithAlias, help="""A *network security group* (NSG) provides virtual firewall rules for a specific set of [VNICs] in a VCN. Compare NSGs with [SecurityLists], which provide virtual firewall rules to all the VNICs in a *subnet*.

A network security group consists of two items:

  * The set of [VNICs] that all have the same security rule needs (for     example, a group of Compute instances all running the same application)   * A set of NSG [SecurityRules] that apply to the VNICs in the group

After creating an NSG, you can add VNICs and security rules to it. For example, when you create an instance, you can specify one or more NSGs to add the instance to (see [CreateVnicDetails]). Or you can add an existing instance to an NSG with [UpdateVnic].

To add security rules to an NSG, see [AddNetworkSecurityGroupSecurityRules].

To list the VNICs in an NSG, see [ListNetworkSecurityGroupVnics].

To list the security rules in an NSG, see [ListNetworkSecurityGroupSecurityRules].

For more information about network security groups, see [Network Security Groups].

**Important:** Oracle Cloud Infrastructure Compute service images automatically include firewall rules (for example, Linux iptables, Windows firewall). If there are issues with some type of access to an instance, make sure all of the following are set correctly:

  * Any security rules in any NSGs the instance's VNIC belongs to   * Any [SecurityLists] associated with the instance's subnet   * The instance's OS firewall rules

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def network_security_group_group():
    pass


@click.command(cli_util.override('virtual_network.security_list_group.command_name', 'security-list'), cls=CommandGroupWithAlias, help="""A set of virtual firewall rules for your VCN. Security lists are configured at the subnet level, but the rules are applied to the ingress and egress traffic for the individual instances in the subnet. The rules can be stateful or stateless. For more information, see [Security Lists]. **Note:** Compare security lists to [NetworkSecurityGroup]s, which let you apply a set of security rules to a *specific set of VNICs* instead of an entire subnet. Oracle recommends using network security groups instead of security lists, although you can use either or both together.

**Important:** Oracle Cloud Infrastructure Compute service images automatically include firewall rules (for example, Linux iptables, Windows firewall). If there are issues with some type of access to an instance, make sure both the security lists associated with the instance's subnet and the instance's firewall rules are set correctly.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def security_list_group():
    pass


@click.command(cli_util.override('virtual_network.byoip_allocated_range_summary_group.command_name', 'byoip-allocated-range-summary'), cls=CommandGroupWithAlias, help="""A summary of CIDR block subranges that are currently allocated to an IP pool.""")
@cli_util.help_option_group
def byoip_allocated_range_summary_group():
    pass


@click.command(cli_util.override('virtual_network.remote_peering_connection_group.command_name', 'remote-peering-connection'), cls=CommandGroupWithAlias, help="""A remote peering connection (RPC) is an object on a DRG that lets the VCN that is attached to the DRG peer with a VCN in a different region. *Peering* means that the two VCNs can communicate using private IP addresses, but without the traffic traversing the internet or routing through your on-premises network. For more information, see [VCN Peering].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def remote_peering_connection_group():
    pass


@click.command(cli_util.override('virtual_network.nat_gateway_group.command_name', 'nat-gateway'), cls=CommandGroupWithAlias, help="""A NAT (Network Address Translation) gateway, which represents a router that lets instances without public IPs contact the public internet without exposing the instance to inbound internet traffic. For more information, see [NAT Gateway].

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def nat_gateway_group():
    pass


@click.command(cli_util.override('virtual_network.drg_attachment_group.command_name', 'drg-attachment'), cls=CommandGroupWithAlias, help="""A DRG attachment serves as a link between a DRG and a network resource. A DRG can be attached to a VCN, IPSec tunnel, remote peering connection, or virtual circuit.

For more information, see [Overview of the Networking Service].""")
@cli_util.help_option_group
def drg_attachment_group():
    pass


@click.command(cli_util.override('virtual_network.networking_topology_group.command_name', 'networking-topology'), cls=CommandGroupWithAlias, help="""Defines the representation of a virtual network topology for a region.""")
@cli_util.help_option_group
def networking_topology_group():
    pass


@click.command(cli_util.override('virtual_network.ip_sec_connection_tunnel_group.command_name', 'ip-sec-connection-tunnel'), cls=CommandGroupWithAlias, help="""Information about a single tunnel in an IPSec connection. This object does not include the tunnel's shared secret (pre-shared key). That is in the [IPSecConnectionTunnelSharedSecret] object.""")
@cli_util.help_option_group
def ip_sec_connection_tunnel_group():
    pass


@click.command(cli_util.override('virtual_network.vcn_dns_resolver_association_group.command_name', 'vcn-dns-resolver-association'), cls=CommandGroupWithAlias, help="""The information about the VCN and the DNS resolver in the association.""")
@cli_util.help_option_group
def vcn_dns_resolver_association_group():
    pass


@click.command(cli_util.override('virtual_network.cross_connect_location_group.command_name', 'cross-connect-location'), cls=CommandGroupWithAlias, help="""An individual FastConnect location.""")
@cli_util.help_option_group
def cross_connect_location_group():
    pass


@click.command(cli_util.override('virtual_network.private_ip_group.command_name', 'private-ip'), cls=CommandGroupWithAlias, help="""A *private IP* is a conceptual term that refers to an IPv4 private IP address and related properties. The `privateIp` object is the API representation of a private IP.

**Note:** For information about IPv6 addresses, see [Ipv6].

Each instance has a *primary private IP* that is automatically created and assigned to the primary VNIC during instance launch. If you add a secondary VNIC to the instance, it also automatically gets a primary private IP. You can't remove a primary private IP from its VNIC. The primary private IP is automatically deleted when the VNIC is terminated.

You can add *secondary private IPs* to a VNIC after it's created. For more information, see the `privateIp` operations and also [IP Addresses].

**Note:** Only [ListPrivateIps] and [GetPrivateIp] work with *primary* private IPs. To create and update primary private IPs, you instead work with instance and VNIC operations. For example, a primary private IP's properties come from the values you specify in [CreateVnicDetails] when calling either [LaunchInstance] or [AttachVnic]. To update the hostname for a primary private IP, you use [UpdateVnic].

`PrivateIp` objects that are created for use with the Oracle Cloud VMware Solution are assigned to a VLAN and not a VNIC in a subnet. See the descriptions of the relevant attributes in the `PrivateIp` object. Also see [Vlan].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def private_ip_group():
    pass


@click.command(cli_util.override('virtual_network.virtual_circuit_group.command_name', 'virtual-circuit'), cls=CommandGroupWithAlias, help="""For use with Oracle Cloud Infrastructure FastConnect.

A virtual circuit is an isolated network path that runs over one or more physical network connections to provide a single, logical connection between the edge router on the customer's existing network and Oracle Cloud Infrastructure. *Private* virtual circuits support private peering, and *public* virtual circuits support public peering. For more information, see [FastConnect Overview].

Each virtual circuit is made up of information shared between a customer, Oracle, and a provider (if the customer is using FastConnect via a provider). Who fills in a given property of a virtual circuit depends on whether the BGP session related to that virtual circuit goes from the customer's edge router to Oracle, or from the provider's edge router to Oracle. Also, in the case where the customer is using a provider, values for some of the properties may not be present immediately, but may get filled in as the provider and Oracle each do their part to provision the virtual circuit.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def virtual_circuit_group():
    pass


@click.command(cli_util.override('virtual_network.local_peering_gateway_group.command_name', 'local-peering-gateway'), cls=CommandGroupWithAlias, help="""A local peering gateway (LPG) is an object on a VCN that lets that VCN peer with another VCN in the same region. *Peering* means that the two VCNs can communicate using private IP addresses, but without the traffic traversing the internet or routing through your on-premises network. For more information, see [VCN Peering].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def local_peering_gateway_group():
    pass


@click.command(cli_util.override('virtual_network.cross_connect_mapping_details_collection_group.command_name', 'cross-connect-mapping-details-collection'), cls=CommandGroupWithAlias, help="""An array of CrossConnectMappingDetails""")
@cli_util.help_option_group
def cross_connect_mapping_details_collection_group():
    pass


@click.command(cli_util.override('virtual_network.tunnel_cpe_device_config_group.command_name', 'tunnel-cpe-device-config'), cls=CommandGroupWithAlias, help="""The set of CPE configuration answers for the tunnel, which the customer provides in [UpdateTunnelCpeDeviceConfig]. The answers correlate to the questions that are specific to the CPE device type (see the `parameters` attribute of [CpeDeviceShapeDetail]).

See these related operations:

  * [GetTunnelCpeDeviceConfig]   * [GetTunnelCpeDeviceConfigContent]   * [GetIpsecCpeDeviceConfigContent]   * [GetCpeDeviceConfigContent]""")
@cli_util.help_option_group
def tunnel_cpe_device_config_group():
    pass


@click.command(cli_util.override('virtual_network.vlan_group.command_name', 'vlan'), cls=CommandGroupWithAlias, help="""A resource to be used only with the Oracle Cloud VMware Solution.

Conceptually, a virtual LAN (VLAN) is a broadcast domain that is created by partitioning and isolating a network at the data link layer (a *layer 2 network*). VLANs work by using IEEE 802.1Q VLAN tags. Layer 2 traffic is forwarded within the VLAN based on MAC learning.

In the Networking service, a VLAN is an object within a VCN. You use VLANs to partition the VCN at the data link layer (layer 2). A VLAN is analagous to a subnet, which is an object for partitioning the VCN at the IP layer (layer 3).""")
@cli_util.help_option_group
def vlan_group():
    pass


@click.command(cli_util.override('virtual_network.ipv6_group.command_name', 'ipv6'), cls=CommandGroupWithAlias, help="""An *IPv6* is a conceptual term that refers to an IPv6 address and related properties. The `IPv6` object is the API representation of an IPv6.

You can create and assign an IPv6 to any VNIC that is in an IPv6-enabled subnet in an IPv6-enabled VCN.

**Note:** IPv6 addressing is supported for all commercial and government regions. For important details about IPv6 addressing in a VCN, see [IPv6 Addresses].""")
@cli_util.help_option_group
def ipv6_group():
    pass


@click.command(cli_util.override('virtual_network.cross_connect_port_speed_shape_group.command_name', 'cross-connect-port-speed-shape'), cls=CommandGroupWithAlias, help="""An individual port speed level for cross-connects.""")
@cli_util.help_option_group
def cross_connect_port_speed_shape_group():
    pass


@click.command(cli_util.override('virtual_network.public_ip_pool_group.command_name', 'public-ip-pool'), cls=CommandGroupWithAlias, help="""A public IP pool is a set of public IP addresses represented as one or more IPv4 CIDR blocks. Resources like load balancers and compute instances can be allocated public IP addresses from a public IP pool.""")
@cli_util.help_option_group
def public_ip_pool_group():
    pass


@click.command(cli_util.override('virtual_network.route_table_group.command_name', 'route-table'), cls=CommandGroupWithAlias, help="""A collection of `RouteRule` objects, which are used to route packets based on destination IP to a particular network entity. For more information, see [Overview of the Networking Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def route_table_group():
    pass


@click.command(cli_util.override('virtual_network.vcn_group.command_name', 'vcn'), cls=CommandGroupWithAlias, help="""A virtual cloud network (VCN). For more information, see [Overview of the Networking Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def vcn_group():
    pass


@click.command(cli_util.override('virtual_network.network_security_group_vnic_group.command_name', 'network-security-group-vnic'), cls=CommandGroupWithAlias, help="""Information about a VNIC that belongs to a network security group.""")
@cli_util.help_option_group
def network_security_group_vnic_group():
    pass


@click.command(cli_util.override('virtual_network.vnic_group.command_name', 'vnic'), cls=CommandGroupWithAlias, help="""A virtual network interface card. Each VNIC resides in a subnet in a VCN. An instance attaches to a VNIC to obtain a network connection into the VCN through that subnet. Each instance has a *primary VNIC* that is automatically created and attached during launch. You can add *secondary VNICs* to an instance after it's launched. For more information, see [Virtual Network Interface Cards (VNICs)].

Each VNIC has a *primary private IP* that is automatically assigned during launch. You can add *secondary private IPs* to a VNIC after it's created. For more information, see [CreatePrivateIp] and [IP Addresses].

 If you are an Oracle Cloud VMware Solution customer, you will have secondary VNICs that reside in a VLAN instead of a subnet. These VNICs have other differences, which are called out in the descriptions of the relevant attributes in the `Vnic` object. Also see [Vlan].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def vnic_group():
    pass


@click.command(cli_util.override('virtual_network.dhcp_options_group.command_name', 'dhcp-options'), cls=CommandGroupWithAlias, help="""A set of DHCP options. Used by the VCN to automatically provide configuration information to the instances when they boot up. There are two options you can set:

- [DhcpDnsOption]: Lets you specify how DNS (hostname resolution) is handled in the subnets in your VCN.

- [DhcpSearchDomainOption]: Lets you specify a search domain name to use for DNS queries.

For more information, see  [DNS in Your Virtual Cloud Network] and [DHCP Options].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def dhcp_options_group():
    pass


@click.command(cli_util.override('virtual_network.virtual_circuit_bandwidth_shape_group.command_name', 'virtual-circuit-bandwidth-shape'), cls=CommandGroupWithAlias, help="""An individual bandwidth level for virtual circuits.""")
@cli_util.help_option_group
def virtual_circuit_bandwidth_shape_group():
    pass


@click.command(cli_util.override('virtual_network.peer_region_for_remote_peering_group.command_name', 'peer-region-for-remote-peering'), cls=CommandGroupWithAlias, help="""Details about a region that supports remote VCN peering. For more information, see [VCN Peering].""")
@cli_util.help_option_group
def peer_region_for_remote_peering_group():
    pass


@click.command(cli_util.override('virtual_network.drg_route_distribution_group.command_name', 'drg-route-distribution'), cls=CommandGroupWithAlias, help="""A route distribution establishes how routes get imported into DRG route tables and exported through the DRG attachments.

A route distribution is a list of statements. Each statement consists of a set of matches, all of which must be `True` in order for the statement's action to take place. Each statement determines which routes are propagated.

You can assign a route distribution as a route table's import distribution. The statements in an import route distribution specify how how incoming route advertisements through a referenced attachment or all attachments of a certain type are inserted into the route table.

You can assign a route distribution as a DRG attachment's export distribution. Export route distribution statements specify how routes in a DRG attachment's assigned table are advertised out through the attachment. When a DRG attachment is created, a route distribution is created with a single ACCEPT statement with an empty match criteria (empty match criteria implies match ALL). Exporting routes through VCN attachments is unsupported, so no VCN attachments are assigned an export distribution.

The two auto-generated DRG route tables (one as the default for VCN attachments, and the other for all other types of attachments) are each assigned an auto generated import route distribution. The default VCN table's import distribution has a single statement with empty match criteria statement to import routes from each DRG attachment type. The other table's import distribution has a statement to import routes from attachments with the VCN type.

The route distribution is always in the same compartment as the DRG.""")
@cli_util.help_option_group
def drg_route_distribution_group():
    pass


@click.command(cli_util.override('virtual_network.service_gateway_group.command_name', 'service-gateway'), cls=CommandGroupWithAlias, help="""Represents a router that lets your VCN privately access specific Oracle services such as Object Storage without exposing the VCN to the public internet. Traffic leaving the VCN and destined for a supported Oracle service (see [ListServices]) is routed through the service gateway and does not traverse the internet. The instances in the VCN do not need to have public IP addresses nor be in a public subnet. The VCN does not need an internet gateway for this traffic. For more information, see [Access to Oracle Services: Service Gateway].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def service_gateway_group():
    pass


@click.command(cli_util.override('virtual_network.service_group.command_name', 'service'), cls=CommandGroupWithAlias, help="""An object that represents one or multiple Oracle services that you can enable for a [ServiceGateway]. In the User Guide topic [Access to Oracle Services: Service Gateway], the term *service CIDR label* is used to refer to the string that represents the regional public IP address ranges of the Oracle service or services covered by a given `Service` object. That unique string is the value of the `Service` object's `cidrBlock` attribute.""")
@cli_util.help_option_group
def service_group():
    pass


@click.command(cli_util.override('virtual_network.cross_connect_group_group.command_name', 'cross-connect-group'), cls=CommandGroupWithAlias, help="""For use with Oracle Cloud Infrastructure FastConnect. A cross-connect group is a link aggregation group (LAG), which can contain one or more [CrossConnects]. Customers who are colocated with Oracle in a FastConnect location create and use cross-connect groups. For more information, see [FastConnect Overview].

**Note:** If you're a provider who is setting up a physical connection to Oracle so customers can use FastConnect over the connection, be aware that your connection is modeled the same way as a colocated customer's (with `CrossConnect` and `CrossConnectGroup` objects, and so on).

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def cross_connect_group_group():
    pass


@click.command(cli_util.override('virtual_network.drg_redundancy_status_group.command_name', 'drg-redundancy-status'), cls=CommandGroupWithAlias, help="""The redundancy status of the DRG. For more information, see [Redundancy Remedies].""")
@cli_util.help_option_group
def drg_redundancy_status_group():
    pass


@click.command(cli_util.override('virtual_network.internal_public_ip_group.command_name', 'internal-public-ip'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def internal_public_ip_group():
    pass


core_service_cli.core_service_group.add_command(virtual_network_root_group)
virtual_network_root_group.add_command(subnet_group)
virtual_network_root_group.add_command(public_ip_group)
virtual_network_root_group.add_command(ip_sec_connection_device_config_group)
virtual_network_root_group.add_command(byoip_range_group)
virtual_network_root_group.add_command(fast_connect_provider_service_group)
virtual_network_root_group.add_command(virtual_circuit_public_prefix_group)
virtual_network_root_group.add_command(ip_sec_connection_tunnel_shared_secret_group)
virtual_network_root_group.add_command(drg_group)
virtual_network_root_group.add_command(cpe_group)
virtual_network_root_group.add_command(cross_connect_group)
virtual_network_root_group.add_command(letter_of_authority_group)
virtual_network_root_group.add_command(cross_connect_status_group)
virtual_network_root_group.add_command(security_rule_group)
virtual_network_root_group.add_command(vcn_topology_group)
virtual_network_root_group.add_command(cpe_device_shape_group)
virtual_network_root_group.add_command(drg_route_rule_group)
virtual_network_root_group.add_command(ip_sec_connection_device_status_group)
virtual_network_root_group.add_command(cpe_device_shape_detail_group)
virtual_network_root_group.add_command(fast_connect_provider_service_key_group)
virtual_network_root_group.add_command(drg_route_distribution_statement_group)
virtual_network_root_group.add_command(drg_route_table_group)
virtual_network_root_group.add_command(internet_gateway_group)
virtual_network_root_group.add_command(ip_sec_connection_group)
virtual_network_root_group.add_command(network_security_group_group)
virtual_network_root_group.add_command(security_list_group)
virtual_network_root_group.add_command(byoip_allocated_range_summary_group)
virtual_network_root_group.add_command(remote_peering_connection_group)
virtual_network_root_group.add_command(nat_gateway_group)
virtual_network_root_group.add_command(drg_attachment_group)
virtual_network_root_group.add_command(networking_topology_group)
virtual_network_root_group.add_command(ip_sec_connection_tunnel_group)
virtual_network_root_group.add_command(vcn_dns_resolver_association_group)
virtual_network_root_group.add_command(cross_connect_location_group)
virtual_network_root_group.add_command(private_ip_group)
virtual_network_root_group.add_command(virtual_circuit_group)
virtual_network_root_group.add_command(local_peering_gateway_group)
virtual_network_root_group.add_command(cross_connect_mapping_details_collection_group)
virtual_network_root_group.add_command(tunnel_cpe_device_config_group)
virtual_network_root_group.add_command(vlan_group)
virtual_network_root_group.add_command(ipv6_group)
virtual_network_root_group.add_command(cross_connect_port_speed_shape_group)
virtual_network_root_group.add_command(public_ip_pool_group)
virtual_network_root_group.add_command(route_table_group)
virtual_network_root_group.add_command(vcn_group)
virtual_network_root_group.add_command(network_security_group_vnic_group)
virtual_network_root_group.add_command(vnic_group)
virtual_network_root_group.add_command(dhcp_options_group)
virtual_network_root_group.add_command(virtual_circuit_bandwidth_shape_group)
virtual_network_root_group.add_command(peer_region_for_remote_peering_group)
virtual_network_root_group.add_command(drg_route_distribution_group)
virtual_network_root_group.add_command(service_gateway_group)
virtual_network_root_group.add_command(service_group)
virtual_network_root_group.add_command(cross_connect_group_group)
virtual_network_root_group.add_command(drg_redundancy_status_group)
virtual_network_root_group.add_command(internal_public_ip_group)


@drg_route_distribution_statement_group.command(name=cli_util.override('virtual_network.add_drg_route_distribution_statements.command_name', 'add'), help=u"""Adds one or more route distribution statements to the specified route distribution. \n[Command Reference](addDrgRouteDistributionStatements)""")
@cli_util.option('--drg-route-distribution-id', required=True, help=u"""The [OCID] of the route distribution.""")
@cli_util.option('--statements', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The collection of route distribution statements to insert into the route distribution.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'statements': {'module': 'core', 'class': 'list[AddDrgRouteDistributionStatementDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'statements': {'module': 'core', 'class': 'list[AddDrgRouteDistributionStatementDetails]'}}, output_type={'module': 'core', 'class': 'list[DrgRouteDistributionStatement]'})
@cli_util.wrap_exceptions
def add_drg_route_distribution_statements(ctx, from_json, drg_route_distribution_id, statements):

    if isinstance(drg_route_distribution_id, six.string_types) and len(drg_route_distribution_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-route-distribution-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}
    _details['statements'] = cli_util.parse_json_parameter("statements", statements)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.add_drg_route_distribution_statements(
        drg_route_distribution_id=drg_route_distribution_id,
        add_drg_route_distribution_statements_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@drg_route_rule_group.command(name=cli_util.override('virtual_network.add_drg_route_rules.command_name', 'add'), help=u"""Adds one or more static route rules to the specified DRG route table. \n[Command Reference](addDrgRouteRules)""")
@cli_util.option('--drg-route-table-id', required=True, help=u"""The [OCID] of the DRG route table.""")
@cli_util.option('--route-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The collection of static rules used to insert routes into the DRG route table.

This option is a JSON list with items of type AddDrgRouteRuleDetails.  For documentation on AddDrgRouteRuleDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/AddDrgRouteRuleDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'route-rules': {'module': 'core', 'class': 'list[AddDrgRouteRuleDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'route-rules': {'module': 'core', 'class': 'list[AddDrgRouteRuleDetails]'}}, output_type={'module': 'core', 'class': 'list[DrgRouteRule]'})
@cli_util.wrap_exceptions
def add_drg_route_rules(ctx, from_json, drg_route_table_id, route_rules):

    if isinstance(drg_route_table_id, six.string_types) and len(drg_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-route-table-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}

    if route_rules is not None:
        _details['routeRules'] = cli_util.parse_json_parameter("route_rules", route_rules)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.add_drg_route_rules(
        drg_route_table_id=drg_route_table_id,
        add_drg_route_rules_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vcn_group.command(name=cli_util.override('virtual_network.add_ipv6_vcn_cidr.command_name', 'add'), help=u"""Add an IPv6 CIDR to a VCN. The VCN size is always /56 and assigned by Oracle. Once added the IPv6 CIDR block cannot be removed or modified. \n[Command Reference](addIpv6VcnCidr)""")
@cli_util.option('--vcn-id', required=True, help=u"""The [OCID] of the VCN.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def add_ipv6_vcn_cidr(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vcn_id, if_match):

    if isinstance(vcn_id, six.string_types) and len(vcn_id.strip()) == 0:
        raise click.UsageError('Parameter --vcn-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.add_ipv6_vcn_cidr(
        vcn_id=vcn_id,
        **kwargs
    )
    work_request_client = cli_util.build_client('work_requests', 'work_request', ctx)
    if wait_for_state:

        if hasattr(work_request_client, 'get_work_request') and callable(getattr(work_request_client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(work_request_client, work_request_client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
                if hasattr(result, "data") and hasattr(result.data, "resources") and len(result.data.resources) == 1:
                    entity_type = result.data.resources[0].entity_type
                    identifier = result.data.resources[0].identifier
                    get_operation = 'get_' + entity_type
                    if hasattr(client, get_operation) and callable(getattr(client, get_operation)):
                        result = getattr(client, get_operation)(identifier)

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


@security_rule_group.command(name=cli_util.override('virtual_network.add_network_security_group_security_rules.command_name', 'add'), help=u"""Adds one or more security rules to the specified network security group. \n[Command Reference](addNetworkSecurityGroupSecurityRules)""")
@cli_util.option('--network-security-group-id', required=True, help=u"""The [OCID] of the network security group.""")
@cli_util.option('--security-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The NSG security rules to add.

This option is a JSON list with items of type AddSecurityRuleDetails.  For documentation on AddSecurityRuleDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/AddSecurityRuleDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'security-rules': {'module': 'core', 'class': 'list[AddSecurityRuleDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'security-rules': {'module': 'core', 'class': 'list[AddSecurityRuleDetails]'}}, output_type={'module': 'core', 'class': 'AddedNetworkSecurityGroupSecurityRules'})
@cli_util.wrap_exceptions
def add_network_security_group_security_rules(ctx, from_json, network_security_group_id, security_rules):

    if isinstance(network_security_group_id, six.string_types) and len(network_security_group_id.strip()) == 0:
        raise click.UsageError('Parameter --network-security-group-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}

    if security_rules is not None:
        _details['securityRules'] = cli_util.parse_json_parameter("security_rules", security_rules)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.add_network_security_group_security_rules(
        network_security_group_id=network_security_group_id,
        add_network_security_group_security_rules_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_pool_group.command(name=cli_util.override('virtual_network.add_public_ip_pool_capacity.command_name', 'add'), help=u"""Adds some or all of a CIDR block to a public IP pool.

The CIDR block (or subrange) must not overlap with any other CIDR block already added to this or any other public IP pool. \n[Command Reference](addPublicIpPoolCapacity)""")
@cli_util.option('--public-ip-pool-id', required=True, help=u"""The [OCID] of the public IP pool.""")
@cli_util.option('--byoip-range-id', required=True, help=u"""The [OCID] of the `ByoipRange` resource to which the CIDR block belongs.""")
@cli_util.option('--cidr-block', required=True, help=u"""The CIDR block to add to the public IP pool. It could be all of the CIDR block identified in `byoipRangeId`, or a subrange. Example: `10.0.1.0/24`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["INACTIVE", "UPDATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PublicIpPool'})
@cli_util.wrap_exceptions
def add_public_ip_pool_capacity(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, public_ip_pool_id, byoip_range_id, cidr_block):

    if isinstance(public_ip_pool_id, six.string_types) and len(public_ip_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --public-ip-pool-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['byoipRangeId'] = byoip_range_id
    _details['cidrBlock'] = cidr_block

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.add_public_ip_pool_capacity(
        public_ip_pool_id=public_ip_pool_id,
        add_public_ip_pool_capacity_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_public_ip_pool') and callable(getattr(client, 'get_public_ip_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_public_ip_pool(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@vcn_group.command(name=cli_util.override('virtual_network.add_vcn_cidr.command_name', 'add'), help=u"""Adds a CIDR block to a VCN. The CIDR block you add:

- Must be valid. - Must not overlap with another CIDR block in the VCN, a CIDR block of a peered VCN, or the on-premises network CIDR block. - Must not exceed the limit of CIDR blocks allowed per VCN.

**Note:** Adding a CIDR block places your VCN in an updating state until the changes are complete. You cannot create or update the VCN's subnets, VLANs, LPGs, or route tables during this operation. The time to completion can take a few minutes. You can use the `GetWorkRequest` operation to check the status of the update. \n[Command Reference](addVcnCidr)""")
@cli_util.option('--vcn-id', required=True, help=u"""The [OCID] of the VCN.""")
@cli_util.option('--cidr-block', required=True, help=u"""The CIDR block to add.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def add_vcn_cidr(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vcn_id, cidr_block, if_match):

    if isinstance(vcn_id, six.string_types) and len(vcn_id.strip()) == 0:
        raise click.UsageError('Parameter --vcn-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['cidrBlock'] = cidr_block

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.add_vcn_cidr(
        vcn_id=vcn_id,
        add_vcn_cidr_details=_details,
        **kwargs
    )
    work_request_client = cli_util.build_client('work_requests', 'work_request', ctx)
    if wait_for_state:

        if hasattr(work_request_client, 'get_work_request') and callable(getattr(work_request_client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(work_request_client, work_request_client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
                if hasattr(result, "data") and hasattr(result.data, "resources") and len(result.data.resources) == 1:
                    entity_type = result.data.resources[0].entity_type
                    identifier = result.data.resources[0].identifier
                    get_operation = 'get_' + entity_type
                    if hasattr(client, get_operation) and callable(getattr(client, get_operation)):
                        result = getattr(client, get_operation)(identifier)

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


@byoip_range_group.command(name=cli_util.override('virtual_network.advertise_byoip_range.command_name', 'advertise'), help=u"""Begins BGP route advertisements for the BYOIP CIDR block you imported to the Oracle Cloud. The `ByoipRange` resource must be in the PROVISIONED state before the BYOIP CIDR block routes can be advertised with BGP. \n[Command Reference](advertiseByoipRange)""")
@cli_util.option('--byoip-range-id', required=True, help=u"""The [OCID] of the `ByoipRange` resource containing the BYOIP CIDR block.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def advertise_byoip_range(ctx, from_json, byoip_range_id):

    if isinstance(byoip_range_id, six.string_types) and len(byoip_range_id.strip()) == 0:
        raise click.UsageError('Parameter --byoip-range-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.advertise_byoip_range(
        byoip_range_id=byoip_range_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@service_gateway_group.command(name=cli_util.override('virtual_network.attach_service_id.command_name', 'attach'), help=u"""Adds the specified [Service] to the list of enabled `Service` objects for the specified gateway. You must also set up a route rule with the `cidrBlock` of the `Service` as the rule's destination and the service gateway as the rule's target. See [Route Table].

**Note:** The `AttachServiceId` operation is an easy way to add an individual `Service` to the service gateway. Compare it with [UpdateServiceGateway], which replaces the entire existing list of enabled `Service` objects with the list that you provide in the `Update` call. \n[Command Reference](attachServiceId)""")
@cli_util.option('--service-gateway-id', required=True, help=u"""The service gateway's [OCID].""")
@cli_util.option('--service-id', required=True, help=u"""The [OCID] of the [Service].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    _details = {}
    _details['serviceId'] = service_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.attach_service_id(
        service_gateway_id=service_gateway_id,
        attach_service_details=_details,
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


@virtual_circuit_public_prefix_group.command(name=cli_util.override('virtual_network.bulk_add_virtual_circuit_public_prefixes.command_name', 'bulk-add'), help=u"""Adds one or more customer public IP prefixes to the specified public virtual circuit. Use this operation (and not [UpdateVirtualCircuit]) to add prefixes to the virtual circuit. Oracle must verify the customer's ownership of each prefix before traffic for that prefix will flow across the virtual circuit. \n[Command Reference](bulkAddVirtualCircuitPublicPrefixes)""")
@cli_util.option('--virtual-circuit-id', required=True, help=u"""The [OCID] of the virtual circuit.""")
@cli_util.option('--public-prefixes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The public IP prefixes (CIDRs) to add to the public virtual circuit.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'public-prefixes': {'module': 'core', 'class': 'list[CreateVirtualCircuitPublicPrefixDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'public-prefixes': {'module': 'core', 'class': 'list[CreateVirtualCircuitPublicPrefixDetails]'}})
@cli_util.wrap_exceptions
def bulk_add_virtual_circuit_public_prefixes(ctx, from_json, virtual_circuit_id, public_prefixes):

    if isinstance(virtual_circuit_id, six.string_types) and len(virtual_circuit_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-circuit-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}
    _details['publicPrefixes'] = cli_util.parse_json_parameter("public_prefixes", public_prefixes)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.bulk_add_virtual_circuit_public_prefixes(
        virtual_circuit_id=virtual_circuit_id,
        bulk_add_virtual_circuit_public_prefixes_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@virtual_circuit_public_prefix_group.command(name=cli_util.override('virtual_network.bulk_delete_virtual_circuit_public_prefixes.command_name', 'bulk-delete'), help=u"""Removes one or more customer public IP prefixes from the specified public virtual circuit. Use this operation (and not [UpdateVirtualCircuit]) to remove prefixes from the virtual circuit. When the virtual circuit's state switches back to PROVISIONED, Oracle stops advertising the specified prefixes across the connection. \n[Command Reference](bulkDeleteVirtualCircuitPublicPrefixes)""")
@cli_util.option('--virtual-circuit-id', required=True, help=u"""The [OCID] of the virtual circuit.""")
@cli_util.option('--public-prefixes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The public IP prefixes (CIDRs) to remove from the public virtual circuit.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'public-prefixes': {'module': 'core', 'class': 'list[DeleteVirtualCircuitPublicPrefixDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'public-prefixes': {'module': 'core', 'class': 'list[DeleteVirtualCircuitPublicPrefixDetails]'}})
@cli_util.wrap_exceptions
def bulk_delete_virtual_circuit_public_prefixes(ctx, from_json, virtual_circuit_id, public_prefixes):

    if isinstance(virtual_circuit_id, six.string_types) and len(virtual_circuit_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-circuit-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}
    _details['publicPrefixes'] = cli_util.parse_json_parameter("public_prefixes", public_prefixes)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.bulk_delete_virtual_circuit_public_prefixes(
        virtual_circuit_id=virtual_circuit_id,
        bulk_delete_virtual_circuit_public_prefixes_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@byoip_range_group.command(name=cli_util.override('virtual_network.change_byoip_range_compartment.command_name', 'change-compartment'), help=u"""Moves a BYOIP CIDR block to a different compartment. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeByoipRangeCompartment)""")
@cli_util.option('--byoip-range-id', required=True, help=u"""The [OCID] of the `ByoipRange` resource containing the BYOIP CIDR block.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the destination compartment for the BYOIP CIDR block move.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_byoip_range_compartment(ctx, from_json, byoip_range_id, compartment_id):

    if isinstance(byoip_range_id, six.string_types) and len(byoip_range_id.strip()) == 0:
        raise click.UsageError('Parameter --byoip-range-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_byoip_range_compartment(
        byoip_range_id=byoip_range_id,
        change_byoip_range_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cpe_group.command(name=cli_util.override('virtual_network.change_cpe_compartment.command_name', 'change-compartment'), help=u"""Moves a CPE object into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeCpeCompartment)""")
@cli_util.option('--cpe-id', required=True, help=u"""The [OCID] of the CPE.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the CPE object to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_cpe_compartment(ctx, from_json, cpe_id, compartment_id):

    if isinstance(cpe_id, six.string_types) and len(cpe_id.strip()) == 0:
        raise click.UsageError('Parameter --cpe-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_cpe_compartment(
        cpe_id=cpe_id,
        change_cpe_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cross_connect_group.command(name=cli_util.override('virtual_network.change_cross_connect_compartment.command_name', 'change-compartment'), help=u"""Moves a cross-connect into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeCrossConnectCompartment)""")
@cli_util.option('--cross-connect-id', required=True, help=u"""The [OCID] of the cross-connect.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the cross-connect to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_cross_connect_compartment(ctx, from_json, cross_connect_id, compartment_id):

    if isinstance(cross_connect_id, six.string_types) and len(cross_connect_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_cross_connect_compartment(
        cross_connect_id=cross_connect_id,
        change_cross_connect_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cross_connect_group_group.command(name=cli_util.override('virtual_network.change_cross_connect_group_compartment.command_name', 'change-compartment'), help=u"""Moves a cross-connect group into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeCrossConnectGroupCompartment)""")
@cli_util.option('--cross-connect-group-id', required=True, help=u"""The [OCID] of the cross-connect group.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the cross-connect group to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_cross_connect_group_compartment(ctx, from_json, cross_connect_group_id, compartment_id):

    if isinstance(cross_connect_group_id, six.string_types) and len(cross_connect_group_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-group-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_cross_connect_group_compartment(
        cross_connect_group_id=cross_connect_group_id,
        change_cross_connect_group_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dhcp_options_group.command(name=cli_util.override('virtual_network.change_dhcp_options_compartment.command_name', 'change-compartment'), help=u"""Moves a set of DHCP options into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeDhcpOptionsCompartment)""")
@cli_util.option('--dhcp-id', required=True, help=u"""The [OCID] for the set of DHCP options.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the set of DHCP options to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_dhcp_options_compartment(ctx, from_json, dhcp_id, compartment_id):

    if isinstance(dhcp_id, six.string_types) and len(dhcp_id.strip()) == 0:
        raise click.UsageError('Parameter --dhcp-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_dhcp_options_compartment(
        dhcp_id=dhcp_id,
        change_dhcp_options_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@drg_group.command(name=cli_util.override('virtual_network.change_drg_compartment.command_name', 'change-compartment'), help=u"""Moves a DRG into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeDrgCompartment)""")
@cli_util.option('--drg-id', required=True, help=u"""The [[OCID]](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the DRG to.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_drg_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_id, compartment_id):

    if isinstance(drg_id, six.string_types) and len(drg_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_drg_compartment(
        drg_id=drg_id,
        change_drg_compartment_details=_details,
        **kwargs
    )
    work_request_client = cli_util.build_client('work_requests', 'work_request', ctx)
    if wait_for_state:

        if hasattr(work_request_client, 'get_work_request') and callable(getattr(work_request_client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(work_request_client, work_request_client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
                if hasattr(result, "data") and hasattr(result.data, "resources") and len(result.data.resources) == 1:
                    entity_type = result.data.resources[0].entity_type
                    identifier = result.data.resources[0].identifier
                    get_operation = 'get_' + entity_type
                    if hasattr(client, get_operation) and callable(getattr(client, get_operation)):
                        result = getattr(client, get_operation)(identifier)

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


@internet_gateway_group.command(name=cli_util.override('virtual_network.change_internet_gateway_compartment.command_name', 'change-compartment'), help=u"""Moves an internet gateway into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeInternetGatewayCompartment)""")
@cli_util.option('--ig-id', required=True, help=u"""The [OCID] of the internet gateway.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the internet gateway to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_internet_gateway_compartment(ctx, from_json, ig_id, compartment_id):

    if isinstance(ig_id, six.string_types) and len(ig_id.strip()) == 0:
        raise click.UsageError('Parameter --ig-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_internet_gateway_compartment(
        ig_id=ig_id,
        change_internet_gateway_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ip_sec_connection_group.command(name=cli_util.override('virtual_network.change_ip_sec_connection_compartment.command_name', 'change-compartment'), help=u"""Moves an IPSec connection into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeIPSecConnectionCompartment)""")
@cli_util.option('--ipsc-id', required=True, help=u"""The [OCID] of the IPSec connection.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the IPSec connection to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_ip_sec_connection_compartment(ctx, from_json, ipsc_id, compartment_id):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_ip_sec_connection_compartment(
        ipsc_id=ipsc_id,
        change_ip_sec_connection_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@local_peering_gateway_group.command(name=cli_util.override('virtual_network.change_local_peering_gateway_compartment.command_name', 'change-compartment'), help=u"""Moves a local peering gateway into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeLocalPeeringGatewayCompartment)""")
@cli_util.option('--local-peering-gateway-id', required=True, help=u"""The [OCID] of the local peering gateway.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the local peering gateway to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_local_peering_gateway_compartment(ctx, from_json, local_peering_gateway_id, compartment_id):

    if isinstance(local_peering_gateway_id, six.string_types) and len(local_peering_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --local-peering-gateway-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_local_peering_gateway_compartment(
        local_peering_gateway_id=local_peering_gateway_id,
        change_local_peering_gateway_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@nat_gateway_group.command(name=cli_util.override('virtual_network.change_nat_gateway_compartment.command_name', 'change-compartment'), help=u"""Moves a NAT gateway into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeNatGatewayCompartment)""")
@cli_util.option('--nat-gateway-id', required=True, help=u"""The NAT gateway's [OCID].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the NAT gateway to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_nat_gateway_compartment(ctx, from_json, nat_gateway_id, compartment_id):

    if isinstance(nat_gateway_id, six.string_types) and len(nat_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --nat-gateway-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_nat_gateway_compartment(
        nat_gateway_id=nat_gateway_id,
        change_nat_gateway_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@network_security_group_group.command(name=cli_util.override('virtual_network.change_network_security_group_compartment.command_name', 'change-compartment'), help=u"""Moves a network security group into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeNetworkSecurityGroupCompartment)""")
@cli_util.option('--network-security-group-id', required=True, help=u"""The [OCID] of the network security group.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the network security group to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_network_security_group_compartment(ctx, from_json, network_security_group_id, compartment_id):

    if isinstance(network_security_group_id, six.string_types) and len(network_security_group_id.strip()) == 0:
        raise click.UsageError('Parameter --network-security-group-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_network_security_group_compartment(
        network_security_group_id=network_security_group_id,
        change_network_security_group_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_group.command(name=cli_util.override('virtual_network.change_public_ip_compartment.command_name', 'change-compartment'), help=u"""Moves a public IP into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].

This operation applies only to reserved public IPs. Ephemeral public IPs always belong to the same compartment as their VNIC and move accordingly. \n[Command Reference](changePublicIpCompartment)""")
@cli_util.option('--public-ip-id', required=True, help=u"""The [OCID] of the public IP.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the public IP to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_public_ip_compartment(ctx, from_json, public_ip_id, compartment_id):

    if isinstance(public_ip_id, six.string_types) and len(public_ip_id.strip()) == 0:
        raise click.UsageError('Parameter --public-ip-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_public_ip_compartment(
        public_ip_id=public_ip_id,
        change_public_ip_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_pool_group.command(name=cli_util.override('virtual_network.change_public_ip_pool_compartment.command_name', 'change-compartment'), help=u"""Moves a public IP pool to a different compartment. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changePublicIpPoolCompartment)""")
@cli_util.option('--public-ip-pool-id', required=True, help=u"""The [OCID] of the public IP pool.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the destination compartment for the public IP pool move.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_public_ip_pool_compartment(ctx, from_json, public_ip_pool_id, compartment_id):

    if isinstance(public_ip_pool_id, six.string_types) and len(public_ip_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --public-ip-pool-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_public_ip_pool_compartment(
        public_ip_pool_id=public_ip_pool_id,
        change_public_ip_pool_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@remote_peering_connection_group.command(name=cli_util.override('virtual_network.change_remote_peering_connection_compartment.command_name', 'change-compartment'), help=u"""Moves a remote peering connection (RPC) into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeRemotePeeringConnectionCompartment)""")
@cli_util.option('--remote-peering-connection-id', required=True, help=u"""The [OCID] of the remote peering connection (RPC).""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the remote peering connection to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_remote_peering_connection_compartment(ctx, from_json, remote_peering_connection_id, compartment_id):

    if isinstance(remote_peering_connection_id, six.string_types) and len(remote_peering_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --remote-peering-connection-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_remote_peering_connection_compartment(
        remote_peering_connection_id=remote_peering_connection_id,
        change_remote_peering_connection_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@route_table_group.command(name=cli_util.override('virtual_network.change_route_table_compartment.command_name', 'change-compartment'), help=u"""Moves a route table into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeRouteTableCompartment)""")
@cli_util.option('--rt-id', required=True, help=u"""The [OCID] of the route table.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the route table to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_route_table_compartment(ctx, from_json, rt_id, compartment_id):

    if isinstance(rt_id, six.string_types) and len(rt_id.strip()) == 0:
        raise click.UsageError('Parameter --rt-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_route_table_compartment(
        rt_id=rt_id,
        change_route_table_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@security_list_group.command(name=cli_util.override('virtual_network.change_security_list_compartment.command_name', 'change-compartment'), help=u"""Moves a security list into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeSecurityListCompartment)""")
@cli_util.option('--security-list-id', required=True, help=u"""The [OCID] of the security list.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the security list to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_security_list_compartment(ctx, from_json, security_list_id, compartment_id):

    if isinstance(security_list_id, six.string_types) and len(security_list_id.strip()) == 0:
        raise click.UsageError('Parameter --security-list-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_security_list_compartment(
        security_list_id=security_list_id,
        change_security_list_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@service_gateway_group.command(name=cli_util.override('virtual_network.change_service_gateway_compartment.command_name', 'change-compartment'), help=u"""Moves a service gateway into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeServiceGatewayCompartment)""")
@cli_util.option('--service-gateway-id', required=True, help=u"""The service gateway's [OCID].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the service gateway to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_service_gateway_compartment(ctx, from_json, service_gateway_id, compartment_id):

    if isinstance(service_gateway_id, six.string_types) and len(service_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --service-gateway-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_service_gateway_compartment(
        service_gateway_id=service_gateway_id,
        change_service_gateway_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subnet_group.command(name=cli_util.override('virtual_network.change_subnet_compartment.command_name', 'change-compartment'), help=u"""Moves a subnet into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeSubnetCompartment)""")
@cli_util.option('--subnet-id', required=True, help=u"""The [OCID] of the subnet.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the subnet to.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_subnet_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, subnet_id, compartment_id):

    if isinstance(subnet_id, six.string_types) and len(subnet_id.strip()) == 0:
        raise click.UsageError('Parameter --subnet-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_subnet_compartment(
        subnet_id=subnet_id,
        change_subnet_compartment_details=_details,
        **kwargs
    )
    work_request_client = cli_util.build_client('work_requests', 'work_request', ctx)
    if wait_for_state:

        if hasattr(work_request_client, 'get_work_request') and callable(getattr(work_request_client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(work_request_client, work_request_client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
                if hasattr(result, "data") and hasattr(result.data, "resources") and len(result.data.resources) == 1:
                    entity_type = result.data.resources[0].entity_type
                    identifier = result.data.resources[0].identifier
                    get_operation = 'get_' + entity_type
                    if hasattr(client, get_operation) and callable(getattr(client, get_operation)):
                        result = getattr(client, get_operation)(identifier)

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


@vcn_group.command(name=cli_util.override('virtual_network.change_vcn_compartment.command_name', 'change-compartment'), help=u"""Moves a VCN into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeVcnCompartment)""")
@cli_util.option('--vcn-id', required=True, help=u"""The [OCID] of the VCN.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the VCN to.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_vcn_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vcn_id, compartment_id):

    if isinstance(vcn_id, six.string_types) and len(vcn_id.strip()) == 0:
        raise click.UsageError('Parameter --vcn-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_vcn_compartment(
        vcn_id=vcn_id,
        change_vcn_compartment_details=_details,
        **kwargs
    )
    work_request_client = cli_util.build_client('work_requests', 'work_request', ctx)
    if wait_for_state:

        if hasattr(work_request_client, 'get_work_request') and callable(getattr(work_request_client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(work_request_client, work_request_client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
                if hasattr(result, "data") and hasattr(result.data, "resources") and len(result.data.resources) == 1:
                    entity_type = result.data.resources[0].entity_type
                    identifier = result.data.resources[0].identifier
                    get_operation = 'get_' + entity_type
                    if hasattr(client, get_operation) and callable(getattr(client, get_operation)):
                        result = getattr(client, get_operation)(identifier)

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


@virtual_circuit_group.command(name=cli_util.override('virtual_network.change_virtual_circuit_compartment.command_name', 'change-compartment'), help=u"""Moves a virtual circuit into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeVirtualCircuitCompartment)""")
@cli_util.option('--virtual-circuit-id', required=True, help=u"""The [OCID] of the virtual circuit.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the virtual circuit to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_virtual_circuit_compartment(ctx, from_json, virtual_circuit_id, compartment_id):

    if isinstance(virtual_circuit_id, six.string_types) and len(virtual_circuit_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-circuit-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_virtual_circuit_compartment(
        virtual_circuit_id=virtual_circuit_id,
        change_virtual_circuit_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vlan_group.command(name=cli_util.override('virtual_network.change_vlan_compartment.command_name', 'change-compartment'), help=u"""Moves a VLAN into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeVlanCompartment)""")
@cli_util.option('--vlan-id', required=True, help=u"""The [OCID] of the VLAN.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the VLAN to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_vlan_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vlan_id, compartment_id, if_match):

    if isinstance(vlan_id, six.string_types) and len(vlan_id.strip()) == 0:
        raise click.UsageError('Parameter --vlan-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.change_vlan_compartment(
        vlan_id=vlan_id,
        change_vlan_compartment_details=_details,
        **kwargs
    )
    work_request_client = cli_util.build_client('work_requests', 'work_request', ctx)
    if wait_for_state:

        if hasattr(work_request_client, 'get_work_request') and callable(getattr(work_request_client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(work_request_client, work_request_client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
                if hasattr(result, "data") and hasattr(result.data, "resources") and len(result.data.resources) == 1:
                    entity_type = result.data.resources[0].entity_type
                    identifier = result.data.resources[0].identifier
                    get_operation = 'get_' + entity_type
                    if hasattr(client, get_operation) and callable(getattr(client, get_operation)):
                        result = getattr(client, get_operation)(identifier)

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


@local_peering_gateway_group.command(name=cli_util.override('virtual_network.connect_local_peering_gateways.command_name', 'connect'), help=u"""Connects this local peering gateway (LPG) to another one in the same region.

This operation must be called by the VCN administrator who is designated as the *requestor* in the peering relationship. The *acceptor* must implement an Identity and Access Management (IAM) policy that gives the requestor permission to connect to LPGs in the acceptor's compartment. Without that permission, this operation will fail. For more information, see [VCN Peering]. \n[Command Reference](connectLocalPeeringGateways)""")
@cli_util.option('--local-peering-gateway-id', required=True, help=u"""The [OCID] of the local peering gateway.""")
@cli_util.option('--peer-id', required=True, help=u"""The OCID of the LPG you want to peer with.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def connect_local_peering_gateways(ctx, from_json, local_peering_gateway_id, peer_id):

    if isinstance(local_peering_gateway_id, six.string_types) and len(local_peering_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --local-peering-gateway-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}
    _details['peerId'] = peer_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.connect_local_peering_gateways(
        local_peering_gateway_id=local_peering_gateway_id,
        connect_local_peering_gateways_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@remote_peering_connection_group.command(name=cli_util.override('virtual_network.connect_remote_peering_connections.command_name', 'connect'), help=u"""Connects this RPC to another one in a different region.

This operation must be called by the VCN administrator who is designated as the *requestor* in the peering relationship. The *acceptor* must implement an Identity and Access Management (IAM) policy that gives the requestor permission to connect to RPCs in the acceptor's compartment. Without that permission, this operation will fail. For more information, see [VCN Peering]. \n[Command Reference](connectRemotePeeringConnections)""")
@cli_util.option('--remote-peering-connection-id', required=True, help=u"""The [OCID] of the remote peering connection (RPC).""")
@cli_util.option('--peer-id', required=True, help=u"""The OCID of the RPC you want to peer with.""")
@cli_util.option('--peer-region-name', required=True, help=u"""The name of the region that contains the RPC you want to peer with.

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

    _details = {}
    _details['peerId'] = peer_id
    _details['peerRegionName'] = peer_region_name

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.connect_remote_peering_connections(
        remote_peering_connection_id=remote_peering_connection_id,
        connect_remote_peering_connections_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@byoip_range_group.command(name=cli_util.override('virtual_network.create_byoip_range.command_name', 'create'), help=u"""Creates a subrange of the BYOIP CIDR block. \n[Command Reference](createByoipRange)""")
@cli_util.option('--cidr-block', required=True, help=u"""The BYOIP CIDR block. You can assign some or all of it to a public IP pool after it is validated. Example: `10.0.1.0/24`""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the BYOIP CIDR block.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["INACTIVE", "UPDATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'ByoipRange'})
@cli_util.wrap_exceptions
def create_byoip_range(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, cidr_block, compartment_id, defined_tags, display_name, freeform_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['cidrBlock'] = cidr_block
    _details['compartmentId'] = compartment_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_byoip_range(
        create_byoip_range_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_byoip_range') and callable(getattr(client, 'get_byoip_range')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_byoip_range(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cpe_group.command(name=cli_util.override('virtual_network.create_cpe.command_name', 'create'), help=u"""Creates a new virtual customer-premises equipment (CPE) object in the specified compartment. For more information, see [IPSec VPNs].

For the purposes of access control, you must provide the [OCID] of the compartment where you want the CPE to reside. Notice that the CPE doesn't have to be in the same compartment as the IPSec connection or other Networking Service components. If you're not sure which compartment to use, put the CPE in the same compartment as the DRG. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You must provide the public IP address of your on-premises router. See [Configuring Your On-Premises Router for an IPSec VPN].

You may optionally specify a *display name* for the CPE, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information. \n[Command Reference](createCpe)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to contain the CPE.""")
@cli_util.option('--ip-address', required=True, help=u"""The public IP address of the on-premises router.

Example: `203.0.113.2`""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--cpe-device-shape-id', help=u"""The [OCID] of the CPE device type. You can provide a value if you want to later generate CPE device configuration content for IPSec connections that use this CPE. You can also call [UpdateCpe] later to provide a value. For a list of possible values, see [ListCpeDeviceShapes].

For more information about generating CPE device configuration content, see:

  * [GetCpeDeviceConfigContent]   * [GetIpsecCpeDeviceConfigContent]   * [GetTunnelCpeDeviceConfigContent]   * [GetTunnelCpeDeviceConfig]""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Cpe'})
@cli_util.wrap_exceptions
def create_cpe(ctx, from_json, compartment_id, ip_address, defined_tags, display_name, freeform_tags, cpe_device_shape_id):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['ipAddress'] = ip_address

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if cpe_device_shape_id is not None:
        _details['cpeDeviceShapeId'] = cpe_device_shape_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_cpe(
        create_cpe_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cross_connect_group.command(name=cli_util.override('virtual_network.create_cross_connect.command_name', 'create'), help=u"""Creates a new cross-connect. Oracle recommends you create each cross-connect in a [CrossConnectGroup] so you can use link aggregation with the connection.

After creating the `CrossConnect` object, you need to go the FastConnect location and request to have the physical cable installed. For more information, see [FastConnect Overview].

For the purposes of access control, you must provide the [OCID] of the compartment where you want the cross-connect to reside. If you're not sure which compartment to use, put the cross-connect in the same compartment with your VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the cross-connect. It does not have to be unique, and you can change it. Avoid entering confidential information. \n[Command Reference](createCrossConnect)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to contain the cross-connect.""")
@cli_util.option('--location-name', required=True, help=u"""The name of the FastConnect location where this cross-connect will be installed. To get a list of the available locations, see [ListCrossConnectLocations].

Example: `CyrusOne, Chandler, AZ`""")
@cli_util.option('--port-speed-shape-name', required=True, help=u"""The port speed for this cross-connect. To get a list of the available port speeds, see [ListCrossConnectPortSpeedShapes].

Example: `10 Gbps`""")
@cli_util.option('--cross-connect-group-id', help=u"""The OCID of the cross-connect group to put this cross-connect in.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--far-cross-connect-or-cross-connect-group-id', help=u"""If you already have an existing cross-connect or cross-connect group at this FastConnect location, and you want this new cross-connect to be on a different router (for the purposes of redundancy), provide the OCID of that existing cross-connect or cross-connect group.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--near-cross-connect-or-cross-connect-group-id', help=u"""If you already have an existing cross-connect or cross-connect group at this FastConnect location, and you want this new cross-connect to be on the same router, provide the OCID of that existing cross-connect or cross-connect group.""")
@cli_util.option('--customer-reference-name', help=u"""A reference name or identifier for the physical fiber connection that this cross-connect uses.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'CrossConnect'})
@cli_util.wrap_exceptions
def create_cross_connect(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, location_name, port_speed_shape_name, cross_connect_group_id, defined_tags, display_name, far_cross_connect_or_cross_connect_group_id, freeform_tags, near_cross_connect_or_cross_connect_group_id, customer_reference_name):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['locationName'] = location_name
    _details['portSpeedShapeName'] = port_speed_shape_name

    if cross_connect_group_id is not None:
        _details['crossConnectGroupId'] = cross_connect_group_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if far_cross_connect_or_cross_connect_group_id is not None:
        _details['farCrossConnectOrCrossConnectGroupId'] = far_cross_connect_or_cross_connect_group_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if near_cross_connect_or_cross_connect_group_id is not None:
        _details['nearCrossConnectOrCrossConnectGroupId'] = near_cross_connect_or_cross_connect_group_id

    if customer_reference_name is not None:
        _details['customerReferenceName'] = customer_reference_name

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_cross_connect(
        create_cross_connect_details=_details,
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


@cross_connect_group_group.command(name=cli_util.override('virtual_network.create_cross_connect_group.command_name', 'create'), help=u"""Creates a new cross-connect group to use with Oracle Cloud Infrastructure FastConnect. For more information, see [FastConnect Overview].

For the purposes of access control, you must provide the [OCID] of the compartment where you want the cross-connect group to reside. If you're not sure which compartment to use, put the cross-connect group in the same compartment with your VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the cross-connect group. It does not have to be unique, and you can change it. Avoid entering confidential information. \n[Command Reference](createCrossConnectGroup)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to contain the cross-connect group.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--customer-reference-name', help=u"""A reference name or identifier for the physical fiber connection that this cross-connect group uses.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'CrossConnectGroup'})
@cli_util.wrap_exceptions
def create_cross_connect_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, defined_tags, display_name, customer_reference_name, freeform_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if customer_reference_name is not None:
        _details['customerReferenceName'] = customer_reference_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_cross_connect_group(
        create_cross_connect_group_details=_details,
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


@dhcp_options_group.command(name=cli_util.override('virtual_network.create_dhcp_options.command_name', 'create'), help=u"""Creates a new set of DHCP options for the specified VCN. For more information, see [DhcpOptions].

For the purposes of access control, you must provide the [OCID] of the compartment where you want the set of DHCP options to reside. Notice that the set of options doesn't have to be in the same compartment as the VCN, subnets, or other Networking Service components. If you're not sure which compartment to use, put the set of DHCP options in the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the set of DHCP options, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information. \n[Command Reference](createDhcpOptions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to contain the set of DHCP options.""")
@cli_util.option('--options', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A set of DHCP options.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vcn-id', required=True, help=u"""The OCID of the VCN the set of DHCP options belongs to.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'options': {'module': 'core', 'class': 'list[DhcpOption]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'options': {'module': 'core', 'class': 'list[DhcpOption]'}}, output_type={'module': 'core', 'class': 'DhcpOptions'})
@cli_util.wrap_exceptions
def create_dhcp_options(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, options, vcn_id, defined_tags, display_name, freeform_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['options'] = cli_util.parse_json_parameter("options", options)
    _details['vcnId'] = vcn_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_dhcp_options(
        create_dhcp_details=_details,
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


@drg_group.command(name=cli_util.override('virtual_network.create_drg.command_name', 'create'), help=u"""Creates a new dynamic routing gateway (DRG) in the specified compartment. For more information, see [Dynamic Routing Gateways (DRGs)].

For the purposes of access control, you must provide the OCID of the compartment where you want the DRG to reside. Notice that the DRG doesn't have to be in the same compartment as the VCN, the DRG attachment, or other Networking Service components. If you're not sure which compartment to use, put the DRG in the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the DRG, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information. \n[Command Reference](createDrg)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to contain the DRG.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Drg'})
@cli_util.wrap_exceptions
def create_drg(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, defined_tags, display_name, freeform_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_drg(
        create_drg_details=_details,
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


@drg_attachment_group.command(name=cli_util.override('virtual_network.create_drg_attachment.command_name', 'create'), help=u"""Attaches the specified DRG to the specified network resource. A VCN can be attached to only one DRG at a time, but a DRG can be attached to more than one VCN. The response includes a `DrgAttachment` object with its own [OCID]. For more information about DRGs, see [Dynamic Routing Gateways (DRGs)].

You may optionally specify a *display name* for the attachment, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

For the purposes of access control, the DRG attachment is automatically placed into the currently selected compartment. For more information about compartments and access control, see [Overview of the IAM Service]. \n[Command Reference](createDrgAttachment)""")
@cli_util.option('--drg-id', required=True, help=u"""The [OCID] of the DRG.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique. Avoid entering confidential information.""")
@cli_util.option('--drg-route-table-id', help=u"""The [OCID] of the DRG route table that is assigned to this attachment.

The DRG route table manages traffic inside the DRG.""")
@cli_util.option('--network-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--route-table-id', help=u"""The [OCID] of the route table used by the DRG attachment.

If you don't specify a route table here, the DRG attachment is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the DRG attachment. For information about why you would associate a route table with a DRG attachment, see:

  * [Transit Routing: Access to Multiple VCNs in Same Region]   * [Transit Routing: Private Access to Oracle Services] This field is deprecated. Instead, use the networkDetails field to specify the VCN route table for this attachment.""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN. This field is deprecated. Instead, use the `networkDetails` field to specify the [OCID] of the attached resource.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'network-details': {'module': 'core', 'class': 'DrgAttachmentNetworkCreateDetails'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-details': {'module': 'core', 'class': 'DrgAttachmentNetworkCreateDetails'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'DrgAttachment'})
@cli_util.wrap_exceptions
def create_drg_attachment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_id, display_name, drg_route_table_id, network_details, defined_tags, freeform_tags, route_table_id, vcn_id):

    kwargs = {}

    _details = {}
    _details['drgId'] = drg_id

    if display_name is not None:
        _details['displayName'] = display_name

    if drg_route_table_id is not None:
        _details['drgRouteTableId'] = drg_route_table_id

    if network_details is not None:
        _details['networkDetails'] = cli_util.parse_json_parameter("network_details", network_details)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if route_table_id is not None:
        _details['routeTableId'] = route_table_id

    if vcn_id is not None:
        _details['vcnId'] = vcn_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_drg_attachment(
        create_drg_attachment_details=_details,
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


@drg_attachment_group.command(name=cli_util.override('virtual_network.create_drg_attachment_vcn_drg_attachment_network_create_details.command_name', 'create-drg-attachment-vcn-drg-attachment-network-create-details'), help=u"""Attaches the specified DRG to the specified network resource. A VCN can be attached to only one DRG at a time, but a DRG can be attached to more than one VCN. The response includes a `DrgAttachment` object with its own [OCID]. For more information about DRGs, see [Dynamic Routing Gateways (DRGs)].

You may optionally specify a *display name* for the attachment, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

For the purposes of access control, the DRG attachment is automatically placed into the currently selected compartment. For more information about compartments and access control, see [Overview of the IAM Service]. \n[Command Reference](createDrgAttachment)""")
@cli_util.option('--drg-id', required=True, help=u"""The [OCID] of the DRG.""")
@cli_util.option('--network-details-id', required=True, help=u"""The [OCID] of the network attached to the DRG.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique. Avoid entering confidential information.""")
@cli_util.option('--drg-route-table-id', help=u"""The [OCID] of the DRG route table that is assigned to this attachment.

The DRG route table manages traffic inside the DRG.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--route-table-id', help=u"""The [OCID] of the route table used by the DRG attachment.

If you don't specify a route table here, the DRG attachment is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the DRG attachment. For information about why you would associate a route table with a DRG attachment, see:

  * [Transit Routing: Access to Multiple VCNs in Same Region]   * [Transit Routing: Private Access to Oracle Services] This field is deprecated. Instead, use the networkDetails field to specify the VCN route table for this attachment.""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN. This field is deprecated. Instead, use the `networkDetails` field to specify the [OCID] of the attached resource.""")
@cli_util.option('--network-details-route-table-id', help=u"""This is the [OCID] of the route table that is used to route the traffic as it enters a VCN through this attachment.

For information about why you would associate a route table with a DRG attachment, see [Advanced Scenario: Transit Routing]. For information about why you would associate a route table with a DRG attachment, see:

  * [Transit Routing: Access to Multiple VCNs in Same Region]   * [Transit Routing: Private Access to Oracle Services]""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'DrgAttachment'})
@cli_util.wrap_exceptions
def create_drg_attachment_vcn_drg_attachment_network_create_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_id, network_details_id, display_name, drg_route_table_id, defined_tags, freeform_tags, route_table_id, vcn_id, network_details_route_table_id):

    kwargs = {}

    _details = {}
    _details['networkDetails'] = {}
    _details['drgId'] = drg_id
    _details['networkDetails']['id'] = network_details_id

    if display_name is not None:
        _details['displayName'] = display_name

    if drg_route_table_id is not None:
        _details['drgRouteTableId'] = drg_route_table_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if route_table_id is not None:
        _details['routeTableId'] = route_table_id

    if vcn_id is not None:
        _details['vcnId'] = vcn_id

    if network_details_route_table_id is not None:
        _details['networkDetails']['routeTableId'] = network_details_route_table_id

    _details['networkDetails']['type'] = 'VCN'

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_drg_attachment(
        create_drg_attachment_details=_details,
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


@drg_route_distribution_group.command(name=cli_util.override('virtual_network.create_drg_route_distribution.command_name', 'create'), help=u"""Creates a new route distribution for the specified DRG. Assign the route distribution as an import distribution to a DRG route table using the `UpdateDrgRouteTable` or `CreateDrgRouteTable` operations. Assign the route distribution as an export distribution to a DRG attachment using the `UpdateDrgAttachment` or `CreateDrgAttachment` operations. \n[Command Reference](createDrgRouteDistribution)""")
@cli_util.option('--drg-id', required=True, help=u"""The [OCID] of the DRG the DRG route table belongs to.""")
@cli_util.option('--distribution-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["IMPORT"]), help=u"""Whether this distribution defines how routes get imported into route tables or exported through DRG Attachments""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'DrgRouteDistribution'})
@cli_util.wrap_exceptions
def create_drg_route_distribution(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_id, distribution_type, defined_tags, display_name, freeform_tags):

    kwargs = {}

    _details = {}
    _details['drgId'] = drg_id
    _details['distributionType'] = distribution_type

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_drg_route_distribution(
        create_drg_route_distribution_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_drg_route_distribution') and callable(getattr(client, 'get_drg_route_distribution')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_drg_route_distribution(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@drg_route_table_group.command(name=cli_util.override('virtual_network.create_drg_route_table.command_name', 'create'), help=u"""Creates a new DRG route table for the specified DRG. Assign the DRG route table to a DRG attachment using the `UpdateDrgAttachment` or `CreateDrgAttachment` operations. \n[Command Reference](createDrgRouteTable)""")
@cli_util.option('--drg-id', required=True, help=u"""The [OCID] of the DRG the DRG route table belongs to.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--import-drg-route-distribution-id', help=u"""The [OCID] of the import route distribution used to specify how incoming route advertisements through referenced attachments are inserted into the DRG route table.""")
@cli_util.option('--is-ecmp-enabled', type=click.BOOL, help=u"""If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to your on-premises networks, enable ECMP on the DRG route table.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'DrgRouteTable'})
@cli_util.wrap_exceptions
def create_drg_route_table(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_id, defined_tags, display_name, freeform_tags, import_drg_route_distribution_id, is_ecmp_enabled):

    kwargs = {}

    _details = {}
    _details['drgId'] = drg_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if import_drg_route_distribution_id is not None:
        _details['importDrgRouteDistributionId'] = import_drg_route_distribution_id

    if is_ecmp_enabled is not None:
        _details['isEcmpEnabled'] = is_ecmp_enabled

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_drg_route_table(
        create_drg_route_table_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_drg_route_table') and callable(getattr(client, 'get_drg_route_table')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_drg_route_table(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@internet_gateway_group.command(name=cli_util.override('virtual_network.create_internet_gateway.command_name', 'create'), help=u"""Creates a new internet gateway for the specified VCN. For more information, see [Access to the Internet].

For the purposes of access control, you must provide the [OCID] of the compartment where you want the Internet Gateway to reside. Notice that the internet gateway doesn't have to be in the same compartment as the VCN or other Networking Service components. If you're not sure which compartment to use, put the Internet Gateway in the same compartment with the VCN. For more information about compartments and access control, see [Overview of the IAM Service].

You may optionally specify a *display name* for the internet gateway, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

For traffic to flow between a subnet and an internet gateway, you must create a route rule accordingly in the subnet's route table (for example, 0.0.0.0/0 > internet gateway). See [UpdateRouteTable].

You must specify whether the internet gateway is enabled when you create it. If it's disabled, that means no traffic will flow to/from the internet even if there's a route rule that enables that traffic. You can later use [UpdateInternetGateway] to easily disable/enable the gateway without changing the route rule. \n[Command Reference](createInternetGateway)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to contain the internet gateway.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Whether the gateway is enabled upon creation.""")
@cli_util.option('--vcn-id', required=True, help=u"""The OCID of the VCN the internet gateway is attached to.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'InternetGateway'})
@cli_util.wrap_exceptions
def create_internet_gateway(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, is_enabled, vcn_id, defined_tags, display_name, freeform_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['isEnabled'] = is_enabled
    _details['vcnId'] = vcn_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_internet_gateway(
        create_internet_gateway_details=_details,
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


@ip_sec_connection_group.command(name=cli_util.override('virtual_network.create_ip_sec_connection.command_name', 'create'), help=u"""Creates a new IPSec connection between the specified DRG and CPE. For more information, see [IPSec VPNs].

If you configure at least one tunnel to use static routing, then in the request you must provide at least one valid static route (you're allowed a maximum of 10). For example: 10.0.0.0/16. If you configure both tunnels to use BGP dynamic routing, you can provide an empty list for the static routes. For more information, see the important note in [IPSecConnection].

For the purposes of access control, you must provide the [OCID] of the compartment where you want the IPSec connection to reside. Notice that the IPSec connection doesn't have to be in the same compartment as the DRG, CPE, or other Networking Service components. If you're not sure which compartment to use, put the IPSec connection in the same compartment as the DRG. For more information about compartments and access control, see [Overview of the IAM Service].

You may optionally specify a *display name* for the IPSec connection, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

After creating the IPSec connection, you need to configure your on-premises router with tunnel-specific information. For tunnel status and the required configuration information, see:

  * [IPSecConnectionTunnel]   * [IPSecConnectionTunnelSharedSecret]

For each tunnel, you need the IP address of Oracle's VPN headend and the shared secret (that is, the pre-shared key). For more information, see [Configuring Your On-Premises Router for an IPSec VPN]. \n[Command Reference](createIPSecConnection)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to contain the IPSec connection.""")
@cli_util.option('--cpe-id', required=True, help=u"""The OCID of the [Cpe] object.""")
@cli_util.option('--drg-id', required=True, help=u"""The [OCID] of the DRG.""")
@cli_util.option('--static-routes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Static routes to the CPE. A static route's CIDR must not be a multicast address or class E address.

Used for routing a given IPSec tunnel's traffic only if the tunnel is using static routing. If you configure at least one tunnel to use static routing, then you must provide at least one valid static route. If you configure both tunnels to use BGP dynamic routing, you can provide an empty list for the static routes. For more information, see the important note in [IPSecConnection].

The CIDR can be either IPv4 or IPv6. IPv6 addressing is supported for all commercial and government regions. See [IPv6 Addresses].

Example: `10.0.1.0/24`

Example: `2001:db8::/32`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--cpe-local-identifier', help=u"""Your identifier for your CPE device. Can be either an IP address or a hostname (specifically, the fully qualified domain name (FQDN)). The type of identifier you provide here must correspond to the value for `cpeLocalIdentifierType`.

If you don't provide a value, the `ipAddress` attribute for the [Cpe] object specified by `cpeId` is used as the `cpeLocalIdentifier`.

For information about why you'd provide this value, see [If Your CPE Is Behind a NAT Device].

Example IP address: `10.0.3.3`

Example hostname: `cpe.example.com`""")
@cli_util.option('--cpe-local-identifier-type', type=custom_types.CliCaseInsensitiveChoice(["IP_ADDRESS", "HOSTNAME"]), help=u"""The type of identifier for your CPE device. The value you provide here must correspond to the value for `cpeLocalIdentifier`.""")
@cli_util.option('--tunnel-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Information for creating the individual tunnels in the IPSec connection. You can provide a maximum of 2 `tunnelConfiguration` objects in the array (one for each of the two tunnels).

This option is a JSON list with items of type CreateIPSecConnectionTunnelDetails.  For documentation on CreateIPSecConnectionTunnelDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/CreateIPSecConnectionTunnelDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'static-routes': {'module': 'core', 'class': 'list[string]'}, 'tunnel-configuration': {'module': 'core', 'class': 'list[CreateIPSecConnectionTunnelDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'static-routes': {'module': 'core', 'class': 'list[string]'}, 'tunnel-configuration': {'module': 'core', 'class': 'list[CreateIPSecConnectionTunnelDetails]'}}, output_type={'module': 'core', 'class': 'IPSecConnection'})
@cli_util.wrap_exceptions
def create_ip_sec_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, cpe_id, drg_id, static_routes, defined_tags, display_name, freeform_tags, cpe_local_identifier, cpe_local_identifier_type, tunnel_configuration):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['cpeId'] = cpe_id
    _details['drgId'] = drg_id
    _details['staticRoutes'] = cli_util.parse_json_parameter("static_routes", static_routes)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if cpe_local_identifier is not None:
        _details['cpeLocalIdentifier'] = cpe_local_identifier

    if cpe_local_identifier_type is not None:
        _details['cpeLocalIdentifierType'] = cpe_local_identifier_type

    if tunnel_configuration is not None:
        _details['tunnelConfiguration'] = cli_util.parse_json_parameter("tunnel_configuration", tunnel_configuration)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_ip_sec_connection(
        create_ip_sec_connection_details=_details,
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


@ipv6_group.command(name=cli_util.override('virtual_network.create_ipv6.command_name', 'create'), help=u"""Creates an IPv6 for the specified VNIC. \n[Command Reference](createIpv6)""")
@cli_util.option('--vnic-id', required=True, help=u"""The [OCID] of the VNIC to assign the IPv6 to. The IPv6 will be in the VNIC's subnet.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ip-address', help=u"""An IPv6 address of your choice. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns an IPv6 address from the subnet. The subnet is the one that contains the VNIC you specify in `vnicId`.

Example: `2001:DB8::`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Ipv6'})
@cli_util.wrap_exceptions
def create_ipv6(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vnic_id, defined_tags, display_name, freeform_tags, ip_address):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['vnicId'] = vnic_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if ip_address is not None:
        _details['ipAddress'] = ip_address

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_ipv6(
        create_ipv6_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_ipv6') and callable(getattr(client, 'get_ipv6')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_ipv6(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@local_peering_gateway_group.command(name=cli_util.override('virtual_network.create_local_peering_gateway.command_name', 'create'), help=u"""Creates a new local peering gateway (LPG) for the specified VCN. \n[Command Reference](createLocalPeeringGateway)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment containing the local peering gateway (LPG).""")
@cli_util.option('--vcn-id', required=True, help=u"""The OCID of the VCN the LPG belongs to.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--route-table-id', help=u"""The OCID of the route table the LPG will use.

If you don't specify a route table here, the LPG is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the LPG.

For information about why you would associate a route table with an LPG, see [Transit Routing: Access to Multiple VCNs in Same Region].""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'LocalPeeringGateway'})
@cli_util.wrap_exceptions
def create_local_peering_gateway(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, vcn_id, defined_tags, display_name, freeform_tags, route_table_id):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['vcnId'] = vcn_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if route_table_id is not None:
        _details['routeTableId'] = route_table_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_local_peering_gateway(
        create_local_peering_gateway_details=_details,
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


@nat_gateway_group.command(name=cli_util.override('virtual_network.create_nat_gateway.command_name', 'create'), help=u"""Creates a new NAT gateway for the specified VCN. You must also set up a route rule with the NAT gateway as the rule's target. See [Route Table]. \n[Command Reference](createNatGateway)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to contain the NAT gateway.""")
@cli_util.option('--vcn-id', required=True, help=u"""The [OCID] of the VCN the gateway belongs to.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--block-traffic', type=click.BOOL, help=u"""Whether the NAT gateway blocks traffic through it. The default is `false`.

Example: `true`""")
@cli_util.option('--public-ip-id', help=u"""The [OCID] of the public IP address associated with the NAT gateway.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'NatGateway'})
@cli_util.wrap_exceptions
def create_nat_gateway(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, vcn_id, defined_tags, display_name, freeform_tags, block_traffic, public_ip_id):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['vcnId'] = vcn_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if block_traffic is not None:
        _details['blockTraffic'] = block_traffic

    if public_ip_id is not None:
        _details['publicIpId'] = public_ip_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_nat_gateway(
        create_nat_gateway_details=_details,
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


@network_security_group_group.command(name=cli_util.override('virtual_network.create_network_security_group.command_name', 'create'), help=u"""Creates a new network security group for the specified VCN. \n[Command Reference](createNetworkSecurityGroup)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to contain the network security group.""")
@cli_util.option('--vcn-id', required=True, help=u"""The [OCID] of the VCN to create the network security group in.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the network security group. Does not have to be unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'NetworkSecurityGroup'})
@cli_util.wrap_exceptions
def create_network_security_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, vcn_id, defined_tags, display_name, freeform_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['vcnId'] = vcn_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_network_security_group(
        create_network_security_group_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_network_security_group') and callable(getattr(client, 'get_network_security_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_network_security_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@private_ip_group.command(name=cli_util.override('virtual_network.create_private_ip.command_name', 'create'), help=u"""Creates a secondary private IP for the specified VNIC. For more information about secondary private IPs, see [IP Addresses]. \n[Command Reference](createPrivateIp)""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostname-label', help=u"""The hostname for the private IP. Used for DNS. The value is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952] and [RFC 1123].

For more information, see [DNS in Your Virtual Cloud Network].

Example: `bminstance-1`""")
@cli_util.option('--ip-address', help=u"""A private IP address of your choice. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet.

Example: `10.0.3.3`""")
@cli_util.option('--vnic-id', help=u"""The OCID of the VNIC to assign the private IP to. The VNIC and private IP must be in the same subnet.""")
@cli_util.option('--vlan-id', help=u"""Use this attribute only with the Oracle Cloud VMware Solution.

The OCID of the VLAN from which the private IP is to be drawn. The IP address, *if supplied*, must be valid for the given VLAN. See [Vlan].""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'PrivateIp'})
@cli_util.wrap_exceptions
def create_private_ip(ctx, from_json, defined_tags, display_name, freeform_tags, hostname_label, ip_address, vnic_id, vlan_id):

    kwargs = {}

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if hostname_label is not None:
        _details['hostnameLabel'] = hostname_label

    if ip_address is not None:
        _details['ipAddress'] = ip_address

    if vnic_id is not None:
        _details['vnicId'] = vnic_id

    if vlan_id is not None:
        _details['vlanId'] = vlan_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_private_ip(
        create_private_ip_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_group.command(name=cli_util.override('virtual_network.create_public_ip.command_name', 'create'), help=u"""Creates a public IP. Use the `lifetime` property to specify whether it's an ephemeral or reserved public IP. For information about limits on how many you can create, see [Public IP Addresses].

* **For an ephemeral public IP assigned to a private IP:** You must also specify a `privateIpId` with the OCID of the primary private IP you want to assign the public IP to. The public IP is created in the same availability domain as the private IP. An ephemeral public IP must always be assigned to a private IP, and only to the *primary* private IP on a VNIC, not a secondary private IP. Exception: If you create a [NatGateway], Oracle automatically assigns the NAT gateway a regional ephemeral public IP that you cannot remove.

* **For a reserved public IP:** You may also optionally assign the public IP to a private IP by specifying `privateIpId`. Or you can later assign the public IP with [UpdatePublicIp].

**Note:** When assigning a public IP to a private IP, the private IP must not already have a public IP with `lifecycleState` = ASSIGNING or ASSIGNED. If it does, an error is returned.

Also, for reserved public IPs, the optional assignment part of this operation is asynchronous. Poll the public IP's `lifecycleState` to determine if the assignment succeeded. \n[Command Reference](createPublicIp)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to contain the public IP. For ephemeral public IPs, you must set this to the private IP's compartment OCID.""")
@cli_util.option('--lifetime', required=True, type=custom_types.CliCaseInsensitiveChoice(["EPHEMERAL", "RESERVED"]), help=u"""Defines when the public IP is deleted and released back to the Oracle Cloud Infrastructure public IP pool. For more information, see [Public IP Addresses].""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--private-ip-id', help=u"""The OCID of the private IP to assign the public IP to.

Required for an ephemeral public IP because it must always be assigned to a private IP (specifically a *primary* private IP).

Optional for a reserved public IP. If you don't provide it, the public IP is created but not assigned to a private IP. You can later assign the public IP with [UpdatePublicIp].""")
@cli_util.option('--public-ip-pool-id', help=u"""The [OCID] of the public IP pool.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "ASSIGNING", "ASSIGNED", "UNASSIGNING", "UNASSIGNED", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'PublicIp'})
@cli_util.wrap_exceptions
def create_public_ip(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, lifetime, defined_tags, display_name, freeform_tags, private_ip_id, public_ip_pool_id):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['lifetime'] = lifetime

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if private_ip_id is not None:
        _details['privateIpId'] = private_ip_id

    if public_ip_pool_id is not None:
        _details['publicIpPoolId'] = public_ip_pool_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_public_ip(
        create_public_ip_details=_details,
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


@public_ip_pool_group.command(name=cli_util.override('virtual_network.create_public_ip_pool.command_name', 'create'), help=u"""Creates a public IP pool. \n[Command Reference](createPublicIpPool)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the public IP pool.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["INACTIVE", "UPDATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'PublicIpPool'})
@cli_util.wrap_exceptions
def create_public_ip_pool(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, defined_tags, display_name, freeform_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_public_ip_pool(
        create_public_ip_pool_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_public_ip_pool') and callable(getattr(client, 'get_public_ip_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_public_ip_pool(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@remote_peering_connection_group.command(name=cli_util.override('virtual_network.create_remote_peering_connection.command_name', 'create'), help=u"""Creates a new remote peering connection (RPC) for the specified DRG. \n[Command Reference](createRemotePeeringConnection)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to contain the RPC.""")
@cli_util.option('--drg-id', required=True, help=u"""The OCID of the DRG the RPC belongs to.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "PROVISIONING", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'RemotePeeringConnection'})
@cli_util.wrap_exceptions
def create_remote_peering_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, drg_id, defined_tags, display_name, freeform_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['drgId'] = drg_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_remote_peering_connection(
        create_remote_peering_connection_details=_details,
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


@route_table_group.command(name=cli_util.override('virtual_network.create_route_table.command_name', 'create'), help=u"""Creates a new route table for the specified VCN. In the request you must also include at least one route rule for the new route table. For information on the number of rules you can have in a route table, see [Service Limits]. For general information about route tables in your VCN and the types of targets you can use in route rules, see [Route Tables].

For the purposes of access control, you must provide the OCID of the compartment where you want the route table to reside. Notice that the route table doesn't have to be in the same compartment as the VCN, subnets, or other Networking Service components. If you're not sure which compartment to use, put the route table in the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the route table, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information. \n[Command Reference](createRouteTable)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to contain the route table.""")
@cli_util.option('--route-rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The collection of rules used for routing destination IPs to network devices.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vcn-id', required=True, help=u"""The OCID of the VCN the route table belongs to.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'route-rules': {'module': 'core', 'class': 'list[RouteRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'route-rules': {'module': 'core', 'class': 'list[RouteRule]'}}, output_type={'module': 'core', 'class': 'RouteTable'})
@cli_util.wrap_exceptions
def create_route_table(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, route_rules, vcn_id, defined_tags, display_name, freeform_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['routeRules'] = cli_util.parse_json_parameter("route_rules", route_rules)
    _details['vcnId'] = vcn_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_route_table(
        create_route_table_details=_details,
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


@security_list_group.command(name=cli_util.override('virtual_network.create_security_list.command_name', 'create'), help=u"""Creates a new security list for the specified VCN. For more information about security lists, see [Security Lists]. For information on the number of rules you can have in a security list, see [Service Limits].

For the purposes of access control, you must provide the OCID of the compartment where you want the security list to reside. Notice that the security list doesn't have to be in the same compartment as the VCN, subnets, or other Networking Service components. If you're not sure which compartment to use, put the security list in the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the security list, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information. \n[Command Reference](createSecurityList)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to contain the security list.""")
@cli_util.option('--egress-security-rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Rules for allowing egress IP packets.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ingress-security-rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Rules for allowing ingress IP packets.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vcn-id', required=True, help=u"""The OCID of the VCN the security list belongs to.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'egress-security-rules': {'module': 'core', 'class': 'list[EgressSecurityRule]'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'ingress-security-rules': {'module': 'core', 'class': 'list[IngressSecurityRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'egress-security-rules': {'module': 'core', 'class': 'list[EgressSecurityRule]'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'ingress-security-rules': {'module': 'core', 'class': 'list[IngressSecurityRule]'}}, output_type={'module': 'core', 'class': 'SecurityList'})
@cli_util.wrap_exceptions
def create_security_list(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, egress_security_rules, ingress_security_rules, vcn_id, defined_tags, display_name, freeform_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['egressSecurityRules'] = cli_util.parse_json_parameter("egress_security_rules", egress_security_rules)
    _details['ingressSecurityRules'] = cli_util.parse_json_parameter("ingress_security_rules", ingress_security_rules)
    _details['vcnId'] = vcn_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_security_list(
        create_security_list_details=_details,
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


@service_gateway_group.command(name=cli_util.override('virtual_network.create_service_gateway.command_name', 'create'), help=u"""Creates a new service gateway in the specified compartment.

For the purposes of access control, you must provide the OCID of the compartment where you want the service gateway to reside. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the service gateway, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information. \n[Command Reference](createServiceGateway)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID]  of the compartment to contain the service gateway.""")
@cli_util.option('--services', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of the OCIDs of the [Service] objects to enable for the service gateway. This list can be empty if you don't want to enable any `Service` objects when you create the gateway. You can enable a `Service` object later by using either [AttachServiceId] or [UpdateServiceGateway].

For each enabled `Service`, make sure there's a route rule with the `Service` object's `cidrBlock` as the rule's destination and the service gateway as the rule's target. See [Route Table].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vcn-id', required=True, help=u"""The [OCID] of the VCN.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--route-table-id', help=u"""The OCID of the route table the service gateway will use.

If you don't specify a route table here, the service gateway is created without an associated route table. The Networking service does NOT automatically associate the attached VCN's default route table with the service gateway.

For information about why you would associate a route table with a service gateway, see [Transit Routing: Private Access to Oracle Services].""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'services': {'module': 'core', 'class': 'list[ServiceIdRequestDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'services': {'module': 'core', 'class': 'list[ServiceIdRequestDetails]'}}, output_type={'module': 'core', 'class': 'ServiceGateway'})
@cli_util.wrap_exceptions
def create_service_gateway(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, services, vcn_id, defined_tags, display_name, freeform_tags, route_table_id):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['services'] = cli_util.parse_json_parameter("services", services)
    _details['vcnId'] = vcn_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if route_table_id is not None:
        _details['routeTableId'] = route_table_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_service_gateway(
        create_service_gateway_details=_details,
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


@subnet_group.command(name=cli_util.override('virtual_network.create_subnet.command_name', 'create'), help=u"""Creates a new subnet in the specified VCN. You can't change the size of the subnet after creation, so it's important to think about the size of subnets you need before creating them. For more information, see [VCNs and Subnets]. For information on the number of subnets you can have in a VCN, see [Service Limits].

For the purposes of access control, you must provide the OCID of the compartment where you want the subnet to reside. Notice that the subnet doesn't have to be in the same compartment as the VCN, route tables, or other Networking Service components. If you're not sure which compartment to use, put the subnet in the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally associate a route table with the subnet. If you don't, the subnet will use the VCN's default route table. For more information about route tables, see [Route Tables].

You may optionally associate a security list with the subnet. If you don't, the subnet will use the VCN's default security list. For more information about security lists, see [Security Lists].

You may optionally associate a set of DHCP options with the subnet. If you don't, the subnet will use the VCN's default set. For more information about DHCP options, see [DHCP Options].

You may optionally specify a *display name* for the subnet, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

You can also add a DNS label for the subnet, which is required if you want the Internet and VCN Resolver to resolve hostnames for instances in the subnet. For more information, see [DNS in Your Virtual Cloud Network]. \n[Command Reference](createSubnet)""")
@cli_util.option('--cidr-block', required=True, help=u"""The CIDR IP address range of the subnet. The CIDR must maintain the following rules -

a. The CIDR block is valid and correctly formatted. b. The new range is within one of the parent VCN ranges.

Example: `10.0.1.0/24`""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to contain the subnet.""")
@cli_util.option('--vcn-id', required=True, help=u"""The OCID of the VCN to contain the subnet.""")
@cli_util.option('--availability-domain', help=u"""Controls whether the subnet is regional or specific to an availability domain. Oracle recommends creating regional subnets because they're more flexible and make it easier to implement failover across availability domains. Originally, AD-specific subnets were the only kind available to use.

To create a regional subnet, omit this attribute. Then any resources later created in this subnet (such as a Compute instance) can be created in any availability domain in the region.

To instead create an AD-specific subnet, set this attribute to the availability domain you want this subnet to be in. Then any resources later created in this subnet can only be created in that availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dhcp-options-id', help=u"""The OCID of the set of DHCP options the subnet will use. If you don't provide a value, the subnet uses the VCN's default set of DHCP options.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--dns-label', help=u"""A DNS label for the subnet, used in conjunction with the VNIC's hostname and VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be an alphanumeric string that begins with a letter and is unique within the VCN. The value cannot be changed.

This value must be set if you want to use the Internet and VCN Resolver to resolve the hostnames of instances in the subnet. It can only be set if the VCN itself was created with a DNS label.

For more information, see [DNS in Your Virtual Cloud Network].

Example: `subnet123`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ipv6-cidr-block', help=u"""Use this to enable IPv6 addressing for this subnet. The VCN must be enabled for IPv6. You can't change this subnet characteristic later. All subnets are /64 in size. The subnet portion of the IPv6 address is the fourth hextet from the left (1111 in the following example).

For important details about IPv6 addressing in a VCN, see [IPv6 Addresses].

Example: `2001:0db8:0123:1111::/64`""")
@cli_util.option('--prohibit-internet-ingress', type=click.BOOL, help=u"""Whether to disallow ingress internet traffic to VNICs within this subnet. Defaults to false.

For IPv6, if `prohibitInternetIngress` is set to `true`, internet access is not allowed for any IPv6s assigned to VNICs in the subnet. Otherwise, ingress internet traffic is allowed by default.

`prohibitPublicIpOnVnic` will be set to the value of `prohibitInternetIngress` to dictate IPv4 behavior in this subnet. Only one or the other flag should be specified.

Example: `true`""")
@cli_util.option('--prohibit-public-ip-on-vnic', type=click.BOOL, help=u"""Whether VNICs within this subnet can have public IP addresses. Defaults to false, which means VNICs created in this subnet will automatically be assigned public IP addresses unless specified otherwise during instance launch or VNIC creation (with the `assignPublicIp` flag in [CreateVnicDetails]). If `prohibitPublicIpOnVnic` is set to true, VNICs created in this subnet cannot have public IP addresses (that is, it's a private subnet).

If you intend to use an IPv6 CIDR block, you should use the flag `prohibitInternetIngress` to specify ingress internet traffic behavior of the subnet.

Example: `true`""")
@cli_util.option('--route-table-id', help=u"""The OCID of the route table the subnet will use. If you don't provide a value, the subnet uses the VCN's default route table.""")
@cli_util.option('--security-list-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The OCIDs of the security list or lists the subnet will use. If you don't provide a value, the subnet uses the VCN's default security list. Remember that security lists are associated *with the subnet*, but the rules are applied to the individual VNICs in the subnet.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'security-list-ids': {'module': 'core', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'security-list-ids': {'module': 'core', 'class': 'list[string]'}}, output_type={'module': 'core', 'class': 'Subnet'})
@cli_util.wrap_exceptions
def create_subnet(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, cidr_block, compartment_id, vcn_id, availability_domain, defined_tags, dhcp_options_id, display_name, dns_label, freeform_tags, ipv6_cidr_block, prohibit_internet_ingress, prohibit_public_ip_on_vnic, route_table_id, security_list_ids):

    kwargs = {}

    _details = {}
    _details['cidrBlock'] = cidr_block
    _details['compartmentId'] = compartment_id
    _details['vcnId'] = vcn_id

    if availability_domain is not None:
        _details['availabilityDomain'] = availability_domain

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if dhcp_options_id is not None:
        _details['dhcpOptionsId'] = dhcp_options_id

    if display_name is not None:
        _details['displayName'] = display_name

    if dns_label is not None:
        _details['dnsLabel'] = dns_label

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if ipv6_cidr_block is not None:
        _details['ipv6CidrBlock'] = ipv6_cidr_block

    if prohibit_internet_ingress is not None:
        _details['prohibitInternetIngress'] = prohibit_internet_ingress

    if prohibit_public_ip_on_vnic is not None:
        _details['prohibitPublicIpOnVnic'] = prohibit_public_ip_on_vnic

    if route_table_id is not None:
        _details['routeTableId'] = route_table_id

    if security_list_ids is not None:
        _details['securityListIds'] = cli_util.parse_json_parameter("security_list_ids", security_list_ids)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_subnet(
        create_subnet_details=_details,
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


@vcn_group.command(name=cli_util.override('virtual_network.create_vcn.command_name', 'create'), help=u"""Creates a new virtual cloud network (VCN). For more information, see [VCNs and Subnets].

For the VCN, you specify a list of one or more IPv4 CIDR blocks that meet the following criteria:

- The CIDR blocks must be valid. - They must not overlap with each other or with the on-premises network CIDR block. - The number of CIDR blocks does not exceed the limit of CIDR blocks allowed per VCN.

For a CIDR block, Oracle recommends that you use one of the private IP address ranges specified in [RFC 1918] (10.0.0.0/8, 172.16/12, and 192.168/16). Example: 172.16.0.0/16. The CIDR blocks can range from /16 to /30.

For the purposes of access control, you must provide the OCID of the compartment where you want the VCN to reside. Consult an Oracle Cloud Infrastructure administrator in your organization if you're not sure which compartment to use. Notice that the VCN doesn't have to be in the same compartment as the subnets or other Networking Service components. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the VCN, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

You can also add a DNS label for the VCN, which is required if you want the instances to use the Interent and VCN Resolver option for DNS in the VCN. For more information, see [DNS in Your Virtual Cloud Network].

The VCN automatically comes with a default route table, default security list, and default set of DHCP options. The OCID for each is returned in the response. You can't delete these default objects, but you can change their contents (that is, change the route rules, security list rules, and so on).

The VCN and subnets you create are not accessible until you attach an internet gateway or set up an IPSec VPN or FastConnect. For more information, see [Overview of the Networking Service]. \n[Command Reference](createVcn)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to contain the VCN.""")
@cli_util.option('--cidr-block', help=u"""**Deprecated.** Do *not* set this value. Use `cidrBlocks` instead. Example: `10.0.0.0/16`""")
@cli_util.option('--cidr-blocks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of one or more IPv4 CIDR blocks for the VCN that meet the following criteria: - The CIDR blocks must be valid. - They must not overlap with each other or with the on-premises network CIDR block. - The number of CIDR blocks must not exceed the limit of CIDR blocks allowed per VCN.

**Important:** Do *not* specify a value for `cidrBlock`. Use this parameter instead.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--dns-label', help=u"""A DNS label for the VCN, used in conjunction with the VNIC's hostname and subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`). Not required to be unique, but it's a best practice to set unique DNS labels for VCNs in your tenancy. Must be an alphanumeric string that begins with a letter. The value cannot be changed.

You must set this value if you want instances to be able to use hostnames to resolve other instances in the VCN. Otherwise the Internet and VCN Resolver will not work.

For more information, see [DNS in Your Virtual Cloud Network].

Example: `vcn1`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-ipv6-enabled', type=click.BOOL, help=u"""Whether IPv6 is enabled for the VCN. Default is `false`. If enabled, Oracle will assign the VCN a IPv6 /56 CIDR block. For important details about IPv6 addressing in a VCN, see [IPv6 Addresses].

Example: `true`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'cidr-blocks': {'module': 'core', 'class': 'list[string]'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'cidr-blocks': {'module': 'core', 'class': 'list[string]'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Vcn'})
@cli_util.wrap_exceptions
def create_vcn(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, cidr_block, cidr_blocks, defined_tags, display_name, dns_label, freeform_tags, is_ipv6_enabled):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id

    if cidr_block is not None:
        _details['cidrBlock'] = cidr_block

    if cidr_blocks is not None:
        _details['cidrBlocks'] = cli_util.parse_json_parameter("cidr_blocks", cidr_blocks)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if dns_label is not None:
        _details['dnsLabel'] = dns_label

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if is_ipv6_enabled is not None:
        _details['isIpv6Enabled'] = is_ipv6_enabled

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_vcn(
        create_vcn_details=_details,
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


@virtual_circuit_group.command(name=cli_util.override('virtual_network.create_virtual_circuit.command_name', 'create'), help=u"""Creates a new virtual circuit to use with Oracle Cloud Infrastructure FastConnect. For more information, see [FastConnect Overview].

For the purposes of access control, you must provide the OCID of the compartment where you want the virtual circuit to reside. If you're not sure which compartment to use, put the virtual circuit in the same compartment with the DRG it's using. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the virtual circuit. It does not have to be unique, and you can change it. Avoid entering confidential information.

**Important:** When creating a virtual circuit, you specify a DRG for the traffic to flow through. Make sure you attach the DRG to your VCN and confirm the VCN's routing sends traffic to the DRG. Otherwise traffic will not flow. For more information, see [Route Tables]. \n[Command Reference](createVirtualCircuit)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to contain the virtual circuit.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["PUBLIC", "PRIVATE"]), help=u"""The type of IP addresses used in this virtual circuit. PRIVATE means [RFC 1918] addresses (10.0.0.0/8, 172.16/12, and 192.168/16).""")
@cli_util.option('--bandwidth-shape-name', help=u"""The provisioned data rate of the connection. To get a list of the available bandwidth levels (that is, shapes), see [ListFastConnectProviderServiceVirtualCircuitBandwidthShapes].

Example: `10 Gbps`""")
@cli_util.option('--cross-connect-mappings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Create a `CrossConnectMapping` for each cross-connect or cross-connect group this virtual circuit will run on.

This option is a JSON list with items of type CrossConnectMapping.  For documentation on CrossConnectMapping please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/CrossConnectMapping.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--routing-policy', type=custom_types.CliCaseInsensitiveChoice(["ORACLE_SERVICE_NETWORK", "REGIONAL", "MARKET_LEVEL", "GLOBAL"]), help=u"""The routing policy sets how routing information about the Oracle cloud is shared over a public virtual circuit. Policies available are: `ORACLE_SERVICE_NETWORK`, `REGIONAL`, `MARKET_LEVEL`, and `GLOBAL`. See [Route Filtering] for details. By default, routing information is shared for all routes in the same market.""")
@cli_util.option('--customer-bgp-asn', type=click.INT, help=u"""Deprecated. Instead use `customerAsn`. If you specify values for both, the request will be rejected.""")
@cli_util.option('--customer-asn', type=click.INT, help=u"""Your BGP ASN (either public or private). Provide this value only if there's a BGP session that goes from your edge router to Oracle. Otherwise, leave this empty or null. Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format.

Example: `12345` (2-byte) or `1587232876` (4-byte)""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--gateway-id', help=u"""For private virtual circuits only. The OCID of the [dynamic routing gateway (DRG)] that this virtual circuit uses.""")
@cli_util.option('--provider-name', help=u"""Deprecated. Instead use `providerServiceId`. To get a list of the provider names, see [ListFastConnectProviderServices].""")
@cli_util.option('--provider-service-id', help=u"""The OCID of the service offered by the provider (if you're connecting via a provider). To get a list of the available service offerings, see [ListFastConnectProviderServices].""")
@cli_util.option('--provider-service-key-name', help=u"""The service key name offered by the provider (if the customer is connecting via a provider).""")
@cli_util.option('--provider-service-name', help=u"""Deprecated. Instead use `providerServiceId`. To get a list of the provider names, see [ListFastConnectProviderServices].""")
@cli_util.option('--public-prefixes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to advertise across the connection.

This option is a JSON list with items of type CreateVirtualCircuitPublicPrefixDetails.  For documentation on CreateVirtualCircuitPublicPrefixDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/CreateVirtualCircuitPublicPrefixDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--region-parameterconflict', help=u"""The Oracle Cloud Infrastructure region where this virtual circuit is located. Example: `phx`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_PROVIDER", "VERIFYING", "PROVISIONING", "PROVISIONED", "FAILED", "INACTIVE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'cross-connect-mappings': {'module': 'core', 'class': 'list[CrossConnectMapping]'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'public-prefixes': {'module': 'core', 'class': 'list[CreateVirtualCircuitPublicPrefixDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'cross-connect-mappings': {'module': 'core', 'class': 'list[CrossConnectMapping]'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'public-prefixes': {'module': 'core', 'class': 'list[CreateVirtualCircuitPublicPrefixDetails]'}}, output_type={'module': 'core', 'class': 'VirtualCircuit'})
@cli_util.wrap_exceptions
def create_virtual_circuit(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, type, bandwidth_shape_name, cross_connect_mappings, routing_policy, customer_bgp_asn, customer_asn, defined_tags, display_name, freeform_tags, gateway_id, provider_name, provider_service_id, provider_service_key_name, provider_service_name, public_prefixes, region_parameterconflict):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['type'] = type

    if bandwidth_shape_name is not None:
        _details['bandwidthShapeName'] = bandwidth_shape_name

    if cross_connect_mappings is not None:
        _details['crossConnectMappings'] = cli_util.parse_json_parameter("cross_connect_mappings", cross_connect_mappings)

    if routing_policy is not None:
        _details['routingPolicy'] = cli_util.parse_json_parameter("routing_policy", routing_policy)

    if customer_bgp_asn is not None:
        _details['customerBgpAsn'] = customer_bgp_asn

    if customer_asn is not None:
        _details['customerAsn'] = customer_asn

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if gateway_id is not None:
        _details['gatewayId'] = gateway_id

    if provider_name is not None:
        _details['providerName'] = provider_name

    if provider_service_id is not None:
        _details['providerServiceId'] = provider_service_id

    if provider_service_key_name is not None:
        _details['providerServiceKeyName'] = provider_service_key_name

    if provider_service_name is not None:
        _details['providerServiceName'] = provider_service_name

    if public_prefixes is not None:
        _details['publicPrefixes'] = cli_util.parse_json_parameter("public_prefixes", public_prefixes)

    if region_parameterconflict is not None:
        _details['region'] = region_parameterconflict

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_virtual_circuit(
        create_virtual_circuit_details=_details,
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


@vlan_group.command(name=cli_util.override('virtual_network.create_vlan.command_name', 'create'), help=u"""Creates a VLAN in the specified VCN and the specified compartment. \n[Command Reference](createVlan)""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain of the VLAN.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--cidr-block', required=True, help=u"""The range of IPv4 addresses that will be used for layer 3 communication with hosts outside the VLAN. The CIDR must maintain the following rules -

a. The CIDR block is valid and correctly formatted. b. The new range is within one of the parent VCN ranges.

Example: `192.0.2.0/24`""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to contain the VLAN.""")
@cli_util.option('--vcn-id', required=True, help=u"""The OCID of the VCN to contain the VLAN.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A descriptive name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the OCIDs of the network security groups (NSGs) to add all VNICs in the VLAN to. For more information about NSGs, see [NetworkSecurityGroup].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--route-table-id', help=u"""The OCID of the route table the VLAN will use. If you don't provide a value, the VLAN uses the VCN's default route table.""")
@cli_util.option('--vlan-tag', type=click.INT, help=u"""The IEEE 802.1Q VLAN tag for this VLAN. The value must be unique across all VLANs in the VCN. If you don't provide a value, Oracle assigns one. You cannot change the value later. VLAN tag 0 is reserved for use by Oracle.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'core', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'core', 'class': 'list[string]'}}, output_type={'module': 'core', 'class': 'Vlan'})
@cli_util.wrap_exceptions
def create_vlan(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, cidr_block, compartment_id, vcn_id, defined_tags, display_name, freeform_tags, nsg_ids, route_table_id, vlan_tag):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['availabilityDomain'] = availability_domain
    _details['cidrBlock'] = cidr_block
    _details['compartmentId'] = compartment_id
    _details['vcnId'] = vcn_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if route_table_id is not None:
        _details['routeTableId'] = route_table_id

    if vlan_tag is not None:
        _details['vlanTag'] = vlan_tag

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.create_vlan(
        create_vlan_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vlan') and callable(getattr(client, 'get_vlan')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vlan(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@byoip_range_group.command(name=cli_util.override('virtual_network.delete_byoip_range.command_name', 'delete'), help=u"""Deletes the specified `ByoipRange` resource. The resource must be in one of the following states: CREATING, PROVISIONED, ACTIVE, or FAILED. It must not have any subranges currently allocated to a PublicIpPool object or the deletion will fail. You must specify the [OCID]. If the `ByoipRange` resource is currently in the PROVISIONED or ACTIVE state, it will be de-provisioned and then deleted. \n[Command Reference](deleteByoipRange)""")
@cli_util.option('--byoip-range-id', required=True, help=u"""The [OCID] of the `ByoipRange` resource containing the BYOIP CIDR block.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_byoip_range(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, byoip_range_id, if_match):

    if isinstance(byoip_range_id, six.string_types) and len(byoip_range_id.strip()) == 0:
        raise click.UsageError('Parameter --byoip-range-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.delete_byoip_range(
        byoip_range_id=byoip_range_id,
        **kwargs
    )
    work_request_client = cli_util.build_client('work_requests', 'work_request', ctx)
    if wait_for_state:

        if hasattr(work_request_client, 'get_work_request') and callable(getattr(work_request_client, 'get_work_request')):
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


@cpe_group.command(name=cli_util.override('virtual_network.delete_cpe.command_name', 'delete'), help=u"""Deletes the specified CPE object. The CPE must not be connected to a DRG. This is an asynchronous operation. The CPE's `lifecycleState` will change to TERMINATING temporarily until the CPE is completely removed. \n[Command Reference](deleteCpe)""")
@cli_util.option('--cpe-id', required=True, help=u"""The [OCID] of the CPE.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.delete_cpe(
        cpe_id=cpe_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cross_connect_group.command(name=cli_util.override('virtual_network.delete_cross_connect.command_name', 'delete'), help=u"""Deletes the specified cross-connect. It must not be mapped to a [VirtualCircuit]. \n[Command Reference](deleteCrossConnect)""")
@cli_util.option('--cross-connect-id', required=True, help=u"""The [OCID] of the cross-connect.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cross_connect_group_group.command(name=cli_util.override('virtual_network.delete_cross_connect_group.command_name', 'delete'), help=u"""Deletes the specified cross-connect group. It must not contain any cross-connects, and it cannot be mapped to a [VirtualCircuit]. \n[Command Reference](deleteCrossConnectGroup)""")
@cli_util.option('--cross-connect-group-id', required=True, help=u"""The [OCID] of the cross-connect group.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dhcp_options_group.command(name=cli_util.override('virtual_network.delete_dhcp_options.command_name', 'delete'), help=u"""Deletes the specified set of DHCP options, but only if it's not associated with a subnet. You can't delete a VCN's default set of DHCP options.

This is an asynchronous operation. The state of the set of options will switch to TERMINATING temporarily until the set is completely removed. \n[Command Reference](deleteDhcpOptions)""")
@cli_util.option('--dhcp-id', required=True, help=u"""The [OCID] for the set of DHCP options.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@drg_group.command(name=cli_util.override('virtual_network.delete_drg.command_name', 'delete'), help=u"""Deletes the specified DRG. The DRG must not be attached to a VCN or be connected to your on-premise network. Also, there must not be a route table that lists the DRG as a target. This is an asynchronous operation. The DRG's `lifecycleState` will change to TERMINATING temporarily until the DRG is completely removed. \n[Command Reference](deleteDrg)""")
@cli_util.option('--drg-id', required=True, help=u"""The [[OCID]](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@drg_attachment_group.command(name=cli_util.override('virtual_network.delete_drg_attachment.command_name', 'delete'), help=u"""Detaches a DRG from a network resource by deleting the corresponding `DrgAttachment` resource. This is an asynchronous operation. The attachment's `lifecycleState` will temporarily change to DETACHING until the attachment is completely removed. \n[Command Reference](deleteDrgAttachment)""")
@cli_util.option('--drg-attachment-id', required=True, help=u"""The [OCID] of the DRG attachment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@drg_route_distribution_statement_group.command(name=cli_util.override('virtual_network.delete_drg_route_distribution.command_name', 'delete-drg-route-distribution'), help=u"""Deletes the specified route distribution. You can't delete a route distribution currently in use by a DRG attachment or DRG route table.

Remove the DRG route distribution from a DRG attachment or DRG route table by using the \"RemoveExportDrgRouteDistribution\" or \"RemoveImportDrgRouteDistribution' operations. \n[Command Reference](deleteDrgRouteDistribution)""")
@cli_util.option('--drg-route-distribution-id', required=True, help=u"""The [OCID] of the route distribution.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_drg_route_distribution(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_route_distribution_id, if_match):

    if isinstance(drg_route_distribution_id, six.string_types) and len(drg_route_distribution_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-route-distribution-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.delete_drg_route_distribution(
        drg_route_distribution_id=drg_route_distribution_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_drg_route_distribution') and callable(getattr(client, 'get_drg_route_distribution')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_drg_route_distribution(drg_route_distribution_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@internal_public_ip_group.command(name=cli_util.override('virtual_network.delete_drg_route_table.command_name', 'delete-drg-route-table'), help=u"""Deletes the specified DRG route table. There must not be any DRG attachments assigned. \n[Command Reference](deleteDrgRouteTable)""")
@cli_util.option('--drg-route-table-id', required=True, help=u"""The [OCID] of the DRG route table.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_drg_route_table(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_route_table_id, if_match):

    if isinstance(drg_route_table_id, six.string_types) and len(drg_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-route-table-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.delete_drg_route_table(
        drg_route_table_id=drg_route_table_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_drg_route_table') and callable(getattr(client, 'get_drg_route_table')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_drg_route_table(drg_route_table_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@internet_gateway_group.command(name=cli_util.override('virtual_network.delete_internet_gateway.command_name', 'delete'), help=u"""Deletes the specified internet gateway. The internet gateway does not have to be disabled, but there must not be a route table that lists it as a target.

This is an asynchronous operation. The gateway's `lifecycleState` will change to TERMINATING temporarily until the gateway is completely removed. \n[Command Reference](deleteInternetGateway)""")
@cli_util.option('--ig-id', required=True, help=u"""The [OCID] of the internet gateway.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@ip_sec_connection_group.command(name=cli_util.override('virtual_network.delete_ip_sec_connection.command_name', 'delete'), help=u"""Deletes the specified IPSec connection. If your goal is to disable the IPSec VPN between your VCN and on-premises network, it's easiest to simply detach the DRG but keep all the IPSec VPN components intact. If you were to delete all the components and then later need to create an IPSec VPN again, you would need to configure your on-premises router again with the new information returned from [CreateIPSecConnection].

This is an asynchronous operation. The connection's `lifecycleState` will change to TERMINATING temporarily until the connection is completely removed. \n[Command Reference](deleteIPSecConnection)""")
@cli_util.option('--ipsc-id', required=True, help=u"""The [OCID] of the IPSec connection.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@ipv6_group.command(name=cli_util.override('virtual_network.delete_ipv6.command_name', 'delete'), help=u"""Unassigns and deletes the specified IPv6. You must specify the object's [OCID]. The IPv6 address is returned to the subnet's pool of available addresses. \n[Command Reference](deleteIpv6)""")
@cli_util.option('--ipv6-id', required=True, help=u"""The [OCID] of the IPv6.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_ipv6(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, ipv6_id, if_match):

    if isinstance(ipv6_id, six.string_types) and len(ipv6_id.strip()) == 0:
        raise click.UsageError('Parameter --ipv6-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.delete_ipv6(
        ipv6_id=ipv6_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_ipv6') and callable(getattr(client, 'get_ipv6')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_ipv6(ipv6_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@local_peering_gateway_group.command(name=cli_util.override('virtual_network.delete_local_peering_gateway.command_name', 'delete'), help=u"""Deletes the specified local peering gateway (LPG).

This is an asynchronous operation; the local peering gateway's `lifecycleState` changes to TERMINATING temporarily until the local peering gateway is completely removed. \n[Command Reference](deleteLocalPeeringGateway)""")
@cli_util.option('--local-peering-gateway-id', required=True, help=u"""The [OCID] of the local peering gateway.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@nat_gateway_group.command(name=cli_util.override('virtual_network.delete_nat_gateway.command_name', 'delete'), help=u"""Deletes the specified NAT gateway. The NAT gateway does not have to be disabled, but there must not be a route rule that lists the NAT gateway as a target.

This is an asynchronous operation. The NAT gateway's `lifecycleState` will change to TERMINATING temporarily until the NAT gateway is completely removed. \n[Command Reference](deleteNatGateway)""")
@cli_util.option('--nat-gateway-id', required=True, help=u"""The NAT gateway's [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@network_security_group_group.command(name=cli_util.override('virtual_network.delete_network_security_group.command_name', 'delete'), help=u"""Deletes the specified network security group. The group must not contain any VNICs.

To get a list of the VNICs in a network security group, use [ListNetworkSecurityGroupVnics]. Each returned [NetworkSecurityGroupVnic] object contains both the OCID of the VNIC and the OCID of the VNIC's parent resource (for example, the Compute instance that the VNIC is attached to). \n[Command Reference](deleteNetworkSecurityGroup)""")
@cli_util.option('--network-security-group-id', required=True, help=u"""The [OCID] of the network security group.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_network_security_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, network_security_group_id, if_match):

    if isinstance(network_security_group_id, six.string_types) and len(network_security_group_id.strip()) == 0:
        raise click.UsageError('Parameter --network-security-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.delete_network_security_group(
        network_security_group_id=network_security_group_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_network_security_group') and callable(getattr(client, 'get_network_security_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_network_security_group(network_security_group_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@private_ip_group.command(name=cli_util.override('virtual_network.delete_private_ip.command_name', 'delete'), help=u"""Unassigns and deletes the specified private IP. You must specify the object's OCID. The private IP address is returned to the subnet's pool of available addresses.

This operation cannot be used with primary private IPs, which are automatically unassigned and deleted when the VNIC is terminated.

**Important:** If a secondary private IP is the [target of a route rule], unassigning it from the VNIC causes that route rule to blackhole and the traffic will be dropped. \n[Command Reference](deletePrivateIp)""")
@cli_util.option('--private-ip-id', required=True, help=u"""The [OCID] of the private IP.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.delete_private_ip(
        private_ip_id=private_ip_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_group.command(name=cli_util.override('virtual_network.delete_public_ip.command_name', 'delete'), help=u"""Unassigns and deletes the specified public IP (either ephemeral or reserved). You must specify the object's OCID. The public IP address is returned to the Oracle Cloud Infrastructure public IP pool.

**Note:** You cannot update, unassign, or delete the public IP that Oracle automatically assigned to an entity for you (such as a load balancer or NAT gateway). The public IP is automatically deleted if the assigned entity is terminated.

For an assigned reserved public IP, the initial unassignment portion of this operation is asynchronous. Poll the public IP's `lifecycleState` to determine if the operation succeeded.

If you want to simply unassign a reserved public IP and return it to your pool of reserved public IPs, instead use [UpdatePublicIp]. \n[Command Reference](deletePublicIp)""")
@cli_util.option('--public-ip-id', required=True, help=u"""The [OCID] of the public IP.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "ASSIGNING", "ASSIGNED", "UNASSIGNING", "UNASSIGNED", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@public_ip_pool_group.command(name=cli_util.override('virtual_network.delete_public_ip_pool.command_name', 'delete'), help=u"""Deletes the specified public IP pool. To delete a public IP pool it must not have any active IP address allocations. You must specify the object's [OCID] when deleting an IP pool. \n[Command Reference](deletePublicIpPool)""")
@cli_util.option('--public-ip-pool-id', required=True, help=u"""The [OCID] of the public IP pool.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["INACTIVE", "UPDATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_public_ip_pool(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, public_ip_pool_id, if_match):

    if isinstance(public_ip_pool_id, six.string_types) and len(public_ip_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --public-ip-pool-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.delete_public_ip_pool(
        public_ip_pool_id=public_ip_pool_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_public_ip_pool') and callable(getattr(client, 'get_public_ip_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_public_ip_pool(public_ip_pool_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@remote_peering_connection_group.command(name=cli_util.override('virtual_network.delete_remote_peering_connection.command_name', 'delete'), help=u"""Deletes the remote peering connection (RPC).

This is an asynchronous operation; the RPC's `lifecycleState` changes to TERMINATING temporarily until the RPC is completely removed. \n[Command Reference](deleteRemotePeeringConnection)""")
@cli_util.option('--remote-peering-connection-id', required=True, help=u"""The [OCID] of the remote peering connection (RPC).""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "PROVISIONING", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@route_table_group.command(name=cli_util.override('virtual_network.delete_route_table.command_name', 'delete'), help=u"""Deletes the specified route table, but only if it's not associated with a subnet. You can't delete a VCN's default route table.

This is an asynchronous operation. The route table's `lifecycleState` will change to TERMINATING temporarily until the route table is completely removed. \n[Command Reference](deleteRouteTable)""")
@cli_util.option('--rt-id', required=True, help=u"""The [OCID] of the route table.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@security_list_group.command(name=cli_util.override('virtual_network.delete_security_list.command_name', 'delete'), help=u"""Deletes the specified security list, but only if it's not associated with a subnet. You can't delete a VCN's default security list.

This is an asynchronous operation. The security list's `lifecycleState` will change to TERMINATING temporarily until the security list is completely removed. \n[Command Reference](deleteSecurityList)""")
@cli_util.option('--security-list-id', required=True, help=u"""The [OCID] of the security list.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@service_gateway_group.command(name=cli_util.override('virtual_network.delete_service_gateway.command_name', 'delete'), help=u"""Deletes the specified service gateway. There must not be a route table that lists the service gateway as a target. \n[Command Reference](deleteServiceGateway)""")
@cli_util.option('--service-gateway-id', required=True, help=u"""The service gateway's [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@subnet_group.command(name=cli_util.override('virtual_network.delete_subnet.command_name', 'delete'), help=u"""Deletes the specified subnet, but only if there are no instances in the subnet. This is an asynchronous operation. The subnet's `lifecycleState` will change to TERMINATING temporarily. If there are any instances in the subnet, the state will instead change back to AVAILABLE. \n[Command Reference](deleteSubnet)""")
@cli_util.option('--subnet-id', required=True, help=u"""The [OCID] of the subnet.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vcn_group.command(name=cli_util.override('virtual_network.delete_vcn.command_name', 'delete'), help=u"""Deletes the specified VCN. The VCN must be empty and have no attached gateways. This is an asynchronous operation. The VCN's `lifecycleState` will change to TERMINATING temporarily until the VCN is completely removed. \n[Command Reference](deleteVcn)""")
@cli_util.option('--vcn-id', required=True, help=u"""The [OCID] of the VCN.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@virtual_circuit_group.command(name=cli_util.override('virtual_network.delete_virtual_circuit.command_name', 'delete'), help=u"""Deletes the specified virtual circuit.

**Important:** If you're using FastConnect via a provider, make sure to also terminate the connection with the provider, or else the provider may continue to bill you. \n[Command Reference](deleteVirtualCircuit)""")
@cli_util.option('--virtual-circuit-id', required=True, help=u"""The [OCID] of the virtual circuit.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_PROVIDER", "VERIFYING", "PROVISIONING", "PROVISIONED", "FAILED", "INACTIVE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vlan_group.command(name=cli_util.override('virtual_network.delete_vlan.command_name', 'delete'), help=u"""Deletes the specified VLAN, but only if there are no VNICs in the VLAN. \n[Command Reference](deleteVlan)""")
@cli_util.option('--vlan-id', required=True, help=u"""The [OCID] of the VLAN.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_vlan(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vlan_id, if_match):

    if isinstance(vlan_id, six.string_types) and len(vlan_id.strip()) == 0:
        raise click.UsageError('Parameter --vlan-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.delete_vlan(
        vlan_id=vlan_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vlan') and callable(getattr(client, 'get_vlan')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_vlan(vlan_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@service_gateway_group.command(name=cli_util.override('virtual_network.detach_service_id.command_name', 'detach'), help=u"""Removes the specified [Service] from the list of enabled `Service` objects for the specified gateway. You do not need to remove any route rules that specify this `Service` object's `cidrBlock` as the destination CIDR. However, consider removing the rules if your intent is to permanently disable use of the `Service` through this service gateway.

**Note:** The `DetachServiceId` operation is an easy way to remove an individual `Service` from the service gateway. Compare it with [UpdateServiceGateway], which replaces the entire existing list of enabled `Service` objects with the list that you provide in the `Update` call. `UpdateServiceGateway` also lets you block all traffic through the service gateway without having to remove each of the individual `Service` objects. \n[Command Reference](detachServiceId)""")
@cli_util.option('--service-gateway-id', required=True, help=u"""The service gateway's [OCID].""")
@cli_util.option('--service-id', required=True, help=u"""The [OCID] of the [Service].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    _details = {}
    _details['serviceId'] = service_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.detach_service_id(
        service_gateway_id=service_gateway_id,
        detach_service_details=_details,
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


@drg_group.command(name=cli_util.override('virtual_network.get_all_drg_attachments.command_name', 'get-all-drg-attachments'), help=u"""Returns a complete list of DRG attachments that belong to a particular DRG. \n[Command Reference](getAllDrgAttachments)""")
@cli_util.option('--drg-id', required=True, help=u"""The [[OCID]](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--attachment-type', type=custom_types.CliCaseInsensitiveChoice(["VCN", "VIRTUAL_CIRCUIT", "REMOTE_PEERING_CONNECTION", "IPSEC_TUNNEL", "ALL"]), help=u"""The type for the network resource attached to the DRG.""")
@cli_util.option('--is-cross-tenancy', type=click.BOOL, help=u"""Whether the DRG attachment lives in a different tenancy than the DRG.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[DrgAttachmentInfo]'})
@cli_util.wrap_exceptions
def get_all_drg_attachments(ctx, from_json, drg_id, limit, page, attachment_type, is_cross_tenancy):

    if isinstance(drg_id, six.string_types) and len(drg_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if attachment_type is not None:
        kwargs['attachment_type'] = attachment_type
    if is_cross_tenancy is not None:
        kwargs['is_cross_tenancy'] = is_cross_tenancy
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_all_drg_attachments(
        drg_id=drg_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@byoip_range_group.command(name=cli_util.override('virtual_network.get_byoip_range.command_name', 'get'), help=u"""Gets the `ByoipRange` resource. You must specify the [OCID]. \n[Command Reference](getByoipRange)""")
@cli_util.option('--byoip-range-id', required=True, help=u"""The [OCID] of the `ByoipRange` resource containing the BYOIP CIDR block.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ByoipRange'})
@cli_util.wrap_exceptions
def get_byoip_range(ctx, from_json, byoip_range_id):

    if isinstance(byoip_range_id, six.string_types) and len(byoip_range_id.strip()) == 0:
        raise click.UsageError('Parameter --byoip-range-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_byoip_range(
        byoip_range_id=byoip_range_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cpe_group.command(name=cli_util.override('virtual_network.get_cpe.command_name', 'get'), help=u"""Gets the specified CPE's information. \n[Command Reference](getCpe)""")
@cli_util.option('--cpe-id', required=True, help=u"""The [OCID] of the CPE.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Cpe'})
@cli_util.wrap_exceptions
def get_cpe(ctx, from_json, cpe_id):

    if isinstance(cpe_id, six.string_types) and len(cpe_id.strip()) == 0:
        raise click.UsageError('Parameter --cpe-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_cpe(
        cpe_id=cpe_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cpe_group.command(name=cli_util.override('virtual_network.get_cpe_device_config_content.command_name', 'get-cpe-device-config-content'), help=u"""Renders a set of CPE configuration content that can help a network engineer configure the actual CPE device (for example, a hardware router) represented by the specified [Cpe] object.

The rendered content is specific to the type of CPE device (for example, Cisco ASA). Therefore the [Cpe] must have the CPE's device type specified by the `cpeDeviceShapeId` attribute. The content optionally includes answers that the customer provides (see [UpdateTunnelCpeDeviceConfig]), merged with a template of other information specific to the CPE device type.

The operation returns configuration information for *all* of the [IPSecConnection] objects that use the specified CPE. Here are similar operations:

  * [GetIpsecCpeDeviceConfigContent]   returns CPE configuration content for all tunnels in a single IPSec connection.   * [GetTunnelCpeDeviceConfigContent]   returns CPE configuration content for a specific tunnel within an IPSec connection. \n[Command Reference](getCpeDeviceConfigContent)""")
@cli_util.option('--cpe-id', required=True, help=u"""The [OCID] of the CPE.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_cpe_device_config_content(ctx, from_json, file, cpe_id):

    if isinstance(cpe_id, six.string_types) and len(cpe_id.strip()) == 0:
        raise click.UsageError('Parameter --cpe-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_cpe_device_config_content(
        cpe_id=cpe_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@cpe_device_shape_detail_group.command(name=cli_util.override('virtual_network.get_cpe_device_shape.command_name', 'get-cpe-device-shape'), help=u"""Gets the detailed information about the specified CPE device type. This might include a set of questions that are specific to the particular CPE device type. The customer must supply answers to those questions (see [UpdateTunnelCpeDeviceConfig]). The service merges the answers with a template of other information for the CPE device type. The following operations return the merged content:

  * [GetCpeDeviceConfigContent]   * [GetIpsecCpeDeviceConfigContent]   * [GetTunnelCpeDeviceConfigContent] \n[Command Reference](getCpeDeviceShape)""")
@cli_util.option('--cpe-device-shape-id', required=True, help=u"""The [OCID] of the CPE device shape.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'CpeDeviceShapeDetail'})
@cli_util.wrap_exceptions
def get_cpe_device_shape(ctx, from_json, cpe_device_shape_id):

    if isinstance(cpe_device_shape_id, six.string_types) and len(cpe_device_shape_id.strip()) == 0:
        raise click.UsageError('Parameter --cpe-device-shape-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_cpe_device_shape(
        cpe_device_shape_id=cpe_device_shape_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cross_connect_group.command(name=cli_util.override('virtual_network.get_cross_connect.command_name', 'get'), help=u"""Gets the specified cross-connect's information. \n[Command Reference](getCrossConnect)""")
@cli_util.option('--cross-connect-id', required=True, help=u"""The [OCID] of the cross-connect.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'CrossConnect'})
@cli_util.wrap_exceptions
def get_cross_connect(ctx, from_json, cross_connect_id):

    if isinstance(cross_connect_id, six.string_types) and len(cross_connect_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_cross_connect(
        cross_connect_id=cross_connect_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cross_connect_group_group.command(name=cli_util.override('virtual_network.get_cross_connect_group.command_name', 'get'), help=u"""Gets the specified cross-connect group's information. \n[Command Reference](getCrossConnectGroup)""")
@cli_util.option('--cross-connect-group-id', required=True, help=u"""The [OCID] of the cross-connect group.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'CrossConnectGroup'})
@cli_util.wrap_exceptions
def get_cross_connect_group(ctx, from_json, cross_connect_group_id):

    if isinstance(cross_connect_group_id, six.string_types) and len(cross_connect_group_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-group-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_cross_connect_group(
        cross_connect_group_id=cross_connect_group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@letter_of_authority_group.command(name=cli_util.override('virtual_network.get_cross_connect_letter_of_authority.command_name', 'get-cross-connect'), help=u"""Gets the Letter of Authority for the specified cross-connect. \n[Command Reference](getCrossConnectLetterOfAuthority)""")
@cli_util.option('--cross-connect-id', required=True, help=u"""The [OCID] of the cross-connect.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'LetterOfAuthority'})
@cli_util.wrap_exceptions
def get_cross_connect_letter_of_authority(ctx, from_json, cross_connect_id):

    if isinstance(cross_connect_id, six.string_types) and len(cross_connect_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_cross_connect_letter_of_authority(
        cross_connect_id=cross_connect_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cross_connect_status_group.command(name=cli_util.override('virtual_network.get_cross_connect_status.command_name', 'get'), help=u"""Gets the status of the specified cross-connect. \n[Command Reference](getCrossConnectStatus)""")
@cli_util.option('--cross-connect-id', required=True, help=u"""The [OCID] of the cross-connect.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'CrossConnectStatus'})
@cli_util.wrap_exceptions
def get_cross_connect_status(ctx, from_json, cross_connect_id):

    if isinstance(cross_connect_id, six.string_types) and len(cross_connect_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_cross_connect_status(
        cross_connect_id=cross_connect_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dhcp_options_group.command(name=cli_util.override('virtual_network.get_dhcp_options.command_name', 'get'), help=u"""Gets the specified set of DHCP options. \n[Command Reference](getDhcpOptions)""")
@cli_util.option('--dhcp-id', required=True, help=u"""The [OCID] for the set of DHCP options.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'DhcpOptions'})
@cli_util.wrap_exceptions
def get_dhcp_options(ctx, from_json, dhcp_id):

    if isinstance(dhcp_id, six.string_types) and len(dhcp_id.strip()) == 0:
        raise click.UsageError('Parameter --dhcp-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_dhcp_options(
        dhcp_id=dhcp_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@drg_group.command(name=cli_util.override('virtual_network.get_drg.command_name', 'get'), help=u"""Gets the specified DRG's information. \n[Command Reference](getDrg)""")
@cli_util.option('--drg-id', required=True, help=u"""The [[OCID]](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Drg'})
@cli_util.wrap_exceptions
def get_drg(ctx, from_json, drg_id):

    if isinstance(drg_id, six.string_types) and len(drg_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_drg(
        drg_id=drg_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@drg_attachment_group.command(name=cli_util.override('virtual_network.get_drg_attachment.command_name', 'get'), help=u"""Gets the `DrgAttachment` resource. \n[Command Reference](getDrgAttachment)""")
@cli_util.option('--drg-attachment-id', required=True, help=u"""The [OCID] of the DRG attachment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'DrgAttachment'})
@cli_util.wrap_exceptions
def get_drg_attachment(ctx, from_json, drg_attachment_id):

    if isinstance(drg_attachment_id, six.string_types) and len(drg_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_drg_attachment(
        drg_attachment_id=drg_attachment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@drg_redundancy_status_group.command(name=cli_util.override('virtual_network.get_drg_redundancy_status.command_name', 'get'), help=u"""Gets the redundancy status for the specified DRG. For more information, see [Redundancy Remedies]. \n[Command Reference](getDrgRedundancyStatus)""")
@cli_util.option('--drg-id', required=True, help=u"""The [[OCID]](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'DrgRedundancyStatus'})
@cli_util.wrap_exceptions
def get_drg_redundancy_status(ctx, from_json, drg_id):

    if isinstance(drg_id, six.string_types) and len(drg_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_drg_redundancy_status(
        drg_id=drg_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@drg_route_distribution_group.command(name=cli_util.override('virtual_network.get_drg_route_distribution.command_name', 'get'), help=u"""Gets the specified route distribution's information. \n[Command Reference](getDrgRouteDistribution)""")
@cli_util.option('--drg-route-distribution-id', required=True, help=u"""The [OCID] of the route distribution.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'DrgRouteDistribution'})
@cli_util.wrap_exceptions
def get_drg_route_distribution(ctx, from_json, drg_route_distribution_id):

    if isinstance(drg_route_distribution_id, six.string_types) and len(drg_route_distribution_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-route-distribution-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_drg_route_distribution(
        drg_route_distribution_id=drg_route_distribution_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@drg_route_table_group.command(name=cli_util.override('virtual_network.get_drg_route_table.command_name', 'get'), help=u"""Gets the specified DRG route table's information. \n[Command Reference](getDrgRouteTable)""")
@cli_util.option('--drg-route-table-id', required=True, help=u"""The [OCID] of the DRG route table.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'DrgRouteTable'})
@cli_util.wrap_exceptions
def get_drg_route_table(ctx, from_json, drg_route_table_id):

    if isinstance(drg_route_table_id, six.string_types) and len(drg_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-route-table-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_drg_route_table(
        drg_route_table_id=drg_route_table_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fast_connect_provider_service_group.command(name=cli_util.override('virtual_network.get_fast_connect_provider_service.command_name', 'get'), help=u"""Gets the specified provider service. For more information, see [FastConnect Overview]. \n[Command Reference](getFastConnectProviderService)""")
@cli_util.option('--provider-service-id', required=True, help=u"""The [OCID] of the provider service.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'FastConnectProviderService'})
@cli_util.wrap_exceptions
def get_fast_connect_provider_service(ctx, from_json, provider_service_id):

    if isinstance(provider_service_id, six.string_types) and len(provider_service_id.strip()) == 0:
        raise click.UsageError('Parameter --provider-service-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_fast_connect_provider_service(
        provider_service_id=provider_service_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fast_connect_provider_service_key_group.command(name=cli_util.override('virtual_network.get_fast_connect_provider_service_key.command_name', 'get'), help=u"""Gets the specified provider service key's information. Use this operation to validate a provider service key. An invalid key returns a 404 error. \n[Command Reference](getFastConnectProviderServiceKey)""")
@cli_util.option('--provider-service-id', required=True, help=u"""The [OCID] of the provider service.""")
@cli_util.option('--provider-service-key-name', required=True, help=u"""The provider service key that the provider gives you when you set up a virtual circuit connection from the provider to Oracle Cloud Infrastructure. You can set up that connection and get your provider service key at the provider's website or portal. For the portal location, see the `description` attribute of the [FastConnectProviderService].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'FastConnectProviderServiceKey'})
@cli_util.wrap_exceptions
def get_fast_connect_provider_service_key(ctx, from_json, provider_service_id, provider_service_key_name):

    if isinstance(provider_service_id, six.string_types) and len(provider_service_id.strip()) == 0:
        raise click.UsageError('Parameter --provider-service-id cannot be whitespace or empty string')

    if isinstance(provider_service_key_name, six.string_types) and len(provider_service_key_name.strip()) == 0:
        raise click.UsageError('Parameter --provider-service-key-name cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_fast_connect_provider_service_key(
        provider_service_id=provider_service_id,
        provider_service_key_name=provider_service_key_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@internet_gateway_group.command(name=cli_util.override('virtual_network.get_internet_gateway.command_name', 'get'), help=u"""Gets the specified internet gateway's information. \n[Command Reference](getInternetGateway)""")
@cli_util.option('--ig-id', required=True, help=u"""The [OCID] of the internet gateway.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InternetGateway'})
@cli_util.wrap_exceptions
def get_internet_gateway(ctx, from_json, ig_id):

    if isinstance(ig_id, six.string_types) and len(ig_id.strip()) == 0:
        raise click.UsageError('Parameter --ig-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_internet_gateway(
        ig_id=ig_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ip_sec_connection_group.command(name=cli_util.override('virtual_network.get_ip_sec_connection.command_name', 'get'), help=u"""Gets the specified IPSec connection's basic information, including the static routes for the on-premises router. If you want the status of the connection (whether it's up or down), use [GetIPSecConnectionTunnel]. \n[Command Reference](getIPSecConnection)""")
@cli_util.option('--ipsc-id', required=True, help=u"""The [OCID] of the IPSec connection.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'IPSecConnection'})
@cli_util.wrap_exceptions
def get_ip_sec_connection(ctx, from_json, ipsc_id):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_ip_sec_connection(
        ipsc_id=ipsc_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ip_sec_connection_device_config_group.command(name=cli_util.override('virtual_network.get_ip_sec_connection_device_config.command_name', 'get'), help=u"""Deprecated. To get tunnel information, instead use:

* [GetIPSecConnectionTunnel] * [GetIPSecConnectionTunnelSharedSecret] \n[Command Reference](getIPSecConnectionDeviceConfig)""")
@cli_util.option('--ipsc-id', required=True, help=u"""The [OCID] of the IPSec connection.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'IPSecConnectionDeviceConfig'})
@cli_util.wrap_exceptions
def get_ip_sec_connection_device_config(ctx, from_json, ipsc_id):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_ip_sec_connection_device_config(
        ipsc_id=ipsc_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ip_sec_connection_device_status_group.command(name=cli_util.override('virtual_network.get_ip_sec_connection_device_status.command_name', 'get'), help=u"""Deprecated. To get the tunnel status, instead use [GetIPSecConnectionTunnel]. \n[Command Reference](getIPSecConnectionDeviceStatus)""")
@cli_util.option('--ipsc-id', required=True, help=u"""The [OCID] of the IPSec connection.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'IPSecConnectionDeviceStatus'})
@cli_util.wrap_exceptions
def get_ip_sec_connection_device_status(ctx, from_json, ipsc_id):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_ip_sec_connection_device_status(
        ipsc_id=ipsc_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ip_sec_connection_tunnel_group.command(name=cli_util.override('virtual_network.get_ip_sec_connection_tunnel.command_name', 'get'), help=u"""Gets the specified tunnel's information. The resulting object does not include the tunnel's shared secret (pre-shared key). To retrieve that, use [GetIPSecConnectionTunnelSharedSecret]. \n[Command Reference](getIPSecConnectionTunnel)""")
@cli_util.option('--ipsc-id', required=True, help=u"""The [OCID] of the IPSec connection.""")
@cli_util.option('--tunnel-id', required=True, help=u"""The [OCID] of the tunnel.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'IPSecConnectionTunnel'})
@cli_util.wrap_exceptions
def get_ip_sec_connection_tunnel(ctx, from_json, ipsc_id, tunnel_id):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')

    if isinstance(tunnel_id, six.string_types) and len(tunnel_id.strip()) == 0:
        raise click.UsageError('Parameter --tunnel-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_ip_sec_connection_tunnel(
        ipsc_id=ipsc_id,
        tunnel_id=tunnel_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ip_sec_connection_tunnel_shared_secret_group.command(name=cli_util.override('virtual_network.get_ip_sec_connection_tunnel_shared_secret.command_name', 'get'), help=u"""Gets the specified tunnel's shared secret (pre-shared key). To get other information about the tunnel, use [GetIPSecConnectionTunnel]. \n[Command Reference](getIPSecConnectionTunnelSharedSecret)""")
@cli_util.option('--ipsc-id', required=True, help=u"""The [OCID] of the IPSec connection.""")
@cli_util.option('--tunnel-id', required=True, help=u"""The [OCID] of the tunnel.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'IPSecConnectionTunnelSharedSecret'})
@cli_util.wrap_exceptions
def get_ip_sec_connection_tunnel_shared_secret(ctx, from_json, ipsc_id, tunnel_id):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')

    if isinstance(tunnel_id, six.string_types) and len(tunnel_id.strip()) == 0:
        raise click.UsageError('Parameter --tunnel-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_ip_sec_connection_tunnel_shared_secret(
        ipsc_id=ipsc_id,
        tunnel_id=tunnel_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ip_sec_connection_group.command(name=cli_util.override('virtual_network.get_ipsec_cpe_device_config_content.command_name', 'get-ipsec-cpe-device-config-content'), help=u"""Renders a set of CPE configuration content for the specified IPSec connection (for all the tunnels in the connection). The content helps a network engineer configure the actual CPE device (for example, a hardware router) that the specified IPSec connection terminates on.

The rendered content is specific to the type of CPE device (for example, Cisco ASA). Therefore the [Cpe] used by the specified [IPSecConnection] must have the CPE's device type specified by the `cpeDeviceShapeId` attribute. The content optionally includes answers that the customer provides (see [UpdateTunnelCpeDeviceConfig]), merged with a template of other information specific to the CPE device type.

The operation returns configuration information for all tunnels in the single specified [IPSecConnection] object. Here are other similar operations:

  * [GetTunnelCpeDeviceConfigContent]   returns CPE configuration content for a specific tunnel within an IPSec connection.   * [GetCpeDeviceConfigContent]   returns CPE configuration content for *all* IPSec connections that use a specific CPE. \n[Command Reference](getIpsecCpeDeviceConfigContent)""")
@cli_util.option('--ipsc-id', required=True, help=u"""The [OCID] of the IPSec connection.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_ipsec_cpe_device_config_content(ctx, from_json, file, ipsc_id):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_ipsec_cpe_device_config_content(
        ipsc_id=ipsc_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@ipv6_group.command(name=cli_util.override('virtual_network.get_ipv6.command_name', 'get'), help=u"""Gets the specified IPv6. You must specify the object's [OCID]. Alternatively, you can get the object by using [ListIpv6s] with the IPv6 address (for example, 2001:0db8:0123:1111:98fe:dcba:9876:4321) and subnet OCID. \n[Command Reference](getIpv6)""")
@cli_util.option('--ipv6-id', required=True, help=u"""The [OCID] of the IPv6.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Ipv6'})
@cli_util.wrap_exceptions
def get_ipv6(ctx, from_json, ipv6_id):

    if isinstance(ipv6_id, six.string_types) and len(ipv6_id.strip()) == 0:
        raise click.UsageError('Parameter --ipv6-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_ipv6(
        ipv6_id=ipv6_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@local_peering_gateway_group.command(name=cli_util.override('virtual_network.get_local_peering_gateway.command_name', 'get'), help=u"""Gets the specified local peering gateway's information. \n[Command Reference](getLocalPeeringGateway)""")
@cli_util.option('--local-peering-gateway-id', required=True, help=u"""The [OCID] of the local peering gateway.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'LocalPeeringGateway'})
@cli_util.wrap_exceptions
def get_local_peering_gateway(ctx, from_json, local_peering_gateway_id):

    if isinstance(local_peering_gateway_id, six.string_types) and len(local_peering_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --local-peering-gateway-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_local_peering_gateway(
        local_peering_gateway_id=local_peering_gateway_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@nat_gateway_group.command(name=cli_util.override('virtual_network.get_nat_gateway.command_name', 'get'), help=u"""Gets the specified NAT gateway's information. \n[Command Reference](getNatGateway)""")
@cli_util.option('--nat-gateway-id', required=True, help=u"""The NAT gateway's [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'NatGateway'})
@cli_util.wrap_exceptions
def get_nat_gateway(ctx, from_json, nat_gateway_id):

    if isinstance(nat_gateway_id, six.string_types) and len(nat_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --nat-gateway-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_nat_gateway(
        nat_gateway_id=nat_gateway_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@network_security_group_group.command(name=cli_util.override('virtual_network.get_network_security_group.command_name', 'get'), help=u"""Gets the specified network security group's information.

To list the VNICs in an NSG, see [ListNetworkSecurityGroupVnics].

To list the security rules in an NSG, see [ListNetworkSecurityGroupSecurityRules]. \n[Command Reference](getNetworkSecurityGroup)""")
@cli_util.option('--network-security-group-id', required=True, help=u"""The [OCID] of the network security group.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'NetworkSecurityGroup'})
@cli_util.wrap_exceptions
def get_network_security_group(ctx, from_json, network_security_group_id):

    if isinstance(network_security_group_id, six.string_types) and len(network_security_group_id.strip()) == 0:
        raise click.UsageError('Parameter --network-security-group-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_network_security_group(
        network_security_group_id=network_security_group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@networking_topology_group.command(name=cli_util.override('virtual_network.get_networking_topology.command_name', 'get'), help=u"""Gets a virtual networking topology for the current region. \n[Command Reference](getNetworkingTopology)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["ANY", "ACCESSIBLE"]), help=u"""Valid values are `ANY` and `ACCESSIBLE`. The default is `ANY`. Setting this to `ACCESSIBLE` returns only compartments for which a user has INSPECT permissions, either directly or indirectly (permissions can be on a resource in a subcompartment). A restricted set of fields is returned for compartments in which a user has indirect INSPECT permissions.

When set to `ANY` permissions are not checked.""")
@cli_util.option('--query-compartment-subtree', type=click.BOOL, help=u"""When set to true, the hierarchy of compartments is traversed and the specified compartment and its subcompartments are inspected depending on the the setting of `accessLevel`. Default is false.""")
@cli_util.option('--if-none-match', help=u"""For querying if there is a cached value on the server. The If-None-Match HTTP request header makes the request conditional. For GET and HEAD methods, the server will send back the requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones. For other methods, the request will be processed only if the eventually existing resource's ETag doesn't match any of the values listed.""")
@cli_util.option('--cache-control', help=u"""The Cache-Control HTTP header holds directives (instructions) for caching in both requests and responses.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'NetworkingTopology'})
@cli_util.wrap_exceptions
def get_networking_topology(ctx, from_json, compartment_id, access_level, query_compartment_subtree, if_none_match, cache_control):

    kwargs = {}
    if access_level is not None:
        kwargs['access_level'] = access_level
    if query_compartment_subtree is not None:
        kwargs['query_compartment_subtree'] = query_compartment_subtree
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if cache_control is not None:
        kwargs['cache_control'] = cache_control
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_networking_topology(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@private_ip_group.command(name=cli_util.override('virtual_network.get_private_ip.command_name', 'get'), help=u"""Gets the specified private IP. You must specify the object's OCID. Alternatively, you can get the object by using [ListPrivateIps] with the private IP address (for example, 10.0.3.3) and subnet OCID. \n[Command Reference](getPrivateIp)""")
@cli_util.option('--private-ip-id', required=True, help=u"""The [OCID] of the private IP.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PrivateIp'})
@cli_util.wrap_exceptions
def get_private_ip(ctx, from_json, private_ip_id):

    if isinstance(private_ip_id, six.string_types) and len(private_ip_id.strip()) == 0:
        raise click.UsageError('Parameter --private-ip-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_private_ip(
        private_ip_id=private_ip_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_group.command(name=cli_util.override('virtual_network.get_public_ip.command_name', 'get'), help=u"""Gets the specified public IP. You must specify the object's OCID.

Alternatively, you can get the object by using [GetPublicIpByIpAddress] with the public IP address (for example, 203.0.113.2).

Or you can use [GetPublicIpByPrivateIpId] with the OCID of the private IP that the public IP is assigned to.

**Note:** If you're fetching a reserved public IP that is in the process of being moved to a different private IP, the service returns the public IP object with `lifecycleState` = ASSIGNING and `assignedEntityId` = OCID of the target private IP. \n[Command Reference](getPublicIp)""")
@cli_util.option('--public-ip-id', required=True, help=u"""The [OCID] of the public IP.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PublicIp'})
@cli_util.wrap_exceptions
def get_public_ip(ctx, from_json, public_ip_id):

    if isinstance(public_ip_id, six.string_types) and len(public_ip_id.strip()) == 0:
        raise click.UsageError('Parameter --public-ip-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_public_ip(
        public_ip_id=public_ip_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_group.command(name=cli_util.override('virtual_network.get_public_ip_by_ip_address.command_name', 'get-public-ip-by-ip-address'), help=u"""Gets the public IP based on the public IP address (for example, 203.0.113.2).

**Note:** If you're fetching a reserved public IP that is in the process of being moved to a different private IP, the service returns the public IP object with `lifecycleState` = ASSIGNING and `assignedEntityId` = OCID of the target private IP. \n[Command Reference](getPublicIpByIpAddress)""")
@cli_util.option('--ip-address', required=True, help=u"""The public IP address. Example: 203.0.113.2""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PublicIp'})
@cli_util.wrap_exceptions
def get_public_ip_by_ip_address(ctx, from_json, ip_address):

    kwargs = {}

    _details = {}
    _details['ipAddress'] = ip_address

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_public_ip_by_ip_address(
        get_public_ip_by_ip_address_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_group.command(name=cli_util.override('virtual_network.get_public_ip_by_private_ip_id.command_name', 'get-public-ip-by-private-ip-id'), help=u"""Gets the public IP assigned to the specified private IP. You must specify the OCID of the private IP. If no public IP is assigned, a 404 is returned.

**Note:** If you're fetching a reserved public IP that is in the process of being moved to a different private IP, and you provide the OCID of the original private IP, this operation returns a 404. If you instead provide the OCID of the target private IP, or if you instead call [GetPublicIp] or [GetPublicIpByIpAddress], the service returns the public IP object with `lifecycleState` = ASSIGNING and `assignedEntityId` = OCID of the target private IP. \n[Command Reference](getPublicIpByPrivateIpId)""")
@cli_util.option('--private-ip-id', required=True, help=u"""OCID of the private IP.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PublicIp'})
@cli_util.wrap_exceptions
def get_public_ip_by_private_ip_id(ctx, from_json, private_ip_id):

    kwargs = {}

    _details = {}
    _details['privateIpId'] = private_ip_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_public_ip_by_private_ip_id(
        get_public_ip_by_private_ip_id_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_pool_group.command(name=cli_util.override('virtual_network.get_public_ip_pool.command_name', 'get'), help=u"""Gets the specified `PublicIpPool` object. You must specify the object's [OCID]. \n[Command Reference](getPublicIpPool)""")
@cli_util.option('--public-ip-pool-id', required=True, help=u"""The [OCID] of the public IP pool.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PublicIpPool'})
@cli_util.wrap_exceptions
def get_public_ip_pool(ctx, from_json, public_ip_pool_id):

    if isinstance(public_ip_pool_id, six.string_types) and len(public_ip_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --public-ip-pool-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_public_ip_pool(
        public_ip_pool_id=public_ip_pool_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@remote_peering_connection_group.command(name=cli_util.override('virtual_network.get_remote_peering_connection.command_name', 'get'), help=u"""Get the specified remote peering connection's information. \n[Command Reference](getRemotePeeringConnection)""")
@cli_util.option('--remote-peering-connection-id', required=True, help=u"""The [OCID] of the remote peering connection (RPC).""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'RemotePeeringConnection'})
@cli_util.wrap_exceptions
def get_remote_peering_connection(ctx, from_json, remote_peering_connection_id):

    if isinstance(remote_peering_connection_id, six.string_types) and len(remote_peering_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --remote-peering-connection-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_remote_peering_connection(
        remote_peering_connection_id=remote_peering_connection_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@route_table_group.command(name=cli_util.override('virtual_network.get_route_table.command_name', 'get'), help=u"""Gets the specified route table's information. \n[Command Reference](getRouteTable)""")
@cli_util.option('--rt-id', required=True, help=u"""The [OCID] of the route table.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'RouteTable'})
@cli_util.wrap_exceptions
def get_route_table(ctx, from_json, rt_id):

    if isinstance(rt_id, six.string_types) and len(rt_id.strip()) == 0:
        raise click.UsageError('Parameter --rt-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_route_table(
        rt_id=rt_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@security_list_group.command(name=cli_util.override('virtual_network.get_security_list.command_name', 'get'), help=u"""Gets the specified security list's information. \n[Command Reference](getSecurityList)""")
@cli_util.option('--security-list-id', required=True, help=u"""The [OCID] of the security list.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'SecurityList'})
@cli_util.wrap_exceptions
def get_security_list(ctx, from_json, security_list_id):

    if isinstance(security_list_id, six.string_types) and len(security_list_id.strip()) == 0:
        raise click.UsageError('Parameter --security-list-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_security_list(
        security_list_id=security_list_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@service_group.command(name=cli_util.override('virtual_network.get_service.command_name', 'get'), help=u"""Gets the specified [Service] object. \n[Command Reference](getService)""")
@cli_util.option('--service-id', required=True, help=u"""The service's [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Service'})
@cli_util.wrap_exceptions
def get_service(ctx, from_json, service_id):

    if isinstance(service_id, six.string_types) and len(service_id.strip()) == 0:
        raise click.UsageError('Parameter --service-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_service(
        service_id=service_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@service_gateway_group.command(name=cli_util.override('virtual_network.get_service_gateway.command_name', 'get'), help=u"""Gets the specified service gateway's information. \n[Command Reference](getServiceGateway)""")
@cli_util.option('--service-gateway-id', required=True, help=u"""The service gateway's [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ServiceGateway'})
@cli_util.wrap_exceptions
def get_service_gateway(ctx, from_json, service_gateway_id):

    if isinstance(service_gateway_id, six.string_types) and len(service_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --service-gateway-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_service_gateway(
        service_gateway_id=service_gateway_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subnet_group.command(name=cli_util.override('virtual_network.get_subnet.command_name', 'get'), help=u"""Gets the specified subnet's information. \n[Command Reference](getSubnet)""")
@cli_util.option('--subnet-id', required=True, help=u"""The [OCID] of the subnet.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Subnet'})
@cli_util.wrap_exceptions
def get_subnet(ctx, from_json, subnet_id):

    if isinstance(subnet_id, six.string_types) and len(subnet_id.strip()) == 0:
        raise click.UsageError('Parameter --subnet-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_subnet(
        subnet_id=subnet_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tunnel_cpe_device_config_group.command(name=cli_util.override('virtual_network.get_tunnel_cpe_device_config.command_name', 'get'), help=u"""Gets the set of CPE configuration answers for the tunnel, which the customer provided in [UpdateTunnelCpeDeviceConfig]. To get the full set of content for the tunnel (any answers merged with the template of other information specific to the CPE device type), use [GetTunnelCpeDeviceConfigContent]. \n[Command Reference](getTunnelCpeDeviceConfig)""")
@cli_util.option('--ipsc-id', required=True, help=u"""The [OCID] of the IPSec connection.""")
@cli_util.option('--tunnel-id', required=True, help=u"""The [OCID] of the tunnel.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'TunnelCpeDeviceConfig'})
@cli_util.wrap_exceptions
def get_tunnel_cpe_device_config(ctx, from_json, ipsc_id, tunnel_id):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')

    if isinstance(tunnel_id, six.string_types) and len(tunnel_id.strip()) == 0:
        raise click.UsageError('Parameter --tunnel-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_tunnel_cpe_device_config(
        ipsc_id=ipsc_id,
        tunnel_id=tunnel_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tunnel_cpe_device_config_group.command(name=cli_util.override('virtual_network.get_tunnel_cpe_device_config_content.command_name', 'get-tunnel-cpe-device-config-content'), help=u"""Renders a set of CPE configuration content for the specified IPSec tunnel. The content helps a network engineer configure the actual CPE device (for example, a hardware router) that the specified IPSec tunnel terminates on.

The rendered content is specific to the type of CPE device (for example, Cisco ASA). Therefore the [Cpe] used by the specified [IPSecConnection] must have the CPE's device type specified by the `cpeDeviceShapeId` attribute. The content optionally includes answers that the customer provides (see [UpdateTunnelCpeDeviceConfig]), merged with a template of other information specific to the CPE device type.

The operation returns configuration information for only the specified IPSec tunnel. Here are other similar operations:

  * [GetIpsecCpeDeviceConfigContent]   returns CPE configuration content for all tunnels in a single IPSec connection.   * [GetCpeDeviceConfigContent]   returns CPE configuration content for *all* IPSec connections that use a specific CPE. \n[Command Reference](getTunnelCpeDeviceConfigContent)""")
@cli_util.option('--ipsc-id', required=True, help=u"""The [OCID] of the IPSec connection.""")
@cli_util.option('--tunnel-id', required=True, help=u"""The [OCID] of the tunnel.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_tunnel_cpe_device_config_content(ctx, from_json, file, ipsc_id, tunnel_id):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')

    if isinstance(tunnel_id, six.string_types) and len(tunnel_id.strip()) == 0:
        raise click.UsageError('Parameter --tunnel-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_tunnel_cpe_device_config_content(
        ipsc_id=ipsc_id,
        tunnel_id=tunnel_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@drg_group.command(name=cli_util.override('virtual_network.get_upgrade_status.command_name', 'get-upgrade-status'), help=u"""Returns the DRG upgrade status. The status can be not updated, in progress, or updated. Also indicates how much of the upgrade is completed. \n[Command Reference](getUpgradeStatus)""")
@cli_util.option('--drg-id', required=True, help=u"""The [[OCID]](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'UpgradeStatus'})
@cli_util.wrap_exceptions
def get_upgrade_status(ctx, from_json, drg_id):

    if isinstance(drg_id, six.string_types) and len(drg_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_upgrade_status(
        drg_id=drg_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vcn_group.command(name=cli_util.override('virtual_network.get_vcn.command_name', 'get'), help=u"""Gets the specified VCN's information. \n[Command Reference](getVcn)""")
@cli_util.option('--vcn-id', required=True, help=u"""The [OCID] of the VCN.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Vcn'})
@cli_util.wrap_exceptions
def get_vcn(ctx, from_json, vcn_id):

    if isinstance(vcn_id, six.string_types) and len(vcn_id.strip()) == 0:
        raise click.UsageError('Parameter --vcn-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_vcn(
        vcn_id=vcn_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vcn_dns_resolver_association_group.command(name=cli_util.override('virtual_network.get_vcn_dns_resolver_association.command_name', 'get'), help=u"""Get the associated DNS resolver information with a vcn \n[Command Reference](getVcnDnsResolverAssociation)""")
@cli_util.option('--vcn-id', required=True, help=u"""The [OCID] of the VCN.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VcnDnsResolverAssociation'})
@cli_util.wrap_exceptions
def get_vcn_dns_resolver_association(ctx, from_json, vcn_id):

    if isinstance(vcn_id, six.string_types) and len(vcn_id.strip()) == 0:
        raise click.UsageError('Parameter --vcn-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_vcn_dns_resolver_association(
        vcn_id=vcn_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vcn_topology_group.command(name=cli_util.override('virtual_network.get_vcn_topology.command_name', 'get'), help=u"""Gets a virtual network topology for a given VCN. \n[Command Reference](getVcnTopology)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--vcn-id', required=True, help=u"""The [OCID] of the VCN.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["ANY", "ACCESSIBLE"]), help=u"""Valid values are `ANY` and `ACCESSIBLE`. The default is `ANY`. Setting this to `ACCESSIBLE` returns only compartments for which a user has INSPECT permissions, either directly or indirectly (permissions can be on a resource in a subcompartment). A restricted set of fields is returned for compartments in which a user has indirect INSPECT permissions.

When set to `ANY` permissions are not checked.""")
@cli_util.option('--query-compartment-subtree', type=click.BOOL, help=u"""When set to true, the hierarchy of compartments is traversed and the specified compartment and its subcompartments are inspected depending on the the setting of `accessLevel`. Default is false.""")
@cli_util.option('--if-none-match', help=u"""For querying if there is a cached value on the server. The If-None-Match HTTP request header makes the request conditional. For GET and HEAD methods, the server will send back the requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones. For other methods, the request will be processed only if the eventually existing resource's ETag doesn't match any of the values listed.""")
@cli_util.option('--cache-control', help=u"""The Cache-Control HTTP header holds directives (instructions) for caching in both requests and responses.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VcnTopology'})
@cli_util.wrap_exceptions
def get_vcn_topology(ctx, from_json, compartment_id, vcn_id, access_level, query_compartment_subtree, if_none_match, cache_control):

    kwargs = {}
    if access_level is not None:
        kwargs['access_level'] = access_level
    if query_compartment_subtree is not None:
        kwargs['query_compartment_subtree'] = query_compartment_subtree
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if cache_control is not None:
        kwargs['cache_control'] = cache_control
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_vcn_topology(
        compartment_id=compartment_id,
        vcn_id=vcn_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@virtual_circuit_group.command(name=cli_util.override('virtual_network.get_virtual_circuit.command_name', 'get'), help=u"""Gets the specified virtual circuit's information. \n[Command Reference](getVirtualCircuit)""")
@cli_util.option('--virtual-circuit-id', required=True, help=u"""The [OCID] of the virtual circuit.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VirtualCircuit'})
@cli_util.wrap_exceptions
def get_virtual_circuit(ctx, from_json, virtual_circuit_id):

    if isinstance(virtual_circuit_id, six.string_types) and len(virtual_circuit_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-circuit-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_virtual_circuit(
        virtual_circuit_id=virtual_circuit_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vlan_group.command(name=cli_util.override('virtual_network.get_vlan.command_name', 'get'), help=u"""Gets the specified VLAN's information. \n[Command Reference](getVlan)""")
@cli_util.option('--vlan-id', required=True, help=u"""The [OCID] of the VLAN.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Vlan'})
@cli_util.wrap_exceptions
def get_vlan(ctx, from_json, vlan_id):

    if isinstance(vlan_id, six.string_types) and len(vlan_id.strip()) == 0:
        raise click.UsageError('Parameter --vlan-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_vlan(
        vlan_id=vlan_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vnic_group.command(name=cli_util.override('virtual_network.get_vnic.command_name', 'get'), help=u"""Gets the information for the specified virtual network interface card (VNIC). You can get the VNIC OCID from the [ListVnicAttachments] operation. \n[Command Reference](getVnic)""")
@cli_util.option('--vnic-id', required=True, help=u"""The [OCID] of the VNIC.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Vnic'})
@cli_util.wrap_exceptions
def get_vnic(ctx, from_json, vnic_id):

    if isinstance(vnic_id, six.string_types) and len(vnic_id.strip()) == 0:
        raise click.UsageError('Parameter --vnic-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.get_vnic(
        vnic_id=vnic_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@peer_region_for_remote_peering_group.command(name=cli_util.override('virtual_network.list_allowed_peer_regions_for_remote_peering.command_name', 'list-allowed-peer-regions-for-remote-peering'), help=u"""Lists the regions that support remote VCN peering (which is peering across regions). For more information, see [VCN Peering]. \n[Command Reference](listAllowedPeerRegionsForRemotePeering)""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[PeerRegionForRemotePeering]'})
@cli_util.wrap_exceptions
def list_allowed_peer_regions_for_remote_peering(ctx, from_json, all_pages, ):

    kwargs = {}
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.list_allowed_peer_regions_for_remote_peering(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@byoip_allocated_range_summary_group.command(name=cli_util.override('virtual_network.list_byoip_allocated_ranges.command_name', 'list-byoip-allocated-ranges'), help=u"""Lists the subranges of a BYOIP CIDR block currently allocated to an IP pool. Each `ByoipAllocatedRange` object also lists the IP pool where it is allocated. \n[Command Reference](listByoipAllocatedRanges)""")
@cli_util.option('--byoip-range-id', required=True, help=u"""The [OCID] of the `ByoipRange` resource containing the BYOIP CIDR block.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ByoipAllocatedRangeCollection'})
@cli_util.wrap_exceptions
def list_byoip_allocated_ranges(ctx, from_json, all_pages, page_size, byoip_range_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(byoip_range_id, six.string_types) and len(byoip_range_id.strip()) == 0:
        raise click.UsageError('Parameter --byoip-range-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_byoip_allocated_ranges,
            byoip_range_id=byoip_range_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_byoip_allocated_ranges,
            limit,
            page_size,
            byoip_range_id=byoip_range_id,
            **kwargs
        )
    else:
        result = client.list_byoip_allocated_ranges(
            byoip_range_id=byoip_range_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@byoip_range_group.command(name=cli_util.override('virtual_network.list_byoip_ranges.command_name', 'list'), help=u"""Lists the `ByoipRange` resources in the specified compartment. You can filter the list using query parameters. \n[Command Reference](listByoipRanges)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--lifecycle-state', help=u"""A filter to return only resources that match the given lifecycle state name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ByoipRangeCollection'})
@cli_util.wrap_exceptions
def list_byoip_ranges(ctx, from_json, all_pages, page_size, compartment_id, limit, page, display_name, lifecycle_state, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_byoip_ranges,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_byoip_ranges,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_byoip_ranges(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@cpe_device_shape_group.command(name=cli_util.override('virtual_network.list_cpe_device_shapes.command_name', 'list'), help=u"""Lists the CPE device types that the Networking service provides CPE configuration content for (example: Cisco ASA). The content helps a network engineer configure the actual CPE device represented by a [Cpe] object.

If you want to generate CPE configuration content for one of the returned CPE device types, ensure that the [Cpe] object's `cpeDeviceShapeId` attribute is set to the CPE device type's [OCID] (returned by this operation).

For information about generating CPE configuration content, see these operations:

  * [GetCpeDeviceConfigContent]   * [GetIpsecCpeDeviceConfigContent]   * [GetTunnelCpeDeviceConfigContent] \n[Command Reference](listCpeDeviceShapes)""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[CpeDeviceShapeSummary]'})
@cli_util.wrap_exceptions
def list_cpe_device_shapes(ctx, from_json, all_pages, page_size, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_cpe_device_shapes,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_cpe_device_shapes,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_cpe_device_shapes(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@cpe_group.command(name=cli_util.override('virtual_network.list_cpes.command_name', 'list'), help=u"""Lists the customer-premises equipment objects (CPEs) in the specified compartment. \n[Command Reference](listCpes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@cross_connect_group_group.command(name=cli_util.override('virtual_network.list_cross_connect_groups.command_name', 'list'), help=u"""Lists the cross-connect groups in the specified compartment. \n[Command Reference](listCrossConnectGroups)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@cross_connect_location_group.command(name=cli_util.override('virtual_network.list_cross_connect_locations.command_name', 'list'), help=u"""Lists the available FastConnect locations for cross-connect installation. You need this information so you can specify your desired location when you create a cross-connect. \n[Command Reference](listCrossConnectLocations)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@cross_connect_mapping_details_collection_group.command(name=cli_util.override('virtual_network.list_cross_connect_mappings.command_name', 'list-cross-connect-mappings'), help=u"""Lists the Cross Connect mapping Details for the specified virtual circuit. \n[Command Reference](listCrossConnectMappings)""")
@cli_util.option('--virtual-circuit-id', required=True, help=u"""The [OCID] of the virtual circuit.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'CrossConnectMappingDetailsCollection'})
@cli_util.wrap_exceptions
def list_cross_connect_mappings(ctx, from_json, all_pages, virtual_circuit_id):

    if isinstance(virtual_circuit_id, six.string_types) and len(virtual_circuit_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-circuit-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.list_cross_connect_mappings(
        virtual_circuit_id=virtual_circuit_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cross_connect_group.command(name=cli_util.override('virtual_network.list_cross_connects.command_name', 'list'), help=u"""Lists the cross-connects in the specified compartment. You can filter the list by specifying the [OCID] of a cross-connect group. \n[Command Reference](listCrossConnects)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--cross-connect-group-id', help=u"""The [OCID] of the cross-connect group.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@cross_connect_port_speed_shape_group.command(name=cli_util.override('virtual_network.list_crossconnect_port_speed_shapes.command_name', 'list-crossconnect-port-speed-shapes'), help=u"""Lists the available port speeds for cross-connects. You need this information so you can specify your desired port speed (that is, shape) when you create a cross-connect. \n[Command Reference](listCrossconnectPortSpeedShapes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@dhcp_options_group.command(name=cli_util.override('virtual_network.list_dhcp_options.command_name', 'list'), help=u"""Lists the sets of DHCP options in the specified VCN and specified compartment. If the VCN ID is not provided, then the list includes the sets of DHCP options from all VCNs in the specified compartment. The response includes the default set of options that automatically comes with each VCN, plus any other sets you've created. \n[Command Reference](listDhcpOptions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help=u"""A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_dhcp_options,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_dhcp_options,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_dhcp_options(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@drg_attachment_group.command(name=cli_util.override('virtual_network.list_drg_attachments.command_name', 'list'), help=u"""Lists the `DrgAttachment` resource for the specified compartment. You can filter the results by DRG, attached network, attachment type, DRG route table or VCN route table.

The LIST API lists DRG attachments by attachment type. It will default to list VCN attachments, but you may request to list ALL attachments of ALL types. \n[Command Reference](listDrgAttachments)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN.""")
@cli_util.option('--drg-id', help=u"""The [OCID] of the DRG.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--network-id', help=u"""The [OCID] of the resource (virtual circuit, VCN, IPSec tunnel, or remote peering connection) attached to the DRG.""")
@cli_util.option('--attachment-type', type=custom_types.CliCaseInsensitiveChoice(["VCN", "VIRTUAL_CIRCUIT", "REMOTE_PEERING_CONNECTION", "IPSEC_TUNNEL", "ALL"]), help=u"""The type for the network resource attached to the DRG.""")
@cli_util.option('--drg-route-table-id', help=u"""The [OCID] of the DRG route table assigned to the DRG attachment.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[DrgAttachment]'})
@cli_util.wrap_exceptions
def list_drg_attachments(ctx, from_json, all_pages, page_size, compartment_id, vcn_id, drg_id, limit, page, network_id, attachment_type, drg_route_table_id, display_name, sort_by, sort_order, lifecycle_state):

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
    if network_id is not None:
        kwargs['network_id'] = network_id
    if attachment_type is not None:
        kwargs['attachment_type'] = attachment_type
    if drg_route_table_id is not None:
        kwargs['drg_route_table_id'] = drg_route_table_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@drg_route_distribution_statement_group.command(name=cli_util.override('virtual_network.list_drg_route_distribution_statements.command_name', 'list'), help=u"""Lists the statements for the specified route distribution. \n[Command Reference](listDrgRouteDistributionStatements)""")
@cli_util.option('--drg-route-distribution-id', required=True, help=u"""The [OCID] of the route distribution.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED"]), help=u"""The field to sort by.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[DrgRouteDistributionStatement]'})
@cli_util.wrap_exceptions
def list_drg_route_distribution_statements(ctx, from_json, all_pages, page_size, drg_route_distribution_id, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(drg_route_distribution_id, six.string_types) and len(drg_route_distribution_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-route-distribution-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_drg_route_distribution_statements,
            drg_route_distribution_id=drg_route_distribution_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_drg_route_distribution_statements,
            limit,
            page_size,
            drg_route_distribution_id=drg_route_distribution_id,
            **kwargs
        )
    else:
        result = client.list_drg_route_distribution_statements(
            drg_route_distribution_id=drg_route_distribution_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@drg_route_distribution_group.command(name=cli_util.override('virtual_network.list_drg_route_distributions.command_name', 'list'), help=u"""Lists the route distributions in the specified DRG.

To retrieve the statements in a distribution, use the ListDrgRouteDistributionStatements operation. \n[Command Reference](listDrgRouteDistributions)""")
@cli_util.option('--drg-id', required=True, help=u"""The [OCID] of the DRG.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help=u"""A filter that only returns resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[DrgRouteDistribution]'})
@cli_util.wrap_exceptions
def list_drg_route_distributions(ctx, from_json, all_pages, page_size, drg_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):

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
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_drg_route_distributions,
            drg_id=drg_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_drg_route_distributions,
            limit,
            page_size,
            drg_id=drg_id,
            **kwargs
        )
    else:
        result = client.list_drg_route_distributions(
            drg_id=drg_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@drg_route_rule_group.command(name=cli_util.override('virtual_network.list_drg_route_rules.command_name', 'list'), help=u"""Lists the route rules in the specified DRG route table. \n[Command Reference](listDrgRouteRules)""")
@cli_util.option('--drg-route-table-id', required=True, help=u"""The [OCID] of the DRG route table.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--route-type', type=custom_types.CliCaseInsensitiveChoice(["STATIC", "DYNAMIC"]), help=u"""Static routes are specified through the DRG route table API. Dynamic routes are learned by the DRG from the DRG attachments through various routing protocols.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[DrgRouteRule]'})
@cli_util.wrap_exceptions
def list_drg_route_rules(ctx, from_json, all_pages, page_size, drg_route_table_id, limit, page, route_type):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(drg_route_table_id, six.string_types) and len(drg_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-route-table-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if route_type is not None:
        kwargs['route_type'] = route_type
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_drg_route_rules,
            drg_route_table_id=drg_route_table_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_drg_route_rules,
            limit,
            page_size,
            drg_route_table_id=drg_route_table_id,
            **kwargs
        )
    else:
        result = client.list_drg_route_rules(
            drg_route_table_id=drg_route_table_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@drg_route_table_group.command(name=cli_util.override('virtual_network.list_drg_route_tables.command_name', 'list'), help=u"""Lists the DRG route tables for the specified DRG.

Use the `ListDrgRouteRules` operation to retrieve the route rules in a table. \n[Command Reference](listDrgRouteTables)""")
@cli_util.option('--drg-id', required=True, help=u"""The [OCID] of the DRG.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--import-drg-route-distribution-id', help=u"""The [OCID] of the import route distribution.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help=u"""A filter that only returns matches for the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[DrgRouteTable]'})
@cli_util.wrap_exceptions
def list_drg_route_tables(ctx, from_json, all_pages, page_size, drg_id, limit, page, display_name, sort_by, sort_order, import_drg_route_distribution_id, lifecycle_state):

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
    if import_drg_route_distribution_id is not None:
        kwargs['import_drg_route_distribution_id'] = import_drg_route_distribution_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_drg_route_tables,
            drg_id=drg_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_drg_route_tables,
            limit,
            page_size,
            drg_id=drg_id,
            **kwargs
        )
    else:
        result = client.list_drg_route_tables(
            drg_id=drg_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@drg_group.command(name=cli_util.override('virtual_network.list_drgs.command_name', 'list'), help=u"""Lists the DRGs in the specified compartment. \n[Command Reference](listDrgs)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@fast_connect_provider_service_group.command(name=cli_util.override('virtual_network.list_fast_connect_provider_services.command_name', 'list'), help=u"""Lists the service offerings from supported providers. You need this information so you can specify your desired provider and service offering when you create a virtual circuit.

For the compartment ID, provide the [OCID] of your tenancy (the root compartment).

For more information, see [FastConnect Overview]. \n[Command Reference](listFastConnectProviderServices)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@fast_connect_provider_service_group.command(name=cli_util.override('virtual_network.list_fast_connect_provider_virtual_circuit_bandwidth_shapes.command_name', 'list-fast-connect-provider-virtual-circuit-bandwidth-shapes'), help=u"""Gets the list of available virtual circuit bandwidth levels for a provider. You need this information so you can specify your desired bandwidth level (shape) when you create a virtual circuit.

For more information about virtual circuits, see [FastConnect Overview]. \n[Command Reference](listFastConnectProviderVirtualCircuitBandwidthShapes)""")
@cli_util.option('--provider-service-id', required=True, help=u"""The [OCID] of the provider service.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@internet_gateway_group.command(name=cli_util.override('virtual_network.list_internet_gateways.command_name', 'list'), help=u"""Lists the internet gateways in the specified VCN and the specified compartment. If the VCN ID is not provided, then the list includes the internet gateways from all VCNs in the specified compartment. \n[Command Reference](listInternetGateways)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help=u"""A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_internet_gateways,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_internet_gateways,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_internet_gateways(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@ip_sec_connection_tunnel_group.command(name=cli_util.override('virtual_network.list_ip_sec_connection_tunnels.command_name', 'list'), help=u"""Lists the tunnel information for the specified IPSec connection. \n[Command Reference](listIPSecConnectionTunnels)""")
@cli_util.option('--ipsc-id', required=True, help=u"""The [OCID] of the IPSec connection.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[IPSecConnectionTunnel]'})
@cli_util.wrap_exceptions
def list_ip_sec_connection_tunnels(ctx, from_json, all_pages, page_size, ipsc_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_ip_sec_connection_tunnels,
            ipsc_id=ipsc_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_ip_sec_connection_tunnels,
            limit,
            page_size,
            ipsc_id=ipsc_id,
            **kwargs
        )
    else:
        result = client.list_ip_sec_connection_tunnels(
            ipsc_id=ipsc_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@ip_sec_connection_group.command(name=cli_util.override('virtual_network.list_ip_sec_connections.command_name', 'list'), help=u"""Lists the IPSec connections for the specified compartment. You can filter the results by DRG or CPE. \n[Command Reference](listIPSecConnections)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--drg-id', help=u"""The [OCID] of the DRG.""")
@cli_util.option('--cpe-id', help=u"""The [OCID] of the CPE.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@ipv6_group.command(name=cli_util.override('virtual_network.list_ipv6s.command_name', 'list'), help=u"""Lists the [IPv6] objects based on one of these filters:

  * Subnet OCID.   * VNIC OCID.   * Both IPv6 address and subnet OCID: This lets you get an `Ipv6` object based on its private   IPv6 address (for example, 2001:0db8:0123:1111:abcd:ef01:2345:6789) and not its OCID. For comparison,   [GetIpv6] requires the OCID. \n[Command Reference](listIpv6s)""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--ip-address', help=u"""An IP address. This could be either IPv4 or IPv6, depending on the resource. Example: `10.0.3.3`""")
@cli_util.option('--subnet-id', help=u"""The [OCID] of the subnet.""")
@cli_util.option('--vnic-id', help=u"""The OCID of the VNIC.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Ipv6]'})
@cli_util.wrap_exceptions
def list_ipv6s(ctx, from_json, all_pages, page_size, limit, page, ip_address, subnet_id, vnic_id):

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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_ipv6s,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_ipv6s,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_ipv6s(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@local_peering_gateway_group.command(name=cli_util.override('virtual_network.list_local_peering_gateways.command_name', 'list'), help=u"""Lists the local peering gateways (LPGs) for the specified VCN and specified compartment. If the VCN ID is not provided, then the list includes the LPGs from all VCNs in the specified compartment. \n[Command Reference](listLocalPeeringGateways)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[LocalPeeringGateway]'})
@cli_util.wrap_exceptions
def list_local_peering_gateways(ctx, from_json, all_pages, page_size, compartment_id, limit, page, vcn_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if vcn_id is not None:
        kwargs['vcn_id'] = vcn_id
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_local_peering_gateways,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_local_peering_gateways,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_local_peering_gateways(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@nat_gateway_group.command(name=cli_util.override('virtual_network.list_nat_gateways.command_name', 'list'), help=u"""Lists the NAT gateways in the specified compartment. You may optionally specify a VCN OCID to filter the results by VCN. \n[Command Reference](listNatGateways)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@security_rule_group.command(name=cli_util.override('virtual_network.list_network_security_group_security_rules.command_name', 'list-network-security-group'), help=u"""Lists the security rules in the specified network security group. \n[Command Reference](listNetworkSecurityGroupSecurityRules)""")
@cli_util.option('--network-security-group-id', required=True, help=u"""The [OCID] of the network security group.""")
@cli_util.option('--direction', type=custom_types.CliCaseInsensitiveChoice(["EGRESS", "INGRESS"]), help=u"""Direction of the security rule. Set to `EGRESS` for rules that allow outbound IP packets, or `INGRESS` for rules that allow inbound IP packets.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED"]), help=u"""The field to sort by.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[SecurityRule]'})
@cli_util.wrap_exceptions
def list_network_security_group_security_rules(ctx, from_json, all_pages, page_size, network_security_group_id, direction, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(network_security_group_id, six.string_types) and len(network_security_group_id.strip()) == 0:
        raise click.UsageError('Parameter --network-security-group-id cannot be whitespace or empty string')

    kwargs = {}
    if direction is not None:
        kwargs['direction'] = direction
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_network_security_group_security_rules,
            network_security_group_id=network_security_group_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_network_security_group_security_rules,
            limit,
            page_size,
            network_security_group_id=network_security_group_id,
            **kwargs
        )
    else:
        result = client.list_network_security_group_security_rules(
            network_security_group_id=network_security_group_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@network_security_group_vnic_group.command(name=cli_util.override('virtual_network.list_network_security_group_vnics.command_name', 'list'), help=u"""Lists the VNICs in the specified network security group. \n[Command Reference](listNetworkSecurityGroupVnics)""")
@cli_util.option('--network-security-group-id', required=True, help=u"""The [OCID] of the network security group.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMEASSOCIATED"]), help=u"""The field to sort by.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[NetworkSecurityGroupVnic]'})
@cli_util.wrap_exceptions
def list_network_security_group_vnics(ctx, from_json, all_pages, page_size, network_security_group_id, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(network_security_group_id, six.string_types) and len(network_security_group_id.strip()) == 0:
        raise click.UsageError('Parameter --network-security-group-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_network_security_group_vnics,
            network_security_group_id=network_security_group_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_network_security_group_vnics,
            limit,
            page_size,
            network_security_group_id=network_security_group_id,
            **kwargs
        )
    else:
        result = client.list_network_security_group_vnics(
            network_security_group_id=network_security_group_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@network_security_group_group.command(name=cli_util.override('virtual_network.list_network_security_groups.command_name', 'list'), help=u"""Lists the network security groups in the specified compartment. \n[Command Reference](listNetworkSecurityGroups)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[NetworkSecurityGroup]'})
@cli_util.wrap_exceptions
def list_network_security_groups(ctx, from_json, all_pages, page_size, compartment_id, vcn_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):

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
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_network_security_groups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_network_security_groups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_network_security_groups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@private_ip_group.command(name=cli_util.override('virtual_network.list_private_ips.command_name', 'list'), help=u"""Lists the [PrivateIp] objects based on one of these filters:

  - Subnet OCID.   - VNIC OCID.   - Both private IP address and subnet OCID: This lets   you get a `privateIP` object based on its private IP   address (for example, 10.0.3.3) and not its OCID. For comparison,   [GetPrivateIp]   requires the OCID.

If you're listing all the private IPs associated with a given subnet or VNIC, the response includes both primary and secondary private IPs.

If you are an Oracle Cloud VMware Solution customer and have VLANs in your VCN, you can filter the list by VLAN OCID. See [Vlan]. \n[Command Reference](listPrivateIps)""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--ip-address', help=u"""An IP address. This could be either IPv4 or IPv6, depending on the resource. Example: `10.0.3.3`""")
@cli_util.option('--subnet-id', help=u"""The [OCID] of the subnet.""")
@cli_util.option('--vnic-id', help=u"""The OCID of the VNIC.""")
@cli_util.option('--vlan-id', help=u"""The [OCID] of the VLAN.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[PrivateIp]'})
@cli_util.wrap_exceptions
def list_private_ips(ctx, from_json, all_pages, page_size, limit, page, ip_address, subnet_id, vnic_id, vlan_id):

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
    if vlan_id is not None:
        kwargs['vlan_id'] = vlan_id
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@public_ip_pool_group.command(name=cli_util.override('virtual_network.list_public_ip_pools.command_name', 'list'), help=u"""Lists the public IP pools in the specified compartment. You can filter the list using query parameters. \n[Command Reference](listPublicIpPools)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--byoip-range-id', help=u"""A filter to return only resources that match the given BYOIP CIDR block.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PublicIpPoolCollection'})
@cli_util.wrap_exceptions
def list_public_ip_pools(ctx, from_json, all_pages, page_size, compartment_id, limit, page, display_name, byoip_range_id, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if byoip_range_id is not None:
        kwargs['byoip_range_id'] = byoip_range_id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_public_ip_pools,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_public_ip_pools,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_public_ip_pools(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@public_ip_group.command(name=cli_util.override('virtual_network.list_public_ips.command_name', 'list'), help=u"""Lists the [PublicIp] objects in the specified compartment. You can filter the list by using query parameters.

To list your reserved public IPs:   * Set `scope` = `REGION`  (required)   * Leave the `availabilityDomain` parameter empty   * Set `lifetime` = `RESERVED`

To list the ephemeral public IPs assigned to a regional entity such as a NAT gateway:   * Set `scope` = `REGION`  (required)   * Leave the `availabilityDomain` parameter empty   * Set `lifetime` = `EPHEMERAL`

To list the ephemeral public IPs assigned to private IPs:   * Set `scope` = `AVAILABILITY_DOMAIN` (required)   * Set the `availabilityDomain` parameter to the desired availability domain (required)   * Set `lifetime` = `EPHEMERAL`

**Note:** An ephemeral public IP assigned to a private IP is always in the same availability domain and compartment as the private IP. \n[Command Reference](listPublicIps)""")
@cli_util.option('--scope', required=True, type=custom_types.CliCaseInsensitiveChoice(["REGION", "AVAILABILITY_DOMAIN"]), help=u"""Whether the public IP is regional or specific to a particular availability domain.

* `REGION`: The public IP exists within a region and is assigned to a regional entity (such as a [NatGateway]), or can be assigned to a private IP in any availability domain in the region. Reserved public IPs have `scope` = `REGION`, as do ephemeral public IPs assigned to a regional entity.

* `AVAILABILITY_DOMAIN`: The public IP exists within the availability domain of the entity it's assigned to, which is specified by the `availabilityDomain` property of the public IP object. Ephemeral public IPs that are assigned to private IPs have `scope` = `AVAILABILITY_DOMAIN`.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--availability-domain', help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--lifetime', type=custom_types.CliCaseInsensitiveChoice(["EPHEMERAL", "RESERVED"]), help=u"""A filter to return only public IPs that match given lifetime.""")
@cli_util.option('--public-ip-pool-id', help=u"""A filter to return only resources that belong to the given public IP pool.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[PublicIp]'})
@cli_util.wrap_exceptions
def list_public_ips(ctx, from_json, all_pages, page_size, scope, compartment_id, limit, page, availability_domain, lifetime, public_ip_pool_id):

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
    if public_ip_pool_id is not None:
        kwargs['public_ip_pool_id'] = public_ip_pool_id
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@remote_peering_connection_group.command(name=cli_util.override('virtual_network.list_remote_peering_connections.command_name', 'list'), help=u"""Lists the remote peering connections (RPCs) for the specified DRG and compartment (the RPC's compartment). \n[Command Reference](listRemotePeeringConnections)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--drg-id', help=u"""The [OCID] of the DRG.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@route_table_group.command(name=cli_util.override('virtual_network.list_route_tables.command_name', 'list'), help=u"""Lists the route tables in the specified VCN and specified compartment. If the VCN ID is not provided, then the list includes the route tables from all VCNs in the specified compartment. The response includes the default route table that automatically comes with each VCN in the specified compartment, plus any route tables you've created. \n[Command Reference](listRouteTables)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help=u"""A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[RouteTable]'})
@cli_util.wrap_exceptions
def list_route_tables(ctx, from_json, all_pages, page_size, compartment_id, limit, page, vcn_id, display_name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if vcn_id is not None:
        kwargs['vcn_id'] = vcn_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_route_tables,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_route_tables,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_route_tables(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@security_list_group.command(name=cli_util.override('virtual_network.list_security_lists.command_name', 'list'), help=u"""Lists the security lists in the specified VCN and compartment. If the VCN ID is not provided, then the list includes the security lists from all VCNs in the specified compartment. \n[Command Reference](listSecurityLists)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help=u"""A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[SecurityList]'})
@cli_util.wrap_exceptions
def list_security_lists(ctx, from_json, all_pages, page_size, compartment_id, limit, page, vcn_id, display_name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if vcn_id is not None:
        kwargs['vcn_id'] = vcn_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_security_lists,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_security_lists,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_security_lists(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@service_gateway_group.command(name=cli_util.override('virtual_network.list_service_gateways.command_name', 'list'), help=u"""Lists the service gateways in the specified compartment. You may optionally specify a VCN OCID to filter the results by VCN. \n[Command Reference](listServiceGateways)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), help=u"""A filter to return only resources that match the given lifecycle state. The state value is case-insensitive.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@service_group.command(name=cli_util.override('virtual_network.list_services.command_name', 'list'), help=u"""Lists the available [Service] objects that you can enable for a service gateway in this region. \n[Command Reference](listServices)""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@subnet_group.command(name=cli_util.override('virtual_network.list_subnets.command_name', 'list'), help=u"""Lists the subnets in the specified VCN and the specified compartment. If the VCN ID is not provided, then the list includes the subnets from all VCNs in the specified compartment. \n[Command Reference](listSubnets)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"]), help=u"""A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Subnet]'})
@cli_util.wrap_exceptions
def list_subnets(ctx, from_json, all_pages, page_size, compartment_id, limit, page, vcn_id, display_name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if vcn_id is not None:
        kwargs['vcn_id'] = vcn_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_subnets,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_subnets,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_subnets(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@vcn_group.command(name=cli_util.override('virtual_network.list_vcns.command_name', 'list'), help=u"""Lists the virtual cloud networks (VCNs) in the specified compartment. \n[Command Reference](listVcns)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"]), help=u"""A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@virtual_circuit_bandwidth_shape_group.command(name=cli_util.override('virtual_network.list_virtual_circuit_bandwidth_shapes.command_name', 'list'), help=u"""The deprecated operation lists available bandwidth levels for virtual circuits. For the compartment ID, provide the OCID of your tenancy (the root compartment). \n[Command Reference](listVirtualCircuitBandwidthShapes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@virtual_circuit_public_prefix_group.command(name=cli_util.override('virtual_network.list_virtual_circuit_public_prefixes.command_name', 'list'), help=u"""Lists the public IP prefixes and their details for the specified public virtual circuit. \n[Command Reference](listVirtualCircuitPublicPrefixes)""")
@cli_util.option('--virtual-circuit-id', required=True, help=u"""The [OCID] of the virtual circuit.""")
@cli_util.option('--verification-state', type=custom_types.CliCaseInsensitiveChoice(["IN_PROGRESS", "COMPLETED", "FAILED"]), help=u"""A filter to only return resources that match the given verification state.

The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VirtualCircuitPublicPrefix]'})
@cli_util.wrap_exceptions
def list_virtual_circuit_public_prefixes(ctx, from_json, all_pages, virtual_circuit_id, verification_state):

    if isinstance(virtual_circuit_id, six.string_types) and len(virtual_circuit_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-circuit-id cannot be whitespace or empty string')

    kwargs = {}
    if verification_state is not None:
        kwargs['verification_state'] = verification_state
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.list_virtual_circuit_public_prefixes(
        virtual_circuit_id=virtual_circuit_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@virtual_circuit_group.command(name=cli_util.override('virtual_network.list_virtual_circuits.command_name', 'list'), help=u"""Lists the virtual circuits in the specified compartment. \n[Command Reference](listVirtualCircuits)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_PROVIDER", "VERIFYING", "PROVISIONING", "PROVISIONED", "FAILED", "INACTIVE", "TERMINATING", "TERMINATED"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
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
    client = cli_util.build_client('core', 'virtual_network', ctx)
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


@vlan_group.command(name=cli_util.override('virtual_network.list_vlans.command_name', 'list'), help=u"""Lists the VLANs in the specified VCN and the specified compartment. \n[Command Reference](listVlans)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--vcn-id', required=True, help=u"""The [OCID] of the VCN.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"]), help=u"""A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Vlan]'})
@cli_util.wrap_exceptions
def list_vlans(ctx, from_json, all_pages, page_size, compartment_id, vcn_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):

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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_vlans,
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_vlans,
            limit,
            page_size,
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    else:
        result = client.list_vlans(
            compartment_id=compartment_id,
            vcn_id=vcn_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@vcn_group.command(name=cli_util.override('virtual_network.modify_vcn_cidr.command_name', 'modify-vcn-cidr'), help=u"""Updates the specified CIDR block of a VCN. The new CIDR IP range must meet the following criteria:

- Must be valid. - Must not overlap with another CIDR block in the VCN, a CIDR block of a peered VCN, or the on-premises network CIDR block. - Must not exceed the limit of CIDR blocks allowed per VCN. - Must include IP addresses from the original CIDR block that are used in the VCN's existing route rules. - No IP address in an existing subnet should be outside of the new CIDR block range.

**Note:** Modifying a CIDR block places your VCN in an updating state until the changes are complete. You cannot create or update the VCN's subnets, VLANs, LPGs, or route tables during this operation. The time to completion can vary depending on the size of your network. Updating a small network could take about a minute, and updating a large network could take up to an hour. You can use the `GetWorkRequest` operation to check the status of the update. \n[Command Reference](modifyVcnCidr)""")
@cli_util.option('--vcn-id', required=True, help=u"""The [OCID] of the VCN.""")
@cli_util.option('--original-cidr-block', required=True, help=u"""The CIDR IP address to update.""")
@cli_util.option('--new-cidr-block', required=True, help=u"""The new CIDR IP address.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def modify_vcn_cidr(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vcn_id, original_cidr_block, new_cidr_block, if_match):

    if isinstance(vcn_id, six.string_types) and len(vcn_id.strip()) == 0:
        raise click.UsageError('Parameter --vcn-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['originalCidrBlock'] = original_cidr_block
    _details['newCidrBlock'] = new_cidr_block

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.modify_vcn_cidr(
        vcn_id=vcn_id,
        modify_vcn_cidr_details=_details,
        **kwargs
    )
    work_request_client = cli_util.build_client('work_requests', 'work_request', ctx)
    if wait_for_state:

        if hasattr(work_request_client, 'get_work_request') and callable(getattr(work_request_client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(work_request_client, work_request_client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
                if hasattr(result, "data") and hasattr(result.data, "resources") and len(result.data.resources) == 1:
                    entity_type = result.data.resources[0].entity_type
                    identifier = result.data.resources[0].identifier
                    get_operation = 'get_' + entity_type
                    if hasattr(client, get_operation) and callable(getattr(client, get_operation)):
                        result = getattr(client, get_operation)(identifier)

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


@drg_route_distribution_statement_group.command(name=cli_util.override('virtual_network.remove_drg_route_distribution_statements.command_name', 'remove'), help=u"""Removes one or more route distribution statements from the specified route distribution's map. \n[Command Reference](removeDrgRouteDistributionStatements)""")
@cli_util.option('--drg-route-distribution-id', required=True, help=u"""The [OCID] of the route distribution.""")
@cli_util.option('--statement-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The Oracle-assigned ID of each route distribution to remove.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'statement-ids': {'module': 'core', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'statement-ids': {'module': 'core', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def remove_drg_route_distribution_statements(ctx, from_json, drg_route_distribution_id, statement_ids):

    if isinstance(drg_route_distribution_id, six.string_types) and len(drg_route_distribution_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-route-distribution-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}

    if statement_ids is not None:
        _details['statementIds'] = cli_util.parse_json_parameter("statement_ids", statement_ids)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.remove_drg_route_distribution_statements(
        drg_route_distribution_id=drg_route_distribution_id,
        remove_drg_route_distribution_statements_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@drg_route_rule_group.command(name=cli_util.override('virtual_network.remove_drg_route_rules.command_name', 'remove'), help=u"""Removes one or more route rules from the specified DRG route table. \n[Command Reference](removeDrgRouteRules)""")
@cli_util.option('--drg-route-table-id', required=True, help=u"""The [OCID] of the DRG route table.""")
@cli_util.option('--route-rule-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The Oracle-assigned ID of each DRG route rule to be deleted.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'route-rule-ids': {'module': 'core', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'route-rule-ids': {'module': 'core', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def remove_drg_route_rules(ctx, from_json, drg_route_table_id, route_rule_ids):

    if isinstance(drg_route_table_id, six.string_types) and len(drg_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-route-table-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}

    if route_rule_ids is not None:
        _details['routeRuleIds'] = cli_util.parse_json_parameter("route_rule_ids", route_rule_ids)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.remove_drg_route_rules(
        drg_route_table_id=drg_route_table_id,
        remove_drg_route_rules_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@drg_attachment_group.command(name=cli_util.override('virtual_network.remove_export_drg_route_distribution.command_name', 'remove'), help=u"""Removes the export route distribution from the DRG attachment so no routes are advertised to it. \n[Command Reference](removeExportDrgRouteDistribution)""")
@cli_util.option('--drg-attachment-id', required=True, help=u"""The [OCID] of the DRG attachment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'DrgAttachment'})
@cli_util.wrap_exceptions
def remove_export_drg_route_distribution(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_attachment_id, if_match):

    if isinstance(drg_attachment_id, six.string_types) and len(drg_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.remove_export_drg_route_distribution(
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
                result = oci.wait_until(client, client.get_drg_attachment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@drg_route_table_group.command(name=cli_util.override('virtual_network.remove_import_drg_route_distribution.command_name', 'remove'), help=u"""Removes the import route distribution from the DRG route table so no routes are imported into it. \n[Command Reference](removeImportDrgRouteDistribution)""")
@cli_util.option('--drg-route-table-id', required=True, help=u"""The [OCID] of the DRG route table.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'DrgRouteTable'})
@cli_util.wrap_exceptions
def remove_import_drg_route_distribution(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_route_table_id, if_match):

    if isinstance(drg_route_table_id, six.string_types) and len(drg_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-route-table-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.remove_import_drg_route_distribution(
        drg_route_table_id=drg_route_table_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_drg_route_table') and callable(getattr(client, 'get_drg_route_table')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_drg_route_table(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@security_rule_group.command(name=cli_util.override('virtual_network.remove_network_security_group_security_rules.command_name', 'remove'), help=u"""Removes one or more security rules from the specified network security group. \n[Command Reference](removeNetworkSecurityGroupSecurityRules)""")
@cli_util.option('--network-security-group-id', required=True, help=u"""The [OCID] of the network security group.""")
@cli_util.option('--security-rule-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The Oracle-assigned ID of each [SecurityRule] to be deleted.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'security-rule-ids': {'module': 'core', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'security-rule-ids': {'module': 'core', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def remove_network_security_group_security_rules(ctx, from_json, network_security_group_id, security_rule_ids):

    if isinstance(network_security_group_id, six.string_types) and len(network_security_group_id.strip()) == 0:
        raise click.UsageError('Parameter --network-security-group-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}

    if security_rule_ids is not None:
        _details['securityRuleIds'] = cli_util.parse_json_parameter("security_rule_ids", security_rule_ids)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.remove_network_security_group_security_rules(
        network_security_group_id=network_security_group_id,
        remove_network_security_group_security_rules_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_pool_group.command(name=cli_util.override('virtual_network.remove_public_ip_pool_capacity.command_name', 'remove'), help=u"""Removes a CIDR block from the referenced public IP pool. \n[Command Reference](removePublicIpPoolCapacity)""")
@cli_util.option('--public-ip-pool-id', required=True, help=u"""The [OCID] of the public IP pool.""")
@cli_util.option('--cidr-block', required=True, help=u"""The CIDR block to remove from the  public IP pool. Example: `10.0.1.0/24`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["INACTIVE", "UPDATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'PublicIpPool'})
@cli_util.wrap_exceptions
def remove_public_ip_pool_capacity(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, public_ip_pool_id, cidr_block):

    if isinstance(public_ip_pool_id, six.string_types) and len(public_ip_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --public-ip-pool-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['cidrBlock'] = cidr_block

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.remove_public_ip_pool_capacity(
        public_ip_pool_id=public_ip_pool_id,
        remove_public_ip_pool_capacity_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_public_ip_pool') and callable(getattr(client, 'get_public_ip_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_public_ip_pool(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@vcn_group.command(name=cli_util.override('virtual_network.remove_vcn_cidr.command_name', 'remove'), help=u"""Removes a specified CIDR block from a VCN.

**Notes:** - You cannot remove a CIDR block if an IP address in its range is in use. - Removing a CIDR block places your VCN in an updating state until the changes are complete. You cannot create or update the VCN's subnets, VLANs, LPGs, or route tables during this operation. The time to completion can take a few minutes. You can use the `GetWorkRequest` operation to check the status of the update. \n[Command Reference](removeVcnCidr)""")
@cli_util.option('--vcn-id', required=True, help=u"""The [OCID] of the VCN.""")
@cli_util.option('--cidr-block', required=True, help=u"""The CIDR block to remove.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def remove_vcn_cidr(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vcn_id, cidr_block, if_match):

    if isinstance(vcn_id, six.string_types) and len(vcn_id.strip()) == 0:
        raise click.UsageError('Parameter --vcn-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['cidrBlock'] = cidr_block

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.remove_vcn_cidr(
        vcn_id=vcn_id,
        remove_vcn_cidr_details=_details,
        **kwargs
    )
    work_request_client = cli_util.build_client('work_requests', 'work_request', ctx)
    if wait_for_state:

        if hasattr(work_request_client, 'get_work_request') and callable(getattr(work_request_client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(work_request_client, work_request_client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
                if hasattr(result, "data") and hasattr(result.data, "resources") and len(result.data.resources) == 1:
                    entity_type = result.data.resources[0].entity_type
                    identifier = result.data.resources[0].identifier
                    get_operation = 'get_' + entity_type
                    if hasattr(client, get_operation) and callable(getattr(client, get_operation)):
                        result = getattr(client, get_operation)(identifier)

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


@byoip_range_group.command(name=cli_util.override('virtual_network.update_byoip_range.command_name', 'update'), help=u"""Updates the tags or display name associated to the specified BYOIP CIDR block. \n[Command Reference](updateByoipRange)""")
@cli_util.option('--byoip-range-id', required=True, help=u"""The [OCID] of the `ByoipRange` resource containing the BYOIP CIDR block.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["INACTIVE", "UPDATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'ByoipRange'})
@cli_util.wrap_exceptions
def update_byoip_range(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, byoip_range_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(byoip_range_id, six.string_types) and len(byoip_range_id.strip()) == 0:
        raise click.UsageError('Parameter --byoip-range-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_byoip_range(
        byoip_range_id=byoip_range_id,
        update_byoip_range_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_byoip_range') and callable(getattr(client, 'get_byoip_range')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_byoip_range(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cpe_group.command(name=cli_util.override('virtual_network.update_cpe.command_name', 'update'), help=u"""Updates the specified CPE's display name or tags. Avoid entering confidential information. \n[Command Reference](updateCpe)""")
@cli_util.option('--cpe-id', required=True, help=u"""The [OCID] of the CPE.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--cpe-device-shape-id', help=u"""The [OCID] of the CPE device type. You can provide a value if you want to generate CPE device configuration content for IPSec connections that use this CPE. For a list of possible values, see [ListCpeDeviceShapes].

For more information about generating CPE device configuration content, see:

  * [GetCpeDeviceConfigContent]   * [GetIpsecCpeDeviceConfigContent]   * [GetTunnelCpeDeviceConfigContent]   * [GetTunnelCpeDeviceConfig]""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Cpe'})
@cli_util.wrap_exceptions
def update_cpe(ctx, from_json, force, cpe_id, defined_tags, display_name, freeform_tags, cpe_device_shape_id, if_match):

    if isinstance(cpe_id, six.string_types) and len(cpe_id.strip()) == 0:
        raise click.UsageError('Parameter --cpe-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if cpe_device_shape_id is not None:
        _details['cpeDeviceShapeId'] = cpe_device_shape_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_cpe(
        cpe_id=cpe_id,
        update_cpe_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cross_connect_group.command(name=cli_util.override('virtual_network.update_cross_connect.command_name', 'update'), help=u"""Updates the specified cross-connect. \n[Command Reference](updateCrossConnect)""")
@cli_util.option('--cross-connect-id', required=True, help=u"""The [OCID] of the cross-connect.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-active', type=click.BOOL, help=u"""Set to true to activate the cross-connect. You activate it after the physical cabling is complete, and you've confirmed the cross-connect's light levels are good and your side of the interface is up. Activation indicates to Oracle that the physical connection is ready.

Example: `true`""")
@cli_util.option('--customer-reference-name', help=u"""A reference name or identifier for the physical fiber connection that this cross-connect uses.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'CrossConnect'})
@cli_util.wrap_exceptions
def update_cross_connect(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, cross_connect_id, defined_tags, display_name, freeform_tags, is_active, customer_reference_name, if_match):

    if isinstance(cross_connect_id, six.string_types) and len(cross_connect_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if is_active is not None:
        _details['isActive'] = is_active

    if customer_reference_name is not None:
        _details['customerReferenceName'] = customer_reference_name

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_cross_connect(
        cross_connect_id=cross_connect_id,
        update_cross_connect_details=_details,
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


@cross_connect_group_group.command(name=cli_util.override('virtual_network.update_cross_connect_group.command_name', 'update'), help=u"""Updates the specified cross-connect group's display name. Avoid entering confidential information. \n[Command Reference](updateCrossConnectGroup)""")
@cli_util.option('--cross-connect-group-id', required=True, help=u"""The [OCID] of the cross-connect group.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--customer-reference-name', help=u"""A reference name or identifier for the physical fiber connection that this cross-connect group uses.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'CrossConnectGroup'})
@cli_util.wrap_exceptions
def update_cross_connect_group(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, cross_connect_group_id, defined_tags, display_name, customer_reference_name, freeform_tags, if_match):

    if isinstance(cross_connect_group_id, six.string_types) and len(cross_connect_group_id.strip()) == 0:
        raise click.UsageError('Parameter --cross-connect-group-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if customer_reference_name is not None:
        _details['customerReferenceName'] = customer_reference_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_cross_connect_group(
        cross_connect_group_id=cross_connect_group_id,
        update_cross_connect_group_details=_details,
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


@dhcp_options_group.command(name=cli_util.override('virtual_network.update_dhcp_options.command_name', 'update'), help=u"""Updates the specified set of DHCP options. You can update the display name or the options themselves. Avoid entering confidential information.

Note that the `options` object you provide replaces the entire existing set of options. \n[Command Reference](updateDhcpOptions)""")
@cli_util.option('--dhcp-id', required=True, help=u"""The [OCID] for the set of DHCP options.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type DhcpOption.  For documentation on DhcpOption please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/DhcpOption.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if options is not None:
        _details['options'] = cli_util.parse_json_parameter("options", options)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_dhcp_options(
        dhcp_id=dhcp_id,
        update_dhcp_details=_details,
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


@drg_group.command(name=cli_util.override('virtual_network.update_drg.command_name', 'update'), help=u"""Updates the specified DRG's display name or tags. Avoid entering confidential information. \n[Command Reference](updateDrg)""")
@cli_util.option('--drg-id', required=True, help=u"""The [[OCID]](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--default-drg-route-tables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'default-drg-route-tables': {'module': 'core', 'class': 'DefaultDrgRouteTables'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'default-drg-route-tables': {'module': 'core', 'class': 'DefaultDrgRouteTables'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Drg'})
@cli_util.wrap_exceptions
def update_drg(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_id, defined_tags, default_drg_route_tables, display_name, freeform_tags, if_match):

    if isinstance(drg_id, six.string_types) and len(drg_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or default_drg_route_tables or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and default-drg-route-tables and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if default_drg_route_tables is not None:
        _details['defaultDrgRouteTables'] = cli_util.parse_json_parameter("default_drg_route_tables", default_drg_route_tables)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_drg(
        drg_id=drg_id,
        update_drg_details=_details,
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


@drg_attachment_group.command(name=cli_util.override('virtual_network.update_drg_attachment.command_name', 'update'), help=u"""Updates the display name and routing information for the specified `DrgAttachment`. Avoid entering confidential information. \n[Command Reference](updateDrgAttachment)""")
@cli_util.option('--drg-attachment-id', required=True, help=u"""The [OCID] of the DRG attachment.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--drg-route-table-id', help=u"""The [OCID] of the DRG route table that is assigned to this attachment.

The DRG route table manages traffic inside the DRG.

You can't remove a DRG route table from a DRG attachment, but you can reassign which DRG route table it uses.""")
@cli_util.option('--network-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--export-drg-route-distribution-id', help=u"""The [OCID] of the export route distribution used to specify how routes in the assigned DRG route table are advertised out through the attachment. If this value is null, no routes are advertised through this attachment.""")
@cli_util.option('--route-table-id', help=u"""This is the [OCID] of the route table that is used to route the traffic as it enters a VCN through this attachment.

For information about why you would associate a route table with a DRG attachment, see:

  * [Transit Routing: Access to Multiple VCNs in Same Region]   * [Transit Routing: Private Access to Oracle Services]""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'network-details': {'module': 'core', 'class': 'DrgAttachmentNetworkUpdateDetails'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-details': {'module': 'core', 'class': 'DrgAttachmentNetworkUpdateDetails'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'DrgAttachment'})
@cli_util.wrap_exceptions
def update_drg_attachment(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_attachment_id, display_name, drg_route_table_id, network_details, defined_tags, freeform_tags, export_drg_route_distribution_id, route_table_id, if_match):

    if isinstance(drg_attachment_id, six.string_types) and len(drg_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-attachment-id cannot be whitespace or empty string')
    if not force:
        if network_details or defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to network-details and defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if drg_route_table_id is not None:
        _details['drgRouteTableId'] = drg_route_table_id

    if network_details is not None:
        _details['networkDetails'] = cli_util.parse_json_parameter("network_details", network_details)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if export_drg_route_distribution_id is not None:
        _details['exportDrgRouteDistributionId'] = export_drg_route_distribution_id

    if route_table_id is not None:
        _details['routeTableId'] = route_table_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_drg_attachment(
        drg_attachment_id=drg_attachment_id,
        update_drg_attachment_details=_details,
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


@drg_attachment_group.command(name=cli_util.override('virtual_network.update_drg_attachment_vcn_drg_attachment_network_update_details.command_name', 'update-drg-attachment-vcn-drg-attachment-network-update-details'), help=u"""Updates the display name and routing information for the specified `DrgAttachment`. Avoid entering confidential information. \n[Command Reference](updateDrgAttachment)""")
@cli_util.option('--drg-attachment-id', required=True, help=u"""The [OCID] of the DRG attachment.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--drg-route-table-id', help=u"""The [OCID] of the DRG route table that is assigned to this attachment.

The DRG route table manages traffic inside the DRG.

You can't remove a DRG route table from a DRG attachment, but you can reassign which DRG route table it uses.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--export-drg-route-distribution-id', help=u"""The [OCID] of the export route distribution used to specify how routes in the assigned DRG route table are advertised out through the attachment. If this value is null, no routes are advertised through this attachment.""")
@cli_util.option('--route-table-id', help=u"""This is the [OCID] of the route table that is used to route the traffic as it enters a VCN through this attachment.

For information about why you would associate a route table with a DRG attachment, see:

  * [Transit Routing: Access to Multiple VCNs in Same Region]   * [Transit Routing: Private Access to Oracle Services]""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--network-details-route-table-id', help=u"""This is the [OCID] of the route table that is used to route the traffic as it enters a VCN through this attachment.

For information about why you would associate a route table with a DRG attachment, see:

  * [Transit Routing: Access to Multiple VCNs in Same Region]   * [Transit Routing: Private Access to Oracle Services]""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'DrgAttachment'})
@cli_util.wrap_exceptions
def update_drg_attachment_vcn_drg_attachment_network_update_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_attachment_id, display_name, drg_route_table_id, defined_tags, freeform_tags, export_drg_route_distribution_id, route_table_id, if_match, network_details_route_table_id):

    if isinstance(drg_attachment_id, six.string_types) and len(drg_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-attachment-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}
    _details['networkDetails'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if drg_route_table_id is not None:
        _details['drgRouteTableId'] = drg_route_table_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if export_drg_route_distribution_id is not None:
        _details['exportDrgRouteDistributionId'] = export_drg_route_distribution_id

    if route_table_id is not None:
        _details['routeTableId'] = route_table_id

    if network_details_route_table_id is not None:
        _details['networkDetails']['routeTableId'] = network_details_route_table_id

    _details['networkDetails']['type'] = 'VCN'

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_drg_attachment(
        drg_attachment_id=drg_attachment_id,
        update_drg_attachment_details=_details,
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


@drg_route_distribution_group.command(name=cli_util.override('virtual_network.update_drg_route_distribution.command_name', 'update'), help=u"""Updates the specified route distribution \n[Command Reference](updateDrgRouteDistribution)""")
@cli_util.option('--drg-route-distribution-id', required=True, help=u"""The [OCID] of the route distribution.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

You cannot assign a table to a virtual circuit or IPSec connection attachment if there is a static route rule for an RPC attachment.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'DrgRouteDistribution'})
@cli_util.wrap_exceptions
def update_drg_route_distribution(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_route_distribution_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(drg_route_distribution_id, six.string_types) and len(drg_route_distribution_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-route-distribution-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_drg_route_distribution(
        drg_route_distribution_id=drg_route_distribution_id,
        update_drg_route_distribution_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_drg_route_distribution') and callable(getattr(client, 'get_drg_route_distribution')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_drg_route_distribution(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@drg_route_distribution_statement_group.command(name=cli_util.override('virtual_network.update_drg_route_distribution_statements.command_name', 'update'), help=u"""Updates one or more route distribution statements in the specified route distribution. \n[Command Reference](updateDrgRouteDistributionStatements)""")
@cli_util.option('--drg-route-distribution-id', required=True, help=u"""The [OCID] of the route distribution.""")
@cli_util.option('--statements', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The route distribution statements to update, and the details to be updated.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'statements': {'module': 'core', 'class': 'list[UpdateDrgRouteDistributionStatementDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'statements': {'module': 'core', 'class': 'list[UpdateDrgRouteDistributionStatementDetails]'}}, output_type={'module': 'core', 'class': 'list[DrgRouteDistributionStatement]'})
@cli_util.wrap_exceptions
def update_drg_route_distribution_statements(ctx, from_json, drg_route_distribution_id, statements):

    if isinstance(drg_route_distribution_id, six.string_types) and len(drg_route_distribution_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-route-distribution-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}
    _details['statements'] = cli_util.parse_json_parameter("statements", statements)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_drg_route_distribution_statements(
        drg_route_distribution_id=drg_route_distribution_id,
        update_drg_route_distribution_statements_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@drg_route_rule_group.command(name=cli_util.override('virtual_network.update_drg_route_rules.command_name', 'update'), help=u"""Updates one or more route rules in the specified DRG route table. \n[Command Reference](updateDrgRouteRules)""")
@cli_util.option('--drg-route-table-id', required=True, help=u"""The [OCID] of the DRG route table.""")
@cli_util.option('--route-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The DRG rute rules to update.

This option is a JSON list with items of type UpdateDrgRouteRuleDetails.  For documentation on UpdateDrgRouteRuleDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/UpdateDrgRouteRuleDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'route-rules': {'module': 'core', 'class': 'list[UpdateDrgRouteRuleDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'route-rules': {'module': 'core', 'class': 'list[UpdateDrgRouteRuleDetails]'}}, output_type={'module': 'core', 'class': 'list[DrgRouteRule]'})
@cli_util.wrap_exceptions
def update_drg_route_rules(ctx, from_json, drg_route_table_id, route_rules):

    if isinstance(drg_route_table_id, six.string_types) and len(drg_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-route-table-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}

    if route_rules is not None:
        _details['routeRules'] = cli_util.parse_json_parameter("route_rules", route_rules)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_drg_route_rules(
        drg_route_table_id=drg_route_table_id,
        update_drg_route_rules_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@drg_route_table_group.command(name=cli_util.override('virtual_network.update_drg_route_table.command_name', 'update'), help=u"""Updates the specified DRG route table. \n[Command Reference](updateDrgRouteTable)""")
@cli_util.option('--drg-route-table-id', required=True, help=u"""The [OCID] of the DRG route table.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

You can't assign a table to a virtual circuit or IPSec connection attachment if there is a static route rule for an RPC attachment.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--import-drg-route-distribution-id', help=u"""The [OCID] of the import route distribution used to specify how incoming route advertisements through referenced attachements are inserted into the DRG route table.""")
@cli_util.option('--is-ecmp-enabled', type=click.BOOL, help=u"""If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to your on-prem networks, set this value to true on the route table.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'DrgRouteTable'})
@cli_util.wrap_exceptions
def update_drg_route_table(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_route_table_id, defined_tags, display_name, freeform_tags, import_drg_route_distribution_id, is_ecmp_enabled, if_match):

    if isinstance(drg_route_table_id, six.string_types) and len(drg_route_table_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-route-table-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if import_drg_route_distribution_id is not None:
        _details['importDrgRouteDistributionId'] = import_drg_route_distribution_id

    if is_ecmp_enabled is not None:
        _details['isEcmpEnabled'] = is_ecmp_enabled

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_drg_route_table(
        drg_route_table_id=drg_route_table_id,
        update_drg_route_table_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_drg_route_table') and callable(getattr(client, 'get_drg_route_table')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_drg_route_table(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@internet_gateway_group.command(name=cli_util.override('virtual_network.update_internet_gateway.command_name', 'update'), help=u"""Updates the specified internet gateway. You can disable/enable it, or change its display name or tags. Avoid entering confidential information.

If the gateway is disabled, that means no traffic will flow to/from the internet even if there's a route rule that enables that traffic. \n[Command Reference](updateInternetGateway)""")
@cli_util.option('--ig-id', required=True, help=u"""The [OCID] of the internet gateway.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the gateway is enabled.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_internet_gateway(
        ig_id=ig_id,
        update_internet_gateway_details=_details,
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


@ip_sec_connection_group.command(name=cli_util.override('virtual_network.update_ip_sec_connection.command_name', 'update'), help=u"""Updates the specified IPSec connection.

To update an individual IPSec tunnel's attributes, use [UpdateIPSecConnectionTunnel]. \n[Command Reference](updateIPSecConnection)""")
@cli_util.option('--ipsc-id', required=True, help=u"""The [OCID] of the IPSec connection.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--cpe-local-identifier', help=u"""Your identifier for your CPE device. Can be either an IP address or a hostname (specifically, the fully qualified domain name (FQDN)). The type of identifier you provide here must correspond to the value for `cpeLocalIdentifierType`.

For information about why you'd provide this value, see [If Your CPE Is Behind a NAT Device].

Example IP address: `10.0.3.3`

Example hostname: `cpe.example.com`""")
@cli_util.option('--cpe-local-identifier-type', type=custom_types.CliCaseInsensitiveChoice(["IP_ADDRESS", "HOSTNAME"]), help=u"""The type of identifier for your CPE device. The value you provide here must correspond to the value for `cpeLocalIdentifier`.""")
@cli_util.option('--static-routes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Static routes to the CPE. If you provide this attribute, it replaces the entire current set of static routes. A static route's CIDR must not be a multicast address or class E address. The CIDR can be either IPv4 or IPv6. IPv6 addressing is supported for all commercial and government regions. See [IPv6 Addresses].

Example: `10.0.1.0/24`

Example: `2001:db8::/32`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'static-routes': {'module': 'core', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'static-routes': {'module': 'core', 'class': 'list[string]'}}, output_type={'module': 'core', 'class': 'IPSecConnection'})
@cli_util.wrap_exceptions
def update_ip_sec_connection(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, ipsc_id, defined_tags, display_name, freeform_tags, cpe_local_identifier, cpe_local_identifier_type, static_routes, if_match):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or static_routes:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and static-routes will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if cpe_local_identifier is not None:
        _details['cpeLocalIdentifier'] = cpe_local_identifier

    if cpe_local_identifier_type is not None:
        _details['cpeLocalIdentifierType'] = cpe_local_identifier_type

    if static_routes is not None:
        _details['staticRoutes'] = cli_util.parse_json_parameter("static_routes", static_routes)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_ip_sec_connection(
        ipsc_id=ipsc_id,
        update_ip_sec_connection_details=_details,
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


@ip_sec_connection_tunnel_group.command(name=cli_util.override('virtual_network.update_ip_sec_connection_tunnel.command_name', 'update'), help=u"""Updates the specified tunnel. This operation lets you change tunnel attributes such as the routing type (BGP dynamic routing or static routing). Here are some important notes:

  * If you change the tunnel's routing type or BGP session configuration, the tunnel will go     down while it's reprovisioned.

  * If you want to switch the tunnel's `routing` from `STATIC` to `BGP`, make sure the tunnel's     BGP session configuration attributes have been set ([bgpSessionConfig]).

  * If you want to switch the tunnel's `routing` from `BGP` to `STATIC`, make sure the     [IPSecConnection] already has at least one valid CIDR     static route. \n[Command Reference](updateIPSecConnectionTunnel)""")
@cli_util.option('--ipsc-id', required=True, help=u"""The [OCID] of the IPSec connection.""")
@cli_util.option('--tunnel-id', required=True, help=u"""The [OCID] of the tunnel.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--routing', type=custom_types.CliCaseInsensitiveChoice(["BGP", "STATIC", "POLICY"]), help=u"""The type of routing to use for this tunnel (either BGP dynamic routing or static routing).""")
@cli_util.option('--ike-version', type=custom_types.CliCaseInsensitiveChoice(["V1", "V2"]), help=u"""Internet Key Exchange protocol version.""")
@cli_util.option('--bgp-session-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--encryption-domain-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'bgp-session-config': {'module': 'core', 'class': 'UpdateIPSecTunnelBgpSessionDetails'}, 'encryption-domain-config': {'module': 'core', 'class': 'UpdateIPSecTunnelEncryptionDomainDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'bgp-session-config': {'module': 'core', 'class': 'UpdateIPSecTunnelBgpSessionDetails'}, 'encryption-domain-config': {'module': 'core', 'class': 'UpdateIPSecTunnelEncryptionDomainDetails'}}, output_type={'module': 'core', 'class': 'IPSecConnectionTunnel'})
@cli_util.wrap_exceptions
def update_ip_sec_connection_tunnel(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, ipsc_id, tunnel_id, display_name, routing, ike_version, bgp_session_config, encryption_domain_config, if_match):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')

    if isinstance(tunnel_id, six.string_types) and len(tunnel_id.strip()) == 0:
        raise click.UsageError('Parameter --tunnel-id cannot be whitespace or empty string')
    if not force:
        if bgp_session_config or encryption_domain_config:
            if not click.confirm("WARNING: Updates to bgp-session-config and encryption-domain-config will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if routing is not None:
        _details['routing'] = routing

    if ike_version is not None:
        _details['ikeVersion'] = ike_version

    if bgp_session_config is not None:
        _details['bgpSessionConfig'] = cli_util.parse_json_parameter("bgp_session_config", bgp_session_config)

    if encryption_domain_config is not None:
        _details['encryptionDomainConfig'] = cli_util.parse_json_parameter("encryption_domain_config", encryption_domain_config)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_ip_sec_connection_tunnel(
        ipsc_id=ipsc_id,
        tunnel_id=tunnel_id,
        update_ip_sec_connection_tunnel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_ip_sec_connection_tunnel') and callable(getattr(client, 'get_ip_sec_connection_tunnel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_ip_sec_connection_tunnel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@ip_sec_connection_tunnel_shared_secret_group.command(name=cli_util.override('virtual_network.update_ip_sec_connection_tunnel_shared_secret.command_name', 'update'), help=u"""Updates the shared secret (pre-shared key) for the specified tunnel.

**Important:** If you change the shared secret, the tunnel will go down while it's reprovisioned. \n[Command Reference](updateIPSecConnectionTunnelSharedSecret)""")
@cli_util.option('--ipsc-id', required=True, help=u"""The [OCID] of the IPSec connection.""")
@cli_util.option('--tunnel-id', required=True, help=u"""The [OCID] of the tunnel.""")
@cli_util.option('--shared-secret', help=u"""The shared secret (pre-shared key) to use for the tunnel. Only numbers, letters, and spaces are allowed.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'IPSecConnectionTunnelSharedSecret'})
@cli_util.wrap_exceptions
def update_ip_sec_connection_tunnel_shared_secret(ctx, from_json, ipsc_id, tunnel_id, shared_secret, if_match):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')

    if isinstance(tunnel_id, six.string_types) and len(tunnel_id.strip()) == 0:
        raise click.UsageError('Parameter --tunnel-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if shared_secret is not None:
        _details['sharedSecret'] = shared_secret

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_ip_sec_connection_tunnel_shared_secret(
        ipsc_id=ipsc_id,
        tunnel_id=tunnel_id,
        update_ip_sec_connection_tunnel_shared_secret_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ipv6_group.command(name=cli_util.override('virtual_network.update_ipv6.command_name', 'update'), help=u"""Updates the specified IPv6. You must specify the object's OCID. Use this operation if you want to:

  * Move an IPv6 to a different VNIC in the same subnet.   * Enable/disable internet access for an IPv6.   * Change the display name for an IPv6.   * Update resource tags for an IPv6. \n[Command Reference](updateIpv6)""")
@cli_util.option('--ipv6-id', required=True, help=u"""The [OCID] of the IPv6.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vnic-id', help=u"""The [OCID] of the VNIC to reassign the IPv6 to. The VNIC must be in the same subnet as the current VNIC.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Ipv6'})
@cli_util.wrap_exceptions
def update_ipv6(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, ipv6_id, defined_tags, display_name, freeform_tags, vnic_id, if_match):

    if isinstance(ipv6_id, six.string_types) and len(ipv6_id.strip()) == 0:
        raise click.UsageError('Parameter --ipv6-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if vnic_id is not None:
        _details['vnicId'] = vnic_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_ipv6(
        ipv6_id=ipv6_id,
        update_ipv6_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_ipv6') and callable(getattr(client, 'get_ipv6')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_ipv6(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@local_peering_gateway_group.command(name=cli_util.override('virtual_network.update_local_peering_gateway.command_name', 'update'), help=u"""Updates the specified local peering gateway (LPG). \n[Command Reference](updateLocalPeeringGateway)""")
@cli_util.option('--local-peering-gateway-id', required=True, help=u"""The [OCID] of the local peering gateway.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--route-table-id', help=u"""The OCID of the route table the LPG will use.

For information about why you would associate a route table with an LPG, see [Transit Routing: Access to Multiple VCNs in Same Region].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'LocalPeeringGateway'})
@cli_util.wrap_exceptions
def update_local_peering_gateway(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, local_peering_gateway_id, defined_tags, display_name, freeform_tags, route_table_id, if_match):

    if isinstance(local_peering_gateway_id, six.string_types) and len(local_peering_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --local-peering-gateway-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if route_table_id is not None:
        _details['routeTableId'] = route_table_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_local_peering_gateway(
        local_peering_gateway_id=local_peering_gateway_id,
        update_local_peering_gateway_details=_details,
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


@nat_gateway_group.command(name=cli_util.override('virtual_network.update_nat_gateway.command_name', 'update'), help=u"""Updates the specified NAT gateway. \n[Command Reference](updateNatGateway)""")
@cli_util.option('--nat-gateway-id', required=True, help=u"""The NAT gateway's [OCID].""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--block-traffic', type=click.BOOL, help=u"""Whether the NAT gateway blocks traffic through it. The default is `false`.

Example: `true`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if block_traffic is not None:
        _details['blockTraffic'] = block_traffic

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_nat_gateway(
        nat_gateway_id=nat_gateway_id,
        update_nat_gateway_details=_details,
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


@network_security_group_group.command(name=cli_util.override('virtual_network.update_network_security_group.command_name', 'update'), help=u"""Updates the specified network security group.

To add or remove an existing VNIC from the group, use [UpdateVnic].

To add a VNIC to the group *when you create the VNIC*, specify the NSG's OCID during creation. For example, see the `nsgIds` attribute in [CreateVnicDetails].

To add or remove security rules from the group, use [AddNetworkSecurityGroupSecurityRules] or [RemoveNetworkSecurityGroupSecurityRules].

To edit the contents of existing security rules in the group, use [UpdateNetworkSecurityGroupSecurityRules]. \n[Command Reference](updateNetworkSecurityGroup)""")
@cli_util.option('--network-security-group-id', required=True, help=u"""The [OCID] of the network security group.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'NetworkSecurityGroup'})
@cli_util.wrap_exceptions
def update_network_security_group(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, network_security_group_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(network_security_group_id, six.string_types) and len(network_security_group_id.strip()) == 0:
        raise click.UsageError('Parameter --network-security-group-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_network_security_group(
        network_security_group_id=network_security_group_id,
        update_network_security_group_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_network_security_group') and callable(getattr(client, 'get_network_security_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_network_security_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@security_rule_group.command(name=cli_util.override('virtual_network.update_network_security_group_security_rules.command_name', 'update-network-security-group'), help=u"""Updates one or more security rules in the specified network security group. \n[Command Reference](updateNetworkSecurityGroupSecurityRules)""")
@cli_util.option('--network-security-group-id', required=True, help=u"""The [OCID] of the network security group.""")
@cli_util.option('--security-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The NSG security rules to update.

This option is a JSON list with items of type UpdateSecurityRuleDetails.  For documentation on UpdateSecurityRuleDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/UpdateSecurityRuleDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'security-rules': {'module': 'core', 'class': 'list[UpdateSecurityRuleDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'security-rules': {'module': 'core', 'class': 'list[UpdateSecurityRuleDetails]'}}, output_type={'module': 'core', 'class': 'UpdatedNetworkSecurityGroupSecurityRules'})
@cli_util.wrap_exceptions
def update_network_security_group_security_rules(ctx, from_json, network_security_group_id, security_rules):

    if isinstance(network_security_group_id, six.string_types) and len(network_security_group_id.strip()) == 0:
        raise click.UsageError('Parameter --network-security-group-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}

    if security_rules is not None:
        _details['securityRules'] = cli_util.parse_json_parameter("security_rules", security_rules)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_network_security_group_security_rules(
        network_security_group_id=network_security_group_id,
        update_network_security_group_security_rules_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@private_ip_group.command(name=cli_util.override('virtual_network.update_private_ip.command_name', 'update'), help=u"""Updates the specified private IP. You must specify the object's OCID. Use this operation if you want to:

  - Move a secondary private IP to a different VNIC in the same subnet.   - Change the display name for a secondary private IP.   - Change the hostname for a secondary private IP.

This operation cannot be used with primary private IPs. To update the hostname for the primary IP on a VNIC, use [UpdateVnic]. \n[Command Reference](updatePrivateIp)""")
@cli_util.option('--private-ip-id', required=True, help=u"""The [OCID] of the private IP.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostname-label', help=u"""The hostname for the private IP. Used for DNS. The value is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952] and [RFC 1123].

For more information, see [DNS in Your Virtual Cloud Network].

Example: `bminstance-1`""")
@cli_util.option('--vnic-id', help=u"""The OCID of the VNIC to reassign the private IP to. The VNIC must be in the same subnet as the current VNIC.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
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

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if hostname_label is not None:
        _details['hostnameLabel'] = hostname_label

    if vnic_id is not None:
        _details['vnicId'] = vnic_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_private_ip(
        private_ip_id=private_ip_id,
        update_private_ip_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@public_ip_group.command(name=cli_util.override('virtual_network.update_public_ip.command_name', 'update'), help=u"""Updates the specified public IP. You must specify the object's OCID. Use this operation if you want to:

* Assign a reserved public IP in your pool to a private IP. * Move a reserved public IP to a different private IP. * Unassign a reserved public IP from a private IP (which returns it to your pool of reserved public IPs). * Change the display name or tags for a public IP.

Assigning, moving, and unassigning a reserved public IP are asynchronous operations. Poll the public IP's `lifecycleState` to determine if the operation succeeded.

**Note:** When moving a reserved public IP, the target private IP must not already have a public IP with `lifecycleState` = ASSIGNING or ASSIGNED. If it does, an error is returned. Also, the initial unassignment from the original private IP always succeeds, but the assignment to the target private IP is asynchronous and could fail silently (for example, if the target private IP is deleted or has a different public IP assigned to it in the interim). If that occurs, the public IP remains unassigned and its `lifecycleState` switches to AVAILABLE (it is not reassigned to its original private IP). You must poll the public IP's `lifecycleState` to determine if the move succeeded.

Regarding ephemeral public IPs:

* If you want to assign an ephemeral public IP to a primary private IP, use [CreatePublicIp]. * You can't move an ephemeral public IP to a different private IP. * If you want to unassign an ephemeral public IP from its private IP, use [DeletePublicIp], which unassigns and deletes the ephemeral public IP.

**Note:** If a public IP is assigned to a secondary private IP (see [PrivateIp]), and you move that secondary private IP to another VNIC, the public IP moves with it.

**Note:** There's a limit to the number of [public IPs] a VNIC or instance can have. If you try to move a reserved public IP to a VNIC or instance that has already reached its public IP limit, an error is returned. For information about the public IP limits, see [Public IP Addresses]. \n[Command Reference](updatePublicIp)""")
@cli_util.option('--public-ip-id', required=True, help=u"""The [OCID] of the public IP.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--private-ip-id', help=u"""The OCID of the private IP to assign the public IP to. * If the public IP is already assigned to a different private IP, it will be unassigned and then reassigned to the specified private IP. * If you set this field to an empty string, the public IP will be unassigned from the private IP it is currently assigned to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "ASSIGNING", "ASSIGNED", "UNASSIGNING", "UNASSIGNED", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if private_ip_id is not None:
        _details['privateIpId'] = private_ip_id

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_public_ip(
        public_ip_id=public_ip_id,
        update_public_ip_details=_details,
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


@public_ip_pool_group.command(name=cli_util.override('virtual_network.update_public_ip_pool.command_name', 'update'), help=u"""Updates the specified public IP pool. \n[Command Reference](updatePublicIpPool)""")
@cli_util.option('--public-ip-pool-id', required=True, help=u"""The [OCID] of the public IP pool.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["INACTIVE", "UPDATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'PublicIpPool'})
@cli_util.wrap_exceptions
def update_public_ip_pool(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, public_ip_pool_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(public_ip_pool_id, six.string_types) and len(public_ip_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --public-ip-pool-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_public_ip_pool(
        public_ip_pool_id=public_ip_pool_id,
        update_public_ip_pool_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_public_ip_pool') and callable(getattr(client, 'get_public_ip_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_public_ip_pool(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@remote_peering_connection_group.command(name=cli_util.override('virtual_network.update_remote_peering_connection.command_name', 'update'), help=u"""Updates the specified remote peering connection (RPC). \n[Command Reference](updateRemotePeeringConnection)""")
@cli_util.option('--remote-peering-connection-id', required=True, help=u"""The [OCID] of the remote peering connection (RPC).""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "PROVISIONING", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'RemotePeeringConnection'})
@cli_util.wrap_exceptions
def update_remote_peering_connection(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, remote_peering_connection_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(remote_peering_connection_id, six.string_types) and len(remote_peering_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --remote-peering-connection-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_remote_peering_connection(
        remote_peering_connection_id=remote_peering_connection_id,
        update_remote_peering_connection_details=_details,
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


@route_table_group.command(name=cli_util.override('virtual_network.update_route_table.command_name', 'update'), help=u"""Updates the specified route table's display name or route rules. Avoid entering confidential information.

Note that the `routeRules` object you provide replaces the entire existing set of rules. \n[Command Reference](updateRouteTable)""")
@cli_util.option('--rt-id', required=True, help=u"""The [OCID] of the route table.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--route-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The collection of rules used for routing destination IPs to network devices.

This option is a JSON list with items of type RouteRule.  For documentation on RouteRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/RouteRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if route_rules is not None:
        _details['routeRules'] = cli_util.parse_json_parameter("route_rules", route_rules)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_route_table(
        rt_id=rt_id,
        update_route_table_details=_details,
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


@security_list_group.command(name=cli_util.override('virtual_network.update_security_list.command_name', 'update'), help=u"""Updates the specified security list's display name or rules. Avoid entering confidential information.

Note that the `egressSecurityRules` or `ingressSecurityRules` objects you provide replace the entire existing objects. \n[Command Reference](updateSecurityList)""")
@cli_util.option('--security-list-id', required=True, help=u"""The [OCID] of the security list.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--egress-security-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Rules for allowing egress IP packets.

This option is a JSON list with items of type EgressSecurityRule.  For documentation on EgressSecurityRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/EgressSecurityRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ingress-security-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Rules for allowing ingress IP packets.

This option is a JSON list with items of type IngressSecurityRule.  For documentation on IngressSecurityRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/IngressSecurityRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if egress_security_rules is not None:
        _details['egressSecurityRules'] = cli_util.parse_json_parameter("egress_security_rules", egress_security_rules)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if ingress_security_rules is not None:
        _details['ingressSecurityRules'] = cli_util.parse_json_parameter("ingress_security_rules", ingress_security_rules)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_security_list(
        security_list_id=security_list_id,
        update_security_list_details=_details,
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


@service_gateway_group.command(name=cli_util.override('virtual_network.update_service_gateway.command_name', 'update'), help=u"""Updates the specified service gateway. The information you provide overwrites the existing attributes of the gateway. \n[Command Reference](updateServiceGateway)""")
@cli_util.option('--service-gateway-id', required=True, help=u"""The service gateway's [OCID].""")
@cli_util.option('--block-traffic', type=click.BOOL, help=u"""Whether the service gateway blocks all traffic through it. The default is `false`. When this is `true`, traffic is not routed to any services, regardless of route rules.

Example: `true`""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--route-table-id', help=u"""The OCID of the route table the service gateway will use. For information about why you would associate a route table with a service gateway, see [Transit Routing: Private Access to Oracle Services].""")
@cli_util.option('--services', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of all the `Service` objects you want enabled on this service gateway. Sending an empty list means you want to disable all services. Omitting this parameter entirely keeps the existing list of services intact.

You can also enable or disable a particular `Service` by using [AttachServiceId] or [DetachServiceId].

For each enabled `Service`, make sure there's a route rule with the `Service` object's `cidrBlock` as the rule's destination and the service gateway as the rule's target. See [Route Table].

This option is a JSON list with items of type ServiceIdRequestDetails.  For documentation on ServiceIdRequestDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/ServiceIdRequestDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'services': {'module': 'core', 'class': 'list[ServiceIdRequestDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'services': {'module': 'core', 'class': 'list[ServiceIdRequestDetails]'}}, output_type={'module': 'core', 'class': 'ServiceGateway'})
@cli_util.wrap_exceptions
def update_service_gateway(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, service_gateway_id, block_traffic, defined_tags, display_name, freeform_tags, route_table_id, services, if_match):

    if isinstance(service_gateway_id, six.string_types) and len(service_gateway_id.strip()) == 0:
        raise click.UsageError('Parameter --service-gateway-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or services:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and services will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if block_traffic is not None:
        _details['blockTraffic'] = block_traffic

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if route_table_id is not None:
        _details['routeTableId'] = route_table_id

    if services is not None:
        _details['services'] = cli_util.parse_json_parameter("services", services)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_service_gateway(
        service_gateway_id=service_gateway_id,
        update_service_gateway_details=_details,
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


@subnet_group.command(name=cli_util.override('virtual_network.update_subnet.command_name', 'update'), help=u"""Updates the specified subnet. \n[Command Reference](updateSubnet)""")
@cli_util.option('--subnet-id', required=True, help=u"""The [OCID] of the subnet.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dhcp-options-id', help=u"""The OCID of the set of DHCP options the subnet will use.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--route-table-id', help=u"""The OCID of the route table the subnet will use.""")
@cli_util.option('--security-list-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The OCIDs of the security list or lists the subnet will use. This replaces the entire current set of security lists. Remember that security lists are associated *with the subnet*, but the rules are applied to the individual VNICs in the subnet.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--cidr-block', help=u"""The CIDR block of the subnet. The new CIDR block must meet the following criteria:

- Must be valid. - The CIDR block's IP range must be completely within one of the VCN's CIDR block ranges. - The old and new CIDR block ranges must use the same network address. Example: `10.0.0.0/25` and `10.0.0.0/24`. - Must contain all IP addresses in use in the old CIDR range. - The new CIDR range's broadcast address (last IP address of CIDR range) must not be an IP address in use in the old CIDR range.

**Note:** If you are changing the CIDR block, you cannot create VNICs or private IPs for this resource while the update is in progress.

Example: `172.16.0.0/16`""")
@cli_util.option('--ipv6-cidr-block', help=u"""This is the IPv6 CIDR block for the subnet's IP address space. The subnet size is always /64. See [IPv6 Addresses]. The provided CIDR must maintain the following rules -

a. The IPv6 CIDR block is valid and correctly formatted. b. The IPv6 CIDR is within the parent VCN IPv6 range.

Example: `2001:0db8:0123:1111::/64`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'security-list-ids': {'module': 'core', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'security-list-ids': {'module': 'core', 'class': 'list[string]'}}, output_type={'module': 'core', 'class': 'Subnet'})
@cli_util.wrap_exceptions
def update_subnet(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, subnet_id, defined_tags, dhcp_options_id, display_name, freeform_tags, route_table_id, security_list_ids, cidr_block, ipv6_cidr_block, if_match):

    if isinstance(subnet_id, six.string_types) and len(subnet_id.strip()) == 0:
        raise click.UsageError('Parameter --subnet-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or security_list_ids:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and security-list-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if dhcp_options_id is not None:
        _details['dhcpOptionsId'] = dhcp_options_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if route_table_id is not None:
        _details['routeTableId'] = route_table_id

    if security_list_ids is not None:
        _details['securityListIds'] = cli_util.parse_json_parameter("security_list_ids", security_list_ids)

    if cidr_block is not None:
        _details['cidrBlock'] = cidr_block

    if ipv6_cidr_block is not None:
        _details['ipv6CidrBlock'] = ipv6_cidr_block

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_subnet(
        subnet_id=subnet_id,
        update_subnet_details=_details,
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


@tunnel_cpe_device_config_group.command(name=cli_util.override('virtual_network.update_tunnel_cpe_device_config.command_name', 'update'), help=u"""Creates or updates the set of CPE configuration answers for the specified tunnel. The answers correlate to the questions that are specific to the CPE device type (see the `parameters` attribute of [CpeDeviceShapeDetail]). \n[Command Reference](updateTunnelCpeDeviceConfig)""")
@cli_util.option('--ipsc-id', required=True, help=u"""The [OCID] of the IPSec connection.""")
@cli_util.option('--tunnel-id', required=True, help=u"""The [OCID] of the tunnel.""")
@cli_util.option('--tunnel-cpe-device-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The set of configuration answers for a CPE device.

This option is a JSON list with items of type CpeDeviceConfigAnswer.  For documentation on CpeDeviceConfigAnswer please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/CpeDeviceConfigAnswer.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'tunnel-cpe-device-config': {'module': 'core', 'class': 'list[CpeDeviceConfigAnswer]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'tunnel-cpe-device-config': {'module': 'core', 'class': 'list[CpeDeviceConfigAnswer]'}}, output_type={'module': 'core', 'class': 'TunnelCpeDeviceConfig'})
@cli_util.wrap_exceptions
def update_tunnel_cpe_device_config(ctx, from_json, force, ipsc_id, tunnel_id, tunnel_cpe_device_config, if_match):

    if isinstance(ipsc_id, six.string_types) and len(ipsc_id.strip()) == 0:
        raise click.UsageError('Parameter --ipsc-id cannot be whitespace or empty string')

    if isinstance(tunnel_id, six.string_types) and len(tunnel_id.strip()) == 0:
        raise click.UsageError('Parameter --tunnel-id cannot be whitespace or empty string')
    if not force:
        if tunnel_cpe_device_config:
            if not click.confirm("WARNING: Updates to tunnel-cpe-device-config will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if tunnel_cpe_device_config is not None:
        _details['tunnelCpeDeviceConfig'] = cli_util.parse_json_parameter("tunnel_cpe_device_config", tunnel_cpe_device_config)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_tunnel_cpe_device_config(
        ipsc_id=ipsc_id,
        tunnel_id=tunnel_id,
        update_tunnel_cpe_device_config_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vcn_group.command(name=cli_util.override('virtual_network.update_vcn.command_name', 'update'), help=u"""Updates the specified VCN. \n[Command Reference](updateVcn)""")
@cli_util.option('--vcn-id', required=True, help=u"""The [OCID] of the VCN.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_vcn(
        vcn_id=vcn_id,
        update_vcn_details=_details,
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


@virtual_circuit_group.command(name=cli_util.override('virtual_network.update_virtual_circuit.command_name', 'update'), help=u"""Updates the specified virtual circuit. This can be called by either the customer who owns the virtual circuit, or the provider (when provisioning or de-provisioning the virtual circuit from their end). The documentation for [UpdateVirtualCircuitDetails] indicates who can update each property of the virtual circuit.

**Important:** If the virtual circuit is working and in the PROVISIONED state, updating any of the network-related properties (such as the DRG being used, the BGP ASN, and so on) will cause the virtual circuit's state to switch to PROVISIONING and the related BGP session to go down. After Oracle re-provisions the virtual circuit, its state will return to PROVISIONED. Make sure you confirm that the associated BGP session is back up. For more information about the various states and how to test connectivity, see [FastConnect Overview].

To change the list of public IP prefixes for a public virtual circuit, use [BulkAddVirtualCircuitPublicPrefixes] and [BulkDeleteVirtualCircuitPublicPrefixes]. Updating the list of prefixes does NOT cause the BGP session to go down. However, Oracle must verify the customer's ownership of each added prefix before traffic for that prefix will flow across the virtual circuit. \n[Command Reference](updateVirtualCircuit)""")
@cli_util.option('--virtual-circuit-id', required=True, help=u"""The [OCID] of the virtual circuit.""")
@cli_util.option('--bandwidth-shape-name', help=u"""The provisioned data rate of the connection. To get a list of the available bandwidth levels (that is, shapes), see [ListFastConnectProviderVirtualCircuitBandwidthShapes]. To be updated only by the customer who owns the virtual circuit.""")
@cli_util.option('--cross-connect-mappings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of mappings, each containing properties for a cross-connect or cross-connect group associated with this virtual circuit.

The customer and provider can update different properties in the mapping depending on the situation. See the description of the [CrossConnectMapping].

This option is a JSON list with items of type CrossConnectMapping.  For documentation on CrossConnectMapping please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/CrossConnectMapping.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--routing-policy', type=custom_types.CliCaseInsensitiveChoice(["ORACLE_SERVICE_NETWORK", "REGIONAL", "MARKET_LEVEL", "GLOBAL"]), help=u"""The routing policy sets how routing information about the Oracle cloud is shared over a public virtual circuit. Policies available are: `ORACLE_SERVICE_NETWORK`, `REGIONAL`, `MARKET_LEVEL`, and `GLOBAL`. See [Route Filtering] for details. By default, routing information is shared for all routes in the same market.""")
@cli_util.option('--customer-bgp-asn', type=click.INT, help=u"""Deprecated. Instead use `customerAsn`. If you specify values for both, the request will be rejected.""")
@cli_util.option('--customer-asn', type=click.INT, help=u"""The BGP ASN of the network at the other end of the BGP session from Oracle.

If the BGP session is from the customer's edge router to Oracle, the required value is the customer's ASN, and it can be updated only by the customer.

If the BGP session is from the provider's edge router to Oracle, the required value is the provider's ASN, and it can be updated only by the provider.

Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique. Avoid entering confidential information.

To be updated only by the customer who owns the virtual circuit.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--gateway-id', help=u"""The OCID of the [dynamic routing gateway (DRG)] that this private virtual circuit uses.

To be updated only by the customer who owns the virtual circuit.""")
@cli_util.option('--provider-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), help=u"""The provider's state in relation to this virtual circuit. Relevant only if the customer is using FastConnect via a provider. ACTIVE means the provider has provisioned the virtual circuit from their end. INACTIVE means the provider has not yet provisioned the virtual circuit, or has de-provisioned it.

To be updated only by the provider.""")
@cli_util.option('--provider-service-key-name', help=u"""The service key name offered by the provider (if the customer is connecting via a provider).""")
@cli_util.option('--reference-comment', help=u"""Provider-supplied reference information about this virtual circuit. Relevant only if the customer is using FastConnect via a provider.

To be updated only by the provider.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PENDING_PROVIDER", "VERIFYING", "PROVISIONING", "PROVISIONED", "FAILED", "INACTIVE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'cross-connect-mappings': {'module': 'core', 'class': 'list[CrossConnectMapping]'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'cross-connect-mappings': {'module': 'core', 'class': 'list[CrossConnectMapping]'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'VirtualCircuit'})
@cli_util.wrap_exceptions
def update_virtual_circuit(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, virtual_circuit_id, bandwidth_shape_name, cross_connect_mappings, routing_policy, customer_bgp_asn, customer_asn, defined_tags, display_name, freeform_tags, gateway_id, provider_state, provider_service_key_name, reference_comment, if_match):

    if isinstance(virtual_circuit_id, six.string_types) and len(virtual_circuit_id.strip()) == 0:
        raise click.UsageError('Parameter --virtual-circuit-id cannot be whitespace or empty string')
    if not force:
        if cross_connect_mappings or routing_policy or defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to cross-connect-mappings and routing-policy and defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if bandwidth_shape_name is not None:
        _details['bandwidthShapeName'] = bandwidth_shape_name

    if cross_connect_mappings is not None:
        _details['crossConnectMappings'] = cli_util.parse_json_parameter("cross_connect_mappings", cross_connect_mappings)

    if routing_policy is not None:
        _details['routingPolicy'] = cli_util.parse_json_parameter("routing_policy", routing_policy)

    if customer_bgp_asn is not None:
        _details['customerBgpAsn'] = customer_bgp_asn

    if customer_asn is not None:
        _details['customerAsn'] = customer_asn

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if gateway_id is not None:
        _details['gatewayId'] = gateway_id

    if provider_state is not None:
        _details['providerState'] = provider_state

    if provider_service_key_name is not None:
        _details['providerServiceKeyName'] = provider_service_key_name

    if reference_comment is not None:
        _details['referenceComment'] = reference_comment

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_virtual_circuit(
        virtual_circuit_id=virtual_circuit_id,
        update_virtual_circuit_details=_details,
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


@vlan_group.command(name=cli_util.override('virtual_network.update_vlan.command_name', 'update'), help=u"""Updates the specified VLAN. Note that this operation might require changes to all the VNICs in the VLAN, which can take a while. The VLAN will be in the UPDATING state until the changes are complete. \n[Command Reference](updateVlan)""")
@cli_util.option('--vlan-id', required=True, help=u"""The [OCID] of the VLAN.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A descriptive name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the OCIDs of the network security groups (NSGs) to use with this VLAN. All VNICs in the VLAN will belong to these NSGs. For more information about NSGs, see [NetworkSecurityGroup].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--route-table-id', help=u"""The OCID of the route table the VLAN will use.""")
@cli_util.option('--cidr-block', help=u"""The CIDR block of the VLAN. The new CIDR block must meet the following criteria:

- Must be valid. - The CIDR block's IP range must be completely within one of the VCN's CIDR block ranges. - The old and new CIDR block ranges must use the same network address. Example: `10.0.0.0/25` and `10.0.0.0/24`. - Must contain all IP addresses in use in the old CIDR range. - The new CIDR range's broadcast address (last IP address of CIDR range) must not be an IP address in use in the old CIDR range.

**Note:** If you are changing the CIDR block, you cannot create VNICs or private IPs for this resource while the update is in progress.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'core', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'core', 'class': 'list[string]'}}, output_type={'module': 'core', 'class': 'Vlan'})
@cli_util.wrap_exceptions
def update_vlan(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, vlan_id, defined_tags, display_name, freeform_tags, nsg_ids, route_table_id, cidr_block, if_match):

    if isinstance(vlan_id, six.string_types) and len(vlan_id.strip()) == 0:
        raise click.UsageError('Parameter --vlan-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or nsg_ids:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and nsg-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if route_table_id is not None:
        _details['routeTableId'] = route_table_id

    if cidr_block is not None:
        _details['cidrBlock'] = cidr_block

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_vlan(
        vlan_id=vlan_id,
        update_vlan_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vlan') and callable(getattr(client, 'get_vlan')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vlan(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@vnic_group.command(name=cli_util.override('virtual_network.update_vnic.command_name', 'update'), help=u"""Updates the specified VNIC. \n[Command Reference](updateVnic)""")
@cli_util.option('--vnic-id', required=True, help=u"""The [OCID] of the VNIC.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostname-label', help=u"""The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952] and [RFC 1123]. The value appears in the [Vnic] object and also the [PrivateIp] object returned by [ListPrivateIps] and [GetPrivateIp].

For more information, see [DNS in Your Virtual Cloud Network].""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. Setting this as an empty array removes the VNIC from all network security groups.

If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of belonging to a subnet), the value of the `nsgIds` attribute is ignored. Instead, the VNIC belongs to the NSGs that are associated with the VLAN itself. See [Vlan].

For more information about NSGs, see [NetworkSecurityGroup].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--skip-source-dest-check', type=click.BOOL, help=u"""Whether the source/destination check is disabled on the VNIC. Defaults to `false`, which means the check is performed. For information about why you would skip the source/destination check, see [Using a Private IP as a Route Target].

If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of belonging to a subnet), the value of the `skipSourceDestCheck` attribute is ignored. This is because the source/destination check is always disabled for VNICs in a VLAN. Example: `true`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'core', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'core', 'class': 'list[string]'}}, output_type={'module': 'core', 'class': 'Vnic'})
@cli_util.wrap_exceptions
def update_vnic(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, vnic_id, defined_tags, display_name, freeform_tags, hostname_label, nsg_ids, skip_source_dest_check, if_match):

    if isinstance(vnic_id, six.string_types) and len(vnic_id.strip()) == 0:
        raise click.UsageError('Parameter --vnic-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or nsg_ids:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and nsg-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if hostname_label is not None:
        _details['hostnameLabel'] = hostname_label

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if skip_source_dest_check is not None:
        _details['skipSourceDestCheck'] = skip_source_dest_check

    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.update_vnic(
        vnic_id=vnic_id,
        update_vnic_details=_details,
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


@drg_group.command(name=cli_util.override('virtual_network.upgrade_drg.command_name', 'upgrade'), help=u"""Upgrades the DRG. After upgrade, you can control routing inside your DRG via DRG attachments, route distributions, and DRG route tables. \n[Command Reference](upgradeDrg)""")
@cli_util.option('--drg-id', required=True, help=u"""The [[OCID]](/iaas/Content/General/Concepts/identifiers.htm) of the DRG.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def upgrade_drg(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, drg_id):

    if isinstance(drg_id, six.string_types) and len(drg_id.strip()) == 0:
        raise click.UsageError('Parameter --drg-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.upgrade_drg(
        drg_id=drg_id,
        **kwargs
    )
    work_request_client = cli_util.build_client('work_requests', 'work_request', ctx)
    if wait_for_state:

        if hasattr(work_request_client, 'get_work_request') and callable(getattr(work_request_client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(work_request_client, work_request_client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
                if hasattr(result, "data") and hasattr(result.data, "resources") and len(result.data.resources) == 1:
                    entity_type = result.data.resources[0].entity_type
                    identifier = result.data.resources[0].identifier
                    get_operation = 'get_' + entity_type
                    if hasattr(client, get_operation) and callable(getattr(client, get_operation)):
                        result = getattr(client, get_operation)(identifier)

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


@byoip_range_group.command(name=cli_util.override('virtual_network.validate_byoip_range.command_name', 'validate'), help=u"""Submits the BYOIP CIDR block you are importing for validation. Do not submit to Oracle for validation if you have not already modified the information for the BYOIP CIDR block with your Regional Internet Registry. See [To import a CIDR block] for details. \n[Command Reference](validateByoipRange)""")
@cli_util.option('--byoip-range-id', required=True, help=u"""The [OCID] of the `ByoipRange` resource containing the BYOIP CIDR block.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def validate_byoip_range(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, byoip_range_id):

    if isinstance(byoip_range_id, six.string_types) and len(byoip_range_id.strip()) == 0:
        raise click.UsageError('Parameter --byoip-range-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.validate_byoip_range(
        byoip_range_id=byoip_range_id,
        **kwargs
    )
    work_request_client = cli_util.build_client('work_requests', 'work_request', ctx)
    if wait_for_state:

        if hasattr(work_request_client, 'get_work_request') and callable(getattr(work_request_client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(work_request_client, work_request_client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
                if hasattr(result, "data") and hasattr(result.data, "resources") and len(result.data.resources) == 1:
                    entity_type = result.data.resources[0].entity_type
                    identifier = result.data.resources[0].identifier
                    get_operation = 'get_' + entity_type
                    if hasattr(client, get_operation) and callable(getattr(client, get_operation)):
                        result = getattr(client, get_operation)(identifier)

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


@byoip_range_group.command(name=cli_util.override('virtual_network.withdraw_byoip_range.command_name', 'withdraw'), help=u"""Withdraws BGP route advertisement for the BYOIP CIDR block. \n[Command Reference](withdrawByoipRange)""")
@cli_util.option('--byoip-range-id', required=True, help=u"""The [OCID] of the `ByoipRange` resource containing the BYOIP CIDR block.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def withdraw_byoip_range(ctx, from_json, byoip_range_id):

    if isinstance(byoip_range_id, six.string_types) and len(byoip_range_id.strip()) == 0:
        raise click.UsageError('Parameter --byoip-range-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'virtual_network', ctx)
    result = client.withdraw_byoip_range(
        byoip_range_id=byoip_range_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)
