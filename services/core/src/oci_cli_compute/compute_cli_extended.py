# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
from base64 import b64encode
import click
import json
import re
import six
import sys

from services.core.src.oci_cli_compute.generated import compute_cli

from oci import wait_until
from oci import exceptions
from oci.exceptions import ServiceError
from oci.exceptions import MaximumWaitTimeExceeded
from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli import custom_types
from oci_cli import json_skeleton_utils
from oci_cli.aliasing import CommandGroupWithAlias

INSTANCE_CONSOLE_CONNECTION_STRING_INTERMEDIATE_HOST_REGEX = "(instance-console\.[a-z0-9-]+\.(oraclecloud|oracleiaas)\.com)"  # noqa: W605
DEFAULT_LOCAL_VNC_PORT = 5900
DEFAULT_SSH_PROXY_PORT = 5905

cli.add_command(compute_cli.compute_root_group)

compute_cli.compute_root_group.commands.pop(compute_cli.instance_credentials_group.name)

# oci compute compute-capacity-reservation ... -> oci compute capacity-reservation ...
cli_util.rename_command(compute_cli, compute_cli.compute_root_group, compute_cli.compute_capacity_reservation_group, "capacity-reservation")
# oci compute capacity-reservation list-compute -> oci compute capacity-reservation list
cli_util.rename_command(compute_cli, compute_cli.compute_capacity_reservation_group, compute_cli.list_compute_capacity_reservations, "list")

# oci compute compute-capacity-reservation-instance ... -> oci compute capacity-reservation instance ...
compute_cli.compute_root_group.commands.pop(compute_cli.capacity_reservation_instance_group.name)
compute_cli.compute_capacity_reservation_group.add_command(compute_cli.capacity_reservation_instance_group)
cli_util.rename_command(compute_cli, compute_cli.compute_capacity_reservation_group, compute_cli.capacity_reservation_instance_group, 'instance')
# oci compute capacity-reservation instance list-compute ->  oci compute capacity-reservation instance list
cli_util.rename_command(compute_cli, compute_cli.capacity_reservation_instance_group, compute_cli.list_compute_capacity_reservation_instances, "list")

# oci compute compute-capacity-reservation-instance-shape ... -> oci compute capacity-reservation instance-shape ...
compute_cli.compute_root_group.commands.pop(compute_cli.compute_capacity_reservation_instance_shape_group.name)
compute_cli.compute_capacity_reservation_group.add_command(compute_cli.compute_capacity_reservation_instance_shape_group)
cli_util.rename_command(compute_cli, compute_cli.compute_capacity_reservation_group, compute_cli.compute_capacity_reservation_instance_shape_group, 'instance-shape')
# oci compute capacity-reservation instance-shape list-compute ->  oci compute capacity-reservation instance-shape list

# oci compute dedicated-vm-host-instance-shape list to
# oci compute dedicated-vm-host instance-shape list
compute_cli.compute_root_group.commands.pop(compute_cli.dedicated_vm_host_instance_shape_group.name)
compute_cli.dedicated_vm_host_group.add_command(compute_cli.dedicated_vm_host_instance_shape_group)
cli_util.rename_command(compute_cli, compute_cli.dedicated_vm_host_group, compute_cli.dedicated_vm_host_instance_shape_group, 'instance-shape')


# oci compute dedicated-vm-host-shape list
# oci compute dedicated-vm-host host-shape list
compute_cli.compute_root_group.commands.pop(compute_cli.dedicated_vm_host_shape_group.name)
compute_cli.dedicated_vm_host_group.add_command(compute_cli.dedicated_vm_host_shape_group)
cli_util.rename_command(compute_cli, compute_cli.dedicated_vm_host_group, compute_cli.dedicated_vm_host_shape_group, 'host-shape')


# Disabling subclass commands
compute_cli.image_group.commands.pop(compute_cli.export_image_export_image_via_object_storage_uri_details.name)
compute_cli.image_group.commands.pop(compute_cli.export_image_export_image_via_object_storage_tuple_details.name)

# Disable nested polymorphic commands
compute_cli.image_group.commands.pop(compute_cli.create_image_image_source_via_object_storage_tuple_details.name)
compute_cli.image_group.commands.pop(compute_cli.create_image_image_source_via_object_storage_uri_details.name)
compute_cli.instance_group.commands.pop(compute_cli.launch_instance_instance_source_via_image_details.name)
compute_cli.instance_group.commands.pop(compute_cli.launch_instance_instance_source_via_boot_volume_details.name)

compute_cli.image_group.commands.pop(compute_cli.export_image.name)

compute_cli.instance_group.commands.pop(compute_cli.change_instance_compartment.name)

compute_cli.compute_root_group.add_command(compute_cli.instance_group)
compute_cli.compute_root_group.add_command(compute_cli.shape_group)
compute_cli.compute_root_group.add_command(compute_cli.vnic_attachment_group)
compute_cli.compute_root_group.add_command(compute_cli.boot_volume_attachment_group)
compute_cli.compute_root_group.add_command(compute_cli.volume_attachment_group)

# Disabling subclass commands
compute_cli.volume_attachment_group.commands.pop(compute_cli.attach_volume_attach_service_determined_volume_details.name)
compute_cli.volume_attachment_group.commands.pop(compute_cli.attach_volume_attach_emulated_volume_details.name)

cli_util.rename_command(compute_cli, compute_cli.volume_attachment_group, compute_cli.attach_volume_attach_i_scsi_volume_details, 'attach-iscsi-volume')

compute_cli.compute_root_group.add_command(compute_cli.console_history_group)
cli_util.rename_command(compute_cli, compute_cli.console_history_group, compute_cli.get_console_history_content, "get-content")
compute_cli.compute_root_group.add_command(compute_cli.instance_console_connection_group)
cli_util.rename_command(compute_cli, compute_cli.instance_group, compute_cli.instance_action, "action")
cli_util.rename_command(compute_cli, compute_cli.instance_credentials_group, compute_cli.get_windows_instance_initial_credentials, "get-windows-initial-creds")
compute_cli.get_windows_instance_initial_credentials.name = "get-windows-initial-creds"
compute_cli.instance_group.add_command(compute_cli.get_windows_instance_initial_credentials)
compute_cli.vnic_attachment_group.commands.pop(compute_cli.attach_vnic.name)
compute_cli.vnic_attachment_group.commands.pop(compute_cli.detach_vnic.name)
compute_cli.instance_console_connection_group.commands.pop(compute_cli.create_instance_console_connection.name)
cli_util.rename_command(compute_cli, compute_cli.volume_attachment_group, compute_cli.attach_volume_attach_paravirtualized_volume_details, "attach-paravirtualized-volume")
compute_cli.compute_root_group.help = "Compute Service CLI"
compute_cli.compute_root_group.short_help = "Compute Service"

# boot volume related commands under 'oci compute' belong in boot-volume-attachment group
compute_cli.compute_root_group.commands.pop(compute_cli.boot_volume_group.name)
compute_cli.boot_volume_attachment_group.add_command(compute_cli.detach_boot_volume)

# help for oci compute instance launch --metadata
compute_instance_launch_metadata_example = """'{"ssh_authorized_keys": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDbVpuGODmhsRZOLWNgm0aEYUoWIDSPNWHmg2M6mZpmZNHfiNfx2dSofxUpKOiu5S8Th52AuAHSmkzNe6lXBO9wxnjOvkowe1mAleRTEl8zPI8Jkz6HrmJCzHEtS04kC4bx+tXRZhIfRq1uGaPcriKyquTnQs52Ahoxgw5vdXXQMwxWZLAcyaP01JrZwcUqPlB/GRiBFSTj0E/AIiVW3APNME5HjreOd/djjPRpvWu7AUpOqskG38kr8lhxo1hJifqeMg5W7cQsecTLJHgTDAPJD68ujM93jdzV2llIXwR1zyl80i6c3lDLyLgUrCLM0R1xex/zITTdT6/Z84buS/Xl my public key"}'"""
compute_instance_launch_metadata_help = """Custom metadata key/value pairs that you provide, such as the SSH public key required to connect to the instance. For more info see documentation: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/requests/LaunchInstanceDetails. This must be provided in JSON format.

Note: user_data and ssh_authorized_keys can instead be specified using the parameters --user-data-file and --ssh-authorized-keys-file."""

compute_instance_launch_hostname_label_help = """The hostname for the VNIC that is created during instance launch. Used for DNS. The value is the hostname portion of the instance's fully qualified domain name (FQDN) (e.g., `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952] and [RFC 1123]. The value cannot be changed, and it can be retrieved from the [Vnic].

For more information, see [DNS in Your Virtual Cloud Network]."""
cli_util.update_param_help(compute_cli.launch_instance, 'metadata', compute_instance_launch_metadata_help, append=False, example=compute_instance_launch_metadata_example)
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

cli_util.get_param(compute_cli.attach_volume, 'type').type = custom_types.CliCaseInsensitiveChoice(['service_determined', 'emulated', 'iscsi', 'paravirtualized'])

cli_util.update_param_help(compute_cli.create_image, 'image_source_details', """[DEPRECATED] The use of the `oci compute image create` command to import an image from Object Storage is deprecated.

\b
Please use the `oci compute image import` command instead.

""" + cli_util.get_param(compute_cli.create_image, 'image_source_details').help, append=False)


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
def export_image_to_object(ctx, from_json, image_id, if_match, namespace, bucket_name, name, export_format):
    export_image_details = {}
    export_image_details['destinationType'] = 'objectStorageTuple'
    export_image_details['namespaceName'] = namespace
    export_image_details['bucketName'] = bucket_name
    export_image_details['objectName'] = name
    if export_format is not None:
        export_image_details['exportFormat'] = export_format

    export_image_internal(ctx, image_id, export_image_details, if_match)


@cli_util.copy_params_from_generated_command(compute_cli.instance_action, params_to_exclude=['action_type'])
@compute_cli.instance_group.command(name=cli_util.override('compute.instance_action.command_name', 'instance-action'), help=u"""Performs one of the following power actions on the specified instance:

- **START** - Powers on the instance.

- **STOP** - Powers off the instance.

- **RESET** - Powers off the instance and then powers it back on.

- **SOFTSTOP** - Gracefully shuts down the instance by sending a shutdown command to the operating system. After waiting 15 minutes for the OS to shut down, the instance is powered off. If the applications that run on the instance take more than 15 minutes to shut down, they could be improperly stopped, resulting in data corruption. To avoid this, manually shut down the instance using the commands available in the OS before you softstop the instance.

- **SOFTRESET** - Gracefully reboots the instance by sending a shutdown command to the operating system. After waiting 15 minutes for the OS to shut down, the instance is powered off and then powered back on.

- **SENDDIAGNOSTICINTERRUPT** - For advanced users. **Warning: Sending a diagnostic interrupt to a live system can cause data corruption or system failure.** Sends a diagnostic interrupt that causes the instance's OS to crash and then reboot. Before you send a diagnostic interrupt, you must configure the instance to generate a crash dump file when it crashes. The crash dump captures information about the state of the OS at the time of the crash. After the OS restarts, you can analyze the crash dump to diagnose the issue. For more information, see [Sending a Diagnostic Interrupt].

 - **DIAGNOSTICREBOOT** - Powers off the instance, rebuilds it on the physical host, and then powers it back on. Before you send a diagnostic reboot, restart the instance's OS, confirm that the instance and networking settings are configured correctly, and try other [troubleshooting steps]. Use diagnostic reboot as a final attempt to troubleshoot an unreachable instance. For virtual machine (VM) instances only. For more information, see [Performing a Diagnostic Reboot].

 - **REBOOTMIGRATE** - Powers off the instance, moves it to new hardware, and then powers it back on.

 For more information about managing instance lifecycle states, see [Stopping and Starting an Instance]. \n[Command Reference](instanceAction)""")
@cli_util.option('--allow-dense-reboot-migration', type=click.BOOL, help=u"""For use with RESET and SOFTRESET actions on instances that use a DenseIO shape, the flag denoting whether [reboot migration] is performed for the instance. The default value is `false`.

If the instance has a date in the Maintenance reboot field and you do nothing (or set this flag to `false`), the instance will be rebuilt at the scheduled maintenance time. The instance will experience 2-6 hours of downtime during the maintenance process. The local NVMe-based SSD will be preserved.

If you want to minimize downtime and can delete the SSD, you can set this flag to `true` and proactively reboot the instance before the scheduled maintenance time. The instance will be reboot migrated to a healthy host and the SSD will be deleted. A short downtime occurs during the migration.

**Caution:** When `true`, the SSD is permanently deleted. We recommend that you create a backup of the SSD before proceeding.""")
@cli_util.option('--delete-local-storage', type=click.BOOL, help=u"""For bare metal instances that have local storage, this must be set to true to verify that the local storage will be deleted during the migration.  For instances without, this parameter has no effect.""")
@cli_util.option('--time-scheduled', type=custom_types.CLI_DATETIME, help=u"""If present, this parameter will set (or re-set) the scheduled time that the instance will be reboot migrated in the format defined by [RFC3339].  This will also change the timeRebootMigrationDue field on the instance. If not present, the reboot migration will be triggered immediately.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Instance'})
@cli_util.wrap_exceptions
def instance_action_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_id, action, if_match, delete_local_storage, time_scheduled,
                             allow_dense_reboot_migration):

    if isinstance(instance_id, six.string_types) and len(instance_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-id cannot be whitespace or empty string')
    if delete_local_storage is not None and not action.lower() == 'rebootmigrate':
        raise click.UsageError('Parameter --delete-local-storage is for REBOOTMIGRATE actions only')
    if time_scheduled is not None and not action.lower() == 'rebootmigrate':
        raise click.UsageError('Parameter --time-scheduled is for REBOOTMIGRATE actions only')
    if allow_dense_reboot_migration is not None and not (action.lower() == 'reset' or action.lower() == 'softreset'):
        raise click.UsageError('Parameter --allow-dense-reboot-migration is for RESET and SOFTRESET actions only')

    _details = None
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    if action.lower() == 'reset':
        _details = {'actionType': 'reset'}
        if allow_dense_reboot_migration is not None:
            _details['allowDenseRebootMigration'] = allow_dense_reboot_migration

    if action.lower() == 'softreset':
        _details = {'actionType': 'softreset'}
        if allow_dense_reboot_migration is not None:
            _details['allowDenseRebootMigration'] = allow_dense_reboot_migration

    if action.lower() == 'rebootmigrate':
        _details = {'actionType': 'rebootMigrate'}
        if delete_local_storage is not None:
            _details['deleteLocalStorage'] = delete_local_storage

        if time_scheduled is not None:
            _details['timeScheduled'] = time_scheduled

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.instance_action(
        instance_id=instance_id,
        action=action,
        instance_power_action_details=_details,
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
                result = wait_until(client, client.get_instance(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except exceptions.MaximumWaitTimeExceeded as e:
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


@cli_util.copy_params_from_generated_command(compute_cli.export_image, params_to_exclude=['destination_type', 'wait_for_state', 'max_wait_seconds', 'wait_interval_seconds'])
@export_image_group.command(name='to-object-uri', help="""Exports the specified image to the Oracle Cloud Infrastructure Object Storage Service using the Object Storage Service URL to identify the location to export to.

For more information about exporting images, see [Image Import/Export].

See [Object Storage URLs] and [pre-authenticated requests] for constructing URLs for image import/export.
""")
@cli_util.option('--uri', required=True, help='The Object Storage URL to export the image to.')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def export_image_to_uri(ctx, from_json, image_id, if_match, uri, export_format):
    export_image_details = {}
    export_image_details['destinationType'] = 'objectStorageUri'
    export_image_details['destinationUri'] = uri
    if export_format is not None:
        export_image_details['exportFormat'] = export_format

    export_image_internal(ctx, image_id, export_image_details, if_match)


def export_image_internal(ctx, image_id, export_image_details, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    client = cli_util.build_client('core', 'compute', ctx)
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
@cli_util.option('--operating-system', help=u"""The image's operating system.

Example: `Oracle Linux`""")
@cli_util.option('--operating-system-version', help=u"""The image's operating system version.

Example: `7.2`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'image-source-details': {'module': 'core', 'class': 'ImageSourceDetails'}}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def import_image_from_object(ctx, from_json, compartment_id, display_name, namespace, bucket_name, name, source_image_type, operating_system, operating_system_version, launch_mode, defined_tags, freeform_tags):
    import_image_details = {}
    import_image_details['sourceType'] = 'objectStorageTuple'
    import_image_details['namespaceName'] = namespace
    import_image_details['bucketName'] = bucket_name
    import_image_details['objectName'] = name

    if source_image_type is not None:
        import_image_details['sourceImageType'] = source_image_type

    if operating_system is not None:
        import_image_details['operatingSystem'] = operating_system

    if operating_system_version is not None:
        import_image_details['operatingSystemVersion'] = operating_system_version

    import_image_internal(ctx, compartment_id, display_name, import_image_details, launch_mode, defined_tags, freeform_tags)


@cli_util.copy_params_from_generated_command(compute_cli.create_image, params_to_exclude=['image_source_details', 'instance_id', 'wait_for_state', 'max_wait_seconds', 'wait_interval_seconds'])
@import_image_group.command(name='from-object-uri', help="""Imports an exported image from the Oracle Cloud Infrastructure Object Storage Service using the Object Storage Service URL to identify the location to import from.

For more information about importing exported images, see [Image Import/Export].

See [Object Storage URLs] and [pre-authenticated requests] for constructing URLs for image import/export.

You may optionally specify a display name for the image, which is simply a friendly name or description. It does not have to be unique, and you can change it. See [UpdateImage].
Avoid entering confidential information.
""")
@cli_util.option('--uri', required=True, help='The Object Storage URL to import the image from.')
@cli_util.option('--source-image-type', type=custom_types.CliCaseInsensitiveChoice(["QCOW2", "VMDK"]), help='The format of the image to be imported. Exported Oracle images are QCOW2. Only monolithic images are supported.')
@cli_util.option('--operating-system', help=u"""The image's operating system.

Example: `Oracle Linux`""")
@cli_util.option('--operating-system-version', help=u"""The image's operating system version.

Example: `7.2`""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'image-source-details': {'module': 'core', 'class': 'ImageSourceDetails'}}, output_type={'module': 'core', 'class': 'Image'})
@cli_util.wrap_exceptions
def import_image_from_uri(ctx, from_json, compartment_id, display_name, uri, source_image_type, operating_system, operating_system_version, launch_mode, defined_tags, freeform_tags):
    import_image_details = {}
    import_image_details['sourceType'] = 'objectStorageUri'
    import_image_details['sourceUri'] = uri

    if source_image_type is not None:
        import_image_details['sourceImageType'] = source_image_type

    if operating_system is not None:
        import_image_details['operatingSystem'] = operating_system

    if operating_system_version is not None:
        import_image_details['operatingSystemVersion'] = operating_system_version

    import_image_internal(ctx, compartment_id, display_name, import_image_details, launch_mode, defined_tags, freeform_tags)


def import_image_internal(ctx, compartment_id, display_name, import_image_details, launch_mode, defined_tags, freeform_tags):
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

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.create_image(
        create_image_details=details,
        **kwargs
    )

    cli_util.render_response(result, ctx)


@compute_cli.instance_group.command(name='list-vnics', help="""Lists the VNICs that are attached to the specified instance. VNICs that are in the process of attaching or detaching will not be returned.""")
@cli_util.option('--compartment-id', help="""The OCID of the compartment.""")
@cli_util.option('--availability-domain', help=u"""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--instance-id', help="""The OCID of the instance.""")
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
def list_vnics(ctx, from_json, compartment_id, availability_domain, instance_id, limit, page, all_pages, page_size):
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if not compartment_id and not instance_id:
        raise click.UsageError('--compartment-id or --instance-id must be provided')

    client = cli_util.build_client('core', 'compute', ctx)
    if not compartment_id:
        compartment_id = client.get_instance(instance_id=instance_id).data.compartment_id

    kwargs = {}
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
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

    networking_client = cli_util.build_client('core', 'virtual_network', ctx)
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
    # if no result, just show error message
    if not result or not len(result):
        if instance_id:
            click.echo('No VNICs found for this instance. Please check that the instance is in RUNNING state.',
                       file=sys.stderr)
        else:
            click.echo(
                'No VNICs found under this compartment. Please check that the compartment has instances in RUNNING state.',
                file=sys.stderr)
    cli_util.render(result, vnic_attachments_result.headers, ctx=ctx)


@cli_util.copy_params_from_generated_command(compute_cli.launch_instance, params_to_exclude=['create_vnic_details', 'subnet_id'])
@compute_cli.instance_group.command(name='launch', help=compute_cli.launch_instance.help)
@cli_util.option('--vnic-display-name', help="""A user-friendly name for the default VNIC attached to this instance. Does not have to be unique.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the [OCIDs] of the network security groups (NSGs) to add the VNIC to..""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--assign-public-ip', type=click.BOOL, help="""Whether the default VNIC attached to this instance should be assigned a public IP address. Defaults to whether the subnet is public or private. If not set and the VNIC is being created in a private subnet (i.e., where prohibitPublicIpOnVnic=true in the Subnet), then no public IP address is assigned. If not set and the subnet is public (prohibitPublicIpOnVnic=false), then a public IP address is assigned. If set to true and prohibitPublicIpOnVnic=true, an error is returned.""")
@cli_util.option('--private-ip', help="""A private IP address of your choice to assign to the default VNIC attached to this instance. Must be an available IP address within the subnet's CIDR. If no value is specified, a private IP address from the subnet will be automatically assigned.""")
@cli_util.option('--skip-source-dest-check', type=click.BOOL, help="""Indicates whether Source/Destination check is disabled on the VNIC. Defaults to `false`, in which case we enable Source/Destination check on the VNIC.""")
@cli_util.option('--assign-private-dns-record', type=click.BOOL, help="""Whether the VNIC should be assigned a DNS record. If set to false, no DNS record registion for the VNIC; if set to true, DNS record will be registered. The default value is `true`.""")
@cli_util.option('--user-data-file', type=click.File('rb'), help="""A file containing data that Cloud-Init can use to run custom scripts or provide custom Cloud-Init configuration. This parameter is a convenience wrapper around the 'user_data' field of the --metadata parameter.  Populating both values in the same call will result in an error. For more info see Cloud-Init documentation: https://cloudinit.readthedocs.org/en/latest/topics/format.html.""")
@cli_util.option('--ssh-authorized-keys-file', type=click.File('r'), help="""A file containing one or more public SSH keys to be included in the ~/.ssh/authorized_keys file for the default user on the instance. Use a newline character to separate multiple keys. The SSH keys must be in the format necessary for the authorized_keys file. This parameter is a convenience wrapper around the 'ssh_authorized_keys' field of the --metadata parameter. Populating both values in the same call will result in an error. For more info see documentation: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/requests/LaunchInstanceDetails.""")
@cli_util.option('--source-boot-volume-id', help="""The OCID of the boot volume used to boot the instance. This is a shortcut for specifying a boot volume source via the --source-details complex JSON parameter. If this parameter is provided, you cannot provide the --source-details or --image-id parameters.""")
@cli_util.option('--boot-volume-size-in-gbs', type=click.INT, help="""The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 16384 GB (16TB). This is a shortcut for specifying a boot volume size via the --source-details complex JSON parameter. If this parameter is provided, you cannot provide the --source-details or --source-boot-volume-id parameters.""")
@cli_util.option('--subnet-id', required=True, help=u"""The OCID of the subnet where the VNIC attached to this instance will be created.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'create-vnic-details': {'module': 'core', 'class': 'CreateVnicDetails'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'extended-metadata': {'module': 'core', 'class': 'dict(str, object)'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'launch-options': {'module': 'core', 'class': 'LaunchOptions'}, 'instance-options': {'module': 'core', 'class': 'InstanceOptions'}, 'availability-config': {'module': 'core', 'class': 'LaunchInstanceAvailabilityConfigDetails'}, 'preemptible-instance-config': {'module': 'core', 'class': 'PreemptibleInstanceConfigDetails'}, 'metadata': {'module': 'core', 'class': 'dict(str, string)'}, 'agent-config': {'module': 'core', 'class': 'LaunchInstanceAgentConfigDetails'}, 'shape-config': {'module': 'core', 'class': 'LaunchInstanceShapeConfigDetails'}, 'source-details': {'module': 'core', 'class': 'InstanceSourceDetails'}, 'platform-config': {'module': 'core', 'class': 'LaunchInstancePlatformConfig'}, 'nsg-ids': {'module': 'core', 'class': 'list[string]'}}, output_type={'module': 'core', 'class': 'Instance'})
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

    if not (kwargs.get('source_details') or kwargs.get('image_id') or kwargs.get('source_boot_volume_id')):
        raise click.UsageError(
            'Must specify --source-details or --image-id or --source-boot-volume-id'
        )

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

    if 'assign_private_dns_record' in kwargs and kwargs['assign_private_dns_record'] is not None:
        create_vnic_details['assignPrivateDnsRecord'] = kwargs['assign_private_dns_record']

    if kwargs['hostname_label']:
        create_vnic_details['hostnameLabel'] = kwargs['hostname_label']

    if kwargs['private_ip']:
        create_vnic_details['privateIp'] = kwargs['private_ip']

    if kwargs['subnet_id']:
        create_vnic_details['subnetId'] = kwargs['subnet_id']

    if kwargs['nsg_ids']:
        create_vnic_details['nsg_ids'] = cli_util.parse_json_parameter("nsg_ids", kwargs['nsg_ids'])

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
    del kwargs['assign_private_dns_record']
    del kwargs['nsg_ids']

    # Remove the source_boot_volume_id and boot_volume_size_in_gbs parameters. image_id is an existing parameter so the underlying
    # CLI operation will accept it
    kwargs.pop('boot_volume_size_in_gbs', None)
    kwargs.pop('source_boot_volume_id', None)

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)

    ctx.invoke(compute_cli.launch_instance, **kwargs)


@compute_cli.instance_group.command(name='attach-vnic', help="""Creates a secondary VNIC and attaches it to the specified instance. You can specify either --subnet-id or --vlan-id for this create request, but not both. For more information about secondary VNICs, see [Virtual Network Interface Cards (VNICs)].""")
@cli_util.option('--instance-id', required=True, help="""The OCID of the instance.""")
@cli_util.option('--subnet-id', help="""The OCID of the subnet to create the VNIC in. You can specify either this parameter or --vlan-id, but not both.""")
@cli_util.option('--vlan-id', help="""The OCID of the VLAN to create the VNIC in. You can specify either this parameter or --subnet-id, but not both.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the [OCIDs] of the network security groups (NSGs) to add the VNIC to..""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vnic-display-name', help="""A user-friendly name for the VNIC. Does not have to be unique.""")
@cli_util.option('--assign-public-ip', type=click.BOOL, help="""Whether the VNIC should be assigned a public IP address. Defaults to whether the subnet is public or private. If not set and the VNIC is being created in a private subnet (i.e., where prohibitPublicIpOnVnic=true in the Subnet), then no public IP address is assigned. If not set and the subnet is public (prohibitPublicIpOnVnic=false), then a public IP address is assigned. If set to true and prohibitPublicIpOnVnic=true, an error is returned.""")
@cli_util.option('--skip-source-dest-check', type=click.BOOL, help="""Indicates whether Source/Destination check is disabled on the VNIC. Defaults to `false`, in which case we enable Source/Destination check on the VNIC.""")
@cli_util.option('--private-ip', help="""A private IP address of your choice to assign to the VNIC. Must be an available IP address within the subnet's CIDR. If no value is specified, a private IP address from the subnet will be automatically assigned.""")
@cli_util.option('--assign-private-dns-record', type=click.BOOL, help="""Whether the VNIC should be assigned a DNS record. If set to false, no DNS record registion for the VNIC; if set to true, DNS record will be registered. The default value is `true`.""")
@cli_util.option('--hostname-label', help="""The hostname for the VNIC. Used for DNS. The value is the hostname portion of the VNIC's fully qualified domain name (FQDN) (e.g., `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952](https://tools.ietf.org/html/rfc952) and [RFC 1123](https://tools.ietf.org/html/rfc1123). The value can be retrieved from the [Vnic](#/en/iaas/20160918/Vnic/).""")
@cli_util.option('--nic-index', type=click.INT, help="""Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use.""")
@cli_util.option('--wait', is_flag=True, default=False, help="""If set, then wait for the attachment to complete and return the newly attached VNIC. If not set, then the command will not wait and will return nothing on success.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'core', 'class': 'list[string]'}}, output_type={'module': 'core', 'class': 'Vnic'})
@cli_util.wrap_exceptions
def attach_vnic(ctx, from_json, instance_id, subnet_id, vlan_id, nsg_ids, vnic_display_name, assign_public_ip, private_ip, assign_private_dns_record, skip_source_dest_check, hostname_label, nic_index, wait, freeform_tags, defined_tags):
    kwargs = {}

    if subnet_id is None and vlan_id is None:
        raise click.UsageError('At least one of the options (--subnet-id or '
                               '--vlan-id) MUST be specified')

    if subnet_id is not None and vlan_id is not None:
        raise click.UsageError('This command accepts ONLY one option: EITHER '
                               '--subnet-id OR --vlan-id')

    vnic_details = {}
    vnic_details['displayName'] = vnic_display_name
    vnic_details['assignPublicIp'] = assign_public_ip
    vnic_details['privateIp'] = private_ip
    vnic_details['hostnameLabel'] = hostname_label

    if subnet_id is not None:
        vnic_details['subnetId'] = subnet_id

    if vlan_id is not None:
        vnic_details['vlanId'] = vlan_id

    if nsg_ids is not None:
        vnic_details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if freeform_tags is not None:
        vnic_details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        vnic_details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if skip_source_dest_check is not None:
        vnic_details['skipSourceDestCheck'] = skip_source_dest_check

    if assign_private_dns_record is not None:
        vnic_details['assignPrivateDnsRecord'] = assign_private_dns_record

    attachment_details = {}
    attachment_details['createVnicDetails'] = vnic_details
    attachment_details['instanceId'] = instance_id
    attachment_details['nicIndex'] = nic_index

    compute_client = cli_util.build_client('core', 'compute', ctx)
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

    network_client = cli_util.build_client('core', 'virtual_network', ctx)
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
    compute_client = cli_util.build_client('core', 'compute', ctx)
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
    client = cli_util.build_client('core', 'compute', ctx)
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


@cli_util.copy_params_from_generated_command(compute_cli.change_instance_compartment, params_to_exclude=['wait_for_state', 'max_wait_seconds', 'wait_interval_seconds'])
@compute_cli.instance_group.command(name='change-compartment', help=compute_cli.change_instance_compartment.help)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_instance_compartment(ctx, instance_id, compartment_id, if_match, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds):

    if isinstance(instance_id, six.string_types) and len(instance_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {'compartmentId': compartment_id}

    client = cli_util.build_client('core', 'compute', ctx)
    result = client.change_instance_compartment(
        instance_id=instance_id,
        change_instance_compartment_details=details,
        **kwargs
    )
    work_request_client = cli_util.build_client('core', 'work_request', ctx)
    if wait_for_state:
        if hasattr(work_request_client, 'get_work_request') and callable(getattr(work_request_client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)

                # There's an inconsistency in WorkRequest model returned by the service and API spec.
                # Service returns the WorkRequest state as Accepted, In_Progress, Failed, Succeeded(Case mis-match with Spec). We cannot directly compare wait_for_state and WorkRequest.status.
                # Defined a lambda function to perform the case-insensitive comparison.
                result = wait_until(work_request_client, work_request_client.get_work_request(result.headers['opc-work-request-id']), evaluate_response=lambda r: r.data.status and r.data.status.lower() == wait_for_state.lower(), **wait_period_kwargs)

            except MaximumWaitTimeExceeded as e:
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


# Change the required field compartment_id to be optional and make sure either compartment_id or instance_id is
# provided.
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--instance-id', help=u"""The OCID of the instance. If --compartment-id is not provided, then --instance-id must be provided.""")
@cli_util.copy_params_from_generated_command(compute_cli.list_volume_attachments, params_to_exclude=['compartment_id', 'instance_id'])
@compute_cli.volume_attachment_group.command(name=cli_util.override('compute.list_volume_attachments.command_name', 'list'), help=compute_cli.list_volume_attachments.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VolumeAttachment]'})
@cli_util.wrap_exceptions
def list_volume_attachments_extended(ctx, **kwargs):

    if not kwargs['compartment_id'] and not kwargs['instance_id']:
        raise click.UsageError('Either --compartment-id or --instance-id has to be provided')

    if not kwargs['compartment_id']:
        # Use instance_id to get compartment_id
        client = cli_util.build_client('core', 'compute', ctx)
        kwargs['compartment_id'] = client.get_instance(instance_id=kwargs['instance_id']).data.compartment_id
    ctx.invoke(compute_cli.list_volume_attachments, **kwargs)


# Change the following
# oci compute compute-global-image-capability-schema get
# oci compute compute-global-image-capability-schema list
# oci compute compute-global-image-capability-schema-version get
# oci compute compute-global-image-capability-schema-version list
# oci compute compute-image-capability-schema change-compartment
# oci compute compute-image-capability-schema create
# oci compute compute-image-capability-schema delete
# oci compute compute-image-capability-schema get
# oci compute compute-image-capability-schema list
# oci compute compute-image-capability-schema update
#
# With these:
# oci compute global-image-capability-schema get
# oci compute global-image-capability-schema list
# oci compute global-image-capability-schema-version get
# oci compute global-image-capability-schema-version list
# oci compute image-capability-schema change-compartment
# oci compute image-capability-schema create
# oci compute image-capability-schema delete
# oci compute image-capability-schema get
# oci compute image-capability-schema list
# oci compute image-capability-schema update
#
# Change Parameters:
# --compute-global-image-capability-schema-id
# --compute-global-image-capability-schema-version-name
# --compute-image-capability-schema-id
#
# With these:
# --global-image-capability-schema-id
# --global-image-capability-schema-version-name
# --image-capability-schema-id
compute_cli.compute_root_group.commands.pop(compute_cli.compute_global_image_capability_schema_group.name)
compute_cli.compute_root_group.commands.pop(compute_cli.compute_global_image_capability_schema_version_group.name)
compute_cli.compute_root_group.commands.pop(compute_cli.compute_image_capability_schema_group.name)


@click.command('global-image-capability-schema', cls=CommandGroupWithAlias, help="""Global Image Capability Schema""")
@cli_util.help_option_group
def global_image_capability_schema_group():
    pass


@click.command('global-image-capability-schema-version', cls=CommandGroupWithAlias, help="""Global Image Capability Schema Version""")
@cli_util.help_option_group
def global_image_capability_schema_version_group():
    pass


@click.command('image-capability-schema', cls=CommandGroupWithAlias, help="""Image Capability Schema""")
@cli_util.help_option_group
def image_capability_schema_group():
    pass


compute_cli.compute_root_group.add_command(global_image_capability_schema_group)
compute_cli.compute_root_group.add_command(global_image_capability_schema_version_group)
compute_cli.compute_root_group.add_command(image_capability_schema_group)


global_image_capability_schema_group.add_command(compute_cli.list_compute_global_image_capability_schemas)
image_capability_schema_group.add_command(compute_cli.list_compute_image_capability_schemas)


@cli_util.copy_params_from_generated_command(compute_cli.get_compute_global_image_capability_schema, params_to_exclude=['compute_global_image_capability_schema_id'])
@global_image_capability_schema_group.command(name='get', help=compute_cli.get_compute_global_image_capability_schema.help)
@cli_util.option('--global-image-capability-schema-id', required=True, help=u"""The [OCID] of the compute global image capability schema""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ComputeGlobalImageCapabilitySchema'})
@cli_util.wrap_exceptions
def get_global_image_capability_schema(ctx, **kwargs):
    if 'global_image_capability_schema_id' in kwargs:
        kwargs['compute_global_image_capability_schema_id'] = kwargs['global_image_capability_schema_id']
        kwargs.pop('global_image_capability_schema_id')
    ctx.invoke(compute_cli.get_compute_global_image_capability_schema, **kwargs)


@cli_util.copy_params_from_generated_command(compute_cli.list_compute_global_image_capability_schema_versions, params_to_exclude=['compute_global_image_capability_schema_id'])
@global_image_capability_schema_version_group.command(name='list',
                                                      help=compute_cli.list_compute_global_image_capability_schema_versions.help)
@cli_util.option('--global-image-capability-schema-id', required=True, help=u"""The [OCID] of the compute global image capability schema""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[ComputeGlobalImageCapabilitySchemaVersionSummary]'})
@cli_util.wrap_exceptions
def list_global_image_capability_schema_versions(ctx, **kwargs):
    if 'global_image_capability_schema_id' in kwargs:
        kwargs['compute_global_image_capability_schema_id'] = kwargs['global_image_capability_schema_id']
        kwargs.pop('global_image_capability_schema_id')
    ctx.invoke(compute_cli.list_compute_global_image_capability_schema_versions, **kwargs)


@cli_util.copy_params_from_generated_command(compute_cli.get_compute_global_image_capability_schema_version, params_to_exclude=['compute_global_image_capability_schema_id', 'compute_global_image_capability_schema_version_name'])
@global_image_capability_schema_version_group.command(name='get',
                                                      help=compute_cli.get_compute_global_image_capability_schema_version.help)
@cli_util.option('--global-image-capability-schema-id', required=True, help=u"""The [OCID] of the compute global image capability schema""")
@cli_util.option('--global-image-capability-schema-version-name', required=True, help=u"""The name of the compute global image capability schema version""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ComputeGlobalImageCapabilitySchemaVersion'})
@cli_util.wrap_exceptions
def get_global_image_capability_schema_version(ctx, **kwargs):
    if 'global_image_capability_schema_id' in kwargs:
        kwargs['compute_global_image_capability_schema_id'] = kwargs['global_image_capability_schema_id']
        kwargs.pop('global_image_capability_schema_id')
    if 'global_image_capability_schema_version_name' in kwargs:
        kwargs['compute_global_image_capability_schema_version_name'] = kwargs['global_image_capability_schema_version_name']
        kwargs.pop('global_image_capability_schema_version_name')
    ctx.invoke(compute_cli.get_compute_global_image_capability_schema_version, **kwargs)


@cli_util.copy_params_from_generated_command(compute_cli.change_compute_image_capability_schema_compartment,
                                             params_to_exclude=['compute_image_capability_schema_id'])
@image_capability_schema_group.command(name='change-compartment',
                                       help=compute_cli.change_compute_image_capability_schema_compartment.help)
@cli_util.option('--image-capability-schema-id', required=True, help=u"""The [OCID] of the compute image capability schema""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def change_image_capability_schema_compartment(ctx, **kwargs):
    if 'image_capability_schema_id' in kwargs:
        kwargs['compute_image_capability_schema_id'] = kwargs['image_capability_schema_id']
        kwargs.pop('image_capability_schema_id')
    ctx.invoke(compute_cli.change_compute_image_capability_schema_compartment, **kwargs)


@cli_util.copy_params_from_generated_command(compute_cli.create_compute_image_capability_schema,
                                             params_to_exclude=['compute_global_image_capability_schema_version_name'])
@image_capability_schema_group.command(name='create',
                                       help=compute_cli.create_compute_image_capability_schema.help)
@cli_util.option('--global-image-capability-schema-version-name', required=True, help=u"""The name of the compute global image capability schema version""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'schema-data': {'module': 'core', 'class': 'dict(str, ImageCapabilitySchemaDescriptor)'}}, output_type={'module': 'core', 'class': 'ComputeImageCapabilitySchema'})
@cli_util.wrap_exceptions
def create_image_capability_schema(ctx, **kwargs):
    if 'global_image_capability_schema_version_name' in kwargs:
        kwargs['compute_global_image_capability_schema_version_name'] = kwargs['global_image_capability_schema_version_name']
        kwargs.pop('global_image_capability_schema_version_name')
    ctx.invoke(compute_cli.create_compute_image_capability_schema, **kwargs)


@cli_util.copy_params_from_generated_command(compute_cli.delete_compute_image_capability_schema,
                                             params_to_exclude=['compute_image_capability_schema_id'])
@image_capability_schema_group.command(name='delete',
                                       help=compute_cli.delete_compute_image_capability_schema.help)
@cli_util.option('--image-capability-schema-id', required=True, help=u"""The [OCID] of the compute image capability schema""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def delete_image_capability_schema(ctx, **kwargs):
    if 'image_capability_schema_id' in kwargs:
        kwargs['compute_image_capability_schema_id'] = kwargs['image_capability_schema_id']
        kwargs.pop('image_capability_schema_id')
    ctx.invoke(compute_cli.delete_compute_image_capability_schema, **kwargs)


@cli_util.copy_params_from_generated_command(compute_cli.get_compute_image_capability_schema,
                                             params_to_exclude=['compute_image_capability_schema_id'])
@image_capability_schema_group.command(name='get',
                                       help=compute_cli.get_compute_image_capability_schema.help)
@cli_util.option('--image-capability-schema-id', required=True, help=u"""The [OCID] of the compute image capability schema""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ComputeImageCapabilitySchema'})
@cli_util.wrap_exceptions
def get_image_capability_schema(ctx, **kwargs):
    if 'image_capability_schema_id' in kwargs:
        kwargs['compute_image_capability_schema_id'] = kwargs['image_capability_schema_id']
        kwargs.pop('image_capability_schema_id')
    ctx.invoke(compute_cli.get_compute_image_capability_schema, **kwargs)


@cli_util.copy_params_from_generated_command(compute_cli.update_compute_image_capability_schema,
                                             params_to_exclude=['compute_image_capability_schema_id'])
@image_capability_schema_group.command(name='update',
                                       help=compute_cli.update_compute_image_capability_schema.help)
@cli_util.option('--image-capability-schema-id', required=True, help=u"""The [OCID] of the compute image capability schema""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'schema-data': {'module': 'core', 'class': 'dict(str, ImageCapabilitySchemaDescriptor)'}, 'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'core', 'class': 'ComputeImageCapabilitySchema'})
@cli_util.wrap_exceptions
def update_image_capability_schema(ctx, **kwargs):
    if 'image_capability_schema_id' in kwargs:
        kwargs['compute_image_capability_schema_id'] = kwargs['image_capability_schema_id']
        kwargs.pop('image_capability_schema_id')
    ctx.invoke(compute_cli.update_compute_image_capability_schema, **kwargs)


# Remove launch-instance-amd-milan-bm-launch-instance-platform-config from oci compute instance
compute_cli.instance_group.commands.pop(compute_cli.launch_instance_amd_milan_bm_launch_instance_platform_config.name)
