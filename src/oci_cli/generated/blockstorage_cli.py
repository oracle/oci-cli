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


@cli.command(cli_util.override('blockstorage_root_group.command_name', 'blockstorage'), cls=CommandGroupWithAlias, help=cli_util.override('blockstorage_root_group.help', """APIs for Networking Service, Compute Service, and Block Volume Service."""), short_help=cli_util.override('blockstorage_root_group.short_help', """Core Services API"""))
@cli_util.help_option_group
def blockstorage_root_group():
    pass


@click.command(cli_util.override('boot_volume_kms_key_group.command_name', 'boot-volume-kms-key'), cls=CommandGroupWithAlias, help="""Kms key id associated with this volume.""")
@cli_util.help_option_group
def boot_volume_kms_key_group():
    pass


@click.command(cli_util.override('volume_group.command_name', 'volume'), cls=CommandGroupWithAlias, help="""A detachable block volume device that allows you to dynamically expand the storage capacity of an instance. For more information, see [Overview of Cloud Volume Storage].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def volume_group():
    pass


@click.command(cli_util.override('boot_volume_backup_group.command_name', 'boot-volume-backup'), cls=CommandGroupWithAlias, help="""A point-in-time copy of a boot volume that can then be used to create a new boot volume or recover a boot volume. For more information, see [Overview of Boot Volume Backups] To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def boot_volume_backup_group():
    pass


@click.command(cli_util.override('boot_volume_group.command_name', 'boot-volume'), cls=CommandGroupWithAlias, help="""A detachable boot volume device that contains the image used to boot a Compute instance. For more information, see [Overview of Boot Volumes].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def boot_volume_group():
    pass


@click.command(cli_util.override('volume_backup_group.command_name', 'volume-backup'), cls=CommandGroupWithAlias, help="""A point-in-time copy of a volume that can then be used to create a new block volume or recover a block volume. For more information, see [Overview of Cloud Volume Storage].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def volume_backup_group():
    pass


@click.command(cli_util.override('volume_group_backup_group.command_name', 'volume-group-backup'), cls=CommandGroupWithAlias, help="""A point-in-time copy of a volume group that can then be used to create a new volume group or restore a volume group. For more information, see [Volume Groups].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def volume_group_backup_group():
    pass


@click.command(cli_util.override('volume_backup_policy_assignment_group.command_name', 'volume-backup-policy-assignment'), cls=CommandGroupWithAlias, help="""Specifies that a particular volume backup policy is assigned to an asset such as a volume.""")
@cli_util.help_option_group
def volume_backup_policy_assignment_group():
    pass


@click.command(cli_util.override('volume_group_group.command_name', 'volume-group'), cls=CommandGroupWithAlias, help="""Specifies a volume group which is a collection of volumes. For more information, see [Volume Groups].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def volume_group_group():
    pass


@click.command(cli_util.override('volume_backup_policy_group.command_name', 'volume-backup-policy'), cls=CommandGroupWithAlias, help="""A policy for automatically creating volume backups according to a recurring schedule. Has a set of one or more schedules that control when and how backups are created.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def volume_backup_policy_group():
    pass


@click.command(cli_util.override('volume_kms_key_group.command_name', 'volume-kms-key'), cls=CommandGroupWithAlias, help="""Kms key id associated with this volume.""")
@cli_util.help_option_group
def volume_kms_key_group():
    pass


blockstorage_root_group.add_command(boot_volume_kms_key_group)
blockstorage_root_group.add_command(volume_group)
blockstorage_root_group.add_command(boot_volume_backup_group)
blockstorage_root_group.add_command(boot_volume_group)
blockstorage_root_group.add_command(volume_backup_group)
blockstorage_root_group.add_command(volume_group_backup_group)
blockstorage_root_group.add_command(volume_backup_policy_assignment_group)
blockstorage_root_group.add_command(volume_group_group)
blockstorage_root_group.add_command(volume_backup_policy_group)
blockstorage_root_group.add_command(volume_kms_key_group)


@volume_backup_group.command(name=cli_util.override('copy_volume_backup.command_name', 'copy'), help="""Creates a volume backup copy in specified region. For general information about volume backups, see [Overview of Block Volume Service Backups]""")
@cli_util.option('--volume-backup-id', required=True, help="""The OCID of the volume backup.""")
@cli_util.option('--destination-region', required=True, help="""The name of the destination region.

Example: `us-ashburn-1`""")
@cli_util.option('--display-name', help="""A user-friendly name for the volume backup. Does not have to be unique and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeBackup'})
@cli_util.wrap_exceptions
def copy_volume_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_backup_id, destination_region, display_name):

    if isinstance(volume_backup_id, six.string_types) and len(volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-backup-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['destinationRegion'] = destination_region

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('blockstorage', ctx)
    result = client.copy_volume_backup(
        volume_backup_id=volume_backup_id,
        copy_volume_backup_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_volume_backup') and callable(getattr(client, 'get_volume_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_volume_backup(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@boot_volume_group.command(name=cli_util.override('create_boot_volume.command_name', 'create'), help="""Creates a new boot volume in the specified compartment from an existing boot volume or a boot volume backup. For general information about boot volumes, see [Boot Volumes]. You may optionally specify a *display name* for the volume, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--availability-domain', required=True, help="""The availability domain of the boot volume.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment that contains the boot volume.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""Specifies the boot volume source details for a new boot volume. The volume source is either another boot volume in the same availability domain or a boot volume backup. This is a mandatory field for a boot volume.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--backup-policy-id', help="""If provided, specifies the ID of the boot volume backup policy to assign to the newly created boot volume. If omitted, no policy will be assigned.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help="""The OCID of the KMS key to be used as the master encryption key for the boot volume.""")
@cli_util.option('--size-in-gbs', type=click.INT, help="""The size of the volume in GBs.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'BootVolumeSourceDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'BootVolumeSourceDetails'}}, output_type={'module': 'core', 'class': 'BootVolume'})
@cli_util.wrap_exceptions
def create_boot_volume(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, source_details, backup_policy_id, defined_tags, display_name, freeform_tags, kms_key_id, size_in_gbs):
    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['compartmentId'] = compartment_id
    details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if backup_policy_id is not None:
        details['backupPolicyId'] = backup_policy_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if kms_key_id is not None:
        details['kmsKeyId'] = kms_key_id

    if size_in_gbs is not None:
        details['sizeInGBs'] = size_in_gbs

    client = cli_util.build_client('blockstorage', ctx)
    result = client.create_boot_volume(
        create_boot_volume_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_boot_volume') and callable(getattr(client, 'get_boot_volume')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_boot_volume(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@boot_volume_backup_group.command(name=cli_util.override('create_boot_volume_backup.command_name', 'create'), help="""Creates a new boot volume backup of the specified boot volume. For general information about boot volume backups, see [Overview of Boot Volume Backups]

When the request is received, the backup object is in a REQUEST_RECEIVED state. When the data is imaged, it goes into a CREATING state. After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.""")
@cli_util.option('--boot-volume-id', required=True, help="""The OCID of the boot volume that needs to be backed up.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name for the boot volume backup. Does not have to be unique and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["FULL", "INCREMENTAL"]), help="""The type of backup to create. If omitted, defaults to incremental.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'BootVolumeBackup'})
@cli_util.wrap_exceptions
def create_boot_volume_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, boot_volume_id, defined_tags, display_name, freeform_tags, type):
    kwargs = {}

    details = {}
    details['bootVolumeId'] = boot_volume_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if type is not None:
        details['type'] = type

    client = cli_util.build_client('blockstorage', ctx)
    result = client.create_boot_volume_backup(
        create_boot_volume_backup_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_boot_volume_backup') and callable(getattr(client, 'get_boot_volume_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_boot_volume_backup(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('create_volume.command_name', 'create'), help="""Creates a new volume in the specified compartment. Volumes can be created in sizes ranging from 50 GB (51200 MB) to 32 TB (33554432 MB), in 1 GB (1024 MB) increments. By default, volumes are 1 TB (1048576 MB). For general information about block volumes, see [Overview of Block Volume Service].

A volume and instance can be in separate compartments but must be in the same availability domain. For information about access control and compartments, see [Overview of the IAM Service]. For information about availability domains, see [Regions and Availability Domains]. To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

You may optionally specify a *display name* for the volume, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--availability-domain', required=True, help="""The availability domain of the volume.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment that contains the volume.""")
@cli_util.option('--backup-policy-id', help="""If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help="""The OCID of the KMS key to be used as the master encryption key for the volume.""")
@cli_util.option('--size-in-gbs', type=click.INT, help="""The size of the volume in GBs.""")
@cli_util.option('--size-in-mbs', type=click.INT, help="""The size of the volume in MBs. The value must be a multiple of 1024. This field is deprecated. Use sizeInGBs instead.""")
@cli_util.option('--source-details', type=custom_types.CLI_COMPLEX_TYPE, help="""Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--volume-backup-id', help="""The OCID of the volume backup from which the data should be restored on the newly created volume. This field is deprecated. Use the sourceDetails field instead to specify the backup for the volume.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'VolumeSourceDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'VolumeSourceDetails'}}, output_type={'module': 'core', 'class': 'Volume'})
@cli_util.wrap_exceptions
def create_volume(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, backup_policy_id, defined_tags, display_name, freeform_tags, kms_key_id, size_in_gbs, size_in_mbs, source_details, volume_backup_id):
    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['compartmentId'] = compartment_id

    if backup_policy_id is not None:
        details['backupPolicyId'] = backup_policy_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if kms_key_id is not None:
        details['kmsKeyId'] = kms_key_id

    if size_in_gbs is not None:
        details['sizeInGBs'] = size_in_gbs

    if size_in_mbs is not None:
        details['sizeInMBs'] = size_in_mbs

    if source_details is not None:
        details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if volume_backup_id is not None:
        details['volumeBackupId'] = volume_backup_id

    client = cli_util.build_client('blockstorage', ctx)
    result = client.create_volume(
        create_volume_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_volume') and callable(getattr(client, 'get_volume')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_volume(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_backup_group.command(name=cli_util.override('create_volume_backup.command_name', 'create'), help="""Creates a new backup of the specified volume. For general information about volume backups, see [Overview of Block Volume Service Backups]

When the request is received, the backup object is in a REQUEST_RECEIVED state. When the data is imaged, it goes into a CREATING state. After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.""")
@cli_util.option('--volume-id', required=True, help="""The OCID of the volume that needs to be backed up.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name for the volume backup. Does not have to be unique and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["FULL", "INCREMENTAL"]), help="""The type of backup to create. If omitted, defaults to INCREMENTAL.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'VolumeBackup'})
@cli_util.wrap_exceptions
def create_volume_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_id, defined_tags, display_name, freeform_tags, type):
    kwargs = {}

    details = {}
    details['volumeId'] = volume_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if type is not None:
        details['type'] = type

    client = cli_util.build_client('blockstorage', ctx)
    result = client.create_volume_backup(
        create_volume_backup_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_volume_backup') and callable(getattr(client, 'get_volume_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_volume_backup(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_backup_policy_assignment_group.command(name=cli_util.override('create_volume_backup_policy_assignment.command_name', 'create'), help="""Assigns a policy to the specified asset, such as a volume. Note that a given asset can only have one policy assigned to it; if this method is called for an asset that previously has a different policy assigned, the prior assignment will be silently deleted.""")
@cli_util.option('--asset-id', required=True, help="""The OCID of the asset (e.g. a volume) to which to assign the policy.""")
@cli_util.option('--policy-id', required=True, help="""The OCID of the volume backup policy to assign to an asset.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeBackupPolicyAssignment'})
@cli_util.wrap_exceptions
def create_volume_backup_policy_assignment(ctx, from_json, asset_id, policy_id):
    kwargs = {}

    details = {}
    details['assetId'] = asset_id
    details['policyId'] = policy_id

    client = cli_util.build_client('blockstorage', ctx)
    result = client.create_volume_backup_policy_assignment(
        create_volume_backup_policy_assignment_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group_group.command(name=cli_util.override('create_volume_group.command_name', 'create'), help="""Creates a new volume group in the specified compartment. A volume group is a collection of volumes and may be created from a list of volumes, cloning an existing volume group, or by restoring a volume group backup. A volume group can contain up to 64 volumes. You may optionally specify a *display name* for the volume group, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information.

For more information, see [Volume Groups].""")
@cli_util.option('--availability-domain', required=True, help="""The availability domain of the volume group.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment that contains the volume group.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""Specifies the volume group source details for a new volume group. The volume source is either another a list of volume ids in the same availability domain, another volume group or a volume group backup.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name for the volume group. Does not have to be unique, and it's changeable.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'VolumeGroupSourceDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'source-details': {'module': 'core', 'class': 'VolumeGroupSourceDetails'}}, output_type={'module': 'core', 'class': 'VolumeGroup'})
@cli_util.wrap_exceptions
def create_volume_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, source_details, defined_tags, display_name, freeform_tags):
    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['compartmentId'] = compartment_id
    details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('blockstorage', ctx)
    result = client.create_volume_group(
        create_volume_group_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_volume_group') and callable(getattr(client, 'get_volume_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_volume_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_group_backup_group.command(name=cli_util.override('create_volume_group_backup.command_name', 'create'), help="""Creates a new backup volume group of the specified volume group. For more information, see [Volume Groups].""")
@cli_util.option('--volume-group-id', required=True, help="""The OCID of the volume group that needs to be backed up.""")
@cli_util.option('--compartment-id', help="""The OCID of the compartment that will contain the volume group backup. This parameter is optional, by default backup will be created in the same compartment and source volume group.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name for the volume group backup. Does not have to be unique and it's changeable.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["FULL", "INCREMENTAL"]), help="""The type of backup to create. If omitted, defaults to incremental.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "COMMITTED", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'VolumeGroupBackup'})
@cli_util.wrap_exceptions
def create_volume_group_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_group_id, compartment_id, defined_tags, display_name, freeform_tags, type):
    kwargs = {}

    details = {}
    details['volumeGroupId'] = volume_group_id

    if compartment_id is not None:
        details['compartmentId'] = compartment_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if type is not None:
        details['type'] = type

    client = cli_util.build_client('blockstorage', ctx)
    result = client.create_volume_group_backup(
        create_volume_group_backup_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_volume_group_backup') and callable(getattr(client, 'get_volume_group_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_volume_group_backup(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@boot_volume_group.command(name=cli_util.override('delete_boot_volume.command_name', 'delete'), help="""Deletes the specified boot volume. The volume cannot have an active connection to an instance. To disconnect the boot volume from a connected instance, see [Disconnecting From a Boot Volume]. **Warning:** All data on the boot volume will be permanently lost when the boot volume is deleted.""")
@cli_util.option('--boot-volume-id', required=True, help="""The OCID of the boot volume.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_boot_volume(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, boot_volume_id, if_match):

    if isinstance(boot_volume_id, six.string_types) and len(boot_volume_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('blockstorage', ctx)
    result = client.delete_boot_volume(
        boot_volume_id=boot_volume_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_boot_volume') and callable(getattr(client, 'get_boot_volume')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_boot_volume(boot_volume_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@boot_volume_backup_group.command(name=cli_util.override('delete_boot_volume_backup.command_name', 'delete'), help="""Deletes a boot volume backup.""")
@cli_util.option('--boot-volume-backup-id', required=True, help="""The OCID of the boot volume backup.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_boot_volume_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, boot_volume_backup_id, if_match):

    if isinstance(boot_volume_backup_id, six.string_types) and len(boot_volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-backup-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('blockstorage', ctx)
    result = client.delete_boot_volume_backup(
        boot_volume_backup_id=boot_volume_backup_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_boot_volume_backup') and callable(getattr(client, 'get_boot_volume_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_boot_volume_backup(boot_volume_backup_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@boot_volume_kms_key_group.command(name=cli_util.override('delete_boot_volume_kms_key.command_name', 'delete'), help="""Remove kms for the specific boot volume. If the volume doesn't use KMS, then do nothing.""")
@cli_util.option('--boot-volume-id', required=True, help="""The OCID of the boot volume.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_boot_volume_kms_key(ctx, from_json, boot_volume_id, if_match):

    if isinstance(boot_volume_id, six.string_types) and len(boot_volume_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('blockstorage', ctx)
    result = client.delete_boot_volume_kms_key(
        boot_volume_id=boot_volume_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('delete_volume.command_name', 'delete'), help="""Deletes the specified volume. The volume cannot have an active connection to an instance. To disconnect the volume from a connected instance, see [Disconnecting From a Volume]. **Warning:** All data on the volume will be permanently lost when the volume is deleted.""")
@cli_util.option('--volume-id', required=True, help="""The OCID of the volume.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_volume(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_id, if_match):

    if isinstance(volume_id, six.string_types) and len(volume_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('blockstorage', ctx)
    result = client.delete_volume(
        volume_id=volume_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_volume') and callable(getattr(client, 'get_volume')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_volume(volume_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@volume_backup_group.command(name=cli_util.override('delete_volume_backup.command_name', 'delete'), help="""Deletes a volume backup.""")
@cli_util.option('--volume-backup-id', required=True, help="""The OCID of the volume backup.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_volume_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_backup_id, if_match):

    if isinstance(volume_backup_id, six.string_types) and len(volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-backup-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('blockstorage', ctx)
    result = client.delete_volume_backup(
        volume_backup_id=volume_backup_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_volume_backup') and callable(getattr(client, 'get_volume_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_volume_backup(volume_backup_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@volume_backup_policy_assignment_group.command(name=cli_util.override('delete_volume_backup_policy_assignment.command_name', 'delete'), help="""Deletes a volume backup policy assignment (i.e. unassigns the policy from an asset).""")
@cli_util.option('--policy-assignment-id', required=True, help="""The OCID of the volume backup policy assignment.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_volume_backup_policy_assignment(ctx, from_json, policy_assignment_id, if_match):

    if isinstance(policy_assignment_id, six.string_types) and len(policy_assignment_id.strip()) == 0:
        raise click.UsageError('Parameter --policy-assignment-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('blockstorage', ctx)
    result = client.delete_volume_backup_policy_assignment(
        policy_assignment_id=policy_assignment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group_group.command(name=cli_util.override('delete_volume_group.command_name', 'delete'), help="""Deletes the specified volume group. Individual volumes are not deleted, only the volume group is deleted. For more information, see [Volume Groups].""")
@cli_util.option('--volume-group-id', required=True, help="""The Oracle Cloud ID (OCID) that uniquely identifies the volume group.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_volume_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_group_id, if_match):

    if isinstance(volume_group_id, six.string_types) and len(volume_group_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-group-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('blockstorage', ctx)
    result = client.delete_volume_group(
        volume_group_id=volume_group_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_volume_group') and callable(getattr(client, 'get_volume_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_volume_group(volume_group_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@volume_group_backup_group.command(name=cli_util.override('delete_volume_group_backup.command_name', 'delete'), help="""Deletes a volume group backup. This operation deletes all the backups in the volume group. For more information, see [Volume Groups].""")
@cli_util.option('--volume-group-backup-id', required=True, help="""The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "COMMITTED", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_volume_group_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_group_backup_id, if_match):

    if isinstance(volume_group_backup_id, six.string_types) and len(volume_group_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-group-backup-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('blockstorage', ctx)
    result = client.delete_volume_group_backup(
        volume_group_backup_id=volume_group_backup_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_volume_group_backup') and callable(getattr(client, 'get_volume_group_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_volume_group_backup(volume_group_backup_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@volume_kms_key_group.command(name=cli_util.override('delete_volume_kms_key.command_name', 'delete'), help="""Remove kms for the specific volume. If the volume doesn't use KMS, then do nothing.""")
@cli_util.option('--volume-id', required=True, help="""The OCID of the volume.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_volume_kms_key(ctx, from_json, volume_id, if_match):

    if isinstance(volume_id, six.string_types) and len(volume_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('blockstorage', ctx)
    result = client.delete_volume_kms_key(
        volume_id=volume_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@boot_volume_group.command(name=cli_util.override('get_boot_volume.command_name', 'get'), help="""Gets information for the specified boot volume.""")
@cli_util.option('--boot-volume-id', required=True, help="""The OCID of the boot volume.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'BootVolume'})
@cli_util.wrap_exceptions
def get_boot_volume(ctx, from_json, boot_volume_id):

    if isinstance(boot_volume_id, six.string_types) and len(boot_volume_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('blockstorage', ctx)
    result = client.get_boot_volume(
        boot_volume_id=boot_volume_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@boot_volume_backup_group.command(name=cli_util.override('get_boot_volume_backup.command_name', 'get'), help="""Gets information for the specified boot volume backup.""")
@cli_util.option('--boot-volume-backup-id', required=True, help="""The OCID of the boot volume backup.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'BootVolumeBackup'})
@cli_util.wrap_exceptions
def get_boot_volume_backup(ctx, from_json, boot_volume_backup_id):

    if isinstance(boot_volume_backup_id, six.string_types) and len(boot_volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-backup-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('blockstorage', ctx)
    result = client.get_boot_volume_backup(
        boot_volume_backup_id=boot_volume_backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@boot_volume_kms_key_group.command(name=cli_util.override('get_boot_volume_kms_key.command_name', 'get'), help="""Gets kms key id for the specified boot volume.""")
@cli_util.option('--boot-volume-id', required=True, help="""The OCID of the boot volume.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'BootVolumeKmsKey'})
@cli_util.wrap_exceptions
def get_boot_volume_kms_key(ctx, from_json, boot_volume_id, if_match):

    if isinstance(boot_volume_id, six.string_types) and len(boot_volume_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('blockstorage', ctx)
    result = client.get_boot_volume_kms_key(
        boot_volume_id=boot_volume_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('get_volume.command_name', 'get'), help="""Gets information for the specified volume.""")
@cli_util.option('--volume-id', required=True, help="""The OCID of the volume.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Volume'})
@cli_util.wrap_exceptions
def get_volume(ctx, from_json, volume_id):

    if isinstance(volume_id, six.string_types) and len(volume_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('blockstorage', ctx)
    result = client.get_volume(
        volume_id=volume_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_group.command(name=cli_util.override('get_volume_backup.command_name', 'get'), help="""Gets information for the specified volume backup.""")
@cli_util.option('--volume-backup-id', required=True, help="""The OCID of the volume backup.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeBackup'})
@cli_util.wrap_exceptions
def get_volume_backup(ctx, from_json, volume_backup_id):

    if isinstance(volume_backup_id, six.string_types) and len(volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-backup-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('blockstorage', ctx)
    result = client.get_volume_backup(
        volume_backup_id=volume_backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_policy_group.command(name=cli_util.override('get_volume_backup_policy.command_name', 'get'), help="""Gets information for the specified volume backup policy.""")
@cli_util.option('--policy-id', required=True, help="""The OCID of the volume backup policy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeBackupPolicy'})
@cli_util.wrap_exceptions
def get_volume_backup_policy(ctx, from_json, policy_id):

    if isinstance(policy_id, six.string_types) and len(policy_id.strip()) == 0:
        raise click.UsageError('Parameter --policy-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('blockstorage', ctx)
    result = client.get_volume_backup_policy(
        policy_id=policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_policy_assignment_group.command(name=cli_util.override('get_volume_backup_policy_asset_assignment.command_name', 'get-volume-backup-policy-asset-assignment'), help="""Gets the volume backup policy assignment for the specified asset. Note that the assetId query parameter is required, and that the returned list will contain at most one item (since any given asset can only have one policy assigned to it).""")
@cli_util.option('--asset-id', required=True, help="""The OCID of an asset (e.g. a volume).""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VolumeBackupPolicyAssignment]'})
@cli_util.wrap_exceptions
def get_volume_backup_policy_asset_assignment(ctx, from_json, asset_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('blockstorage', ctx)
    result = client.get_volume_backup_policy_asset_assignment(
        asset_id=asset_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_policy_assignment_group.command(name=cli_util.override('get_volume_backup_policy_assignment.command_name', 'get'), help="""Gets information for the specified volume backup policy assignment.""")
@cli_util.option('--policy-assignment-id', required=True, help="""The OCID of the volume backup policy assignment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeBackupPolicyAssignment'})
@cli_util.wrap_exceptions
def get_volume_backup_policy_assignment(ctx, from_json, policy_assignment_id):

    if isinstance(policy_assignment_id, six.string_types) and len(policy_assignment_id.strip()) == 0:
        raise click.UsageError('Parameter --policy-assignment-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('blockstorage', ctx)
    result = client.get_volume_backup_policy_assignment(
        policy_assignment_id=policy_assignment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group_group.command(name=cli_util.override('get_volume_group.command_name', 'get'), help="""Gets information for the specified volume group. For more information, see [Volume Groups].""")
@cli_util.option('--volume-group-id', required=True, help="""The Oracle Cloud ID (OCID) that uniquely identifies the volume group.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeGroup'})
@cli_util.wrap_exceptions
def get_volume_group(ctx, from_json, volume_group_id):

    if isinstance(volume_group_id, six.string_types) and len(volume_group_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-group-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('blockstorage', ctx)
    result = client.get_volume_group(
        volume_group_id=volume_group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group_backup_group.command(name=cli_util.override('get_volume_group_backup.command_name', 'get'), help="""Gets information for the specified volume group backup. For more information, see [Volume Groups].""")
@cli_util.option('--volume-group-backup-id', required=True, help="""The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeGroupBackup'})
@cli_util.wrap_exceptions
def get_volume_group_backup(ctx, from_json, volume_group_backup_id):

    if isinstance(volume_group_backup_id, six.string_types) and len(volume_group_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-group-backup-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('blockstorage', ctx)
    result = client.get_volume_group_backup(
        volume_group_backup_id=volume_group_backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_kms_key_group.command(name=cli_util.override('get_volume_kms_key.command_name', 'get'), help="""Gets kms key id for the specified volume.""")
@cli_util.option('--volume-id', required=True, help="""The OCID of the volume.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeKmsKey'})
@cli_util.wrap_exceptions
def get_volume_kms_key(ctx, from_json, volume_id, if_match):

    if isinstance(volume_id, six.string_types) and len(volume_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('blockstorage', ctx)
    result = client.get_volume_kms_key(
        volume_id=volume_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@boot_volume_backup_group.command(name=cli_util.override('list_boot_volume_backups.command_name', 'list'), help="""Lists the boot volume backups in the specified compartment. You can filter the results by boot volume.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--boot-volume-id', help="""The OCID of the boot volume.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[BootVolumeBackup]'})
@cli_util.wrap_exceptions
def list_boot_volume_backups(ctx, from_json, all_pages, page_size, compartment_id, boot_volume_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if boot_volume_id is not None:
        kwargs['boot_volume_id'] = boot_volume_id
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
    client = cli_util.build_client('blockstorage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_boot_volume_backups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_boot_volume_backups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_boot_volume_backups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@boot_volume_group.command(name=cli_util.override('list_boot_volumes.command_name', 'list'), help="""Lists the boot volumes in the specified compartment and availability domain.""")
@cli_util.option('--availability-domain', required=True, help="""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--volume-group-id', help="""The OCID of the volume group.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[BootVolume]'})
@cli_util.wrap_exceptions
def list_boot_volumes(ctx, from_json, all_pages, page_size, availability_domain, compartment_id, limit, page, volume_group_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if volume_group_id is not None:
        kwargs['volume_group_id'] = volume_group_id
    client = cli_util.build_client('blockstorage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_boot_volumes,
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_boot_volumes,
            limit,
            page_size,
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_boot_volumes(
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@volume_backup_policy_group.command(name=cli_util.override('list_volume_backup_policies.command_name', 'list'), help="""Lists all volume backup policies available to the caller.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VolumeBackupPolicy]'})
@cli_util.wrap_exceptions
def list_volume_backup_policies(ctx, from_json, all_pages, page_size, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('blockstorage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_volume_backup_policies,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_volume_backup_policies,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_volume_backup_policies(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@volume_backup_group.command(name=cli_util.override('list_volume_backups.command_name', 'list'), help="""Lists the volume backups in the specified compartment. You can filter the results by volume.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--volume-id', help="""The OCID of the volume.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--source-volume-backup-id', help="""A filter to return only resources that originated from the given source volume backup.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VolumeBackup]'})
@cli_util.wrap_exceptions
def list_volume_backups(ctx, from_json, all_pages, page_size, compartment_id, volume_id, limit, page, display_name, source_volume_backup_id, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if volume_id is not None:
        kwargs['volume_id'] = volume_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if source_volume_backup_id is not None:
        kwargs['source_volume_backup_id'] = source_volume_backup_id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('blockstorage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_volume_backups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_volume_backups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_volume_backups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@volume_group_backup_group.command(name=cli_util.override('list_volume_group_backups.command_name', 'list'), help="""Lists the volume group backups in the specified compartment. You can filter the results by volume group. For more information, see [Volume Groups].""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--volume-group-id', help="""The OCID of the volume group.""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VolumeGroupBackup]'})
@cli_util.wrap_exceptions
def list_volume_group_backups(ctx, from_json, all_pages, page_size, compartment_id, volume_group_id, limit, page, display_name, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if volume_group_id is not None:
        kwargs['volume_group_id'] = volume_group_id
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
    client = cli_util.build_client('blockstorage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_volume_group_backups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_volume_group_backups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_volume_group_backups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@volume_group_group.command(name=cli_util.override('list_volume_groups.command_name', 'list'), help="""Lists the volume groups in the specified compartment and availability domain. For more information, see [Volume Groups].""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--availability-domain', help="""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VolumeGroup]'})
@cli_util.wrap_exceptions
def list_volume_groups(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, limit, page, display_name, sort_by, sort_order, lifecycle_state):

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
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('blockstorage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_volume_groups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_volume_groups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_volume_groups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('list_volumes.command_name', 'list'), help="""Lists the volumes in the specified compartment and availability domain.""")
@cli_util.option('--compartment-id', required=True, help="""The OCID of the compartment.""")
@cli_util.option('--availability-domain', help="""The name of the availability domain.

Example: `Uocm:PHX-AD-1`""")
@cli_util.option('--limit', type=click.INT, help="""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help="""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--volume-group-id', help="""The OCID of the volume group.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Volume]'})
@cli_util.wrap_exceptions
def list_volumes(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, limit, page, display_name, sort_by, sort_order, volume_group_id, lifecycle_state):

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
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if volume_group_id is not None:
        kwargs['volume_group_id'] = volume_group_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('blockstorage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_volumes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_volumes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_volumes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@boot_volume_group.command(name=cli_util.override('update_boot_volume.command_name', 'update'), help="""Updates the specified boot volume's display name, defined tags, and free-form tags.""")
@cli_util.option('--boot-volume-id', required=True, help="""The OCID of the boot volume.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--size-in-gbs', type=click.INT, help="""The size to resize the volume to in GBs. Has to be larger than the current size.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'BootVolume'})
@cli_util.wrap_exceptions
def update_boot_volume(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, boot_volume_id, defined_tags, display_name, freeform_tags, size_in_gbs, if_match):

    if isinstance(boot_volume_id, six.string_types) and len(boot_volume_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-id cannot be whitespace or empty string')
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

    if size_in_gbs is not None:
        details['sizeInGBs'] = size_in_gbs

    client = cli_util.build_client('blockstorage', ctx)
    result = client.update_boot_volume(
        boot_volume_id=boot_volume_id,
        update_boot_volume_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_boot_volume') and callable(getattr(client, 'get_boot_volume')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_boot_volume(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@boot_volume_backup_group.command(name=cli_util.override('update_boot_volume_backup.command_name', 'update'), help="""Updates the display name for the specified boot volume backup. Avoid entering confidential information.""")
@cli_util.option('--boot-volume-backup-id', required=True, help="""The OCID of the boot volume backup.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A friendly user-specified name for the boot volume backup. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'BootVolumeBackup'})
@cli_util.wrap_exceptions
def update_boot_volume_backup(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, boot_volume_backup_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(boot_volume_backup_id, six.string_types) and len(boot_volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-backup-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('blockstorage', ctx)
    result = client.update_boot_volume_backup(
        boot_volume_backup_id=boot_volume_backup_id,
        update_boot_volume_backup_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_boot_volume_backup') and callable(getattr(client, 'get_boot_volume_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_boot_volume_backup(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@boot_volume_kms_key_group.command(name=cli_util.override('update_boot_volume_kms_key.command_name', 'update'), help="""Update kms key id for the specific volume.""")
@cli_util.option('--boot-volume-id', required=True, help="""The OCID of the boot volume.""")
@cli_util.option('--kms-key-id', help="""The new kms key which will be used to protect the specific volume. This key has to be a valid kms key ocid, and user must have key delegation policy to allow them to access this key. Even if this new kms key is the same as the previous kms key id, block storage service will use it to regenerate a new volume encryption key. Example: `{\"kmsKeyId\": \"ocid1.key.region1.sea.afnl2n7daag4s.abzwkljs6uevhlgcznhmh7oiatyrxngrywc3tje3uk3g77hzmewqiieuk75f\"}`""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'BootVolumeKmsKey'})
@cli_util.wrap_exceptions
def update_boot_volume_kms_key(ctx, from_json, boot_volume_id, kms_key_id, if_match):

    if isinstance(boot_volume_id, six.string_types) and len(boot_volume_id.strip()) == 0:
        raise click.UsageError('Parameter --boot-volume-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if kms_key_id is not None:
        details['kmsKeyId'] = kms_key_id

    client = cli_util.build_client('blockstorage', ctx)
    result = client.update_boot_volume_kms_key(
        boot_volume_id=boot_volume_id,
        update_boot_volume_kms_key_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('update_volume.command_name', 'update'), help="""Updates the specified volume's display name. Avoid entering confidential information.""")
@cli_util.option('--volume-id', required=True, help="""The OCID of the volume.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--size-in-gbs', type=click.INT, help="""The size to resize the volume to in GBs. Has to be larger than the current size.""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'Volume'})
@cli_util.wrap_exceptions
def update_volume(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_id, defined_tags, display_name, freeform_tags, size_in_gbs, if_match):

    if isinstance(volume_id, six.string_types) and len(volume_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-id cannot be whitespace or empty string')
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

    if size_in_gbs is not None:
        details['sizeInGBs'] = size_in_gbs

    client = cli_util.build_client('blockstorage', ctx)
    result = client.update_volume(
        volume_id=volume_id,
        update_volume_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_volume') and callable(getattr(client, 'get_volume')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_volume(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_backup_group.command(name=cli_util.override('update_volume_backup.command_name', 'update'), help="""Updates the display name for the specified volume backup. Avoid entering confidential information.""")
@cli_util.option('--volume-backup-id', required=True, help="""The OCID of the volume backup.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A friendly user-specified name for the volume backup. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'VolumeBackup'})
@cli_util.wrap_exceptions
def update_volume_backup(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_backup_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(volume_backup_id, six.string_types) and len(volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-backup-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('blockstorage', ctx)
    result = client.update_volume_backup(
        volume_backup_id=volume_backup_id,
        update_volume_backup_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_volume_backup') and callable(getattr(client, 'get_volume_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_volume_backup(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_group_group.command(name=cli_util.override('update_volume_group.command_name', 'update'), help="""Updates the set of volumes in a volume group along with the display name. Use this operation to add or remove volumes in a volume group. Specify the full list of volume IDs to include in the volume group. If the volume ID is not specified in the call, it will be removed from the volume group. Avoid entering confidential information.

For more information, see [Volume Groups].""")
@cli_util.option('--volume-group-id', required=True, help="""The Oracle Cloud ID (OCID) that uniquely identifies the volume group.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A user-friendly name for the volume group.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--volume-ids', type=custom_types.CLI_COMPLEX_TYPE, help="""OCIDs for the volumes in this volume group.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'volume-ids': {'module': 'core', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'volume-ids': {'module': 'core', 'class': 'list[string]'}}, output_type={'module': 'core', 'class': 'VolumeGroup'})
@cli_util.wrap_exceptions
def update_volume_group(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_group_id, defined_tags, display_name, freeform_tags, volume_ids, if_match):

    if isinstance(volume_group_id, six.string_types) and len(volume_group_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-group-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or volume_ids:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and volume-ids will replace any existing values. Are you sure you want to continue?"):
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

    if volume_ids is not None:
        details['volumeIds'] = cli_util.parse_json_parameter("volume_ids", volume_ids)

    client = cli_util.build_client('blockstorage', ctx)
    result = client.update_volume_group(
        volume_group_id=volume_group_id,
        update_volume_group_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_volume_group') and callable(getattr(client, 'get_volume_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_volume_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_group_backup_group.command(name=cli_util.override('update_volume_group_backup.command_name', 'update'), help="""Updates the display name for the specified volume group backup. For more information, see [Volume Groups].""")
@cli_util.option('--volume-group-backup-id', required=True, help="""The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help="""A friendly user-specified name for the volume group backup.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help="""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "COMMITTED", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'VolumeGroupBackup'})
@cli_util.wrap_exceptions
def update_volume_group_backup(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, volume_group_backup_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(volume_group_backup_id, six.string_types) and len(volume_group_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-group-backup-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('blockstorage', ctx)
    result = client.update_volume_group_backup(
        volume_group_backup_id=volume_group_backup_id,
        update_volume_group_backup_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_volume_group_backup') and callable(getattr(client, 'get_volume_group_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_volume_group_backup(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@volume_kms_key_group.command(name=cli_util.override('update_volume_kms_key.command_name', 'update'), help="""Update kms key id for the specific volume.""")
@cli_util.option('--volume-id', required=True, help="""The OCID of the volume.""")
@cli_util.option('--kms-key-id', help="""The new kms key which will be used to protect the specific volume. This key has to be a valid kms key ocid, and user must have key delegation policy to allow them to access this key. Even if this new kms key is the same as the previous kms key id, block storage service will use it to regenerate a new volume encryption key. Example: `{\"kmsKeyId\": \"ocid1.key.region1.sea.afnl2n7daag4s.abzwkljs6uevhlgcznhmh7oiatyrxngrywc3tje3uk3g77hzmewqiieuk75f\"}`""")
@cli_util.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeKmsKey'})
@cli_util.wrap_exceptions
def update_volume_kms_key(ctx, from_json, volume_id, kms_key_id, if_match):

    if isinstance(volume_id, six.string_types) and len(volume_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if kms_key_id is not None:
        details['kmsKeyId'] = kms_key_id

    client = cli_util.build_client('blockstorage', ctx)
    result = client.update_volume_kms_key(
        volume_id=volume_id,
        update_volume_kms_key_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
