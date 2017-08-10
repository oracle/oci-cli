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

from oraclebmc import wait_until
from oraclebmc.exceptions import ServiceError
from oraclebmc.exceptions import MaximumWaitTimeExceeded
from . import cli_util

blockstorage_cli.blockstorage_group.add_command(blockstorage_cli.volume_group)
blockstorage_cli.blockstorage_group.add_command(blockstorage_cli.volume_backup_group)

compute_cli.compute_group.add_command(compute_cli.image_group)
compute_cli.image_group.commands.pop(compute_cli.export_image.name)

compute_cli.compute_group.add_command(compute_cli.instance_group)
compute_cli.compute_group.add_command(compute_cli.shape_group)
compute_cli.compute_group.add_command(compute_cli.vnic_attachment_group)
compute_cli.compute_group.add_command(compute_cli.volume_attachment_group)
compute_cli.compute_group.add_command(compute_cli.console_history_group)
compute_cli.instance_group.add_command(compute_cli.get_windows_instance_initial_credentials)
compute_cli.volume_attachment_group.add_command(compute_cli.detach_volume)
compute_cli.vnic_attachment_group.commands.pop(compute_cli.attach_vnic.name)
compute_cli.vnic_attachment_group.commands.pop(compute_cli.detach_vnic.name)

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
virtualnetwork_cli.virtual_network_group.add_command(virtualnetwork_cli.private_ip_group)
virtualnetwork_cli.private_ip_group.commands.pop(virtualnetwork_cli.create_private_ip.name)
virtualnetwork_cli.private_ip_group.commands.pop(virtualnetwork_cli.update_private_ip.name)

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


image_source_details_example = """'{ "objectName": "image-to-import.qcow2", "bucketName": "MyBucket", "namespaceName": "MyNamespace", "sourceType": "objectStorageTuple" }'

or

'{ "sourceUri": "https://objectstorage.us-phoenix-1.oraclecloud.com/n/MyNamespace/b/MyBucket/o/image-to-import.qcow2", "sourceType": "objectStorageUri" }'"""
cli_util.update_param_help(compute_cli.create_image, 'image_source_details', "", append=True, example=image_source_details_example)

destination_type_example = """'{ "objectName": "image-to-import.qcow2", "bucketName": "MyBucket", "namespaceName": "MyNamespace", "destinationType": "objectStorageTuple" }'

or

'{ "destinationUri": "https://objectstorage.us-phoenix-1.oraclecloud.com/n/MyNamespace/b/MyBucket/o/exported-image.qcow2", "destinationType": "objectStorageUri" }'"""
cli_util.update_param_help(compute_cli.export_image, 'destination_type', "", append=True, example=destination_type_example)

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

# Formatting of the help for the bcms network private-ip list command
virtualnetwork_cli.list_private_ips.help = """Lists the [PrivateIp] objects based on one of these filters:

  \b
  - Subnet OCID.
  - VNIC OCID.
  - Both private IP address and subnet OCID: This lets you get a `privateIP` object
    based on its private IP address (for example, 10.0.3.3)  and not its OCID.
    For comparison, [GetPrivateIp] requires the OCID.

If you're listing all the private IPs associated with a given subnet or VNIC, the response includes both primary and secondary private IPs."""

cli_util.update_param_help(compute_cli.create_image, 'image_source_details', """[DEPRECATED] The use of the `bmcs compute image create` command to import an image from Object Storage is deprecated.

\b
Please use the `bmcs compute image import` command instead.

""" + cli_util.get_param(compute_cli.create_image, 'image_source_details').help, append=False)


@compute_cli.image_group.group(cli_util.override('export_image_group.command_name', 'export'), help="""Exports an image to the Oracle Bare Metal Cloud Object Storage Service. You can use the
Object Storage Service URL, or the namespace, bucket name, and object name when specifying the location to export to.

For more information about exporting images, see [Image Import/Export].

To perform an image export, you need write access to the Object Storage Service bucket for the image, see [Let Users Write Objects to Object Storage Buckets].

See [Object Storage URLs] and [pre-authenticated requests] for constructing URLs for image import/export.
""")
@cli_util.help_option_group
def export_image_group():
    pass


@compute_cli.image_group.group(cli_util.override('import_image_group.command_name', 'import'), help="""Imports an exported image from the Oracle Bare Metal Cloud Object Storage Service. You can use the
Object Storage Service URL, or the namespace, bucket name, and object name when specifying the location to import from.

For more information about importing exported images, see [Image Import/Export].

See [Object Storage URLs] and [pre-authenticated requests] for constructing URLs for image import/export.

You may optionally specify a display name for the image, which is simply a friendly name or description. It does not have to be unique, and you can change it. See [UpdateImage]. Avoid entering
confidential information.
""")
@cli_util.help_option_group
def import_image_group():
    pass


@cli_util.copy_params_from_generated_command(compute_cli.export_image, params_to_exclude=['destination_type'])
@export_image_group.command(name='to-object', help="""Exports the specified image to the Oracle Bare Metal Cloud Object Storage Service using the namespace, bucket name, and object name to identify the location to export to.

For more information about exporting images, see [Image Import/Export].

To perform an image export, you need write access to the Object Storage Service bucket for the image, see [Let Users Write Objects to Object Storage Buckets].
""")
@click.option('-ns', '--namespace', required=True, help='The Object Storage Service namespace to export the image to.')
@click.option('-bn', '--bucket-name', required=True, help='The name of the bucket to export the image to.')
@click.option('--name', required=True, help='The name which will be given to the exported image object.')
@click.pass_context
def export_image_to_object(ctx, image_id, if_match, namespace, bucket_name, name):
    export_image_details = {}
    export_image_details['destinationType'] = 'objectStorageTuple'
    export_image_details['namespaceName'] = namespace
    export_image_details['bucketName'] = bucket_name
    export_image_details['objectName'] = name

    export_image_internal(ctx, image_id, export_image_details, if_match)


@cli_util.copy_params_from_generated_command(compute_cli.export_image, params_to_exclude=['destination_type'])
@export_image_group.command(name='to-object-uri', help="""Exports the specified image to the Oracle Bare Metal Cloud Object Storage Service using the Object Storage Service URL to identify the location to export to.

For more information about exporting images, see [Image Import/Export].

See [Object Storage URLs] and [pre-authenticated requests] for constructing URLs for image import/export.
""")
@click.option('--uri', required=True, help='The Object Storage URL to export the image to.')
@click.pass_context
def export_image_to_uri(ctx, image_id, if_match, uri):
    export_image_details = {}
    export_image_details['destinationType'] = 'objectStorageUri'
    export_image_details['destinationUri'] = uri

    export_image_internal(ctx, image_id, export_image_details, if_match)


def export_image_internal(ctx, image_id, export_image_details, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    client = cli_util.build_client('compute', ctx)
    result = client.export_image(
        image_id=image_id,
        export_image_details=export_image_details,
        **kwargs
    )

    cli_util.render_response(result)


@cli_util.copy_params_from_generated_command(compute_cli.create_image, params_to_exclude=['image_source_details', 'instance_id'])
@import_image_group.command(name='from-object', help="""Imports an exported image from the Oracle Bare Metal Cloud Object Storage Service using the namespace, bucket name, and object name to identify the location to import from.

For more information about importing exported images, see [Image Import/Export].

You may optionally specify a display name for the image, which is simply a friendly name or description. It does not have to be unique, and you can change it. See [UpdateImage].
Avoid entering confidential information.
""")
@click.option('-ns', '--namespace', required=True, help='The Object Storage Service namespace to import the image from.')
@click.option('-bn', '--bucket-name', required=True, help='The name of the bucket to import the image from.')
@click.option('--name', required=True, help='The name of the object identifying the image to import.')
@click.pass_context
def import_image_from_object(ctx, compartment_id, display_name, namespace, bucket_name, name):
    import_image_details = {}
    import_image_details['sourceType'] = 'objectStorageTuple'
    import_image_details['namespaceName'] = namespace
    import_image_details['bucketName'] = bucket_name
    import_image_details['objectName'] = name

    import_image_internal(ctx, compartment_id, display_name, import_image_details)


@cli_util.copy_params_from_generated_command(compute_cli.create_image, params_to_exclude=['image_source_details', 'instance_id'])
@import_image_group.command(name='from-object-uri', help="""Imports an exported image from the Oracle Bare Metal Cloud Object Storage Service using the Object Storage Service URL to identify the location to import from.

For more information about importing exported images, see [Image Import/Export].

See [Object Storage URLs] and [pre-authenticated requests] for constructing URLs for image import/export.

You may optionally specify a display name for the image, which is simply a friendly name or description. It does not have to be unique, and you can change it. See [UpdateImage].
Avoid entering confidential information.
""")
@click.option('--uri', required=True, help='The Object Storage URL to import the image from.')
@click.pass_context
def import_image_from_uri(ctx, compartment_id, display_name, uri):
    import_image_details = {}
    import_image_details['sourceType'] = 'objectStorageUri'
    import_image_details['sourceUri'] = uri

    import_image_internal(ctx, compartment_id, display_name, import_image_details)


def import_image_internal(ctx, compartment_id, display_name, import_image_details):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['imageSourceDetails'] = import_image_details

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('compute', ctx)
    result = client.create_image(
        create_image_details=details,
        **kwargs
    )

    cli_util.render_response(result)


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


@compute_cli.instance_group.command(name='attach-vnic', help="""Creates a secondary VNIC and attaches it to the specified instance. For more information about secondary VNICs, see [Managing Virtual Network Interface Cards (VNICs)].""")
@click.option('--instance-id', required=True, help="""The OCID of the instance.""")
@click.option('--subnet-id', required=True, help="""The OCID of the subnet to create the VNIC in.""")
@click.option('--vnic-display-name', required=False, help="""A user-friendly name for the VNIC. Does not have to be unique.""")
@click.option('--assign-public-ip', required=False, type=click.BOOL, help="""Whether the VNIC should be assigned a public IP address. Defaults to whether the subnet is public or private. If not set and the VNIC is being created in a private subnet (i.e., where prohibitPublicIpOnVnic=true in the Subnet), then no public IP address is assigned. If not set and the subnet is public (prohibitPublicIpOnVnic=false), then a public IP address is assigned. If set to true and prohibitPublicIpOnVnic=true, an error is returned.""")
@click.option('--private-ip', required=False, help="""A private IP address of your choice to assign to the VNIC. Must be an available IP address within the subnet's CIDR. If no value is specified, a private IP address from the subnet will be automatically assigned.""")
@click.option('--hostname-label', help="""The hostname for the VNIC. Used for DNS. The value is the hostname portion of the VNIC's fully qualified domain name (FQDN) (e.g., `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952](https://tools.ietf.org/html/rfc952) and [RFC 1123](https://tools.ietf.org/html/rfc1123). The value can be retrieved from the [Vnic](#/en/iaas/20160918/Vnic/).""")
@click.option('--wait', is_flag=True, default=False, help="""If set, then wait for the attachment to complete and return the newly attached VNIC. If not set, then the command will not wait and will return nothing on success.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def attach_vnic(ctx, instance_id, subnet_id, vnic_display_name, assign_public_ip, private_ip, hostname_label, wait):
    kwargs = {}

    vnic_details = {}
    vnic_details['subnetId'] = subnet_id
    vnic_details['displayName'] = vnic_display_name
    vnic_details['assignPublicIp'] = assign_public_ip
    vnic_details['privateIp'] = private_ip
    vnic_details['hostnameLabel'] = hostname_label

    attachment_details = {}
    attachment_details['createVnicDetails'] = vnic_details
    attachment_details['instanceId'] = instance_id

    compute_client = cli_util.build_client('compute', ctx)
    response = compute_client.attach_vnic(
        attach_vnic_details=attachment_details,
        **kwargs
    )

    if not wait:
        return

    response = compute_client.get_vnic_attachment(response.data.id)

    try:
        response = wait_until(compute_client, response, 'lifecycle_state', 'ATTACHED', max_wait_seconds=180)
    except MaximumWaitTimeExceeded:
        sys.exit('Timed out while waiting for the VNIC attachment to reach the ATTACHED state.')

    if not response.data.vnic_id:
        sys.exit('The VNIC ID is not set on the VNIC attachment.')

    network_client = cli_util.build_client('virtual_network', ctx)
    response = network_client.get_vnic(vnic_id=response.data.vnic_id)
    cli_util.render_response(response)


@compute_cli.instance_group.command(name='detach-vnic', help="""Detaches and deletes the specified secondary VNIC. This operation cannot be used on the instance's primary VNIC. When you terminate an instance, all attached VNICs (primary and secondary) are automatically detached and deleted.""")
@click.option('--vnic-id', required=True, help="""The OCID of the VNIC.""")
@click.option('--compartment-id', required=True, help="""The OCID of the instance's compartment.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def detach_vnic(ctx, vnic_id, compartment_id):
    compute_client = cli_util.build_client('compute', ctx)
    result = compute_client.list_vnic_attachments(compartment_id=compartment_id, vnic_id=vnic_id)

    if result.data is None or len(result.data) == 0:
        sys.exit('A VNIC attachment could not be found for the given VNIC ID.')

    vnic_attachment_id = result.data[0].id
    result = compute_client.detach_vnic(vnic_attachment_id=vnic_attachment_id)

    cli_util.render_response(result)


@cli_util.copy_params_from_generated_command(virtualnetwork_cli.create_private_ip, params_to_exclude=[''])
@virtualnetwork_cli.vnic_group.command(name='assign-private-ip', help="""Assigns a secondary private IP address to the specified VNIC. The secondary private IP must be in the same subnet as the VNIC.
This command can also be used to move an existing secondary private IP to the specified VNIC.

For more information about secondary private IPs, see [Managing IP Addresses]
""")
@click.option('--unassign-if-already-assigned', is_flag=True, default=False, help="""Force reassignment of the IP address if it's already assigned to another VNIC in the subnet. This is only relevant if an IP address is associated with this command.""")
@click.pass_context
@cli_util.wrap_exceptions
def assign_private_ip(ctx, vnic_id, ip_address, display_name, hostname_label, unassign_if_already_assigned):
    networking_client = cli_util.build_client('virtual_network', ctx)

    # First we get the VNIC because we need to know the subnet OCID for the ListPrivateIps call
    vnic = networking_client.get_vnic(vnic_id).data
    subnet_id = vnic.subnet_id

    is_ip_reassignment = False
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

    assign_private_ip_request_body = {}
    assign_private_ip_request_body['vnicId'] = vnic_id

    # These are optional in the request, so check whether we should set them or not.
    if display_name is not None:
        assign_private_ip_request_body['displayName'] = display_name
    if hostname_label is not None:
        assign_private_ip_request_body['hostnameLabel'] = hostname_label

    # If we are here then either the IP address does not exist or it is a candidate to be moved
    if not is_ip_reassignment:
        if ip_address is not None:
            assign_private_ip_request_body['ipAddress'] = ip_address

        result = networking_client.create_private_ip(assign_private_ip_request_body)
    else:
        result = networking_client.update_private_ip(list_private_ips_response_data[0].id, assign_private_ip_request_body)

    private_ip_id = result.data.id
    get_private_id_result = networking_client.get_private_ip(private_ip_id)

    cli_util.render_response(get_private_id_result)


@virtualnetwork_cli.vnic_group.command(name='unassign-private-ip', help="""Unassigns a secondary private IP address from a VNIC. After the IP address is unassigned, you
can assign to another VNIC in the subnet.

This operation cannot be used with primary private IPs, which are automatically unassigned, and then deleted when the VNIC is
terminated.

For more information about secondary private IPs, see [Managing IP Addresses]
""")
@click.option('--vnic-id', required=True, help="""The OCID of the VNIC to unassign the private IP from.""")
@click.option('--ip-address', required=True, help="""The secondary private IP to unassign from the VNIC.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def unassign_private_ip(ctx, vnic_id, ip_address):
    networking_client = cli_util.build_client('virtual_network', ctx)

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
@cli_util.wrap_exceptions
def update_private_ip_extended(ctx, **kwargs):
    ctx.invoke(virtualnetwork_cli.update_private_ip, **kwargs)
