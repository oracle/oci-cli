# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from ..cli_root import cli
from .. import cli_util
from .. import json_skeleton_utils
from .. import retry_utils  # noqa: F401
from .. import custom_types  # noqa: F401
from ..aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('compute_group.command_name', 'compute'), cls=CommandGroupWithAlias, help=cli_util.override('compute_group.help', """APIs for Networking Service, Compute Service, and Block Volume Service."""))
@cli_util.help_option_group
def compute_group():
    pass


@click.command(cli_util.override('volume_group.command_name', 'volume'), cls=CommandGroupWithAlias, help="""A detachable block volume device that allows you to dynamically expand
the storage capacity of an instance. For more information, see
[Overview of Cloud Volume Storage].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def volume_group():
    pass


@click.command(cli_util.override('image_group.command_name', 'image'), cls=CommandGroupWithAlias, help="""A boot disk image for launching an instance. For more information, see
[Overview of the Compute Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def image_group():
    pass


@click.command(cli_util.override('instance_credentials_group.command_name', 'instance-credentials'), cls=CommandGroupWithAlias, help="""The credentials for a particular instance.""")
@cli_util.help_option_group
def instance_credentials_group():
    pass


@click.command(cli_util.override('instance_group.command_name', 'instance'), cls=CommandGroupWithAlias, help="""A compute host. The image used to launch the instance determines its operating system and other
software. The shape specified during the launch process determines the number of CPUs and memory
allocated to the instance. For more information, see
[Overview of the Compute Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def instance_group():
    pass


@click.command(cli_util.override('boot_volume_group.command_name', 'boot-volume'), cls=CommandGroupWithAlias, help="""A detachable boot volume device that contains the image used to boot an Compute instance. For more information, see
[Overview of Boot Volumes].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def boot_volume_group():
    pass


@click.command(cli_util.override('shape_group.command_name', 'shape'), cls=CommandGroupWithAlias, help="""A compute instance shape that can be used in [LaunchInstance].
For more information, see [Overview of the Compute Service].""")
@cli_util.help_option_group
def shape_group():
    pass


@click.command(cli_util.override('vnic_attachment_group.command_name', 'vnic-attachment'), cls=CommandGroupWithAlias, help="""Represents an attachment between a VNIC and an instance. For more information, see
[Virtual Network Interface Cards (VNICs)].""")
@cli_util.help_option_group
def vnic_attachment_group():
    pass


@click.command(cli_util.override('volume_attachment_group.command_name', 'volume-attachment'), cls=CommandGroupWithAlias, help="""A base object for all types of attachments between a storage volume and an instance.
For specific details about iSCSI attachments, see
[IScsiVolumeAttachment Reference].

For general information about volume attachments, see
[Overview of Block Volume Storage].""")
@cli_util.help_option_group
def volume_attachment_group():
    pass


@click.command(cli_util.override('boot_volume_attachment_group.command_name', 'boot-volume-attachment'), cls=CommandGroupWithAlias, help="""Represents an attachment between a boot volume and an instance.""")
@cli_util.help_option_group
def boot_volume_attachment_group():
    pass


@click.command(cli_util.override('instance_console_connection_group.command_name', 'instance-console-connection'), cls=CommandGroupWithAlias, help="""The `InstanceConsoleConnection` API provides you with console access to virtual machine (VM) instances,
enabling you to troubleshoot malfunctioning instances remotely.

For more information about console access, see
[Accessing the Console].""")
@cli_util.help_option_group
def instance_console_connection_group():
    pass


@click.command(cli_util.override('console_history_group.command_name', 'console-history'), cls=CommandGroupWithAlias, help="""An instance's serial console data. It includes configuration messages that occur when the
instance boots, such as kernel and BIOS messages, and is useful for checking the status of
the instance or diagnosing problems. The console data is minimally formatted ASCII text.""")
@cli_util.help_option_group
def console_history_group():
    pass


@boot_volume_attachment_group.command(name=cli_util.override('attach_boot_volume.command_name', 'attach'), help="""Attaches the specified boot volume to the specified instance.""")
@click.option('--boot-volume-id', callback=cli_util.handle_required_param, help="""The OCID of the  boot volume. [required]""")
@click.option('--instance-id', callback=cli_util.handle_required_param, help="""The OCID of the instance. [required]""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'BootVolumeAttachment'})
@cli_util.wrap_exceptions
def attach_boot_volume(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, boot_volume_id, instance_id, display_name):
    kwargs = {}

    details = {}
    details['bootVolumeId'] = boot_volume_id
    details['instanceId'] = instance_id

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('compute', ctx)
    result = client.attach_boot_volume(
        attach_boot_volume_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_boot_volume_attachment') and callable(getattr(client, 'get_boot_volume_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_boot_volume_attachment, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vnic_attachment_group.command(name=cli_util.override('attach_vnic.command_name', 'attach'), help="""Creates a secondary VNIC and attaches it to the specified instance. For more information about secondary VNICs, see [Virtual Network Interface Cards (VNICs)].""")
@click.option('--create-vnic-details', callback=cli_util.handle_required_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Details for creating a new VNIC. [required]""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--instance-id', callback=cli_util.handle_required_param, help="""The OCID of the instance. [required]""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.""")
@click.option('--nic-index', callback=cli_util.handle_optional_param, type=click.INT, help="""Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)].""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'create-vnic-details': {'module': 'core', 'class': 'CreateVnicDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'create-vnic-details': {'module': 'core', 'class': 'CreateVnicDetails'}}, output_type={'module': 'core', 'class': 'VnicAttachment'})
@cli_util.wrap_exceptions
def attach_vnic(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, create_vnic_details, instance_id, display_name, nic_index):
    kwargs = {}

    details = {}
    details['createVnicDetails'] = cli_util.parse_json_parameter("create_vnic_details", create_vnic_details)
    details['instanceId'] = instance_id

    if display_name is not None:
        details['displayName'] = display_name

    if nic_index is not None:
        details['nicIndex'] = nic_index

    client = cli_util.build_client('compute', ctx)
    result = client.attach_vnic(
        attach_vnic_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_vnic_attachment') and callable(getattr(client, 'get_vnic_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_vnic_attachment, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_attachment_group.command(name=cli_util.override('attach_volume.command_name', 'attach'), help="""Attaches the specified storage volume to the specified instance.""")
@click.option('--instance-id', callback=cli_util.handle_required_param, help="""The OCID of the instance. [required]""")
@click.option('--type', callback=cli_util.handle_required_param, help="""The type of volume. The only supported value is \"iscsi\". [required]""")
@click.option('--volume-id', callback=cli_util.handle_required_param, help="""The OCID of the volume. [required]""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeAttachment'})
@cli_util.wrap_exceptions
def attach_volume(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_id, type, volume_id, display_name):
    kwargs = {}

    details = {}
    details['instanceId'] = instance_id
    details['type'] = type
    details['volumeId'] = volume_id

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('compute', ctx)
    result = client.attach_volume(
        attach_volume_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_volume_attachment') and callable(getattr(client, 'get_volume_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_volume_attachment, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@console_history_group.command(name=cli_util.override('capture_console_history.command_name', 'capture'), help="""Captures the most recent serial console data (up to a megabyte) for the specified instance.

The `CaptureConsoleHistory` operation works with the other console history operations as described below.

1. Use `CaptureConsoleHistory` to request the capture of up to a megabyte of the most recent console history. This call returns a `ConsoleHistory` object. The object will have a state of REQUESTED. 2. Wait for the capture operation to succeed by polling `GetConsoleHistory` with the identifier of the console history metadata. The state of the `ConsoleHistory` object will go from REQUESTED to GETTING-HISTORY and then SUCCEEDED (or FAILED). 3. Use `GetConsoleHistoryContent` to get the actual console history data (not the metadata). 4. Optionally, use `DeleteConsoleHistory` to delete the console history metadata and the console history data.""")
@click.option('--instance-id', callback=cli_util.handle_required_param, help="""The OCID of the instance to get the console history from. [required]""")
@click.option('--defined-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. Does not have to be unique, and it's changeable.""")
@click.option('--freeform-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["REQUESTED", "GETTING-HISTORY", "SUCCEEDED", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'ConsoleHistory'})
@cli_util.wrap_exceptions
def capture_console_history(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_id, defined_tags, display_name, freeform_tags):
    kwargs = {}

    details = {}
    details['instanceId'] = instance_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('compute', ctx)
    result = client.capture_console_history(
        capture_console_history_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_console_history') and callable(getattr(client, 'get_console_history')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_console_history, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@image_group.command(name=cli_util.override('create_image.command_name', 'create'), help="""Creates a boot disk image for the specified instance or imports an exported image from the Oracle Cloud Infrastructure Object Storage service.

When creating a new image, you must provide the OCID of the instance you want to use as the basis for the image, and the OCID of the compartment containing that instance. For more information about images, see [Managing Custom Images].

When importing an exported image from Object Storage, you specify the source information in [ImageSourceDetails].

When importing an image based on the namespace, bucket name, and object name, use [ImageSourceViaObjectStorageTupleDetails].

When importing an image based on the Object Storage URL, use [ImageSourceViaObjectStorageUriDetails]. See [Object Storage URLs] and [pre-authenticated requests] for constructing URLs for image import/export.

For more information about importing exported images, see [Image Import/Export].

You may optionally specify a *display name* for the image, which is simply a friendly name or description. It does not have to be unique, and you can change it. See [UpdateImage]. Avoid entering confidential information.""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment containing the instance you want to use as the basis for the image. [required]""")
@click.option('--defined-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name for the image. It does not have to be unique, and it's changeable. Avoid entering confidential information.

You cannot use an Oracle-provided image name as a custom image name.

Example: `My Oracle Linux image`""")
@click.option('--freeform-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--image-source-details', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Details for creating an image through import""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--instance-id', callback=cli_util.handle_optional_param, help="""The OCID of the instance you want to use as the basis for the image.""")
@click.option('--launch-mode', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["NATIVE", "EMULATED", "CUSTOM"]), help="""Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are: * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images. * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller. * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'image-source-details': {'module': 'core', 'class': 'ImageSourceDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'image-source-details': {'module': 'core', 'class': 'ImageSourceDetails'}}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def create_image(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, defined_tags, display_name, freeform_tags, image_source_details, instance_id, launch_mode):
    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if image_source_details is not None:
        details['imageSourceDetails'] = cli_util.parse_json_parameter("image_source_details", image_source_details)

    if instance_id is not None:
        details['instanceId'] = instance_id

    if launch_mode is not None:
        details['launchMode'] = launch_mode

    client = cli_util.build_client('compute', ctx)
    result = client.create_image(
        create_image_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_image') and callable(getattr(client, 'get_image')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_image, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@instance_console_connection_group.command(name=cli_util.override('create_instance_console_connection.command_name', 'create'), help="""Creates a new console connection to the specified instance. Once the console connection has been created and is available, you connect to the console using SSH.

For more information about console access, see [Accessing the Console].""")
@click.option('--instance-id', callback=cli_util.handle_required_param, help="""The OCID of the instance to create the console connection to. [required]""")
@click.option('--public-key', callback=cli_util.handle_required_param, help="""The SSH public key used to authenticate the console connection. [required]""")
@click.option('--defined-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--freeform-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'InstanceConsoleConnection'})
@cli_util.wrap_exceptions
def create_instance_console_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_id, public_key, defined_tags, freeform_tags):
    kwargs = {}

    details = {}
    details['instanceId'] = instance_id
    details['publicKey'] = public_key

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('compute', ctx)
    result = client.create_instance_console_connection(
        create_instance_console_connection_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_instance_console_connection') and callable(getattr(client, 'get_instance_console_connection')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_instance_console_connection, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@console_history_group.command(name=cli_util.override('delete_console_history.command_name', 'delete'), help="""Deletes the specified console history metadata and the console history data.""")
@click.option('--instance-console-history-id', callback=cli_util.handle_required_param, help="""The OCID of the console history. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["REQUESTED", "GETTING-HISTORY", "SUCCEEDED", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
    client = cli_util.build_client('compute', ctx)
    result = client.delete_console_history(
        instance_console_history_id=instance_console_history_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_console_history') and callable(getattr(client, 'get_console_history')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_console_history, instance_console_history_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@image_group.command(name=cli_util.override('delete_image.command_name', 'delete'), help="""Deletes an image.""")
@click.option('--image-id', callback=cli_util.handle_required_param, help="""The OCID of the image. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
    client = cli_util.build_client('compute', ctx)
    result = client.delete_image(
        image_id=image_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_image') and callable(getattr(client, 'get_image')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_image, image_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@instance_console_connection_group.command(name=cli_util.override('delete_instance_console_connection.command_name', 'delete'), help="""Deletes the specified instance console connection.""")
@click.option('--instance-console-connection-id', callback=cli_util.handle_required_param, help="""The OCID of the intance console connection [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
    client = cli_util.build_client('compute', ctx)
    result = client.delete_instance_console_connection(
        instance_console_connection_id=instance_console_connection_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_instance_console_connection') and callable(getattr(client, 'get_instance_console_connection')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_instance_console_connection, instance_console_connection_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@boot_volume_group.command(name=cli_util.override('detach_boot_volume.command_name', 'detach'), help="""Detaches a boot volume from an instance. You must specify the OCID of the boot volume attachment.

This is an asynchronous operation. The attachment's `lifecycleState` will change to DETACHING temporarily until the attachment is completely removed.""")
@click.option('--boot-volume-attachment-id', callback=cli_util.handle_required_param, help="""The OCID of the boot volume attachment. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
    client = cli_util.build_client('compute', ctx)
    result = client.detach_boot_volume(
        boot_volume_attachment_id=boot_volume_attachment_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_boot_volume_attachment') and callable(getattr(client, 'get_boot_volume_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_boot_volume_attachment, boot_volume_attachment_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vnic_attachment_group.command(name=cli_util.override('detach_vnic.command_name', 'detach'), help="""Detaches and deletes the specified secondary VNIC. This operation cannot be used on the instance's primary VNIC. When you terminate an instance, all attached VNICs (primary and secondary) are automatically detached and deleted.

**Important:** If the VNIC has a [private IP] that is the [target of a route rule], deleting the VNIC causes that route rule to blackhole and the traffic will be dropped.""")
@click.option('--vnic-attachment-id', callback=cli_util.handle_required_param, help="""The OCID of the VNIC attachment. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
    client = cli_util.build_client('compute', ctx)
    result = client.detach_vnic(
        vnic_attachment_id=vnic_attachment_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_vnic_attachment') and callable(getattr(client, 'get_vnic_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_vnic_attachment, vnic_attachment_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('detach_volume.command_name', 'detach'), help="""Detaches a storage volume from an instance. You must specify the OCID of the volume attachment.

This is an asynchronous operation. The attachment's `lifecycleState` will change to DETACHING temporarily until the attachment is completely removed.""")
@click.option('--volume-attachment-id', callback=cli_util.handle_required_param, help="""The OCID of the volume attachment. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
    client = cli_util.build_client('compute', ctx)
    result = client.detach_volume(
        volume_attachment_id=volume_attachment_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_volume_attachment') and callable(getattr(client, 'get_volume_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_volume_attachment, volume_attachment_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@image_group.command(name=cli_util.override('export_image.command_name', 'export'), help="""Exports the specified image to the Oracle Cloud Infrastructure Object Storage service. You can use the Object Storage URL, or the namespace, bucket name, and object name when specifying the location to export to.

For more information about exporting images, see [Image Import/Export].

To perform an image export, you need write access to the Object Storage bucket for the image, see [Let Users Write Objects to Object Storage Buckets].

See [Object Storage URLs] and [pre-authenticated requests] for constructing URLs for image import/export.""")
@click.option('--image-id', callback=cli_util.handle_required_param, help="""The OCID of the image. [required]""")
@click.option('--destination-type', callback=cli_util.handle_required_param, help="""The destination type. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def export_image(ctx, from_json, image_id, destination_type, if_match):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['destinationType'] = destination_type

    client = cli_util.build_client('compute', ctx)
    result = client.export_image(
        image_id=image_id,
        export_image_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@boot_volume_attachment_group.command(name=cli_util.override('get_boot_volume_attachment.command_name', 'get'), help="""Gets information about the specified boot volume attachment.""")
@click.option('--boot-volume-attachment-id', callback=cli_util.handle_required_param, help="""The OCID of the boot volume attachment. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'BootVolumeAttachment'})
@cli_util.wrap_exceptions
def get_boot_volume_attachment(ctx, from_json, boot_volume_attachment_id):

    if isinstance(boot_volume_attachment_id, six.string_types) and len(boot_volume_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-attachment-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('compute', ctx)
    result = client.get_boot_volume_attachment(
        boot_volume_attachment_id=boot_volume_attachment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@console_history_group.command(name=cli_util.override('get_console_history.command_name', 'get'), help="""Shows the metadata for the specified console history. See [CaptureConsoleHistory] for details about using the console history operations.""")
@click.option('--instance-console-history-id', callback=cli_util.handle_required_param, help="""The OCID of the console history. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ConsoleHistory'})
@cli_util.wrap_exceptions
def get_console_history(ctx, from_json, instance_console_history_id):

    if isinstance(instance_console_history_id, six.string_types) and len(instance_console_history_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-console-history-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('compute', ctx)
    result = client.get_console_history(
        instance_console_history_id=instance_console_history_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@console_history_group.command(name=cli_util.override('get_console_history_content.command_name', 'get-console-history-content'), help="""Gets the actual console history data (not the metadata). See [CaptureConsoleHistory] for details about using the console history operations.""")
@click.option('--instance-console-history-id', callback=cli_util.handle_required_param, help="""The OCID of the console history. [required]""")
@click.option('--file', type=click.File(mode='wb'), callback=cli_util.handle_required_param, help="The name of the file that will receive the response data, or '-' to write to STDOUT. [required]")
@click.option('--offset', callback=cli_util.handle_optional_param, type=click.INT, help="""Offset of the snapshot data to retrieve.""")
@click.option('--length', callback=cli_util.handle_optional_param, type=click.INT, help="""Length of the snapshot data to retrieve.""")
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
    client = cli_util.build_client('compute', ctx)
    result = client.get_console_history_content(
        instance_console_history_id=instance_console_history_id,
        **kwargs
    )
    file.write(result.data)


@image_group.command(name=cli_util.override('get_image.command_name', 'get'), help="""Gets the specified image.""")
@click.option('--image-id', callback=cli_util.handle_required_param, help="""The OCID of the image. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def get_image(ctx, from_json, image_id):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('compute', ctx)
    result = client.get_image(
        image_id=image_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_group.command(name=cli_util.override('get_instance.command_name', 'get'), help="""Gets information about the specified instance.""")
@click.option('--instance-id', callback=cli_util.handle_required_param, help="""The OCID of the instance. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Instance'})
@cli_util.wrap_exceptions
def get_instance(ctx, from_json, instance_id):

    if isinstance(instance_id, six.string_types) and len(instance_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('compute', ctx)
    result = client.get_instance(
        instance_id=instance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_console_connection_group.command(name=cli_util.override('get_instance_console_connection.command_name', 'get'), help="""Gets the specified instance console connection's information.""")
@click.option('--instance-console-connection-id', callback=cli_util.handle_required_param, help="""The OCID of the intance console connection [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstanceConsoleConnection'})
@cli_util.wrap_exceptions
def get_instance_console_connection(ctx, from_json, instance_console_connection_id):

    if isinstance(instance_console_connection_id, six.string_types) and len(instance_console_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-console-connection-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('compute', ctx)
    result = client.get_instance_console_connection(
        instance_console_connection_id=instance_console_connection_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vnic_attachment_group.command(name=cli_util.override('get_vnic_attachment.command_name', 'get'), help="""Gets the information for the specified VNIC attachment.""")
@click.option('--vnic-attachment-id', callback=cli_util.handle_required_param, help="""The OCID of the VNIC attachment. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VnicAttachment'})
@cli_util.wrap_exceptions
def get_vnic_attachment(ctx, from_json, vnic_attachment_id):

    if isinstance(vnic_attachment_id, six.string_types) and len(vnic_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --vnic-attachment-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('compute', ctx)
    result = client.get_vnic_attachment(
        vnic_attachment_id=vnic_attachment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_attachment_group.command(name=cli_util.override('get_volume_attachment.command_name', 'get'), help="""Gets information about the specified volume attachment.""")
@click.option('--volume-attachment-id', callback=cli_util.handle_required_param, help="""The OCID of the volume attachment. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeAttachment'})
@cli_util.wrap_exceptions
def get_volume_attachment(ctx, from_json, volume_attachment_id):

    if isinstance(volume_attachment_id, six.string_types) and len(volume_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-attachment-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('compute', ctx)
    result = client.get_volume_attachment(
        volume_attachment_id=volume_attachment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_credentials_group.command(name=cli_util.override('get_windows_instance_initial_credentials.command_name', 'get-windows-instance-initial-credentials'), help="""Gets the generated credentials for the instance. Only works for Windows instances. The returned credentials are only valid for the initial login.""")
@click.option('--instance-id', callback=cli_util.handle_required_param, help="""The OCID of the instance. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstanceCredentials'})
@cli_util.wrap_exceptions
def get_windows_instance_initial_credentials(ctx, from_json, instance_id):

    if isinstance(instance_id, six.string_types) and len(instance_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('compute', ctx)
    result = client.get_windows_instance_initial_credentials(
        instance_id=instance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_group.command(name=cli_util.override('instance_action.command_name', 'instance-action'), help="""Performs one of the power actions (start, stop, softreset, or reset) on the specified instance.

**start** - power on

**stop** - power off

**softreset** - ACPI shutdown and power on

**reset** - power off and power on

Note that the **stop** state has no effect on the resources you consume. Billing continues for instances that you stop, and related resources continue to apply against any relevant quotas. You must terminate an instance ([TerminateInstance]) to remove its resources from billing and quotas.""")
@click.option('--instance-id', callback=cli_util.handle_required_param, help="""The OCID of the instance. [required]""")
@click.option('--action', callback=cli_util.handle_required_param, help="""The action to perform on the instance. Allowed values are: STOP, START, SOFTRESET, RESET [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
    client = cli_util.build_client('compute', ctx)
    result = client.instance_action(
        instance_id=instance_id,
        action=action,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_instance') and callable(getattr(client, 'get_instance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_instance, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@instance_group.command(name=cli_util.override('launch_instance.command_name', 'launch'), help="""Creates a new instance in the specified compartment and the specified Availability Domain. For general information about instances, see [Overview of the Compute Service].

For information about access control and compartments, see [Overview of the IAM Service].

For information about Availability Domains, see [Regions and Availability Domains]. To get a list of Availability Domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

All Oracle Cloud Infrastructure resources, including instances, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

To launch an instance using an image or a boot volume use the `sourceDetails` parameter in [LaunchInstanceDetails].

When you launch an instance, it is automatically attached to a virtual network interface card (VNIC), called the *primary VNIC*. The VNIC has a private IP address from the subnet's CIDR. You can either assign a private IP address of your choice or let Oracle automatically assign one. You can choose whether the instance has a public IP address. To retrieve the addresses, use the [ListVnicAttachments] operation to get the VNIC ID for the instance, and then call [GetVnic] with the VNIC ID.

You can later add secondary VNICs to an instance. For more information, see [Virtual Network Interface Cards (VNICs)].""")
@click.option('--availability-domain', callback=cli_util.handle_required_param, help="""The Availability Domain of the instance.

Example: `Uocm:PHX-AD-1` [required]""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--shape', callback=cli_util.handle_required_param, help="""The shape of an instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance.

You can enumerate all available shapes by calling [ListShapes]. [required]""")
@click.option('--create-vnic-details', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Details for the primary VNIC, which is automatically created and attached when the instance is launched.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--defined-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

Example: `My bare metal instance`""")
@click.option('--extended-metadata', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Additional metadata key/value pairs that you provide.  They serve a similar purpose and functionality from fields in the 'metadata' object.

They are distinguished from 'metadata' fields in that these can be nested JSON objects (whereas 'metadata' fields are string/string maps only).

If you don't need nested metadata values, it is strongly advised to avoid using this object and use the Metadata object instead.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--freeform-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--hostname-label', callback=cli_util.handle_optional_param, help="""Deprecated. Instead use `hostnameLabel` in [CreateVnicDetails]. If you provide both, the values must match.""")
@click.option('--image-id', callback=cli_util.handle_optional_param, help="""Deprecated. Use `sourceDetails` with [InstanceSourceViaImageDetails] source type instead. If you specify values for both, the values must match.""")
@click.option('--ipxe-script-file', callback=cli_util.handle_optional_param, type=click.File(mode='r'), help="""This is an advanced option.

When a bare metal or virtual machine instance boots, the iPXE firmware that runs on the instance is configured to run an iPXE script to continue the boot process.

If you want more control over the boot process, you can provide your own custom iPXE script that will run when the instance boots; however, you should be aware that the same iPXE script will run every time an instance boots; not only after the initial LaunchInstance call.

The default iPXE script connects to the instance's local boot volume over iSCSI and performs a network boot. If you use a custom iPXE script and want to network-boot from the instance's local boot volume over iSCSI the same way as the default iPXE script, you should use the following iSCSI IP address: 169.254.0.2, and boot volume IQN: iqn.2015-02.oracle.boot.

For more information about the Bring Your Own Image feature of Oracle Cloud Infrastructure, see [Bring Your Own Image].

For more information about iPXE, see http://ipxe.org.""")
@click.option('--metadata', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Custom metadata key/value pairs that you provide, such as the SSH public key required to connect to the instance.

A metadata service runs on every launched instance. The service is an HTTP endpoint listening on 169.254.169.254. You can use the service to:

* Provide information to [Cloud-Init]   to be used for various system initialization tasks.

* Get information about the instance, including the custom metadata that you   provide when you launch the instance.

 **Providing Cloud-Init Metadata**

 You can use the following metadata key names to provide information to  Cloud-Init:

 **\"ssh_authorized_keys\"** - Provide one or more public SSH keys to be  included in the `~/.ssh/authorized_keys` file for the default user on the  instance. Use a newline character to separate multiple keys. The SSH  keys must be in the format necessary for the `authorized_keys` file, as shown  in the example below.

 **\"user_data\"** - Provide your own base64-encoded data to be used by  Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For  information about how to take advantage of user data, see the  [Cloud-Init Documentation].

 **Note:** Cloud-Init does not pull this data from the `http://169.254.169.254/opc/v1/instance/metadata/`  path. When the instance launches and either of these keys are provided, the key values are formatted as  OpenStack metadata and copied to the following locations, which are recognized by Cloud-Init:

 `http://169.254.169.254/openstack/latest/meta_data.json` - This JSON blob  contains, among other things, the SSH keys that you provided for   **\"ssh_authorized_keys\"**.

 `http://169.254.169.254/openstack/latest/user_data` - Contains the  base64-decoded data that you provided for **\"user_data\"**.

 **Metadata Example**

      \"metadata\" : {          \"quake_bot_level\" : \"Severe\",          \"ssh_authorized_keys\" : \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCZ06fccNTQfq+xubFlJ5ZR3kt+uzspdH9tXL+lAejSM1NXM+CFZev7MIxfEjas06y80ZBZ7DUTQO0GxJPeD8NCOb1VorF8M4xuLwrmzRtkoZzU16umt4y1W0Q4ifdp3IiiU0U8/WxczSXcUVZOLqkz5dc6oMHdMVpkimietWzGZ4LBBsH/LjEVY7E0V+a0sNchlVDIZcm7ErReBLcdTGDq0uLBiuChyl6RUkX1PNhusquTGwK7zc8OBXkRuubn5UKXhI3Ul9Nyk4XESkVWIGNKmw8mSpoJSjR8P9ZjRmcZVo8S+x4KVPMZKQEor== ryan.smith@company.com          ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAzJSAtwEPoB3Jmr58IXrDGzLuDYkWAYg8AsLYlo6JZvKpjY1xednIcfEVQJm4T2DhVmdWhRrwQ8DmayVZvBkLt+zs2LdoAJEVimKwXcJFD/7wtH8Lnk17HiglbbbNXsemjDY0hea4JUE5CfvkIdZBITuMrfqSmA4n3VNoorXYdvtTMoGG8fxMub46RPtuxtqi9bG9Zqenordkg5FJt2mVNfQRqf83CWojcOkklUWq4CjyxaeLf5i9gv1fRoBo4QhiA8I6NCSppO8GnoV/6Ox6TNoh9BiifqGKC9VGYuC89RvUajRBTZSK2TK4DPfaT+2R+slPsFrwiT/oPEhhEK1S5Q== rsa-key-20160227\",          \"user_data\" : \"SWYgeW91IGNhbiBzZWUgdGhpcywgdGhlbiBpdCB3b3JrZWQgbWF5YmUuCg==\"       }  **Getting Metadata on the Instance**

 To get information about your instance, connect to the instance using SSH and issue any of the  following GET requests:

     curl http://169.254.169.254/opc/v1/instance/      curl http://169.254.169.254/opc/v1/instance/metadata/      curl http://169.254.169.254/opc/v1/instance/metadata/<any-key-name>

 You'll get back a response that includes all the instance information; only the metadata information; or  the metadata information for the specified key name, respectively.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--source-details', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Details for creating an instance. Use this parameter to specify whether a boot volume or an image should be used to launch a new instance.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--subnet-id', callback=cli_util.handle_optional_param, help="""Deprecated. Instead use `subnetId` in [CreateVnicDetails]. At least one of them is required; if you provide both, the values must match.""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'create-vnic-details': {'module': 'core', 'class': 'CreateVnicDetails'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'extended-metadata': {'module': 'core', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'metadata': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'InstanceSourceDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'create-vnic-details': {'module': 'core', 'class': 'CreateVnicDetails'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'extended-metadata': {'module': 'core', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'metadata': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'InstanceSourceDetails'}}, output_type={'module': 'core', 'class': 'Instance'})
@cli_util.wrap_exceptions
def launch_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, shape, create_vnic_details, defined_tags, display_name, extended_metadata, freeform_tags, hostname_label, image_id, ipxe_script_file, metadata, source_details, subnet_id):
    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['compartmentId'] = compartment_id
    details['shape'] = shape

    if create_vnic_details is not None:
        details['createVnicDetails'] = cli_util.parse_json_parameter("create_vnic_details", create_vnic_details)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if extended_metadata is not None:
        details['extendedMetadata'] = cli_util.parse_json_parameter("extended_metadata", extended_metadata)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if hostname_label is not None:
        details['hostnameLabel'] = hostname_label

    if image_id is not None:
        details['imageId'] = image_id

    if ipxe_script_file is not None:
        details['ipxeScript'] = ipxe_script_file.read()

    if metadata is not None:
        details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if source_details is not None:
        details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if subnet_id is not None:
        details['subnetId'] = subnet_id

    client = cli_util.build_client('compute', ctx)
    result = client.launch_instance(
        launch_instance_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_instance') and callable(getattr(client, 'get_instance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_instance, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@boot_volume_attachment_group.command(name=cli_util.override('list_boot_volume_attachments.command_name', 'list'), help="""Lists the boot volume attachments in the specified compartment. You can filter the list by specifying an instance OCID, boot volume OCID, or both.""")
@click.option('--availability-domain', callback=cli_util.handle_required_param, help="""The name of the Availability Domain.

Example: `Uocm:PHX-AD-1` [required]""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--instance-id', callback=cli_util.handle_optional_param, help="""The OCID of the instance.""")
@click.option('--boot-volume-id', callback=cli_util.handle_optional_param, help="""The OCID of the boot volume.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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
    client = cli_util.build_client('compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_boot_volume_attachments,
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@console_history_group.command(name=cli_util.override('list_console_histories.command_name', 'list'), help="""Lists the console history metadata for the specified compartment or instance.""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--availability-domain', callback=cli_util.handle_optional_param, help="""The name of the Availability Domain.

Example: `Uocm:PHX-AD-1`""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--instance-id', callback=cli_util.handle_optional_param, help="""The OCID of the instance.""")
@click.option('--sort-by', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@click.option('--sort-order', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@click.option('--lifecycle-state', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["REQUESTED", "GETTING-HISTORY", "SUCCEEDED", "FAILED"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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
    client = cli_util.build_client('compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_console_histories,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@image_group.command(name=cli_util.override('list_images.command_name', 'list'), help="""Lists the available images in the specified compartment. If you specify a value for the `sortBy` parameter, Oracle-provided images appear first in the list, followed by custom images. For more information about images, see [Managing Custom Images].""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A filter to return only resources that match the given display name exactly.""")
@click.option('--operating-system', callback=cli_util.handle_optional_param, help="""The image's operating system.

Example: `Oracle Linux`""")
@click.option('--operating-system-version', callback=cli_util.handle_optional_param, help="""The image's operating system version.

Example: `7.2`""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--sort-by', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@click.option('--sort-order', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@click.option('--lifecycle-state', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Image]'})
@cli_util.wrap_exceptions
def list_images(ctx, from_json, all_pages, page_size, compartment_id, display_name, operating_system, operating_system_version, limit, page, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if operating_system is not None:
        kwargs['operating_system'] = operating_system
    if operating_system_version is not None:
        kwargs['operating_system_version'] = operating_system_version
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
    client = cli_util.build_client('compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_images,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@instance_console_connection_group.command(name=cli_util.override('list_instance_console_connections.command_name', 'list'), help="""Lists the console connections for the specified compartment or instance.

For more information about console access, see [Accessing the Instance Console].""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--instance-id', callback=cli_util.handle_optional_param, help="""The OCID of the instance.""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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
    client = cli_util.build_client('compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_instance_console_connections,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@instance_group.command(name=cli_util.override('list_instances.command_name', 'list'), help="""Lists the instances in the specified compartment and the specified Availability Domain. You can filter the results by specifying an instance name (the list will include all the identically-named instances in the compartment).""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--availability-domain', callback=cli_util.handle_optional_param, help="""The name of the Availability Domain.

Example: `Uocm:PHX-AD-1`""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A filter to return only resources that match the given display name exactly.""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--sort-by', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@click.option('--sort-order', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@click.option('--lifecycle-state', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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
    client = cli_util.build_client('compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_instances,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@shape_group.command(name=cli_util.override('list_shapes.command_name', 'list'), help="""Lists the shapes that can be used to launch an instance within the specified compartment. You can filter the list by compatibility with a specific image.""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--availability-domain', callback=cli_util.handle_optional_param, help="""The name of the Availability Domain.

Example: `Uocm:PHX-AD-1`""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--image-id', callback=cli_util.handle_optional_param, help="""The OCID of an image.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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
    client = cli_util.build_client('compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_shapes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@vnic_attachment_group.command(name=cli_util.override('list_vnic_attachments.command_name', 'list'), help="""Lists the VNIC attachments in the specified compartment. A VNIC attachment resides in the same compartment as the attached instance. The list can be filtered by instance, VNIC, or Availability Domain.""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--availability-domain', callback=cli_util.handle_optional_param, help="""The name of the Availability Domain.

Example: `Uocm:PHX-AD-1`""")
@click.option('--instance-id', callback=cli_util.handle_optional_param, help="""The OCID of the instance.""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--vnic-id', callback=cli_util.handle_optional_param, help="""The OCID of the VNIC.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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
    client = cli_util.build_client('compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_vnic_attachments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@volume_attachment_group.command(name=cli_util.override('list_volume_attachments.command_name', 'list'), help="""Lists the volume attachments in the specified compartment. You can filter the list by specifying an instance OCID, volume OCID, or both.

Currently, the only supported volume attachment type is [IScsiVolumeAttachment].""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--availability-domain', callback=cli_util.handle_optional_param, help="""The name of the Availability Domain.

Example: `Uocm:PHX-AD-1`""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--instance-id', callback=cli_util.handle_optional_param, help="""The OCID of the instance.""")
@click.option('--volume-id', callback=cli_util.handle_optional_param, help="""The OCID of the volume.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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
    client = cli_util.build_client('compute', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_volume_attachments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@instance_group.command(name=cli_util.override('terminate_instance.command_name', 'terminate'), help="""Terminates the specified instance. Any attached VNICs and volumes are automatically detached when the instance terminates.

To preserve the boot volume associated with the instance, specify `true` for `PreserveBootVolumeQueryParam`. To delete the boot volume when the instance is deleted, specify `false` or do not specify a value for `PreserveBootVolumeQueryParam`.

This is an asynchronous operation. The instance's `lifecycleState` will change to TERMINATING temporarily until the instance is completely removed.""")
@click.option('--instance-id', callback=cli_util.handle_required_param, help="""The OCID of the instance. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--preserve-boot-volume', callback=cli_util.handle_optional_param, type=click.BOOL, help="""Specifies whether to delete or preserve the boot volume when terminating an instance. The default value is false.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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
    client = cli_util.build_client('compute', ctx)
    result = client.terminate_instance(
        instance_id=instance_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_instance') and callable(getattr(client, 'get_instance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_instance, instance_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@console_history_group.command(name=cli_util.override('update_console_history.command_name', 'update'), help="""Updates the specified console history metadata.""")
@click.option('--instance-console-history-id', callback=cli_util.handle_required_param, help="""The OCID of the console history. [required]""")
@click.option('--defined-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. Does not have to be unique, and it's changeable.""")
@click.option('--freeform-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', callback=cli_util.handle_optional_param, help="""Perform update without prompting for confirmation.""", is_flag=True)
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["REQUESTED", "GETTING-HISTORY", "SUCCEEDED", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
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

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('compute', ctx)
    result = client.update_console_history(
        instance_console_history_id=instance_console_history_id,
        update_console_history_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_console_history') and callable(getattr(client, 'get_console_history')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_console_history, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@image_group.command(name=cli_util.override('update_image.command_name', 'update'), help="""Updates the display name of the image. Avoid entering confidential information.""")
@click.option('--image-id', callback=cli_util.handle_required_param, help="""The OCID of the image. [required]""")
@click.option('--defined-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

Example: `My custom Oracle Linux image`""")
@click.option('--freeform-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', callback=cli_util.handle_optional_param, help="""Perform update without prompting for confirmation.""", is_flag=True)
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def update_image(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, image_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('compute', ctx)
    result = client.update_image(
        image_id=image_id,
        update_image_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_image') and callable(getattr(client, 'get_image')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_image, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@instance_group.command(name=cli_util.override('update_instance.command_name', 'update'), help="""Updates the display name of the specified instance. Avoid entering confidential information. The OCID of the instance remains the same.""")
@click.option('--instance-id', callback=cli_util.handle_required_param, help="""The OCID of the instance. [required]""")
@click.option('--defined-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

Example: `My bare metal instance`""")
@click.option('--freeform-tags', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', callback=cli_util.handle_optional_param, help="""Perform update without prompting for confirmation.""", is_flag=True)
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Instance'})
@cli_util.wrap_exceptions
def update_instance(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(instance_id, six.string_types) and len(instance_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('compute', ctx)
    result = client.update_instance(
        instance_id=instance_id,
        update_instance_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_instance') and callable(getattr(client, 'get_instance')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_instance, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
