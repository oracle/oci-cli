# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
from base64 import b64encode
import click
import json
import re
import six
import sys
from ..generated import blockstorage_cli
from ..generated import compute_cli
from ..generated import virtualnetwork_cli

from oci import wait_until
from oci.exceptions import ServiceError
from oci.exceptions import MaximumWaitTimeExceeded
from .. import cli_util
from .. import custom_types
from .. import json_skeleton_utils
from ..aliasing import CommandGroupWithAlias
from ..cli_util import option

INSTANCE_CONSOLE_CONNECTION_STRING_INTERMEDIATE_HOST_REGEX = "(instance-console\.[a-z0-9-]+\.(oraclecloud|oracleiaas)\.com)"
DEFAULT_LOCAL_VNC_PORT = 5900
DEFAULT_SSH_PROXY_PORT = 5905

blockstorage_cli.volume_group.commands.pop(blockstorage_cli.create_volume.name)
blockstorage_cli.boot_volume_group.commands.pop(blockstorage_cli.create_boot_volume.name)

compute_cli.compute_root_group.commands.pop(compute_cli.volume_group.name)
compute_cli.compute_root_group.commands.pop(compute_cli.instance_credentials_group.name)
compute_cli.compute_root_group.commands.pop(compute_cli.boot_volume_group.name)

# Disabling subclass commands
compute_cli.image_group.commands.pop(compute_cli.export_image_export_image_via_object_storage_uri_details.name)
compute_cli.image_group.commands.pop(compute_cli.export_image_export_image_via_object_storage_tuple_details.name)

compute_cli.image_group.commands.pop(compute_cli.export_image.name)

compute_cli.compute_root_group.add_command(compute_cli.instance_group)
compute_cli.compute_root_group.add_command(compute_cli.shape_group)
compute_cli.compute_root_group.add_command(compute_cli.vnic_attachment_group)
compute_cli.compute_root_group.add_command(compute_cli.boot_volume_attachment_group)
compute_cli.compute_root_group.add_command(compute_cli.volume_attachment_group)


# Disabling subclass commands
compute_cli.volume_attachment_group.commands.pop(compute_cli.attach_volume_attach_i_scsi_volume_details.name)
compute_cli.volume_attachment_group.commands.pop(compute_cli.attach_volume_attach_paravirtualized_volume_details.name)

compute_cli.compute_root_group.add_command(compute_cli.console_history_group)
compute_cli.compute_root_group.add_command(compute_cli.instance_console_connection_group)
compute_cli.instance_group.add_command(compute_cli.get_windows_instance_initial_credentials)
compute_cli.volume_attachment_group.add_command(compute_cli.detach_volume)
compute_cli.vnic_attachment_group.commands.pop(compute_cli.attach_vnic.name)
compute_cli.vnic_attachment_group.commands.pop(compute_cli.detach_vnic.name)
compute_cli.instance_console_connection_group.commands.pop(compute_cli.create_instance_console_connection.name)
compute_cli.boot_volume_attachment_group.add_command(compute_cli.detach_boot_volume)

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

# help for oci compute instance launch --metadata
compute_instance_launch_metadata_example = """'{"ssh_authorized_keys": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDbVpuGODmhsRZOLWNgm0aEYUoWIDSPNWHmg2M6mZpmZNHfiNfx2dSofxUpKOiu5S8Th52AuAHSmkzNe6lXBO9wxnjOvkowe1mAleRTEl8zPI8Jkz6HrmJCzHEtS04kC4bx+tXRZhIfRq1uGaPcriKyquTnQs52Ahoxgw5vdXXQMwxWZLAcyaP01JrZwcUqPlB/GRiBFSTj0E/AIiVW3APNME5HjreOd/djjPRpvWu7AUpOqskG38kr8lhxo1hJifqeMg5W7cQsecTLJHgTDAPJD68ujM93jdzV2llIXwR1zyl80i6c3lDLyLgUrCLM0R1xex/zITTdT6/Z84buS/Xl my public key"}'"""
compute_instance_launch_metadata_help = """Custom metadata key/value pairs that you provide, such as the SSH public key required to connect to the instance. For more info see documentation: https://docs.us-phoenix-1.oraclecloud.com/api/#/en/iaas/20160918/requests/LaunchInstanceDetails. This must be provided in JSON format.

Note: user_data and ssh_authorized_keys can instead be specified using the parameters --user-data-file and --ssh-authorized-keys-file."""

compute_instance_launch_subnet_id_help = """The OCID of the subnet where the VNIC attached to this instance will be created."""
compute_instance_launch_hostname_label_help = """The hostname for the VNIC that is created during instance launch. Used for DNS. The value is the hostname portion of the instance's fully qualified domain name (FQDN) (e.g., `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952] and [RFC 1123]. The value cannot be changed, and it can be retrieved from the [Vnic].

For more information, see [DNS in Your Virtual Cloud Network]."""
cli_util.update_param_help(compute_cli.launch_instance, 'metadata', compute_instance_launch_metadata_help, append=False, example=compute_instance_launch_metadata_example)
cli_util.update_param_help(compute_cli.launch_instance, 'subnet_id', compute_instance_launch_subnet_id_help)
cli_util.update_param_help(compute_cli.launch_instance, 'hostname_label', compute_instance_launch_hostname_label_help, example='`bminstance-1`')
cli_util.update_param_help(compute_cli.launch_instance, 'source_details', """Use this parameter to specify whether a boot volume or an image should be used to launch a new instance.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
cli_util.update_param_help(compute_cli.launch_instance, 'image_id', """The OCID of the image used to boot the instance. This is a shortcut for specifying an image source via the --source-details complex JSON parameter. If this parameter is provided, you cannot provide the --source-details or --source-boot-volume-id parameters.""", append=False)

image_source_details_example = """'{ "objectName": "image-to-import.qcow2", "bucketName": "MyBucket", "namespaceName": "MyNamespace", "sourceType": "objectStorageTuple" }'

or

'{ "sourceUri": "https://objectstorage.us-phoenix-1.oraclecloud.com/n/MyNamespace/b/MyBucket/o/image-to-import.qcow2", "sourceType": "objectStorageUri" }'"""
cli_util.update_param_help(compute_cli.create_image, 'image_source_details', "", append=True, example=image_source_details_example)

destination_type_example = """'{ "objectName": "image-to-import.qcow2", "bucketName": "MyBucket", "namespaceName": "MyNamespace", "destinationType": "objectStorageTuple" }'

or

'{ "destinationUri": "https://objectstorage.us-phoenix-1.oraclecloud.com/n/MyNamespace/b/MyBucket/o/exported-image.qcow2", "destinationType": "objectStorageUri" }'"""
cli_util.update_param_help(compute_cli.export_image, 'destination_type', "", append=True, example=destination_type_example)

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

cli_util.get_param(compute_cli.attach_volume, 'type').type = custom_types.CliCaseInsensitiveChoice(['iscsi', 'paravirtualized'])

# Formatting of the help for the bcms network private-ip list command
virtualnetwork_cli.list_private_ips.help = """Lists the [PrivateIp] objects based on one of these filters:

  \b
  - Subnet OCID.
  - VNIC OCID.
  - Both private IP address and subnet OCID: This lets you get a `privateIP` object
    based on its private IP address (for example, 10.0.3.3)  and not its OCID.
    For comparison, [GetPrivateIp] requires the OCID.

If you're listing all the private IPs associated with a given subnet or VNIC, the response includes both primary and secondary private IPs."""

cli_util.update_param_help(compute_cli.create_image, 'image_source_details', """[DEPRECATED] The use of the `oci compute image create` command to import an image from Object Storage is deprecated.

\b
Please use the `oci compute image import` command instead.

""" + cli_util.get_param(compute_cli.create_image, 'image_source_details').help, append=False)


# update the type of the --skip-source-dest-check switch on update_vnic to be a boolean
cli_util.get_param(virtualnetwork_cli.update_vnic, 'skip_source_dest_check').type = click.BOOL

# update help for instance console connections on windows
instance_console_connection_windows_help = """If you are attempting to start a VNC connection to an instance from a Windows machine without SSH installed, you can consider using plink instead.
The 'oci compute instance-console-connection get-plink-connection-string' command returns a PowerShell command which uses plink to launch the SSH tunnel necessary to start a VNC connection to the instance."""
compute_cli.instance_console_connection_group.help = compute_cli.instance_console_connection_group.help + '\n\n' + instance_console_connection_windows_help
compute_cli.get_instance_console_connection.help = compute_cli.get_instance_console_connection.help + '\n\n' + instance_console_connection_windows_help


@compute_cli.image_group.command(cli_util.override('export_image_group.command_name', 'export'), cls=CommandGroupWithAlias, help="""Exports an image to the Oracle Cloud Infrastructure Object Storage Service. You can use the
Object Storage Service URL, or the namespace, bucket name, and object name when specifying the location to export to.

For more information about exporting images, see [Image Import/Export].

To perform an image export, you need write access to the Object Storage Service bucket for the image, see [Let Users Write Objects to Object Storage Buckets].

See [Object Storage URLs] and [pre-authenticated requests] for constructing URLs for image import/export.
""")
@cli_util.help_option_group
def export_image_group():
    pass


@compute_cli.image_group.command(cli_util.override('import_image_group.command_name', 'import'), cls=CommandGroupWithAlias, help="""Imports an exported image from the Oracle Cloud Infrastructure Object Storage Service. You can use the
Object Storage Service URL, or the namespace, bucket name, and object name when specifying the location to import from.

For more information about importing exported images, see [Image Import/Export].

See [Object Storage URLs] and [pre-authenticated requests] for constructing URLs for image import/export.

You may optionally specify a display name for the image, which is simply a friendly name or description. It does not have to be unique, and you can change it. See [UpdateImage]. Avoid entering
confidential information.
""")
@cli_util.help_option_group
def import_image_group():
    pass


@cli_util.copy_params_from_generated_command(compute_cli.export_image, params_to_exclude=['destination_type', 'wait_for_state', 'max_wait_seconds', 'wait_interval_seconds'])
@export_image_group.command(name='to-object', help="""Exports the specified image to the Oracle Cloud Infrastructure Object Storage Service using the namespace, bucket name, and object name to identify the location to export to.

For more information about exporting images, see [Image Import/Export].

To perform an image export, you need write access to the Object Storage Service bucket for the image, see [Let Users Write Objects to Object Storage Buckets].
""")
@cli_util.option('-ns', '--namespace', required=True, help='The Object Storage Service namespace to export the image to.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket to export the image to.')
@cli_util.option('--name', required=True, help='The name which will be given to the exported image object.')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def export_image_to_object(ctx, from_json, image_id, if_match, namespace, bucket_name, name):
    export_image_details = {}
    export_image_details['destinationType'] = 'objectStorageTuple'
    export_image_details['namespaceName'] = namespace
    export_image_details['bucketName'] = bucket_name
    export_image_details['objectName'] = name

    export_image_internal(ctx, image_id, export_image_details, if_match)


@cli_util.copy_params_from_generated_command(compute_cli.export_image, params_to_exclude=['destination_type', 'wait_for_state', 'max_wait_seconds', 'wait_interval_seconds'])
@export_image_group.command(name='to-object-uri', help="""Exports the specified image to the Oracle Cloud Infrastructure Object Storage Service using the Object Storage Service URL to identify the location to export to.

For more information about exporting images, see [Image Import/Export].

See [Object Storage URLs] and [pre-authenticated requests] for constructing URLs for image import/export.
""")
@cli_util.option('--uri', required=True, help='The Object Storage URL to export the image to.')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def export_image_to_uri(ctx, from_json, image_id, if_match, uri):
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

    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(compute_cli.create_image, params_to_exclude=['image_source_details', 'instance_id', 'wait_for_state', 'max_wait_seconds', 'wait_interval_seconds'])
@import_image_group.command(name='from-object', help="""Imports an exported image from the Oracle Cloud Infrastructure Object Storage Service using the namespace, bucket name, and object name to identify the location to import from.

For more information about importing exported images, see [Image Import/Export].

You may optionally specify a display name for the image, which is simply a friendly name or description. It does not have to be unique, and you can change it. See [UpdateImage].
Avoid entering confidential information.
""")
@cli_util.option('-ns', '--namespace', required=True, help='The Object Storage Service namespace to import the image from.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket to import the image from.')
@cli_util.option('--name', required=True, help='The name of the object identifying the image to import.')
@cli_util.option('--source-image-type', type=custom_types.CliCaseInsensitiveChoice(["QCOW2", "VMDK"]), help='The format of the image to be imported. Exported Oracle images are QCOW2. Only monolithic images are supported.')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'image-source-details': {'module': 'core', 'class': 'ImageSourceDetails'}}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def import_image_from_object(ctx, from_json, compartment_id, display_name, namespace, bucket_name, name, source_image_type, launch_mode, defined_tags, freeform_tags):
    import_image_details = {}
    import_image_details['sourceType'] = 'objectStorageTuple'
    import_image_details['namespaceName'] = namespace
    import_image_details['bucketName'] = bucket_name
    import_image_details['objectName'] = name

    if source_image_type is not None:
        import_image_details['sourceImageType'] = source_image_type

    import_image_internal(ctx, compartment_id, display_name, launch_mode, import_image_details, defined_tags, freeform_tags)


@cli_util.copy_params_from_generated_command(compute_cli.create_image, params_to_exclude=['image_source_details', 'instance_id', 'wait_for_state', 'max_wait_seconds', 'wait_interval_seconds'])
@import_image_group.command(name='from-object-uri', help="""Imports an exported image from the Oracle Cloud Infrastructure Object Storage Service using the Object Storage Service URL to identify the location to import from.

For more information about importing exported images, see [Image Import/Export].

See [Object Storage URLs] and [pre-authenticated requests] for constructing URLs for image import/export.

You may optionally specify a display name for the image, which is simply a friendly name or description. It does not have to be unique, and you can change it. See [UpdateImage].
Avoid entering confidential information.
""")
@cli_util.option('--uri', required=True, help='The Object Storage URL to import the image from.')
@cli_util.option('--source-image-type', type=custom_types.CliCaseInsensitiveChoice(["QCOW2", "VMDK"]), help='The format of the image to be imported. Exported Oracle images are QCOW2. Only monolithic images are supported.')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'image-source-details': {'module': 'core', 'class': 'ImageSourceDetails'}}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def import_image_from_uri(ctx, from_json, compartment_id, display_name, uri, source_image_type, launch_mode, defined_tags, freeform_tags):
    import_image_details = {}
    import_image_details['sourceType'] = 'objectStorageUri'
    import_image_details['sourceUri'] = uri

    if source_image_type is not None:
        import_image_details['sourceImageType'] = source_image_type

    import_image_internal(ctx, compartment_id, display_name, launch_mode, import_image_details, defined_tags, freeform_tags)


def import_image_internal(ctx, compartment_id, display_name, launch_mode, import_image_details, defined_tags, freeform_tags):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['imageSourceDetails'] = import_image_details

    if display_name is not None:
        details['displayName'] = display_name

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)
    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)
    if launch_mode is not None:
        details['launchMode'] = launch_mode

    client = cli_util.build_client('compute', ctx)
    result = client.create_image(
        create_image_details=details,
        **kwargs
    )

    cli_util.render_response(result, ctx)


@compute_cli.instance_group.command(name='list-vnics', help="""Lists the VNICs that are attached to the specified instance. VNICs that are in the process of attaching or detaching will not be returned.""")
@cli_util.option('--instance-id', required=True, help="""The OCID of the instance.""")
@cli_util.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@cli_util.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Vnic]'})
@cli_util.wrap_exceptions
def list_vnics(ctx, from_json, instance_id, limit, page, all_pages, page_size):
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    client = cli_util.build_client('compute', ctx)
    compartment_id = client.get_instance(instance_id=instance_id).data.compartment_id

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page

    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        vnic_attachments_result = cli_util.list_call_get_all_results(
            client.list_vnic_attachments,
            compartment_id=compartment_id,
            instance_id=instance_id,
            **kwargs
        )
    elif limit is not None:
        vnic_attachments_result = cli_util.list_call_get_up_to_limit(
            client.list_vnic_attachments,
            limit,
            page_size,
            compartment_id=compartment_id,
            instance_id=instance_id,
            **kwargs
        )
    else:
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

    cli_util.render(result, vnic_attachments_result.headers, ctx=ctx)


@cli_util.copy_params_from_generated_command(compute_cli.launch_instance, params_to_exclude=['create_vnic_details'])
@compute_cli.instance_group.command(name='launch', help=compute_cli.launch_instance.help)
@cli_util.option('--vnic-display-name', help="""A user-friendly name for the default VNIC attached to this instance. Does not have to be unique.""")
@cli_util.option('--assign-public-ip', type=click.BOOL, help="""Whether the default VNIC attached to this instance should be assigned a public IP address. Defaults to whether the subnet is public or private. If not set and the VNIC is being created in a private subnet (i.e., where prohibitPublicIpOnVnic=true in the Subnet), then no public IP address is assigned. If not set and the subnet is public (prohibitPublicIpOnVnic=false), then a public IP address is assigned. If set to true and prohibitPublicIpOnVnic=true, an error is returned.""")
@cli_util.option('--private-ip', help="""A private IP address of your choice to assign to the default VNIC attached to this instance. Must be an available IP address within the subnet's CIDR. If no value is specified, a private IP address from the subnet will be automatically assigned.""")
@cli_util.option('--skip-source-dest-check', type=click.BOOL, help="""Indicates whether Source/Destination check is disabled on the VNIC. Defaults to `false`, in which case we enable Source/Destination check on the VNIC.""")
@cli_util.option('--user-data-file', type=click.File('rb'), help="""A file containing data that Cloud-Init can use to run custom scripts or provide custom Cloud-Init configuration. This parameter is a convenience wrapper around the 'user_data' field of the --metadata parameter.  Populating both values in the same call will result in an error. For more info see Cloud-Init documentation: https://cloudinit.readthedocs.org/en/latest/topics/format.html.""")
@cli_util.option('--ssh-authorized-keys-file', type=click.File('r'), help="""A file containing one or more public SSH keys to be included in the ~/.ssh/authorized_keys file for the default user on the instance. Use a newline character to separate multiple keys. The SSH keys must be in the format necessary for the authorized_keys file. This parameter is a convenience wrapper around the 'ssh_authorized_keys' field of the --metadata parameter. Populating both values in the same call will result in an error. For more info see documentation: https://docs.us-phoenix-1.oraclecloud.com/api/#/en/iaas/20160918/requests/LaunchInstanceDetails.""")
@cli_util.option('--source-boot-volume-id', help="""The OCID of the boot volume used to boot the instance. This is a shortcut for specifying a boot volume source via the --source-details complex JSON parameter. If this parameter is provided, you cannot provide the --source-details or --image-id parameters.""")
@cli_util.option('--boot-volume-size-in-gbs', type=click.INT, help="""The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 16384 GB (16TB). This is a shortcut for specifying a boot volume size via the --source-details complex JSON parameter. If this parameter is provided, you cannot provide the --source-details or --source-boot-volume-id parameters.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'create-vnic-details': {'module': 'core', 'class': 'CreateVnicDetails'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'extended-metadata': {'module': 'core', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'metadata': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'InstanceSourceDetails'}}, output_type={'module': 'core', 'class': 'Instance'})
@cli_util.wrap_exceptions
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

    if kwargs.get('source_details') and (kwargs.get('image_id') or kwargs.get('source_boot_volume_id') or kwargs.get('boot_volume_size_in_gbs')):
        raise click.UsageError(
            'Cannot specify --source-details with any of: --image-id, --source-boot-volume-id, or --boot-volume-size-in-gbs'
        )
    if kwargs.get('image_id') and kwargs.get('source_boot_volume_id'):
        raise click.UsageError(
            'Cannot specify both an --image-id and a --source-boot-volume-id to be used to boot the instance'
        )
    if kwargs.get('boot_volume_size_in_gbs') and kwargs.get('source_boot_volume_id'):
        raise click.UsageError(
            'Cannot specify both a --source-boot-volume-id and a --boot-volume-size-in-gbs to be used to boot the instance'
        )

    kwargs['metadata'] = json.dumps(metadata)

    create_vnic_details = {}
    if 'assign_public_ip' in kwargs and kwargs['assign_public_ip'] is not None:
        create_vnic_details['assignPublicIp'] = kwargs['assign_public_ip']

    if 'skip_source_dest_check' in kwargs and kwargs['skip_source_dest_check'] is not None:
        create_vnic_details['skipSourceDestCheck'] = kwargs['skip_source_dest_check']

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

    if kwargs.get('image_id'):
        source_details = {'sourceType': 'image', 'imageId': kwargs['image_id']}
        if kwargs.get('boot_volume_size_in_gbs'):
            source_details['bootVolumeSizeInGBs'] = kwargs.get('boot_volume_size_in_gbs')

        kwargs['source_details'] = json.dumps(source_details)
    if kwargs.get('source_boot_volume_id'):
        kwargs['source_details'] = json.dumps({'sourceType': 'bootVolume', 'bootVolumeId': kwargs['source_boot_volume_id']})

    # delete additional kwargs because launch_instance will not recognize them
    del kwargs['assign_public_ip']
    del kwargs['hostname_label']
    del kwargs['private_ip']
    del kwargs['ssh_authorized_keys_file']
    del kwargs['subnet_id']
    del kwargs['user_data_file']
    del kwargs['vnic_display_name']
    del kwargs['skip_source_dest_check']

    # Remove the source_boot_volume_id and boot_volume_size_in_gbs parameters. image_id is an existing parameter so the underlying
    # CLI operation will accept it
    kwargs.pop('boot_volume_size_in_gbs', None)
    kwargs.pop('source_boot_volume_id', None)

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)

    ctx.invoke(compute_cli.launch_instance, **kwargs)


@compute_cli.instance_group.command(name='attach-vnic', help="""Creates a secondary VNIC and attaches it to the specified instance. For more information about secondary VNICs, see [Virtual Network Interface Cards (VNICs)].""")
@cli_util.option('--instance-id', required=True, help="""The OCID of the instance.""")
@cli_util.option('--subnet-id', required=True, help="""The OCID of the subnet to create the VNIC in.""")
@cli_util.option('--vnic-display-name', help="""A user-friendly name for the VNIC. Does not have to be unique.""")
@cli_util.option('--assign-public-ip', type=click.BOOL, help="""Whether the VNIC should be assigned a public IP address. Defaults to whether the subnet is public or private. If not set and the VNIC is being created in a private subnet (i.e., where prohibitPublicIpOnVnic=true in the Subnet), then no public IP address is assigned. If not set and the subnet is public (prohibitPublicIpOnVnic=false), then a public IP address is assigned. If set to true and prohibitPublicIpOnVnic=true, an error is returned.""")
@cli_util.option('--skip-source-dest-check', type=click.BOOL, help="""Indicates whether Source/Destination check is disabled on the VNIC. Defaults to `false`, in which case we enable Source/Destination check on the VNIC.""")
@cli_util.option('--private-ip', help="""A private IP address of your choice to assign to the VNIC. Must be an available IP address within the subnet's CIDR. If no value is specified, a private IP address from the subnet will be automatically assigned.""")
@cli_util.option('--hostname-label', help="""The hostname for the VNIC. Used for DNS. The value is the hostname portion of the VNIC's fully qualified domain name (FQDN) (e.g., `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952](https://tools.ietf.org/html/rfc952) and [RFC 1123](https://tools.ietf.org/html/rfc1123). The value can be retrieved from the [Vnic](#/en/iaas/20160918/Vnic/).""")
@cli_util.option('--nic-index', type=click.INT, help="""Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use.""")
@cli_util.option('--wait', is_flag=True, default=False, help="""If set, then wait for the attachment to complete and return the newly attached VNIC. If not set, then the command will not wait and will return nothing on success.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Vnic'})
@cli_util.wrap_exceptions
def attach_vnic(ctx, from_json, instance_id, subnet_id, vnic_display_name, assign_public_ip, private_ip, skip_source_dest_check, hostname_label, nic_index, wait, freeform_tags, defined_tags):
    kwargs = {}

    vnic_details = {}
    vnic_details['subnetId'] = subnet_id
    vnic_details['displayName'] = vnic_display_name
    vnic_details['assignPublicIp'] = assign_public_ip
    vnic_details['privateIp'] = private_ip
    vnic_details['hostnameLabel'] = hostname_label

    if freeform_tags is not None:
        vnic_details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        vnic_details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if skip_source_dest_check is not None:
        vnic_details['skipSourceDestCheck'] = skip_source_dest_check

    attachment_details = {}
    attachment_details['createVnicDetails'] = vnic_details
    attachment_details['instanceId'] = instance_id
    attachment_details['nicIndex'] = nic_index

    compute_client = cli_util.build_client('compute', ctx)
    response = compute_client.attach_vnic(
        attach_vnic_details=attachment_details,
        **kwargs
    )

    # Returning without rendering any response in "no-wait" case makes sense here because displaying VNIC attachment
    # details is not useful to the CLI user. VNIC details are more useful for which CLI user must use --wait option
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
    cli_util.render_response(response, ctx)


@compute_cli.instance_group.command(name='detach-vnic', help="""Detaches and deletes the specified secondary VNIC. This operation cannot be used on the instance's primary VNIC. When you terminate an instance, all attached VNICs (primary and secondary) are automatically detached and deleted.""")
@cli_util.option('--vnic-id', required=True, help="""The OCID of the VNIC.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the instance's compartment.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def detach_vnic(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vnic_id, compartment_id):
    compute_client = cli_util.build_client('compute', ctx)
    result = compute_client.list_vnic_attachments(compartment_id=compartment_id, vnic_id=vnic_id)

    if result.data is None or len(result.data) == 0:
        sys.exit('A VNIC attachment could not be found for the given VNIC ID.')

    vnic_attachment_id = result.data[0].id
    result = compute_client.detach_vnic(vnic_attachment_id=vnic_attachment_id)
    if wait_for_state:
        if hasattr(compute_client, 'get_vnic_attachment') and callable(getattr(compute_client, 'get_vnic_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                wait_until(compute_client, compute_client.get_vnic_attachment(vnic_attachment_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except ServiceError as e:
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


@cli_util.copy_params_from_generated_command(virtualnetwork_cli.create_private_ip, params_to_exclude=[''])
@virtualnetwork_cli.vnic_group.command(name='assign-private-ip', help="""Assigns a secondary private IP address to the specified VNIC. The secondary private IP must be in the same subnet as the VNIC.
This command can also be used to move an existing secondary private IP to the specified VNIC.

For more information about secondary private IPs, see [IP Addresses]
""")
@cli_util.option('--unassign-if-already-assigned', is_flag=True, default=False, help="""Force reassignment of the IP address if it's already assigned to another VNIC in the subnet. This is only relevant if an IP address is associated with this command.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'PrivateIp'})
@cli_util.wrap_exceptions
def assign_private_ip(ctx, from_json, vnic_id, ip_address, display_name, hostname_label, unassign_if_already_assigned, defined_tags, freeform_tags):
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'PrivateIp'})
@cli_util.wrap_exceptions
def update_private_ip_extended(ctx, **kwargs):
    ctx.invoke(virtualnetwork_cli.update_private_ip, **kwargs)


@cli_util.copy_params_from_generated_command(compute_cli.create_instance_console_connection, params_to_exclude=['public_key'])
@compute_cli.instance_console_connection_group.command(name=cli_util.override('create_instance_console_connection.command_name', 'create'), help="""Creates a new serial console connection to the specified instance. Once the serial console connection has been created and is available, you connect to the serial console using an SSH client.

The default number of enabled serial console connections per tenancy is 10.

For more information about serial console access, see [Accessing the Console].""")
@cli_util.option('--ssh-public-key-file', required=True, type=click.File('r'), help="""A file containing the SSH public key used to authenticate the serial console connection""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'InstanceConsoleConnection'})
@cli_util.wrap_exceptions
def create_instance_console_connection(ctx, from_json, instance_id, ssh_public_key_file, wait_for_state, max_wait_seconds, wait_interval_seconds, defined_tags, freeform_tags):
    # Empirically, if the public key file contains multiple entires this is accepted but the serial console
    # will use the first key in the file
    kwargs = {
        'instance_id': instance_id,
        'public_key': ssh_public_key_file.read(),
        'wait_for_state': wait_for_state,
        'max_wait_seconds': max_wait_seconds,
        'wait_interval_seconds': wait_interval_seconds,
        'defined_tags': defined_tags,
        'freeform_tags': freeform_tags
    }

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)

    ctx.invoke(compute_cli.create_instance_console_connection, **kwargs)


cli_util.update_param_help(blockstorage_cli.create_volume, 'availability_domain', """The Availability Domain of the volume. Example: `Uocm:PHX-AD-1`.

This is optional when cloning a volume as the newly created volume will be created in the same Availability Domain as its source. This is required when creating an empty volume or restoring a volume from a backup.""", append=False)
cli_util.update_param_help(blockstorage_cli.create_volume, 'compartment_id', """The OCID of the compartment that contains the volume. This is optional when cloning a volume or restoring a volume from a backup. If it is not supplied then the volume will be created in the same compartment as the source. This is requied when creating an empty volume.""", append=False)
cli_util.update_param_help(blockstorage_cli.create_volume, 'size_in_mbs', """[DEPRECATED] The size of the volume in MBs. The value must be a multiple of 1024. This field is deprecated. Use --size-in-gbs instead.""", append=False)


@cli_util.copy_params_from_generated_command(blockstorage_cli.create_volume, params_to_exclude=['source_details', 'volume_backup_id', 'availability_domain', 'compartment_id'])
@blockstorage_cli.volume_group.command(name=cli_util.override('create_volume.command_name', 'create'), help="""Creates a new volume in the specified compartment. Volumes can be created in sizes ranging from 50 GB (51200 MB) to 16 TB (16777216 MB), in 1 GB (1024 MB) increments. By default, volumes are 1 TB (1048576 MB). For general information about block volumes, see [Overview of Block Volume Service].

A volume and instance can be in separate compartments but must be in the same Availability Domain. For information about access control and compartments, see [Overview of the IAM Service]. For information about Availability Domains, see [Regions and Availability Domains]. To get a list of Availability Domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

You may optionally specify a *display name* for the volume, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--availability-domain', help="""The Availability Domain of the volume.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', help="""The OCID of the compartment that contains the volume.""")
@cli_util.option('--source-volume-id', help="""The OCID of a Block volume in the same Availability Domain from which the data should be cloned to the newly created volume. You can specify either this or --volume-backup-id but not both. If neither is specified then the new Block volume will be empty.""")
@cli_util.option('--volume-backup-id', help="""The OCID of the volume backup from which the data should be restored on the newly created volume. You can specify either this or --source-volume-id but not both. If neither is specified then the new Block volume will be empty.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Volume'})
@cli_util.wrap_exceptions
def create_volume_extended(ctx, **kwargs):
    if kwargs['source_volume_id'] and kwargs['volume_backup_id']:
        raise click.UsageError('You cannot specify both the --volume-backup-id and --source-volume-id options')

    if not kwargs['source_volume_id'] and not kwargs['availability_domain']:
        raise click.UsageError('An availability domain must be specified when creating an empty volume or restoring a volume from a backup')

    if not kwargs['source_volume_id'] and not kwargs['volume_backup_id'] and not kwargs['compartment_id']:
        raise click.UsageError('A compartment ID must be specified when creating an empty volume')

    if kwargs['size_in_mbs'] and kwargs['size_in_gbs']:
        raise click.UsageError('You cannot specify both --size-in-mbs and --size-in-gbs')

    client = cli_util.build_client('blockstorage', ctx)

    if kwargs['source_volume_id']:
        source_volume = client.get_volume(volume_id=kwargs['source_volume_id'])
        kwargs['availability_domain'] = source_volume.data.availability_domain
        if not kwargs['compartment_id']:
            kwargs['compartment_id'] = source_volume.data.compartment_id

    if kwargs['volume_backup_id']:
        source_backup = client.get_volume_backup(volume_backup_id=kwargs['volume_backup_id'])
        if not kwargs['compartment_id']:
            kwargs['compartment_id'] = source_backup.data.compartment_id

    if kwargs['source_volume_id'] or kwargs['volume_backup_id']:
        if kwargs['volume_backup_id']:
            source_details = {
                'type': 'volumeBackup',
                'id': kwargs['volume_backup_id']
            }
        else:
            source_details = {
                'type': 'volume',
                'id': kwargs['source_volume_id']
            }

        kwargs['source_details'] = json.dumps(source_details)

    kwargs.pop('source_volume_id', None)
    kwargs.pop('volume_backup_id', None)

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)

    ctx.invoke(blockstorage_cli.create_volume, **kwargs)


@cli_util.copy_params_from_generated_command(blockstorage_cli.create_boot_volume, params_to_exclude=['source_details', 'availability_domain', 'compartment_id'])
@blockstorage_cli.boot_volume_group.command(name=cli_util.override('create_boot_volume.command_name', 'create'), help="""Creates a new boot volume in the specified compartment from an existing boot volume or a boot volume backup. For general information about boot volumes, see [Boot Volumes]. You may optionally specify a *display name* for the volume, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--availability-domain', help="""The Availability Domain of the boot volume. Example: `Uocm:PHX-AD-1`.

This is optional when cloning a boot volume as the newly created boot volume will be created in the same Availability Domain as its source. This is required when restoring a volume from a backup.""")
@cli_util.option('--compartment-id', help="""The OCID of the compartment that contains the boot volume. This is optional when cloning a boot volume or restoring a boot volume from a backup. If it is not supplied then the boot volume will be created in the same compartment as the source.""")
@cli_util.option('--source-boot-volume-id', help="""The OCID of a boot volume in the same Availability Domain from which the data should be cloned to the newly created boot volume. You can specify either this or --boot-volume-backup-id but not both.""")
@cli_util.option('--boot-volume-backup-id', help="""The OCID of the boot volume backup from which the data should be restored on the newly created boot volume. You can specify either this or --source-boot-volume-id but not both.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'BootVolume'})
@cli_util.wrap_exceptions
def create_boot_volume_extended(ctx, **kwargs):
    if kwargs['source_boot_volume_id'] and kwargs['boot_volume_backup_id']:
        raise click.UsageError('You cannot specify both the --boot-volume-backup-id and --source-boot-volume-id options')

    if not kwargs['source_boot_volume_id'] and not kwargs['boot_volume_backup_id']:
        raise click.UsageError('An empty boot volume cannot be created. Please specify either --boot-volume-backup-id or --source-boot-volume-id')

    if not kwargs['source_boot_volume_id'] and not kwargs['availability_domain']:
        raise click.UsageError('An availability domain must be specified when restoring a boot volume from backup')

    client = cli_util.build_client('blockstorage', ctx)

    if kwargs['source_boot_volume_id']:
        source_boot_volume = client.get_boot_volume(boot_volume_id=kwargs['source_boot_volume_id'])
        kwargs['availability_domain'] = source_boot_volume.data.availability_domain
        if not kwargs['compartment_id']:
            kwargs['compartment_id'] = source_boot_volume.data.compartment_id

    if kwargs['boot_volume_backup_id']:
        source_backup = client.get_boot_volume_backup(boot_volume_backup_id=kwargs['boot_volume_backup_id'])
        if not kwargs['compartment_id']:
            kwargs['compartment_id'] = source_backup.data.compartment_id

    if kwargs['source_boot_volume_id'] or kwargs['boot_volume_backup_id']:
        if kwargs['boot_volume_backup_id']:
            source_details = {
                'type': 'bootVolumeBackup',
                'id': kwargs['boot_volume_backup_id']
            }
        else:
            source_details = {
                'type': 'bootVolume',
                'id': kwargs['source_boot_volume_id']
            }

        kwargs['source_details'] = json.dumps(source_details)

    kwargs.pop('source_boot_volume_id', None)
    kwargs.pop('boot_volume_backup_id', None)

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)

    ctx.invoke(blockstorage_cli.create_boot_volume, **kwargs)


@virtualnetwork_cli.public_ip_group.command(name='get', help="""Gets the specified public IP object.
The command needs at least one of the options to be used to be able to get the public IP object successfully.""")
@option('--public-ip-address', help="""A public IP address. Example: 129.146.2.1""")
@option('--public-ip-id', help="""The public IP's OCID.""")
@option('--private-ip-id', help="""The private IP's OCID.""")
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


@compute_cli.instance_console_connection_group.command(name='get-plink-connection-string', help="""Gets the plink command for starting an SSH tunnel on Windows which will allow VNC connections to the instance. Once you have started the tunnel, you can point your VNC client to localhost:{{--local-vnc-port}} to connect to the instance (default --local-vnc-port is {}).""".format(DEFAULT_LOCAL_VNC_PORT))
@cli_util.option('--instance-console-connection-id', required=True, help="""The OCID of the intance console connection""")
@cli_util.option('--private-key-file', required=True, help="""The path to the private key to be used for authentication. This is inserted into the generated connection string.""")
@cli_util.option('--local-vnc-port', help="""This is the local port that you will point your VNC client at. This will be forwarded to the SSH tunnel created by executing the PowerShell command in the output. Default is {}.""".format(DEFAULT_LOCAL_VNC_PORT))
@cli_util.option('--ssh-proxy-port', help="""This is the local and remote port for the SSH tunnel.  This may be any open port on your local machine.  Default is {}.""".format(DEFAULT_SSH_PROXY_PORT))
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstanceConsoleConnection'})
@cli_util.wrap_exceptions
def get_plink_connection_string(ctx, from_json, instance_console_connection_id, private_key_file, local_vnc_port, ssh_proxy_port):
    if isinstance(instance_console_connection_id, six.string_types) and len(instance_console_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-console-connection-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('compute', ctx)
    result = client.get_instance_console_connection(
        instance_console_connection_id=instance_console_connection_id,
        **kwargs
    )

    instance_console_connection = result.data

    if local_vnc_port is None:
        local_vnc_port = DEFAULT_LOCAL_VNC_PORT

    if ssh_proxy_port is None:
        ssh_proxy_port = DEFAULT_SSH_PROXY_PORT

    # extract the intermediate host from the SSH connection string (this is the same regex used by the console)
    m = re.search(INSTANCE_CONSOLE_CONNECTION_STRING_INTERMEDIATE_HOST_REGEX, instance_console_connection.connection_string)
    intermediate_host = m.group(0)

    # There are two calls to plink
    # plink -ssh -N -i {KEY} -P 443 -l  {ICC_OCID} {ICC_HOST_SERVER} -L 5905:{INSTANCE_OCID}:5905
    # plink -L 5900:localhost:5900 localhost -P 5905 -N -i {KEY} -l {ICC_OCID}
    connection_template = (
        'Start-Job {{echo N | '
        'plink -ssh -N -i "{private_key_file}" -P 443 -l {instance_console_connection_id} {intermediate_host} -L {ssh_proxy_port}:{instance_id}:{ssh_proxy_port}}}; sleep 5 ; '
        'plink -L {local_vnc_port}:localhost:5900 localhost -P {ssh_proxy_port} -N -i "{private_key_file}" -l {instance_console_connection_id}'
    )

    connection_string = connection_template.format(
        instance_id=instance_console_connection.instance_id,
        instance_console_connection_id=instance_console_connection.id,
        intermediate_host=intermediate_host,
        private_key_file=private_key_file,
        local_vnc_port=local_vnc_port,
        ssh_proxy_port=ssh_proxy_port
    )

    # print directly to avoid escaping double quotes
    click.echo(connection_string)


@cli_util.copy_params_from_generated_command(virtualnetwork_cli.connect_remote_peering_connections, params_to_exclude=['peer_region_name'])
@virtualnetwork_cli.remote_peering_connection_group.command(name='connect', help="""Connects this RPC to another one in a different region.

This operation must be called by the VCN administrator who is designated as the *requestor* in the peering relationship. The *acceptor* must implement an Identity and Access Management (IAM) policy that gives the requestor permission to connect to RPCs in the acceptor's compartment. Without that permission, this operation will fail. For more information, see [VCN Peering].""")
# Below param is not enforced as an enum to allow backward compatibility for old CLIs to support newer regions.
@cli_util.option('--peer-region-name', required=True, help="""The name of the region that contains the RPC you want to peer with.

The region names that could be used are listed here: https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm
Example: `us-ashburn-1`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def connect_remote_peering_connections_extended(ctx, **kwargs):
    try:
        # Get the valid region list by querying IAM service
        client = cli_util.build_client('identity', ctx)
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

#################################################################
# Begin Partner image catalog
#
# We want to replace the following:
#   oci compute app-catalog-listing get
#   oci compute app-catalog-listing list
#   oci compute app-catalog-listing-resource-version get
#   oci compute app-catalog-listing-resource-version list
#   oci compute app-catalog-listing-resource-version-agreements get-app-catalog-listing-agreements
#   oci compute app-catalog-subscription create --oracle-terms-of-use-link
#   oci compute app-catalog-subscription delete
#   oci compute app-catalog-subscription list
#
# With these:
#   oci compute pic listing get
#   oci compute pic listing list
#   oci compute pic version get
#   oci compute pic version list
#   oci compute pic agreements get
#   oci compute pic subscription create --oracle-tou-link
#   oci compute pic subscription delete
#   oci compute pic subscription list

# Disabling app_catalog commands
compute_cli.compute_root_group.commands.pop(compute_cli.app_catalog_listing_group.name)
compute_cli.compute_root_group.commands.pop(compute_cli.app_catalog_listing_resource_version_agreements_group.name)
compute_cli.compute_root_group.commands.pop(compute_cli.app_catalog_listing_resource_version_group.name)
compute_cli.compute_root_group.commands.pop(compute_cli.app_catalog_subscription_group.name)


@click.command('pic', cls=CommandGroupWithAlias, help="""Partner image catalog (PIC).""")
@cli_util.help_option_group
def pic_group():
    pass


@click.command('listing', cls=CommandGroupWithAlias, help="""A PIC listing.""")
@cli_util.help_option_group
def pic_listing_group():
    pass


@click.command('version', cls=CommandGroupWithAlias, help="""A PIC listing resource version.""")
@cli_util.help_option_group
def pic_version_group():
    pass


@click.command('agreements', cls=CommandGroupWithAlias, help="""PIC listing resource version agreements.""")
@cli_util.help_option_group
def pic_agreements_group():
    pass


@click.command('subscription', cls=CommandGroupWithAlias, help="""A PIC subscription.""")
@cli_util.help_option_group
def pic_subscription_group():
    pass


compute_cli.compute_root_group.add_command(pic_group)
pic_group.add_command(pic_listing_group)
pic_group.add_command(pic_version_group)
pic_group.add_command(pic_agreements_group)
pic_group.add_command(pic_subscription_group)

pic_listing_group.add_command(compute_cli.list_app_catalog_listings)
pic_listing_group.add_command(compute_cli.get_app_catalog_listing)
pic_version_group.add_command(compute_cli.list_app_catalog_listing_resource_versions)
pic_version_group.add_command(compute_cli.get_app_catalog_listing_resource_version)
pic_subscription_group.add_command(compute_cli.list_app_catalog_subscriptions)
pic_subscription_group.add_command(compute_cli.delete_app_catalog_subscription)


@cli_util.copy_params_from_generated_command(compute_cli.get_app_catalog_listing_agreements, params_to_exclude=[])
@pic_agreements_group.command(name='get', help=compute_cli.get_app_catalog_listing_agreements.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def get_app_catalog_listing_agreements(ctx, **kwargs):
    ctx.invoke(compute_cli.get_app_catalog_listing_agreements, **kwargs)


@cli_util.copy_params_from_generated_command(compute_cli.create_app_catalog_subscription, params_to_exclude=['oracle_terms_of_use_link', 'listing_resource_version'])
@pic_subscription_group.command(name='create', help=compute_cli.create_app_catalog_subscription.help)
@cli_util.option('--listing-id', required=True, help="""The OCID of the listing.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--resource-version', required=True, help="""Listing Resource Version.""")
@cli_util.option('--signature', required=True, help="""A generated signature for this listing resource version retrieved the agreements API.""")
@cli_util.option('--oracle-tou-link', required=True, help='''Oracle Terms of Use link''')
@cli_util.option('--eula-link', required=True, help='''EULA link''')
@cli_util.option('--time-retrieved', required=True, type=custom_types.CLI_DATETIME, help="""Date and time the agreements were retrieved, in RFC3339 format. Example: `2018-03-20T12:32:53.532Z`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def create_app_catalog_subscription(ctx, **kwargs):
    if 'oracle_tou_link' in kwargs:
        kwargs['oracle_terms_of_use_link'] = kwargs['oracle_tou_link']
        kwargs.pop('oracle_tou_link')
    if 'resource_version' in kwargs:
        kwargs['listing_resource_version'] = kwargs['resource_version']
        kwargs.pop('resource_version')
    ctx.invoke(compute_cli.create_app_catalog_subscription, **kwargs)

# End of Partner image catalog
#################################################################
