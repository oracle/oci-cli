# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
from ..cli_root import cli
from .. import cli_util


@cli.group(cli_util.override('virtual_network_group.command_name', 'virtual_network'), help=cli_util.override('virtual_network_group.help', """APIs for Networking Service, Compute Service, and Block Volume Service."""))
@cli_util.help_option_group
def virtual_network_group():
    pass


@click.group(cli_util.override('vcn_group.command_name', 'vcn'), help="""A Virtual Cloud Network (VCN). For more information, see
[Overview of the Networking Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def vcn_group():
    pass


@click.group(cli_util.override('subnet_group.command_name', 'subnet'), help="""A logical subdivision of a VCN. Each subnet exists in a single Availability Domain and
consists of a contiguous range of IP addresses that do not overlap with
other subnets in the VCN. Example: 172.16.1.0/24. For more information, see
[Overview of the Networking Service] and
[Managing Subnets].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def subnet_group():
    pass


@click.group(cli_util.override('ip_sec_connection_device_status_group.command_name', 'ip-sec-connection-device-status'), help="""Status of the IPSec connection.""")
@cli_util.help_option_group
def ip_sec_connection_device_status_group():
    pass


@click.group(cli_util.override('drg_attachment_group.command_name', 'drg-attachment'), help="""A link between a DRG and VCN. For more information, see
[Overview of the Networking Service].""")
@cli_util.help_option_group
def drg_attachment_group():
    pass


@click.group(cli_util.override('ip_sec_connection_device_config_group.command_name', 'ip-sec-connection-device-config'), help="""Information about the IPSecConnection device configuration.""")
@cli_util.help_option_group
def ip_sec_connection_device_config_group():
    pass


@click.group(cli_util.override('vnic_group.command_name', 'vnic'), help="""A virtual network interface card. Each VNIC resides in a subnet in a VCN.
An instance attaches to a VNIC to obtain a network connection into the VCN
through that subnet. Each instance has a *primary VNIC* that is automatically
created and attached during launch. You can add *secondary VNICs* to an
instance after it's launched. For more information, see
[Managing Virtual Network Interface Cards (VNICs)].

Each VNIC has a *primary private IP* that is automatically assigned during launch.
You can add *secondary private IPs* to a VNIC after it's created. For more
information, see [CreatePrivateIp] and
[Managing IP Addresses].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def vnic_group():
    pass


@click.group(cli_util.override('dhcp_options_group.command_name', 'dhcp-options'), help="""A set of DHCP options. Used by the VCN to automatically provide configuration
information to the instances when they boot up. There are two options you can set:

- [DhcpDnsOption]: Lets you specify how DNS (hostname resolution) is
handled in the subnets in your VCN.

- [DhcpSearchDomainOption]: Lets you specify
a search domain name to use for DNS queries.

For more information, see  [DNS in Your Virtual Cloud Network]
and [Managing DHCP Options].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def dhcp_options_group():
    pass


@click.group(cli_util.override('fast_connect_provider_service_group.command_name', 'fast-connect-provider-service'), help="""A service offering from a supported provider. For more information,
see [FastConnect Overview].""")
@cli_util.help_option_group
def fast_connect_provider_service_group():
    pass


@click.group(cli_util.override('virtual_circuit_bandwidth_shape_group.command_name', 'virtual-circuit-bandwidth-shape'), help="""An individual bandwidth level for virtual circuits.""")
@cli_util.help_option_group
def virtual_circuit_bandwidth_shape_group():
    pass


@click.group(cli_util.override('cross_connect_location_group.command_name', 'cross-connect-location'), help="""An individual FastConnect location.""")
@cli_util.help_option_group
def cross_connect_location_group():
    pass


@click.group(cli_util.override('private_ip_group.command_name', 'private-ip'), help="""A *private IP* is a conceptual term that refers to a private IP address and related properties.
The `privateIp` object is the API representation of a private IP.

Each instance has a *primary private IP* that is automatically created and
assigned to the primary VNIC during instance launch. If you add a secondary
VNIC to the instance, it also automatically gets a primary private IP. You
can't remove a primary private IP from its VNIC. The primary private IP is
automatically deleted when the VNIC is terminated.

You can add *secondary private IPs* to a VNIC after it's created. For more
information, see the `privateIp` operations and also
[Managing IP Addresses].

**Note:** Only
[ListPrivateIps] and
[GetPrivateIp] work with
*primary* private IPs. To create and update primary private IPs, you instead
work with instance and VNIC operations. For example, a primary private IP's
properties come from the values you specify in
[CreateVnicDetails] when calling either
[LaunchInstance] or
[AttachVnic]. To update the hostname
for a primary private IP, you use [UpdateVnic].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def private_ip_group():
    pass


@click.group(cli_util.override('virtual_circuit_group.command_name', 'virtual-circuit'), help="""For use with Oracle Bare Metal Cloud Services FastConnect.

A virtual circuit is an isolated network path that runs over one or more physical
network connections to provide a single, logical connection between the edge router
on the customer's existing network and a DRG. A customer could have multiple virtual
circuits, for example, to isolate traffic from different parts of their organization
(one virtual circuit for 10.0.1.0/24; another for 172.16.0.0/16), or to provide redundancy.

Each virtual circuit is made up of information shared between a customer, Oracle,
and a provider (if the customer is using FastConnect via a provider). Who fills in
a given property of a virtual circuit depends on whether the BGP session related to
that virtual circuit goes from the customer's edge router to Oracle, or from the provider's
edge router to Oracle. Also, in the case where the customer is using a provider, values
for some of the properties may not be present immediately, but may get filled in as the
provider and Oracle each do their part to provision the virtual circuit.

For more information, see [FastConnect Overview].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def virtual_circuit_group():
    pass


@click.group(cli_util.override('internet_gateway_group.command_name', 'internet-gateway'), help="""Represents a router that connects the edge of a VCN with the Internet. For an example scenario
that uses an Internet Gateway, see
[Typical Networking Service Scenarios].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def internet_gateway_group():
    pass


@click.group(cli_util.override('ip_sec_connection_group.command_name', 'ip-sec-connection'), help="""A connection between a DRG and CPE. This connection consists of multiple IPSec
tunnels. Creating this connection is one of the steps required when setting up
an IPSec VPN. For more information, see
[Overview of the Networking Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def ip_sec_connection_group():
    pass


@click.group(cli_util.override('cross_connect_port_speed_shape_group.command_name', 'cross-connect-port-speed-shape'), help="""An individual port speed level for cross-connects.""")
@cli_util.help_option_group
def cross_connect_port_speed_shape_group():
    pass


@click.group(cli_util.override('drg_group.command_name', 'drg'), help="""A Dynamic Routing Gateway (DRG), which is a virtual router that provides a path for private
network traffic between your VCN and your existing network. You use it with other Networking
Service components to create an IPSec VPN or a connection that uses
Oracle Bare Metal Cloud Services FastConnect. For more information, see
[Overview of the Networking Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def drg_group():
    pass


@click.group(cli_util.override('route_table_group.command_name', 'route-table'), help="""A collection of `RouteRule` objects, which are used to route packets
based on destination IP to a particular network entity. For more information, see
[Overview of the Networking Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def route_table_group():
    pass


@click.group(cli_util.override('cpe_group.command_name', 'cpe'), help="""An object you create when setting up an IPSec VPN between your on-premise network
and VCN. The `Cpe` is a virtual representation of your Customer-Premises Equipment,
which is the actual router on-premise at your site at your end of the IPSec VPN connection.
For more information,
see [Overview of the Networking Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def cpe_group():
    pass


@click.group(cli_util.override('cross_connect_group_group.command_name', 'cross-connect-group'), help="""For use with Oracle Bare Metal Cloud Services FastConnect. A cross-connect group
is a link aggregation group (LAG), which can contain one or more
[CrossConnects]. Customers who are colocated with
Oracle in a FastConnect location create and use cross-connect groups. For more
information, see [FastConnect Overview].

**Note:** If you're a provider who is setting up a physical connection to Oracle so customers
can use FastConnect over the connection, be aware that your connection is modeled the
same way as a colocated customer's (with `CrossConnect` and `CrossConnectGroup` objects, etc.).

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def cross_connect_group_group():
    pass


@click.group(cli_util.override('cross_connect_group.command_name', 'cross-connect'), help="""For use with Oracle Bare Metal Cloud Services FastConnect. A cross-connect represents a
physical connection between an existing network and Oracle. Customers who are colocated
with Oracle in a FastConnect location create and use cross-connects. For more
information, see [FastConnect Overview].

Oracle recommends you create each cross-connect in a
[CrossConnectGroup] so you can use link aggregation
with the connection.

**Note:** If you're a provider who is setting up a physical connection to Oracle so customers
can use FastConnect over the connection, be aware that your connection is modeled the
same way as a colocated customer's (with `CrossConnect` and `CrossConnectGroup` objects, etc.).

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def cross_connect_group():
    pass


@click.group(cli_util.override('letter_of_authority_group.command_name', 'letter-of-authority'), help="""The Letter of Authority for the cross-connect. You must submit this letter when
requesting cabling for the cross-connect at the FastConnect location.""")
@cli_util.help_option_group
def letter_of_authority_group():
    pass


@click.group(cli_util.override('cross_connect_status_group.command_name', 'cross-connect-status'), help="""The status of the cross-connect.""")
@cli_util.help_option_group
def cross_connect_status_group():
    pass


@click.group(cli_util.override('security_list_group.command_name', 'security-list'), help="""A set of virtual firewall rules for your VCN. Security lists are configured at the subnet
level, but the rules are applied to the ingress and egress traffic for the individual instances
in the subnet. The rules can be stateful or stateless. For more information, see
[Security Lists].

**Important:** Oracle Bare Metal Cloud Services images automatically include firewall rules (e.g.,
Linux iptables, Windows firewall). If there are issues with some type of access to an instance,
make sure both the security lists associated with the instance's subnet and the instance's
firewall rules are set correctly.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def security_list_group():
    pass


@cpe_group.command(name=cli_util.override('create_cpe.command_name', 'create'), help="""Creates a new virtual Customer-Premises Equipment (CPE) object in the specified compartment. For more information, see [Managing IPSec VPNs].

For the purposes of access control, you must provide the OCID of the compartment where you want the CPE to reside. Notice that the CPE doesn't have to be in the same compartment as the IPSec connection or other Networking Service components. If you're not sure which compartment to use, put the CPE in the same compartment as the DRG. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You must provide the public IP address of your on-premise router. See [Configuring Your On-Premise Router].

You may optionally specify a *display name* for the CPE, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the CPE.""")
@click.option('--ip-address', required=True, help="""The public IP address of the on-premise router.

Example: `143.19.23.16`""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_cpe(ctx, compartment_id, ip_address, display_name):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['ipAddress'] = ip_address

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_cpe(
        create_cpe_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@cross_connect_group.command(name=cli_util.override('create_cross_connect.command_name', 'create'), help="""Creates a new cross-connect. Oracle recommends you create each cross-connect in a [CrossConnectGroup] so you can use link aggregation with the connection.

After creating the `CrossConnect` object, you need to go the FastConnect location and request to have the physical cable installed. For more information, see [FastConnect Overview].

For the purposes of access control, you must provide the OCID of the compartment where you want the cross-connect to reside. If you're not sure which compartment to use, put the cross-connect in the same compartment with your VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the cross-connect. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the cross-connect.""")
@click.option('--location-name', required=True, help="""The name of the FastConnect location where this cross-connect will be installed. To get a list of the available locations, see [ListCrossConnectLocations].

Example: `CyrusOne, Chandler, AZ`""")
@click.option('--port-speed-shape-name', required=True, help="""The port speed for this cross-connect. To get a list of the available port speeds, see [ListCrossConnectPortSpeedShapes].

Example: `10 Gbps`""")
@click.option('--cross-connect-group-id', help="""The OCID of the cross-connect group to put this cross-connect in.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--far-cross-connect-or-cross-connect-group-id', help="""If you already have an existing cross-connect or cross-connect group at this FastConnect location, and you want this new cross-connect to be on a different router (for the purposes of redundancy), provide the OCID of that existing cross-connect or cross-connect group.""")
@click.option('--near-cross-connect-or-cross-connect-group-id', help="""If you already have an existing cross-connect or cross-connect group at this FastConnect location, and you want this new cross-connect to be on the same router, provide the OCID of that existing cross-connect or cross-connect group.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_cross_connect(ctx, compartment_id, location_name, port_speed_shape_name, cross_connect_group_id, display_name, far_cross_connect_or_cross_connect_group_id, near_cross_connect_or_cross_connect_group_id):
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
    cli_util.render_response(result)


@cross_connect_group_group.command(name=cli_util.override('create_cross_connect_group.command_name', 'create'), help="""Creates a new cross-connect group to use with Oracle Bare Metal Cloud Services FastConnect. For more information, see [FastConnect Overview].

For the purposes of access control, you must provide the OCID of the compartment where you want the cross-connect group to reside. If you're not sure which compartment to use, put the cross-connect group in the same compartment with your VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the cross-connect group. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the cross-connect group.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_cross_connect_group(ctx, compartment_id, display_name):
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
    cli_util.render_response(result)


@dhcp_options_group.command(name=cli_util.override('create_dhcp_options.command_name', 'create'), help="""Creates a new set of DHCP options for the specified VCN. For more information, see [DhcpOptions].

For the purposes of access control, you must provide the OCID of the compartment where you want the set of DHCP options to reside. Notice that the set of options doesn't have to be in the same compartment as the VCN, subnets, or other Networking Service components. If you're not sure which compartment to use, put the set of DHCP options in the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the set of DHCP options, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the set of DHCP options.""")
@click.option('--options', required=True, help="""A set of DHCP options.""")
@click.option('--vcn-id', required=True, help="""The OCID of the VCN the set of DHCP options belongs to.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_dhcp_options(ctx, compartment_id, options, vcn_id, display_name):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['options'] = cli_util.parse_json_parameter("options", options)
    details['vcnId'] = vcn_id

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_dhcp_options(
        create_dhcp_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@drg_group.command(name=cli_util.override('create_drg.command_name', 'create'), help="""Creates a new Dynamic Routing Gateway (DRG) in the specified compartment. For more information, see [Managing Dynamic Routing Gateways (DRGs)].

For the purposes of access control, you must provide the OCID of the compartment where you want the DRG to reside. Notice that the DRG doesn't have to be in the same compartment as the VCN, the DRG attachment, or other Networking Service components. If you're not sure which compartment to use, put the DRG in the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the DRG, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the DRG.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_drg(ctx, compartment_id, display_name):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_drg(
        create_drg_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@drg_attachment_group.command(name=cli_util.override('create_drg_attachment.command_name', 'create'), help="""Attaches the specified DRG to the specified VCN. A VCN can be attached to only one DRG at a time, and vice versa. The response includes a `DrgAttachment` object with its own OCID. For more information about DRGs, see [Managing Dynamic Routing Gateways (DRGs)].

You may optionally specify a *display name* for the attachment, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

For the purposes of access control, the DRG attachment is automatically placed into the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service].""")
@click.option('--drg-id', required=True, help="""The OCID of the DRG.""")
@click.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique. Avoid entering confidential information.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_drg_attachment(ctx, drg_id, vcn_id, display_name):
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
    cli_util.render_response(result)


@internet_gateway_group.command(name=cli_util.override('create_internet_gateway.command_name', 'create'), help="""Creates a new Internet Gateway for the specified VCN. For more information, see [Managing Internet Gateways].

For the purposes of access control, you must provide the OCID of the compartment where you want the Internet Gateway to reside. Notice that the Internet Gateway doesn't have to be in the same compartment as the VCN or other Networking Service components. If you're not sure which compartment to use, put the Internet Gateway in the same compartment with the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the Internet Gateway, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

For traffic to flow between a subnet and an Internet Gateway, you must create a route rule accordingly in the subnet's route table (e.g., 0.0.0.0/0 > Internet Gateway). See [UpdateRouteTable].

You must specify whether the Internet Gateway is enabled when you create it. If it's disabled, that means no traffic will flow to/from the internet even if there's a route rule that enables that traffic. You can later use [UpdateInternetGateway] to easily disable/enable the gateway without changing the route rule.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the Internet Gateway.""")
@click.option('--is-enabled', required=True, help="""Whether the gateway is enabled upon creation.""")
@click.option('--vcn-id', required=True, help="""The OCID of the VCN the Internet Gateway is attached to.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_internet_gateway(ctx, compartment_id, is_enabled, vcn_id, display_name):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['isEnabled'] = is_enabled
    details['vcnId'] = vcn_id

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_internet_gateway(
        create_internet_gateway_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@ip_sec_connection_group.command(name=cli_util.override('create_ip_sec_connection.command_name', 'create'), help="""Creates a new IPSec connection between the specified DRG and CPE. For more information, see [Managing IPSec Connections].

In the request, you must include at least one static route to the CPE object (you're allowed a maximum of 10). For example: 10.0.8.0/16.

For the purposes of access control, you must provide the OCID of the compartment where you want the IPSec connection to reside. Notice that the IPSec connection doesn't have to be in the same compartment as the DRG, CPE, or other Networking Service components. If you're not sure which compartment to use, put the IPSec connection in the same compartment as the DRG. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the IPSec connection, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

After creating the IPSec connection, you need to configure your on-premise router with tunnel-specific information returned by [GetIPSecConnectionDeviceConfig]. For each tunnel, that operation gives you the IP address of Oracle's VPN headend and the shared secret (i.e., the pre-shared key). For more information, see [Configuring Your On-Premise Router].

To get the status of the tunnels (whether they're up or down), use [GetIPSecConnectionDeviceStatus].""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the IPSec connection.""")
@click.option('--cpe-id', required=True, help="""The OCID of the CPE.""")
@click.option('--drg-id', required=True, help="""The OCID of the DRG.""")
@click.option('--static-routes', required=True, help="""Static routes to the CPE. At least one route must be included. The CIDR must not be a multicast address or class E address.

Example: `10.0.1.0/24`""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_ip_sec_connection(ctx, compartment_id, cpe_id, drg_id, static_routes, display_name):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['cpeId'] = cpe_id
    details['drgId'] = drg_id
    details['staticRoutes'] = cli_util.parse_json_parameter("static_routes", static_routes)

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_ip_sec_connection(
        create_ip_sec_connection_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@private_ip_group.command(name=cli_util.override('create_private_ip.command_name', 'create'), help="""Creates a secondary private IP for the specified VNIC. For more information about secondary private IPs, see [Managing IP Addresses].""")
@click.option('--vnic-id', required=True, help="""The OCID of the VNIC to assign the private IP to. The VNIC and private IP must be in the same subnet.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--hostname-label', help="""The hostname for the private IP. Used for DNS. The value is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952] and [RFC 1123].

For more information, see [DNS in Your Virtual Cloud Network].

Example: `bminstance-1`""")
@click.option('--ip-address', help="""A private IP address of your choice. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet.

Example: `10.0.3.3`""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_private_ip(ctx, vnic_id, display_name, hostname_label, ip_address):
    kwargs = {}

    details = {}
    details['vnicId'] = vnic_id

    if display_name is not None:
        details['displayName'] = display_name

    if hostname_label is not None:
        details['hostnameLabel'] = hostname_label

    if ip_address is not None:
        details['ipAddress'] = ip_address

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_private_ip(
        create_private_ip_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@route_table_group.command(name=cli_util.override('create_route_table.command_name', 'create'), help="""Creates a new route table for the specified VCN. In the request you must also include at least one route rule for the new route table. For information on the number of rules you can have in a route table, see [Service Limits]. For general information about route tables in your VCN, see [Managing Route Tables].

For the purposes of access control, you must provide the OCID of the compartment where you want the route table to reside. Notice that the route table doesn't have to be in the same compartment as the VCN, subnets, or other Networking Service components. If you're not sure which compartment to use, put the route table in the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the route table, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the route table.""")
@click.option('--route-rules', required=True, help="""The collection of rules used for routing destination IPs to network devices.""")
@click.option('--vcn-id', required=True, help="""The OCID of the VCN the route table belongs to.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_route_table(ctx, compartment_id, route_rules, vcn_id, display_name):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['routeRules'] = cli_util.parse_json_parameter("route_rules", route_rules)
    details['vcnId'] = vcn_id

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_route_table(
        create_route_table_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@security_list_group.command(name=cli_util.override('create_security_list.command_name', 'create'), help="""Creates a new security list for the specified VCN. For more information about security lists, see [Security Lists]. For information on the number of rules you can have in a security list, see [Service Limits].

For the purposes of access control, you must provide the OCID of the compartment where you want the security list to reside. Notice that the security list doesn't have to be in the same compartment as the VCN, subnets, or other Networking Service components. If you're not sure which compartment to use, put the security list in the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the security list, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the security list.""")
@click.option('--egress-security-rules', required=True, help="""Rules for allowing egress IP packets.""")
@click.option('--ingress-security-rules', required=True, help="""Rules for allowing ingress IP packets.""")
@click.option('--vcn-id', required=True, help="""The OCID of the VCN the security list belongs to.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_security_list(ctx, compartment_id, egress_security_rules, ingress_security_rules, vcn_id, display_name):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['egressSecurityRules'] = cli_util.parse_json_parameter("egress_security_rules", egress_security_rules)
    details['ingressSecurityRules'] = cli_util.parse_json_parameter("ingress_security_rules", ingress_security_rules)
    details['vcnId'] = vcn_id

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_security_list(
        create_security_list_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@subnet_group.command(name=cli_util.override('create_subnet.command_name', 'create'), help="""Creates a new subnet in the specified VCN. You can't change the size of the subnet after creation, so it's important to think about the size of subnets you need before creating them. For more information, see [Managing Subnets]. For information on the number of subnets you can have in a VCN, see [Service Limits].

For the purposes of access control, you must provide the OCID of the compartment where you want the subnet to reside. Notice that the subnet doesn't have to be in the same compartment as the VCN, route tables, or other Networking Service components. If you're not sure which compartment to use, put the subnet in the same compartment as the VCN. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally associate a route table with the subnet. If you don't, the subnet will use the VCN's default route table. For more information about route tables, see [Managing Route Tables].

You may optionally associate a security list with the subnet. If you don't, the subnet will use the VCN's default security list. For more information about security lists, see [Security Lists].

You may optionally associate a set of DHCP options with the subnet. If you don't, the subnet will use the VCN's default set. For more information about DHCP options, see [Managing DHCP Options].

You may optionally specify a *display name* for the subnet, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

You can also add a DNS label for the subnet, which is required if you want the Internet and VCN Resolver to resolve hostnames for instances in the subnet. For more information, see [DNS in Your Virtual Cloud Network].""")
@click.option('--availability-domain', required=True, help="""The Availability Domain to contain the subnet.

Example: `Uocm:PHX-AD-1`""")
@click.option('--cidr-block', required=True, help="""The CIDR IP address range of the subnet.

Example: `172.16.1.0/24`""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the subnet.""")
@click.option('--vcn-id', required=True, help="""The OCID of the VCN to contain the subnet.""")
@click.option('--dhcp-options-id', help="""The OCID of the set of DHCP options the subnet will use. If you don't provide a value, the subnet will use the VCN's default set of DHCP options.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--dns-label', help="""A DNS label for the subnet, used in conjunction with the VNIC's hostname and VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (e.g., `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be an alphanumeric string that begins with a letter and is unique within the VCN. The value cannot be changed.

This value must be set if you want to use the Internet and VCN Resolver to resolve the hostnames of instances in the subnet. It can only be set if the VCN itself was created with a DNS label.

For more information, see [DNS in Your Virtual Cloud Network].

Example: `subnet123`""")
@click.option('--prohibit-public-ip-on-vnic', help="""Whether VNICs within this subnet can have public IP addresses. Defaults to false, which means VNICs created in this subnet will automatically be assigned public IP addresses unless specified otherwise during instance launch or VNIC creation (with the `assignPublicIp` flag in [CreateVnicDetails]). If `prohibitPublicIpOnVnic` is set to true, VNICs created in this subnet cannot have public IP addresses (i.e., it's a private subnet).

Example: `true`""")
@click.option('--route-table-id', help="""The OCID of the route table the subnet will use. If you don't provide a value, the subnet will use the VCN's default route table.""")
@click.option('--security-list-ids', help="""OCIDs for the security lists to associate with the subnet. If you don't provide a value, the VCN's default security list will be associated with the subnet. Remember that security lists are associated at the subnet level, but the rules are applied to the individual VNICs in the subnet.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_subnet(ctx, availability_domain, cidr_block, compartment_id, vcn_id, dhcp_options_id, display_name, dns_label, prohibit_public_ip_on_vnic, route_table_id, security_list_ids):
    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['cidrBlock'] = cidr_block
    details['compartmentId'] = compartment_id
    details['vcnId'] = vcn_id

    if dhcp_options_id is not None:
        details['dhcpOptionsId'] = dhcp_options_id

    if display_name is not None:
        details['displayName'] = display_name

    if dns_label is not None:
        details['dnsLabel'] = dns_label

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
    cli_util.render_response(result)


@vcn_group.command(name=cli_util.override('create_vcn.command_name', 'create'), help="""Creates a new Virtual Cloud Network (VCN). For more information, see [Managing Virtual Cloud Networks (VCNs)].

For the VCN you must specify a single, contiguous IPv4 CIDR block. Oracle recommends using one of the private IP address ranges specified in [RFC 1918] (10.0.0.0/8, 172.16/12, and 192.168/16). Example: 172.16.0.0/16. The CIDR block can range from /16 to /30, and it must not overlap with your on-premise network. You can't change the size of the VCN after creation.

For the purposes of access control, you must provide the OCID of the compartment where you want the VCN to reside. Consult an Oracle Bare Metal Cloud Services administrator in your organization if you're not sure which compartment to use. Notice that the VCN doesn't have to be in the same compartment as the subnets or other Networking Service components. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the VCN, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

You can also add a DNS label for the VCN, which is required if you want the instances to use the Interent and VCN Resolver option for DNS in the VCN. For more information, see [DNS in Your Virtual Cloud Network].

The VCN automatically comes with a default route table, default security list, and default set of DHCP options. The OCID for each is returned in the response. You can't delete these default objects, but you can change their contents (i.e., route rules, etc.)

The VCN and subnets you create are not accessible until you attach an Internet Gateway or set up an IPSec VPN or FastConnect. For more information, see [Overview of the Networking Service].""")
@click.option('--cidr-block', required=True, help="""The CIDR IP address block of the VCN.

Example: `172.16.0.0/16`""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the VCN.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--dns-label', help="""A DNS label for the VCN, used in conjunction with the VNIC's hostname and subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (e.g., `bminstance-1.subnet123.vcn1.oraclevcn.com`). Not required to be unique, but it's a best practice to set unique DNS labels for VCNs in your tenancy. Must be an alphanumeric string that begins with a letter. The value cannot be changed.

You must set this value if you want instances to be able to use hostnames to resolve other instances in the VCN. Otherwise the Internet and VCN Resolver will not work.

For more information, see [DNS in Your Virtual Cloud Network].

Example: `vcn1`""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_vcn(ctx, cidr_block, compartment_id, display_name, dns_label):
    kwargs = {}

    details = {}
    details['cidrBlock'] = cidr_block
    details['compartmentId'] = compartment_id

    if display_name is not None:
        details['displayName'] = display_name

    if dns_label is not None:
        details['dnsLabel'] = dns_label

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_vcn(
        create_vcn_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@virtual_circuit_group.command(name=cli_util.override('create_virtual_circuit.command_name', 'create'), help="""Creates a new virtual circuit to use with Oracle Bare Metal Cloud Services FastConnect. For more information, see [FastConnect Overview].

For the purposes of access control, you must provide the OCID of the compartment where you want the virtual circuit to reside. If you're not sure which compartment to use, put the virtual circuit in the same compartment with the DRG it's using. For more information about compartments and access control, see [Overview of the IAM Service]. For information about OCIDs, see [Resource Identifiers].

You may optionally specify a *display name* for the virtual circuit. It does not have to be unique, and you can change it. Avoid entering confidential information.

**Important:** When creating a virtual circuit, you specify a DRG for the traffic to flow through. Make sure you attach the DRG to your VCN and confirm the VCN's routing sends traffic to the DRG. Otherwise traffic will not flow. For more information, see [Managing Route Tables].""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment to contain the virtual circuit.""")
@click.option('--region', required=True, help="""The Oracle Bare Metal Cloud Services region where this virtual circuit is located.

Example: `phx`""")
@click.option('--type', required=True, help="""The type of IP addresses used in this virtual circuit. PRIVATE means [RFC 1918] addresses (10.0.0.0/8, 172.16/12, and 192.168/16). Only PRIVATE is supported.""")
@click.option('--bandwidth-shape-name', help="""The provisioned data rate of the connection.  To get a list of the available bandwidth levels (i.e., shapes), see [ListVirtualCircuitBandwidthShapes].

Example: `10 Gbps`""")
@click.option('--cross-connect-mappings', help="""Create a `CrossConnectMapping` for each cross-connect or cross-connect group this virtual circuit will run on.""")
@click.option('--customer-bgp-asn', help="""Your BGP ASN (either public or private). Provide this value only if there's a BGP session that goes from your edge router to Oracle. Otherwise, leave this empty or null.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--gateway-id', help="""The OCID of the [Dynamic Routing Gateway (DRG)] that this virtual circuit uses.""")
@click.option('--provider-name', help="""The name of the provider (if you're connecting via a provider). To get a list of the provider names, see [ListFastConnectProviderServices].""")
@click.option('--provider-service-name', help="""The name of the service offered by the provider (if you're connecting via a provider). To get a list of the available service offerings, see [ListFastConnectProviderServices].""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_virtual_circuit(ctx, compartment_id, region, type, bandwidth_shape_name, cross_connect_mappings, customer_bgp_asn, display_name, gateway_id, provider_name, provider_service_name):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['region'] = region
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

    if provider_service_name is not None:
        details['providerServiceName'] = provider_service_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.create_virtual_circuit(
        create_virtual_circuit_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@cpe_group.command(name=cli_util.override('delete_cpe.command_name', 'delete'), help="""Deletes the specified CPE object. The CPE must not be connected to a DRG. This is an asynchronous operation; the CPE's `lifecycleState` will change to TERMINATING temporarily until the CPE is completely removed.""")
@click.option('--cpe-id', required=True, help="""The OCID of the CPE.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_cpe(ctx, cpe_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_cpe(
        cpe_id=cpe_id,
        **kwargs
    )
    cli_util.render_response(result)


@cross_connect_group.command(name=cli_util.override('delete_cross_connect.command_name', 'delete'), help="""Deletes the specified cross-connect. It must not be mapped to a [VirtualCircuit].""")
@click.option('--cross-connect-id', required=True, help="""The OCID of the cross-connect.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_cross_connect(ctx, cross_connect_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_cross_connect(
        cross_connect_id=cross_connect_id,
        **kwargs
    )
    cli_util.render_response(result)


@cross_connect_group_group.command(name=cli_util.override('delete_cross_connect_group.command_name', 'delete'), help="""Deletes the specified cross-connect group. It must not contain any cross-connects, and it cannot be mapped to a [VirtualCircuit].""")
@click.option('--cross-connect-group-id', required=True, help="""The OCID of the cross-connect group.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_cross_connect_group(ctx, cross_connect_group_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_cross_connect_group(
        cross_connect_group_id=cross_connect_group_id,
        **kwargs
    )
    cli_util.render_response(result)


@dhcp_options_group.command(name=cli_util.override('delete_dhcp_options.command_name', 'delete'), help="""Deletes the specified set of DHCP options, but only if it's not associated with a subnet. You can't delete a VCN's default set of DHCP options.

This is an asynchronous operation; the state of the set of options will switch to TERMINATING temporarily until the set is completely removed.""")
@click.option('--dhcp-id', required=True, help="""The OCID for the set of DHCP options.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_dhcp_options(ctx, dhcp_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_dhcp_options(
        dhcp_id=dhcp_id,
        **kwargs
    )
    cli_util.render_response(result)


@drg_group.command(name=cli_util.override('delete_drg.command_name', 'delete'), help="""Deletes the specified DRG. The DRG must not be attached to a VCN or be connected to your on-premise network. Also, there must not be a route table that lists the DRG as a target. This is an asynchronous operation; the DRG's `lifecycleState` will change to TERMINATING temporarily until the DRG is completely removed.""")
@click.option('--drg-id', required=True, help="""The OCID of the DRG.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_drg(ctx, drg_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_drg(
        drg_id=drg_id,
        **kwargs
    )
    cli_util.render_response(result)


@drg_attachment_group.command(name=cli_util.override('delete_drg_attachment.command_name', 'delete'), help="""Detaches a DRG from a VCN by deleting the corresponding `DrgAttachment`. This is an asynchronous operation; the attachment's `lifecycleState` will change to DETACHING temporarily until the attachment is completely removed.""")
@click.option('--drg-attachment-id', required=True, help="""The OCID of the DRG attachment.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_drg_attachment(ctx, drg_attachment_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_drg_attachment(
        drg_attachment_id=drg_attachment_id,
        **kwargs
    )
    cli_util.render_response(result)


@internet_gateway_group.command(name=cli_util.override('delete_internet_gateway.command_name', 'delete'), help="""Deletes the specified Internet Gateway. The Internet Gateway does not have to be disabled, but there must not be a route table that lists it as a target.

This is an asynchronous operation; the gateway's `lifecycleState` will change to TERMINATING temporarily until the gateway is completely removed.""")
@click.option('--ig-id', required=True, help="""The OCID of the Internet Gateway.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_internet_gateway(ctx, ig_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_internet_gateway(
        ig_id=ig_id,
        **kwargs
    )
    cli_util.render_response(result)


@ip_sec_connection_group.command(name=cli_util.override('delete_ip_sec_connection.command_name', 'delete'), help="""Deletes the specified IPSec connection. If your goal is to disable the IPSec VPN between your VCN and on-premise network, it's easiest to simply detach the DRG but keep all the IPSec VPN components intact. If you were to delete all the components and then later need to create an IPSec VPN again, you would need to configure your on-premise router again with the new information returned from [CreateIPSecConnection].

This is an asynchronous operation; the connection's `lifecycleState` will change to TERMINATING temporarily until the connection is completely removed.""")
@click.option('--ipsc-id', required=True, help="""The OCID of the IPSec connection.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_ip_sec_connection(ctx, ipsc_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_ip_sec_connection(
        ipsc_id=ipsc_id,
        **kwargs
    )
    cli_util.render_response(result)


@private_ip_group.command(name=cli_util.override('delete_private_ip.command_name', 'delete'), help="""Unassigns and deletes the specified private IP. You must specify the object's OCID. The private IP address is returned to the subnet's pool of available addresses.

This operation cannot be used with primary private IPs, which are automatically unassigned and deleted when the VNIC is terminated.""")
@click.option('--private-ip-id', required=True, help="""The private IP's OCID.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_private_ip(ctx, private_ip_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_private_ip(
        private_ip_id=private_ip_id,
        **kwargs
    )
    cli_util.render_response(result)


@route_table_group.command(name=cli_util.override('delete_route_table.command_name', 'delete'), help="""Deletes the specified route table, but only if it's not associated with a subnet. You can't delete a VCN's default route table.

This is an asynchronous operation; the route table's `lifecycleState` will change to TERMINATING temporarily until the route table is completely removed.""")
@click.option('--rt-id', required=True, help="""The OCID of the route table.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_route_table(ctx, rt_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_route_table(
        rt_id=rt_id,
        **kwargs
    )
    cli_util.render_response(result)


@security_list_group.command(name=cli_util.override('delete_security_list.command_name', 'delete'), help="""Deletes the specified security list, but only if it's not associated with a subnet. You can't delete a VCN's default security list.

This is an asynchronous operation; the security list's `lifecycleState` will change to TERMINATING temporarily until the security list is completely removed.""")
@click.option('--security-list-id', required=True, help="""The OCID of the security list.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_security_list(ctx, security_list_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_security_list(
        security_list_id=security_list_id,
        **kwargs
    )
    cli_util.render_response(result)


@subnet_group.command(name=cli_util.override('delete_subnet.command_name', 'delete'), help="""Deletes the specified subnet, but only if there are no instances in the subnet. This is an asynchronous operation; the subnet's `lifecycleState` will change to TERMINATING temporarily. If there are any instances in the subnet, the state will instead change back to AVAILABLE.""")
@click.option('--subnet-id', required=True, help="""The OCID of the subnet.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_subnet(ctx, subnet_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_subnet(
        subnet_id=subnet_id,
        **kwargs
    )
    cli_util.render_response(result)


@vcn_group.command(name=cli_util.override('delete_vcn.command_name', 'delete'), help="""Deletes the specified VCN. The VCN must be empty and have no attached gateways. This is an asynchronous operation; the VCN's `lifecycleState` will change to TERMINATING temporarily until the VCN is completely removed.""")
@click.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_vcn(ctx, vcn_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_vcn(
        vcn_id=vcn_id,
        **kwargs
    )
    cli_util.render_response(result)


@virtual_circuit_group.command(name=cli_util.override('delete_virtual_circuit.command_name', 'delete'), help="""Deletes the specified virtual circuit.

**Important:** If you're using FastConnect via a provider, make sure to also terminate the connection with the provider, or else the provider may continue to bill you.""")
@click.option('--virtual-circuit-id', required=True, help="""The OCID of the virtual circuit.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_virtual_circuit(ctx, virtual_circuit_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('virtual_network', ctx)
    result = client.delete_virtual_circuit(
        virtual_circuit_id=virtual_circuit_id,
        **kwargs
    )
    cli_util.render_response(result)


@cpe_group.command(name=cli_util.override('get_cpe.command_name', 'get'), help="""Gets the specified CPE's information.""")
@click.option('--cpe-id', required=True, help="""The OCID of the CPE.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_cpe(ctx, cpe_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_cpe(
        cpe_id=cpe_id,
        **kwargs
    )
    cli_util.render_response(result)


@cross_connect_group.command(name=cli_util.override('get_cross_connect.command_name', 'get'), help="""Gets the specified cross-connect's information.""")
@click.option('--cross-connect-id', required=True, help="""The OCID of the cross-connect.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_cross_connect(ctx, cross_connect_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_cross_connect(
        cross_connect_id=cross_connect_id,
        **kwargs
    )
    cli_util.render_response(result)


@cross_connect_group_group.command(name=cli_util.override('get_cross_connect_group.command_name', 'get'), help="""Gets the specified cross-connect group's information.""")
@click.option('--cross-connect-group-id', required=True, help="""The OCID of the cross-connect group.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_cross_connect_group(ctx, cross_connect_group_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_cross_connect_group(
        cross_connect_group_id=cross_connect_group_id,
        **kwargs
    )
    cli_util.render_response(result)


@letter_of_authority_group.command(name=cli_util.override('get_cross_connect_letter_of_authority.command_name', 'get-cross-connect'), help="""Gets the Letter of Authority for the specified cross-connect.""")
@click.option('--cross-connect-id', required=True, help="""The OCID of the cross-connect.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_cross_connect_letter_of_authority(ctx, cross_connect_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_cross_connect_letter_of_authority(
        cross_connect_id=cross_connect_id,
        **kwargs
    )
    cli_util.render_response(result)


@cross_connect_status_group.command(name=cli_util.override('get_cross_connect_status.command_name', 'get'), help="""Gets the status of the specified cross-connect.""")
@click.option('--cross-connect-id', required=True, help="""The OCID of the cross-connect.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_cross_connect_status(ctx, cross_connect_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_cross_connect_status(
        cross_connect_id=cross_connect_id,
        **kwargs
    )
    cli_util.render_response(result)


@dhcp_options_group.command(name=cli_util.override('get_dhcp_options.command_name', 'get'), help="""Gets the specified set of DHCP options.""")
@click.option('--dhcp-id', required=True, help="""The OCID for the set of DHCP options.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_dhcp_options(ctx, dhcp_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_dhcp_options(
        dhcp_id=dhcp_id,
        **kwargs
    )
    cli_util.render_response(result)


@drg_group.command(name=cli_util.override('get_drg.command_name', 'get'), help="""Gets the specified DRG's information.""")
@click.option('--drg-id', required=True, help="""The OCID of the DRG.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_drg(ctx, drg_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_drg(
        drg_id=drg_id,
        **kwargs
    )
    cli_util.render_response(result)


@drg_attachment_group.command(name=cli_util.override('get_drg_attachment.command_name', 'get'), help="""Gets the information for the specified `DrgAttachment`.""")
@click.option('--drg-attachment-id', required=True, help="""The OCID of the DRG attachment.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_drg_attachment(ctx, drg_attachment_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_drg_attachment(
        drg_attachment_id=drg_attachment_id,
        **kwargs
    )
    cli_util.render_response(result)


@internet_gateway_group.command(name=cli_util.override('get_internet_gateway.command_name', 'get'), help="""Gets the specified Internet Gateway's information.""")
@click.option('--ig-id', required=True, help="""The OCID of the Internet Gateway.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_internet_gateway(ctx, ig_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_internet_gateway(
        ig_id=ig_id,
        **kwargs
    )
    cli_util.render_response(result)


@ip_sec_connection_group.command(name=cli_util.override('get_ip_sec_connection.command_name', 'get'), help="""Gets the specified IPSec connection's basic information, including the static routes for the on-premise router. If you want the status of the connection (whether it's up or down), use [GetIPSecConnectionDeviceStatus].""")
@click.option('--ipsc-id', required=True, help="""The OCID of the IPSec connection.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_ip_sec_connection(ctx, ipsc_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_ip_sec_connection(
        ipsc_id=ipsc_id,
        **kwargs
    )
    cli_util.render_response(result)


@ip_sec_connection_device_config_group.command(name=cli_util.override('get_ip_sec_connection_device_config.command_name', 'get'), help="""Gets the configuration information for the specified IPSec connection. For each tunnel, the response includes the IP address of Oracle's VPN headend and the shared secret.""")
@click.option('--ipsc-id', required=True, help="""The OCID of the IPSec connection.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_ip_sec_connection_device_config(ctx, ipsc_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_ip_sec_connection_device_config(
        ipsc_id=ipsc_id,
        **kwargs
    )
    cli_util.render_response(result)


@ip_sec_connection_device_status_group.command(name=cli_util.override('get_ip_sec_connection_device_status.command_name', 'get'), help="""Gets the status of the specified IPSec connection (whether it's up or down).""")
@click.option('--ipsc-id', required=True, help="""The OCID of the IPSec connection.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_ip_sec_connection_device_status(ctx, ipsc_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_ip_sec_connection_device_status(
        ipsc_id=ipsc_id,
        **kwargs
    )
    cli_util.render_response(result)


@private_ip_group.command(name=cli_util.override('get_private_ip.command_name', 'get'), help="""Gets the specified private IP. You must specify the object's OCID. Alternatively, you can get the object by using [ListPrivateIps] with the private IP address (for example, 10.0.3.3) and subnet OCID.""")
@click.option('--private-ip-id', required=True, help="""The private IP's OCID.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_private_ip(ctx, private_ip_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_private_ip(
        private_ip_id=private_ip_id,
        **kwargs
    )
    cli_util.render_response(result)


@route_table_group.command(name=cli_util.override('get_route_table.command_name', 'get'), help="""Gets the specified route table's information.""")
@click.option('--rt-id', required=True, help="""The OCID of the route table.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_route_table(ctx, rt_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_route_table(
        rt_id=rt_id,
        **kwargs
    )
    cli_util.render_response(result)


@security_list_group.command(name=cli_util.override('get_security_list.command_name', 'get'), help="""Gets the specified security list's information.""")
@click.option('--security-list-id', required=True, help="""The OCID of the security list.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_security_list(ctx, security_list_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_security_list(
        security_list_id=security_list_id,
        **kwargs
    )
    cli_util.render_response(result)


@subnet_group.command(name=cli_util.override('get_subnet.command_name', 'get'), help="""Gets the specified subnet's information.""")
@click.option('--subnet-id', required=True, help="""The OCID of the subnet.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_subnet(ctx, subnet_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_subnet(
        subnet_id=subnet_id,
        **kwargs
    )
    cli_util.render_response(result)


@vcn_group.command(name=cli_util.override('get_vcn.command_name', 'get'), help="""Gets the specified VCN's information.""")
@click.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_vcn(ctx, vcn_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_vcn(
        vcn_id=vcn_id,
        **kwargs
    )
    cli_util.render_response(result)


@virtual_circuit_group.command(name=cli_util.override('get_virtual_circuit.command_name', 'get'), help="""Gets the specified virtual circuit's information.""")
@click.option('--virtual-circuit-id', required=True, help="""The OCID of the virtual circuit.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_virtual_circuit(ctx, virtual_circuit_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_virtual_circuit(
        virtual_circuit_id=virtual_circuit_id,
        **kwargs
    )
    cli_util.render_response(result)


@vnic_group.command(name=cli_util.override('get_vnic.command_name', 'get'), help="""Gets the information for the specified virtual network interface card (VNIC). You can get the VNIC OCID from the [ListVnicAttachments] operation.""")
@click.option('--vnic-id', required=True, help="""The OCID of the VNIC.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_vnic(ctx, vnic_id):
    kwargs = {}
    client = cli_util.build_client('virtual_network', ctx)
    result = client.get_vnic(
        vnic_id=vnic_id,
        **kwargs
    )
    cli_util.render_response(result)


@cpe_group.command(name=cli_util.override('list_cpes.command_name', 'list'), help="""Lists the Customer-Premises Equipment objects (CPEs) in the specified compartment.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_cpes(ctx, compartment_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_cpes(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@cross_connect_group_group.command(name=cli_util.override('list_cross_connect_groups.command_name', 'list'), help="""Lists the cross-connect groups in the specified compartment.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_cross_connect_groups(ctx, compartment_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_cross_connect_groups(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@cross_connect_location_group.command(name=cli_util.override('list_cross_connect_locations.command_name', 'list'), help="""Lists the available FastConnect locations for cross-connect installation. You need this information so you can specify your desired location when you create a cross-connect.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_cross_connect_locations(ctx, compartment_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_cross_connect_locations(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@cross_connect_group.command(name=cli_util.override('list_cross_connects.command_name', 'list'), help="""Lists the cross-connects in the specified compartment. You can filter the list by specifying the OCID of a cross-connect group.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--cross-connect-group-id', help="""The OCID of the cross-connect group.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_cross_connects(ctx, compartment_id, cross_connect_group_id, limit, page):
    kwargs = {}
    if cross_connect_group_id is not None:
        kwargs['cross_connect_group_id'] = cross_connect_group_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_cross_connects(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@cross_connect_port_speed_shape_group.command(name=cli_util.override('list_crossconnect_port_speed_shapes.command_name', 'list-crossconnect-port-speed-shapes'), help="""Lists the available port speeds for cross-connects. You need this information so you can specify your desired port speed (i.e., shape) when you create a cross-connect.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_crossconnect_port_speed_shapes(ctx, compartment_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_crossconnect_port_speed_shapes(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@dhcp_options_group.command(name=cli_util.override('list_dhcp_options.command_name', 'list'), help="""Lists the sets of DHCP options in the specified VCN and specified compartment. The response includes the default set of options that automatically comes with each VCN, plus any other sets you've created.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_dhcp_options(ctx, compartment_id, vcn_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_dhcp_options(
        compartment_id=compartment_id,
        vcn_id=vcn_id,
        **kwargs
    )
    cli_util.render_response(result)


@drg_attachment_group.command(name=cli_util.override('list_drg_attachments.command_name', 'list'), help="""Lists the `DrgAttachment` objects for the specified compartment. You can filter the results by VCN or DRG.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--vcn-id', help="""The OCID of the VCN.""")
@click.option('--drg-id', help="""The OCID of the DRG.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_drg_attachments(ctx, compartment_id, vcn_id, drg_id, limit, page):
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
    result = client.list_drg_attachments(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@drg_group.command(name=cli_util.override('list_drgs.command_name', 'list'), help="""Lists the DRGs in the specified compartment.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_drgs(ctx, compartment_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_drgs(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@fast_connect_provider_service_group.command(name=cli_util.override('list_fast_connect_provider_services.command_name', 'list'), help="""Lists the service offerings from supported providers. You need this information so you can specify your desired provider and service offering when you create a virtual circuit.

For the compartment ID, provide the OCID of your tenancy (the root compartment).

For more information, see [FastConnect Overview].""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_fast_connect_provider_services(ctx, compartment_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_fast_connect_provider_services(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@internet_gateway_group.command(name=cli_util.override('list_internet_gateways.command_name', 'list'), help="""Lists the Internet Gateways in the specified VCN and the specified compartment.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_internet_gateways(ctx, compartment_id, vcn_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_internet_gateways(
        compartment_id=compartment_id,
        vcn_id=vcn_id,
        **kwargs
    )
    cli_util.render_response(result)


@ip_sec_connection_group.command(name=cli_util.override('list_ip_sec_connections.command_name', 'list'), help="""Lists the IPSec connections for the specified compartment. You can filter the results by DRG or CPE.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--drg-id', help="""The OCID of the DRG.""")
@click.option('--cpe-id', help="""The OCID of the CPE.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_ip_sec_connections(ctx, compartment_id, drg_id, cpe_id, limit, page):
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
    result = client.list_ip_sec_connections(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@private_ip_group.command(name=cli_util.override('list_private_ips.command_name', 'list'), help="""Lists the [PrivateIp] objects based on one of these filters:

  - Subnet OCID.   - VNIC OCID.   - Both private IP address and subnet OCID: This lets   you get a `privateIP` object based on its private IP   address (for example, 10.0.3.3) and not its OCID. For comparison,   [GetPrivateIp]   requires the OCID.

If you're listing all the private IPs associated with a given subnet or VNIC, the response includes both primary and secondary private IPs.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--ip-address', help="""The private IP address of the `privateIp` object.

Example: `10.0.3.3`""")
@click.option('--subnet-id', help="""The OCID of the subnet.""")
@click.option('--vnic-id', help="""The OCID of the VNIC.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_private_ips(ctx, limit, page, ip_address, subnet_id, vnic_id):
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
    result = client.list_private_ips(
        **kwargs
    )
    cli_util.render_response(result)


@route_table_group.command(name=cli_util.override('list_route_tables.command_name', 'list'), help="""Lists the route tables in the specified VCN and specified compartment. The response includes the default route table that automatically comes with each VCN, plus any route tables you've created.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_route_tables(ctx, compartment_id, vcn_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_route_tables(
        compartment_id=compartment_id,
        vcn_id=vcn_id,
        **kwargs
    )
    cli_util.render_response(result)


@security_list_group.command(name=cli_util.override('list_security_lists.command_name', 'list'), help="""Lists the security lists in the specified VCN and compartment.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_security_lists(ctx, compartment_id, vcn_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_security_lists(
        compartment_id=compartment_id,
        vcn_id=vcn_id,
        **kwargs
    )
    cli_util.render_response(result)


@subnet_group.command(name=cli_util.override('list_subnets.command_name', 'list'), help="""Lists the subnets in the specified VCN and the specified compartment.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_subnets(ctx, compartment_id, vcn_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_subnets(
        compartment_id=compartment_id,
        vcn_id=vcn_id,
        **kwargs
    )
    cli_util.render_response(result)


@vcn_group.command(name=cli_util.override('list_vcns.command_name', 'list'), help="""Lists the Virtual Cloud Networks (VCNs) in the specified compartment.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_vcns(ctx, compartment_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_vcns(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@virtual_circuit_bandwidth_shape_group.command(name=cli_util.override('list_virtual_circuit_bandwidth_shapes.command_name', 'list'), help="""Lists the available bandwidth levels for virtual circuits. You need this information so you can specify your desired bandwidth level (i.e., shape) when you create a virtual circuit.

For the compartment ID, provide the OCID of your tenancy (the root compartment).

For more information about virtual circuits, see [FastConnect Overview].""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_virtual_circuit_bandwidth_shapes(ctx, compartment_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_virtual_circuit_bandwidth_shapes(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@virtual_circuit_group.command(name=cli_util.override('list_virtual_circuits.command_name', 'list'), help="""Lists the virtual circuits in the specified compartment.""")
@click.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_virtual_circuits(ctx, compartment_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('virtual_network', ctx)
    result = client.list_virtual_circuits(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@cpe_group.command(name=cli_util.override('update_cpe.command_name', 'update'), help="""Updates the specified CPE's display name. Avoid entering confidential information.""")
@click.option('--cpe-id', required=True, help="""The OCID of the CPE.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_cpe(ctx, cpe_id, display_name, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_cpe(
        cpe_id=cpe_id,
        update_cpe_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@cross_connect_group.command(name=cli_util.override('update_cross_connect.command_name', 'update'), help="""Updates the specified cross-connect.""")
@click.option('--cross-connect-id', required=True, help="""The OCID of the cross-connect.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--is-active', help="""Set to true to activate the cross-connect. You activate it after the physical cabling is complete, and you've confirmed the cross-connect's light levels are good and your side of the interface is up. Activation indicates to Oracle that the physical connection is ready.

Example: `true`""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_cross_connect(ctx, cross_connect_id, display_name, is_active, if_match):
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
    cli_util.render_response(result)


@cross_connect_group_group.command(name=cli_util.override('update_cross_connect_group.command_name', 'update'), help="""Updates the specified cross-connect group's display name. Avoid entering confidential information.""")
@click.option('--cross-connect-group-id', required=True, help="""The OCID of the cross-connect group.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_cross_connect_group(ctx, cross_connect_group_id, display_name, if_match):
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
    cli_util.render_response(result)


@dhcp_options_group.command(name=cli_util.override('update_dhcp_options.command_name', 'update'), help="""Updates the specified set of DHCP options. You can update the display name or the options themselves. Avoid entering confidential information.

Note that the `options` object you provide replaces the entire existing set of options.""")
@click.option('--dhcp-id', required=True, help="""The OCID for the set of DHCP options.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--options', help="""""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_dhcp_options(ctx, force, dhcp_id, display_name, options, if_match):
    if not force:
        if options:
            if not click.confirm("WARNING: Updates to options will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if options is not None:
        details['options'] = cli_util.parse_json_parameter("options", options)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_dhcp_options(
        dhcp_id=dhcp_id,
        update_dhcp_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@drg_group.command(name=cli_util.override('update_drg.command_name', 'update'), help="""Updates the specified DRG's display name. Avoid entering confidential information.""")
@click.option('--drg-id', required=True, help="""The OCID of the DRG.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_drg(ctx, drg_id, display_name, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_drg(
        drg_id=drg_id,
        update_drg_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@drg_attachment_group.command(name=cli_util.override('update_drg_attachment.command_name', 'update'), help="""Updates the display name for the specified `DrgAttachment`. Avoid entering confidential information.""")
@click.option('--drg-attachment-id', required=True, help="""The OCID of the DRG attachment.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_drg_attachment(ctx, drg_attachment_id, display_name, if_match):
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
    cli_util.render_response(result)


@internet_gateway_group.command(name=cli_util.override('update_internet_gateway.command_name', 'update'), help="""Updates the specified Internet Gateway. You can disable/enable it, or change its display name. Avoid entering confidential information.

If the gateway is disabled, that means no traffic will flow to/from the internet even if there's a route rule that enables that traffic.""")
@click.option('--ig-id', required=True, help="""The OCID of the Internet Gateway.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--is-enabled', help="""Whether the gateway is enabled.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_internet_gateway(ctx, ig_id, display_name, is_enabled, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if is_enabled is not None:
        details['isEnabled'] = is_enabled

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_internet_gateway(
        ig_id=ig_id,
        update_internet_gateway_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@ip_sec_connection_group.command(name=cli_util.override('update_ip_sec_connection.command_name', 'update'), help="""Updates the display name for the specified IPSec connection. Avoid entering confidential information.""")
@click.option('--ipsc-id', required=True, help="""The OCID of the IPSec connection.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_ip_sec_connection(ctx, ipsc_id, display_name, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_ip_sec_connection(
        ipsc_id=ipsc_id,
        update_ip_sec_connection_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@private_ip_group.command(name=cli_util.override('update_private_ip.command_name', 'update'), help="""Updates the specified private IP. You must specify the object's OCID. Use this operation if you want to:

  - Move a secondary private IP to a different VNIC in the same subnet.   - Change the display name for a secondary private IP.   - Change the hostname for a secondary private IP.

This operation cannot be used with primary private IPs. To update the hostname for the primary IP on a VNIC, use [UpdateVnic].""")
@click.option('--private-ip-id', required=True, help="""The private IP's OCID.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--hostname-label', help="""The hostname for the private IP. Used for DNS. The value is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952] and [RFC 1123].

For more information, see [DNS in Your Virtual Cloud Network].

Example: `bminstance-1`""")
@click.option('--vnic-id', help="""The OCID of the VNIC to reassign the private IP to. The VNIC must be in the same subnet as the current VNIC.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_private_ip(ctx, private_ip_id, display_name, hostname_label, vnic_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

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
    cli_util.render_response(result)


@route_table_group.command(name=cli_util.override('update_route_table.command_name', 'update'), help="""Updates the specified route table's display name or route rules. Avoid entering confidential information.

Note that the `routeRules` object you provide replaces the entire existing set of rules.""")
@click.option('--rt-id', required=True, help="""The OCID of the route table.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--route-rules', help="""The collection of rules used for routing destination IPs to network devices.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_route_table(ctx, force, rt_id, display_name, route_rules, if_match):
    if not force:
        if route_rules:
            if not click.confirm("WARNING: Updates to route-rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if route_rules is not None:
        details['routeRules'] = cli_util.parse_json_parameter("route_rules", route_rules)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_route_table(
        rt_id=rt_id,
        update_route_table_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@security_list_group.command(name=cli_util.override('update_security_list.command_name', 'update'), help="""Updates the specified security list's display name or rules. Avoid entering confidential information.

Note that the `egressSecurityRules` or `ingressSecurityRules` objects you provide replace the entire existing objects.""")
@click.option('--security-list-id', required=True, help="""The OCID of the security list.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--egress-security-rules', help="""Rules for allowing egress IP packets.""")
@click.option('--ingress-security-rules', help="""Rules for allowing ingress IP packets.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_security_list(ctx, force, security_list_id, display_name, egress_security_rules, ingress_security_rules, if_match):
    if not force:
        if egress_security_rules or ingress_security_rules:
            if not click.confirm("WARNING: Updates to egress-security-rules and ingress-security-rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if egress_security_rules is not None:
        details['egressSecurityRules'] = cli_util.parse_json_parameter("egress_security_rules", egress_security_rules)

    if ingress_security_rules is not None:
        details['ingressSecurityRules'] = cli_util.parse_json_parameter("ingress_security_rules", ingress_security_rules)

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_security_list(
        security_list_id=security_list_id,
        update_security_list_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@subnet_group.command(name=cli_util.override('update_subnet.command_name', 'update'), help="""Updates the specified subnet's display name. Avoid entering confidential information.""")
@click.option('--subnet-id', required=True, help="""The OCID of the subnet.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_subnet(ctx, subnet_id, display_name, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_subnet(
        subnet_id=subnet_id,
        update_subnet_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@vcn_group.command(name=cli_util.override('update_vcn.command_name', 'update'), help="""Updates the specified VCN's display name. Avoid entering confidential information.""")
@click.option('--vcn-id', required=True, help="""The OCID of the VCN.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_vcn(ctx, vcn_id, display_name, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_vcn(
        vcn_id=vcn_id,
        update_vcn_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@virtual_circuit_group.command(name=cli_util.override('update_virtual_circuit.command_name', 'update'), help="""Updates the specified virtual circuit. This can be called by either the customer who owns the virtual circuit, or the provider (when provisioning or de-provisioning the virtual circuit from their end). The documentation for [UpdateVirtualCircuitDetails] indicates who can update each property of the virtual circuit.

**Important:** If the virtual circuit is working and in the PROVISIONED state, updating any of the network-related properties (such as the DRG being used, the BGP ASN, etc.) will cause the virtual circuit's state to switch to PROVISIONING and the related BGP session to go down. After Oracle re-provisions the virtual circuit, its state will return to PROVISIONED. Make sure you confirm that the associated BGP session is back up. For more information about the various states and how to test connectivity, see [FastConnect Overview].""")
@click.option('--virtual-circuit-id', required=True, help="""The OCID of the virtual circuit.""")
@click.option('--bandwidth-shape-name', help="""The provisioned data rate of the connection. To get a list of the available bandwidth levels (i.e., shapes), see [ListVirtualCircuitBandwidthShapes].

To be updated only by the customer who owns the virtual circuit.""")
@click.option('--cross-connect-mappings', help="""An array of mappings, each containing properties for a cross-connect or cross-connect group associated with this virtual circuit.

The customer and provider can update different properties in the mapping depending on the situation. See the description of the [CrossConnectMapping].""")
@click.option('--customer-bgp-asn', help="""The BGP ASN of the network at the other end of the BGP session from Oracle.

If the BGP session is from the customer's edge router to Oracle, the required value is the customer's ASN, and it can be updated only by the customer.

If the BGP session is from the provider's edge router to Oracle, the required value is the provider's ASN, and it can be updated only by the provider.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique. Avoid entering confidential information.

To be updated only by the customer who owns the virtual circuit.""")
@click.option('--gateway-id', help="""The OCID of the [Dynamic Routing Gateway (DRG)] that this virtual circuit uses.

To be updated only by the customer who owns the virtual circuit.""")
@click.option('--provider-state', help="""The provider's state in relation to this virtual circuit. Relevant only if the customer is using FastConnect via a provider.  ACTIVE means the provider has provisioned the virtual circuit from their end. INACTIVE means the provider has not yet provisioned the virtual circuit, or has de-provisioned it.

To be updated only by the provider.""")
@click.option('--reference-comment', help="""Provider-supplied reference information about this virtual circuit. Relevant only if the customer is using FastConnect via a provider.

To be updated only by the provider.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_virtual_circuit(ctx, force, virtual_circuit_id, bandwidth_shape_name, cross_connect_mappings, customer_bgp_asn, display_name, gateway_id, provider_state, reference_comment, if_match):
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
    cli_util.render_response(result)


@vnic_group.command(name=cli_util.override('update_vnic.command_name', 'update'), help="""Updates the specified VNIC.""")
@click.option('--vnic-id', required=True, help="""The OCID of the VNIC.""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable.""")
@click.option('--hostname-label', help="""The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952] and [RFC 1123]. The value appears in the [Vnic] object and also the [PrivateIp] object returned by [ListPrivateIps] and [GetPrivateIp].

For more information, see [DNS in Your Virtual Cloud Network].""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_vnic(ctx, vnic_id, display_name, hostname_label, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if hostname_label is not None:
        details['hostnameLabel'] = hostname_label

    client = cli_util.build_client('virtual_network', ctx)
    result = client.update_vnic(
        vnic_id=vnic_id,
        update_vnic_details=details,
        **kwargs
    )
    cli_util.render_response(result)
