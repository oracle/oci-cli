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
from services.core.src.oci_cli_core.generated import core_service_cli


@click.command(cli_util.override('compute.compute_root_group.command_name', 'compute'), cls=CommandGroupWithAlias, help=cli_util.override('compute.compute_root_group.help', """API covering the [Networking],
[Compute], and
[Block Volume] services. Use this API
to manage resources such as virtual cloud networks (VCNs), compute instances, and
block storage volumes."""), short_help=cli_util.override('compute.compute_root_group.short_help', """Core Services API"""))
@cli_util.help_option_group
def compute_root_group():
    pass


@click.command(cli_util.override('compute.dedicated_vm_host_group.command_name', 'dedicated-vm-host'), cls=CommandGroupWithAlias, help="""A dedicated virtual machine host that enables you to host multiple VM instances on a dedicated host that is not shared with other tenancies.""")
@cli_util.help_option_group
def dedicated_vm_host_group():
    pass


@click.command(cli_util.override('compute.image_group.command_name', 'image'), cls=CommandGroupWithAlias, help="""A boot disk image for launching an instance. For more information, see [Overview of the Compute Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def image_group():
    pass


@click.command(cli_util.override('compute.instance_group.command_name', 'instance'), cls=CommandGroupWithAlias, help="""A compute host. The image used to launch the instance determines its operating system and other software. The shape specified during the launch process determines the number of CPUs and memory allocated to the instance. For more information, see [Overview of the Compute Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def instance_group():
    pass


@click.command(cli_util.override('compute.shape_group.command_name', 'shape'), cls=CommandGroupWithAlias, help="""A compute instance shape that can be used in [LaunchInstance]. For more information, see [Overview of the Compute Service] and [Compute Shapes].""")
@cli_util.help_option_group
def shape_group():
    pass


@click.command(cli_util.override('compute.compute_image_capability_schema_group.command_name', 'compute-image-capability-schema'), cls=CommandGroupWithAlias, help="""Compute Image Capability Schema is a set of capabilities that filter the compute global capability schema version for an image.""")
@cli_util.help_option_group
def compute_image_capability_schema_group():
    pass


@click.command(cli_util.override('compute.vnic_attachment_group.command_name', 'vnic-attachment'), cls=CommandGroupWithAlias, help="""Represents an attachment between a VNIC and an instance. For more information, see [Virtual Network Interface Cards (VNICs)].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def vnic_attachment_group():
    pass


@click.command(cli_util.override('compute.volume_attachment_group.command_name', 'volume-attachment'), cls=CommandGroupWithAlias, help="""A base object for all types of attachments between a storage volume and an instance. For specific details about iSCSI attachments, see [IScsiVolumeAttachment Reference].

For general information about volume attachments, see [Overview of Block Volume Storage].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def volume_attachment_group():
    pass


@click.command(cli_util.override('compute.app_catalog_listing_resource_version_group.command_name', 'app-catalog-listing-resource-version'), cls=CommandGroupWithAlias, help="""Listing Resource Version""")
@cli_util.help_option_group
def app_catalog_listing_resource_version_group():
    pass


@click.command(cli_util.override('compute.dedicated_vm_host_instance_group.command_name', 'dedicated-vm-host-instance'), cls=CommandGroupWithAlias, help="""Condensed instance data when listing instances on a dedicated VM host.""")
@cli_util.help_option_group
def dedicated_vm_host_instance_group():
    pass


@click.command(cli_util.override('compute.image_shape_compatibility_entry_group.command_name', 'image-shape-compatibility-entry'), cls=CommandGroupWithAlias, help="""An image and shape that are compatible.""")
@cli_util.help_option_group
def image_shape_compatibility_entry_group():
    pass


@click.command(cli_util.override('compute.app_catalog_listing_group.command_name', 'app-catalog-listing'), cls=CommandGroupWithAlias, help="""Listing details.""")
@cli_util.help_option_group
def app_catalog_listing_group():
    pass


@click.command(cli_util.override('compute.app_catalog_subscription_group.command_name', 'app-catalog-subscription'), cls=CommandGroupWithAlias, help="""a subscription for a listing resource version.""")
@cli_util.help_option_group
def app_catalog_subscription_group():
    pass


@click.command(cli_util.override('compute.boot_volume_attachment_group.command_name', 'boot-volume-attachment'), cls=CommandGroupWithAlias, help="""Represents an attachment between a boot volume and an instance.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def boot_volume_attachment_group():
    pass


@click.command(cli_util.override('compute.instance_console_connection_group.command_name', 'instance-console-connection'), cls=CommandGroupWithAlias, help="""The `InstanceConsoleConnection` API provides you with console access to Compute instances, enabling you to troubleshoot malfunctioning instances remotely.

For more information about console access, see [Accessing the Console].""")
@cli_util.help_option_group
def instance_console_connection_group():
    pass


@click.command(cli_util.override('compute.compute_global_image_capability_schema_version_group.command_name', 'compute-global-image-capability-schema-version'), cls=CommandGroupWithAlias, help="""Compute Global Image Capability Schema Version is a set of all possible capabilities for a collection of images.""")
@cli_util.help_option_group
def compute_global_image_capability_schema_version_group():
    pass


@click.command(cli_util.override('compute.dedicated_vm_host_instance_shape_group.command_name', 'dedicated-vm-host-instance-shape'), cls=CommandGroupWithAlias, help="""The shape used to launch instances associated with the dedicated VM host.""")
@cli_util.help_option_group
def dedicated_vm_host_instance_shape_group():
    pass


@click.command(cli_util.override('compute.volume_group.command_name', 'volume'), cls=CommandGroupWithAlias, help="""A detachable block volume device that allows you to dynamically expand the storage capacity of an instance. For more information, see [Overview of Cloud Volume Storage].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def volume_group():
    pass


@click.command(cli_util.override('compute.compute_global_image_capability_schema_group.command_name', 'compute-global-image-capability-schema'), cls=CommandGroupWithAlias, help="""Compute Global Image Capability Schema is a container for a set of compute global image capability schema versions""")
@cli_util.help_option_group
def compute_global_image_capability_schema_group():
    pass


@click.command(cli_util.override('compute.instance_credentials_group.command_name', 'instance-credentials'), cls=CommandGroupWithAlias, help="""The credentials for a particular instance.""")
@cli_util.help_option_group
def instance_credentials_group():
    pass


@click.command(cli_util.override('compute.boot_volume_group.command_name', 'boot-volume'), cls=CommandGroupWithAlias, help="""A detachable boot volume device that contains the image used to boot a Compute instance. For more information, see [Overview of Boot Volumes].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def boot_volume_group():
    pass


@click.command(cli_util.override('compute.dedicated_vm_host_shape_group.command_name', 'dedicated-vm-host-shape'), cls=CommandGroupWithAlias, help="""The shape used to launch the dedicated virtual machine (VM) host.""")
@cli_util.help_option_group
def dedicated_vm_host_shape_group():
    pass


@click.command(cli_util.override('compute.app_catalog_listing_resource_version_agreements_group.command_name', 'app-catalog-listing-resource-version-agreements'), cls=CommandGroupWithAlias, help="""Agreements for a listing resource version.""")
@cli_util.help_option_group
def app_catalog_listing_resource_version_agreements_group():
    pass


@click.command(cli_util.override('compute.device_group.command_name', 'device'), cls=CommandGroupWithAlias, help="""Device Path corresponding to the block devices attached to instances having a name and isAvailable flag.""")
@cli_util.help_option_group
def device_group():
    pass


@click.command(cli_util.override('compute.console_history_group.command_name', 'console-history'), cls=CommandGroupWithAlias, help="""An instance's serial console data. It includes configuration messages that occur when the instance boots, such as kernel and BIOS messages, and is useful for checking the status of the instance or diagnosing problems. The console data is minimally formatted ASCII text.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def console_history_group():
    pass


core_service_cli.core_service_group.add_command(compute_root_group)
compute_root_group.add_command(dedicated_vm_host_group)
compute_root_group.add_command(image_group)
compute_root_group.add_command(instance_group)
compute_root_group.add_command(shape_group)
compute_root_group.add_command(compute_image_capability_schema_group)
compute_root_group.add_command(vnic_attachment_group)
compute_root_group.add_command(volume_attachment_group)
compute_root_group.add_command(app_catalog_listing_resource_version_group)
compute_root_group.add_command(dedicated_vm_host_instance_group)
compute_root_group.add_command(image_shape_compatibility_entry_group)
compute_root_group.add_command(app_catalog_listing_group)
compute_root_group.add_command(app_catalog_subscription_group)
compute_root_group.add_command(boot_volume_attachment_group)
compute_root_group.add_command(instance_console_connection_group)
compute_root_group.add_command(compute_global_image_capability_schema_version_group)
compute_root_group.add_command(dedicated_vm_host_instance_shape_group)
compute_root_group.add_command(volume_group)
compute_root_group.add_command(compute_global_image_capability_schema_group)
compute_root_group.add_command(instance_credentials_group)
compute_root_group.add_command(boot_volume_group)
compute_root_group.add_command(dedicated_vm_host_shape_group)
compute_root_group.add_command(app_catalog_listing_resource_version_agreements_group)
compute_root_group.add_command(device_group)
compute_root_group.add_command(console_history_group)


@image_shape_compatibility_entry_group.command(name=cli_util.override('compute.add_image_shape_compatibility_entry.command_name', 'add'), help=u"""Adds a shape to the compatible shapes list for the image. \n[Command Reference](addImageShapeCompatibilityEntry)""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the image.""")
@cli_util.option('--shape-name', required=True, help=u"""Shape name.""")
@cli_util.option('--memory-constraints', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ocpu-constraints', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'memory-constraints': {'module': 'core', 'class': 'ImageMemoryConstraints'}, 'ocpu-constraints': {'module': 'core', 'class': 'ImageOcpuConstraints'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'memory-constraints': {'module': 'core', 'class': 'ImageMemoryConstraints'}, 'ocpu-constraints': {'module': 'core', 'class': 'ImageOcpuConstraints'}}, output_type={'module': 'core', 'class': 'ImageShapeCompatibilityEntry'})
@cli_util.wrap_exceptions
def add_image_shape_compatibility_entry(ctx, from_json, force, image_id, shape_name, memory_constraints, ocpu_constraints):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')

    if isinstance(shape_name, six.string_types) and len(shape_name.strip()) == 0:
        raise click.UsageError('Parameter --shape-name cannot be whitespace or empty string')
    if not force:
        if memory_constraints or ocpu_constraints:
            if not click.confirm("WARNING: Updates to memory-constraints and ocpu-constraints will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}

    _details = {}

    if memory_constraints is not None:
        _details['memoryConstraints'] = cli_util.parse_json_parameter("memory_constraints", memory_constraints)

    if ocpu_constraints is not None:
        _details['ocpuConstraints'] = cli_util.parse_json_parameter("ocpu_constraints", ocpu_constraints)

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.add_image_shape_compatibility_entry(
        image_id=image_id,
        shape_name=shape_name,
        add_image_shape_compatibility_entry_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@boot_volume_attachment_group.command(name=cli_util.override('compute.attach_boot_volume.command_name', 'attach'), help=u"""Attaches the specified boot volume to the specified instance. \n[Command Reference](attachBootVolume)""")
@cli_util.option('--boot-volume-id', required=True, help=u"""The OCID of the  boot volume.""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'BootVolumeAttachment'})
@cli_util.wrap_exceptions
def attach_boot_volume(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, boot_volume_id, instance_id, display_name):

    kwargs = {}

    _details = {}
    _details['bootVolumeId'] = boot_volume_id
    _details['instanceId'] = instance_id

    if display_name is not None:
        _details['displayName'] = display_name

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.attach_boot_volume(
        attach_boot_volume_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_boot_volume_attachment') and callable(getattr(client, 'get_boot_volume_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_boot_volume_attachment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@vnic_attachment_group.command(name=cli_util.override('compute.attach_vnic.command_name', 'attach'), help=u"""Creates a secondary VNIC and attaches it to the specified instance. For more information about secondary VNICs, see [Virtual Network Interface Cards (VNICs)]. \n[Command Reference](attachVnic)""")
@cli_util.option('--create-vnic-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Details for creating a new VNIC.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.""")
@cli_util.option('--nic-index', type=click.INT, help=u"""Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)].""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'create-vnic-details': {'module': 'core', 'class': 'CreateVnicDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'create-vnic-details': {'module': 'core', 'class': 'CreateVnicDetails'}}, output_type={'module': 'core', 'class': 'VnicAttachment'})
@cli_util.wrap_exceptions
def attach_vnic(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, create_vnic_details, instance_id, display_name, nic_index):

    kwargs = {}

    _details = {}
    _details['createVnicDetails'] = cli_util.parse_json_parameter("create_vnic_details", create_vnic_details)
    _details['instanceId'] = instance_id

    if display_name is not None:
        _details['displayName'] = display_name

    if nic_index is not None:
        _details['nicIndex'] = nic_index

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.attach_vnic(
        attach_vnic_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vnic_attachment') and callable(getattr(client, 'get_vnic_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vnic_attachment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@volume_attachment_group.command(name=cli_util.override('compute.attach_volume.command_name', 'attach'), help=u"""Attaches the specified storage volume to the specified instance. \n[Command Reference](attachVolume)""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@cli_util.option('--type', required=True, help=u"""The type of volume. The only supported values are \"iscsi\" and \"paravirtualized\".""")
@cli_util.option('--volume-id', required=True, help=u"""The OCID of the volume.""")
@cli_util.option('--device', help=u"""The device name.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.""")
@cli_util.option('--is-read-only', type=click.BOOL, help=u"""Whether the attachment was created in read-only mode.""")
@cli_util.option('--is-shareable', type=click.BOOL, help=u"""Whether the attachment should be created in shareable mode. If an attachment is created in shareable mode, then other instances can attach the same volume, provided that they also create their attachments in shareable mode. Only certain volume types can be attached in shareable mode. Defaults to false if not specified.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeAttachment'})
@cli_util.wrap_exceptions
def attach_volume(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_id, type, volume_id, device, display_name, is_read_only, is_shareable):

    kwargs = {}

    _details = {}
    _details['instanceId'] = instance_id
    _details['type'] = type
    _details['volumeId'] = volume_id

    if device is not None:
        _details['device'] = device

    if display_name is not None:
        _details['displayName'] = display_name

    if is_read_only is not None:
        _details['isReadOnly'] = is_read_only

    if is_shareable is not None:
        _details['isShareable'] = is_shareable

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.attach_volume(
        attach_volume_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_volume_attachment') and callable(getattr(client, 'get_volume_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_volume_attachment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@volume_attachment_group.command(name=cli_util.override('compute.attach_volume_attach_service_determined_volume_details.command_name', 'attach-volume-attach-service-determined-volume-details'), help=u"""Attaches the specified storage volume to the specified instance. \n[Command Reference](attachVolume)""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@cli_util.option('--volume-id', required=True, help=u"""The OCID of the volume.""")
@cli_util.option('--device', help=u"""The device name.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.""")
@cli_util.option('--is-read-only', type=click.BOOL, help=u"""Whether the attachment was created in read-only mode.""")
@cli_util.option('--is-shareable', type=click.BOOL, help=u"""Whether the attachment should be created in shareable mode. If an attachment is created in shareable mode, then other instances can attach the same volume, provided that they also create their attachments in shareable mode. Only certain volume types can be attached in shareable mode. Defaults to false if not specified.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeAttachment'})
@cli_util.wrap_exceptions
def attach_volume_attach_service_determined_volume_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_id, volume_id, device, display_name, is_read_only, is_shareable):

    kwargs = {}

    _details = {}
    _details['instanceId'] = instance_id
    _details['volumeId'] = volume_id

    if device is not None:
        _details['device'] = device

    if display_name is not None:
        _details['displayName'] = display_name

    if is_read_only is not None:
        _details['isReadOnly'] = is_read_only

    if is_shareable is not None:
        _details['isShareable'] = is_shareable

    _details['type'] = 'service_determined'

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.attach_volume(
        attach_volume_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_volume_attachment') and callable(getattr(client, 'get_volume_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_volume_attachment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@volume_attachment_group.command(name=cli_util.override('compute.attach_volume_attach_emulated_volume_details.command_name', 'attach-volume-attach-emulated-volume-details'), help=u"""Attaches the specified storage volume to the specified instance. \n[Command Reference](attachVolume)""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@cli_util.option('--volume-id', required=True, help=u"""The OCID of the volume.""")
@cli_util.option('--device', help=u"""The device name.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.""")
@cli_util.option('--is-read-only', type=click.BOOL, help=u"""Whether the attachment was created in read-only mode.""")
@cli_util.option('--is-shareable', type=click.BOOL, help=u"""Whether the attachment should be created in shareable mode. If an attachment is created in shareable mode, then other instances can attach the same volume, provided that they also create their attachments in shareable mode. Only certain volume types can be attached in shareable mode. Defaults to false if not specified.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeAttachment'})
@cli_util.wrap_exceptions
def attach_volume_attach_emulated_volume_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_id, volume_id, device, display_name, is_read_only, is_shareable):

    kwargs = {}

    _details = {}
    _details['instanceId'] = instance_id
    _details['volumeId'] = volume_id

    if device is not None:
        _details['device'] = device

    if display_name is not None:
        _details['displayName'] = display_name

    if is_read_only is not None:
        _details['isReadOnly'] = is_read_only

    if is_shareable is not None:
        _details['isShareable'] = is_shareable

    _details['type'] = 'emulated'

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.attach_volume(
        attach_volume_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_volume_attachment') and callable(getattr(client, 'get_volume_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_volume_attachment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@volume_attachment_group.command(name=cli_util.override('compute.attach_volume_attach_i_scsi_volume_details.command_name', 'attach-volume-attach-i-scsi-volume-details'), help=u"""Attaches the specified storage volume to the specified instance. \n[Command Reference](attachVolume)""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@cli_util.option('--volume-id', required=True, help=u"""The OCID of the volume.""")
@cli_util.option('--device', help=u"""The device name.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.""")
@cli_util.option('--is-read-only', type=click.BOOL, help=u"""Whether the attachment was created in read-only mode.""")
@cli_util.option('--is-shareable', type=click.BOOL, help=u"""Whether the attachment should be created in shareable mode. If an attachment is created in shareable mode, then other instances can attach the same volume, provided that they also create their attachments in shareable mode. Only certain volume types can be attached in shareable mode. Defaults to false if not specified.""")
@cli_util.option('--use-chap', type=click.BOOL, help=u"""Whether to use CHAP authentication for the volume attachment. Defaults to false.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeAttachment'})
@cli_util.wrap_exceptions
def attach_volume_attach_i_scsi_volume_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_id, volume_id, device, display_name, is_read_only, is_shareable, use_chap):

    kwargs = {}

    _details = {}
    _details['instanceId'] = instance_id
    _details['volumeId'] = volume_id

    if device is not None:
        _details['device'] = device

    if display_name is not None:
        _details['displayName'] = display_name

    if is_read_only is not None:
        _details['isReadOnly'] = is_read_only

    if is_shareable is not None:
        _details['isShareable'] = is_shareable

    if use_chap is not None:
        _details['useChap'] = use_chap

    _details['type'] = 'iscsi'

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.attach_volume(
        attach_volume_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_volume_attachment') and callable(getattr(client, 'get_volume_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_volume_attachment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@volume_attachment_group.command(name=cli_util.override('compute.attach_volume_attach_paravirtualized_volume_details.command_name', 'attach-volume-attach-paravirtualized-volume-details'), help=u"""Attaches the specified storage volume to the specified instance. \n[Command Reference](attachVolume)""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@cli_util.option('--volume-id', required=True, help=u"""The OCID of the volume.""")
@cli_util.option('--device', help=u"""The device name.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.""")
@cli_util.option('--is-read-only', type=click.BOOL, help=u"""Whether the attachment was created in read-only mode.""")
@cli_util.option('--is-shareable', type=click.BOOL, help=u"""Whether the attachment should be created in shareable mode. If an attachment is created in shareable mode, then other instances can attach the same volume, provided that they also create their attachments in shareable mode. Only certain volume types can be attached in shareable mode. Defaults to false if not specified.""")
@cli_util.option('--is-pv-encryption-in-transit-enabled', type=click.BOOL, help=u"""Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeAttachment'})
@cli_util.wrap_exceptions
def attach_volume_attach_paravirtualized_volume_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_id, volume_id, device, display_name, is_read_only, is_shareable, is_pv_encryption_in_transit_enabled):

    kwargs = {}

    _details = {}
    _details['instanceId'] = instance_id
    _details['volumeId'] = volume_id

    if device is not None:
        _details['device'] = device

    if display_name is not None:
        _details['displayName'] = display_name

    if is_read_only is not None:
        _details['isReadOnly'] = is_read_only

    if is_shareable is not None:
        _details['isShareable'] = is_shareable

    if is_pv_encryption_in_transit_enabled is not None:
        _details['isPvEncryptionInTransitEnabled'] = is_pv_encryption_in_transit_enabled

    _details['type'] = 'paravirtualized'

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.attach_volume(
        attach_volume_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_volume_attachment') and callable(getattr(client, 'get_volume_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_volume_attachment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@console_history_group.command(name=cli_util.override('compute.capture_console_history.command_name', 'capture'), help=u"""Captures the most recent serial console data (up to a megabyte) for the specified instance.

The `CaptureConsoleHistory` operation works with the other console history operations as described below.

1. Use `CaptureConsoleHistory` to request the capture of up to a megabyte of the most recent console history. This call returns a `ConsoleHistory` object. The object will have a state of REQUESTED. 2. Wait for the capture operation to succeed by polling `GetConsoleHistory` with the identifier of the console history metadata. The state of the `ConsoleHistory` object will go from REQUESTED to GETTING-HISTORY and then SUCCEEDED (or FAILED). 3. Use `GetConsoleHistoryContent` to get the actual console history data (not the metadata). 4. Optionally, use `DeleteConsoleHistory` to delete the console history metadata and the console history data. \n[Command Reference](captureConsoleHistory)""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance to get the console history from.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["REQUESTED", "GETTING-HISTORY", "SUCCEEDED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'ConsoleHistory'})
@cli_util.wrap_exceptions
def capture_console_history(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_id, defined_tags, display_name, freeform_tags):

    kwargs = {}

    _details = {}
    _details['instanceId'] = instance_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.capture_console_history(
        capture_console_history_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_console_history') and callable(getattr(client, 'get_console_history')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_console_history(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@compute_image_capability_schema_group.command(name=cli_util.override('compute.change_compute_image_capability_schema_compartment.command_name', 'change-compartment'), help=u"""Moves a compute image capability schema into a different compartment within the same tenancy. For information about moving resources between compartments, see         [Moving Resources to a Different Compartment]. \n[Command Reference](changeComputeImageCapabilitySchemaCompartment)""")
@cli_util.option('--compute-image-capability-schema-id', required=True, help=u"""The id of the compute image capability schema or the image ocid""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the instance configuration to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_compute_image_capability_schema_compartment(ctx, from_json, compute_image_capability_schema_id, compartment_id, if_match):

    if isinstance(compute_image_capability_schema_id, six.string_types) and len(compute_image_capability_schema_id.strip()) == 0:
        raise click.UsageError('Parameter --compute-image-capability-schema-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.change_compute_image_capability_schema_compartment(
        compute_image_capability_schema_id=compute_image_capability_schema_id,
        change_compute_image_capability_schema_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dedicated_vm_host_group.command(name=cli_util.override('compute.change_dedicated_vm_host_compartment.command_name', 'change-compartment'), help=u"""Moves a dedicated virtual machine host from one compartment to another. \n[Command Reference](changeDedicatedVmHostCompartment)""")
@cli_util.option('--dedicated-vm-host-id', required=True, help=u"""The OCID of the dedicated VM host.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the dedicated virtual machine host to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_dedicated_vm_host_compartment(ctx, from_json, dedicated_vm_host_id, compartment_id, if_match):

    if isinstance(dedicated_vm_host_id, six.string_types) and len(dedicated_vm_host_id.strip()) == 0:
        raise click.UsageError('Parameter --dedicated-vm-host-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.change_dedicated_vm_host_compartment(
        dedicated_vm_host_id=dedicated_vm_host_id,
        change_dedicated_vm_host_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@image_group.command(name=cli_util.override('compute.change_image_compartment.command_name', 'change-compartment'), help=u"""Moves an image into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeImageCompartment)""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the image.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the image to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_image_compartment(ctx, from_json, image_id, compartment_id, if_match):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.change_image_compartment(
        image_id=image_id,
        change_image_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_group.command(name=cli_util.override('compute.change_instance_compartment.command_name', 'change-compartment'), help=u"""Moves an instance into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].

When you move an instance to a different compartment, associated resources such as boot volumes and VNICs are not moved. \n[Command Reference](changeInstanceCompartment)""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the instance to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_instance_compartment(ctx, from_json, instance_id, compartment_id, if_match):

    if isinstance(instance_id, six.string_types) and len(instance_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.change_instance_compartment(
        instance_id=instance_id,
        change_instance_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@app_catalog_subscription_group.command(name=cli_util.override('compute.create_app_catalog_subscription.command_name', 'create'), help=u"""Create a subscription for listing resource version for a compartment. It will take some time to propagate to all regions. \n[Command Reference](createAppCatalogSubscription)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartmentID for the subscription.""")
@cli_util.option('--listing-id', required=True, help=u"""The OCID of the listing.""")
@cli_util.option('--listing-resource-version', required=True, help=u"""Listing resource version.""")
@cli_util.option('--oracle-terms-of-use-link', required=True, help=u"""Oracle TOU link""")
@cli_util.option('--time-retrieved', required=True, type=custom_types.CLI_DATETIME, help=u"""Date and time the agreements were retrieved, in [RFC3339] format. Example: `2018-03-20T12:32:53.532Z`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--signature', required=True, help=u"""A generated signature for this listing resource version retrieved the agreements API.""")
@cli_util.option('--eula-link', help=u"""EULA link""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'AppCatalogSubscription'})
@cli_util.wrap_exceptions
def create_app_catalog_subscription(ctx, from_json, compartment_id, listing_id, listing_resource_version, oracle_terms_of_use_link, time_retrieved, signature, eula_link):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['listingId'] = listing_id
    _details['listingResourceVersion'] = listing_resource_version
    _details['oracleTermsOfUseLink'] = oracle_terms_of_use_link
    _details['timeRetrieved'] = time_retrieved
    _details['signature'] = signature

    if eula_link is not None:
        _details['eulaLink'] = eula_link

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.create_app_catalog_subscription(
        create_app_catalog_subscription_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@compute_image_capability_schema_group.command(name=cli_util.override('compute.create_compute_image_capability_schema.command_name', 'create'), help=u"""Creates compute image capability schema. \n[Command Reference](createComputeImageCapabilitySchema)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the resource.""")
@cli_util.option('--compute-global-image-capability-schema-version-name', required=True, help=u"""The name of the compute global image capability schema version""")
@cli_util.option('--image-id', required=True, help=u"""The ocid of the image""")
@cli_util.option('--schema-data', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The map of each capability name to its ImageCapabilitySchemaDescriptor.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the compute image capability schema""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'schema-data': {'module': 'core', 'class': 'dict(str, ImageCapabilitySchemaDescriptor)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'schema-data': {'module': 'core', 'class': 'dict(str, ImageCapabilitySchemaDescriptor)'}}, output_type={'module': 'core', 'class': 'ComputeImageCapabilitySchema'})
@cli_util.wrap_exceptions
def create_compute_image_capability_schema(ctx, from_json, compartment_id, compute_global_image_capability_schema_version_name, image_id, schema_data, freeform_tags, display_name, defined_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['computeGlobalImageCapabilitySchemaVersionName'] = compute_global_image_capability_schema_version_name
    _details['imageId'] = image_id
    _details['schemaData'] = cli_util.parse_json_parameter("schema_data", schema_data)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.create_compute_image_capability_schema(
        create_compute_image_capability_schema_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dedicated_vm_host_group.command(name=cli_util.override('compute.create_dedicated_vm_host.command_name', 'create'), help=u"""Creates a new dedicated virtual machine host in the specified compartment and the specified availability domain. Dedicated virtual machine hosts enable you to run your Compute virtual machine (VM) instances on dedicated servers that are a single tenant and not shared with other customers. For more information, see [Dedicated Virtual Machine Hosts]. \n[Command Reference](createDedicatedVmHost)""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain of the dedicated virtual machine host.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--dedicated-vm-host-shape', required=True, help=u"""The dedicated virtual machine host shape. The shape determines the number of CPUs and other resources available for VM instances launched on the dedicated virtual machine host.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

Example: `My dedicated VM host`""")
@cli_util.option('--fault-domain', help=u"""The fault domain for the dedicated virtual machine host's assigned instances. For more information, see [Fault Domains]. If you do not specify the fault domain, the system selects one for you. To change the fault domain for a dedicated virtual machine host, delete it and create a new dedicated virtual machine host in the preferred fault domain.

To get a list of fault domains, use the `ListFaultDomains` operation in the [Identity and Access Management Service API].

Example: `FAULT-DOMAIN-1`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'DedicatedVmHost'})
@cli_util.wrap_exceptions
def create_dedicated_vm_host(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, dedicated_vm_host_shape, defined_tags, display_name, fault_domain, freeform_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id
    _details['dedicatedVmHostShape'] = dedicated_vm_host_shape

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if fault_domain is not None:
        _details['faultDomain'] = fault_domain

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.create_dedicated_vm_host(
        create_dedicated_vm_host_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dedicated_vm_host') and callable(getattr(client, 'get_dedicated_vm_host')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_dedicated_vm_host(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@image_group.command(name=cli_util.override('compute.create_image.command_name', 'create'), help=u"""Creates a boot disk image for the specified instance or imports an exported image from the Oracle Cloud Infrastructure Object Storage service.

When creating a new image, you must provide the OCID of the instance you want to use as the basis for the image, and the OCID of the compartment containing that instance. For more information about images, see [Managing Custom Images].

When importing an exported image from Object Storage, you specify the source information in [ImageSourceDetails].

When importing an image based on the namespace, bucket name, and object name, use [ImageSourceViaObjectStorageTupleDetails].

When importing an image based on the Object Storage URL, use [ImageSourceViaObjectStorageUriDetails]. See [Object Storage URLs] and [Using Pre-Authenticated Requests] for constructing URLs for image import/export.

For more information about importing exported images, see [Image Import/Export].

You may optionally specify a *display name* for the image, which is simply a friendly name or description. It does not have to be unique, and you can change it. See [UpdateImage]. Avoid entering confidential information. \n[Command Reference](createImage)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment you want the image to be created in.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the image. It does not have to be unique, and it's changeable. Avoid entering confidential information.

You cannot use an Oracle-provided image name as a custom image name.

Example: `My Oracle Linux image`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--image-source-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Details for creating an image through import""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--instance-id', help=u"""The OCID of the instance you want to use as the basis for the image.""")
@cli_util.option('--launch-mode', type=custom_types.CliCaseInsensitiveChoice(["NATIVE", "EMULATED", "PARAVIRTUALIZED", "CUSTOM"]), help=u"""Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are: * `NATIVE` - VM instances launch with paravirtualized boot and VFIO devices. The default value for Oracle-provided images. * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers. * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'image-source-details': {'module': 'core', 'class': 'ImageSourceDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'image-source-details': {'module': 'core', 'class': 'ImageSourceDetails'}}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def create_image(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, defined_tags, display_name, freeform_tags, image_source_details, instance_id, launch_mode):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if image_source_details is not None:
        _details['imageSourceDetails'] = cli_util.parse_json_parameter("image_source_details", image_source_details)

    if instance_id is not None:
        _details['instanceId'] = instance_id

    if launch_mode is not None:
        _details['launchMode'] = launch_mode

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.create_image(
        create_image_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_image') and callable(getattr(client, 'get_image')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_image(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@image_group.command(name=cli_util.override('compute.create_image_image_source_via_object_storage_tuple_details.command_name', 'create-image-image-source-via-object-storage-tuple-details'), help=u"""Creates a boot disk image for the specified instance or imports an exported image from the Oracle Cloud Infrastructure Object Storage service.

When creating a new image, you must provide the OCID of the instance you want to use as the basis for the image, and the OCID of the compartment containing that instance. For more information about images, see [Managing Custom Images].

When importing an exported image from Object Storage, you specify the source information in [ImageSourceDetails].

When importing an image based on the namespace, bucket name, and object name, use [ImageSourceViaObjectStorageTupleDetails].

When importing an image based on the Object Storage URL, use [ImageSourceViaObjectStorageUriDetails]. See [Object Storage URLs] and [Using Pre-Authenticated Requests] for constructing URLs for image import/export.

For more information about importing exported images, see [Image Import/Export].

You may optionally specify a *display name* for the image, which is simply a friendly name or description. It does not have to be unique, and you can change it. See [UpdateImage]. Avoid entering confidential information. \n[Command Reference](createImage)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment you want the image to be created in.""")
@cli_util.option('--image-source-details-bucket-name', required=True, help=u"""The Object Storage bucket for the image.""")
@cli_util.option('--image-source-details-namespace-name', required=True, help=u"""The Object Storage namespace for the image.""")
@cli_util.option('--image-source-details-object-name', required=True, help=u"""The Object Storage name for the image.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the image. It does not have to be unique, and it's changeable. Avoid entering confidential information.

You cannot use an Oracle-provided image name as a custom image name.

Example: `My Oracle Linux image`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--instance-id', help=u"""The OCID of the instance you want to use as the basis for the image.""")
@cli_util.option('--launch-mode', type=custom_types.CliCaseInsensitiveChoice(["NATIVE", "EMULATED", "PARAVIRTUALIZED", "CUSTOM"]), help=u"""Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are: * `NATIVE` - VM instances launch with paravirtualized boot and VFIO devices. The default value for Oracle-provided images. * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers. * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.""")
@cli_util.option('--image-source-details-operating-system', help=u"""""")
@cli_util.option('--image-source-details-operating-system-version', help=u"""""")
@cli_util.option('--image-source-details-source-image-type', type=custom_types.CliCaseInsensitiveChoice(["QCOW2", "VMDK"]), help=u"""The format of the image to be imported.  Only monolithic images are supported. This attribute is not used for exported Oracle images with the OCI image format.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def create_image_image_source_via_object_storage_tuple_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, image_source_details_bucket_name, image_source_details_namespace_name, image_source_details_object_name, defined_tags, display_name, freeform_tags, instance_id, launch_mode, image_source_details_operating_system, image_source_details_operating_system_version, image_source_details_source_image_type):

    kwargs = {}

    _details = {}
    _details['imageSourceDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['imageSourceDetails']['bucketName'] = image_source_details_bucket_name
    _details['imageSourceDetails']['namespaceName'] = image_source_details_namespace_name
    _details['imageSourceDetails']['objectName'] = image_source_details_object_name

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if instance_id is not None:
        _details['instanceId'] = instance_id

    if launch_mode is not None:
        _details['launchMode'] = launch_mode

    if image_source_details_operating_system is not None:
        _details['imageSourceDetails']['operatingSystem'] = image_source_details_operating_system

    if image_source_details_operating_system_version is not None:
        _details['imageSourceDetails']['operatingSystemVersion'] = image_source_details_operating_system_version

    if image_source_details_source_image_type is not None:
        _details['imageSourceDetails']['sourceImageType'] = image_source_details_source_image_type

    _details['imageSourceDetails']['sourceType'] = 'objectStorageTuple'

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.create_image(
        create_image_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_image') and callable(getattr(client, 'get_image')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_image(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@image_group.command(name=cli_util.override('compute.create_image_image_source_via_object_storage_uri_details.command_name', 'create-image-image-source-via-object-storage-uri-details'), help=u"""Creates a boot disk image for the specified instance or imports an exported image from the Oracle Cloud Infrastructure Object Storage service.

When creating a new image, you must provide the OCID of the instance you want to use as the basis for the image, and the OCID of the compartment containing that instance. For more information about images, see [Managing Custom Images].

When importing an exported image from Object Storage, you specify the source information in [ImageSourceDetails].

When importing an image based on the namespace, bucket name, and object name, use [ImageSourceViaObjectStorageTupleDetails].

When importing an image based on the Object Storage URL, use [ImageSourceViaObjectStorageUriDetails]. See [Object Storage URLs] and [Using Pre-Authenticated Requests] for constructing URLs for image import/export.

For more information about importing exported images, see [Image Import/Export].

You may optionally specify a *display name* for the image, which is simply a friendly name or description. It does not have to be unique, and you can change it. See [UpdateImage]. Avoid entering confidential information. \n[Command Reference](createImage)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment you want the image to be created in.""")
@cli_util.option('--image-source-details-source-uri', required=True, help=u"""The Object Storage URL for the image.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the image. It does not have to be unique, and it's changeable. Avoid entering confidential information.

You cannot use an Oracle-provided image name as a custom image name.

Example: `My Oracle Linux image`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--instance-id', help=u"""The OCID of the instance you want to use as the basis for the image.""")
@cli_util.option('--launch-mode', type=custom_types.CliCaseInsensitiveChoice(["NATIVE", "EMULATED", "PARAVIRTUALIZED", "CUSTOM"]), help=u"""Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are: * `NATIVE` - VM instances launch with paravirtualized boot and VFIO devices. The default value for Oracle-provided images. * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers. * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.""")
@cli_util.option('--image-source-details-operating-system', help=u"""""")
@cli_util.option('--image-source-details-operating-system-version', help=u"""""")
@cli_util.option('--image-source-details-source-image-type', type=custom_types.CliCaseInsensitiveChoice(["QCOW2", "VMDK"]), help=u"""The format of the image to be imported.  Only monolithic images are supported. This attribute is not used for exported Oracle images with the OCI image format.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def create_image_image_source_via_object_storage_uri_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, image_source_details_source_uri, defined_tags, display_name, freeform_tags, instance_id, launch_mode, image_source_details_operating_system, image_source_details_operating_system_version, image_source_details_source_image_type):

    kwargs = {}

    _details = {}
    _details['imageSourceDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['imageSourceDetails']['sourceUri'] = image_source_details_source_uri

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if instance_id is not None:
        _details['instanceId'] = instance_id

    if launch_mode is not None:
        _details['launchMode'] = launch_mode

    if image_source_details_operating_system is not None:
        _details['imageSourceDetails']['operatingSystem'] = image_source_details_operating_system

    if image_source_details_operating_system_version is not None:
        _details['imageSourceDetails']['operatingSystemVersion'] = image_source_details_operating_system_version

    if image_source_details_source_image_type is not None:
        _details['imageSourceDetails']['sourceImageType'] = image_source_details_source_image_type

    _details['imageSourceDetails']['sourceType'] = 'objectStorageUri'

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.create_image(
        create_image_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_image') and callable(getattr(client, 'get_image')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_image(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@instance_console_connection_group.command(name=cli_util.override('compute.create_instance_console_connection.command_name', 'create'), help=u"""Creates a new console connection to the specified instance. After the console connection has been created and is available, you connect to the console using SSH.

For more information about console access, see [Accessing the Console]. \n[Command Reference](createInstanceConsoleConnection)""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance to create the console connection to.""")
@cli_util.option('--public-key', required=True, help=u"""The SSH public key used to authenticate the console connection.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'InstanceConsoleConnection'})
@cli_util.wrap_exceptions
def create_instance_console_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_id, public_key, defined_tags, freeform_tags):

    kwargs = {}

    _details = {}
    _details['instanceId'] = instance_id
    _details['publicKey'] = public_key

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.create_instance_console_connection(
        create_instance_console_connection_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_instance_console_connection') and callable(getattr(client, 'get_instance_console_connection')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_instance_console_connection(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@app_catalog_subscription_group.command(name=cli_util.override('compute.delete_app_catalog_subscription.command_name', 'delete'), help=u"""Delete a subscription for a listing resource version for a compartment. \n[Command Reference](deleteAppCatalogSubscription)""")
@cli_util.option('--listing-id', required=True, help=u"""The OCID of the listing.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-version', required=True, help=u"""Listing Resource Version.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_app_catalog_subscription(ctx, from_json, listing_id, compartment_id, resource_version):

    kwargs = {}
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.delete_app_catalog_subscription(
        listing_id=listing_id,
        compartment_id=compartment_id,
        resource_version=resource_version,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@compute_image_capability_schema_group.command(name=cli_util.override('compute.delete_compute_image_capability_schema.command_name', 'delete'), help=u"""Deletes the specified Compute Image Capability Schema \n[Command Reference](deleteComputeImageCapabilitySchema)""")
@cli_util.option('--compute-image-capability-schema-id', required=True, help=u"""The id of the compute image capability schema or the image ocid""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_compute_image_capability_schema(ctx, from_json, compute_image_capability_schema_id, if_match):

    if isinstance(compute_image_capability_schema_id, six.string_types) and len(compute_image_capability_schema_id.strip()) == 0:
        raise click.UsageError('Parameter --compute-image-capability-schema-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.delete_compute_image_capability_schema(
        compute_image_capability_schema_id=compute_image_capability_schema_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@console_history_group.command(name=cli_util.override('compute.delete_console_history.command_name', 'delete'), help=u"""Deletes the specified console history metadata and the console history data. \n[Command Reference](deleteConsoleHistory)""")
@cli_util.option('--instance-console-history-id', required=True, help=u"""The OCID of the console history.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["REQUESTED", "GETTING-HISTORY", "SUCCEEDED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_console_history(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_console_history_id, if_match):

    if isinstance(instance_console_history_id, six.string_types) and len(instance_console_history_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-console-history-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.delete_console_history(
        instance_console_history_id=instance_console_history_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_console_history') and callable(getattr(client, 'get_console_history')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_console_history(instance_console_history_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@dedicated_vm_host_group.command(name=cli_util.override('compute.delete_dedicated_vm_host.command_name', 'delete'), help=u"""Deletes the specified dedicated virtual machine host.

If any VM instances are assigned to the dedicated virtual machine host, the delete operation will fail and the service will return a 409 response code. \n[Command Reference](deleteDedicatedVmHost)""")
@cli_util.option('--dedicated-vm-host-id', required=True, help=u"""The OCID of the dedicated VM host.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_dedicated_vm_host(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dedicated_vm_host_id):

    if isinstance(dedicated_vm_host_id, six.string_types) and len(dedicated_vm_host_id.strip()) == 0:
        raise click.UsageError('Parameter --dedicated-vm-host-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.delete_dedicated_vm_host(
        dedicated_vm_host_id=dedicated_vm_host_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dedicated_vm_host') and callable(getattr(client, 'get_dedicated_vm_host')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_dedicated_vm_host(dedicated_vm_host_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@image_group.command(name=cli_util.override('compute.delete_image.command_name', 'delete'), help=u"""Deletes an image. \n[Command Reference](deleteImage)""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the image.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_image(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, image_id, if_match):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.delete_image(
        image_id=image_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_image') and callable(getattr(client, 'get_image')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_image(image_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@instance_console_connection_group.command(name=cli_util.override('compute.delete_instance_console_connection.command_name', 'delete'), help=u"""Deletes the specified instance console connection. \n[Command Reference](deleteInstanceConsoleConnection)""")
@cli_util.option('--instance-console-connection-id', required=True, help=u"""The OCID of the instance console connection.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_instance_console_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_console_connection_id, if_match):

    if isinstance(instance_console_connection_id, six.string_types) and len(instance_console_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-console-connection-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.delete_instance_console_connection(
        instance_console_connection_id=instance_console_connection_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_instance_console_connection') and callable(getattr(client, 'get_instance_console_connection')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_instance_console_connection(instance_console_connection_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@boot_volume_group.command(name=cli_util.override('compute.detach_boot_volume.command_name', 'detach'), help=u"""Detaches a boot volume from an instance. You must specify the OCID of the boot volume attachment.

This is an asynchronous operation. The attachment's `lifecycleState` will change to DETACHING temporarily until the attachment is completely removed. \n[Command Reference](detachBootVolume)""")
@cli_util.option('--boot-volume-attachment-id', required=True, help=u"""The OCID of the boot volume attachment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def detach_boot_volume(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, boot_volume_attachment_id, if_match):

    if isinstance(boot_volume_attachment_id, six.string_types) and len(boot_volume_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.detach_boot_volume(
        boot_volume_attachment_id=boot_volume_attachment_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_boot_volume_attachment') and callable(getattr(client, 'get_boot_volume_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_boot_volume_attachment(boot_volume_attachment_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@vnic_attachment_group.command(name=cli_util.override('compute.detach_vnic.command_name', 'detach'), help=u"""Detaches and deletes the specified secondary VNIC. This operation cannot be used on the instance's primary VNIC. When you terminate an instance, all attached VNICs (primary and secondary) are automatically detached and deleted.

**Important:** If the VNIC has a [private IP] that is the [target of a route rule], deleting the VNIC causes that route rule to blackhole and the traffic will be dropped. \n[Command Reference](detachVnic)""")
@cli_util.option('--vnic-attachment-id', required=True, help=u"""The OCID of the VNIC attachment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def detach_vnic(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vnic_attachment_id, if_match):

    if isinstance(vnic_attachment_id, six.string_types) and len(vnic_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --vnic-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.detach_vnic(
        vnic_attachment_id=vnic_attachment_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vnic_attachment') and callable(getattr(client, 'get_vnic_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_vnic_attachment(vnic_attachment_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@volume_group.command(name=cli_util.override('compute.detach_volume.command_name', 'detach'), help=u"""Detaches a storage volume from an instance. You must specify the OCID of the volume attachment.

This is an asynchronous operation. The attachment's `lifecycleState` will change to DETACHING temporarily until the attachment is completely removed. \n[Command Reference](detachVolume)""")
@cli_util.option('--volume-attachment-id', required=True, help=u"""The OCID of the volume attachment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def detach_volume(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_attachment_id, if_match):

    if isinstance(volume_attachment_id, six.string_types) and len(volume_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.detach_volume(
        volume_attachment_id=volume_attachment_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_volume_attachment') and callable(getattr(client, 'get_volume_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_volume_attachment(volume_attachment_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@image_group.command(name=cli_util.override('compute.export_image.command_name', 'export'), help=u"""Exports the specified image to the Oracle Cloud Infrastructure Object Storage service. You can use the Object Storage URL, or the namespace, bucket name, and object name when specifying the location to export to.

For more information about exporting images, see [Image Import/Export].

To perform an image export, you need write access to the Object Storage bucket for the image, see [Let Users Write Objects to Object Storage Buckets].

See [Object Storage URLs] and [Using Pre-Authenticated Requests] for constructing URLs for image import/export. \n[Command Reference](exportImage)""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the image.""")
@cli_util.option('--destination-type', required=True, help=u"""The destination type. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def export_image(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, image_id, destination_type, if_match):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}
    _details['destinationType'] = destination_type

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.export_image(
        image_id=image_id,
        export_image_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_image') and callable(getattr(client, 'get_image')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_image(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@image_group.command(name=cli_util.override('compute.export_image_export_image_via_object_storage_uri_details.command_name', 'export-image-export-image-via-object-storage-uri-details'), help=u"""Exports the specified image to the Oracle Cloud Infrastructure Object Storage service. You can use the Object Storage URL, or the namespace, bucket name, and object name when specifying the location to export to.

For more information about exporting images, see [Image Import/Export].

To perform an image export, you need write access to the Object Storage bucket for the image, see [Let Users Write Objects to Object Storage Buckets].

See [Object Storage URLs] and [Using Pre-Authenticated Requests] for constructing URLs for image import/export. \n[Command Reference](exportImage)""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the image.""")
@cli_util.option('--destination-uri', required=True, help=u"""The Object Storage URL to export the image to. See [Object Storage URLs] and [Using Pre-Authenticated Requests] for constructing URLs for image import/export.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def export_image_export_image_via_object_storage_uri_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, image_id, destination_uri, if_match):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}
    _details['destinationUri'] = destination_uri

    _details['destinationType'] = 'objectStorageUri'

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.export_image(
        image_id=image_id,
        export_image_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_image') and callable(getattr(client, 'get_image')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_image(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@image_group.command(name=cli_util.override('compute.export_image_export_image_via_object_storage_tuple_details.command_name', 'export-image-export-image-via-object-storage-tuple-details'), help=u"""Exports the specified image to the Oracle Cloud Infrastructure Object Storage service. You can use the Object Storage URL, or the namespace, bucket name, and object name when specifying the location to export to.

For more information about exporting images, see [Image Import/Export].

To perform an image export, you need write access to the Object Storage bucket for the image, see [Let Users Write Objects to Object Storage Buckets].

See [Object Storage URLs] and [Using Pre-Authenticated Requests] for constructing URLs for image import/export. \n[Command Reference](exportImage)""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the image.""")
@cli_util.option('--bucket-name', required=True, help=u"""The Object Storage bucket to export the image to.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace to export the image to.""")
@cli_util.option('--object-name', required=True, help=u"""The Object Storage object name for the exported image.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def export_image_export_image_via_object_storage_tuple_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, image_id, bucket_name, namespace_name, object_name, if_match):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}
    _details['bucketName'] = bucket_name
    _details['namespaceName'] = namespace_name
    _details['objectName'] = object_name

    _details['destinationType'] = 'objectStorageTuple'

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.export_image(
        image_id=image_id,
        export_image_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_image') and callable(getattr(client, 'get_image')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_image(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@app_catalog_listing_group.command(name=cli_util.override('compute.get_app_catalog_listing.command_name', 'get'), help=u"""Gets the specified listing. \n[Command Reference](getAppCatalogListing)""")
@cli_util.option('--listing-id', required=True, help=u"""The OCID of the listing.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'AppCatalogListing'})
@cli_util.wrap_exceptions
def get_app_catalog_listing(ctx, from_json, listing_id):

    if isinstance(listing_id, six.string_types) and len(listing_id.strip()) == 0:
        raise click.UsageError('Parameter --listing-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_app_catalog_listing(
        listing_id=listing_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@app_catalog_listing_resource_version_agreements_group.command(name=cli_util.override('compute.get_app_catalog_listing_agreements.command_name', 'get-app-catalog-listing-agreements'), help=u"""Retrieves the agreements for a particular resource version of a listing. \n[Command Reference](getAppCatalogListingAgreements)""")
@cli_util.option('--listing-id', required=True, help=u"""The OCID of the listing.""")
@cli_util.option('--resource-version', required=True, help=u"""Listing Resource Version.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'AppCatalogListingResourceVersionAgreements'})
@cli_util.wrap_exceptions
def get_app_catalog_listing_agreements(ctx, from_json, listing_id, resource_version):

    if isinstance(listing_id, six.string_types) and len(listing_id.strip()) == 0:
        raise click.UsageError('Parameter --listing-id cannot be whitespace or empty string')

    if isinstance(resource_version, six.string_types) and len(resource_version.strip()) == 0:
        raise click.UsageError('Parameter --resource-version cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_app_catalog_listing_agreements(
        listing_id=listing_id,
        resource_version=resource_version,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@app_catalog_listing_resource_version_group.command(name=cli_util.override('compute.get_app_catalog_listing_resource_version.command_name', 'get'), help=u"""Gets the specified listing resource version. \n[Command Reference](getAppCatalogListingResourceVersion)""")
@cli_util.option('--listing-id', required=True, help=u"""The OCID of the listing.""")
@cli_util.option('--resource-version', required=True, help=u"""Listing Resource Version.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'AppCatalogListingResourceVersion'})
@cli_util.wrap_exceptions
def get_app_catalog_listing_resource_version(ctx, from_json, listing_id, resource_version):

    if isinstance(listing_id, six.string_types) and len(listing_id.strip()) == 0:
        raise click.UsageError('Parameter --listing-id cannot be whitespace or empty string')

    if isinstance(resource_version, six.string_types) and len(resource_version.strip()) == 0:
        raise click.UsageError('Parameter --resource-version cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_app_catalog_listing_resource_version(
        listing_id=listing_id,
        resource_version=resource_version,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@boot_volume_attachment_group.command(name=cli_util.override('compute.get_boot_volume_attachment.command_name', 'get'), help=u"""Gets information about the specified boot volume attachment. \n[Command Reference](getBootVolumeAttachment)""")
@cli_util.option('--boot-volume-attachment-id', required=True, help=u"""The OCID of the boot volume attachment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'BootVolumeAttachment'})
@cli_util.wrap_exceptions
def get_boot_volume_attachment(ctx, from_json, boot_volume_attachment_id):

    if isinstance(boot_volume_attachment_id, six.string_types) and len(boot_volume_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_boot_volume_attachment(
        boot_volume_attachment_id=boot_volume_attachment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@compute_global_image_capability_schema_group.command(name=cli_util.override('compute.get_compute_global_image_capability_schema.command_name', 'get'), help=u"""Gets the specified Compute Global Image Capability Schema \n[Command Reference](getComputeGlobalImageCapabilitySchema)""")
@cli_util.option('--compute-global-image-capability-schema-id', required=True, help=u"""The [OCID] of the compute global image capability schema""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ComputeGlobalImageCapabilitySchema'})
@cli_util.wrap_exceptions
def get_compute_global_image_capability_schema(ctx, from_json, compute_global_image_capability_schema_id):

    if isinstance(compute_global_image_capability_schema_id, six.string_types) and len(compute_global_image_capability_schema_id.strip()) == 0:
        raise click.UsageError('Parameter --compute-global-image-capability-schema-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_compute_global_image_capability_schema(
        compute_global_image_capability_schema_id=compute_global_image_capability_schema_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@compute_global_image_capability_schema_version_group.command(name=cli_util.override('compute.get_compute_global_image_capability_schema_version.command_name', 'get'), help=u"""Gets the specified Compute Global Image Capability Schema Version \n[Command Reference](getComputeGlobalImageCapabilitySchemaVersion)""")
@cli_util.option('--compute-global-image-capability-schema-id', required=True, help=u"""The [OCID] of the compute global image capability schema""")
@cli_util.option('--compute-global-image-capability-schema-version-name', required=True, help=u"""The name of the compute global image capability schema version""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ComputeGlobalImageCapabilitySchemaVersion'})
@cli_util.wrap_exceptions
def get_compute_global_image_capability_schema_version(ctx, from_json, compute_global_image_capability_schema_id, compute_global_image_capability_schema_version_name):

    if isinstance(compute_global_image_capability_schema_id, six.string_types) and len(compute_global_image_capability_schema_id.strip()) == 0:
        raise click.UsageError('Parameter --compute-global-image-capability-schema-id cannot be whitespace or empty string')

    if isinstance(compute_global_image_capability_schema_version_name, six.string_types) and len(compute_global_image_capability_schema_version_name.strip()) == 0:
        raise click.UsageError('Parameter --compute-global-image-capability-schema-version-name cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_compute_global_image_capability_schema_version(
        compute_global_image_capability_schema_id=compute_global_image_capability_schema_id,
        compute_global_image_capability_schema_version_name=compute_global_image_capability_schema_version_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@compute_image_capability_schema_group.command(name=cli_util.override('compute.get_compute_image_capability_schema.command_name', 'get'), help=u"""Gets the specified Compute Image Capability Schema \n[Command Reference](getComputeImageCapabilitySchema)""")
@cli_util.option('--compute-image-capability-schema-id', required=True, help=u"""The id of the compute image capability schema or the image ocid""")
@cli_util.option('--is-merge-enabled', type=click.BOOL, help=u"""Merge the image capability schema with the global image capability schema""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ComputeImageCapabilitySchema'})
@cli_util.wrap_exceptions
def get_compute_image_capability_schema(ctx, from_json, compute_image_capability_schema_id, is_merge_enabled):

    if isinstance(compute_image_capability_schema_id, six.string_types) and len(compute_image_capability_schema_id.strip()) == 0:
        raise click.UsageError('Parameter --compute-image-capability-schema-id cannot be whitespace or empty string')

    kwargs = {}
    if is_merge_enabled is not None:
        kwargs['is_merge_enabled'] = is_merge_enabled
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_compute_image_capability_schema(
        compute_image_capability_schema_id=compute_image_capability_schema_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@console_history_group.command(name=cli_util.override('compute.get_console_history.command_name', 'get'), help=u"""Shows the metadata for the specified console history. See [CaptureConsoleHistory] for details about using the console history operations. \n[Command Reference](getConsoleHistory)""")
@cli_util.option('--instance-console-history-id', required=True, help=u"""The OCID of the console history.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ConsoleHistory'})
@cli_util.wrap_exceptions
def get_console_history(ctx, from_json, instance_console_history_id):

    if isinstance(instance_console_history_id, six.string_types) and len(instance_console_history_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-console-history-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_console_history(
        instance_console_history_id=instance_console_history_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@console_history_group.command(name=cli_util.override('compute.get_console_history_content.command_name', 'get-console-history-content'), help=u"""Gets the actual console history data (not the metadata). See [CaptureConsoleHistory] for details about using the console history operations. \n[Command Reference](getConsoleHistoryContent)""")
@cli_util.option('--instance-console-history-id', required=True, help=u"""The OCID of the console history.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--offset', type=click.INT, help=u"""Offset of the snapshot data to retrieve.""")
@cli_util.option('--length', type=click.INT, help=u"""Length of the snapshot data to retrieve.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_console_history_content(ctx, from_json, file, instance_console_history_id, offset, length):

    if isinstance(instance_console_history_id, six.string_types) and len(instance_console_history_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-console-history-id cannot be whitespace or empty string')

    kwargs = {}
    if offset is not None:
        kwargs['offset'] = offset
    if length is not None:
        kwargs['length'] = length
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_console_history_content(
        instance_console_history_id=instance_console_history_id,
        **kwargs
    )
    file.write(result.data)


@dedicated_vm_host_group.command(name=cli_util.override('compute.get_dedicated_vm_host.command_name', 'get'), help=u"""Gets information about the specified dedicated virtual machine host. \n[Command Reference](getDedicatedVmHost)""")
@cli_util.option('--dedicated-vm-host-id', required=True, help=u"""The OCID of the dedicated VM host.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'DedicatedVmHost'})
@cli_util.wrap_exceptions
def get_dedicated_vm_host(ctx, from_json, dedicated_vm_host_id):

    if isinstance(dedicated_vm_host_id, six.string_types) and len(dedicated_vm_host_id.strip()) == 0:
        raise click.UsageError('Parameter --dedicated-vm-host-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_dedicated_vm_host(
        dedicated_vm_host_id=dedicated_vm_host_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@image_group.command(name=cli_util.override('compute.get_image.command_name', 'get'), help=u"""Gets the specified image. \n[Command Reference](getImage)""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the image.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def get_image(ctx, from_json, image_id):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_image(
        image_id=image_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@image_shape_compatibility_entry_group.command(name=cli_util.override('compute.get_image_shape_compatibility_entry.command_name', 'get'), help=u"""Retrieves an image shape compatibility entry. \n[Command Reference](getImageShapeCompatibilityEntry)""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the image.""")
@cli_util.option('--shape-name', required=True, help=u"""Shape name.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ImageShapeCompatibilityEntry'})
@cli_util.wrap_exceptions
def get_image_shape_compatibility_entry(ctx, from_json, image_id, shape_name):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')

    if isinstance(shape_name, six.string_types) and len(shape_name.strip()) == 0:
        raise click.UsageError('Parameter --shape-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_image_shape_compatibility_entry(
        image_id=image_id,
        shape_name=shape_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_group.command(name=cli_util.override('compute.get_instance.command_name', 'get'), help=u"""Gets information about the specified instance. \n[Command Reference](getInstance)""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Instance'})
@cli_util.wrap_exceptions
def get_instance(ctx, from_json, instance_id):

    if isinstance(instance_id, six.string_types) and len(instance_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_instance(
        instance_id=instance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_console_connection_group.command(name=cli_util.override('compute.get_instance_console_connection.command_name', 'get'), help=u"""Gets the specified instance console connection's information. \n[Command Reference](getInstanceConsoleConnection)""")
@cli_util.option('--instance-console-connection-id', required=True, help=u"""The OCID of the instance console connection.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstanceConsoleConnection'})
@cli_util.wrap_exceptions
def get_instance_console_connection(ctx, from_json, instance_console_connection_id):

    if isinstance(instance_console_connection_id, six.string_types) and len(instance_console_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-console-connection-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_instance_console_connection(
        instance_console_connection_id=instance_console_connection_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vnic_attachment_group.command(name=cli_util.override('compute.get_vnic_attachment.command_name', 'get'), help=u"""Gets the information for the specified VNIC attachment. \n[Command Reference](getVnicAttachment)""")
@cli_util.option('--vnic-attachment-id', required=True, help=u"""The OCID of the VNIC attachment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VnicAttachment'})
@cli_util.wrap_exceptions
def get_vnic_attachment(ctx, from_json, vnic_attachment_id):

    if isinstance(vnic_attachment_id, six.string_types) and len(vnic_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --vnic-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_vnic_attachment(
        vnic_attachment_id=vnic_attachment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_attachment_group.command(name=cli_util.override('compute.get_volume_attachment.command_name', 'get'), help=u"""Gets information about the specified volume attachment. \n[Command Reference](getVolumeAttachment)""")
@cli_util.option('--volume-attachment-id', required=True, help=u"""The OCID of the volume attachment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeAttachment'})
@cli_util.wrap_exceptions
def get_volume_attachment(ctx, from_json, volume_attachment_id):

    if isinstance(volume_attachment_id, six.string_types) and len(volume_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_volume_attachment(
        volume_attachment_id=volume_attachment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_credentials_group.command(name=cli_util.override('compute.get_windows_instance_initial_credentials.command_name', 'get-windows-instance-initial-credentials'), help=u"""Gets the generated credentials for the instance. Only works for instances that require a password to log in, such as Windows. For certain operating systems, users will be forced to change the initial credentials. \n[Command Reference](getWindowsInstanceInitialCredentials)""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstanceCredentials'})
@cli_util.wrap_exceptions
def get_windows_instance_initial_credentials(ctx, from_json, instance_id):

    if isinstance(instance_id, six.string_types) and len(instance_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.get_windows_instance_initial_credentials(
        instance_id=instance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_group.command(name=cli_util.override('compute.instance_action.command_name', 'instance-action'), help=u"""Performs one of the following power actions on the specified instance:

- **START** - Powers on the instance.

- **STOP** - Powers off the instance.

- **RESET** - Powers off the instance and then powers it back on.

- **SOFTSTOP** - Gracefully shuts down the instance by sending a shutdown command to the operating system. If the applications that run on the instance take a long time to shut down, they could be improperly stopped, resulting in data corruption. To avoid this, shut down the instance using the commands available in the OS before you softstop the instance.

- **SOFTRESET** - Gracefully reboots the instance by sending a shutdown command to the operating system, and then powers the instance back on.

For more information, see [Stopping and Starting an Instance]. \n[Command Reference](instanceAction)""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@cli_util.option('--action', required=True, help=u"""The action to perform on the instance. Allowed values are: STOP, START, SOFTRESET, RESET, SOFTSTOP, SENDDIAGNOSTICINTERRUPT""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["MOVING", "PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Instance'})
@cli_util.wrap_exceptions
def instance_action(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_id, action, if_match):

    if isinstance(instance_id, six.string_types) and len(instance_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.instance_action(
        instance_id=instance_id,
        action=action,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_instance') and callable(getattr(client, 'get_instance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_instance(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@instance_group.command(name=cli_util.override('compute.launch_instance.command_name', 'launch'), help=u"""Creates a new instance in the specified compartment and the specified availability domain. For general information about instances, see [Overview of the Compute Service].

For information about access control and compartments, see [Overview of the IAM Service].

For information about availability domains, see [Regions and Availability Domains]. To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

All Oracle Cloud Infrastructure resources, including instances, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

To launch an instance using an image or a boot volume use the `sourceDetails` parameter in [LaunchInstanceDetails].

When you launch an instance, it is automatically attached to a virtual network interface card (VNIC), called the *primary VNIC*. The VNIC has a private IP address from the subnet's CIDR. You can either assign a private IP address of your choice or let Oracle automatically assign one. You can choose whether the instance has a public IP address. To retrieve the addresses, use the [ListVnicAttachments] operation to get the VNIC ID for the instance, and then call [GetVnic] with the VNIC ID.

You can later add secondary VNICs to an instance. For more information, see [Virtual Network Interface Cards (VNICs)].

To launch an instance from a Marketplace image listing, you must provide the image ID of the listing resource version that you want, but you also must subscribe to the listing before you try to launch the instance. To subscribe to the listing, use the [GetAppCatalogListingAgreements] operation to get the signature for the terms of use agreement for the desired listing resource version. Then, call [CreateAppCatalogSubscription] with the signature. To get the image ID for the LaunchInstance operation, call [GetAppCatalogListingResourceVersion]. \n[Command Reference](launchInstance)""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain of the instance.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--shape', required=True, help=u"""The shape of an instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance.

You can enumerate all available shapes by calling [ListShapes].""")
@cli_util.option('--create-vnic-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Details for the primary VNIC, which is automatically created and attached when the instance is launched.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dedicated-vm-host-id', help=u"""The OCID of the dedicated VM host.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

Example: `My bare metal instance`""")
@cli_util.option('--extended-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object.

They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only).

The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--fault-domain', help=u"""A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance that affects one fault domain does not affect instances in other fault domains.

If you do not specify the fault domain, the system selects one for you.

 To get a list of fault domains, use the [ListFaultDomains] operation in the Identity and Access Management Service API.

Example: `FAULT-DOMAIN-1`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostname-label', help=u"""Deprecated. Instead use `hostnameLabel` in [CreateVnicDetails]. If you provide both, the values must match.""")
@cli_util.option('--image-id', help=u"""Deprecated. Use `sourceDetails` with [InstanceSourceViaImageDetails] source type instead. If you specify values for both, the values must match.""")
@cli_util.option('--ipxe-script-file', type=click.File(mode='r'), help=u"""This is an advanced option.

When a bare metal or virtual machine instance boots, the iPXE firmware that runs on the instance is configured to run an iPXE script to continue the boot process.

If you want more control over the boot process, you can provide your own custom iPXE script that will run when the instance boots; however, you should be aware that the same iPXE script will run every time an instance boots; not only after the initial LaunchInstance call.

The default iPXE script connects to the instance's local boot volume over iSCSI and performs a network boot. If you use a custom iPXE script and want to network-boot from the instance's local boot volume over iSCSI the same way as the default iPXE script, you should use the following iSCSI IP address: 169.254.0.2, and boot volume IQN: iqn.2015-02.oracle.boot.

For more information about the Bring Your Own Image feature of Oracle Cloud Infrastructure, see [Bring Your Own Image].

For more information about iPXE, see http://ipxe.org.""")
@cli_util.option('--launch-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Options for tuning the compatibility and performance of VM shapes. The values that you specify override any default values.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--instance-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--availability-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Options for defining the availability of a VM instance after a maintenance event that impacts the underlying hardware.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Custom metadata key/value pairs that you provide, such as the SSH public key required to connect to the instance.

A metadata service runs on every launched instance. The service is an HTTP endpoint listening on 169.254.169.254. You can use the service to:

* Provide information to [Cloud-Init]   to be used for various system initialization tasks.

* Get information about the instance, including the custom metadata that you   provide when you launch the instance.

 **Providing Cloud-Init Metadata**

 You can use the following metadata key names to provide information to  Cloud-Init:

 **\"ssh_authorized_keys\"** - Provide one or more public SSH keys to be  included in the `~/.ssh/authorized_keys` file for the default user on the  instance. Use a newline character to separate multiple keys. The SSH  keys must be in the format necessary for the `authorized_keys` file, as shown  in the example below.

 **\"user_data\"** - Provide your own base64-encoded data to be used by  Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For  information about how to take advantage of user data, see the  [Cloud-Init Documentation].

 **Metadata Example**

      \"metadata\" : {          \"quake_bot_level\" : \"Severe\",          \"ssh_authorized_keys\" : \"ssh-rsa <your_public_SSH_key>== rsa-key-20160227\",          \"user_data\" : \"<your_public_SSH_key>==\"       }  **Getting Metadata on the Instance**

 To get information about your instance, connect to the instance using SSH and issue any of the  following GET requests:

     curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/      curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/metadata/      curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/metadata/<any-key-name>

 You'll get back a response that includes all the instance information; only the metadata information; or  the metadata information for the specified key name, respectively.

 The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--agent-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--shape-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--source-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Details for creating an instance. Use this parameter to specify whether a boot volume or an image should be used to launch a new instance.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--subnet-id', help=u"""Deprecated. Instead use `subnetId` in [CreateVnicDetails]. At least one of them is required; if you provide both, the values must match.""")
@cli_util.option('--is-pv-encryption-in-transit-enabled', type=click.BOOL, help=u"""Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["MOVING", "PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'create-vnic-details': {'module': 'core', 'class': 'CreateVnicDetails'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'extended-metadata': {'module': 'core', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'launch-options': {'module': 'core', 'class': 'LaunchOptions'}, 'instance-options': {'module': 'core', 'class': 'InstanceOptions'}, 'availability-config': {'module': 'core', 'class': 'LaunchInstanceAvailabilityConfigDetails'}, 'metadata': {'module': 'core', 'class': 'dict(str, string)'}, 'agent-config': {'module': 'core', 'class': 'LaunchInstanceAgentConfigDetails'}, 'shape-config': {'module': 'core', 'class': 'LaunchInstanceShapeConfigDetails'}, 'source-details': {'module': 'core', 'class': 'InstanceSourceDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'create-vnic-details': {'module': 'core', 'class': 'CreateVnicDetails'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'extended-metadata': {'module': 'core', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'launch-options': {'module': 'core', 'class': 'LaunchOptions'}, 'instance-options': {'module': 'core', 'class': 'InstanceOptions'}, 'availability-config': {'module': 'core', 'class': 'LaunchInstanceAvailabilityConfigDetails'}, 'metadata': {'module': 'core', 'class': 'dict(str, string)'}, 'agent-config': {'module': 'core', 'class': 'LaunchInstanceAgentConfigDetails'}, 'shape-config': {'module': 'core', 'class': 'LaunchInstanceShapeConfigDetails'}, 'source-details': {'module': 'core', 'class': 'InstanceSourceDetails'}}, output_type={'module': 'core', 'class': 'Instance'})
@cli_util.wrap_exceptions
def launch_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, shape, create_vnic_details, dedicated_vm_host_id, defined_tags, display_name, extended_metadata, fault_domain, freeform_tags, hostname_label, image_id, ipxe_script_file, launch_options, instance_options, availability_config, metadata, agent_config, shape_config, source_details, subnet_id, is_pv_encryption_in_transit_enabled):

    kwargs = {}

    _details = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id
    _details['shape'] = shape

    if create_vnic_details is not None:
        _details['createVnicDetails'] = cli_util.parse_json_parameter("create_vnic_details", create_vnic_details)

    if dedicated_vm_host_id is not None:
        _details['dedicatedVmHostId'] = dedicated_vm_host_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if extended_metadata is not None:
        _details['extendedMetadata'] = cli_util.parse_json_parameter("extended_metadata", extended_metadata)

    if fault_domain is not None:
        _details['faultDomain'] = fault_domain

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if hostname_label is not None:
        _details['hostnameLabel'] = hostname_label

    if image_id is not None:
        _details['imageId'] = image_id

    if ipxe_script_file is not None:
        _details['ipxeScript'] = ipxe_script_file.read()

    if launch_options is not None:
        _details['launchOptions'] = cli_util.parse_json_parameter("launch_options", launch_options)

    if instance_options is not None:
        _details['instanceOptions'] = cli_util.parse_json_parameter("instance_options", instance_options)

    if availability_config is not None:
        _details['availabilityConfig'] = cli_util.parse_json_parameter("availability_config", availability_config)

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if agent_config is not None:
        _details['agentConfig'] = cli_util.parse_json_parameter("agent_config", agent_config)

    if shape_config is not None:
        _details['shapeConfig'] = cli_util.parse_json_parameter("shape_config", shape_config)

    if source_details is not None:
        _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if is_pv_encryption_in_transit_enabled is not None:
        _details['isPvEncryptionInTransitEnabled'] = is_pv_encryption_in_transit_enabled

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.launch_instance(
        launch_instance_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_instance') and callable(getattr(client, 'get_instance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_instance(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@instance_group.command(name=cli_util.override('compute.launch_instance_instance_source_via_image_details.command_name', 'launch-instance-instance-source-via-image-details'), help=u"""Creates a new instance in the specified compartment and the specified availability domain. For general information about instances, see [Overview of the Compute Service].

For information about access control and compartments, see [Overview of the IAM Service].

For information about availability domains, see [Regions and Availability Domains]. To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

All Oracle Cloud Infrastructure resources, including instances, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

To launch an instance using an image or a boot volume use the `sourceDetails` parameter in [LaunchInstanceDetails].

When you launch an instance, it is automatically attached to a virtual network interface card (VNIC), called the *primary VNIC*. The VNIC has a private IP address from the subnet's CIDR. You can either assign a private IP address of your choice or let Oracle automatically assign one. You can choose whether the instance has a public IP address. To retrieve the addresses, use the [ListVnicAttachments] operation to get the VNIC ID for the instance, and then call [GetVnic] with the VNIC ID.

You can later add secondary VNICs to an instance. For more information, see [Virtual Network Interface Cards (VNICs)].

To launch an instance from a Marketplace image listing, you must provide the image ID of the listing resource version that you want, but you also must subscribe to the listing before you try to launch the instance. To subscribe to the listing, use the [GetAppCatalogListingAgreements] operation to get the signature for the terms of use agreement for the desired listing resource version. Then, call [CreateAppCatalogSubscription] with the signature. To get the image ID for the LaunchInstance operation, call [GetAppCatalogListingResourceVersion]. \n[Command Reference](launchInstance)""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain of the instance.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--shape', required=True, help=u"""The shape of an instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance.

You can enumerate all available shapes by calling [ListShapes].""")
@cli_util.option('--source-details-image-id', required=True, help=u"""The OCID of the image used to boot the instance.""")
@cli_util.option('--create-vnic-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Details for the primary VNIC, which is automatically created and attached when the instance is launched.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dedicated-vm-host-id', help=u"""The OCID of the dedicated VM host.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

Example: `My bare metal instance`""")
@cli_util.option('--extended-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object.

They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only).

The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--fault-domain', help=u"""A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance that affects one fault domain does not affect instances in other fault domains.

If you do not specify the fault domain, the system selects one for you.

 To get a list of fault domains, use the [ListFaultDomains] operation in the Identity and Access Management Service API.

Example: `FAULT-DOMAIN-1`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostname-label', help=u"""Deprecated. Instead use `hostnameLabel` in [CreateVnicDetails]. If you provide both, the values must match.""")
@cli_util.option('--image-id', help=u"""Deprecated. Use `sourceDetails` with [InstanceSourceViaImageDetails] source type instead. If you specify values for both, the values must match.""")
@cli_util.option('--ipxe-script-file', type=click.File(mode='r'), help=u"""This is an advanced option.

When a bare metal or virtual machine instance boots, the iPXE firmware that runs on the instance is configured to run an iPXE script to continue the boot process.

If you want more control over the boot process, you can provide your own custom iPXE script that will run when the instance boots; however, you should be aware that the same iPXE script will run every time an instance boots; not only after the initial LaunchInstance call.

The default iPXE script connects to the instance's local boot volume over iSCSI and performs a network boot. If you use a custom iPXE script and want to network-boot from the instance's local boot volume over iSCSI the same way as the default iPXE script, you should use the following iSCSI IP address: 169.254.0.2, and boot volume IQN: iqn.2015-02.oracle.boot.

For more information about the Bring Your Own Image feature of Oracle Cloud Infrastructure, see [Bring Your Own Image].

For more information about iPXE, see http://ipxe.org.""")
@cli_util.option('--launch-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Options for tuning the compatibility and performance of VM shapes. The values that you specify override any default values.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--instance-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--availability-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Options for defining the availability of a VM instance after a maintenance event that impacts the underlying hardware.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Custom metadata key/value pairs that you provide, such as the SSH public key required to connect to the instance.

A metadata service runs on every launched instance. The service is an HTTP endpoint listening on 169.254.169.254. You can use the service to:

* Provide information to [Cloud-Init]   to be used for various system initialization tasks.

* Get information about the instance, including the custom metadata that you   provide when you launch the instance.

 **Providing Cloud-Init Metadata**

 You can use the following metadata key names to provide information to  Cloud-Init:

 **\"ssh_authorized_keys\"** - Provide one or more public SSH keys to be  included in the `~/.ssh/authorized_keys` file for the default user on the  instance. Use a newline character to separate multiple keys. The SSH  keys must be in the format necessary for the `authorized_keys` file, as shown  in the example below.

 **\"user_data\"** - Provide your own base64-encoded data to be used by  Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For  information about how to take advantage of user data, see the  [Cloud-Init Documentation].

 **Metadata Example**

      \"metadata\" : {          \"quake_bot_level\" : \"Severe\",          \"ssh_authorized_keys\" : \"ssh-rsa <your_public_SSH_key>== rsa-key-20160227\",          \"user_data\" : \"<your_public_SSH_key>==\"       }  **Getting Metadata on the Instance**

 To get information about your instance, connect to the instance using SSH and issue any of the  following GET requests:

     curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/      curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/metadata/      curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/metadata/<any-key-name>

 You'll get back a response that includes all the instance information; only the metadata information; or  the metadata information for the specified key name, respectively.

 The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--agent-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--shape-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--subnet-id', help=u"""Deprecated. Instead use `subnetId` in [CreateVnicDetails]. At least one of them is required; if you provide both, the values must match.""")
@cli_util.option('--is-pv-encryption-in-transit-enabled', type=click.BOOL, help=u"""Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.""")
@cli_util.option('--source-details-boot-volume-size-in-gbs', type=click.INT, help=u"""The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 16384 GB (16TB).""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["MOVING", "PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'create-vnic-details': {'module': 'core', 'class': 'CreateVnicDetails'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'extended-metadata': {'module': 'core', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'launch-options': {'module': 'core', 'class': 'LaunchOptions'}, 'instance-options': {'module': 'core', 'class': 'InstanceOptions'}, 'availability-config': {'module': 'core', 'class': 'LaunchInstanceAvailabilityConfigDetails'}, 'metadata': {'module': 'core', 'class': 'dict(str, string)'}, 'agent-config': {'module': 'core', 'class': 'LaunchInstanceAgentConfigDetails'}, 'shape-config': {'module': 'core', 'class': 'LaunchInstanceShapeConfigDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'create-vnic-details': {'module': 'core', 'class': 'CreateVnicDetails'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'extended-metadata': {'module': 'core', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'launch-options': {'module': 'core', 'class': 'LaunchOptions'}, 'instance-options': {'module': 'core', 'class': 'InstanceOptions'}, 'availability-config': {'module': 'core', 'class': 'LaunchInstanceAvailabilityConfigDetails'}, 'metadata': {'module': 'core', 'class': 'dict(str, string)'}, 'agent-config': {'module': 'core', 'class': 'LaunchInstanceAgentConfigDetails'}, 'shape-config': {'module': 'core', 'class': 'LaunchInstanceShapeConfigDetails'}}, output_type={'module': 'core', 'class': 'Instance'})
@cli_util.wrap_exceptions
def launch_instance_instance_source_via_image_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, shape, source_details_image_id, create_vnic_details, dedicated_vm_host_id, defined_tags, display_name, extended_metadata, fault_domain, freeform_tags, hostname_label, image_id, ipxe_script_file, launch_options, instance_options, availability_config, metadata, agent_config, shape_config, subnet_id, is_pv_encryption_in_transit_enabled, source_details_boot_volume_size_in_gbs):

    kwargs = {}

    _details = {}
    _details['sourceDetails'] = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id
    _details['shape'] = shape
    _details['sourceDetails']['imageId'] = source_details_image_id

    if create_vnic_details is not None:
        _details['createVnicDetails'] = cli_util.parse_json_parameter("create_vnic_details", create_vnic_details)

    if dedicated_vm_host_id is not None:
        _details['dedicatedVmHostId'] = dedicated_vm_host_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if extended_metadata is not None:
        _details['extendedMetadata'] = cli_util.parse_json_parameter("extended_metadata", extended_metadata)

    if fault_domain is not None:
        _details['faultDomain'] = fault_domain

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if hostname_label is not None:
        _details['hostnameLabel'] = hostname_label

    if image_id is not None:
        _details['imageId'] = image_id

    if ipxe_script_file is not None:
        _details['ipxeScript'] = ipxe_script_file.read()

    if launch_options is not None:
        _details['launchOptions'] = cli_util.parse_json_parameter("launch_options", launch_options)

    if instance_options is not None:
        _details['instanceOptions'] = cli_util.parse_json_parameter("instance_options", instance_options)

    if availability_config is not None:
        _details['availabilityConfig'] = cli_util.parse_json_parameter("availability_config", availability_config)

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if agent_config is not None:
        _details['agentConfig'] = cli_util.parse_json_parameter("agent_config", agent_config)

    if shape_config is not None:
        _details['shapeConfig'] = cli_util.parse_json_parameter("shape_config", shape_config)

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if is_pv_encryption_in_transit_enabled is not None:
        _details['isPvEncryptionInTransitEnabled'] = is_pv_encryption_in_transit_enabled

    if source_details_boot_volume_size_in_gbs is not None:
        _details['sourceDetails']['bootVolumeSizeInGBs'] = source_details_boot_volume_size_in_gbs

    _details['sourceDetails']['sourceType'] = 'image'

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.launch_instance(
        launch_instance_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_instance') and callable(getattr(client, 'get_instance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_instance(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@instance_group.command(name=cli_util.override('compute.launch_instance_instance_source_via_boot_volume_details.command_name', 'launch-instance-instance-source-via-boot-volume-details'), help=u"""Creates a new instance in the specified compartment and the specified availability domain. For general information about instances, see [Overview of the Compute Service].

For information about access control and compartments, see [Overview of the IAM Service].

For information about availability domains, see [Regions and Availability Domains]. To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

All Oracle Cloud Infrastructure resources, including instances, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

To launch an instance using an image or a boot volume use the `sourceDetails` parameter in [LaunchInstanceDetails].

When you launch an instance, it is automatically attached to a virtual network interface card (VNIC), called the *primary VNIC*. The VNIC has a private IP address from the subnet's CIDR. You can either assign a private IP address of your choice or let Oracle automatically assign one. You can choose whether the instance has a public IP address. To retrieve the addresses, use the [ListVnicAttachments] operation to get the VNIC ID for the instance, and then call [GetVnic] with the VNIC ID.

You can later add secondary VNICs to an instance. For more information, see [Virtual Network Interface Cards (VNICs)].

To launch an instance from a Marketplace image listing, you must provide the image ID of the listing resource version that you want, but you also must subscribe to the listing before you try to launch the instance. To subscribe to the listing, use the [GetAppCatalogListingAgreements] operation to get the signature for the terms of use agreement for the desired listing resource version. Then, call [CreateAppCatalogSubscription] with the signature. To get the image ID for the LaunchInstance operation, call [GetAppCatalogListingResourceVersion]. \n[Command Reference](launchInstance)""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain of the instance.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--shape', required=True, help=u"""The shape of an instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance.

You can enumerate all available shapes by calling [ListShapes].""")
@cli_util.option('--source-details-boot-volume-id', required=True, help=u"""The OCID of the boot volume used to boot the instance.""")
@cli_util.option('--create-vnic-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Details for the primary VNIC, which is automatically created and attached when the instance is launched.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dedicated-vm-host-id', help=u"""The OCID of the dedicated VM host.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

Example: `My bare metal instance`""")
@cli_util.option('--extended-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object.

They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only).

The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--fault-domain', help=u"""A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance that affects one fault domain does not affect instances in other fault domains.

If you do not specify the fault domain, the system selects one for you.

 To get a list of fault domains, use the [ListFaultDomains] operation in the Identity and Access Management Service API.

Example: `FAULT-DOMAIN-1`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostname-label', help=u"""Deprecated. Instead use `hostnameLabel` in [CreateVnicDetails]. If you provide both, the values must match.""")
@cli_util.option('--image-id', help=u"""Deprecated. Use `sourceDetails` with [InstanceSourceViaImageDetails] source type instead. If you specify values for both, the values must match.""")
@cli_util.option('--ipxe-script-file', type=click.File(mode='r'), help=u"""This is an advanced option.

When a bare metal or virtual machine instance boots, the iPXE firmware that runs on the instance is configured to run an iPXE script to continue the boot process.

If you want more control over the boot process, you can provide your own custom iPXE script that will run when the instance boots; however, you should be aware that the same iPXE script will run every time an instance boots; not only after the initial LaunchInstance call.

The default iPXE script connects to the instance's local boot volume over iSCSI and performs a network boot. If you use a custom iPXE script and want to network-boot from the instance's local boot volume over iSCSI the same way as the default iPXE script, you should use the following iSCSI IP address: 169.254.0.2, and boot volume IQN: iqn.2015-02.oracle.boot.

For more information about the Bring Your Own Image feature of Oracle Cloud Infrastructure, see [Bring Your Own Image].

For more information about iPXE, see http://ipxe.org.""")
@cli_util.option('--launch-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Options for tuning the compatibility and performance of VM shapes. The values that you specify override any default values.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--instance-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--availability-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Options for defining the availability of a VM instance after a maintenance event that impacts the underlying hardware.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Custom metadata key/value pairs that you provide, such as the SSH public key required to connect to the instance.

A metadata service runs on every launched instance. The service is an HTTP endpoint listening on 169.254.169.254. You can use the service to:

* Provide information to [Cloud-Init]   to be used for various system initialization tasks.

* Get information about the instance, including the custom metadata that you   provide when you launch the instance.

 **Providing Cloud-Init Metadata**

 You can use the following metadata key names to provide information to  Cloud-Init:

 **\"ssh_authorized_keys\"** - Provide one or more public SSH keys to be  included in the `~/.ssh/authorized_keys` file for the default user on the  instance. Use a newline character to separate multiple keys. The SSH  keys must be in the format necessary for the `authorized_keys` file, as shown  in the example below.

 **\"user_data\"** - Provide your own base64-encoded data to be used by  Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For  information about how to take advantage of user data, see the  [Cloud-Init Documentation].

 **Metadata Example**

      \"metadata\" : {          \"quake_bot_level\" : \"Severe\",          \"ssh_authorized_keys\" : \"ssh-rsa <your_public_SSH_key>== rsa-key-20160227\",          \"user_data\" : \"<your_public_SSH_key>==\"       }  **Getting Metadata on the Instance**

 To get information about your instance, connect to the instance using SSH and issue any of the  following GET requests:

     curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/      curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/metadata/      curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/metadata/<any-key-name>

 You'll get back a response that includes all the instance information; only the metadata information; or  the metadata information for the specified key name, respectively.

 The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--agent-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--shape-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--subnet-id', help=u"""Deprecated. Instead use `subnetId` in [CreateVnicDetails]. At least one of them is required; if you provide both, the values must match.""")
@cli_util.option('--is-pv-encryption-in-transit-enabled', type=click.BOOL, help=u"""Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["MOVING", "PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'create-vnic-details': {'module': 'core', 'class': 'CreateVnicDetails'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'extended-metadata': {'module': 'core', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'launch-options': {'module': 'core', 'class': 'LaunchOptions'}, 'instance-options': {'module': 'core', 'class': 'InstanceOptions'}, 'availability-config': {'module': 'core', 'class': 'LaunchInstanceAvailabilityConfigDetails'}, 'metadata': {'module': 'core', 'class': 'dict(str, string)'}, 'agent-config': {'module': 'core', 'class': 'LaunchInstanceAgentConfigDetails'}, 'shape-config': {'module': 'core', 'class': 'LaunchInstanceShapeConfigDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'create-vnic-details': {'module': 'core', 'class': 'CreateVnicDetails'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'extended-metadata': {'module': 'core', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'launch-options': {'module': 'core', 'class': 'LaunchOptions'}, 'instance-options': {'module': 'core', 'class': 'InstanceOptions'}, 'availability-config': {'module': 'core', 'class': 'LaunchInstanceAvailabilityConfigDetails'}, 'metadata': {'module': 'core', 'class': 'dict(str, string)'}, 'agent-config': {'module': 'core', 'class': 'LaunchInstanceAgentConfigDetails'}, 'shape-config': {'module': 'core', 'class': 'LaunchInstanceShapeConfigDetails'}}, output_type={'module': 'core', 'class': 'Instance'})
@cli_util.wrap_exceptions
def launch_instance_instance_source_via_boot_volume_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, shape, source_details_boot_volume_id, create_vnic_details, dedicated_vm_host_id, defined_tags, display_name, extended_metadata, fault_domain, freeform_tags, hostname_label, image_id, ipxe_script_file, launch_options, instance_options, availability_config, metadata, agent_config, shape_config, subnet_id, is_pv_encryption_in_transit_enabled):

    kwargs = {}

    _details = {}
    _details['sourceDetails'] = {}
    _details['availabilityDomain'] = availability_domain
    _details['compartmentId'] = compartment_id
    _details['shape'] = shape
    _details['sourceDetails']['bootVolumeId'] = source_details_boot_volume_id

    if create_vnic_details is not None:
        _details['createVnicDetails'] = cli_util.parse_json_parameter("create_vnic_details", create_vnic_details)

    if dedicated_vm_host_id is not None:
        _details['dedicatedVmHostId'] = dedicated_vm_host_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if extended_metadata is not None:
        _details['extendedMetadata'] = cli_util.parse_json_parameter("extended_metadata", extended_metadata)

    if fault_domain is not None:
        _details['faultDomain'] = fault_domain

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if hostname_label is not None:
        _details['hostnameLabel'] = hostname_label

    if image_id is not None:
        _details['imageId'] = image_id

    if ipxe_script_file is not None:
        _details['ipxeScript'] = ipxe_script_file.read()

    if launch_options is not None:
        _details['launchOptions'] = cli_util.parse_json_parameter("launch_options", launch_options)

    if instance_options is not None:
        _details['instanceOptions'] = cli_util.parse_json_parameter("instance_options", instance_options)

    if availability_config is not None:
        _details['availabilityConfig'] = cli_util.parse_json_parameter("availability_config", availability_config)

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if agent_config is not None:
        _details['agentConfig'] = cli_util.parse_json_parameter("agent_config", agent_config)

    if shape_config is not None:
        _details['shapeConfig'] = cli_util.parse_json_parameter("shape_config", shape_config)

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if is_pv_encryption_in_transit_enabled is not None:
        _details['isPvEncryptionInTransitEnabled'] = is_pv_encryption_in_transit_enabled

    _details['sourceDetails']['sourceType'] = 'bootVolume'

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.launch_instance(
        launch_instance_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_instance') and callable(getattr(client, 'get_instance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_instance(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@app_catalog_listing_resource_version_group.command(name=cli_util.override('compute.list_app_catalog_listing_resource_versions.command_name', 'list'), help=u"""Gets all resource versions for a particular listing. \n[Command Reference](listAppCatalogListingResourceVersions)""")
@cli_util.option('--listing-id', required=True, help=u"""The OCID of the listing.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[AppCatalogListingResourceVersionSummary]'})
@cli_util.wrap_exceptions
def list_app_catalog_listing_resource_versions(ctx, from_json, all_pages, page_size, listing_id, limit, page, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(listing_id, six.string_types) and len(listing_id.strip()) == 0:
        raise click.UsageError('Parameter --listing-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_app_catalog_listing_resource_versions,
            listing_id=listing_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_app_catalog_listing_resource_versions,
            limit,
            page_size,
            listing_id=listing_id,
            **kwargs
        )
    else:
        result = client.list_app_catalog_listing_resource_versions(
            listing_id=listing_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@app_catalog_listing_group.command(name=cli_util.override('compute.list_app_catalog_listings.command_name', 'list'), help=u"""Lists the published listings. \n[Command Reference](listAppCatalogListings)""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--publisher-name', help=u"""A filter to return only the publisher that matches the given publisher name exactly.""")
@cli_util.option('--publisher-type', help=u"""A filter to return only publishers that match the given publisher type exactly. Valid types are OCI, ORACLE, TRUSTED, STANDARD.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[AppCatalogListingSummary]'})
@cli_util.wrap_exceptions
def list_app_catalog_listings(ctx, from_json, all_pages, page_size, limit, page, sort_order, publisher_name, publisher_type, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if publisher_name is not None:
        kwargs['publisher_name'] = publisher_name
    if publisher_type is not None:
        kwargs['publisher_type'] = publisher_type
    if display_name is not None:
        kwargs['display_name'] = display_name
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_app_catalog_listings,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_app_catalog_listings,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_app_catalog_listings(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@app_catalog_subscription_group.command(name=cli_util.override('compute.list_app_catalog_subscriptions.command_name', 'list'), help=u"""Lists subscriptions for a compartment. \n[Command Reference](listAppCatalogSubscriptions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--listing-id', help=u"""A filter to return only the listings that matches the given listing id.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[AppCatalogSubscriptionSummary]'})
@cli_util.wrap_exceptions
def list_app_catalog_subscriptions(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order, listing_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if listing_id is not None:
        kwargs['listing_id'] = listing_id
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_app_catalog_subscriptions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_app_catalog_subscriptions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_app_catalog_subscriptions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@boot_volume_attachment_group.command(name=cli_util.override('compute.list_boot_volume_attachments.command_name', 'list'), help=u"""Lists the boot volume attachments in the specified compartment. You can filter the list by specifying an instance OCID, boot volume OCID, or both. \n[Command Reference](listBootVolumeAttachments)""")
@cli_util.option('--availability-domain', required=True, help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--instance-id', help=u"""The OCID of the instance.""")
@cli_util.option('--boot-volume-id', help=u"""The OCID of the boot volume.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[BootVolumeAttachment]'})
@cli_util.wrap_exceptions
def list_boot_volume_attachments(ctx, from_json, all_pages, page_size, availability_domain, compartment_id, limit, page, instance_id, boot_volume_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if instance_id is not None:
        kwargs['instance_id'] = instance_id
    if boot_volume_id is not None:
        kwargs['boot_volume_id'] = boot_volume_id
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_boot_volume_attachments,
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_boot_volume_attachments,
            limit,
            page_size,
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_boot_volume_attachments(
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@compute_global_image_capability_schema_version_group.command(name=cli_util.override('compute.list_compute_global_image_capability_schema_versions.command_name', 'list'), help=u"""Lists Compute Global Image Capability Schema versions in the specified compartment. \n[Command Reference](listComputeGlobalImageCapabilitySchemaVersions)""")
@cli_util.option('--compute-global-image-capability-schema-id', required=True, help=u"""The [OCID] of the compute global image capability schema""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[ComputeGlobalImageCapabilitySchemaVersionSummary]'})
@cli_util.wrap_exceptions
def list_compute_global_image_capability_schema_versions(ctx, from_json, all_pages, page_size, compute_global_image_capability_schema_id, display_name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(compute_global_image_capability_schema_id, six.string_types) and len(compute_global_image_capability_schema_id.strip()) == 0:
        raise click.UsageError('Parameter --compute-global-image-capability-schema-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_compute_global_image_capability_schema_versions,
            compute_global_image_capability_schema_id=compute_global_image_capability_schema_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_compute_global_image_capability_schema_versions,
            limit,
            page_size,
            compute_global_image_capability_schema_id=compute_global_image_capability_schema_id,
            **kwargs
        )
    else:
        result = client.list_compute_global_image_capability_schema_versions(
            compute_global_image_capability_schema_id=compute_global_image_capability_schema_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@compute_global_image_capability_schema_group.command(name=cli_util.override('compute.list_compute_global_image_capability_schemas.command_name', 'list'), help=u"""Lists Compute Global Image Capability Schema in the specified compartment. \n[Command Reference](listComputeGlobalImageCapabilitySchemas)""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that match the given compartment OCID exactly.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[ComputeGlobalImageCapabilitySchemaSummary]'})
@cli_util.wrap_exceptions
def list_compute_global_image_capability_schemas(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_compute_global_image_capability_schemas,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_compute_global_image_capability_schemas,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_compute_global_image_capability_schemas(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@compute_image_capability_schema_group.command(name=cli_util.override('compute.list_compute_image_capability_schemas.command_name', 'list'), help=u"""Lists Compute Image Capability Schema in the specified compartment. You can also query by a specific imageId. \n[Command Reference](listComputeImageCapabilitySchemas)""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that match the given compartment OCID exactly.""")
@cli_util.option('--image-id', help=u"""The [OCID] of an image.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[ComputeImageCapabilitySchemaSummary]'})
@cli_util.wrap_exceptions
def list_compute_image_capability_schemas(ctx, from_json, all_pages, page_size, compartment_id, image_id, display_name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if image_id is not None:
        kwargs['image_id'] = image_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_compute_image_capability_schemas,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_compute_image_capability_schemas,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_compute_image_capability_schemas(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@console_history_group.command(name=cli_util.override('compute.list_console_histories.command_name', 'list'), help=u"""Lists the console history metadata for the specified compartment or instance. \n[Command Reference](listConsoleHistories)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--availability-domain', help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--instance-id', help=u"""The OCID of the instance.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["REQUESTED", "GETTING-HISTORY", "SUCCEEDED", "FAILED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[ConsoleHistory]'})
@cli_util.wrap_exceptions
def list_console_histories(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, limit, page, instance_id, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')

    kwargs = {}
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if instance_id is not None:
        kwargs['instance_id'] = instance_id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_console_histories,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_console_histories,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_console_histories(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@dedicated_vm_host_instance_shape_group.command(name=cli_util.override('compute.list_dedicated_vm_host_instance_shapes.command_name', 'list'), help=u"""Lists the shapes that can be used to launch a virtual machine instance on a dedicated virtual machine host within the specified compartment. You can filter the list by compatibility with a specific dedicated virtual machine host shape. \n[Command Reference](listDedicatedVmHostInstanceShapes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--availability-domain', help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--dedicated-vm-host-shape', help=u"""Dedicated VM host shape name""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[DedicatedVmHostInstanceShapeSummary]'})
@cli_util.wrap_exceptions
def list_dedicated_vm_host_instance_shapes(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, dedicated_vm_host_shape, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if dedicated_vm_host_shape is not None:
        kwargs['dedicated_vm_host_shape'] = dedicated_vm_host_shape
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_dedicated_vm_host_instance_shapes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_dedicated_vm_host_instance_shapes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_dedicated_vm_host_instance_shapes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@dedicated_vm_host_instance_group.command(name=cli_util.override('compute.list_dedicated_vm_host_instances.command_name', 'list'), help=u"""Returns the list of instances on the dedicated virtual machine hosts that match the specified criteria. \n[Command Reference](listDedicatedVmHostInstances)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--dedicated-vm-host-id', required=True, help=u"""The OCID of the dedicated VM host.""")
@cli_util.option('--availability-domain', help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[DedicatedVmHostInstanceSummary]'})
@cli_util.wrap_exceptions
def list_dedicated_vm_host_instances(ctx, from_json, all_pages, page_size, compartment_id, dedicated_vm_host_id, availability_domain, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')

    if isinstance(dedicated_vm_host_id, six.string_types) and len(dedicated_vm_host_id.strip()) == 0:
        raise click.UsageError('Parameter --dedicated-vm-host-id cannot be whitespace or empty string')

    kwargs = {}
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_dedicated_vm_host_instances,
            compartment_id=compartment_id,
            dedicated_vm_host_id=dedicated_vm_host_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_dedicated_vm_host_instances,
            limit,
            page_size,
            compartment_id=compartment_id,
            dedicated_vm_host_id=dedicated_vm_host_id,
            **kwargs
        )
    else:
        result = client.list_dedicated_vm_host_instances(
            compartment_id=compartment_id,
            dedicated_vm_host_id=dedicated_vm_host_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@dedicated_vm_host_shape_group.command(name=cli_util.override('compute.list_dedicated_vm_host_shapes.command_name', 'list'), help=u"""Lists the shapes that can be used to launch a dedicated virtual machine host within the specified compartment. \n[Command Reference](listDedicatedVmHostShapes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--availability-domain', help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--instance-shape-name', help=u"""The name for the instance's shape.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[DedicatedVmHostShapeSummary]'})
@cli_util.wrap_exceptions
def list_dedicated_vm_host_shapes(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, instance_shape_name, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if instance_shape_name is not None:
        kwargs['instance_shape_name'] = instance_shape_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_dedicated_vm_host_shapes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_dedicated_vm_host_shapes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_dedicated_vm_host_shapes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@dedicated_vm_host_group.command(name=cli_util.override('compute.list_dedicated_vm_hosts.command_name', 'list'), help=u"""Returns the list of dedicated virtual machine hosts that match the specified criteria in the specified compartment.

You can limit the list by specifying a dedicated virtual machine host display name. The list will include all the identically-named dedicated virtual machine hosts in the compartment. \n[Command Reference](listDedicatedVmHosts)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--availability-domain', help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to only return resources that match the given lifecycle state.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--instance-shape-name', help=u"""The name for the instance's shape.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[DedicatedVmHostSummary]'})
@cli_util.wrap_exceptions
def list_dedicated_vm_hosts(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, lifecycle_state, display_name, instance_shape_name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')

    kwargs = {}
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if instance_shape_name is not None:
        kwargs['instance_shape_name'] = instance_shape_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_dedicated_vm_hosts,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_dedicated_vm_hosts,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_dedicated_vm_hosts(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@image_shape_compatibility_entry_group.command(name=cli_util.override('compute.list_image_shape_compatibility_entries.command_name', 'list'), help=u"""Lists the compatible shapes for the specified image. \n[Command Reference](listImageShapeCompatibilityEntries)""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the image.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[ImageShapeCompatibilitySummary]'})
@cli_util.wrap_exceptions
def list_image_shape_compatibility_entries(ctx, from_json, all_pages, page_size, image_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_image_shape_compatibility_entries,
            image_id=image_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_image_shape_compatibility_entries,
            limit,
            page_size,
            image_id=image_id,
            **kwargs
        )
    else:
        result = client.list_image_shape_compatibility_entries(
            image_id=image_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@image_group.command(name=cli_util.override('compute.list_images.command_name', 'list'), help=u"""Lists the available images in the specified compartment, including both [Oracle-provided images] and [custom images] that have been created. The list of images returned is ordered to first show all Oracle-provided images, then all custom images.

The order of images returned may change when new images are released. \n[Command Reference](listImages)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--operating-system', help=u"""The image's operating system.

Example: `Oracle Linux`""")
@cli_util.option('--operating-system-version', help=u"""The image's operating system version.

Example: `7.2`""")
@cli_util.option('--shape', help=u"""Shape name.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Image]'})
@cli_util.wrap_exceptions
def list_images(ctx, from_json, all_pages, page_size, compartment_id, display_name, operating_system, operating_system_version, shape, limit, page, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if operating_system is not None:
        kwargs['operating_system'] = operating_system
    if operating_system_version is not None:
        kwargs['operating_system_version'] = operating_system_version
    if shape is not None:
        kwargs['shape'] = shape
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
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_images,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_images,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_images(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@instance_console_connection_group.command(name=cli_util.override('compute.list_instance_console_connections.command_name', 'list'), help=u"""Lists the console connections for the specified compartment or instance.

For more information about console access, see [Accessing the Console]. \n[Command Reference](listInstanceConsoleConnections)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--instance-id', help=u"""The OCID of the instance.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[InstanceConsoleConnection]'})
@cli_util.wrap_exceptions
def list_instance_console_connections(ctx, from_json, all_pages, page_size, compartment_id, instance_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if instance_id is not None:
        kwargs['instance_id'] = instance_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_instance_console_connections,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_instance_console_connections,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_instance_console_connections(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@device_group.command(name=cli_util.override('compute.list_instance_devices.command_name', 'list-instance'), help=u"""Gets a list of all the devices for given instance. You can optionally filter results by device availability. \n[Command Reference](listInstanceDevices)""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@cli_util.option('--is-available', type=click.BOOL, help=u"""A filter to return only available devices or only used devices.""")
@cli_util.option('--name', help=u"""A filter to return only devices that match the given name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Device]'})
@cli_util.wrap_exceptions
def list_instance_devices(ctx, from_json, all_pages, page_size, instance_id, is_available, name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(instance_id, six.string_types) and len(instance_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-id cannot be whitespace or empty string')

    kwargs = {}
    if is_available is not None:
        kwargs['is_available'] = is_available
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_instance_devices,
            instance_id=instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_instance_devices,
            limit,
            page_size,
            instance_id=instance_id,
            **kwargs
        )
    else:
        result = client.list_instance_devices(
            instance_id=instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@instance_group.command(name=cli_util.override('compute.list_instances.command_name', 'list'), help=u"""Lists the instances in the specified compartment and the specified availability domain. You can filter the results by specifying an instance name (the list will include all the identically-named instances in the compartment). \n[Command Reference](listInstances)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--availability-domain', help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["MOVING", "PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Instance]'})
@cli_util.wrap_exceptions
def list_instances(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, display_name, limit, page, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')

    kwargs = {}
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if display_name is not None:
        kwargs['display_name'] = display_name
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
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_instances,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_instances,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_instances(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@shape_group.command(name=cli_util.override('compute.list_shapes.command_name', 'list'), help=u"""Lists the shapes that can be used to launch an instance within the specified compartment. You can filter the list by compatibility with a specific image. \n[Command Reference](listShapes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--availability-domain', help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--image-id', help=u"""The [OCID] of an image.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Shape]'})
@cli_util.wrap_exceptions
def list_shapes(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, limit, page, image_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if image_id is not None:
        kwargs['image_id'] = image_id
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_shapes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_shapes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_shapes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@vnic_attachment_group.command(name=cli_util.override('compute.list_vnic_attachments.command_name', 'list'), help=u"""Lists the VNIC attachments in the specified compartment. A VNIC attachment resides in the same compartment as the attached instance. The list can be filtered by instance, VNIC, or availability domain. \n[Command Reference](listVnicAttachments)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--availability-domain', help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--instance-id', help=u"""The OCID of the instance.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--vnic-id', help=u"""The OCID of the VNIC.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VnicAttachment]'})
@cli_util.wrap_exceptions
def list_vnic_attachments(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, instance_id, limit, page, vnic_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if instance_id is not None:
        kwargs['instance_id'] = instance_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if vnic_id is not None:
        kwargs['vnic_id'] = vnic_id
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_vnic_attachments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_vnic_attachments,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_vnic_attachments(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@volume_attachment_group.command(name=cli_util.override('compute.list_volume_attachments.command_name', 'list'), help=u"""Lists the volume attachments in the specified compartment. You can filter the list by specifying an instance OCID, volume OCID, or both.

Currently, the only supported volume attachment type are [IScsiVolumeAttachment] and [ParavirtualizedVolumeAttachment]. \n[Command Reference](listVolumeAttachments)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--availability-domain', help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--instance-id', help=u"""The OCID of the instance.""")
@cli_util.option('--volume-id', help=u"""The OCID of the volume.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VolumeAttachment]'})
@cli_util.wrap_exceptions
def list_volume_attachments(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, limit, page, instance_id, volume_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if instance_id is not None:
        kwargs['instance_id'] = instance_id
    if volume_id is not None:
        kwargs['volume_id'] = volume_id
    client = cli_util.build_client('core', 'compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_volume_attachments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_volume_attachments,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_volume_attachments(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@image_shape_compatibility_entry_group.command(name=cli_util.override('compute.remove_image_shape_compatibility_entry.command_name', 'remove'), help=u"""Removes a shape from the compatible shapes list for the image. \n[Command Reference](removeImageShapeCompatibilityEntry)""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the image.""")
@cli_util.option('--shape-name', required=True, help=u"""Shape name.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def remove_image_shape_compatibility_entry(ctx, from_json, image_id, shape_name):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')

    if isinstance(shape_name, six.string_types) and len(shape_name.strip()) == 0:
        raise click.UsageError('Parameter --shape-name cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.remove_image_shape_compatibility_entry(
        image_id=image_id,
        shape_name=shape_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_group.command(name=cli_util.override('compute.terminate_instance.command_name', 'terminate'), help=u"""Terminates the specified instance. Any attached VNICs and volumes are automatically detached when the instance terminates.

To preserve the boot volume associated with the instance, specify `true` for `PreserveBootVolumeQueryParam`. To delete the boot volume when the instance is deleted, specify `false` or do not specify a value for `PreserveBootVolumeQueryParam`.

This is an asynchronous operation. The instance's `lifecycleState` will change to TERMINATING temporarily until the instance is completely removed. \n[Command Reference](terminateInstance)""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--preserve-boot-volume', type=click.BOOL, help=u"""Specifies whether to delete or preserve the boot volume when terminating an instance. The default value is false.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["MOVING", "PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def terminate_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_id, if_match, preserve_boot_volume):

    if isinstance(instance_id, six.string_types) and len(instance_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if preserve_boot_volume is not None:
        kwargs['preserve_boot_volume'] = preserve_boot_volume
    client = cli_util.build_client('core', 'compute', ctx)
    result = client.terminate_instance(
        instance_id=instance_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_instance') and callable(getattr(client, 'get_instance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_instance(instance_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@compute_image_capability_schema_group.command(name=cli_util.override('compute.update_compute_image_capability_schema.command_name', 'update'), help=u"""Updates the specified Compute Image Capability Schema \n[Command Reference](updateComputeImageCapabilitySchema)""")
@cli_util.option('--compute-image-capability-schema-id', required=True, help=u"""The id of the compute image capability schema or the image ocid""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the compute image capability schema""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema-data', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The map of each capability name to its ImageCapabilitySchemaDescriptor.

This option is a JSON dictionary of type dict(str, ImageCapabilitySchemaDescriptor).  For documentation on ImageCapabilitySchemaDescriptor please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/ImageCapabilitySchemaDescriptor.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'schema-data': {'module': 'core', 'class': 'dict(str, ImageCapabilitySchemaDescriptor)'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'schema-data': {'module': 'core', 'class': 'dict(str, ImageCapabilitySchemaDescriptor)'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'core', 'class': 'ComputeImageCapabilitySchema'})
@cli_util.wrap_exceptions
def update_compute_image_capability_schema(ctx, from_json, force, compute_image_capability_schema_id, display_name, freeform_tags, schema_data, defined_tags, if_match):

    if isinstance(compute_image_capability_schema_id, six.string_types) and len(compute_image_capability_schema_id.strip()) == 0:
        raise click.UsageError('Parameter --compute-image-capability-schema-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or schema_data or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and schema-data and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if schema_data is not None:
        _details['schemaData'] = cli_util.parse_json_parameter("schema_data", schema_data)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.update_compute_image_capability_schema(
        compute_image_capability_schema_id=compute_image_capability_schema_id,
        update_compute_image_capability_schema_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@console_history_group.command(name=cli_util.override('compute.update_console_history.command_name', 'update'), help=u"""Updates the specified console history metadata. \n[Command Reference](updateConsoleHistory)""")
@cli_util.option('--instance-console-history-id', required=True, help=u"""The OCID of the console history.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["REQUESTED", "GETTING-HISTORY", "SUCCEEDED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'ConsoleHistory'})
@cli_util.wrap_exceptions
def update_console_history(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_console_history_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(instance_console_history_id, six.string_types) and len(instance_console_history_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-console-history-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.update_console_history(
        instance_console_history_id=instance_console_history_id,
        update_console_history_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_console_history') and callable(getattr(client, 'get_console_history')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_console_history(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@dedicated_vm_host_group.command(name=cli_util.override('compute.update_dedicated_vm_host.command_name', 'update'), help=u"""Updates the displayName, freeformTags, and definedTags attributes for the specified dedicated virtual machine host. If an attribute value is not included, it will not be updated. \n[Command Reference](updateDedicatedVmHost)""")
@cli_util.option('--dedicated-vm-host-id', required=True, help=u"""The OCID of the dedicated VM host.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

Example: `My dedicated VM host`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'DedicatedVmHost'})
@cli_util.wrap_exceptions
def update_dedicated_vm_host(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, dedicated_vm_host_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(dedicated_vm_host_id, six.string_types) and len(dedicated_vm_host_id.strip()) == 0:
        raise click.UsageError('Parameter --dedicated-vm-host-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.update_dedicated_vm_host(
        dedicated_vm_host_id=dedicated_vm_host_id,
        update_dedicated_vm_host_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dedicated_vm_host') and callable(getattr(client, 'get_dedicated_vm_host')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_dedicated_vm_host(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@image_group.command(name=cli_util.override('compute.update_image.command_name', 'update'), help=u"""Updates the display name of the image. Avoid entering confidential information. \n[Command Reference](updateImage)""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the image.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

Example: `My custom Oracle Linux image`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--operating-system', help=u"""Operating system

Example: `Oracle Linux`""")
@cli_util.option('--operating-system-version', help=u"""Operating system version

Example: `7.4`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def update_image(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, image_id, defined_tags, display_name, freeform_tags, operating_system, operating_system_version, if_match):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')
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

    if operating_system is not None:
        _details['operatingSystem'] = operating_system

    if operating_system_version is not None:
        _details['operatingSystemVersion'] = operating_system_version

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.update_image(
        image_id=image_id,
        update_image_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_image') and callable(getattr(client, 'get_image')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_image(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@instance_group.command(name=cli_util.override('compute.update_instance.command_name', 'update'), help=u"""Updates certain fields on the specified instance. Fields that are not provided in the request will not be updated. Avoid entering confidential information.

Changes to metadata fields will be reflected in the instance metadata service (this may take up to a minute).

The OCID of the instance remains the same. \n[Command Reference](updateInstance)""")
@cli_util.option('--instance-id', required=True, help=u"""The OCID of the instance.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

Example: `My bare metal instance`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--agent-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Instance agent configuration options to choose for updating the instance""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Custom metadata key/value string pairs that you provide. Any set of key/value pairs provided here will completely replace the current set of key/value pairs in the `metadata` field on the instance.

The \"user_data\" field and the \"ssh_authorized_keys\" field cannot be changed after an instance has launched. Any request that updates, removes, or adds either of these fields will be rejected. You must provide the same values for \"user_data\" and \"ssh_authorized_keys\" that already exist on the instance.

The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--extended-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object.

They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only).

The \"user_data\" field and the \"ssh_authorized_keys\" field cannot be changed after an instance has launched. Any request that updates, removes, or adds either of these fields will be rejected. You must provide the same values for \"user_data\" and \"ssh_authorized_keys\" that already exist on the instance.

The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--shape', help=u"""The shape of the instance. The shape determines the number of CPUs and the amount of memory allocated to the instance. For more information about how to change shapes, and a list of shapes that are supported, see [Editing an Instance].

For details about the CPUs, memory, and other properties of each shape, see [Compute Shapes].

The new shape must be compatible with the image that was used to launch the instance. You can enumerate all available shapes and determine image compatibility by calling [ListShapes].

If the instance is running when you change the shape, the instance is rebooted.

Example: `VM.Standard2.1`""")
@cli_util.option('--shape-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--instance-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--fault-domain', help=u"""A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance that affects one fault domain does not affect instances in other fault domains.

To get a list of fault domains, use the [ListFaultDomains] operation in the Identity and Access Management Service API.

Example: `FAULT-DOMAIN-1`""")
@cli_util.option('--launch-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Options for tuning the compatibility and performance of VM shapes.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--availability-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Options for defining the availability of a VM instance after a maintenance event that impacts the underlying hardware.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["MOVING", "PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'agent-config': {'module': 'core', 'class': 'UpdateInstanceAgentConfigDetails'}, 'metadata': {'module': 'core', 'class': 'dict(str, string)'}, 'extended-metadata': {'module': 'core', 'class': 'dict(str, object)'}, 'shape-config': {'module': 'core', 'class': 'UpdateInstanceShapeConfigDetails'}, 'instance-options': {'module': 'core', 'class': 'InstanceOptions'}, 'launch-options': {'module': 'core', 'class': 'UpdateLaunchOptions'}, 'availability-config': {'module': 'core', 'class': 'UpdateInstanceAvailabilityConfigDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'agent-config': {'module': 'core', 'class': 'UpdateInstanceAgentConfigDetails'}, 'metadata': {'module': 'core', 'class': 'dict(str, string)'}, 'extended-metadata': {'module': 'core', 'class': 'dict(str, object)'}, 'shape-config': {'module': 'core', 'class': 'UpdateInstanceShapeConfigDetails'}, 'instance-options': {'module': 'core', 'class': 'InstanceOptions'}, 'launch-options': {'module': 'core', 'class': 'UpdateLaunchOptions'}, 'availability-config': {'module': 'core', 'class': 'UpdateInstanceAvailabilityConfigDetails'}}, output_type={'module': 'core', 'class': 'Instance'})
@cli_util.wrap_exceptions
def update_instance(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_id, defined_tags, display_name, freeform_tags, agent_config, metadata, extended_metadata, shape, shape_config, instance_options, fault_domain, launch_options, availability_config, if_match):

    if isinstance(instance_id, six.string_types) and len(instance_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or agent_config or metadata or extended_metadata or shape_config or instance_options or launch_options or availability_config:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and agent-config and metadata and extended-metadata and shape-config and instance-options and launch-options and availability-config will replace any existing values. Are you sure you want to continue?"):
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

    if agent_config is not None:
        _details['agentConfig'] = cli_util.parse_json_parameter("agent_config", agent_config)

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if extended_metadata is not None:
        _details['extendedMetadata'] = cli_util.parse_json_parameter("extended_metadata", extended_metadata)

    if shape is not None:
        _details['shape'] = shape

    if shape_config is not None:
        _details['shapeConfig'] = cli_util.parse_json_parameter("shape_config", shape_config)

    if instance_options is not None:
        _details['instanceOptions'] = cli_util.parse_json_parameter("instance_options", instance_options)

    if fault_domain is not None:
        _details['faultDomain'] = fault_domain

    if launch_options is not None:
        _details['launchOptions'] = cli_util.parse_json_parameter("launch_options", launch_options)

    if availability_config is not None:
        _details['availabilityConfig'] = cli_util.parse_json_parameter("availability_config", availability_config)

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.update_instance(
        instance_id=instance_id,
        update_instance_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_instance') and callable(getattr(client, 'get_instance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_instance(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@instance_console_connection_group.command(name=cli_util.override('compute.update_instance_console_connection.command_name', 'update'), help=u"""Updates the defined tags and free-form tags for the specified instance console connection. \n[Command Reference](updateInstanceConsoleConnection)""")
@cli_util.option('--instance-console-connection-id', required=True, help=u"""The OCID of the instance console connection.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'InstanceConsoleConnection'})
@cli_util.wrap_exceptions
def update_instance_console_connection(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_console_connection_id, defined_tags, freeform_tags, if_match):

    if isinstance(instance_console_connection_id, six.string_types) and len(instance_console_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-console-connection-id cannot be whitespace or empty string')
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

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.update_instance_console_connection(
        instance_console_connection_id=instance_console_connection_id,
        update_instance_console_connection_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_instance_console_connection') and callable(getattr(client, 'get_instance_console_connection')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_instance_console_connection(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
