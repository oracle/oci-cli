# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('fs.fs_root_group.command_name', 'fs'), cls=CommandGroupWithAlias, help=cli_util.override('fs.fs_root_group.help', """API for the File Storage service. Use this API to manage file systems, mount targets, and snapshots. For more information, see [Overview of File Storage]."""), short_help=cli_util.override('fs.fs_root_group.short_help', """File Storage API"""))
@cli_util.help_option_group
def fs_root_group():
    pass


@click.command(cli_util.override('fs.file_system_group.command_name', 'file-system'), cls=CommandGroupWithAlias, help="""An NFS file system. To allow access to a file system, add it to an export set and associate the export set with a mount target. The same file system can be in multiple export sets and associated with multiple mount targets.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def file_system_group():
    pass


@click.command(cli_util.override('fs.export_set_group.command_name', 'export-set'), cls=CommandGroupWithAlias, help="""A set of file systems to export through one or more mount targets. Composed of zero or more export resources.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def export_set_group():
    pass


@click.command(cli_util.override('fs.mount_target_group.command_name', 'mount-target'), cls=CommandGroupWithAlias, help="""Provides access to a collection of file systems through one or more VNICs on a specified subnet. The set of file systems is controlled through the referenced export set.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def mount_target_group():
    pass


@click.command(cli_util.override('fs.export_group.command_name', 'export'), cls=CommandGroupWithAlias, help="""A file system and the path that you can use to mount it. Each export resource belongs to exactly one export set.

The export's path attribute is not a path in the referenced file system, but the value used by clients for the path component of the remotetarget argument when mounting the file system.

The path must start with a slash (/) followed by a sequence of zero or more slash-separated path elements. For any two export resources associated with the same export set, except those in a 'DELETED' state, the path element sequence for the first export resource can't contain the complete path element sequence of the second export resource.

 For example, the following are acceptable:

  * /example and /path   * /example1 and /example2   * /example and /example1

The following examples are not acceptable:   * /example and /example/path   * / and /example

Paths may not end in a slash (/). No path element can be a period (.) or two periods in sequence (..). All path elements must be 255 bytes or less.

No two non-'DELETED' export resources in the same export set can reference the same file system.

Use `exportOptions` to control access to an export. For more information, see [Export Options].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def export_group():
    pass


@click.command(cli_util.override('fs.snapshot_group.command_name', 'snapshot'), cls=CommandGroupWithAlias, help="""A point-in-time snapshot of a specified file system.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def snapshot_group():
    pass


fs_root_group.add_command(file_system_group)
fs_root_group.add_command(export_set_group)
fs_root_group.add_command(mount_target_group)
fs_root_group.add_command(export_group)
fs_root_group.add_command(snapshot_group)


@file_system_group.command(name=cli_util.override('fs.change_file_system_compartment.command_name', 'change-compartment'), help=u"""Moves a file system and its associated snapshots into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]""")
@cli_util.option('--file-system-id', required=True, help=u"""The OCID of the file system.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the file system to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_file_system_compartment(ctx, from_json, file_system_id, compartment_id, if_match):

    if isinstance(file_system_id, six.string_types) and len(file_system_id.strip()) == 0:
        raise click.UsageError('Parameter --file-system-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.change_file_system_compartment(
        file_system_id=file_system_id,
        change_file_system_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@mount_target_group.command(name=cli_util.override('fs.change_mount_target_compartment.command_name', 'change-compartment'), help=u"""Moves a mount target and its associated export set into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]""")
@cli_util.option('--mount-target-id', required=True, help=u"""The OCID of the mount target.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the mount target to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_mount_target_compartment(ctx, from_json, mount_target_id, compartment_id, if_match):

    if isinstance(mount_target_id, six.string_types) and len(mount_target_id.strip()) == 0:
        raise click.UsageError('Parameter --mount-target-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.change_mount_target_compartment(
        mount_target_id=mount_target_id,
        change_mount_target_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@export_group.command(name=cli_util.override('fs.create_export.command_name', 'create'), help=u"""Creates a new export in the specified export set, path, and file system.""")
@cli_util.option('--export-set-id', required=True, help=u"""The OCID of this export's export set.""")
@cli_util.option('--file-system-id', required=True, help=u"""The OCID of this export's file system.""")
@cli_util.option('--path', required=True, help=u"""Path used to access the associated file system.

Avoid entering confidential information.

Example: `/mediafiles`""")
@cli_util.option('--export-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Export options for the new export. If left unspecified, defaults to:

       [          {             \"source\" : \"0.0.0.0/0\",             \"requirePrivilegedSourcePort\" : false,             \"access\" : \"READ_WRITE\",             \"identitySquash\" : \"NONE\"           }        ]

  **Note:** Mount targets do not have Internet-routable IP   addresses.  Therefore they will not be reachable from the   Internet, even if an associated `ClientOptions` item has   a source of `0.0.0.0/0`.

  **If set to the empty array then the export will not be   visible to any clients.**

  The export's `exportOptions` can be changed after creation   using the `UpdateExport` operation.

This option is a JSON list with items of type ClientOptions.  For documentation on ClientOptions please see our API reference: https://docs.cloud.oracle.com/api/#/en/filestorage/20171215/datatypes/ClientOptions.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'export-options': {'module': 'file_storage', 'class': 'list[ClientOptions]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'export-options': {'module': 'file_storage', 'class': 'list[ClientOptions]'}}, output_type={'module': 'file_storage', 'class': 'Export'})
@cli_util.wrap_exceptions
def create_export(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, export_set_id, file_system_id, path, export_options):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['exportSetId'] = export_set_id
    _details['fileSystemId'] = file_system_id
    _details['path'] = path

    if export_options is not None:
        _details['exportOptions'] = cli_util.parse_json_parameter("export_options", export_options)

    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.create_export(
        create_export_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_export') and callable(getattr(client, 'get_export')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_export(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@file_system_group.command(name=cli_util.override('fs.create_file_system.command_name', 'create'), help=u"""Creates a new file system in the specified compartment and availability domain. Instances can mount file systems in another availability domain, but doing so might increase latency when compared to mounting instances in the same availability domain.

After you create a file system, you can associate it with a mount target. Instances can then mount the file system by connecting to the mount target's IP address. You can associate a file system with more than one mount target at a time.

For information about access control and compartments, see [Overview of the IAM Service].

For information about Network Security Groups access control, see [Network Security Groups].

For information about availability domains, see [Regions and Availability Domains]. To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

All Oracle Cloud Infrastructure resources, including file systems, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID).  When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type or by viewing the resource in the Console.""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain to create the file system in.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to create the file system in.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.

Example: `My file system`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair  with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""The OCID of KMS key used to encrypt the encryption keys associated with this file system.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'file_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'file_storage', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'file_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'file_storage', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'file_storage', 'class': 'FileSystem'})
@cli_util.wrap_exceptions
def create_file_system(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, display_name, freeform_tags, defined_tags, kms_key_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.create_file_system(
        create_file_system_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_file_system') and callable(getattr(client, 'get_file_system')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_file_system(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@mount_target_group.command(name=cli_util.override('fs.create_mount_target.command_name', 'create'), help=u"""Creates a new mount target in the specified compartment and subnet. You can associate a file system with a mount target only when they exist in the same availability domain. Instances can connect to mount targets in another availablity domain, but you might see higher latency than with instances in the same availability domain as the mount target.

Mount targets have one or more private IP addresses that you can provide as the host portion of remote target parameters in client mount commands. These private IP addresses are listed in the privateIpIds property of the mount target and are highly available. Mount targets also consume additional IP addresses in their subnet. Do not use /30 or smaller subnets for mount target creation because they do not have sufficient available IP addresses. Allow at least three IP addresses for each mount target.

For information about access control and compartments, see [Overview of the IAM Service].

For information about availability domains, see [Regions and Availability Domains]. To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

All Oracle Cloud Infrastructure Services resources, including mount targets, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID).  When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain in which to create the mount target.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to create the mount target.""")
@cli_util.option('--subnet-id', required=True, help=u"""The OCID of the subnet in which to create the mount target.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.

Example: `My mount target`""")
@cli_util.option('--hostname-label', help=u"""The hostname for the mount target's IP address, used for DNS resolution. The value is the hostname portion of the private IP address's fully qualified domain name (FQDN). For example, `files-1` in the FQDN `files-1.subnet123.vcn1.oraclevcn.com`. Must be unique across all VNICs in the subnet and comply with [RFC 952] and [RFC 1123].

For more information, see [DNS in Your Virtual Cloud Network].

Example: `files-1`""")
@cli_util.option('--ip-address', help=u"""A private IP address of your choice. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet.

Example: `10.0.3.3`""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of Network Security Group [OCIDs] associated with this mount target. A maximum of 5 is allowed. Setting this to an empty array after the list is created removes the mount target from all NSGs. For more information about NSGs, see [Security Rules].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair  with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nsg-ids': {'module': 'file_storage', 'class': 'list[string]'}, 'freeform-tags': {'module': 'file_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'file_storage', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'file_storage', 'class': 'list[string]'}, 'freeform-tags': {'module': 'file_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'file_storage', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'file_storage', 'class': 'MountTarget'})
@cli_util.wrap_exceptions
def create_mount_target(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, subnet_id, display_name, hostname_label, ip_address, nsg_ids, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id
    _details['subnetId'] = subnet_id

    if display_name is not None:
        _details['displayName'] = display_name

    if hostname_label is not None:
        _details['hostnameLabel'] = hostname_label

    if ip_address is not None:
        _details['ipAddress'] = ip_address

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.create_mount_target(
        create_mount_target_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_mount_target') and callable(getattr(client, 'get_mount_target')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_mount_target(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@snapshot_group.command(name=cli_util.override('fs.create_snapshot.command_name', 'create'), help=u"""Creates a new snapshot of the specified file system. You can access the snapshot at `.snapshot/<name>`.""")
@cli_util.option('--file-system-id', required=True, help=u"""The OCID of the file system to take a snapshot of.""")
@cli_util.option('--name', required=True, help=u"""Name of the snapshot. This value is immutable. It must also be unique with respect to all other non-DELETED snapshots on the associated file system.

Avoid entering confidential information.

Example: `Sunday`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair  with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'file_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'file_storage', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'file_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'file_storage', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'file_storage', 'class': 'Snapshot'})
@cli_util.wrap_exceptions
def create_snapshot(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, file_system_id, name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['fileSystemId'] = file_system_id
    _details['name'] = name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.create_snapshot(
        create_snapshot_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_snapshot') and callable(getattr(client, 'get_snapshot')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_snapshot(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@export_group.command(name=cli_util.override('fs.delete_export.command_name', 'delete'), help=u"""Deletes the specified export.""")
@cli_util.option('--export-id', required=True, help=u"""The OCID of the export.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_export(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, export_id, if_match):

    if isinstance(export_id, six.string_types) and len(export_id.strip()) == 0:
        raise click.UsageError('Parameter --export-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.delete_export(
        export_id=export_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_export') and callable(getattr(client, 'get_export')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_export(export_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@file_system_group.command(name=cli_util.override('fs.delete_file_system.command_name', 'delete'), help=u"""Deletes the specified file system. Before you delete the file system, verify that no remaining export resources still reference it. Deleting a file system also deletes all of its snapshots.""")
@cli_util.option('--file-system-id', required=True, help=u"""The OCID of the file system.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_file_system(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, file_system_id, if_match):

    if isinstance(file_system_id, six.string_types) and len(file_system_id.strip()) == 0:
        raise click.UsageError('Parameter --file-system-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.delete_file_system(
        file_system_id=file_system_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_file_system') and callable(getattr(client, 'get_file_system')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_file_system(file_system_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@mount_target_group.command(name=cli_util.override('fs.delete_mount_target.command_name', 'delete'), help=u"""Deletes the specified mount target. This operation also deletes the mount target's VNICs.""")
@cli_util.option('--mount-target-id', required=True, help=u"""The OCID of the mount target.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_mount_target(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, mount_target_id, if_match):

    if isinstance(mount_target_id, six.string_types) and len(mount_target_id.strip()) == 0:
        raise click.UsageError('Parameter --mount-target-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.delete_mount_target(
        mount_target_id=mount_target_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_mount_target') and callable(getattr(client, 'get_mount_target')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_mount_target(mount_target_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@snapshot_group.command(name=cli_util.override('fs.delete_snapshot.command_name', 'delete'), help=u"""Deletes the specified snapshot.""")
@cli_util.option('--snapshot-id', required=True, help=u"""The OCID of the snapshot.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_snapshot(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, snapshot_id, if_match):

    if isinstance(snapshot_id, six.string_types) and len(snapshot_id.strip()) == 0:
        raise click.UsageError('Parameter --snapshot-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.delete_snapshot(
        snapshot_id=snapshot_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_snapshot') and callable(getattr(client, 'get_snapshot')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_snapshot(snapshot_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@export_group.command(name=cli_util.override('fs.get_export.command_name', 'get'), help=u"""Gets the specified export's information.""")
@cli_util.option('--export-id', required=True, help=u"""The OCID of the export.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'Export'})
@cli_util.wrap_exceptions
def get_export(ctx, from_json, export_id):

    if isinstance(export_id, six.string_types) and len(export_id.strip()) == 0:
        raise click.UsageError('Parameter --export-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.get_export(
        export_id=export_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@export_set_group.command(name=cli_util.override('fs.get_export_set.command_name', 'get'), help=u"""Gets the specified export set's information.""")
@cli_util.option('--export-set-id', required=True, help=u"""The OCID of the export set.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'ExportSet'})
@cli_util.wrap_exceptions
def get_export_set(ctx, from_json, export_set_id):

    if isinstance(export_set_id, six.string_types) and len(export_set_id.strip()) == 0:
        raise click.UsageError('Parameter --export-set-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.get_export_set(
        export_set_id=export_set_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@file_system_group.command(name=cli_util.override('fs.get_file_system.command_name', 'get'), help=u"""Gets the specified file system's information.""")
@cli_util.option('--file-system-id', required=True, help=u"""The OCID of the file system.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'FileSystem'})
@cli_util.wrap_exceptions
def get_file_system(ctx, from_json, file_system_id):

    if isinstance(file_system_id, six.string_types) and len(file_system_id.strip()) == 0:
        raise click.UsageError('Parameter --file-system-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.get_file_system(
        file_system_id=file_system_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@mount_target_group.command(name=cli_util.override('fs.get_mount_target.command_name', 'get'), help=u"""Gets the specified mount target's information.""")
@cli_util.option('--mount-target-id', required=True, help=u"""The OCID of the mount target.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'MountTarget'})
@cli_util.wrap_exceptions
def get_mount_target(ctx, from_json, mount_target_id):

    if isinstance(mount_target_id, six.string_types) and len(mount_target_id.strip()) == 0:
        raise click.UsageError('Parameter --mount-target-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.get_mount_target(
        mount_target_id=mount_target_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@snapshot_group.command(name=cli_util.override('fs.get_snapshot.command_name', 'get'), help=u"""Gets the specified snapshot's information.""")
@cli_util.option('--snapshot-id', required=True, help=u"""The OCID of the snapshot.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'Snapshot'})
@cli_util.wrap_exceptions
def get_snapshot(ctx, from_json, snapshot_id):

    if isinstance(snapshot_id, six.string_types) and len(snapshot_id.strip()) == 0:
        raise click.UsageError('Parameter --snapshot-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.get_snapshot(
        snapshot_id=snapshot_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@export_set_group.command(name=cli_util.override('fs.list_export_sets.command_name', 'list'), help=u"""Lists the export set resources in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--availability-domain', required=True, help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum.

For important details about how pagination works, see [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique, and it is changeable.

Example: `My resource`""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""Filter results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--id', help=u"""Filter results by OCID. Must be an OCID of the correct type for the resouce type.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide either value, but not both. By default, when you sort by time created, results are shown in descending order. When you sort by display name, results are shown in ascending order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending. The default order is 'desc' except for numeric values.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'list[ExportSetSummary]'})
@cli_util.wrap_exceptions
def list_export_sets(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, limit, page, display_name, lifecycle_state, id, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if id is not None:
        kwargs['id'] = id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_export_sets,
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_export_sets,
            limit,
            page_size,
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    else:
        result = client.list_export_sets(
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@export_group.command(name=cli_util.override('fs.list_exports.command_name', 'list'), help=u"""Lists export resources by compartment, file system, or export set. You must specify an export set ID, a file system ID, and / or a compartment ID.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum.

For important details about how pagination works, see [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--export-set-id', help=u"""The OCID of the export set.""")
@cli_util.option('--file-system-id', help=u"""The OCID of the file system.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""Filter results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--id', help=u"""Filter results by OCID. Must be an OCID of the correct type for the resouce type.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "PATH"]), help=u"""The field to sort by. You can provide either value, but not both. By default, when you sort by time created, results are shown in descending order. When you sort by path, results are shown in ascending alphanumeric order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending. The default order is 'desc' except for numeric values.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'list[ExportSummary]'})
@cli_util.wrap_exceptions
def list_exports(ctx, from_json, all_pages, page_size, compartment_id, limit, page, export_set_id, file_system_id, lifecycle_state, id, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if export_set_id is not None:
        kwargs['export_set_id'] = export_set_id
    if file_system_id is not None:
        kwargs['file_system_id'] = file_system_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if id is not None:
        kwargs['id'] = id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_exports,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_exports,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_exports(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@file_system_group.command(name=cli_util.override('fs.list_file_systems.command_name', 'list'), help=u"""Lists the file system resources in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--availability-domain', required=True, help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum.

For important details about how pagination works, see [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique, and it is changeable.

Example: `My resource`""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""Filter results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--id', help=u"""Filter results by OCID. Must be an OCID of the correct type for the resouce type.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide either value, but not both. By default, when you sort by time created, results are shown in descending order. When you sort by display name, results are shown in ascending order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending. The default order is 'desc' except for numeric values.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'list[FileSystemSummary]'})
@cli_util.wrap_exceptions
def list_file_systems(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, limit, page, display_name, lifecycle_state, id, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if id is not None:
        kwargs['id'] = id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_file_systems,
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_file_systems,
            limit,
            page_size,
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    else:
        result = client.list_file_systems(
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@mount_target_group.command(name=cli_util.override('fs.list_mount_targets.command_name', 'list'), help=u"""Lists the mount target resources in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--availability-domain', required=True, help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum.

For important details about how pagination works, see [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique, and it is changeable.

Example: `My resource`""")
@cli_util.option('--export-set-id', help=u"""The OCID of the export set.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""Filter results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--id', help=u"""Filter results by OCID. Must be an OCID of the correct type for the resouce type.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can choose either value, but not both. By default, when you sort by time created, results are shown in descending order. When you sort by display name, results are shown in ascending order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending. The default order is 'desc' except for numeric values.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'list[MountTargetSummary]'})
@cli_util.wrap_exceptions
def list_mount_targets(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, limit, page, display_name, export_set_id, lifecycle_state, id, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if export_set_id is not None:
        kwargs['export_set_id'] = export_set_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if id is not None:
        kwargs['id'] = id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_mount_targets,
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_mount_targets,
            limit,
            page_size,
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    else:
        result = client.list_mount_targets(
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@snapshot_group.command(name=cli_util.override('fs.list_snapshots.command_name', 'list'), help=u"""Lists snapshots of the specified file system.""")
@cli_util.option('--file-system-id', required=True, help=u"""The OCID of the file system.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum.

For important details about how pagination works, see [List Pagination].

Example: `100`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""Filter results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--id', help=u"""Filter results by OCID. Must be an OCID of the correct type for the resouce type.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending. The default order is 'desc' except for numeric values.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'list[SnapshotSummary]'})
@cli_util.wrap_exceptions
def list_snapshots(ctx, from_json, all_pages, page_size, file_system_id, limit, page, lifecycle_state, id, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if id is not None:
        kwargs['id'] = id
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_snapshots,
            file_system_id=file_system_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_snapshots,
            limit,
            page_size,
            file_system_id=file_system_id,
            **kwargs
        )
    else:
        result = client.list_snapshots(
            file_system_id=file_system_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@export_group.command(name=cli_util.override('fs.update_export.command_name', 'update'), help=u"""Updates the specified export's information.""")
@cli_util.option('--export-id', required=True, help=u"""The OCID of the export.""")
@cli_util.option('--export-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""New export options for the export.

**Setting to the empty array will make the export invisible to all clients.**

Leaving unset will leave the `exportOptions` unchanged.

This option is a JSON list with items of type ClientOptions.  For documentation on ClientOptions please see our API reference: https://docs.cloud.oracle.com/api/#/en/filestorage/20171215/datatypes/ClientOptions.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'export-options': {'module': 'file_storage', 'class': 'list[ClientOptions]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'export-options': {'module': 'file_storage', 'class': 'list[ClientOptions]'}}, output_type={'module': 'file_storage', 'class': 'Export'})
@cli_util.wrap_exceptions
def update_export(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, export_id, export_options, if_match):

    if isinstance(export_id, six.string_types) and len(export_id.strip()) == 0:
        raise click.UsageError('Parameter --export-id cannot be whitespace or empty string')
    if not force:
        if export_options:
            if not click.confirm("WARNING: Updates to export-options will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if export_options is not None:
        _details['exportOptions'] = cli_util.parse_json_parameter("export_options", export_options)

    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.update_export(
        export_id=export_id,
        update_export_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_export') and callable(getattr(client, 'get_export')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_export(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@export_set_group.command(name=cli_util.override('fs.update_export_set.command_name', 'update'), help=u"""Updates the specified export set's information.""")
@cli_util.option('--export-set-id', required=True, help=u"""The OCID of the export set.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.

Example: `My export set`""")
@cli_util.option('--max-fs-stat-bytes', type=click.INT, help=u"""Controls the maximum `tbytes`, `fbytes`, and `abytes` values reported by `NFS FSSTAT` calls through any associated mount targets. This is an advanced feature. For most applications, use the default value. The `tbytes` value reported by `FSSTAT` will be `maxFsStatBytes`. The value of `fbytes` and `abytes` will be `maxFsStatBytes` minus the metered size of the file system. If the metered size is larger than `maxFsStatBytes`, then `fbytes` and `abytes` will both be '0'.""")
@cli_util.option('--max-fs-stat-files', type=click.INT, help=u"""Controls the maximum `ffiles`, `ffiles`, and `afiles` values reported by `NFS FSSTAT` calls through any associated mount targets. This is an advanced feature. For most applications, use the default value. The `tfiles` value reported by `FSSTAT` will be `maxFsStatFiles`. The value of `ffiles` and `afiles` will be `maxFsStatFiles` minus the metered size of the file system. If the metered size is larger than `maxFsStatFiles`, then `ffiles` and `afiles` will both be '0'.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'ExportSet'})
@cli_util.wrap_exceptions
def update_export_set(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, export_set_id, display_name, max_fs_stat_bytes, max_fs_stat_files, if_match):

    if isinstance(export_set_id, six.string_types) and len(export_set_id.strip()) == 0:
        raise click.UsageError('Parameter --export-set-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if max_fs_stat_bytes is not None:
        _details['maxFsStatBytes'] = max_fs_stat_bytes

    if max_fs_stat_files is not None:
        _details['maxFsStatFiles'] = max_fs_stat_files

    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.update_export_set(
        export_set_id=export_set_id,
        update_export_set_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_export_set') and callable(getattr(client, 'get_export_set')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_export_set(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@file_system_group.command(name=cli_util.override('fs.update_file_system.command_name', 'update'), help=u"""Updates the specified file system's information. You can use this operation to rename a file system.""")
@cli_util.option('--file-system-id', required=True, help=u"""The OCID of the file system.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.

Example: `My file system`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair  with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""The OCID of the Key Management master encryption key to associate with the specified file system. If this value is empty, the Update operation will remove the associated key, if there is one, from the file system. (The file system will continue to be encrypted, but with an encryption key managed by Oracle.)

If updating to a new Key Management key, the old key must remain enabled so that files previously encrypted continue to be accessible. For more information, see [Overview of Key Management].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'file_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'file_storage', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'file_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'file_storage', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'file_storage', 'class': 'FileSystem'})
@cli_util.wrap_exceptions
def update_file_system(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, file_system_id, display_name, freeform_tags, defined_tags, kms_key_id, if_match):

    if isinstance(file_system_id, six.string_types) and len(file_system_id.strip()) == 0:
        raise click.UsageError('Parameter --file-system-id cannot be whitespace or empty string')
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

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.update_file_system(
        file_system_id=file_system_id,
        update_file_system_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_file_system') and callable(getattr(client, 'get_file_system')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_file_system(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@mount_target_group.command(name=cli_util.override('fs.update_mount_target.command_name', 'update'), help=u"""Updates the specified mount target's information.""")
@cli_util.option('--mount-target-id', required=True, help=u"""The OCID of the mount target.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it is changeable. Avoid entering confidential information.

Example: `My mount target`""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of Network Security Group [OCIDs] associated with this mount target. A maximum of 5 is allowed. Setting this to an empty array after the list is created removes the mount target from all NSGs. For more information about NSGs, see [Security Rules].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair  with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nsg-ids': {'module': 'file_storage', 'class': 'list[string]'}, 'freeform-tags': {'module': 'file_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'file_storage', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'file_storage', 'class': 'list[string]'}, 'freeform-tags': {'module': 'file_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'file_storage', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'file_storage', 'class': 'MountTarget'})
@cli_util.wrap_exceptions
def update_mount_target(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, mount_target_id, display_name, nsg_ids, freeform_tags, defined_tags, if_match):

    if isinstance(mount_target_id, six.string_types) and len(mount_target_id.strip()) == 0:
        raise click.UsageError('Parameter --mount-target-id cannot be whitespace or empty string')
    if not force:
        if nsg_ids or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to nsg-ids and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.update_mount_target(
        mount_target_id=mount_target_id,
        update_mount_target_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_mount_target') and callable(getattr(client, 'get_mount_target')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_mount_target(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@snapshot_group.command(name=cli_util.override('fs.update_snapshot.command_name', 'update'), help=u"""Updates the specified snapshot's information.""")
@cli_util.option('--snapshot-id', required=True, help=u"""The OCID of the snapshot.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair  with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'file_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'file_storage', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'file_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'file_storage', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'file_storage', 'class': 'Snapshot'})
@cli_util.wrap_exceptions
def update_snapshot(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, snapshot_id, freeform_tags, defined_tags, if_match):

    if isinstance(snapshot_id, six.string_types) and len(snapshot_id.strip()) == 0:
        raise click.UsageError('Parameter --snapshot-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('file_storage', 'file_storage', ctx)
    result = client.update_snapshot(
        snapshot_id=snapshot_id,
        update_snapshot_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_snapshot') and callable(getattr(client, 'get_snapshot')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_snapshot(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
