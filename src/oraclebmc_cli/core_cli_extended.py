# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
from base64 import b64encode
import click
import json
import sys
from .generated import blockstorage_cli
from .generated import compute_cli
from .generated import virtualnetwork_cli
from oraclebmc.exceptions import ServiceError
from . import cli_util

blockstorage_cli.blockstorage_group.add_command(blockstorage_cli.volume_group)
blockstorage_cli.blockstorage_group.add_command(blockstorage_cli.volume_backup_group)

compute_cli.compute_group.add_command(compute_cli.image_group)
compute_cli.compute_group.add_command(compute_cli.instance_group)
compute_cli.compute_group.add_command(compute_cli.shape_group)
compute_cli.compute_group.add_command(compute_cli.vnic_attachment_group)
compute_cli.compute_group.add_command(compute_cli.volume_attachment_group)
compute_cli.compute_group.add_command(compute_cli.console_history_group)
compute_cli.instance_group.add_command(compute_cli.get_windows_instance_initial_credentials)
compute_cli.volume_attachment_group.add_command(compute_cli.detach_volume)

virtualnetwork_cli.virtual_network_group.add_command(virtualnetwork_cli.vcn_group)
virtualnetwork_cli.virtual_network_group.add_command(virtualnetwork_cli.subnet_group)
virtualnetwork_cli.virtual_network_group.add_command(virtualnetwork_cli.drg_attachment_group)
virtualnetwork_cli.virtual_network_group.add_command(virtualnetwork_cli.vnic_group)
virtualnetwork_cli.virtual_network_group.add_command(virtualnetwork_cli.dhcp_options_group)
virtualnetwork_cli.virtual_network_group.add_command(virtualnetwork_cli.internet_gateway_group)
virtualnetwork_cli.virtual_network_group.add_command(virtualnetwork_cli.ip_sec_connection_group)
virtualnetwork_cli.virtual_network_group.add_command(virtualnetwork_cli.drg_group)
virtualnetwork_cli.virtual_network_group.add_command(virtualnetwork_cli.route_table_group)
virtualnetwork_cli.virtual_network_group.add_command(virtualnetwork_cli.cpe_group)
virtualnetwork_cli.virtual_network_group.add_command(virtualnetwork_cli.security_list_group)

virtualnetwork_cli.get_ip_sec_connection_device_config.name = 'get-config'
virtualnetwork_cli.get_ip_sec_connection_device_status.name = 'get-status'
virtualnetwork_cli.ip_sec_connection_group.add_command(virtualnetwork_cli.get_ip_sec_connection_device_config)
virtualnetwork_cli.ip_sec_connection_group.add_command(virtualnetwork_cli.get_ip_sec_connection_device_status)

# help for bmcs compute instance launch --metadata
compute_instance_launch_metadata_example = """'{"ssh_authorized_keys": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDbVpuGODmhsRZOLWNgm0aEYUoWIDSPNWHmg2M6mZpmZNHfiNfx2dSofxUpKOiu5S8Th52AuAHSmkzNe6lXBO9wxnjOvkowe1mAleRTEl8zPI8Jkz6HrmJCzHEtS04kC4bx+tXRZhIfRq1uGaPcriKyquTnQs52Ahoxgw5vdXXQMwxWZLAcyaP01JrZwcUqPlB/GRiBFSTj0E/AIiVW3APNME5HjreOd/djjPRpvWu7AUpOqskG38kr8lhxo1hJifqeMg5W7cQsecTLJHgTDAPJD68ujM93jdzV2llIXwR1zyl80i6c3lDLyLgUrCLM0R1xex/zITTdT6/Z84buS/Xl my public key"}'"""
compute_instance_launch_metadata_help = """Custom metadata key/value pairs that you provide, such as the SSH public key required to connect to the instance. For more info see documentation: https://docs.us-phoenix-1.oraclecloud.com/api/#/en/iaas/20160918/requests/LaunchInstanceDetails. This must be provided in JSON format.

Note: user_data and ssh_authorized_keys can instead be specified using the parameters --user-data-file and --ssh-authorized-keys-file."""

compute_instance_launch_subnet_id_help = """The OCID of the subnet where the VNIC attached to this instance will be created."""
compute_instance_launch_hostname_label_help = """The hostname for the VNIC that is created during instance launch. Used for DNS. The value is the hostname portion of the instance's fully qualified domain name (FQDN) (e.g., `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952] and [RFC 1123]. The value cannot be changed, and it can be retrieved from the [Vnic object].

For more information, see [DNS in Your Virtual Cloud Network]."""
cli_util.update_param_help(compute_cli.launch_instance, 'metadata', compute_instance_launch_metadata_help, append=False, example=compute_instance_launch_metadata_example)
cli_util.update_param_help(compute_cli.launch_instance, 'subnet_id', compute_instance_launch_subnet_id_help)
cli_util.update_param_help(compute_cli.launch_instance, 'hostname_label', compute_instance_launch_hostname_label_help, example='`bminstance-1`')

# help for bmcs network ip-sec-connection create --static-routes
network_create_ip_sec_connection_static_routes_example = """'["10.0.0.0/16"]'"""
network_create_ip_sec_connection_static_routes_help = """Static routes to the CPE. At least one route must be included. The CIDR must not be a multicast address or class E address. This must be provided in JSON format."""
cli_util.update_param_help(virtualnetwork_cli.create_ip_sec_connection, 'static_routes', network_create_ip_sec_connection_static_routes_help, append=False, example=network_create_ip_sec_connection_static_routes_example)

network_create_subnet_prohibit_public_ip_on_vnic_help = """Whether VNICs within this subnet can have public IP addresses. Defaults to false, which means VNICs created in this subnet will automatically be assigned public IP addresses unless specified otherwise during instance launch (with the `--assign-public-ip` flag). If `--prohibit-public-ip-on-vnic` is set to true, VNICs created in this subnet cannot have public IP addresses (i.e., it's a private subnet)."""
network_create_subnet_prohibit_public_ip_on_vnic_example = "`true`"
cli_util.update_param_help(virtualnetwork_cli.create_subnet, 'prohibit_public_ip_on_vnic', network_create_subnet_prohibit_public_ip_on_vnic_help, example=network_create_subnet_prohibit_public_ip_on_vnic_example)

# help for bmcs network subnet create --security-list-ids
security_list_example_id = 'ocid1.securitylist.oc1.phx.aaaaaaaadyndu2n3hcmdsjfiljwyq7vpxsvv7ynp4ori7aealcvhzicnzhyq'
network_create_subnet_security_list_ids_example = """'["{sl_id}"]'"""
network_create_subnet_security_list_ids_help = cli_util.GENERIC_JSON_FORMAT_HELP
cli_util.update_param_help(virtualnetwork_cli.create_subnet, 'security_list_ids', network_create_subnet_security_list_ids_help,
                           append=True, example=network_create_subnet_security_list_ids_example.format(sl_id=security_list_example_id))

# help for bmcs network dhcp-options create --options
network_create_dhcp_options_options_example = """'[{"type": "DomainNameServer", "customDnsServers": ["202.44.61.9"], "serverType": "CustomDnsServer"}]'"""
network_create_dhcp_options_options_help = cli_util.GENERIC_JSON_FORMAT_HELP
cli_util.update_param_help(virtualnetwork_cli.create_dhcp_options, 'options', network_create_dhcp_options_options_help, append=True, example=network_create_dhcp_options_options_example)
cli_util.update_param_help(virtualnetwork_cli.update_dhcp_options, 'options', network_create_dhcp_options_options_help, append=True, example=network_create_dhcp_options_options_example)

# help for bmcs network route-table create --route-rules
internet_gateway_example_id = 'ocid1.internetgateway.oc1.phx.aaaaaaaaxtfqb2srw7hoi5cmdum4n6ow2xm2zhrzqqypmlteiiebtmvl75ya'
network_create_route_table_route_rules_example = """'[{{"cidrBlock":"0.0.0.0/0","networkEntityId":"{ig_id}"}}]'"""
network_create_route_table_route_rules_help = cli_util.GENERIC_JSON_FORMAT_HELP
cli_util.update_param_help(virtualnetwork_cli.create_route_table, 'route_rules', network_create_route_table_route_rules_help,
                           append=True, example=network_create_route_table_route_rules_example.format(ig_id=internet_gateway_example_id))
cli_util.update_param_help(virtualnetwork_cli.update_route_table, 'route_rules', network_create_route_table_route_rules_help,
                           append=True, example=network_create_route_table_route_rules_example.format(ig_id=internet_gateway_example_id))

# help for bmcs network security-list create --egress-security-rules
network_create_security_list_egress_security_rules_example = """'[{"destination": "10.0.2.0/24", "protocol": "6", "isStateless": true, "tcpOptions": {"destinationPortRange": {"max": 1521, "min": 1521}, "sourcePortRange": {"max": 1521, "min": 1521}}}]'"""
network_create_security_list_egress_security_rules_help = cli_util.GENERIC_JSON_FORMAT_HELP
cli_util.update_param_help(virtualnetwork_cli.create_security_list, 'egress_security_rules', network_create_security_list_egress_security_rules_help, append=True, example=network_create_security_list_egress_security_rules_example)
cli_util.update_param_help(virtualnetwork_cli.update_security_list, 'egress_security_rules', network_create_security_list_egress_security_rules_help, append=True, example=network_create_security_list_egress_security_rules_example)

# help for bmcs network security-list create --ingress-security-rules
network_create_security_list_ingress_security_rules_example = """'[{"source": "10.0.2.0/24", "protocol": "6", "isStateless": true, "tcpOptions": {"destinationPortRange": {"max": 1521, "min": 1521}, "sourcePortRange": {"max": 1521, "min": 1521}}}]'"""
network_create_security_list_ingress_security_rules_help = cli_util.GENERIC_JSON_FORMAT_HELP
cli_util.update_param_help(virtualnetwork_cli.create_security_list, 'ingress_security_rules', network_create_security_list_ingress_security_rules_help, append=True, example=network_create_security_list_ingress_security_rules_example)
cli_util.update_param_help(virtualnetwork_cli.update_security_list, 'ingress_security_rules', network_create_security_list_ingress_security_rules_help, append=True, example=network_create_security_list_ingress_security_rules_example)


@compute_cli.instance_group.command(name='list-vnics', help="""Lists the VNICs that are attached to the specified instance. VNICs that are in the process of attaching or detaching will not be returned.""")
@click.option('--instance-id', required=True, help="""The OCID of the instance.""")
@click.option('--limit', help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_vnics(ctx, instance_id, limit, page):
    client = cli_util.build_client('compute', ctx)
    compartment_id = client.get_instance(instance_id=instance_id).data.compartment_id

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page

    vnic_attachments_result = client.list_vnic_attachments(
        compartment_id=compartment_id,
        instance_id=instance_id,
        **kwargs
    )

    networking_client = cli_util.build_client('virtual_network', ctx)
    result = []

    for vnic_attachment in vnic_attachments_result.data:
        if vnic_attachment.lifecycle_state == 'ATTACHED':
            try:
                vnic = networking_client.get_vnic(vnic_attachment.vnic_id).data
                result.append(vnic)
            except ServiceError as service_error:
                if service_error.status == 404:
                    click.echo('Either VNIC with ID {} does not exist or you are not authorized to access it.'.format(vnic_attachment.vnic_id), file=sys.stderr)
                else:
                    raise

    cli_util.render(result, vnic_attachments_result.headers)


@cli_util.copy_params_from_generated_command(compute_cli.launch_instance, params_to_exclude=['create_vnic_details'])
@compute_cli.instance_group.command(name='launch', help=compute_cli.launch_instance.help)
@click.option('--vnic-display-name', required=False, help="""A user-friendly name for the default VNIC attached to this instance. Does not have to be unique.""")
@click.option('--assign-public-ip', required=False, type=click.BOOL, help="""Whether the default VNIC attached to this instance should be assigned a public IP address. Defaults to whether the subnet is public or private. If not set and the VNIC is being created in a private subnet (i.e., where prohibitPublicIpOnVnic=true in the Subnet), then no public IP address is assigned. If not set and the subnet is public (prohibitPublicIpOnVnic=false), then a public IP address is assigned. If set to true and prohibitPublicIpOnVnic=true, an error is returned.""")
@click.option('--private-ip', required=False, help="""A private IP address of your choice to assign to the default VNIC attached to this instance. Must be an available IP address within the subnet's CIDR. If no value is specified, a private IP address from the subnet will be automatically assigned.""")
@click.option('--user-data-file', required=False, type=click.File('rb'), help="""A file containing data that Cloud-Init can use to run custom scripts or provide custom Cloud-Init configuration. This parameter is a convenience wrapper around the 'user_data' field of the --metadata parameter.  Populating both values in the same call will result in an error. For more info see Cloud-Init documentation: https://cloudinit.readthedocs.org/en/latest/topics/format.html.""")
@click.option('--ssh-authorized-keys-file', required=False, type=click.File('r'), help="""A file containing one or more public SSH keys to be included in the ~/.ssh/authorized_keys file for the default user on the instance. Use a newline character to separate multiple keys. The SSH keys must be in the format necessary for the authorized_keys file. This parameter is a convenience wrapper around the 'ssh_authorized_keys' field of the --metadata parameter. Populating both values in the same call will result in an error. For more info see documentation: https://docs.us-phoenix-1.oraclecloud.com/api/#/en/iaas/20160918/requests/LaunchInstanceDetails.""")
@click.pass_context
def launch_instance_extended(ctx, **kwargs):
    metadata = {}
    if kwargs['metadata']:
        metadata = cli_util.parse_json_parameter("metadata", kwargs['metadata'])

    user_data_file = kwargs['user_data_file']
    if user_data_file:
        if 'user_data' in metadata:
            raise click.UsageError('Cannot specify CloudInit user-data as part of both --user-data-file and --metadata.')
        else:
            content = b64encode(user_data_file.read()).decode('utf-8')
            metadata['user_data'] = content

    ssh_authorized_keys_file = kwargs['ssh_authorized_keys_file']
    if ssh_authorized_keys_file:
        if 'ssh_authorized_keys' in metadata:
            raise click.UsageError(
                'Cannot specify ssh-authorized-keys as part of both --ssh-authorized-keys-file and --metadata.')
        else:
            metadata['ssh_authorized_keys'] = ssh_authorized_keys_file.read()

    kwargs['metadata'] = json.dumps(metadata)

    create_vnic_details = {}
    if 'assign_public_ip' in kwargs and kwargs['assign_public_ip'] is not None:
        create_vnic_details['assignPublicIp'] = kwargs['assign_public_ip']

    if kwargs['hostname_label']:
        create_vnic_details['hostnameLabel'] = kwargs['hostname_label']

    if kwargs['private_ip']:
        create_vnic_details['privateIp'] = kwargs['private_ip']

    if kwargs['subnet_id']:
        create_vnic_details['subnetId'] = kwargs['subnet_id']

    if kwargs['vnic_display_name']:
        create_vnic_details['displayName'] = kwargs['vnic_display_name']

    if len(create_vnic_details) > 0:
        kwargs['create_vnic_details'] = json.dumps(create_vnic_details)

    # delete additional kwargs because launch_instance will not recognize them
    del kwargs['assign_public_ip']
    del kwargs['hostname_label']
    del kwargs['private_ip']
    del kwargs['ssh_authorized_keys_file']
    del kwargs['subnet_id']
    del kwargs['user_data_file']
    del kwargs['vnic_display_name']

    ctx.invoke(compute_cli.launch_instance, **kwargs)
